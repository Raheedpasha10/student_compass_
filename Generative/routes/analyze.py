from fastapi import APIRouter, HTTPException, Depends
from models.schemas import AnalyzeRequest, AnalyzeResponse, CareerPath, RoadmapStep, Course, Certification, User
from services.ai_service import AIService
from dependencies import get_current_user
from typing import Optional
import logging

# Try to import agent orchestrator (optional - will fallback if not available)
try:
    # from services.agents.orchestrator import CareerGuidanceOrchestrator  # OLD SYSTEM DISABLED
    # Only enable agents when explicitly enabled AND a valid API key is present
    import os
    AGENT_SYSTEM_AVAILABLE = (
        os.getenv("ENABLE_AGENT_SYSTEM", "false").lower() == "true"
        and bool(os.getenv("GOOGLE_GENAI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
    )
except ImportError as e:
    AGENT_SYSTEM_AVAILABLE = False
    CareerGuidanceOrchestrator = None

logger = logging.getLogger(__name__)

router = APIRouter(tags=["analyze"])

# Expose a module-level AI service instance for tests and reuse
ai_service = AIService()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_career_paths(
    request: AnalyzeRequest,
    current_user: Optional[User] = Depends(get_current_user)
):
    """
    Analyze skills and expertise to generate career paths, roadmap, and courses.
    Uses advanced AI agent system if available, automatically falls back to standard AI service.
    Can be used with or without authentication.

    Args:
        request: Analyze request with skills and expertise
        current_user: Optional authenticated user
    """
    try:
        # Use skills and expertise from request or user profile
        skills = request.skills or (current_user.skills if current_user else "")
        expertise = request.expertise or (current_user.expertise if current_user else "")

        if not skills or not expertise:
            raise HTTPException(
                status_code=400,
                detail="Skills and expertise are required. Please provide them in the request or update your profile."
            )

        user_id = str(current_user.id) if current_user else None

        # Try agent-based analysis first (automatically falls back if agents are unavailable)
        analysis = None
        if AGENT_SYSTEM_AVAILABLE:
            try:
                logger.info("Attempting agent-based career analysis")
                orchestrator = CareerGuidanceOrchestrator()
                analysis = await orchestrator.analyze_career(
                    skills=skills,
                    expertise=expertise,
                    user_id=user_id,
                    use_agents=True
                )

                if analysis and analysis.get("career_paths"):
                    logger.info("Agent-based analysis completed successfully")
                else:
                    logger.warning("Agent-based analysis returned empty results, falling back to standard AI service")
                    analysis = None

            except Exception as agent_error:
                logger.warning(f"Agent-based analysis failed: {str(agent_error)}, falling back to standard AI service")
                analysis = None
        else:
            logger.info("Agent system not available, using standard AI service")

        # Fallback to standard AI service if agents failed or disabled
        if not analysis:
            logger.info("Using standard AI service for career analysis")
            analysis = ai_service.generate_career_analysis(skills, expertise)

        # Validate analysis structure
        if not analysis or not isinstance(analysis, dict):
            raise HTTPException(
                status_code=500,
                detail="Invalid analysis result from AI service"
            )

        # Convert to Pydantic models with error handling
        try:
            career_paths = [CareerPath(**path) for path in analysis.get("career_paths", [])]
            selected_path = CareerPath(**analysis.get("selected_path", {}))
            # Normalize roadmap items to RoadmapStep schema
            normalized_roadmap = []
            for step in analysis.get("roadmap", []):
                if isinstance(step, dict) and "phase" in step:
                    # Map alternative format -> RoadmapStep
                    normalized_roadmap.append({
                        "step": len(normalized_roadmap) + 1,
                        "title": step.get("phase", ""),
                        "description": ", ".join(step.get("topics", [])) if step.get("topics") else (step.get("description", "") or ""),
                        "duration": step.get("duration", ""),
                        "resources": step.get("resources", [])
                    })
                else:
                    normalized_roadmap.append(step)
            roadmap = [RoadmapStep(**step) for step in normalized_roadmap]
            # Normalize courses to ensure required fields exist
            normalized_courses = []
            for c in analysis.get("courses", []):
                if isinstance(c, dict):
                    c = {
                        **c,
                        "difficulty": c.get("difficulty") or c.get("level") or "Beginner",
                        "duration": c.get("duration") or "Self-paced",
                        "url": c.get("url") or c.get("link") or "",
                    }
                normalized_courses.append(c)
            courses = [Course(**course) for course in normalized_courses]
            # Normalize certifications to ensure required fields exist
            normalized_certifications = []
            for cert in analysis.get("certifications", []):
                if isinstance(cert, dict):
                    cert = {
                        **cert,
                        "duration": cert.get("duration") or "Varies",
                        "description": cert.get("description") or "Professional certification",
                        "difficulty": cert.get("difficulty") or "Intermediate",
                        "url": cert.get("url") or f"https://www.google.com/search?q={cert.get('name', '').replace(' ', '+')}+certification"
                    }
                normalized_certifications.append(cert)
            certifications = [Certification(**cert) for cert in normalized_certifications]
        except Exception as validation_error:
            logger.error(f"Error validating analysis results: {str(validation_error)}")
            raise HTTPException(
                status_code=500,
                detail=f"Error processing analysis results: {str(validation_error)}"
            )

        # Ensure all certifications have proper URLs
        for cert in certifications:
            if not cert.url or cert.url == "":
                # Provide a default search URL if no specific URL is provided
                cert.url = f"https://www.google.com/search?q={cert.name.replace(' ', '+')}+certification+{cert.provider.replace(' ', '+')}"

        return AnalyzeResponse(
            career_paths=career_paths,
            selected_path=selected_path,
            roadmap=roadmap,
            courses=courses,
            certifications=certifications
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Unexpected error in career analysis: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error analyzing career paths: {str(e)}")
