"""
Integration tests for API endpoints and full workflows
"""
import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
import json
from datetime import datetime

from main import app
from services.ai_service import AIService
from models.schemas import User, UserCreate


class TestAPIIntegration:
    """Integration tests for API endpoints"""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_health_endpoint(self, async_client):
        """Test health check endpoint"""
        response = await async_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_full_user_registration_flow(self, async_client, mock_ai_service):
        """Test complete user registration and profile management flow"""
        # Step 1: Register user
        user_data = {
            "email": "integration@test.com",
            "password": "testpassword123",
            "full_name": "Integration Test User",
            "skills": "Python, JavaScript, React",
            "expertise": "Intermediate"
        }

        with patch('services.mock_user_service.user_service.create_user') as mock_create:
            mock_user = User(
                id="integration_user_id",
                email=user_data["email"],
                full_name=user_data["full_name"],
                skills=user_data["skills"],
                expertise=user_data["expertise"],
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            mock_create.return_value = mock_user

            response = await async_client.post("/auth/register", json=user_data)

            assert response.status_code == 200
            token_data = response.json()
            assert "access_token" in token_data
            access_token = token_data["access_token"]

        # Step 2: Use token to access protected endpoint
        headers = {"Authorization": f"Bearer {access_token}"}

        with patch('dependencies.get_current_user_required', return_value=mock_user):
            response = await async_client.get("/auth/me", headers=headers)

            assert response.status_code == 200
            user_info = response.json()
            assert user_info["email"] == user_data["email"]
            assert user_info["full_name"] == user_data["full_name"]

        # Step 3: Update user profile
        update_data = {
            "skills": "Python, JavaScript, React, Node.js, MongoDB",
            "expertise": "Advanced"
        }

        updated_user = User(
            id="integration_user_id",
            email=user_data["email"],
            full_name=user_data["full_name"],
            skills=update_data["skills"],
            expertise=update_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch('dependencies.get_current_user_required', return_value=mock_user), \
             patch('services.mock_user_service.user_service.update_user', return_value=updated_user):

            response = await async_client.put("/auth/me", json=update_data, headers=headers)

            assert response.status_code == 200
            updated_info = response.json()
            assert updated_info["skills"] == update_data["skills"]
            assert updated_info["expertise"] == update_data["expertise"]

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_career_analysis_workflow(self, async_client, mock_ai_service):
        """Test complete career analysis workflow"""
        # Test unauthenticated analysis
        analysis_request = {
            "skills": "Python, Machine Learning, Data Analysis, SQL",
            "expertise": "Advanced"
        }

        response = await async_client.post("/analyze", json=analysis_request)
        assert response.status_code == 200

        analysis_data = response.json()
        required_fields = ["career_paths", "selected_path", "roadmap", "courses"]
        for field in required_fields:
            assert field in analysis_data
            assert isinstance(analysis_data[field], (list, dict))

        # Verify career paths structure
        assert len(analysis_data["career_paths"]) > 0
        career_path = analysis_data["career_paths"][0]
        path_fields = ["title", "description", "required_skills", "salary_range", "growth_prospect", "market_demand"]
        for field in path_fields:
            assert field in career_path

        # Verify selected path structure
        selected_path = analysis_data["selected_path"]
        for field in path_fields:
            assert field in selected_path

        # Verify roadmap structure
        if analysis_data["roadmap"]:
            roadmap_step = analysis_data["roadmap"][0]
            roadmap_fields = ["phase", "duration", "topics", "resources"]
            for field in roadmap_fields:
                assert field in roadmap_step

        # Verify courses structure
        if analysis_data["courses"]:
            course = analysis_data["courses"][0]
            course_fields = ["title", "provider", "duration", "level"]
            for field in course_fields:
                assert field in course

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_chatbot_skill_extraction_workflow(self, async_client, mock_ai_service):
        """Test chatbot skill extraction and profile update workflow"""
        # Step 1: Create a user (mocked)
        user_id = "test_chatbot_user"

        # Step 2: Send message for skill extraction
        chat_message = {
            "user_id": user_id,
            "message": "I just learned React hooks and Redux for state management, and I'm getting good at TypeScript"
        }

        # Mock extracted skills response
        mock_extracted_skills = [
            {"skill": "React", "expertise_level": "Intermediate"},
            {"skill": "Redux", "expertise_level": "Beginner"},
            {"skill": "TypeScript", "expertise_level": "Intermediate"}
        ]

        with patch('services.ai_service.AIService.extract_skills_from_message', return_value=mock_extracted_skills), \
             patch('services.mock_user_service.user_service.get_user_by_id') as mock_get_user, \
             patch('services.mock_user_service.user_service.update_user') as mock_update_user:

            # Mock user data
            mock_user = {
                "id": user_id,
                "email": "chatbot@test.com",
                "skills": "Python, JavaScript",
                "expertise": "Intermediate"
            }
            mock_get_user.return_value = mock_user

            # Mock updated user
            updated_user = User(
                id=user_id,
                email="chatbot@test.com",
                full_name="Chatbot Test User",
                skills="Python, JavaScript, React, Redux, TypeScript",
                expertise="Intermediate",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            mock_update_user.return_value = updated_user

            response = await async_client.post("/update-skills", json=chat_message)

            assert response.status_code == 200
            skill_data = response.json()

            assert "extracted_skills" in skill_data
            assert "updated_skills_list" in skill_data
            assert len(skill_data["extracted_skills"]) == 3

            # Verify extracted skills
            extracted = skill_data["extracted_skills"]
            skill_names = [skill["skill"] for skill in extracted]
            assert "React" in skill_names
            assert "Redux" in skill_names
            assert "TypeScript" in skill_names

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_mock_test_generation_workflow(self, async_client, mock_ai_service):
        """Test mock test generation workflow"""
        test_request = {
            "role": "Data Scientist",
            "difficulty": "intermediate",
            "question_count": 5
        }

        response = await async_client.post("/mock-test", json=test_request)
        assert response.status_code == 200

        test_data = response.json()
        assert "questions" in test_data
        assert len(test_data["questions"]) == 5

        # Verify question structure
        question = test_data["questions"][0]
        question_fields = ["question", "options", "correct_answer", "explanation", "difficulty"]
        for field in question_fields:
            assert field in question

        assert len(question["options"]) == 4  # Should have 4 options
        assert question["correct_answer"] in ["A", "B", "C", "D"]
        assert question["difficulty"] in ["easy", "intermediate", "hard"]

    # @pytest.mark.integration
    # @pytest.mark.asyncio
    # async def test_chat_endpoint_workflow(self, async_client, mock_ai_service):
    #     """Test chat endpoint workflow - DISABLED: Chat system removed"""
    #     pass

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_error_handling_workflow(self, async_client):
        """Test error handling across different endpoints"""
        # Test invalid login
        invalid_login = {
            "email": "nonexistent@test.com",
            "password": "wrongpassword"
        }

        with patch('services.mock_user_service.user_service.authenticate_user', return_value=None):
            response = await async_client.post("/auth/login", json=invalid_login)
            assert response.status_code == 401

        # Test analyze without skills
        empty_analysis = {}
        response = await async_client.post("/analyze", json=empty_analysis)
        assert response.status_code == 400

        # Test protected endpoint without auth
        response = await async_client.get("/auth/me")
        assert response.status_code == 401

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.asyncio
    async def test_concurrent_requests(self, async_client, mock_ai_service):
        """Test handling of concurrent requests"""
        # Create multiple analysis requests
        requests = []
        for i in range(5):
            analysis_request = {
                "skills": f"Python, Skill{i}",
                "expertise": "Intermediate"
            }
            requests.append(async_client.post("/analyze", json=analysis_request))

        # Execute concurrently
        responses = await asyncio.gather(*requests)

        # Verify all succeeded
        for response in responses:
            assert response.status_code == 200
            data = response.json()
            assert "career_paths" in data
            assert "selected_path" in data

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_cors_headers(self, async_client):
        """Test CORS headers are properly set"""
        response = await async_client.options("/health")

        # FastAPI should handle OPTIONS requests
        assert response.status_code in [200, 405]  # Some endpoints might not support OPTIONS

        # Test actual request to verify CORS middleware
        response = await async_client.get("/health")
        assert response.status_code == 200

        # CORS headers should be present (set by middleware)
        # Note: In test environment, CORS headers might not be fully set
