import uuid
from datetime import datetime
from typing import Optional, Dict, Any
from google.cloud import firestore
from models.schemas import User, UserCreate, UserUpdate
from services.auth_service import auth_service
import os


class UserService:
    """Service for handling user operations with Firestore"""

    def __init__(self):
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")
        try:
            self.firestore_client = firestore.Client(project=self.project_id)
        except Exception as e:
            print(f"Warning: Could not initialize Firestore client: {e}")
            self.firestore_client = None

    async def create_user(self, user_data: UserCreate) -> Optional[User]:
        """Create a new user"""
        if not self.firestore_client:
            raise Exception("Firestore not available")

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

        try:
            # Save to Firestore
            doc_ref = self.firestore_client.collection('users').document(user_id)
            doc_ref.set(user_doc)

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
        except Exception as e:
            print(f"Error creating user: {e}")
            raise Exception("Failed to create user")

    async def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get user by email"""
        if not self.firestore_client:
            return None

        try:
            users_ref = self.firestore_client.collection('users')
            query = users_ref.where('email', '==', email)
            results = query.get()

            for doc in results:
                return doc.to_dict()

            return None
        except Exception as e:
            print(f"Error getting user by email: {e}")
            return None

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        if not self.firestore_client:
            return None

        try:
            doc_ref = self.firestore_client.collection('users').document(user_id)
            doc = doc_ref.get()

            if doc.exists:
                user_data = doc.to_dict()
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
        except Exception as e:
            print(f"Error getting user by ID: {e}")
            return None

    async def update_user(self, user_id: str, user_update: UserUpdate) -> Optional[User]:
        """Update user information"""
        if not self.firestore_client:
            raise Exception("Firestore not available")

        try:
            doc_ref = self.firestore_client.collection('users').document(user_id)
            doc = doc_ref.get()

            if not doc.exists:
                raise Exception("User not found")

            # Prepare update data
            update_data = {"updated_at": datetime.utcnow()}

            if user_update.full_name is not None:
                update_data["full_name"] = user_update.full_name
            if user_update.skills is not None:
                update_data["skills"] = user_update.skills
            if user_update.expertise is not None:
                update_data["expertise"] = user_update.expertise

            # Update document
            doc_ref.update(update_data)

            # Return updated user
            return await self.get_user_by_id(user_id)
        except Exception as e:
            print(f"Error updating user: {e}")
            raise Exception("Failed to update user")

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

# Global user service instance
user_service = UserService()
