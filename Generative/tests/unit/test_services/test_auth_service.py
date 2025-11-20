"""
Unit tests for AuthService
"""
import pytest
from datetime import datetime, timedelta
from unittest.mock import patch, Mock
from jose import jwt

from services.auth_service import AuthService, auth_service
from models.schemas import TokenData
from config.settings import settings


class TestAuthService:
    """Test cases for AuthService"""

    def setup_method(self):
        """Setup test instance"""
        self.auth_service = AuthService()

    @pytest.mark.unit
    def test_get_password_hash(self):
        """Test password hashing"""
        password = "testpassword123"
        hashed = self.auth_service.get_password_hash(password)

        assert hashed is not None
        assert hashed != password
        assert len(hashed) > 20  # Bcrypt hashes are typically longer

    @pytest.mark.unit
    def test_verify_password_correct(self):
        """Test password verification with correct password"""
        password = "testpassword123"
        hashed = self.auth_service.get_password_hash(password)

        assert self.auth_service.verify_password(password, hashed) is True

    @pytest.mark.unit
    def test_verify_password_incorrect(self):
        """Test password verification with incorrect password"""
        password = "testpassword123"
        wrong_password = "wrongpassword"
        hashed = self.auth_service.get_password_hash(password)

        assert self.auth_service.verify_password(wrong_password, hashed) is False

    @pytest.mark.unit
    def test_create_access_token_default_expiry(self):
        """Test creating access token with default expiry"""
        data = {"sub": "test@example.com"}
        token = self.auth_service.create_access_token(data)

        assert token is not None
        assert isinstance(token, str)

        # Verify token can be decoded
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        assert payload["sub"] == "test@example.com"
        assert "exp" in payload

    @pytest.mark.unit
    def test_create_access_token_custom_expiry(self):
        """Test creating access token with custom expiry"""
        data = {"sub": "test@example.com"}
        expires_delta = timedelta(hours=1)
        token = self.auth_service.create_access_token(data, expires_delta)

        assert token is not None

        # Verify expiry time
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        exp_time = datetime.fromtimestamp(payload["exp"])
        expected_exp = datetime.utcnow() + expires_delta

        # Allow 1 minute tolerance for test execution time
        assert abs((exp_time - expected_exp).total_seconds()) < 60

    @pytest.mark.unit
    def test_verify_token_valid(self):
        """Test verifying valid token"""
        data = {"sub": "test@example.com"}
        token = self.auth_service.create_access_token(data)

        token_data = self.auth_service.verify_token(token)

        assert token_data is not None
        assert isinstance(token_data, TokenData)
        assert token_data.email == "test@example.com"

    @pytest.mark.unit
    def test_verify_token_invalid(self):
        """Test verifying invalid token"""
        invalid_token = "invalid.token.here"

        token_data = self.auth_service.verify_token(invalid_token)

        assert token_data is None

    @pytest.mark.unit
    def test_verify_token_expired(self):
        """Test verifying expired token"""
        data = {"sub": "test@example.com"}
        # Create token that expires immediately
        expires_delta = timedelta(seconds=-1)
        token = self.auth_service.create_access_token(data, expires_delta)

        token_data = self.auth_service.verify_token(token)

        assert token_data is None

    @pytest.mark.unit
    def test_verify_token_missing_subject(self):
        """Test verifying token without subject claim"""
        # Create token without 'sub' claim
        data = {"user": "test@example.com"}  # Wrong key
        token = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

        token_data = self.auth_service.verify_token(token)

        assert token_data is None

    @pytest.mark.unit
    def test_global_auth_service_instance(self):
        """Test that global auth_service instance exists"""
        assert auth_service is not None
        assert isinstance(auth_service, AuthService)

    @pytest.mark.unit
    def test_password_hash_consistency(self):
        """Test that the same password produces different hashes (due to salt)"""
        password = "testpassword123"
        hash1 = self.auth_service.get_password_hash(password)
        hash2 = self.auth_service.get_password_hash(password)

        # Hashes should be different due to salt
        assert hash1 != hash2

        # But both should verify correctly
        assert self.auth_service.verify_password(password, hash1) is True
        assert self.auth_service.verify_password(password, hash2) is True

    @pytest.mark.unit
    def test_empty_password_handling(self):
        """Test handling of empty password"""
        empty_password = ""
        hashed = self.auth_service.get_password_hash(empty_password)

        assert hashed is not None
        assert self.auth_service.verify_password(empty_password, hashed) is True
        assert self.auth_service.verify_password("notEmpty", hashed) is False
