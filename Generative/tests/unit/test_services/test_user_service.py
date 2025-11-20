"""
Unit tests for UserService
"""
import pytest
from unittest.mock import Mock, patch, AsyncMock
from datetime import datetime
import uuid

from services.user_service import UserService
from models.schemas import User, UserCreate, UserUpdate
from services.auth_service import auth_service


class TestUserService:
    """Test cases for UserService"""

    def setup_method(self):
        """Setup test instance with mocked Firestore"""
        with patch('services.user_service.firestore.Client'):
            self.user_service = UserService()
            # Mock the Firestore client
            self.user_service.firestore_client = Mock()

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_create_user_success(self):
        """Test successful user creation"""
        # Setup
        user_data = UserCreate(
            email="test@example.com",
            password="testpassword123",
            full_name="Test User",
            skills="Python, JavaScript",
            expertise="Intermediate"
        )

        # Mock Firestore operations
        mock_query = Mock()
        mock_query.get.return_value = []  # No existing user
        self.user_service.firestore_client.collection.return_value.where.return_value = mock_query

        mock_doc_ref = Mock()
        self.user_service.firestore_client.collection.return_value.document.return_value = mock_doc_ref

        # Execute
        result = await self.user_service.create_user(user_data)

        # Verify
        assert result is not None
        assert isinstance(result, User)
        assert result.email == user_data.email
        assert result.full_name == user_data.full_name
        assert result.skills == user_data.skills
        assert result.expertise == user_data.expertise
        assert result.id is not None

        # Verify Firestore calls
        mock_doc_ref.set.assert_called_once()
        call_args = mock_doc_ref.set.call_args[0][0]
        assert call_args["email"] == user_data.email
        assert "password_hash" in call_args
        assert call_args["password_hash"] != user_data.password  # Should be hashed

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_create_user_duplicate_email(self):
        """Test user creation with duplicate email"""
        user_data = UserCreate(
            email="test@example.com",
            password="testpassword123",
            full_name="Test User"
        )

        # Mock existing user
        mock_doc = Mock()
        mock_doc.to_dict.return_value = {"email": "test@example.com"}
        mock_query = Mock()
        mock_query.get.return_value = [mock_doc]
        self.user_service.firestore_client.collection.return_value.where.return_value = mock_query

        # Execute and verify exception
        with pytest.raises(Exception, match="User with this email already exists"):
            await self.user_service.create_user(user_data)

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_create_user_no_firestore(self):
        """Test user creation when Firestore is not available"""
        self.user_service.firestore_client = None

        user_data = UserCreate(
            email="test@example.com",
            password="testpassword123",
            full_name="Test User"
        )

        with pytest.raises(Exception, match="Firestore not available"):
            await self.user_service.create_user(user_data)

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_user_by_email_success(self):
        """Test successful user retrieval by email"""
        email = "test@example.com"
        expected_data = {
            "id": "test_id",
            "email": email,
            "full_name": "Test User",
            "skills": "Python",
            "expertise": "Beginner"
        }

        # Mock Firestore response
        mock_doc = Mock()
        mock_doc.to_dict.return_value = expected_data
        mock_query = Mock()
        mock_query.get.return_value = [mock_doc]
        self.user_service.firestore_client.collection.return_value.where.return_value = mock_query

        # Execute
        result = await self.user_service.get_user_by_email(email)

        # Verify
        assert result == expected_data
        self.user_service.firestore_client.collection.assert_called_with('users')

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_user_by_email_not_found(self):
        """Test user retrieval by email when user doesn't exist"""
        email = "nonexistent@example.com"

        # Mock empty result
        mock_query = Mock()
        mock_query.get.return_value = []
        self.user_service.firestore_client.collection.return_value.where.return_value = mock_query

        # Execute
        result = await self.user_service.get_user_by_email(email)

        # Verify
        assert result is None

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_user_by_id_success(self):
        """Test successful user retrieval by ID"""
        user_id = "test_user_id"
        user_data = {
            "id": user_id,
            "email": "test@example.com",
            "full_name": "Test User",
            "skills": "Python, JavaScript",
            "expertise": "Intermediate",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        # Mock Firestore response
        mock_doc = Mock()
        mock_doc.exists = True
        mock_doc.to_dict.return_value = user_data
        mock_doc_ref = Mock()
        mock_doc_ref.get.return_value = mock_doc
        self.user_service.firestore_client.collection.return_value.document.return_value = mock_doc_ref

        # Execute
        result = await self.user_service.get_user_by_id(user_id)

        # Verify
        assert result is not None
        assert isinstance(result, User)
        assert result.id == user_id
        assert result.email == user_data["email"]
        assert result.full_name == user_data["full_name"]

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_user_by_id_not_found(self):
        """Test user retrieval by ID when user doesn't exist"""
        user_id = "nonexistent_id"

        # Mock document not found
        mock_doc = Mock()
        mock_doc.exists = False
        mock_doc_ref = Mock()
        mock_doc_ref.get.return_value = mock_doc
        self.user_service.firestore_client.collection.return_value.document.return_value = mock_doc_ref

        # Execute
        result = await self.user_service.get_user_by_id(user_id)

        # Verify
        assert result is None

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_update_user_success(self):
        """Test successful user update"""
        user_id = "test_user_id"
        update_data = UserUpdate(
            full_name="Updated Name",
            skills="Python, React, Node.js",
            expertise="Advanced"
        )

        # Mock existing document
        mock_doc = Mock()
        mock_doc.exists = True
        mock_doc_ref = Mock()
        mock_doc_ref.get.return_value = mock_doc
        self.user_service.firestore_client.collection.return_value.document.return_value = mock_doc_ref

        # Mock get_user_by_id for return value
        updated_user = User(
            id=user_id,
            email="test@example.com",
            full_name=update_data.full_name,
            skills=update_data.skills,
            expertise=update_data.expertise,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        with patch.object(self.user_service, 'get_user_by_id', return_value=updated_user):
            # Execute
            result = await self.user_service.update_user(user_id, update_data)

            # Verify
            assert result is not None
            assert result.full_name == update_data.full_name
            assert result.skills == update_data.skills
            assert result.expertise == update_data.expertise

            # Verify update was called
            mock_doc_ref.update.assert_called_once()
            update_call_args = mock_doc_ref.update.call_args[0][0]
            assert update_call_args["full_name"] == update_data.full_name
            assert update_call_args["skills"] == update_data.skills
            assert update_call_args["expertise"] == update_data.expertise
            assert "updated_at" in update_call_args

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_update_user_not_found(self):
        """Test user update when user doesn't exist"""
        user_id = "nonexistent_id"
        update_data = UserUpdate(full_name="Updated Name")

        # Mock document not found
        mock_doc = Mock()
        mock_doc.exists = False
        mock_doc_ref = Mock()
        mock_doc_ref.get.return_value = mock_doc
        self.user_service.firestore_client.collection.return_value.document.return_value = mock_doc_ref

        # Execute and verify exception
        with pytest.raises(Exception, match="User not found"):
            await self.user_service.update_user(user_id, update_data)

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_authenticate_user_success(self):
        """Test successful user authentication"""
        email = "test@example.com"
        password = "testpassword123"
        hashed_password = auth_service.get_password_hash(password)

        user_data = {
            "id": "test_id",
            "email": email,
            "password_hash": hashed_password,
            "full_name": "Test User",
            "skills": "Python",
            "expertise": "Beginner",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        # Mock get_user_by_email
        with patch.object(self.user_service, 'get_user_by_email', return_value=user_data):
            # Execute
            result = await self.user_service.authenticate_user(email, password)

            # Verify
            assert result is not None
            assert isinstance(result, User)
            assert result.email == email
            assert result.full_name == user_data["full_name"]

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_authenticate_user_not_found(self):
        """Test authentication when user doesn't exist"""
        email = "nonexistent@example.com"
        password = "testpassword123"

        # Mock user not found
        with patch.object(self.user_service, 'get_user_by_email', return_value=None):
            # Execute
            result = await self.user_service.authenticate_user(email, password)

            # Verify
            assert result is None

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_authenticate_user_wrong_password(self):
        """Test authentication with wrong password"""
        email = "test@example.com"
        correct_password = "testpassword123"
        wrong_password = "wrongpassword"
        hashed_password = auth_service.get_password_hash(correct_password)

        user_data = {
            "id": "test_id",
            "email": email,
            "password_hash": hashed_password,
            "full_name": "Test User"
        }

        # Mock get_user_by_email
        with patch.object(self.user_service, 'get_user_by_email', return_value=user_data):
            # Execute
            result = await self.user_service.authenticate_user(email, wrong_password)

            # Verify
            assert result is None
