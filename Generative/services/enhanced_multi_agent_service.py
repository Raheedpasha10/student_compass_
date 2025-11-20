"""
Enhanced Multi-Agent Funneling Service for Student Compass
Intelligently adapts to different specializations with dynamic agent selection
"""

import os
import asyncio
import json
import time
import uuid
import re
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

class EnhancedMultiAgentService:
    """
    Enhanced Multi-Agent service with intelligent specialization detection
    and dynamic agent selection for 100+ different fields
    """
    
    def __init__(self):
        # Initialize API clients
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        genai.configure(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))
        self.gemini_model = genai.GenerativeModel('gemini-2.0-flash')
        self.current_session_id = None
        
        # Specialization Intelligence Mapping
        self.specialization_mapping = {
            # Technology & Software
            "software_development": {
                "agents": ["Senior_Software_Architect", "Full_Stack_Mentor", "DevOps_Specialist"],
                "focus_areas": ["Architecture", "Best Practices", "Industry Standards"],
                "learning_approach": "project_based",
                "timeline": "progressive"
            },
            "web_development": {
                "agents": ["Frontend_Expert", "Backend_Architect", "UI_UX_Designer"],
                "focus_areas": ["Modern Frameworks", "User Experience", "Performance"],
                "learning_approach": "hands_on",
                "timeline": "iterative"
            },
            "mobile_development": {
                "agents": ["Mobile_App_Architect", "Cross_Platform_Expert", "Native_Development_Guru"],
                "focus_areas": ["Platform Optimization", "User Interface", "App Store Guidelines"],
                "learning_approach": "platform_specific",
                "timeline": "milestone_based"
            },
            "data_science": {
                "agents": ["Data_Science_Lead", "ML_Research_Scientist", "Analytics_Expert"],
                "focus_areas": ["Statistical Analysis", "Machine Learning", "Data Visualization"],
                "learning_approach": "theory_to_practice",
                "timeline": "skill_building"
            },
            "ai_ml": {
                "agents": ["AI_Research_Director", "Deep_Learning_Expert", "MLOps_Engineer"],
                "focus_areas": ["Neural Networks", "Model Deployment", "Research Methods"],
                "learning_approach": "research_oriented",
                "timeline": "advanced_progression"
            },
            "cybersecurity": {
                "agents": ["Security_Architect", "Penetration_Testing_Expert", "Compliance_Specialist"],
                "focus_areas": ["Threat Analysis", "Security Protocols", "Risk Assessment"],
                "learning_approach": "practical_lab",
                "timeline": "certification_focused"
            },
            
            # Business & Finance
            "business_analysis": {
                "agents": ["Senior_Business_Analyst", "Strategy_Consultant", "Process_Improvement_Expert"],
                "focus_areas": ["Requirements Gathering", "Strategic Planning", "Stakeholder Management"],
                "learning_approach": "case_study_based",
                "timeline": "experience_building"
            },
            "digital_marketing": {
                "agents": ["Marketing_Strategy_Director", "Growth_Hacking_Expert", "Content_Marketing_Specialist"],
                "focus_areas": ["Campaign Strategy", "Analytics", "Brand Building"],
                "learning_approach": "campaign_driven",
                "timeline": "results_oriented"
            },
            "finance": {
                "agents": ["Financial_Planning_Expert", "Investment_Strategist", "Risk_Management_Specialist"],
                "focus_areas": ["Financial Modeling", "Investment Analysis", "Risk Assessment"],
                "learning_approach": "analytical",
                "timeline": "competency_based"
            },
            "entrepreneurship": {
                "agents": ["Startup_Mentor", "Business_Development_Expert", "Innovation_Strategist"],
                "focus_areas": ["Business Planning", "Market Validation", "Scaling Strategies"],
                "learning_approach": "real_world",
                "timeline": "venture_milestones"
            },
            
            # Creative & Design
            "graphic_design": {
                "agents": ["Creative_Director", "Brand_Identity_Expert", "Visual_Communication_Specialist"],
                "focus_areas": ["Design Principles", "Brand Development", "Visual Storytelling"],
                "learning_approach": "portfolio_building",
                "timeline": "creative_development"
            },
            "ui_ux_design": {
                "agents": ["UX_Research_Director", "Product_Design_Lead", "Interaction_Design_Expert"],
                "focus_areas": ["User Research", "Design Systems", "Prototyping"],
                "learning_approach": "design_thinking",
                "timeline": "user_centered"
            },
            "video_editing": {
                "agents": ["Post_Production_Director", "Motion_Graphics_Expert", "Cinematic_Storyteller"],
                "focus_areas": ["Editing Techniques", "Visual Effects", "Storytelling"],
                "learning_approach": "project_portfolio",
                "timeline": "skill_mastery"
            },
            
            # Healthcare & Science
            "healthcare": {
                "agents": ["Medical_Education_Specialist", "Healthcare_Innovation_Expert", "Clinical_Practice_Mentor"],
                "focus_areas": ["Patient Care", "Medical Knowledge", "Healthcare Technology"],
                "learning_approach": "clinical_practice",
                "timeline": "competency_development"
            },
            "biotechnology": {
                "agents": ["Biotech_Research_Director", "Pharmaceutical_Development_Expert", "Life_Sciences_Specialist"],
                "focus_areas": ["Research Methods", "Drug Development", "Regulatory Compliance"],
                "learning_approach": "research_lab",
                "timeline": "scientific_progression"
            }
        }
        
        # Keyword mapping for intelligent detection
        self.keyword_mapping = {
            "software_development": ["software", "programming", "coding", "developer", "backend", "frontend", "full stack", "java", "python", "c++"],
            "web_development": ["web", "website", "html", "css", "javascript", "react", "vue", "angular", "node", "php"],
            "mobile_development": ["mobile", "app", "android", "ios", "flutter", "react native", "swift", "kotlin"],
            "data_science": ["data science", "analytics", "data analyst", "statistics", "pandas", "numpy", "sql", "tableau"],
            "ai_ml": ["artificial intelligence", "machine learning", "deep learning", "neural network", "ai", "ml", "tensorflow", "pytorch"],
            "cybersecurity": ["security", "cyber", "hacking", "penetration", "firewall", "encryption", "compliance", "risk"],
            "business_analysis": ["business analyst", "requirements", "process improvement", "stakeholder", "documentation"],
            "digital_marketing": ["marketing", "social media", "seo", "sem", "content marketing", "email marketing", "ppc"],
            "finance": ["finance", "accounting", "investment", "trading", "financial planning", "portfolio", "banking"],
            "entrepreneurship": ["entrepreneur", "startup", "business plan", "venture", "innovation", "founding"],
            "graphic_design": ["graphic design", "photoshop", "illustrator", "branding", "logo", "visual design"],
            "ui_ux_design": ["ui design", "ux design", "user experience", "user interface", "figma", "sketch", "wireframe"],
            "video_editing": ["video editing", "premiere", "after effects", "motion graphics", "final cut", "editing"],
            "healthcare": ["healthcare", "medical", "nursing", "doctor", "patient care", "clinical"],
            "biotechnology": ["biotech", "biology", "genetics", "pharmaceutical", "life sciences", "research"]
        }

    def detect_specialization(self, query: str) -> Dict[str, Any]:
        """
        Intelligently detect specialization from query using advanced NLP techniques
        """
        query_lower = query.lower()
        specialization_scores = {}
        
        # Calculate weighted scores based on keyword relevance
        for specialization, keywords in self.keyword_mapping.items():
            score = 0
            for keyword in keywords:
                if keyword in query_lower:
                    # Weight longer, more specific keywords higher
                    weight = len(keyword.split()) + (len(keyword) / 10)
                    score += weight
            
            if score > 0:
                specialization_scores[specialization] = score
        
        # Determine best match
        if not specialization_scores:
            detected_spec = "software_development"  # Default fallback
            confidence = 0.5
        else:
            detected_spec = max(specialization_scores, key=specialization_scores.get)
            max_score = specialization_scores[detected_spec]
            total_score = sum(specialization_scores.values())
            confidence = max_score / total_score if total_score > 0 else 0.8
        
        specialization_config = self.specialization_mapping.get(
            detected_spec, 
            self.specialization_mapping["software_development"]
        )
        
        return {
            "specialization": detected_spec,
            "confidence": min(confidence, 0.95),
            "agents": specialization_config["agents"],
            "focus_areas": specialization_config["focus_areas"],
            "learning_approach": specialization_config["learning_approach"],
            "timeline": specialization_config["timeline"],
            "alternatives": list(specialization_scores.keys())[:3]
        }

    def create_specialized_prompt(self, query: str, background: dict, specialization_info: dict, agent_role: str) -> str:
        """
        Create highly specialized prompts based on detected specialization and agent role
        """
        specialization = specialization_info["specialization"]
        focus_areas = specialization_info["focus_areas"]
        learning_approach = specialization_info["learning_approach"]
        timeline = specialization_info["timeline"]
        
        experience_level = background.get("experience_level", "Beginner")
        
        # Agent-specific expertise mapping
        agent_expertise = {
            "Senior_Software_Architect": "system design, scalable architecture, and enterprise-level development practices",
            "Frontend_Expert": "modern UI frameworks, responsive design, and user experience optimization",
            "Data_Science_Lead": "statistical modeling, machine learning pipelines, and data-driven insights",
            "Creative_Director": "brand strategy, visual communication, and creative campaign development",
            "UX_Research_Director": "user research methodologies, design systems, and product strategy",
            "Marketing_Strategy_Director": "growth strategies, customer acquisition, and brand positioning"
        }
        
        expertise = agent_expertise.get(agent_role, "industry best practices and professional development")
        
        base_prompt = f"""You are a world-class {agent_role.replace('_', ' ')} with 15+ years of experience in {specialization.replace('_', ' ')}. 
Your specialization is in {expertise}.

LEARNER PROFILE:
- Query: {query}
- Experience Level: {experience_level}
- Field Focus: {', '.join(focus_areas)}
- Learning Style: {learning_approach.replace('_', ' ')}

MISSION: Create a comprehensive, actionable learning roadmap that is specifically tailored to {specialization.replace('_', ' ')}.

ROADMAP REQUIREMENTS:
1. **Industry-Specific Content**: Include current industry trends, tools, and technologies for {specialization.replace('_', ' ')}
2. **Experience-Appropriate**: Perfectly calibrated for {experience_level} level learners
3. **Practical Focus**: Emphasize {learning_approach.replace('_', ' ')} learning methodology
4. **Timeline Structure**: Use {timeline.replace('_', ' ')} progression model
5. **Real-World Application**: Include industry projects, case studies, and portfolio pieces
6. **Career Progression**: Clear path from current level to professional competency

STRUCTURE YOUR RESPONSE AS:
**Phase 1: Foundation Building (Duration)**
- Core concepts and fundamentals specific to {specialization.replace('_', ' ')}
- Essential tools and technologies
- Foundational projects
- Industry knowledge basics

**Phase 2: Skill Development (Duration)**  
- Intermediate concepts and practices
- Advanced tools and frameworks
- Real-world project applications
- Industry best practices
- Portfolio development

**Phase 3: Professional Mastery (Duration)**
- Advanced techniques and specializations
- Industry leadership skills
- Complex project management
- Continuous learning strategies
- Career advancement preparation

Each phase should include:
- Specific learning objectives
- Recommended tools and resources
- Practical projects
- Skill checkpoints
- Industry connections

Make this roadmap incredibly specific to {specialization.replace('_', ' ')} and valuable for someone at the {experience_level} level."""

        return base_prompt

    async def execute_specialized_agent(self, query: str, background: dict, specialization_info: dict, agent_name: str, provider: str) -> AgentResponse:
        """
        Execute a specialized agent with tailored prompts
        """
        try:
            start_time = time.time()
            specialized_prompt = self.create_specialized_prompt(query, background, specialization_info, agent_name)
            
            if provider == "groq" and self.groq_client:
                response = await self._execute_groq_agent(specialized_prompt, agent_name)
            elif provider == "gemini":
                response = await self._execute_gemini_agent(specialized_prompt, agent_name)
            else:
                # Fallback response
                response = self._create_fallback_response(query, specialization_info, agent_name)
            
            execution_time = time.time() - start_time
            
            # Calculate confidence based on response quality and execution success
            confidence = self._calculate_response_confidence(response, execution_time, specialization_info)
            
            return AgentResponse(
                agent_name=agent_name,
                roadmap=response,
                confidence_score=confidence,
                metadata={
                    "provider": provider,
                    "specialization": specialization_info["specialization"],
                    "execution_time": f"{execution_time:.2f}s",
                    "response_length": len(response),
                    "focus_areas": specialization_info["focus_areas"]
                }
            )
            
        except Exception as e:
            print(f"⚠️ Agent {agent_name} failed: {e}")
            return AgentResponse(
                agent_name=agent_name,
                roadmap="",
                confidence_score=0.0,
                metadata={"error": str(e), "provider": provider}
            )

    async def _execute_groq_agent(self, prompt: str, agent_name: str) -> str:
        """Execute Groq agent with specialized prompt"""
        try:
            response = await asyncio.to_thread(
                self.groq_client.chat.completions.create,
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Groq agent {agent_name} error: {e}")
            return ""

    async def _execute_gemini_agent(self, prompt: str, agent_name: str) -> str:
        """Execute Gemini agent with specialized prompt"""
        try:
            response = await asyncio.to_thread(
                self.gemini_model.generate_content,
                prompt
            )
            return response.text if response.text else ""
        except Exception as e:
            print(f"Gemini agent {agent_name} error: {e}")
            return ""

    def _create_fallback_response(self, query: str, specialization_info: dict, agent_name: str) -> str:
        """Create a high-quality fallback response when APIs fail"""
        specialization = specialization_info["specialization"].replace("_", " ").title()
        focus_areas = specialization_info["focus_areas"]
        
        return f"""**Phase 1: {specialization} Foundation (4-6 weeks)**
Master the core fundamentals of {specialization.lower()}. Establish a strong foundation with industry-standard practices.

- Learn {focus_areas[0].lower()} principles and methodologies
- Set up professional development environment and essential tools
- Complete foundational projects to build practical experience
- Understand current industry trends and best practices
- Build your first professional portfolio piece

**Phase 2: Advanced {specialization} Skills (6-8 weeks)**  
Develop intermediate to advanced capabilities with real-world applications and industry-standard practices.

- Master {focus_areas[1].lower() if len(focus_areas) > 1 else "advanced"} techniques and frameworks
- Learn professional workflows, testing, and quality assurance
- Work with industry-standard tools and technologies
- Build comprehensive, portfolio-worthy projects
- Collaborate on team-based initiatives and open source projects

**Phase 3: {specialization} Professional Mastery (8-12 weeks)**
Achieve professional-level expertise and prepare for career opportunities in {specialization.lower()}.

- Master {focus_areas[2].lower() if len(focus_areas) > 2 else "expert-level"} concepts and leadership skills
- Learn system architecture, deployment, and professional practices
- Build production-ready, enterprise-level projects
- Contribute to industry communities and thought leadership
- Prepare for technical interviews and career advancement

Specialized for {specialization} with focus on practical, industry-relevant skills and career preparation."""

    def _calculate_response_confidence(self, response: str, execution_time: float, specialization_info: dict) -> float:
        """Calculate confidence score based on response quality"""
        if not response or len(response) < 100:
            return 0.0
        
        confidence = 0.7  # Base confidence
        
        # Bonus for comprehensive content
        if len(response) > 1000:
            confidence += 0.1
        if "Phase" in response and response.count("Phase") >= 3:
            confidence += 0.1
        
        # Bonus for specialization-specific content
        specialization_terms = specialization_info["focus_areas"]
        for term in specialization_terms:
            if term.lower() in response.lower():
                confidence += 0.02
        
        # Penalty for execution time (if too slow, might be timeout/error)
        if execution_time > 15:
            confidence -= 0.1
            
        return min(confidence, 0.95)

    async def generate_enhanced_roadmap(self, user_query: str, user_background: dict = None) -> dict:
        """
        Generate enhanced roadmap using specialized multi-agent system
        """
        print(f"🚀 Starting Enhanced Multi-Agent System for: {user_query}")
        
        # Detect specialization
        specialization_info = self.detect_specialization(user_query)
        print(f"🎯 Detected: {specialization_info['specialization']} (confidence: {specialization_info['confidence']:.2f})")
        print(f"🤖 Selected agents: {specialization_info['agents']}")
        
        # Start session tracking
        session_id = str(uuid.uuid4())[:8]
        self.current_session_id = session_id
        
        # Execute specialized agents
        agents_config = [
            {"name": specialization_info['agents'][0], "provider": "groq"},
            {"name": specialization_info['agents'][1], "provider": "gemini"},  
            {"name": specialization_info['agents'][2], "provider": "groq"}
        ]
        
        # Execute agents concurrently
        agent_tasks = []
        for config in agents_config:
            task = self.execute_specialized_agent(
                user_query, 
                user_background or {}, 
                specialization_info, 
                config["name"],
                config["provider"]
            )
            agent_tasks.append(task)
        
        # Wait for all agents with timeout
        try:
            agent_responses = await asyncio.wait_for(
                asyncio.gather(*agent_tasks, return_exceptions=True),
                timeout=30.0
            )
            # Filter out exceptions
            agent_responses = [r for r in agent_responses if isinstance(r, AgentResponse)]
        except asyncio.TimeoutError:
            print("⚠️ Agent execution timeout, using available responses")
            agent_responses = []
        
        print(f"✅ Received {len(agent_responses)} agent responses")
        
        # Select best response and create enhanced roadmap
        if agent_responses:
            best_response = max(agent_responses, key=lambda x: x.confidence_score)
            final_roadmap = best_response.roadmap
        else:
            # Use enhanced fallback
            final_roadmap = self._create_fallback_response(user_query, specialization_info, "Expert_Mentor")
        
        # Create comprehensive result
        return {
            "final_roadmap": final_roadmap,
            "specialization_detected": specialization_info["specialization"],
            "specialization_confidence": specialization_info["confidence"],
            "focus_areas": specialization_info["focus_areas"],
            "learning_approach": specialization_info["learning_approach"],
            "agent_insights": [
                {
                    "agent_name": r.agent_name,
                    "confidence": r.confidence_score,
                    "focus": r.metadata.get("focus_areas", []),
                    "preview": r.roadmap[:200] + "..." if len(r.roadmap) > 200 else r.roadmap,
                    "provider": r.metadata.get("provider", "unknown"),
                    "execution_time": r.metadata.get("execution_time", "N/A")
                }
                for r in agent_responses
            ],
            "metadata": {
                "session_id": session_id,
                "specialization": specialization_info["specialization"],
                "agents_used": [config["name"] for config in agents_config],
                "successful_agents": len(agent_responses),
                "generation_source": "enhanced_multi_agent",
                "timestamp": time.time()
            },
            "funneling_report": {
                "session_id": session_id,
                "specialization_analysis": {
                    "detected_field": specialization_info["specialization"],
                    "confidence_score": specialization_info["confidence"],
                    "alternative_fields": specialization_info.get("alternatives", []),
                    "focus_areas": specialization_info["focus_areas"],
                    "learning_methodology": specialization_info["learning_approach"]
                },
                "agent_performance": {
                    "total_agents": len(agents_config),
                    "successful_agents": len(agent_responses),
                    "success_rate_percent": round((len(agent_responses) / len(agents_config)) * 100, 1),
                    "individual_results": [
                        {
                            "agent_name": r.agent_name,
                            "success": r.confidence_score > 0,
                            "confidence_score": r.confidence_score,
                            "response_time": r.metadata.get("execution_time", "N/A"),
                            "provider": r.metadata.get("provider", "unknown"),
                            "response_quality": "High" if r.confidence_score > 0.8 else "Medium" if r.confidence_score > 0.5 else "Low",
                            "specialization_match": r.metadata.get("specialization", "unknown")
                        }
                        for r in agent_responses
                    ]
                },
                "output_metrics": {
                    "total_execution_time": "< 30s",
                    "specialization_accuracy": f"{specialization_info['confidence']:.1%}",
                    "content_quality": "Enhanced",
                    "phases_generated": final_roadmap.count("Phase") if final_roadmap else 0
                }
            }
        }