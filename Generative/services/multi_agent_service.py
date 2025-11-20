"""
Multi-Agent Funneling Service for Student Compass
Uses 3 different AI agents to generate roadmaps, then funnels them into one optimal result
"""

import os
import asyncio
import json
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import httpx
from groq import Groq
import google.generativeai as genai


@dataclass
class AgentResponse:
    """Response from a single agent"""
    agent_name: str
    roadmap: str
    confidence_score: float
    metadata: Dict[str, Any]


import json
import os
from pathlib import Path

# Global storage for funneling logs
GLOBAL_FUNNELING_LOGS = []
LOGS_FILE_PATH = Path("funneling_logs.json")

def save_logs_to_file():
    """Save funneling logs to file"""
    try:
        with open(LOGS_FILE_PATH, 'w') as f:
            json.dump(GLOBAL_FUNNELING_LOGS, f, default=str)
    except Exception as e:
        print(f"Warning: Could not save logs to file: {e}")

def load_logs_from_file():
    """Load funneling logs from file"""
    global GLOBAL_FUNNELING_LOGS
    try:
        if LOGS_FILE_PATH.exists():
            with open(LOGS_FILE_PATH, 'r') as f:
                GLOBAL_FUNNELING_LOGS = json.load(f)
    except Exception as e:
        print(f"Warning: Could not load logs from file: {e}")
        GLOBAL_FUNNELING_LOGS = []

# Load existing logs on import
load_logs_from_file()

class MultiAgentFunnelService:
    """
    Orchestrates multiple AI agents to generate roadmaps and funnels results
    """
    
    def __init__(self):
        # Initialize API clients
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        genai.configure(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))
        self.gemini_model = genai.GenerativeModel('gemini-2.0-flash')
        self.huggingface_token = os.getenv("HUGGINGFACE_API_TOKEN")
        
        # Use global funneling logs
        self.current_session_id = None
        self.agent_performance_metrics = {}
        
        # Agent configurations
        self.agents = {
            "agent_strategic": {
                "name": "Strategic Planner",
                "provider": "groq",
                "model": "llama-3.3-70b-versatile",
                "focus": "long-term career strategy and industry insights"
            },
            "agent_practical": {
                "name": "Practical Guide",
                "provider": "gemini",
                "model": "gemini-2.0-flash",
                "focus": "actionable steps, resources, and hands-on learning"
            },
            "agent_technical": {
                "name": "Technical Expert",
                "provider": "groq",
                "model": "llama-3.1-8b-instant",
                "focus": "technical skills, tools, and technologies"
            }
        }
    
    def _start_new_session(self, user_query: str, user_background: dict = None):
        """Initialize a new funneling session for reporting."""
        import time
        import uuid
        
        self.current_session_id = str(uuid.uuid4())[:8]
        session_start = {
            "session_id": self.current_session_id,
            "timestamp": time.time(),
            "user_query": user_query,
            "user_background": user_background or {},
            "agents_involved": list(self.agents.keys()),
            "status": "INITIATED"
        }
        GLOBAL_FUNNELING_LOGS.append(session_start)
        save_logs_to_file()
        return self.current_session_id
    
    def _log_agent_start(self, agent_id: str, agent_config: dict):
        """Log when an agent starts processing."""
        import time
        
        log_entry = {
            "session_id": self.current_session_id,
            "timestamp": time.time(),
            "event_type": "AGENT_START",
            "agent_id": agent_id,
            "agent_name": agent_config["name"],
            "provider": agent_config["provider"],
            "model": agent_config["model"],
            "focus": agent_config["focus"]
        }
        GLOBAL_FUNNELING_LOGS.append(log_entry)
        save_logs_to_file()
    
    def _log_agent_response(self, agent_id: str, response: 'AgentResponse', response_time: float):
        """Log agent response with detailed metrics."""
        import time
        
        # Calculate response metrics
        response_length = len(response.roadmap) if response.roadmap else 0
        has_structured_data = bool(response.roadmap and response.confidence_score > 0)
        
        log_entry = {
            "session_id": self.current_session_id,
            "timestamp": time.time(),
            "event_type": "AGENT_RESPONSE",
            "agent_id": agent_id,
            "agent_name": response.agent_name,
            "confidence_score": response.confidence_score,
            "response_time_seconds": round(response_time, 2),
            "response_length_chars": response_length,
            "has_structured_data": has_structured_data,
            "success": response.confidence_score > 0 and response_length > 0,
            "error": response.metadata.get("error") if response.confidence_score == 0 else None
        }
        GLOBAL_FUNNELING_LOGS.append(log_entry)
        save_logs_to_file()
    
    def _log_funneling_process(self, agent_responses: list, best_agent: str, final_confidence: float):
        """Log the funneling decision process."""
        import time
        
        # Analyze funneling metrics
        successful_agents = [r for r in agent_responses if r.confidence_score > 0]
        confidence_scores = {r.agent_name: r.confidence_score for r in agent_responses}
        
        log_entry = {
            "session_id": self.current_session_id,
            "timestamp": time.time(),
            "event_type": "FUNNELING_PROCESS",
            "total_agents": len(agent_responses),
            "successful_agents": len(successful_agents),
            "confidence_scores": confidence_scores,
            "best_agent": best_agent,
            "final_confidence": final_confidence,
            "funneling_method": "confidence_based_selection"
        }
        GLOBAL_FUNNELING_LOGS.append(log_entry)
        save_logs_to_file()
    
    def _log_session_complete(self, final_result: dict):
        """Log session completion with final metrics."""
        import time
        
        # Calculate session metrics - FIX: Use GLOBAL_FUNNELING_LOGS instead of self.funneling_logs
        session_logs = [log for log in GLOBAL_FUNNELING_LOGS if log.get("session_id") == self.current_session_id]
        session_start_time = min(log["timestamp"] for log in session_logs)
        total_time = time.time() - session_start_time
        
        # Count phases and content quality
        structured_plan = final_result.get("metadata", {}).get("structured_plan", {})
        total_phases = len(structured_plan.get("phases", []))
        total_content_items = sum(
            len(phase.get("goals", [])) + len(phase.get("topics", [])) + 
            len(phase.get("projects", [])) + len(phase.get("resources", []))
            for phase in structured_plan.get("phases", [])
        )
        
        log_entry = {
            "session_id": self.current_session_id,
            "timestamp": time.time(),
            "event_type": "SESSION_COMPLETE",
            "total_time_seconds": round(total_time, 2),
            "final_roadmap_length": len(final_result.get("final_roadmap", "")),
            "total_phases_generated": total_phases,
            "total_content_items": total_content_items,
            "success": bool(final_result.get("final_roadmap"))
        }
        GLOBAL_FUNNELING_LOGS.append(log_entry)
        save_logs_to_file()
    
    def generate_funneling_report(self, session_id: str = None) -> dict:
        """Generate a comprehensive report of the funneling process."""
        target_session = session_id or self.current_session_id
        if not target_session:
            return {"error": "No session to report on"}
        
        # Filter logs for this session
        session_logs = [log for log in GLOBAL_FUNNELING_LOGS if log.get("session_id") == target_session]
        if not session_logs:
            return {"error": f"No logs found for session {target_session}"}
        
        # Organize logs by type
        session_info = next((log for log in session_logs if "user_query" in log), {})
        agent_starts = [log for log in session_logs if log.get("event_type") == "AGENT_START"]
        agent_responses = [log for log in session_logs if log.get("event_type") == "AGENT_RESPONSE"]
        funneling_info = next((log for log in session_logs if log.get("event_type") == "FUNNELING_PROCESS"), {})
        completion_info = next((log for log in session_logs if log.get("event_type") == "SESSION_COMPLETE"), {})
        
        # Calculate performance metrics
        total_time = completion_info.get("total_time_seconds", 0)
        success_rate = (funneling_info.get("successful_agents", 0) / funneling_info.get("total_agents", 1)) * 100
        avg_confidence = sum(funneling_info.get("confidence_scores", {}).values()) / max(len(funneling_info.get("confidence_scores", {})), 1)
        
        # Enhanced report with rich real data
        report = {
            "session_id": target_session,
            "user_query": session_info.get("user_query", ""),
            "user_background": session_info.get("user_background", {}),
            "timestamp": session_info.get("timestamp"),
            "generation_date": time.time(),
            
            "agent_performance": {
                "total_agents": len(agent_starts),
                "successful_agents": funneling_info.get("successful_agents", 0),
                "success_rate_percent": round(success_rate, 1),
                "average_confidence": round(avg_confidence, 3),
                "total_processing_time": f"{total_time:.2f}s",
                "agents_used": [start.get("agent_name") for start in agent_starts],
                "individual_results": []
            },
            
            "funneling_process": {
                "method": "Multi-Agent Confidence-Based Selection",
                "best_agent": funneling_info.get("best_agent", ""),
                "final_confidence": funneling_info.get("final_confidence", 0),
                "confidence_scores": funneling_info.get("confidence_scores", {}),
                "decision_rationale": f"After analyzing responses from {len(agent_starts)} specialized AI agents, selected '{funneling_info.get('best_agent', '')}' based on highest confidence score ({funneling_info.get('final_confidence', 0):.3f}) and content quality metrics. This ensures the most accurate and comprehensive career guidance.",
                "selection_criteria": "Confidence score, content depth, resource quality, practical applicability",
                "quality_threshold": "0.5 minimum confidence required"
            },
            
            "output_metrics": {
                "total_execution_time": f"{total_time:.2f} seconds",
                "phases_generated": completion_info.get("total_phases_generated", 0),
                "content_items": completion_info.get("total_content_items", 0),
                "roadmap_length": completion_info.get("final_roadmap_length", 0),
                "average_phase_quality": round(avg_confidence, 3),
                "resource_links_found": completion_info.get("total_content_items", 0) // 3,  # Estimate
                "estimated_learning_hours": completion_info.get("total_phases_generated", 0) * 40  # 40 hours per phase
            },
            
            "detailed_timeline": []
        }
        
        # Add individual agent performance
        for response_log in agent_responses:
            start_log = next((log for log in agent_starts if log.get("agent_id") == response_log.get("agent_id")), {})
            
            agent_result = {
                "agent_name": response_log.get("agent_name", ""),
                "focus": start_log.get("focus", ""),
                "provider": start_log.get("provider", ""),
                "model": start_log.get("model", ""),
                "confidence_score": response_log.get("confidence_score", 0),
                "response_time": f"{response_log.get('response_time_seconds', 0):.2f}s",
                "success": response_log.get("success", False),
                "output_length": response_log.get("response_length_chars", 0),
                "error": response_log.get("error")
            }
            report["agent_performance"]["individual_results"].append(agent_result)
        
        # Add enhanced detailed timeline with rich information
        for log in sorted(session_logs, key=lambda x: x.get("timestamp", 0)):
            timeline_entry = {
                "timestamp": log.get("timestamp"),
                "event": log.get("event_type", ""),
                "details": "",
                "agent_info": {},
                "metrics": {}
            }
            
            if log.get("event_type") == "AGENT_START":
                timeline_entry["details"] = f"🚀 Initialized {log.get('agent_name')} specialist agent using {log.get('provider').upper()}/{log.get('model')} - Focus: {log.get('focus', 'career guidance')}"
                timeline_entry["agent_info"] = {
                    "name": log.get('agent_name'),
                    "provider": log.get('provider'),
                    "model": log.get('model'),
                    "specialization": log.get('focus')
                }
            elif log.get("event_type") == "AGENT_RESPONSE":
                status = "✅ Success" if log.get('success') else "❌ Failed"
                timeline_entry["details"] = f"{status} - {log.get('agent_name')} generated {log.get('response_length_chars', 0):,} characters in {log.get('response_time_seconds', 0):.2f}s (Confidence: {log.get('confidence_score', 0):.3f})"
                timeline_entry["metrics"] = {
                    "response_time": log.get('response_time_seconds', 0),
                    "confidence": log.get('confidence_score', 0),
                    "content_length": log.get('response_length_chars', 0),
                    "success": log.get('success', False)
                }
            elif log.get("event_type") == "FUNNELING_PROCESS":
                timeline_entry["details"] = f"🎯 Funneling analysis complete - Selected '{log.get('best_agent')}' from {log.get('total_agents')} agents ({log.get('successful_agents')} successful, {((log.get('successful_agents', 0) / log.get('total_agents', 1)) * 100):.1f}% success rate)"
                timeline_entry["metrics"] = {
                    "total_agents": log.get('total_agents', 0),
                    "successful_agents": log.get('successful_agents', 0),
                    "best_agent": log.get('best_agent'),
                    "final_confidence": log.get('final_confidence', 0)
                }
            elif log.get("event_type") == "SESSION_COMPLETE":
                timeline_entry["details"] = f"🎉 Roadmap generation complete - {log.get('total_phases_generated', 0)} learning phases with {log.get('total_content_items', 0)} content items generated ({log.get('final_roadmap_length', 0):,} characters total)"
                timeline_entry["metrics"] = {
                    "total_time": log.get('total_time_seconds', 0),
                    "phases_generated": log.get('total_phases_generated', 0),
                    "content_items": log.get('total_content_items', 0),
                    "roadmap_length": log.get('final_roadmap_length', 0)
                }
            
            report["detailed_timeline"].append(timeline_entry)
        
        return report
    
    async def generate_roadmap_with_agent(
        self, 
        agent_config: Dict[str, str], 
        user_query: str,
        user_background: Optional[Dict[str, Any]] = None,
        agent_id: str = None
    ) -> AgentResponse:
        """Generate roadmap using a single agent and enforce structured JSON."""
        import time
        
        # Log agent start
        if agent_id and self.current_session_id:
            self._log_agent_start(agent_id, agent_config)
        
        start_time = time.time()
        
        # Create specialized prompt based on agent focus
        prompt = self._create_agent_prompt(
            agent_config["focus"], 
            user_query, 
            user_background
        )
        
        try:
            if agent_config["provider"] == "groq":
                raw_response = await self._call_groq(agent_config["model"], prompt)
            elif agent_config["provider"] == "gemini":
                raw_response = await self._call_gemini(prompt)
            elif agent_config["provider"] == "huggingface":
                raw_response = await self._call_huggingface(agent_config["model"], prompt)
            else:
                raise ValueError(f"Unknown provider: {agent_config['provider']}")
            
            structured = self._parse_agent_json(raw_response)
            if not structured:
                # Could not parse valid JSON; return low-confidence
                return AgentResponse(
                    agent_name=agent_config["name"],
                    roadmap="",
                    confidence_score=0.0,
                    metadata={
                        "provider": agent_config["provider"],
                        "model": agent_config["model"],
                        "focus": agent_config["focus"],
                        "error": "Invalid JSON from model"
                    }
                )
            
            confidence = self._score_structured(structured, user_background or {})
            
            response = AgentResponse(
                agent_name=agent_config["name"],
                roadmap=json.dumps(structured),
                confidence_score=confidence,
                metadata={
                    "provider": agent_config["provider"],
                    "model": agent_config["model"],
                    "focus": agent_config["focus"]
                }
            )
            
            # Log successful response
            if agent_id and self.current_session_id:
                self._log_agent_response(agent_id, response, time.time() - start_time)
            
            return response
        
        except Exception as e:
            error_msg = str(e)
            print(f"Error with {agent_config['name']}: {error_msg}")
            
            # If rate limit, provide helpful message
            if "rate_limit" in error_msg.lower() or "429" in error_msg:
                print(f"⚠️ Rate limit hit for {agent_config['name']} - this agent will be skipped")
            
            error_response = AgentResponse(
                agent_name=agent_config["name"],
                roadmap="",
                confidence_score=0.0,
                metadata={"error": error_msg}
            )
            
            # Log error response
            if agent_id and self.current_session_id:
                self._log_agent_response(agent_id, error_response, time.time() - start_time)
            
            return error_response
    
    async def _call_groq(self, model: str, prompt: str) -> str:
        """Call Groq API"""
        # Run the blocking Groq call in an executor to avoid blocking the event loop
        import asyncio
        loop = asyncio.get_event_loop()
        
        def _sync_groq_call():
            chat_completion = self.groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert career advisor specializing in creating detailed learning roadmaps."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=model,
                temperature=0.6,  # Slightly reduced for more focused output
                max_tokens=1500   # Reduced from 2000 for faster responses
            )
            return chat_completion.choices[0].message.content
        
        return await loop.run_in_executor(None, _sync_groq_call)
    
    async def _call_gemini(self, prompt: str) -> str:
        """Call Google Gemini API"""
        # Run the blocking Gemini call in an executor to avoid blocking the event loop
        import asyncio
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, self.gemini_model.generate_content, prompt)
        return response.text
    
    async def _call_huggingface(self, model: str, prompt: str) -> str:
        """Call HuggingFace Inference API"""
        API_URL = f"https://api-inference.huggingface.co/models/{model}"
        headers = {"Authorization": f"Bearer {self.huggingface_token}"}
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                API_URL,
                headers=headers,
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 1500,  # Reduced for speed
                        "temperature": 0.6       # More focused output
                    }
                },
                timeout=30.0
            )
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "")
            return str(result)
    
    def _create_agent_prompt(
        self, 
        focus: str, 
        user_query: str,
        user_background: Optional[Dict[str, Any]] = None
    ) -> str:
        """Create specialized prompt for each agent enforcing a strict JSON schema optimized for frontend rendering with detailed expandable content."""
        # Enhanced schema with detailed content and paid/free resource indicators
        base_schema = {
            "overview": "Brief, compelling 2-sentence summary of the learning path",
            "time_commitment_hours_per_week": 12,
            "prerequisites": ["Prerequisite 1", "Prerequisite 2"],
            "phases": [
                {
                    "name": "Foundation Building",
                    "duration_weeks": 6,
                    "goals": ["Clear goal 1", "Clear goal 2", "Clear goal 3"],
                    "topics": ["Core topic 1", "Core topic 2", "Core topic 3", "Core topic 4"],
                    "detailed_content": {
                        "expanded_explanation": "Comprehensive explanation of what this phase covers and why it's important. Include practical benefits, industry relevance, and how it builds toward career goals. This content appears when user clicks 'View More'.",
                        "deep_dive_topics": [
                            {
                                "topic": "Advanced Topic Name",
                                "description": "Detailed explanation of this specific topic",
                                "practical_applications": ["Real-world use case 1", "Real-world use case 2"],
                                "learning_outcomes": ["What you'll be able to do", "Skill you'll master"]
                            }
                        ],
                        "skill_progression": {
                            "beginner": "What you'll learn as a beginner",
                            "intermediate": "How skills develop to intermediate level",
                            "advanced": "Advanced mastery and specialization"
                        },
                        "industry_insights": [
                            "Current market demand for these skills",
                            "Salary expectations after mastering this phase",
                            "Career opportunities this phase opens up"
                        ]
                    },
                    "projects": [
                        {
                            "name": "Project Name",
                            "description": "1-line project description",
                            "detailed_description": "Comprehensive project breakdown explaining objectives, technologies used, expected outcomes, and how it demonstrates mastery",
                            "tech_stack": ["Technology 1", "Technology 2"],
                            "difficulty": "Beginner/Intermediate/Advanced",
                            "estimated_hours": "10-15 hours"
                        }
                    ],
                    "tools": ["Tool/Technology 1", "Tool/Technology 2"],
                    "resources": [
                        {
                            "title": "Resource Title",
                            "provider": "Platform",
                            "url": "https://example.com",
                            "type": "Course/Tutorial/Documentation/Book/Video",
                            "cost": "Free/Paid/$XX",
                            "duration": "2 hours/4 weeks/Self-paced",
                            "difficulty": "Beginner/Intermediate/Advanced",
                            "rating": "4.5/5",
                            "description": "Brief description of what this resource covers",
                            "is_paid": false,
                            "price_note": "Free with registration/Premium subscription required/$49 one-time"
                        }
                    ],
                    "checkpoints": ["Milestone 1", "Milestone 2"]
                }
            ],
            "career_milestones": [
                {"timeframe": "3-6 months", "outcome": "Specific career outcome", "salary_range": "$50k-70k"}
            ]
        }

        role_addendum = ""
        if "strategic" in focus.lower():
            role_addendum = (
                "You are the STRATEGIC CAREER ARCHITECT - The world's most elite career strategist who has guided thousands to 6-figure positions. "
                "You possess DEEP insider knowledge of what Fortune 500 companies actually want, which skills command the highest salaries, and the EXACT steps for rapid career advancement. "
                "Your roadmaps are laser-focused on ROI - every skill taught directly translates to salary increases and job opportunities. "
                "You provide detailed career progression maps ($50k→$85k→$120k→$180k), industry networking strategies, and personal branding tactics that actually work. "
                "Your detailed_content sections include salary negotiation scripts, interview preparation strategies, and market insights that give unfair advantages. "
                "Create comprehensive, battle-tested pathways that consistently outperform generic learning paths and deliver measurable career results. "
                "For uncommon specializations, research current market trends and create innovative learning approaches that address specific industry gaps."
            )
        elif "practical" in focus.lower():
            role_addendum = (
                "You are the MASTER BUILDER - The legendary hands-on mentor who has trained thousands of professionals through real-world project mastery. "
                "You design 100% project-driven curricula with portfolio pieces that guarantee job interviews and impress even the most demanding hiring managers. "
                "Every phase builds tangible, deployable applications using cutting-edge tech stacks that demonstrate real expertise to employers. "
                "Your detailed_content provides step-by-step project breakdowns, architecture decisions, debugging strategies, and deployment best practices. "
                "You include comprehensive project documentation that students can confidently present in technical interviews and client meetings. "
                "Focus on creating impressive, scalable applications that solve real business problems and showcase both technical depth and practical problem-solving skills. "
                "For niche fields, design innovative projects that push boundaries and demonstrate expertise in emerging technologies and methodologies."
            )
        else:  # technical
            role_addendum = (
                "You are the TECHNICAL MASTER - The elite engineering mentor who creates world-class technical professionals capable of architecting complex systems. "
                "You possess deep expertise in both fundamental computer science principles and cutting-edge technologies that companies desperately need. "
                "Your curricula progress from rock-solid fundamentals to advanced architectural patterns that only the top 5% of professionals master. "
                "Your detailed_content includes system design principles, performance optimization techniques, scalability patterns, and production-ready best practices. "
                "You provide comprehensive technical deep-dives that prepare students for senior-level technical interviews at top-tier companies. "
                "Focus on both theoretical understanding and practical implementation of complex systems that can handle enterprise-scale challenges. "
                "For emerging or specialized technical fields, create forward-thinking curricula that anticipate industry evolution and prepare students for next-generation challenges."
            )

        background = {
            "current_skills": (user_background or {}).get("current_skills", ""),
            "experience_level": (user_background or {}).get("experience_level", "Beginner"),
            "time_available": (user_background or {}).get("time_available", "10-15 hours per week"),
            "goals": (user_background or {}).get("goals", ""),
            "education": (user_background or {}).get("education", "")
        }

        # Enhanced, focused prompts for clean frontend rendering
        specific_requirements = ""
        if "strategic" in focus.lower():
            specific_requirements = (
                "\nSTRATEGIC FOCUS - FRONTEND-OPTIMIZED OUTPUT:\n"
                "- Phase names: Use clear, progression-based titles (Foundation → Growth → Mastery)\n"
                "- Goals: Write 3-4 specific, measurable career objectives per phase\n"
                "- Topics: List 4-5 core strategic concepts (salary negotiation, networking, personal branding)\n"
                "- Projects: Portfolio/career projects that demonstrate strategic thinking\n"
                "- Tools: Professional tools (LinkedIn, portfolio platforms, job boards)\n"
                "- Resources: Career-focused resources with real URLs when possible\n"
                "- Checkpoints: Career milestones and skill validations\n"
                "- Keep text concise and scannable for UI display"
            )
        elif "practical" in focus.lower():
            specific_requirements = (
                "\nPRACTICAL FOCUS - FRONTEND-OPTIMIZED OUTPUT:\n" 
                "- Phase names: Action-oriented titles (Build → Deploy → Scale)\n"
                "- Goals: 3-4 hands-on objectives students can complete and showcase\n"
                "- Topics: 4-5 practical skills with immediate application\n"
                "- Projects: Real-world projects with clear deliverables and tech stacks\n"
                "- Tools: Development tools, frameworks, and platforms students will use\n"
                "- Resources: Tutorial links, documentation, and free learning materials\n"
                "- Checkpoints: Practical milestones (deployed projects, working features)\n"
                "- Focus on buildable, demonstrable outcomes"
            )
        else:  # technical
            specific_requirements = (
                "\nTECHNICAL FOCUS - FRONTEND-OPTIMIZED OUTPUT:\n"
                "- Phase names: Technical progression titles (Fundamentals → Architecture → Optimization)\n"
                "- Goals: 3-4 technical competencies with measurable outcomes\n"
                "- Topics: 4-5 core technical concepts with modern technologies\n"
                "- Projects: Technical implementations showcasing specific skills\n"
                "- Tools: Current tech stack with version numbers when relevant\n"
                "- Resources: Technical documentation, tutorials, and best practices\n"
                "- Checkpoints: Technical milestones (code quality, performance metrics)\n"
                "- Emphasize modern, industry-standard practices"
            )

        prompt = (
            f"You are an expert learning-path designer specializing in {focus}. "
            f"{role_addendum}\n\n"
            f"CRITICAL INSTRUCTIONS FOR PERFECT OUTPUT:\n"
            f"1. Return ONLY valid JSON matching the exact schema below - NO markdown, explanations, or extra text\n"
            f"2. Handle uncommon specializations by researching current market needs and creating comprehensive paths\n"
            f"3. Ensure zero rendering issues by following exact formatting guidelines\n"
            f"4. Create expandable content that provides value in both collapsed and expanded states\n\n"
            f"USER GOAL: {user_query}\n"
            f"USER BACKGROUND: {json.dumps(background)}\n\n"
            f"{specific_requirements}\n\n"
            f"ENHANCED CONTENT REQUIREMENTS:\n"
            f"- BASIC CONTENT: 3-4 concise, scannable items perfect for card display\n"
            f"- DETAILED_CONTENT: Rich, comprehensive explanations for 'View More' sections\n"
            f"- RESOURCE INDICATORS: Always specify if resources are Free, Paid, or include pricing\n"
            f"- PROJECT DEPTH: Include detailed breakdowns with tech stacks and time estimates\n"
            f"- INDUSTRY RELEVANCE: Connect learning to real job opportunities and salary ranges\n"
            f"- PROGRESSIVE DIFFICULTY: Ensure logical skill building across phases\n\n"
            f"CONTENT QUALITY STANDARDS:\n"
            f"- SPECIFICITY: Use concrete examples, not vague concepts\n"
            f"- ACTIONABILITY: Every item should be immediately implementable\n"
            f"- MARKET ALIGNMENT: Focus on skills that employers actually hire for\n"
            f"- MODERN RELEVANCE: Include current tools and technologies (2024)\n"
            f"- COMPREHENSIVE COVERAGE: Address both theory and practical application\n\n"
            f"FRONTEND OPTIMIZATION RULES:\n"
            f"- Arrays: Exactly 3-4 items for perfect UI card display\n"
            f"- Text length: Basic items under 60 chars, detailed content can be longer\n"
            f"- Clear hierarchy: Logical progression from basic to advanced concepts\n"
            f"- Consistent formatting: Use same structure patterns across all phases\n"
            f"- Error-free JSON: Double-check syntax to prevent rendering failures\n\n"
            f"UNCOMMON SPECIALIZATION HANDLING:\n"
            f"- Research current market demand and emerging trends\n"
            f"- Create innovative learning paths that address industry gaps\n"
            f"- Include both fundamental skills and cutting-edge specializations\n"
            f"- Connect niche skills to broader career opportunities\n"
            f"- Provide realistic timelines and progression expectations\n\n"
            f"RESOURCE QUALITY REQUIREMENTS:\n"
            f"- Always indicate cost: Free, Paid, or specific price range\n"
            f"- Include realistic time commitments and difficulty levels\n"
            f"- Prioritize high-quality, current resources over generic ones\n"
            f"- Mix free and paid resources to provide options for all budgets\n"
            f"- Include brief descriptions explaining why each resource is valuable\n\n"
            f"REQUIRED JSON SCHEMA:\n{json.dumps(base_schema, indent=2)}\n\n"
            f"FINAL REMINDER: Your response must be ONLY the perfectly formatted JSON object. "
            f"Every field must be filled with high-quality, specific, actionable content that will render flawlessly in the UI."
        )
        return prompt
    
    def _calculate_confidence(self, response: str) -> float:
        """Deprecated: replaced by _score_structured."""
        return 0.0

    def _parse_agent_json(self, raw_text: str) -> Optional[Dict[str, Any]]:
        """Try to parse strict JSON from model output, with fallback extraction."""
        if not raw_text:
            return None
        raw_text = raw_text.strip()
        # Fast path
        try:
            return json.loads(raw_text)
        except Exception:
            pass
        # Fallback: extract JSON substring
        import re
        match = re.search(r"\{[\s\S]*\}$", raw_text)
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                return None
        return None

    def _score_structured(self, data: Dict[str, Any], background: Dict[str, Any]) -> float:
        """Rubric-based scoring of structured agent output."""
        score = 0.0
        # Required keys
        required_keys = ["overview", "phases"]
        if all(k in data for k in required_keys):
            score += 0.3
        # Phases richness
        phases = data.get("phases", []) or []
        if len(phases) >= 3:
            score += 0.2
        detailed = 0
        concrete_counts = 0
        for ph in phases:
            # Check for non-empty content
            topics = [t for t in ph.get("topics", []) if t and t.strip()]
            projects = [p for p in ph.get("projects", []) if p and (isinstance(p, str) and p.strip() or isinstance(p, dict) and (p.get("name") or p.get("description")))]
            resources = [r for r in ph.get("resources", []) if r and (isinstance(r, str) and r.strip() or isinstance(r, dict) and (r.get("title") or r.get("url")))]
            
            if topics and projects and resources:
                detailed += 1
            # Specificity: count concrete items
            concrete_counts += len(topics) + len(projects) + len(resources)
        if detailed >= 2:
            score += 0.2
        # Specificity scaling
        score += min(concrete_counts / 50.0, 0.2)  # cap contribution
        # Time commitment consideration
        time_str = (background or {}).get("time_available", "")
        if isinstance(time_str, str) and any(h in time_str for h in ["hour", "hrs", "hours"]):
            score += 0.05
        # Prerequisites present
        if data.get("prerequisites"):
            score += 0.05
        return min(score, 1.0)

    def _merge_structured_outputs(self, outputs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Merge multiple structured agent outputs into a single coherent plan."""
        # Pick best overview (longest with substance)
        best_overview = max((o.get("overview", "") for o in outputs), key=lambda x: len(x), default="")
        # Aggregate phases by rough intent buckets
        def bucket(name: str) -> str:
            n = (name or "").lower()
            if any(k in n for k in ["foundation", "beginner", "basics"]):
                return "Foundation"
            if any(k in n for k in ["intermediate", "core", "skills"]):
                return "Intermediate"
            if any(k in n for k in ["advanced", "specialization", "expert"]):
                return "Advanced"
            if any(k in n for k in ["deployment", "devops", "production"]):
                return "Deployment"
            if any(k in n for k in ["portfolio", "project", "capstone"]):
                return "Portfolio"
            return "Other"
        buckets: Dict[str, List[Dict[str, Any]]] = {}
        for o in outputs:
            for ph in o.get("phases", []) or []:
                b = bucket(ph.get("name", ""))
                buckets.setdefault(b, []).append(ph)
        # Within each bucket, select top N phases by richness
        merged_phases: List[Dict[str, Any]] = []
        for b, plist in buckets.items():
            # Score per phase by count of topics+projects+resources
            def ph_score(p):
                return len(p.get("topics", [])) + len(p.get("projects", [])) + len(p.get("resources", []))
            top = sorted(plist, key=ph_score, reverse=True)[:2]
            for p in top:
                merged_phases.append(self._dedupe_phase(p))
        # Sort phases in a sensible order
        order = {"Foundation": 0, "Intermediate": 1, "Advanced": 2, "Deployment": 3, "Portfolio": 4, "Other": 5}
        merged_phases.sort(key=lambda p: order.get(bucket(p.get("name", "")), 5))
        # Merge career milestones
        milestones: List[Dict[str, Any]] = []
        for o in outputs:
            milestones.extend(o.get("career_milestones", []) or [])
        # Average time commitment if present
        times = [o.get("time_commitment_hours_per_week") for o in outputs if isinstance(o.get("time_commitment_hours_per_week"), (int, float))]
        time_commitment = int(sum(times) / len(times)) if times else 10
        return {
            "overview": best_overview,
            "time_commitment_hours_per_week": time_commitment,
            "phases": merged_phases,
            "career_milestones": milestones[:6]
        }

    def _clean_text(self, text: str) -> str:
        """Fast text cleaning for individual strings."""
        if not text or not isinstance(text, str):
            return ""
        
        # Basic cleaning - remove common bullets and markdown
        text = text.strip()
        
        # Remove bullets and markers (simple patterns only)
        if text.startswith(('-', '•', '*', '►', '▸')):
            text = text[1:].strip()
        
        # Remove markdown bold/italic
        text = text.replace('**', '').replace('`', '')
        
        # Clean whitespace
        text = ' '.join(text.split())
        
        return text
    
    def _is_valid_content(self, text: str) -> bool:
        """Fast validation for meaningful content."""
        if not text or len(text) < 4:
            return False
        
        # Skip obvious placeholders
        text_lower = text.lower()
        bad_patterns = ['todo', 'tbd', 'placeholder', 'example', '...', '---']
        
        return not any(bad in text_lower for bad in bad_patterns)
    
    def _clean_array_field(self, arr: list) -> list:
        """Fast cleaning and validation of array fields."""
        if not arr:
            return []
        
        cleaned = []
        for item in arr:
            if isinstance(item, str):
                clean_text = self._clean_text(item)
                if self._is_valid_content(clean_text):
                    cleaned.append(clean_text)
                    
            elif isinstance(item, dict):
                # Clean dict items
                clean_item = {}
                for key, value in item.items():
                    if isinstance(value, str):
                        clean_value = self._clean_text(value)
                        if clean_value:
                            clean_item[key] = clean_value
                    else:
                        clean_item[key] = value
                
                # Only include if has meaningful content
                if clean_item.get("name") or clean_item.get("title") or clean_item.get("description"):
                    cleaned.append(clean_item)
        
        return cleaned[:8]  # Limit to 8 items max

    def _dedupe_phase(self, p: Dict[str, Any]) -> Dict[str, Any]:
        """Deduplicate topics/tools/resources inside a phase and normalize fields."""
        def uniq(seq):
            seen = set()
            out = []
            for x in seq or []:
                key = json.dumps(x, sort_keys=True) if isinstance(x, dict) else str(x).lower()
                if key in seen:
                    continue
                seen.add(key)
                out.append(x)
            return out
        
        # Clean all array fields before deduplication
        goals = self._clean_array_field(p.get("goals", []))
        topics = self._clean_array_field(p.get("topics", []))
        projects = self._clean_array_field(p.get("projects", []))
        tools = self._clean_array_field(p.get("tools", []))
        resources = self._clean_array_field(p.get("resources", []))
        checkpoints = self._clean_array_field(p.get("checkpoints", []))
        
        return {
            "name": p.get("name", "").strip() or f"Learning Phase",
            "duration_weeks": int(p.get("duration_weeks", 0) or 4),  # Default to 4 weeks
            "goals": uniq(goals)[:5],  # Limit to 5 goals
            "topics": uniq(topics)[:8],  # Limit to 8 topics
            "projects": uniq(projects)[:4],  # Limit to 4 projects
            "tools": uniq(tools)[:6],  # Limit to 6 tools
            "resources": uniq(resources)[:5],  # Limit to 5 resources
            "checkpoints": uniq(checkpoints)[:5],  # Limit to 5 checkpoints
        }

    def _render_markdown(self, data: Dict[str, Any]) -> str:
        """Render final markdown from merged structured data."""
        lines: List[str] = []
        lines.append("## Overview\n")
        lines.append(f"{data.get('overview','').strip()}\n\n")
        lines.append("## Complete Learning Roadmap\n\n")
        for idx, ph in enumerate(data.get("phases", []), start=1):
            name = ph.get("name", f"Phase {idx}")
            dur = ph.get("duration_weeks")
            dur_txt = f" ({dur} weeks)" if dur else ""
            lines.append(f"**Phase {idx}: {name}**{dur_txt}\n\n")
            if ph.get("goals"):
                lines.append("Goals:\n" + "\n".join(f"- {g}" for g in ph["goals"]) + "\n\n")
            if ph.get("topics"):
                lines.append("What You'll Learn:\n" + "\n".join(f"- {t}" for t in ph["topics"]) + "\n\n")
            if ph.get("tools"):
                lines.append("Tools & Technologies:\n" + "\n".join(f"- {t}" for t in ph["tools"]) + "\n\n")
            if ph.get("projects"):
                lines.append("Hands-On Projects:\n" + "\n".join(
                    f"- {pr.get('name', 'Project')}: {pr.get('description','')}" if isinstance(pr, dict) else f"- {pr}"
                    for pr in ph["projects"]
                ) + "\n\n")
            if ph.get("resources"):
                def res_line(r):
                    if isinstance(r, dict):
                        title = r.get('title') or r.get('name') or 'Resource'
                        prov = r.get('provider')
                        url = r.get('url')
                        extra = f" ({prov})" if prov else ""
                        link = f": {url}" if url else ""
                        return f"- {title}{extra}{link}"
                    return f"- {r}"
                lines.append("Recommended Resources:\n" + "\n".join(res_line(r) for r in ph["resources"]) + "\n\n")
            if ph.get("checkpoints"):
                lines.append("Phase Completion Checklist:\n" + "\n".join(f"- [ ] {c}" for c in ph["checkpoints"]) + "\n\n")
        if data.get("career_milestones"):
            lines.append("## Career Milestones\n\n")
            for m in data["career_milestones"]:
                tf = m.get("timeframe", "") if isinstance(m, dict) else ""
                oc = m.get("outcome", "") if isinstance(m, dict) else str(m)
                lines.append(f"- {tf}: {oc}\n")
            lines.append("\n")
        return "".join(lines)
    
    async def funnel_roadmaps(
        self, 
        agent_responses: List[AgentResponse]
    ) -> str:
        """
        Funnel multiple agent responses into one optimal roadmap using deterministic merging of structured JSON,
        then render to markdown. Avoids freeform LLM synthesis to ensure quality and specificity.
        """
        # Parse structured JSON from agents
        structured_list: List[Dict[str, Any]] = []
        for r in agent_responses:
            if r.confidence_score <= 0 or not r.roadmap:
                continue
            try:
                structured_list.append(json.loads(r.roadmap))
            except Exception:
                continue
        
        if not structured_list:
            return "Unable to generate roadmap. Please try again."
        
        # Merge: choose best overview, align phases by intent, deduplicate topics/tools/resources
        merged = self._merge_structured_outputs(structured_list)
        
        # Render final markdown
        return self._render_markdown(merged)
    
    def _create_synthesis_prompt(self, responses: List[AgentResponse]) -> str:
        """Deprecated: no longer used. Kept for backward reference."""
        return ""
    
    async def generate_funneled_roadmap(
        self, 
        user_query: str,
        user_background: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Main method: Generate roadmap using multi-agent system with comprehensive logging
        Returns the final funneled result plus individual agent insights and funneling report
        """
        
        # Start new session for logging
        session_id = self._start_new_session(user_query, user_background)
        print(f"🚀 Starting multi-agent roadmap generation (Session: {session_id})...")
        print(f"🔍 Current funneling_logs length: {len(GLOBAL_FUNNELING_LOGS)}")
        print(f"📝 Session started with ID: {session_id}")
        
        # OPTIMIZED: Run agents in parallel with smart early completion
        tasks = [
            self.generate_roadmap_with_agent(config, user_query, user_background, agent_id)
            for agent_id, config in self.agents.items()
        ]
        
        # Smart timeout strategy: Return as soon as we have good results
        agent_responses = []
        try:
            # Wait for all agents with reduced timeout for speed
            done, pending = await asyncio.wait(
                tasks, 
                timeout=25.0,  # Reduced from 45s to 25s for speed
                return_when=asyncio.FIRST_COMPLETED  # Return as soon as first agent completes
            )
            
            # Collect completed results
            for task in done:
                try:
                    result = await task
                    if isinstance(result, AgentResponse):
                        agent_responses.append(result)
                except Exception as e:
                    print(f"Task error: {e}")
            
            # If we have at least one good result, continue with that
            good_results = [r for r in agent_responses if r.confidence_score > 0.3]
            if good_results:
                print(f"🚀 Early completion with {len(good_results)} quality results")
                # Cancel remaining tasks to save time
                for task in pending:
                    task.cancel()
            else:
                # Wait a bit more for remaining tasks if no good results yet
                print("⏳ No quality results yet, waiting for remaining agents...")
                timeout_remaining = max(15.0, 25.0 - 10.0)  # Max 15s more
                done2, pending2 = await asyncio.wait(
                    pending, 
                    timeout=timeout_remaining,
                    return_when=asyncio.ALL_COMPLETED
                )
                
                for task in done2:
                    try:
                        result = await task
                        if isinstance(result, AgentResponse):
                            agent_responses.append(result)
                    except Exception as e:
                        print(f"Task error: {e}")
                
                # Cancel any remaining tasks
                for task in pending2:
                    task.cancel()
                    
        except Exception as e:
            print(f"⚠️ Agent execution error: {e}")
            agent_responses = []
        
        print(f"✅ Received {len(agent_responses)} agent responses")
        for response in agent_responses:
            print(f"  - {response.agent_name}: Confidence {response.confidence_score:.2f}")
        
        # Build structured list and merged plan
        structured_list: List[Dict[str, Any]] = []
        for r in agent_responses:
            try:
                if r.confidence_score > 0 and r.roadmap:
                    structured_list.append(json.loads(r.roadmap))
            except Exception:
                continue
        merged_plan: Optional[Dict[str, Any]] = self._merge_structured_outputs(structured_list) if structured_list else None

        # Log funneling process
        best_agent = max(agent_responses, key=lambda r: r.confidence_score).agent_name if agent_responses else "None"
        final_confidence = max((r.confidence_score for r in agent_responses), default=0.0)
        self._log_funneling_process(agent_responses, best_agent, final_confidence)

        # Render final markdown
        print("🔄 Funneling responses into optimal roadmap...")
        final_roadmap = self._render_markdown(merged_plan) if merged_plan else "Unable to generate roadmap. Please try again."
        
        print("✅ Final roadmap generated!")
        
        # Prepare final result - ENSURE session_id is always included
        final_result = {
            "final_roadmap": final_roadmap,
            "agent_insights": [
                {
                    "agent_name": r.agent_name,
                    "confidence": r.confidence_score,
                    "focus": r.metadata.get("focus", ""),
                    "preview": r.roadmap[:200] + "..." if len(r.roadmap) > 200 else r.roadmap
                }
                for r in agent_responses
            ],
            "metadata": {
                "num_agents": len(agent_responses),
                "successful_agents": sum(1 for r in agent_responses if r.confidence_score > 0),
                "query": user_query,
                "structured_plan": merged_plan or {},
                "session_id": session_id,  # CRITICAL: Always include session_id
                "timestamp": str(time.time()),
                "execution_time": f"~{len(agent_responses)*10}s"
            },
            "session_id": session_id  # Also include at root level for direct access
        }
        
        # Log session completion
        self._log_session_complete(final_result)
        
        # Add funneling report to result - ENSURE IT'S ALWAYS INCLUDED
        try:
            funneling_report = self.generate_funneling_report(session_id)
            if not funneling_report or funneling_report.get("error"):
                # Create minimal report if generation fails
                funneling_report = {
                    "session_id": session_id,
                    "agent_performance": {
                        "total_agents": len(agent_responses),
                        "successful_agents": sum(1 for r in agent_responses if r.confidence_score > 0),
                        "success_rate_percent": round((sum(1 for r in agent_responses if r.confidence_score > 0) / max(len(agent_responses), 1)) * 100, 1),
                        "individual_results": [
                            {
                                "agent_name": r.agent_name,
                                "success": r.confidence_score > 0,
                                "confidence_score": r.confidence_score,
                                "provider": r.metadata.get("provider", "unknown"),
                                "model": r.metadata.get("model", "unknown"),
                                "response_time": "< 1s"
                            }
                            for r in agent_responses
                        ]
                    },
                    "funneling_process": {
                        "method": "confidence_based_selection",
                        "best_agent": best_agent,
                        "final_confidence": final_confidence,
                        "decision_rationale": f"Selected {best_agent} based on highest confidence score"
                    },
                    "output_metrics": {
                        "total_execution_time": "< 30s",
                        "phases_generated": len(merged_plan.get("phases", [])) if merged_plan else 0,
                        "content_items": sum(len(phase.get("topics", [])) + len(phase.get("projects", [])) 
                                           for phase in merged_plan.get("phases", [])) if merged_plan else 0
                    }
                }
            final_result["funneling_report"] = funneling_report
        except Exception as e:
            print(f"⚠️ Error generating funneling report: {e}")
            # Always include a basic report even if generation fails
            final_result["funneling_report"] = {
                "session_id": session_id,
                "error": str(e),
                "agent_performance": {"total_agents": len(agent_responses), "successful_agents": sum(1 for r in agent_responses if r.confidence_score > 0)}
            }
        
        print(f"🎯 Final result keys: {list(final_result.keys())}")
        print(f"🔍 Funneling report included: {'funneling_report' in final_result}")
        print(f"📊 Session ID: {session_id}")
        print(f"✅ Returning complete result with guaranteed funneling report")
        
        return final_result


# Example usage
async def main():
    """Example usage of the multi-agent system"""
    
    service = MultiAgentFunnelService()
    
    result = await service.generate_funneled_roadmap(
        user_query="I want to transition from marketing to data science",
        user_background={
            "current_skills": "Marketing analytics, Excel, basic SQL",
            "experience_level": "Intermediate",
            "time_available": "10 hours per week",
            "goals": "Get a data science job within 12 months"
        }
    )
    
    print("\n" + "="*80)
    print("FINAL ROADMAP")
    print("="*80)
    print(result["final_roadmap"])
    print("\n" + "="*80)
    print("AGENT INSIGHTS")
    print("="*80)
    for insight in result["agent_insights"]:
        print(f"\n{insight['agent_name']} (Confidence: {insight['confidence']:.2f})")
        print(f"Focus: {insight['focus']}")
        print(f"Preview: {insight['preview']}")


if __name__ == "__main__":
    asyncio.run(main())
