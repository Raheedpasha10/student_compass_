"""
Career Guidance Orchestrator - High-level interface for agent-based career analysis
"""
import logging
from typing import Dict, Any, Optional
from .agent_service import AgentService
from .schemas import AgentAnalysisResult
from .memory import memory

logger = logging.getLogger(__name__)


class CareerGuidanceOrchestrator:
    """
    High-level orchestrator that manages the agent-based career guidance system.
    Provides a simple interface and handles errors gracefully with fallbacks.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the orchestrator

        Args:
            api_key: Google Gemini API key (optional)
        """
        self.agent_service = None
        self.api_key = api_key
        self._initialized = False

    def _ensure_initialized(self):
        """Ensure the agent service is initialized"""
        if not self._initialized:
            try:
                self.agent_service = AgentService(api_key=self.api_key)
                self._initialized = True
                logger.info("CareerGuidanceOrchestrator initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize AgentService: {e}")
                self._initialized = False
                raise

    async def analyze_career(
        self,
        skills: str,
        expertise: str,
        user_id: Optional[str] = None,
        use_agents: bool = True,
        use_memory: bool = True,
        use_web_search: bool = True
    ) -> Dict[str, Any]:
        """
        Analyze career paths using the agent system

        Args:
            skills: User's skills description
            expertise: User's expertise level description
            user_id: Optional user ID for session management
            use_agents: Whether to use agent system (True) or fallback (False)
            use_memory: Whether to use memory for context (default: True)
            use_web_search: Whether to use web search for resources (default: True)

        Returns:
            Dictionary containing career analysis in legacy format
        """
        if not use_agents:
            logger.info("Agent system disabled, returning empty result for fallback")
            return None

        try:
            self._ensure_initialized()

            # Get user context from memory if available
            user_context = ""
            if use_memory and user_id:
                try:
                    user_context = memory.get_context_for_agent(user_id)
                    if user_context and user_context != "No previous context available.":
                        logger.info(f"Loaded context for user {user_id}")
                except Exception as e:
                    logger.warning(f"Failed to load user context: {e}")

            # Enhance skills/expertise with context if available
            enhanced_skills = skills
            enhanced_expertise = expertise
            if user_context and user_context != "No previous context available.":
                enhanced_skills = f"{skills}\n\nPrevious Context:\n{user_context}"

            # Run agent-based analysis
            agent_results = await self.agent_service.analyze_career_with_agents(
                skills=enhanced_skills,
                expertise=enhanced_expertise,
                user_id=user_id,
                use_web_search=use_web_search
            )

            # Convert to legacy format for API compatibility
            legacy_format = self.agent_service.convert_agent_results_to_legacy_format(agent_results)

            # Save conversation to memory
            if use_memory and user_id:
                try:
                    memory.save_conversation(
                        user_id=user_id,
                        skills=skills,
                        expertise=expertise,
                        analysis_result=legacy_format
                    )
                    logger.info(f"Saved conversation to memory for user {user_id}")
                except Exception as e:
                    logger.warning(f"Failed to save conversation to memory: {e}")

            logger.info("Agent-based career analysis completed successfully")
            return legacy_format

        except Exception as e:
            logger.error(f"Error in agent-based career analysis: {e}", exc_info=True)
            # Return None to trigger fallback to existing AIService
            return None

    async def get_detailed_analysis(
        self,
        skills: str,
        expertise: str,
        user_id: Optional[str] = None
    ) -> Optional[AgentAnalysisResult]:
        """
        Get detailed agent analysis results (not converted to legacy format)

        Args:
            skills: User's skills description
            expertise: User's expertise level description
            user_id: Optional user ID for session management

        Returns:
            AgentAnalysisResult with full agent output, or None if failed
        """
        try:
            self._ensure_initialized()

            agent_results = await self.agent_service.analyze_career_with_agents(
                skills=skills,
                expertise=expertise,
                user_id=user_id
            )

            # Create AgentAnalysisResult
            result = AgentAnalysisResult(
                skill_assessment=agent_results.get("skill_assessment", {}),
                career_analysis=agent_results.get("career_analysis", {}),
                learning_roadmap=agent_results.get("learning_roadmap", {}),
                resources=agent_results.get("resources", {}),
                summary="Career analysis completed successfully using AI agents",
                next_steps=["Review career paths", "Examine roadmap", "Explore resources"]
            )

            return result

        except Exception as e:
            logger.error(f"Error getting detailed analysis: {e}", exc_info=True)
            return None

