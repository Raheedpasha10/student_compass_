"""
Integration tests for authentication flow
"""
import pytest
from httpx import AsyncClient
from unittest.mock import patch, Mock
from datetime import datetime, timedelta

from main import app
from models.schemas import User
from services.auth_service import auth_service


class TestAuthFlow:
    """Integration tests for authentication flow"""

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_complete_auth_flow(self, async_client):
        """Test complete authentication flow from registration to profile access"""

        # Step 1: Register new user
        registration_data = {
            "email": "authflow@test.com",
            "password": "securepassword123",
            "full_name": "Auth Flow Test User",
            "skills": "Python, Django, PostgreSQL",
            "expertise": "Advanced"
        }

        mock_user = User(
            id="auth_flow_user_id",
            email=registration_data["email"],
            full_name=registration_data["full_name"],
            skills=registration_data["skills"],
            expertise=registration_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch('services.mock_user_service.user_service.create_user', return_value=mock_user):
            registration_response = await async_client.post("/auth/register", json=registration_data)

            assert registration_response.status_code == 200
            registration_result = registration_response.json()

            # Verify registration response
            assert "access_token" in registration_result
            assert registration_result["token_type"] == "bearer"
            assert registration_result["user"]["email"] == registration_data["email"]

            access_token = registration_result["access_token"]

        # Step 2: Login with same credentials
        login_data = {
            "email": registration_data["email"],
            "password": registration_data["password"]
        }

        with patch('services.mock_user_service.user_service.authenticate_user', return_value=mock_user):
            login_response = await async_client.post("/auth/login", json=login_data)

            assert login_response.status_code == 200
            login_result = login_response.json()

            # Verify login response
            assert "access_token" in login_result
            assert login_result["token_type"] == "bearer"
            assert login_result["user"]["email"] == registration_data["email"]

            login_token = login_result["access_token"]

        # Step 3: Access protected endpoint with token
        headers = {"Authorization": f"Bearer {access_token}"}

        with patch('dependencies.get_current_user_required', return_value=mock_user):
            profile_response = await async_client.get("/auth/me", headers=headers)

            assert profile_response.status_code == 200
            profile_data = profile_response.json()

            # Verify profile data
            assert profile_data["email"] == registration_data["email"]
            assert profile_data["full_name"] == registration_data["full_name"]
            assert profile_data["skills"] == registration_data["skills"]
            assert profile_data["expertise"] == registration_data["expertise"]

        # Step 4: Update profile
        update_data = {
            "full_name": "Updated Auth Flow User",
            "skills": "Python, Django, PostgreSQL, Redis, Docker",
            "expertise": "Expert"
        }

        updated_user = User(
            id="auth_flow_user_id",
            email=registration_data["email"],
            full_name=update_data["full_name"],
            skills=update_data["skills"],
            expertise=update_data["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch('dependencies.get_current_user_required', return_value=mock_user), \
             patch('services.mock_user_service.user_service.update_user', return_value=updated_user):

            update_response = await async_client.put("/auth/me", json=update_data, headers=headers)

            assert update_response.status_code == 200
            update_result = update_response.json()

            # Verify update
            assert update_result["full_name"] == update_data["full_name"]
            assert update_result["skills"] == update_data["skills"]
            assert update_result["expertise"] == update_data["expertise"]

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_token_expiration_handling(self, async_client):
        """Test handling of expired tokens"""

        # Create expired token
        expired_token_data = {"sub": "test@example.com"}
        expired_token = auth_service.create_access_token(
            expired_token_data,
            expires_delta=timedelta(seconds=-1)  # Already expired
        )

        headers = {"Authorization": f"Bearer {expired_token}"}

        # Try to access protected endpoint with expired token
        response = await async_client.get("/auth/me", headers=headers)

        # Should return 401 Unauthorized
        assert response.status_code == 401

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_invalid_token_handling(self, async_client):
        """Test handling of invalid tokens"""

        # Test with malformed token
        malformed_headers = {"Authorization": "Bearer invalid.token.here"}
        response = await async_client.get("/auth/me", headers=malformed_headers)
        assert response.status_code == 401

        # Test with missing bearer prefix
        no_bearer_headers = {"Authorization": "invalid_token"}
        response = await async_client.get("/auth/me", headers=no_bearer_headers)
        assert response.status_code == 401

        # Test with no authorization header
        response = await async_client.get("/auth/me")
        assert response.status_code == 401

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_registration_validation(self, async_client):
        """Test registration input validation"""

        # Test missing email
        incomplete_data = {
            "password": "testpassword123",
            "full_name": "Test User"
        }
        response = await async_client.post("/auth/register", json=incomplete_data)
        assert response.status_code == 422

        # Test invalid email format
        invalid_email_data = {
            "email": "not_an_email",
            "password": "testpassword123",
            "full_name": "Test User"
        }
        response = await async_client.post("/auth/register", json=invalid_email_data)
        assert response.status_code == 422

        # Test missing password
        no_password_data = {
            "email": "test@example.com",
            "full_name": "Test User"
        }
        response = await async_client.post("/auth/register", json=no_password_data)
        assert response.status_code == 422

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_login_validation(self, async_client):
        """Test login input validation"""

        # Test missing password
        incomplete_login = {
            "email": "test@example.com"
        }
        response = await async_client.post("/auth/login", json=incomplete_login)
        assert response.status_code == 422

        # Test missing email
        no_email_login = {
            "password": "testpassword123"
        }
        response = await async_client.post("/auth/login", json=no_email_login)
        assert response.status_code == 422

        # Test empty data
        response = await async_client.post("/auth/login", json={})
        assert response.status_code == 422

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_duplicate_registration(self, async_client):
        """Test registration with duplicate email"""

        registration_data = {
            "email": "duplicate@test.com",
            "password": "testpassword123",
            "full_name": "Duplicate Test User"
        }

        # First registration succeeds
        mock_user = User(
            id="duplicate_user_id",
            email=registration_data["email"],
            full_name=registration_data["full_name"],
            skills="",
            expertise="",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch('services.mock_user_service.user_service.create_user', return_value=mock_user):
            first_response = await async_client.post("/auth/register", json=registration_data)
            assert first_response.status_code == 200

        # Second registration with same email fails
        with patch('services.mock_user_service.user_service.create_user',
                  side_effect=Exception("User with this email already exists")):
            second_response = await async_client.post("/auth/register", json=registration_data)
            assert second_response.status_code == 400
            assert "User with this email already exists" in second_response.json()["detail"]

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_failed_login_attempts(self, async_client):
        """Test multiple failed login attempts"""

        login_data = {
            "email": "test@example.com",
            "password": "wrongpassword"
        }

        # Mock failed authentication
        with patch('services.mock_user_service.user_service.authenticate_user', return_value=None):

            # Multiple failed attempts
            for _ in range(3):
                response = await async_client.post("/auth/login", json=login_data)
                assert response.status_code == 401
                assert "Incorrect email or password" in response.json()["detail"]

    @pytest.mark.integration
    @pytest.mark.auth
    @pytest.mark.asyncio
    async def test_profile_update_validation(self, async_client):
        """Test profile update validation"""

        mock_user = User(
            id="update_test_user",
            email="update@test.com",
            full_name="Update Test User",
            skills="Python",
            expertise="Beginner",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        token = auth_service.create_access_token(data={"sub": mock_user.email})
        headers = {"Authorization": f"Bearer {token}"}

        # Test valid update
        valid_update = {
            "full_name": "Updated Name",
            "skills": "Python, JavaScript",
            "expertise": "Intermediate"
        }

        updated_user = User(
            id="update_test_user",
            email="update@test.com",
            full_name=valid_update["full_name"],
            skills=valid_update["skills"],
            expertise=valid_update["expertise"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch('dependencies.get_current_user_required', return_value=mock_user), \
             patch('services.mock_user_service.user_service.update_user', return_value=updated_user):

            response = await async_client.put("/auth/me", json=valid_update, headers=headers)
            assert response.status_code == 200

        # Test partial update (only updating skills)
        partial_update = {
            "skills": "Python, JavaScript, React"
        }

        partially_updated_user = User(
            id="update_test_user",
            email="update@test.com",
            full_name=mock_user.full_name,  # Unchanged
            skills=partial_update["skills"],
            expertise=mock_user.expertise,  # Unchanged
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch('dependencies.get_current_user_required', return_value=mock_user), \
             patch('services.mock_user_service.user_service.update_user', return_value=partially_updated_user):

            response = await async_client.put("/auth/me", json=partial_update, headers=headers)
            assert response.status_code == 200
            data = response.json()
            assert data["skills"] == partial_update["skills"]
