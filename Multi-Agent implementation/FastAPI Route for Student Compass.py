"""
FastAPI Route for Multi-Agent Funneling System
Add this to your routes/ directory
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import asyncio
from datetime import datetime

# Import your new service
from services.multi_agent_service import MultiAgentFunnelService

router = APIRouter(prefix="/api/v2", tags=["Multi-Agent Roadmap"])


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


class RoadmapStatusResponse(BaseModel):
    task_id: str
    status: str
    result: Optional[RoadmapResponse] = None


# In-memory task storage (use Redis in production)
task_storage: Dict[str, Any] = {}


@router.post("/roadmap/generate", response_model=RoadmapResponse)
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
        # Initialize the multi-agent service
        service = MultiAgentFunnelService()
        
        # Convert background to dict if provided
        background_dict = None
        if request.background:
            background_dict = request.background.model_dump(exclude_none=True)
        
        # Generate roadmap using multi-agent system
        result = await service.generate_funneled_roadmap(
            user_query=request.query,
            user_background=background_dict
        )
        
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
            timestamp=datetime.utcnow().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate roadmap: {str(e)}"
        )


@router.post("/roadmap/generate-async", response_model=RoadmapStatusResponse)
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


@router.get("/roadmap/status/{task_id}", response_model=RoadmapStatusResponse)
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
        service = MultiAgentFunnelService()
        
        background_dict = None
        if request.background:
            background_dict = request.background.model_dump(exclude_none=True)
        
        result = await service.generate_funneled_roadmap(
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


@router.get("/roadmap/health")
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
    
    all_configured = all(config_status.values())
    
    return {
        "status": "healthy" if all_configured else "partial",
        "multi_agent_enabled": all_configured,
        "configurations": config_status,
        "message": "Multi-agent system ready" if all_configured else "Some API keys missing"
    }


# Integration with existing /analyze endpoint
@router.post("/analyze/enhanced")
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
                "data science", "excel", "tableau", "aws", "docker"]
    
    roadmap_lower = roadmap.lower()
    for keyword in keywords:
        if keyword in roadmap_lower:
            skills.append(keyword.title())
    
    return list(set(skills))
