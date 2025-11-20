import uuid
from datetime import datetime
from typing import Optional, Dict, Any
from models.schemas import User, UserCreate, UserUpdate
from services.auth_service import auth_service

# In-memory user storage for demo purposes
MOCK_USERS = {}


class MockUserService:
    """Mock user service that works without Firestore for testing"""

    def __init__(self):
        pass

    async def create_user(self, user_data: UserCreate) -> Optional[User]:
        """Create a new user"""
        # Check if user already exists
        existing_user = await self.get_user_by_email(user_data.email)
        if existing_user:
            raise Exception("User with this email already exists")

        # Create user document
        user_id = str(uuid.uuid4())
        now = datetime.utcnow()

        user_doc = {
            "id": user_id,
            "email": user_data.email,
            "password_hash": auth_service.get_password_hash(user_data.password),
            "full_name": user_data.full_name,
            "skills": user_data.skills or "",
            "expertise": user_data.expertise or "",
            "created_at": now,
            "updated_at": now
        }

        # Save to memory
        MOCK_USERS[user_id] = user_doc

        # Return user without password hash
        return User(
            id=user_id,
            email=user_data.email,
            full_name=user_data.full_name,
            skills=user_data.skills or "",
            expertise=user_data.expertise or "",
            created_at=now,
            updated_at=now
        )

    async def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get user by email"""
        for user_data in MOCK_USERS.values():
            if user_data["email"] == email:
                return user_data
        return None

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        user_data = MOCK_USERS.get(user_id)
        if user_data:
            return User(
                id=user_data["id"],
                email=user_data["email"],
                full_name=user_data["full_name"],
                skills=user_data.get("skills", ""),
                expertise=user_data.get("expertise", ""),
                created_at=user_data["created_at"],
                updated_at=user_data["updated_at"]
            )
        return None

    async def update_user(self, user_id: str, user_update: UserUpdate) -> Optional[User]:
        """Update user information"""
        if user_id not in MOCK_USERS:
            raise Exception("User not found")

        user_data = MOCK_USERS[user_id]

        # Prepare update data
        if user_update.full_name is not None:
            user_data["full_name"] = user_update.full_name
        if user_update.skills is not None:
            user_data["skills"] = user_update.skills
        if user_update.expertise is not None:
            user_data["expertise"] = user_update.expertise

        user_data["updated_at"] = datetime.utcnow()

        # Return updated user
        return await self.get_user_by_id(user_id)

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password"""
        user_data = await self.get_user_by_email(email)
        if not user_data:
            return None

        if not auth_service.verify_password(password, user_data["password_hash"]):
            return None

        return User(
            id=user_data["id"],
            email=user_data["email"],
            full_name=user_data["full_name"],
            skills=user_data.get("skills", ""),
            expertise=user_data.get("expertise", ""),
            created_at=user_data["created_at"],
            updated_at=user_data["updated_at"]
        )

# Create appropriate service instance based on Firestore availability
try:
    from services.user_service import UserService
    # Try to create real service
    real_service = UserService()
    if real_service.firestore_client:
        user_service = real_service
    else:
        user_service = MockUserService()
        print("Using mock user service (Firestore not available)")
except Exception:
    user_service = MockUserService()
    print("Using mock user service (Firestore not available)")
