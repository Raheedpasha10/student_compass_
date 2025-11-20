"""
Unit tests for auth routes
"""
import pytest
from unittest.mock import Mock, patch, AsyncMock
from fastapi import HTTPException, status
from datetime import datetime

from routes.auth import router
from models.schemas import UserCreate, UserLogin, UserUpdate, User, Token
from services.mock_user_service import user_service
from services.auth_service import auth_service


class TestAuthRoutes:
    """Test cases for authentication routes"""

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_register_success(self, client, sample_user_data):
        """Test successful user registration"""
        # Mock user service
        mock_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name=sample_user_data["full_name"],
            skills=sample_user_data["skills"],
            expertise=sample_user_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch.object(user_service, 'create_user', return_value=mock_user):
            response = client.post("/auth/register", json=sample_user_data)

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["email"] == sample_user_data["email"]
        assert data["user"]["full_name"] == sample_user_data["full_name"]

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_register_duplicate_email(self, client, sample_user_data):
        """Test registration with duplicate email"""
        with patch.object(user_service, 'create_user', side_effect=Exception("User with this email already exists")):
            response = client.post("/auth/register", json=sample_user_data)

        assert response.status_code == 400
        assert "User with this email already exists" in response.json()["detail"]

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_register_invalid_data(self, client):
        """Test registration with invalid data"""
        invalid_data = {
            "email": "invalid_email",  # Invalid email format
            "password": "123",  # Too short
            "full_name": ""  # Empty name
        }

        response = client.post("/auth/register", json=invalid_data)
        assert response.status_code == 422  # Validation error

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_login_success(self, client, sample_user_data):
        """Test successful user login"""
        mock_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name=sample_user_data["full_name"],
            skills=sample_user_data["skills"],
            expertise=sample_user_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        login_data = {
            "email": sample_user_data["email"],
            "password": sample_user_data["password"]
        }

        with patch.object(user_service, 'authenticate_user', return_value=mock_user):
            response = client.post("/auth/login", json=login_data)

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["email"] == sample_user_data["email"]

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_login_invalid_credentials(self, client):
        """Test login with invalid credentials"""
        login_data = {
            "email": "wrong@example.com",
            "password": "wrongpassword"
        }

        with patch.object(user_service, 'authenticate_user', return_value=None):
            response = client.post("/auth/login", json=login_data)

        assert response.status_code == 401
        assert "Incorrect email or password" in response.json()["detail"]

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_login_missing_fields(self, client):
        """Test login with missing fields"""
        login_data = {
            "email": "test@example.com"
            # Missing password
        }

        response = client.post("/auth/login", json=login_data)
        assert response.status_code == 422  # Validation error

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_get_me_success(self, client, sample_user_data):
        """Test getting current user information"""
        mock_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name=sample_user_data["full_name"],
            skills=sample_user_data["skills"],
            expertise=sample_user_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        # Mock the dependency injection
        with patch('routes.auth.get_current_user_required', return_value=mock_user):
            # Create a valid token
            token = auth_service.create_access_token(data={"sub": mock_user.email})
            headers = {"Authorization": f"Bearer {token}"}

            response = client.get("/auth/me", headers=headers)

        assert response.status_code == 200
        data = response.json()
        assert data["email"] == sample_user_data["email"]
        assert data["full_name"] == sample_user_data["full_name"]

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_get_me_unauthorized(self, client):
        """Test getting current user without authentication"""
        response = client.get("/auth/me")
        assert response.status_code == 401

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_update_me_success(self, client, sample_user_data):
        """Test updating current user information"""
        mock_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name=sample_user_data["full_name"],
            skills=sample_user_data["skills"],
            expertise=sample_user_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        updated_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name="Updated Name",
            skills="Python, React, Node.js",
            expertise="Advanced",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        update_data = {
            "full_name": "Updated Name",
            "skills": "Python, React, Node.js",
            "expertise": "Advanced"
        }

        with patch('routes.auth.get_current_user_required', return_value=mock_user), \
             patch.object(user_service, 'update_user', return_value=updated_user):

            token = auth_service.create_access_token(data={"sub": mock_user.email})
            headers = {"Authorization": f"Bearer {token}"}

            response = client.put("/auth/me", json=update_data, headers=headers)

        assert response.status_code == 200
        data = response.json()
        assert data["full_name"] == "Updated Name"
        assert data["skills"] == "Python, React, Node.js"
        assert data["expertise"] == "Advanced"

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_update_me_failure(self, client, sample_user_data):
        """Test updating user information with failure"""
        mock_user = User(
            id="test_user_id",
            email=sample_user_data["email"],
            full_name=sample_user_data["full_name"],
            skills=sample_user_data["skills"],
            expertise=sample_user_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        update_data = {
            "full_name": "Updated Name"
        }

        with patch('routes.auth.get_current_user_required', return_value=mock_user), \
             patch.object(user_service, 'update_user', side_effect=Exception("Update failed")):

            token = auth_service.create_access_token(data={"sub": mock_user.email})
            headers = {"Authorization": f"Bearer {token}"}

            response = client.put("/auth/me", json=update_data, headers=headers)

        assert response.status_code == 400
        assert "Update failed" in response.json()["detail"]

    @pytest.mark.unit
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_update_me_unauthorized(self, client):
        """Test updating user without authentication"""
        update_data = {
            "full_name": "Updated Name"
        }

        response = client.put("/auth/me", json=update_data)
        assert response.status_code == 401

    @pytest.mark.unit
    @pytest.mark.auth
    def test_token_structure(self, sample_user_data):
        """Test token structure and validation"""
        # Create a token
        token_data = {"sub": sample_user_data["email"]}
        token = auth_service.create_access_token(token_data)

        # Verify token
        verified_token = auth_service.verify_token(token)

        assert verified_token is not None
        assert verified_token.email == sample_user_data["email"]
