"""
Agent service module for multi-agent career guidance system

This module provides a sophisticated multi-agent system for career guidance using:
- Google ADK (Agent Development Kit) if available
- Fallback to direct Gemini API calls if ADK is not available

The system uses a sequential agent pattern (funneling) with specialized agents:
1. Skill Analyzer Agent - Analyzes user skills and identifies gaps
2. Career Matcher Agent - Matches skills to suitable career paths
3. Roadmap Generator Agent - Creates personalized learning roadmaps
4. Resource Curator Agent - Curates learning resources
"""
try:
    from .agent_service import AgentService
    from .orchestrator import CareerGuidanceOrchestrator
    __all__ = ["AgentService", "CareerGuidanceOrchestrator"]
except ImportError as e:
    import logging
    logger = logging.getLogger(__name__)
    logger.warning(f"Failed to import agent services: {e}")
    __all__ = []

