"""
Global test configuration and fixtures for pytest
"""
import pytest
import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
import os
import sys

# Add the project root (Generative) to the Python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from main import app
from config.settings import settings
from services.mock_user_service import MockUserService

@pytest.fixture(scope="session")


def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture


def client():
    """Create a test client for the FastAPI app."""
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
async def async_client():
    """Create an async test client for the FastAPI app."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture


def mock_user_service():
    """Create a mock user service for testing."""
    return MockUserService()

@pytest.fixture


def sample_user_data():
    """Sample user data for testing."""
    return {
        "email": "test@example.com",
        "password": "testpassword123",
        "full_name": "Test User",
        "skills": "Python, JavaScript, React",
        "expertise": "Intermediate"
    }

@pytest.fixture


def sample_skills_data():
    """Sample skills data for testing."""
    return {
        "skills": "Python, Machine Learning, Data Analysis, React, JavaScript",
        "expertise": "Advanced"
    }

@pytest.fixture


def mock_ai_service():
    """Mock AI service responses."""
    # Patch to real function names in AIService
    with patch('services.ai_service.AIService.generate_career_analysis') as mock_analyze, \
         patch('services.ai_service.AIService.extract_skills_from_message') as mock_extract:

        # Mock career analysis response
        mock_analyze.return_value = {
            "career_paths": [
                {
                    "title": "Full Stack Developer",
                    "description": "Develop both frontend and backend applications",
                    "required_skills": ["Python", "JavaScript", "React", "SQL"],
                    "salary_range": "$70,000 - $120,000",
                    "growth_prospect": "High",
                    "market_demand": "Very High"
                },
                {
                    "title": "Data Scientist",
                    "description": "Analyze data to extract insights",
                    "required_skills": ["Python", "Machine Learning", "Statistics", "SQL"],
                    "salary_range": "$80,000 - $140,000",
                    "growth_prospect": "Very High",
                    "market_demand": "High"
                }
            ],
            "selected_path": {
                "title": "Full Stack Developer",
                "description": "Develop both frontend and backend applications",
                "required_skills": ["Python", "JavaScript", "React", "SQL"],
                "salary_range": "$70,000 - $120,000",
                "growth_prospect": "High",
                "market_demand": "Very High"
            },
            "roadmap": [
                {
                    "phase": "Foundation",
                    "duration": "1-2 months",
                    "topics": ["HTML/CSS Basics", "JavaScript Fundamentals"],
                    "resources": ["MDN Web Docs", "FreeCodeCamp"]
                }
            ],
            "courses": [
                {
                    "title": "Complete Web Development Bootcamp",
                    "provider": "Udemy",
                    "duration": "40 hours",
                    "level": "Beginner to Advanced"
                }
            ]
        }

        # Mock skill extraction response
        mock_extract.return_value = [
            {"skill": "React", "expertise_level": "Intermediate"},
            {"skill": "Node.js", "expertise_level": "Beginner"}
        ]

        yield {
            "analyze": mock_analyze,
            "extract": mock_extract
        }

@pytest.fixture


def mock_firestore():
    """Mock Firestore database operations."""
    with patch('services.user_service.db') as mock_db:
        mock_collection = Mock()
        mock_doc = Mock()
        mock_doc.get.return_value.exists = True
        mock_doc.get.return_value.to_dict.return_value = {
            "id": "test_user_id",
            "email": "test@example.com",
            "full_name": "Test User",
            "skills": "Python, JavaScript",
            "expertise": "Intermediate",
            "created_at": "2023-01-01T00:00:00"
        }
        mock_collection.document.return_value = mock_doc
        mock_db.collection.return_value = mock_collection
        yield mock_db

@pytest.fixture(autouse=True)


def reset_mocks():
    """Reset all mocks after each test."""
    yield
    # Any cleanup code can go here

# Mark slow tests


def pytest_collection_modifyitems(config, items):
    """Add slow marker to integration tests."""
    for item in items:
        if "integration" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
