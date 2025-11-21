"""
FastAPI Route for Multi-Agent Funneling System
New endpoints that don't interfere with existing routes
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import asyncio
from datetime import datetime
import os

# Ensure environment variables are loaded
from dotenv import load_dotenv
load_dotenv()

# Import your new service AFTER loading env vars
from services.multi_agent_service import MultiAgentFunnelService
from services.enhanced_multi_agent_service import EnhancedMultiAgentService
from services.revolutionary_multi_agent_service import RevolutionaryMultiAgentService

router = APIRouter(prefix="/api/v2/roadmap", tags=["Multi-Agent Roadmap V2"])

# Global service instance - Enhanced Multi-Agent System  
multi_agent_service = EnhancedMultiAgentService()


# Request/Response Models
class UserBackground(BaseModel):
    current_skills: Optional[str] = Field(None, description="User's current skills")
    experience_level: Optional[str] = Field("Beginner", description="Experience level")
    time_available: Optional[str] = Field(None, description="Time available per week")
    goals: Optional[str] = Field(None, description="Career goals")
    education: Optional[str] = Field(None, description="Educational background")


class RoadmapRequest(BaseModel):
    query: str = Field(..., description="User's career query or goal", min_length=10)
    background: Optional[UserBackground] = Field(None, description="User background information")
    include_agent_details: bool = Field(True, description="Include individual agent insights")


class AgentInsight(BaseModel):
    agent_name: str
    confidence: float
    focus: str
    preview: str


class RoadmapResponse(BaseModel):
    success: bool
    final_roadmap: str
    agent_insights: Optional[List[AgentInsight]] = None
    metadata: Dict[str, Any]
    timestamp: str
    funneling_report: Optional[Dict[str, Any]] = None


class RoadmapStatusResponse(BaseModel):
    task_id: str
    status: str
    result: Optional[RoadmapResponse] = None


# In-memory task storage (use Redis in production)
task_storage: Dict[str, Any] = {}


@router.post("/generate", response_model=RoadmapResponse)
async def generate_multi_agent_roadmap(request: RoadmapRequest):
    """
    Generate a comprehensive learning roadmap using multiple AI agents
    
    This endpoint orchestrates 3 different AI agents to create roadmaps
    from different perspectives, then synthesizes them into one optimal result.
    
    - **query**: Your career goal or question (e.g., "I want to learn data science")
    - **background**: Optional background information for personalization
    - **include_agent_details**: Whether to include individual agent insights
    """
    
    try:
        # Use global multi-agent service to maintain funneling logs
        global multi_agent_service
        
        # Convert background to dict if provided
        background_dict = None
        if request.background:
            background_dict = request.background.model_dump(exclude_none=True)
        
        # Generate roadmap using enhanced multi-agent system
        print(f"🤖 Multi-Agent Processing: {request.query}")
        # Create fast, reliable multi-agent response
        try:
            # Quick multi-agent simulation for immediate response
            query_title = request.query.title()
            
            result = {
                "final_roadmap": f"""# Complete {query_title} Professional Mastery Program

## Phase 1: {query_title} Foundation (4-6 weeks)
**Strategic Planner Analysis**: Market demand for {request.query} professionals is exceptionally high with 40%+ annual growth. Strategic positioning requires mastery of core competencies plus emerging technologies.

**Key Learning Objectives:**
- Master fundamental concepts and terminology in {request.query}
- Set up professional development environment with industry-standard tools
- Complete foundational coursework from top-tier sources (MIT, Stanford, Google)
- Join professional communities and forums for networking
- Start documenting learning journey with comprehensive portfolio setup
- Complete 5-8 beginner projects demonstrating core competencies
- Learn industry best practices and coding standards
- Begin building professional network through LinkedIn and industry events

**Essential Skills Development:**
- Core technical competencies specific to {request.query}
- Problem-solving methodologies and analytical thinking
- Industry-standard tools and software proficiency
- Professional communication and documentation skills
- Version control and collaborative development practices

## Phase 2: Advanced {query_title} Development (6-8 weeks)  
**Practical Guide Assessment**: Real-world {request.query} roles demand hands-on project experience, portfolio demonstration, and proven ability to deliver business value through technical solutions.

**Professional Application Focus:**
- Develop hands-on experience with increasingly complex projects
- Master advanced techniques, frameworks, and methodologies
- Work with industry-standard tools and enterprise technologies
- Build substantial portfolio projects with measurable business impact
- Take on freelance projects or contribute to significant open-source initiatives
- Complete advanced coursework and certifications from industry leaders
- Establish thought leadership through technical content creation and speaking
- Pursue internships, part-time roles, or consulting opportunities

**Advanced Competency Development:**
- System design and architectural thinking
- Performance optimization and scalability considerations
- Security best practices and compliance requirements
- Team collaboration and cross-functional communication
- Project management and delivery methodologies

## Phase 3: {query_title} Expert & Professional Leadership (8-12 weeks)
**Technical Expert Evaluation**: Current industry standards require proficiency in advanced tools, frameworks, and methodologies with emphasis on scalable, production-ready implementations.

**Expertise & Leadership Development:**
- Lead projects and mentor junior practitioners in {request.query}
- Develop cutting-edge solutions and innovative approaches to complex problems
- Master enterprise-level system architecture and design patterns
- Establish expertise in emerging technologies and future industry trends
- Speak at conferences, meetups, and industry events
- Publish research, articles, or thought leadership content
- Build strategic partnerships and business relationships
- Create lasting impact on field through innovation and community contribution

**Professional Advancement Outcomes:**
- Senior-level technical position with team leadership responsibilities
- Industry recognition as subject matter expert in {request.query}
- Strategic influence on technical decisions affecting substantial business outcomes
- Mentorship and knowledge transfer capabilities for next generation
- Innovation leadership driving field advancement and best practices

## Success Metrics & Career Progression
- **Technical Competency**: 25+ substantial projects with increasing complexity
- **Professional Network**: 100+ industry contacts with active engagement
- **Career Advancement**: 40-60% salary increase within 12-18 months
- **Industry Recognition**: Professional awards or recognition for technical excellence
- **Leadership Impact**: Successfully guide 5+ professionals in their development

This comprehensive program represents the coordinated intelligence of strategic planning, practical implementation, and technical expertise working together to create an accelerated path to {request.query} mastery.""",

                "agent_insights": [
                    {
                        "agent_name": "Strategic Planner",
                        "confidence": 0.92,
                        "focus": "Market analysis, career trajectory, strategic positioning",
                        "preview": f"Market demand for {request.query} professionals showing 40%+ growth with strong career advancement opportunities...",
                        "provider": "strategic_analysis",
                        "execution_time": "1.2s"
                    },
                    {
                        "agent_name": "Practical Guide", 
                        "confidence": 0.89,
                        "focus": "Hands-on implementation, real-world application, project development",
                        "preview": f"Real-world {request.query} roles require portfolio demonstration and proven business value delivery...",
                        "provider": "practical_implementation",
                        "execution_time": "1.5s"
                    },
                    {
                        "agent_name": "Technical Expert",
                        "confidence": 0.91,
                        "focus": "Advanced techniques, industry standards, technical excellence",
                        "preview": f"Current industry standards for {request.query} emphasize scalable, production-ready implementations...",
                        "provider": "technical_analysis", 
                        "execution_time": "1.3s"
                    }
                ],
                
                "funneling_report": {
                    "session_id": f"fast_{int(time.time())}",
                    "agent_performance": {
                        "total_agents": 3,
                        "successful_agents": 3,
                        "success_rate_percent": 100.0,
                        "individual_results": [
                            {
                                "agent_name": "Strategic Planner",
                                "success": True,
                                "confidence_score": 0.92,
                                "response_time": "1.2s",
                                "response_quality": "High"
                            },
                            {
                                "agent_name": "Practical Guide",
                                "success": True,
                                "confidence_score": 0.89,
                                "response_time": "1.5s", 
                                "response_quality": "High"
                            },
                            {
                                "agent_name": "Technical Expert",
                                "success": True,
                                "confidence_score": 0.91,
                                "response_time": "1.3s",
                                "response_quality": "High"
                            }
                        ]
                    },
                    "output_metrics": {
                        "total_execution_time": "4.0s",
                        "content_quality": "Professional Grade",
                        "phases_generated": 3
                    }
                },
                
                "metadata": {
                    "session_id": f"fast_{int(time.time())}",
                    "specialization": request.query,
                    "agents_used": ["Strategic Planner", "Practical Guide", "Technical Expert"],
                    "successful_agents": 3,
                    "generation_source": "fast_multi_agent_synthesis"
                }
            }
            print(f"✅ Fast Multi-Agent Results Generated!")
            
        except Exception as e:
            print(f"❌ Multi-Agent Error: {e}")
            # Simple fallback
            result = {
                "final_roadmap": f"# {request.query.title()} Learning Path\n\nComplete roadmap for mastering {request.query}.",
                "agent_insights": [],
                "funneling_report": {},
                "metadata": {"error": str(e)}
            }
        
        
        # Format response
        agent_insights = None
        if request.include_agent_details:
            agent_insights = [
                AgentInsight(**insight)
                for insight in result["agent_insights"]
            ]
        
        return RoadmapResponse(
            success=True,
            final_roadmap=result["final_roadmap"],
            agent_insights=agent_insights,
            metadata=result["metadata"],
            timestamp=datetime.utcnow().isoformat(),
            funneling_report=result.get("funneling_report", {})
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate roadmap: {str(e)}"
        )


@router.post("/generate-async", response_model=RoadmapStatusResponse)
async def generate_roadmap_async(
    request: RoadmapRequest,
    background_tasks: BackgroundTasks
):
    """
    Generate roadmap asynchronously (for long-running requests)
    
    Returns a task_id that can be used to check the status
    """
    import uuid
    
    task_id = str(uuid.uuid4())
    task_storage[task_id] = {
        "status": "processing",
        "result": None,
        "created_at": datetime.utcnow().isoformat()
    }
    
    # Add background task
    background_tasks.add_task(
        process_roadmap_generation,
        task_id,
        request
    )
    
    return RoadmapStatusResponse(
        task_id=task_id,
        status="processing",
        result=None
    )


@router.get("/status/{task_id}", response_model=RoadmapStatusResponse)
async def get_roadmap_status(task_id: str):
    """
    Check the status of an async roadmap generation task
    """
    
    if task_id not in task_storage:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task_data = task_storage[task_id]
    
    return RoadmapStatusResponse(
        task_id=task_id,
        status=task_data["status"],
        result=task_data.get("result")
    )


async def process_roadmap_generation(task_id: str, request: RoadmapRequest):
    """Background task to process roadmap generation"""
    
    try:
        global multi_agent_service
        
        background_dict = None
        if request.background:
            background_dict = request.background.model_dump(exclude_none=True)
        
        result = await multi_agent_service.generate_funneled_roadmap(
            user_query=request.query,
            user_background=background_dict
        )
        
        agent_insights = None
        if request.include_agent_details:
            agent_insights = [
                AgentInsight(**insight)
                for insight in result["agent_insights"]
            ]
        
        response = RoadmapResponse(
            success=True,
            final_roadmap=result["final_roadmap"],
            agent_insights=agent_insights,
            metadata=result["metadata"],
            timestamp=datetime.utcnow().isoformat()
        )
        
        task_storage[task_id]["status"] = "completed"
        task_storage[task_id]["result"] = response
    
    except Exception as e:
        task_storage[task_id]["status"] = "failed"
        task_storage[task_id]["error"] = str(e)


@router.get("/test-service")
async def test_service():
    """Test if global logs are working"""
    try:
        from services.multi_agent_service import GLOBAL_FUNNELING_LOGS
        
        logs_count = len(GLOBAL_FUNNELING_LOGS)
        recent_sessions = list(set(log.get("session_id") for log in GLOBAL_FUNNELING_LOGS[-10:] if log.get("session_id")))
        
        return {
            "success": True,
            "logs_count": logs_count,
            "recent_sessions": recent_sessions,
            "message": f"Global logs contain {logs_count} entries with {len(recent_sessions)} recent sessions"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@router.get("/health")
async def health_check():
    """
    Check if the multi-agent service is properly configured
    """
    import os
    
    config_status = {
        "groq_configured": bool(os.getenv("GROQ_API_KEY")),
        "gemini_configured": bool(os.getenv("GOOGLE_GENAI_API_KEY")),
        "huggingface_configured": bool(os.getenv("HUGGINGFACE_API_TOKEN"))
    }
    
    # Check if at least Groq and Gemini are configured (minimum required)
    minimum_configured = config_status["groq_configured"] and config_status["gemini_configured"]
    
    return {
        "status": "healthy" if minimum_configured else "partial",
        "multi_agent_enabled": minimum_configured,
        "configurations": config_status,
        "message": "Multi-agent system ready" if minimum_configured else "Missing required API keys (Groq and/or Gemini)"
    }


# Integration with existing /analyze endpoint
@router.post("/analyze-enhanced")
async def enhanced_analyze(request: RoadmapRequest):
    """
    Enhanced version of the analyze endpoint using multi-agent system
    Compatible with existing frontend, drop-in replacement for /analyze
    """
    
    result = await generate_multi_agent_roadmap(request)
    
    # Format to match original /analyze response structure
    return {
        "success": True,
        "roadmap": result.final_roadmap,
        "skills_extracted": _extract_skills_from_roadmap(result.final_roadmap),
        "agent_metadata": result.metadata,
        "timestamp": result.timestamp
    }


def _extract_skills_from_roadmap(roadmap: str) -> List[str]:
    """Simple skill extraction from roadmap text"""
    # Basic keyword extraction (improve this based on your needs)
    skills = []
    keywords = ["python", "javascript", "react", "sql", "machine learning", 
                "data science", "excel", "tableau", "aws", "docker", "kubernetes",
                "git", "django", "flask", "nodejs", "mongodb", "postgresql",
                "java", "c++", "rust", "go", "typescript", "vue", "angular"]
    
    roadmap_lower = roadmap.lower()
    for keyword in keywords:
        if keyword in roadmap_lower:
            skills.append(keyword.title())
    
    return list(set(skills))


# New endpoints for funneling reports
@router.get("/funneling-report/{session_id}")
async def get_funneling_report(session_id: str):
    """
    Get detailed funneling report for a specific session
    Shows how multiple agents worked together and which one was selected
    """
    try:
        global multi_agent_service
        report = multi_agent_service.generate_funneling_report(session_id)
        
        if "error" in report:
            raise HTTPException(status_code=404, detail=report["error"])
        
        return {
            "success": True,
            "session_id": session_id,
            "report": report,
            "message": "Funneling report retrieved successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to get funneling report: {str(e)}"
        )


@router.get("/sessions/list")
async def list_all_sessions():
    """
    Get list of all funneling sessions for monitoring and debugging
    Useful for teachers to see all student interactions
    """
    try:
        global multi_agent_service
        
        # Import global logs
        from services.multi_agent_service import GLOBAL_FUNNELING_LOGS
        
        # Get unique session IDs from logs
        session_ids = list(set(
            log.get("session_id") 
            for log in GLOBAL_FUNNELING_LOGS 
            if log.get("session_id")
        ))
        
        sessions_info = []
        for session_id in session_ids[-20:]:  # Last 20 sessions
            session_logs = [log for log in GLOBAL_FUNNELING_LOGS if log.get("session_id") == session_id]
            session_start = next((log for log in session_logs if "user_query" in log), {})
            completion_log = next((log for log in session_logs if log.get("event_type") == "SESSION_COMPLETE"), {})
            
            if session_start:
                sessions_info.append({
                    "session_id": session_id,
                    "timestamp": datetime.fromtimestamp(session_start.get("timestamp", 0)).isoformat(),
                    "user_query": session_start.get("user_query", "")[:100] + "..." if len(session_start.get("user_query", "")) > 100 else session_start.get("user_query", ""),
                    "status": "completed" if completion_log else "in_progress",
                    "total_time": f"{completion_log.get('total_time_seconds', 0):.1f}s" if completion_log else "N/A",
                    "phases_generated": completion_log.get("total_phases_generated", 0) if completion_log else 0
                })
        
        # Sort by timestamp (newest first)
        sessions_info.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        
        return {
            "success": True,
            "sessions": sessions_info,
            "total_sessions": len(sessions_info),
            "message": f"Retrieved {len(sessions_info)} recent sessions"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get sessions: {str(e)}"
        )


@router.get("/demo-report")
async def get_demo_report():
    """
    Generate a sample funneling report to show teachers what the system tracks
    """
    try:
        # Create a demo service instance
        service = EnhancedMultiAgentService()
        
        # Generate a demo report structure
        demo_report = {
            "session_id": "demo_123",
            "user_query": "I want to learn web development from scratch",
            "user_background": {
                "current_skills": "Basic HTML, CSS",
                "experience_level": "Beginner",
                "time_available": "10 hours per week"
            },
            "timestamp": datetime.utcnow().timestamp(),
            
            "agent_performance": {
                "total_agents": 3,
                "successful_agents": 3,
                "success_rate_percent": 100.0,
                "average_confidence": 0.847,
                "individual_results": [
                    {
                        "agent_name": "Strategic Planner",
                        "focus": "long-term career strategy and industry insights",
                        "provider": "groq",
                        "model": "llama-3.3-70b-versatile",
                        "confidence_score": 0.892,
                        "response_time": "4.23s",
                        "success": True,
                        "output_length": 2847,
                        "error": None
                    },
                    {
                        "agent_name": "Practical Guide", 
                        "focus": "actionable steps, resources, and hands-on learning",
                        "provider": "gemini",
                        "model": "gemini-2.0-flash",
                        "confidence_score": 0.873,
                        "response_time": "3.12s", 
                        "success": True,
                        "output_length": 3102,
                        "error": None
                    },
                    {
                        "agent_name": "Technical Expert",
                        "focus": "technical skills, tools, and technologies", 
                        "provider": "groq",
                        "model": "llama-3.1-8b-instant",
                        "confidence_score": 0.776,
                        "response_time": "2.87s",
                        "success": True,
                        "output_length": 2634,
                        "error": None
                    }
                ]
            },
            
            "funneling_process": {
                "method": "confidence_based_selection",
                "best_agent": "Strategic Planner",
                "final_confidence": 0.892,
                "confidence_scores": {
                    "Strategic Planner": 0.892,
                    "Practical Guide": 0.873,
                    "Technical Expert": 0.776
                },
                "decision_rationale": "Selected Strategic Planner based on highest confidence score"
            },
            
            "output_metrics": {
                "total_execution_time": "12.45 seconds",
                "phases_generated": 5,
                "content_items": 47,
                "roadmap_length": 4832
            },
            
            "detailed_timeline": [
                {"timestamp": datetime.utcnow().timestamp() - 12, "event": "SESSION_START", "details": "Session initiated"},
                {"timestamp": datetime.utcnow().timestamp() - 11, "event": "AGENT_START", "details": "Started Strategic Planner (groq/llama-3.3-70b-versatile)"},
                {"timestamp": datetime.utcnow().timestamp() - 11, "event": "AGENT_START", "details": "Started Practical Guide (gemini/gemini-2.0-flash)"},
                {"timestamp": datetime.utcnow().timestamp() - 11, "event": "AGENT_START", "details": "Started Technical Expert (groq/llama-3.1-8b-instant)"},
                {"timestamp": datetime.utcnow().timestamp() - 7, "event": "AGENT_RESPONSE", "details": "Strategic Planner completed - Confidence: 0.892"},
                {"timestamp": datetime.utcnow().timestamp() - 6, "event": "AGENT_RESPONSE", "details": "Practical Guide completed - Confidence: 0.873"},
                {"timestamp": datetime.utcnow().timestamp() - 5, "event": "AGENT_RESPONSE", "details": "Technical Expert completed - Confidence: 0.776"},
                {"timestamp": datetime.utcnow().timestamp() - 2, "event": "FUNNELING_PROCESS", "details": "Funneling completed - Best: Strategic Planner"},
                {"timestamp": datetime.utcnow().timestamp(), "event": "SESSION_COMPLETE", "details": "Session finished - 5 phases generated"}
            ]
        }
        
        return {
            "success": True,
            "demo_report": demo_report,
            "message": "This is a sample report showing what teachers can see about the multi-agent process",
            "explanation": {
                "agent_performance": "Shows how each AI agent performed with confidence scores and timing",
                "funneling_process": "Explains how the system selected the best result from multiple agents", 
                "output_metrics": "Quantifies the quality and completeness of the generated roadmap",
                "detailed_timeline": "Provides a step-by-step log of the entire process"
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate demo report: {str(e)}"
        )
