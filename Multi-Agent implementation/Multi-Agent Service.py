"""
Multi-Agent Funneling Service for Student Compass
Uses 3 different AI agents to generate roadmaps, then funnels them into one optimal result
"""

import os
import asyncio
import json
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


class MultiAgentFunnelService:
    """
    Orchestrates multiple AI agents to generate roadmaps and funnels results
    """
    
    def __init__(self):
        # Initialize API clients
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        genai.configure(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))
        self.gemini_model = genai.GenerativeModel('gemini-pro')
        self.huggingface_token = os.getenv("HUGGINGFACE_API_TOKEN")
        
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
                "model": "gemini-pro",
                "focus": "actionable steps, resources, and hands-on learning"
            },
            "agent_technical": {
                "name": "Technical Expert",
                "provider": "groq",
                "model": "llama-3.1-8b-instant",
                "focus": "technical skills, tools, and technologies"
            }
        }
    
    async def generate_roadmap_with_agent(
        self, 
        agent_config: Dict[str, str], 
        user_query: str,
        user_background: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """Generate roadmap using a single agent"""
        
        # Create specialized prompt based on agent focus
        prompt = self._create_agent_prompt(
            agent_config["focus"], 
            user_query, 
            user_background
        )
        
        try:
            if agent_config["provider"] == "groq":
                response = await self._call_groq(agent_config["model"], prompt)
            elif agent_config["provider"] == "gemini":
                response = await self._call_gemini(prompt)
            elif agent_config["provider"] == "huggingface":
                response = await self._call_huggingface(agent_config["model"], prompt)
            else:
                raise ValueError(f"Unknown provider: {agent_config['provider']}")
            
            # Calculate confidence score based on response completeness
            confidence = self._calculate_confidence(response)
            
            return AgentResponse(
                agent_name=agent_config["name"],
                roadmap=response,
                confidence_score=confidence,
                metadata={
                    "provider": agent_config["provider"],
                    "model": agent_config["model"],
                    "focus": agent_config["focus"]
                }
            )
        
        except Exception as e:
            print(f"Error with {agent_config['name']}: {str(e)}")
            return AgentResponse(
                agent_name=agent_config["name"],
                roadmap="",
                confidence_score=0.0,
                metadata={"error": str(e)}
            )
    
    async def _call_groq(self, model: str, prompt: str) -> str:
        """Call Groq API"""
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
            temperature=0.7,
            max_tokens=2000
        )
        return chat_completion.choices[0].message.content
    
    async def _call_gemini(self, prompt: str) -> str:
        """Call Google Gemini API"""
        response = self.gemini_model.generate_content(prompt)
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
                        "max_new_tokens": 2000,
                        "temperature": 0.7
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
        """Create specialized prompt for each agent"""
        
        background_context = ""
        if user_background:
            background_context = f"""
User Background:
- Current Skills: {user_background.get('current_skills', 'N/A')}
- Experience Level: {user_background.get('experience_level', 'Beginner')}
- Time Available: {user_background.get('time_available', 'N/A')}
- Goals: {user_background.get('goals', 'N/A')}
"""
        
        return f"""
You are a specialized career advisor with expertise in {focus}.

User Query: {user_query}

{background_context}

Create a detailed learning roadmap focusing specifically on {focus}. 

Structure your response as follows:
1. Overview (2-3 sentences)
2. Phase-by-phase breakdown (3-6 phases)
   - For each phase:
     * Duration estimate
     * Key topics/skills
     * Specific learning objectives
     * Recommended resources
3. Success metrics
4. Pro tips

Focus on your area of expertise: {focus}. Be specific and actionable.
"""
    
    def _calculate_confidence(self, response: str) -> float:
        """Calculate confidence score based on response quality"""
        if not response:
            return 0.0
        
        # Simple heuristics for confidence
        score = 0.5  # base score
        
        # Check for structure indicators
        if "phase" in response.lower() or "step" in response.lower():
            score += 0.2
        if len(response) > 500:
            score += 0.1
        if "resource" in response.lower() or "recommendation" in response.lower():
            score += 0.1
        if any(word in response.lower() for word in ["month", "week", "day"]):
            score += 0.1
        
        return min(score, 1.0)
    
    async def funnel_roadmaps(
        self, 
        agent_responses: List[AgentResponse]
    ) -> str:
        """
        Funnel multiple agent responses into one optimal roadmap
        Uses the best-performing agent (Groq with Llama 3.3 70B) as the funneling agent
        """
        
        # Filter out failed responses
        valid_responses = [r for r in agent_responses if r.confidence_score > 0]
        
        if not valid_responses:
            return "Unable to generate roadmap. Please try again."
        
        # Prepare synthesis prompt
        synthesis_prompt = self._create_synthesis_prompt(valid_responses)
        
        # Use Groq's most powerful model for synthesis
        try:
            synthesized = await self._call_groq(
                "llama-3.3-70b-versatile",
                synthesis_prompt
            )
            return synthesized
        except Exception as e:
            print(f"Synthesis error: {str(e)}")
            # Fallback to highest confidence response
            best_response = max(valid_responses, key=lambda x: x.confidence_score)
            return best_response.roadmap
    
    def _create_synthesis_prompt(self, responses: List[AgentResponse]) -> str:
        """Create prompt for funneling/synthesis"""
        
        responses_text = "\n\n---\n\n".join([
            f"**{r.agent_name}** (Confidence: {r.confidence_score:.2f})\n"
            f"Focus: {r.metadata['focus']}\n\n{r.roadmap}"
            for r in responses
        ])
        
        return f"""
You are an expert career advisor synthesizing multiple perspectives into one optimal learning roadmap.

You have received {len(responses)} different roadmaps from specialized advisors:

{responses_text}

---

Your task: Create ONE comprehensive, well-structured learning roadmap that:
1. Combines the BEST elements from each advisor's perspective
2. Eliminates redundancy and contradictions
3. Maintains logical progression and clear phases
4. Includes specific, actionable steps
5. Provides realistic time estimates
6. Recommends concrete resources

Structure:
- Overview & Goals
- Complete Phase-by-Phase Roadmap (with durations)
- Resources & Tools
- Success Metrics
- Final Tips

Make it cohesive, practical, and motivating. Focus on quality over quantity.
"""
    
    async def generate_funneled_roadmap(
        self, 
        user_query: str,
        user_background: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Main method: Generate roadmap using multi-agent system
        Returns the final funneled result plus individual agent insights
        """
        
        print("🚀 Starting multi-agent roadmap generation...")
        
        # Generate roadmaps from all agents concurrently
        tasks = [
            self.generate_roadmap_with_agent(config, user_query, user_background)
            for config in self.agents.values()
        ]
        
        agent_responses = await asyncio.gather(*tasks)
        
        print(f"✅ Received {len(agent_responses)} agent responses")
        for response in agent_responses:
            print(f"  - {response.agent_name}: Confidence {response.confidence_score:.2f}")
        
        # Funnel into optimal roadmap
        print("🔄 Funneling responses into optimal roadmap...")
        final_roadmap = await self.funnel_roadmaps(agent_responses)
        
        print("✅ Final roadmap generated!")
        
        return {
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
                "query": user_query
            }
        }


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
