"""
Agents API - Direct access to AI agent system
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import logging

# Import agent system
try:
    # from services.agents.orchestrator import CareerGuidanceOrchestrator  # OLD SYSTEM DISABLED
    AGENT_SYSTEM_AVAILABLE = True
except ImportError:
    AGENT_SYSTEM_AVAILABLE = False
    CareerGuidanceOrchestrator = None

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agents", tags=["agents"])


class AgentAnalysisRequest(BaseModel):
    skills: str
    expertise: str
    use_memory: bool = True
    use_web_search: bool = True


class AgentStatusResponse(BaseModel):
    available: bool
    message: str


class AgentAnalysisResponse(BaseModel):
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    source: str  # "agents" or "fallback"


@router.get("/status", response_model=AgentStatusResponse)
async def get_agent_status():
    """Check if the agent system is available and functional"""
    if not AGENT_SYSTEM_AVAILABLE:
        return AgentStatusResponse(
            available=False,
            message="Agent system is not available. Missing dependencies or configuration."
        )
    
    try:
        # Try to initialize orchestrator
        orchestrator = CareerGuidanceOrchestrator()
        return AgentStatusResponse(
            available=True,
            message="Agent system is available and ready."
        )
    except Exception as e:
        return AgentStatusResponse(
            available=False,
            message=f"Agent system initialization failed: {str(e)}"
        )


@router.post("/analyze", response_model=AgentAnalysisResponse)
async def analyze_with_agents(request: AgentAnalysisRequest):
    """
    Perform career analysis using the AI agent system
    This endpoint provides direct access to agent capabilities
    """
    if not AGENT_SYSTEM_AVAILABLE:
        return AgentAnalysisResponse(
            success=False,
            error="Agent system is not available",
            source="error"
        )
    
    try:
        # Initialize orchestrator
        orchestrator = CareerGuidanceOrchestrator()
        
        # Run agent analysis
        result = await orchestrator.analyze_career(
            skills=request.skills,
            expertise=request.expertise,
            use_memory=request.use_memory,
            use_web_search=request.use_web_search
        )
        
        if result:
            return AgentAnalysisResponse(
                success=True,
                data=result,
                source="agents"
            )
        else:
            return AgentAnalysisResponse(
                success=False,
                error="Agent analysis returned empty results",
                source="agents"
            )
            
    except Exception as e:
        logger.error(f"Agent analysis error: {str(e)}", exc_info=True)
        return AgentAnalysisResponse(
            success=False,
            error=f"Agent analysis failed: {str(e)}",
            source="error"
        )


@router.post("/detailed", response_model=Dict[str, Any])
async def get_detailed_agent_analysis(request: AgentAnalysisRequest):
    """
    Get detailed agent analysis with full agent output (not converted to legacy format)
    """
    if not AGENT_SYSTEM_AVAILABLE:
        raise HTTPException(
            status_code=503,
            detail="Agent system is not available"
        )
    
    try:
        orchestrator = CareerGuidanceOrchestrator()
        
        result = await orchestrator.get_detailed_analysis(
            skills=request.skills,
            expertise=request.expertise
        )
        
        if result:
            return {
                "success": True,
                "analysis": result.dict(),
                "source": "agents"
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Detailed agent analysis failed"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Detailed agent analysis error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Detailed agent analysis failed: {str(e)}"
        )