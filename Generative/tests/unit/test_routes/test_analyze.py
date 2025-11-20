"""
Unit tests for analyze routes
"""
import pytest
from unittest.mock import Mock, patch, AsyncMock
from fastapi import HTTPException

from routes.analyze import router, ai_service
from models.schemas import AnalyzeRequest, AnalyzeResponse, CareerPath, RoadmapStep, Course, User


class TestAnalyzeRoutes:
    """Test cases for analyze routes"""

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_career_paths_with_request_data(self, client, mock_ai_service):
        """Test career analysis with data in request"""
        request_data = {
            "skills": "Python, Machine Learning, Data Analysis",
            "expertise": "Advanced"
        }

        # Mock AI service response
        mock_analysis = {
            "career_paths": [
                {
                    "title": "Data Scientist",
                    "description": "Analyze data to extract insights",
                    "required_skills": ["Python", "Machine Learning", "Statistics"],
                    "salary_range": "$80,000 - $140,000",
                    "growth_prospect": "Very High",
                    "market_demand": "High"
                }
            ],
            "selected_path": {
                "title": "Data Scientist",
                "description": "Analyze data to extract insights",
                "required_skills": ["Python", "Machine Learning", "Statistics"],
                "salary_range": "$80,000 - $140,000",
                "growth_prospect": "Very High",
                "market_demand": "High"
            },
            "roadmap": [
                {
                    "phase": "Foundation",
                    "duration": "1-2 months",
                    "topics": ["Statistics Basics", "Python for Data Science"],
                    "resources": ["Python.org", "Coursera"]
                }
            ],
            "courses": [
                {
                    "title": "Data Science Bootcamp",
                    "provider": "Udemy",
                    "duration": "50 hours",
                    "level": "Intermediate to Advanced"
                }
            ]
        }

        with patch.object(ai_service, 'generate_career_analysis', return_value=mock_analysis):
            response = client.post("/analyze", json=request_data)

        assert response.status_code == 200
        data = response.json()

        assert "career_paths" in data
        assert "selected_path" in data
        assert "roadmap" in data
        assert "courses" in data

        assert len(data["career_paths"]) == 1
        assert data["career_paths"][0]["title"] == "Data Scientist"
        assert data["selected_path"]["title"] == "Data Scientist"
        assert len(data["roadmap"]) == 1
        assert len(data["courses"]) == 1

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_career_paths_with_user_profile(self, client, mock_ai_service, sample_user_data):
        """Test career analysis using authenticated user's profile"""
        # Mock authenticated user
        mock_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name=sample_user_data["full_name"],
            skills=sample_user_data["skills"],
            expertise=sample_user_data["expertise"],
            created_at=None,
            updated_at=None
        )

        # Request without skills/expertise (should use user profile)
        request_data = {}

        mock_analysis = {
            "career_paths": [
                {
                    "title": "Full Stack Developer",
                    "description": "Develop both frontend and backend applications",
                    "required_skills": ["Python", "JavaScript", "React"],
                    "salary_range": "$70,000 - $120,000",
                    "growth_prospect": "High",
                    "market_demand": "Very High"
                }
            ],
            "selected_path": {
                "title": "Full Stack Developer",
                "description": "Develop both frontend and backend applications",
                "required_skills": ["Python", "JavaScript", "React"],
                "salary_range": "$70,000 - $120,000",
                "growth_prospect": "High",
                "market_demand": "Very High"
            },
            "roadmap": [
                {
                    "phase": "Frontend Basics",
                    "duration": "2-3 months",
                    "topics": ["HTML/CSS", "JavaScript", "React"],
                    "resources": ["MDN", "React Docs"]
                }
            ],
            "courses": [
                {
                    "title": "Full Stack Web Development",
                    "provider": "FreeCodeCamp",
                    "duration": "300 hours",
                    "level": "Beginner to Advanced"
                }
            ]
        }

        with patch('routes.analyze.get_current_user', return_value=mock_user), \
             patch.object(ai_service, 'generate_career_analysis', return_value=mock_analysis) as mock_generate:

            response = client.post("/analyze", json=request_data)

        assert response.status_code == 200

        # Verify AI service was called with user's profile data
        mock_generate.assert_called_once_with(
            sample_user_data["skills"],
            sample_user_data["expertise"]
        )

        data = response.json()
        assert data["selected_path"]["title"] == "Full Stack Developer"

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_missing_skills_and_expertise(self, client):
        """Test career analysis with missing skills and expertise"""
        request_data = {}  # No skills or expertise

        # Mock no authenticated user
        with patch('routes.analyze.get_current_user', return_value=None):
            response = client.post("/analyze", json=request_data)

        assert response.status_code == 400
        assert "Skills and expertise are required" in response.json()["detail"]

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_request_data_overrides_user_profile(self, client, mock_ai_service, sample_user_data):
        """Test that request data takes precedence over user profile"""
        # Mock authenticated user
        mock_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name=sample_user_data["full_name"],
            skills="Old Skills",  # Different from request
            expertise="Beginner",  # Different from request
            created_at=None,
            updated_at=None
        )

        # Request with specific skills/expertise
        request_data = {
            "skills": "New Skills, Advanced Techniques",
            "expertise": "Expert"
        }

        mock_analysis = {
            "career_paths": [{"title": "Expert Developer", "description": "Expert level development", "required_skills": [], "salary_range": "$100k+", "growth_prospect": "High", "market_demand": "High"}],
            "selected_path": {"title": "Expert Developer", "description": "Expert level development", "required_skills": [], "salary_range": "$100k+", "growth_prospect": "High", "market_demand": "High"},
            "roadmap": [{"phase": "Advanced", "duration": "1 month", "topics": [], "resources": []}],
            "courses": [{"title": "Advanced Course", "provider": "Expert Academy", "duration": "20 hours", "level": "Expert"}]
        }

        with patch('routes.analyze.get_current_user', return_value=mock_user), \
             patch.object(ai_service, 'generate_career_analysis', return_value=mock_analysis) as mock_generate:

            response = client.post("/analyze", json=request_data)

        assert response.status_code == 200

        # Verify AI service was called with request data, not user profile
        mock_generate.assert_called_once_with(
            "New Skills, Advanced Techniques",
            "Expert"
        )

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_ai_service_error(self, client):
        """Test career analysis when AI service fails"""
        request_data = {
            "skills": "Python, JavaScript",
            "expertise": "Intermediate"
        }

        # Mock AI service failure
        with patch.object(ai_service, 'generate_career_analysis', side_effect=Exception("AI service unavailable")):
            response = client.post("/analyze", json=request_data)

        assert response.status_code == 500
        assert "Error analyzing career paths" in response.json()["detail"]
        assert "AI service unavailable" in response.json()["detail"]

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_partial_skills_from_user(self, client, mock_ai_service):
        """Test analysis with skills from request and expertise from user"""
        mock_user = User(
            id="test_user_id",
            email="test@example.com",
            full_name="Test User",
            skills="",  # Empty skills in profile
            expertise="Advanced",  # Has expertise
            created_at=None,
            updated_at=None
        )

        request_data = {
            "skills": "Python, Machine Learning"
            # No expertise in request
        }

        mock_analysis = {
            "career_paths": [{"title": "ML Engineer", "description": "ML development", "required_skills": [], "salary_range": "$90k+", "growth_prospect": "High", "market_demand": "High"}],
            "selected_path": {"title": "ML Engineer", "description": "ML development", "required_skills": [], "salary_range": "$90k+", "growth_prospect": "High", "market_demand": "High"},
            "roadmap": [{"phase": "ML Basics", "duration": "2 months", "topics": [], "resources": []}],
            "courses": [{"title": "ML Course", "provider": "ML Academy", "duration": "40 hours", "level": "Advanced"}]
        }

        with patch('routes.analyze.get_current_user', return_value=mock_user), \
             patch.object(ai_service, 'generate_career_analysis', return_value=mock_analysis) as mock_generate:

            response = client.post("/analyze", json=request_data)

        assert response.status_code == 200

        # Should use skills from request and expertise from user
        mock_generate.assert_called_once_with(
            "Python, Machine Learning",
            "Advanced"
        )

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_empty_strings_validation(self, client):
        """Test analysis with empty string values"""
        request_data = {
            "skills": "",
            "expertise": ""
        }

        with patch('routes.analyze.get_current_user', return_value=None):
            response = client.post("/analyze", json=request_data)

        assert response.status_code == 400
        assert "Skills and expertise are required" in response.json()["detail"]

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_analyze_response_model_validation(self, client, mock_ai_service):
        """Test that response is properly validated against Pydantic models"""
        request_data = {
            "skills": "Python",
            "expertise": "Beginner"
        }

        # Mock incomplete AI response (missing required fields)
        incomplete_analysis = {
            "career_paths": [
                {
                    "title": "Developer",
                    # Missing required fields
                }
            ],
            "selected_path": {
                "title": "Developer",
                # Missing required fields
            },
            "roadmap": [],
            "courses": []
        }

        with patch.object(ai_service, 'generate_career_analysis', return_value=incomplete_analysis):
            response = client.post("/analyze", json=request_data)

        # Should return 500 due to validation error when creating Pydantic models
        assert response.status_code == 500
        assert "Error analyzing career paths" in response.json()["detail"]
