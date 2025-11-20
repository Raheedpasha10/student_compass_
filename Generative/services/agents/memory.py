"""
Memory management for AI agents - Conversation history and context persistence
"""
import json
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)


class AgentMemory:
    """
    Memory system for agents to maintain conversation context and user preferences
    """

    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize agent memory

        Args:
            storage_path: Optional path to store memory data (default: in-memory)
        """
        self.storage_path = storage_path
        self.memory_store: Dict[str, Dict[str, Any]] = {}

        if storage_path:
            self._load_memory()

    def _load_memory(self):
        """Load memory from storage"""
        try:
            if Path(self.storage_path).exists():
                with open(self.storage_path, 'r') as f:
                    self.memory_store = json.load(f)
                logger.info(f"Loaded memory from {self.storage_path}")
        except Exception as e:
            logger.warning(f"Failed to load memory: {e}")

    def _save_memory(self):
        """Save memory to storage"""
        if not self.storage_path:
            return

        try:
            Path(self.storage_path).parent.mkdir(parents=True, exist_ok=True)
            with open(self.storage_path, 'w') as f:
                json.dump(self.memory_store, f, indent=2, default=str)
        except Exception as e:
            logger.warning(f"Failed to save memory: {e}")

    def get_user_context(self, user_id: str) -> Dict[str, Any]:
        """
        Get user's conversation context and history

        Args:
            user_id: User identifier

        Returns:
            User context dictionary
        """
        if user_id not in self.memory_store:
            self.memory_store[user_id] = {
                "user_id": user_id,
                "conversations": [],
                "preferences": {},
                "skills_history": [],
                "career_interests": [],
                "learning_goals": [],
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }

        return self.memory_store[user_id]

    def save_conversation(
        self,
        user_id: str,
        skills: str,
        expertise: str,
        analysis_result: Dict[str, Any],
        timestamp: Optional[datetime] = None
    ):
        """
        Save a conversation/analysis session

        Args:
            user_id: User identifier
            skills: User skills
            expertise: User expertise level
            analysis_result: Analysis results from agents
            timestamp: Optional timestamp (default: now)
        """
        if timestamp is None:
            timestamp = datetime.now()

        user_context = self.get_user_context(user_id)

        conversation = {
            "timestamp": timestamp.isoformat(),
            "skills": skills,
            "expertise": expertise,
            "selected_career": analysis_result.get("selected_path", {}).get("title", ""),
            "career_paths": [path.get("title", "") for path in analysis_result.get("career_paths", [])],
            "roadmap_steps": len(analysis_result.get("roadmap", [])),
            "courses_count": len(analysis_result.get("courses", [])),
            "certifications_count": len(analysis_result.get("certifications", []))
        }

        user_context["conversations"].append(conversation)
        user_context["updated_at"] = datetime.now().isoformat()

        # Keep only last 50 conversations
        if len(user_context["conversations"]) > 50:
            user_context["conversations"] = user_context["conversations"][-50:]

        # Update skills history
        if skills:
            skills_list = [s.strip() for s in skills.split(",")]
            user_context["skills_history"].extend(skills_list)
            # Keep unique skills
            user_context["skills_history"] = list(set(user_context["skills_history"]))

        # Update career interests
        selected_career = analysis_result.get("selected_path", {}).get("title", "")
        if selected_career and selected_career not in user_context["career_interests"]:
            user_context["career_interests"].append(selected_career)
            # Keep last 10 interests
            user_context["career_interests"] = user_context["career_interests"][-10:]

        self._save_memory()

    def get_conversation_history(self, user_id: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Get user's conversation history

        Args:
            user_id: User identifier
            limit: Maximum number of conversations to return

        Returns:
            List of conversation dictionaries
        """
        user_context = self.get_user_context(user_id)
        return user_context["conversations"][-limit:]

    def update_preferences(self, user_id: str, preferences: Dict[str, Any]):
        """
        Update user preferences

        Args:
            user_id: User identifier
            preferences: Preferences dictionary
        """
        user_context = self.get_user_context(user_id)
        user_context["preferences"].update(preferences)
        user_context["updated_at"] = datetime.now().isoformat()
        self._save_memory()

    def get_preferences(self, user_id: str) -> Dict[str, Any]:
        """
        Get user preferences

        Args:
            user_id: User identifier

        Returns:
            Preferences dictionary
        """
        user_context = self.get_user_context(user_id)
        return user_context.get("preferences", {})

    def get_skills_evolution(self, user_id: str) -> List[str]:
        """
        Get user's skill evolution over time

        Args:
            user_id: User identifier

        Returns:
            List of unique skills
        """
        user_context = self.get_user_context(user_id)
        return user_context.get("skills_history", [])

    def get_career_progress(self, user_id: str) -> Dict[str, Any]:
        """
        Get user's career exploration progress

        Args:
            user_id: User identifier

        Returns:
            Career progress dictionary
        """
        user_context = self.get_user_context(user_id)
        conversations = user_context.get("conversations", [])

        if not conversations:
            return {
                "total_sessions": 0,
                "careers_explored": [],
                "most_common_career": None,
                "skills_growth": []
            }

        # Count career explorations
        career_counts = {}
        for conv in conversations:
            career = conv.get("selected_career", "")
            if career:
                career_counts[career] = career_counts.get(career, 0) + 1

        most_common_career = max(career_counts.items(), key=lambda x: x[1])[0] if career_counts else None

        return {
            "total_sessions": len(conversations),
            "careers_explored": list(career_counts.keys()),
            "most_common_career": most_common_career,
            "skills_growth": user_context.get("skills_history", [])
        }

    def get_context_for_agent(self, user_id: str) -> str:
        """
        Get formatted context string for agent prompts

        Args:
            user_id: User identifier

        Returns:
            Formatted context string
        """
        user_context = self.get_user_context(user_id)
        preferences = user_context.get("preferences", {})
        career_progress = self.get_career_progress(user_id)
        recent_conversations = self.get_conversation_history(user_id, limit=3)

        context_parts = []

        if preferences:
            context_parts.append(f"User Preferences: {json.dumps(preferences)}")

        if career_progress.get("total_sessions", 0) > 0:
            context_parts.append(f"Previous Sessions: {career_progress['total_sessions']} analysis sessions")
            if career_progress.get("most_common_career"):
                context_parts.append(f"Previously Interested In: {career_progress['most_common_career']}")

        if recent_conversations:
            last_conversation = recent_conversations[-1]
            context_parts.append(f"Last Analysis: {last_conversation.get('selected_career', 'N/A')} ({last_conversation.get('timestamp', '')})")

        if user_context.get("skills_history"):
            skills = user_context["skills_history"][-10:]  # Last 10 skills
            context_parts.append(f"Known Skills: {', '.join(skills)}")

        return "\n".join(context_parts) if context_parts else "No previous context available."


# Global memory instance (in-memory by default, can be configured with storage path)
memory = AgentMemory()

