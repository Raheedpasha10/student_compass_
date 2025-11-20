"""
Agent Service - Main entry point for agent-based career guidance
Supports both Google ADK (preferred) and fallback to direct Gemini API
"""
import os
import json
import logging
import asyncio
from typing import Dict, Any, Optional
from pydantic import BaseModel

# Try to import Google ADK
GOOGLE_ADK_AVAILABLE = False
try:
    from google.adk.agents import LlmAgent, SequentialAgent
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners import Runner
    GOOGLE_ADK_AVAILABLE = True
except ImportError:
    logger = logging.getLogger(__name__)
    logger.warning("Google ADK not available, will use fallback implementation")

from .schemas import (
    SkillAssessment,
    CareerMatchAnalysis,
    LearningRoadmap,
    ResourceCollection,
    AgentAnalysisResult
)

logger = logging.getLogger(__name__)


class AgentService:
    """
    Main agent service that orchestrates the multi-agent career guidance system.
    Uses Google ADK if available, otherwise falls back to direct Gemini API calls.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the agent service

        Args:
            api_key: Google Gemini API key (optional, will use env var if not provided)
        """
        self.api_key = api_key or os.getenv("GOOGLE_GENAI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_GENAI_API_KEY or GOOGLE_API_KEY is required. Set it in environment variables.")

        self.use_adk = GOOGLE_ADK_AVAILABLE

        if self.use_adk:
            try:
                self.session_service = InMemorySessionService()
                self.runner = Runner(session_service=self.session_service)
                logger.info("AgentService initialized with Google ADK")
            except Exception as e:
                logger.warning(f"Failed to initialize Google ADK, using fallback: {e}")
                self.use_adk = False

        if not self.use_adk:
            # Initialize fallback Gemini service
            self._init_gemini_fallback()
            logger.info("AgentService initialized with Gemini fallback")

    def _init_gemini_fallback(self):
        """Initialize Gemini API for fallback implementation"""
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self.genai_model = genai.GenerativeModel('gemini-2.0-flash-exp')
            self.genai_available = True
        except Exception as e:
            logger.error(f"Failed to initialize Gemini fallback: {e}")
            self.genai_available = False
            # Try REST API approach
            self.genai_api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={self.api_key}"
            self.genai_available = True

    def _get_skill_analyzer_instruction(self) -> str:
        """Get instruction for Skill Analyzer Agent"""
        return """
You are an expert skill assessment agent specializing in analyzing technical and professional skills.

Your task:
1. Analyze the user's stated skills and expertise level in detail
2. Identify all current skills and categorize them (programming languages, frameworks, tools, soft skills, etc.)
3. Assess the proficiency level for each skill (Beginner/Intermediate/Advanced/Expert)
4. Identify strengths - areas where the user excels
5. Identify weaknesses - areas that need improvement
6. Determine overall expertise level based on the skills mentioned
7. Group skills into logical categories

Be thorough and comprehensive. Consider both technical and soft skills.
Provide accurate assessments that will help guide career recommendations.

Respond with valid JSON matching the SkillAssessment schema.
"""

    def _get_career_matcher_instruction(self, skill_assessment: Dict[str, Any]) -> str:
        """Get instruction for Career Matcher Agent"""
        return f"""
You are an expert career matching agent with deep knowledge of tech careers, market trends, and skill requirements.

Your task:
1. Review the following skill assessment: {json.dumps(skill_assessment, indent=2)}
2. Identify 3-5 suitable career paths that match the user's skills and interests
3. For each career path, calculate:
   - Match score (0-100) based on skill alignment
   - Current skill coverage percentage
   - Missing critical skills needed
   - Salary range (provide realistic ranges in INR format like "₹X-Y lakhs")
   - Growth prospects (High/Medium/Low with explanation)
   - Reasoning for why this career matches
4. Select the best matching career path based on:
   - Skill alignment
   - Growth potential
   - Market demand
   - User's expertise level
5. Assess transition difficulty
6. Provide market trends insights

Consider ALL career domains: Software Development, Data Science, DevOps, Cybersecurity,
UI/UX Design, Product Management, etc. Be comprehensive and think outside the box.

Respond with valid JSON matching the CareerMatchAnalysis schema.
"""

    def _get_roadmap_generator_instruction(self, skill_assessment: Dict[str, Any], career_analysis: Dict[str, Any]) -> str:
        """Get instruction for Roadmap Generator Agent"""
        return f"""
You are an expert learning path designer specializing in creating personalized career development roadmaps.

Your task:
1. Review the skill assessment: {json.dumps(skill_assessment, indent=2)}
2. Review the career analysis: {json.dumps(career_analysis, indent=2)}
3. Create a comprehensive, step-by-step learning roadmap that includes:
   - 8-12 detailed steps covering the learning journey
   - Each step should have:
     * Clear title and description
     * Realistic duration estimate
     * Specific skills to learn
     * Resources needed
     * Deliverables/outcomes
     * Difficulty level
   - Key milestones to track progress
   - Overall learning strategy
   - Recommended hours per week
   - Quick wins to build momentum early

The roadmap should:
- Start from the user's current skill level
- Bridge the gap to the target career
- Be practical and actionable
- Include both theoretical learning and hands-on projects
- Progress logically from foundational to advanced topics
- Consider the user's expertise level (beginner/intermediate/advanced)

Make it encouraging and motivating while being realistic about time commitments.

Respond with valid JSON matching the LearningRoadmap schema.
"""

    def _get_resource_curator_instruction(self, skill_assessment: Dict[str, Any], career_analysis: Dict[str, Any], learning_roadmap: Dict[str, Any]) -> str:
        """Get instruction for Resource Curator Agent"""
        return f"""
You are an expert resource curator specializing in finding the best learning resources for career development.

Your task:
1. Review skill assessment: {json.dumps(skill_assessment, indent=2)}
2. Review career analysis: {json.dumps(career_analysis, indent=2)}
3. Review learning roadmap: {json.dumps(learning_roadmap, indent=2)}
4. Curate comprehensive resources:
   - Courses: 5-8 high-quality courses from platforms like Coursera, Udemy, edX, freeCodeCamp, etc.
   - Books: 4-6 relevant books (include titles, authors, and descriptions)
   - Certifications: 3-5 industry-recognized certifications
   - Videos: YouTube channels or video series (optional but helpful)
   - Articles: Key articles or documentation (optional)
   - Tools: Software, platforms, or tools needed
   - Communities: Online communities, forums, Discord servers

For each resource:
- Provide accurate titles and descriptions
- Include provider/platform information
- Add URLs (use actual URLs if known, or Google search URLs format)
- Specify difficulty level
- Include duration if applicable
- Add relevance score (0-100) based on how well it matches the learning goals
- Include cost information if relevant (Free/Paid/Subscription)

Prioritize:
- Resources that align with the roadmap steps
- High-quality, well-regarded resources
- Mix of free and paid options
- Resources suitable for the user's current skill level
- Resources that cover missing skills from the career analysis

Respond with valid JSON matching the ResourceCollection schema.
"""

    async def _call_gemini_with_schema(self, prompt: str, schema_class: BaseModel, max_retries: int = 3) -> Dict[str, Any]:
        """Call Gemini API with schema validation"""
        import requests

        schema_json = schema_class.model_json_schema()
        full_prompt = f"""{prompt}

IMPORTANT: Respond with ONLY valid JSON that matches the following schema structure:
{json.dumps(schema_json, indent=2)}

Do not include any markdown formatting, code blocks, or explanatory text. Return ONLY the JSON object."""

        for attempt in range(max_retries):
            try:
                if hasattr(self, 'genai_model') and self.genai_available:
                    # Use SDK (avoid unsupported GenerationConfig fields for broad compatibility)
                    response = self.genai_model.generate_content(full_prompt)
                    result_text = getattr(response, "text", "")
                else:
                    # Use REST API
                    payload = {
                        "contents": [{
                            "parts": [{
                                "text": full_prompt
                            }]
                        }]
                    }
                    response = requests.post(self.genai_api_url, json=payload, timeout=60)
                    response.raise_for_status()
                    result = response.json()
                    result_text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")

                # Parse JSON
                if isinstance(result_text, str):
                    # Clean up JSON string
                    result_text = result_text.strip()
                    # Remove markdown code blocks
                    if result_text.startswith("```json"):
                        result_text = result_text[7:]
                    elif result_text.startswith("```"):
                        result_text = result_text[3:]
                    if result_text.endswith("```"):
                        result_text = result_text[:-3]
                    result_text = result_text.strip()

                    # Parse JSON
                    try:
                        parsed = json.loads(result_text)
                    except json.JSONDecodeError as json_err:
                        logger.warning(f"JSON parse error: {json_err}, text: {result_text[:200]}")
                        # Try to extract JSON from text
                        start_idx = result_text.find('{')
                        end_idx = result_text.rfind('}') + 1
                        if start_idx != -1 and end_idx > start_idx:
                            parsed = json.loads(result_text[start_idx:end_idx])
                        else:
                            raise

                    # Validate against schema (try to create instance)
                    try:
                        schema_class(**parsed)
                    except Exception as validation_err:
                        logger.warning(f"Schema validation warning: {validation_err}, but continuing with parsed data")

                    return parsed
                else:
                    # Already a dict
                    return result_text if isinstance(result_text, dict) else {}

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    logger.error(f"All {max_retries} attempts failed for schema {schema_class.__name__}")
                    raise
                await asyncio.sleep(1)

        raise Exception("Failed to get valid response from Gemini after all retries")

    async def analyze_career_with_agents(
        self,
        skills: str,
        expertise: str,
        user_id: Optional[str] = None,
        use_web_search: bool = True
    ) -> Dict[str, Any]:
        """
        Run the complete agent-based career analysis

        Args:
            skills: User's skills description
            expertise: User's expertise level description
            user_id: Optional user ID for session management
            use_web_search: Whether to use web search for resource discovery

        Returns:
            Dictionary containing complete analysis results
        """
        if self.use_adk:
            return await self._analyze_with_adk(skills, expertise, user_id, use_web_search)
        else:
            return await self._analyze_with_fallback(skills, expertise, user_id, use_web_search)

    async def _analyze_with_adk(self, skills: str, expertise: str, user_id: Optional[str] = None, use_web_search: bool = True) -> Dict[str, Any]:
        """Analyze using Google ADK"""
        import uuid

        try:
            # Generate unique session ID
            session_id = f"career_session_{uuid.uuid4().hex[:8]}"
            user_id = user_id or "default_user"

            # Create agents
            skill_analyzer = LlmAgent(
                name="SkillAnalyzerAgent",
                model="gemini-2.0-flash-exp",
                description="Analyzes user skills, identifies strengths, weaknesses, and skill gaps",
                instruction=self._get_skill_analyzer_instruction(),
                output_schema=SkillAssessment,
                output_key="skill_assessment"
            )

            career_matcher = LlmAgent(
                name="CareerMatcherAgent",
                model="gemini-2.0-flash-exp",
                description="Matches user skills to suitable career paths with detailed analysis",
                instruction="""You are an expert career matching agent. Read state['skill_assessment'] and provide career matches.
                Use the CareerMatchAnalysis schema.""",
                output_schema=CareerMatchAnalysis,
                output_key="career_analysis"
            )

            roadmap_generator = LlmAgent(
                name="RoadmapGeneratorAgent",
                model="gemini-2.0-flash-exp",
                description="Generates personalized learning roadmaps",
                instruction="""You are an expert learning path designer. Read state['skill_assessment'] and state['career_analysis'].
                Use the LearningRoadmap schema.""",
                output_schema=LearningRoadmap,
                output_key="learning_roadmap"
            )

            resource_curator = LlmAgent(
                name="ResourceCuratorAgent",
                model="gemini-2.0-flash-exp",
                description="Curates high-quality learning resources",
                instruction="""You are an expert resource curator. Read state['skill_assessment'], state['career_analysis'], and state['learning_roadmap'].
                Use the ResourceCollection schema.""",
                output_schema=ResourceCollection,
                output_key="resources"
            )

            # Create sequential agent
            sequential_agent = SequentialAgent(
                name="CareerGuidanceSequentialAgent",
                description="Sequential agent pipeline for comprehensive career guidance",
                sub_agents=[
                    skill_analyzer,
                    career_matcher,
                    roadmap_generator,
                    resource_curator
                ]
            )

            # Initialize runner with agent
            runner = Runner(
                agent=sequential_agent,
                session_service=self.session_service
            )

            # Run agent
            initial_prompt = f"""
Analyze the following user profile for comprehensive career guidance:

Skills: {skills}
Expertise Level: {expertise}

Please conduct a thorough analysis through all agent stages.
"""

            # Create session with initial state
            session = self.session_service.create_session(
                user_id=user_id,
                session_id=session_id
            )

            # Run the agent
            async for event in runner.run_async(
                session=session,
                user_input=initial_prompt
            ):
                # Process events if needed
                logger.debug(f"Agent event: {event}")
                pass

            # Get final state from session
            state = session.state if hasattr(session, 'state') else {}

            # Try to get updated session if available
            try:
                final_session = self.session_service.get_session(user_id, session_id)
                if final_session and hasattr(final_session, 'state'):
                    state = final_session.state
            except Exception:
                pass

            return {
                "skill_assessment": state.get("skill_assessment"),
                "career_analysis": state.get("career_analysis"),
                "learning_roadmap": state.get("learning_roadmap"),
                "resources": state.get("resources"),
                "agent_run_successful": True
            }

        except Exception as e:
            logger.error(f"Error in ADK-based analysis: {str(e)}", exc_info=True)
            # Fallback to direct Gemini calls
            logger.info("Falling back to direct Gemini API calls")
            return await self._analyze_with_fallback(skills, expertise, user_id, use_web_search)

    async def _analyze_with_fallback(self, skills: str, expertise: str, user_id: Optional[str] = None, use_web_search: bool = True) -> Dict[str, Any]:
        """Analyze using direct Gemini API calls (fallback)"""
        try:
            # Stage 1: Skill Assessment
            skill_prompt = f"""
{self._get_skill_analyzer_instruction()}

User Skills: {skills}
User Expertise: {expertise}
"""
            skill_assessment = await self._call_gemini_with_schema(skill_prompt, SkillAssessment)

            # Stage 2: Career Matching
            career_prompt = self._get_career_matcher_instruction(skill_assessment)
            career_analysis = await self._call_gemini_with_schema(career_prompt, CareerMatchAnalysis)

            # Stage 3: Roadmap Generation
            roadmap_prompt = self._get_roadmap_generator_instruction(skill_assessment, career_analysis)
            learning_roadmap = await self._call_gemini_with_schema(roadmap_prompt, LearningRoadmap)

            # Stage 4: Resource Curation (with web search if enabled)
            resource_prompt = self._get_resource_curator_instruction(skill_assessment, career_analysis, learning_roadmap)

            # Enhance with web search if enabled
            if use_web_search:
                try:
                    from .tools import resource_discovery_tool

                    # Get best match career for search
                    best_match = career_analysis.get("best_match", {})
                    career_title = best_match.get("title", "") if isinstance(best_match, dict) else ""

                    if career_title:
                        # Discover real-time resources
                        discovered_courses = resource_discovery_tool.discover_courses_for_skill(
                            career_title, level=expertise.lower()
                        )
                        discovered_certifications = resource_discovery_tool.discover_certifications_for_career(career_title)

                        # Add discovered resources to prompt
                        if discovered_courses or discovered_certifications:
                            resource_prompt += "\n\nReal-time Discovered Resources:\n"
                            if discovered_courses:
                                resource_prompt += f"Courses: {json.dumps(discovered_courses[:5], indent=2)}\n"
                            if discovered_certifications:
                                resource_prompt += f"Certifications: {json.dumps(discovered_certifications[:3], indent=2)}\n"

                            resource_prompt += "\nPlease incorporate these real-time resources into your recommendations."
                except Exception as search_error:
                    logger.warning(f"Web search failed, continuing without real-time resources: {search_error}")

            resources = await self._call_gemini_with_schema(resource_prompt, ResourceCollection)

            return {
                "skill_assessment": skill_assessment,
                "career_analysis": career_analysis,
                "learning_roadmap": learning_roadmap,
                "resources": resources,
                "agent_run_successful": True
            }

        except Exception as e:
            logger.error(f"Error in fallback analysis: {str(e)}", exc_info=True)
            raise

    def convert_agent_results_to_legacy_format(self, agent_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert agent results to the legacy format expected by the API

        This ensures backward compatibility with existing frontend and API consumers
        """
        try:
            # Extract data from agent results
            career_analysis = agent_results.get("career_analysis", {})
            learning_roadmap = agent_results.get("learning_roadmap", {})
            resources = agent_results.get("resources", {})

            # Convert career paths
            career_paths = []
            if isinstance(career_analysis, dict):
                paths = career_analysis.get("career_paths", [])
                for path in paths:
                    if isinstance(path, dict):
                        career_paths.append({
                            "title": path.get("title", ""),
                            "description": path.get("description", ""),
                            "required_skills": path.get("required_skills", []),
                            "salary_range": path.get("salary_range", ""),
                            "growth_prospect": path.get("growth_prospect", "")
                        })

            # Get best match
            selected_path = {}
            if isinstance(career_analysis, dict):
                best_match = career_analysis.get("best_match", {})
                if isinstance(best_match, dict):
                    selected_path = {
                        "title": best_match.get("title", ""),
                        "description": best_match.get("description", ""),
                        "required_skills": best_match.get("required_skills", []),
                        "salary_range": best_match.get("salary_range", ""),
                        "growth_prospect": best_match.get("growth_prospect", "")
                    }

            # Convert roadmap
            roadmap_steps = []
            if isinstance(learning_roadmap, dict):
                steps = learning_roadmap.get("steps", [])
                for step in steps:
                    if isinstance(step, dict):
                        roadmap_steps.append({
                            "step": step.get("step_number", 0),
                            "title": step.get("title", ""),
                            "description": step.get("description", ""),
                            "duration": step.get("duration", ""),
                            "resources": step.get("resources_needed", [])
                        })

            # Convert courses
            courses = []
            if isinstance(resources, dict):
                course_list = resources.get("courses", [])
                for course in course_list:
                    if isinstance(course, dict):
                        courses.append({
                            "title": course.get("title", ""),
                            "provider": course.get("provider", ""),
                            "duration": course.get("duration", ""),
                            "difficulty": course.get("difficulty", ""),
                            "url": course.get("url", ""),
                            "type": course.get("type", "course")
                        })

            # Convert certifications
            certifications = []
            if isinstance(resources, dict):
                cert_list = resources.get("certifications", [])
                for cert in cert_list:
                    if isinstance(cert, dict):
                        url = cert.get("url", "")
                        if not url:
                            url = f"https://www.google.com/search?q={cert.get('title', '').replace(' ', '+')}+certification+{cert.get('provider', '').replace(' ', '+')}"

                        certifications.append({
                            "name": cert.get("title", ""),
                            "provider": cert.get("provider", ""),
                            "description": cert.get("description", ""),
                            "difficulty": cert.get("difficulty", ""),
                            "duration": cert.get("duration", ""),
                            "url": url
                        })

            return {
                "career_paths": career_paths[:3] if career_paths else [],
                "selected_path": selected_path,
                "roadmap": roadmap_steps,
                "courses": courses,
                "certifications": certifications
            }

        except Exception as e:
            logger.error(f"Error converting agent results to legacy format: {str(e)}")
            raise
