from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.schemas import User
from services.auth_service import auth_service
from services.mock_user_service import user_service
from typing import Optional

security = HTTPBearer(auto_error=False)

async def get_current_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> Optional[User]:
    """Get current authenticated user (optional)"""
    if not credentials:
        return None

    token_data = auth_service.verify_token(credentials.credentials)
    if token_data is None:
        return None

    user = await user_service.get_user_by_email(token_data.email)
    if user is None:
        return None

    return User(
        id=user["id"],
        email=user["email"],
        full_name=user["full_name"],
        skills=user.get("skills", ""),
        expertise=user.get("expertise", ""),
        created_at=user["created_at"],
        updated_at=user["updated_at"]
    )

async def get_current_user_required(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """Get current authenticated user (required)"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if not credentials:
        raise credentials_exception

    token_data = auth_service.verify_token(credentials.credentials)
    if token_data is None:
        raise credentials_exception

    user = await user_service.get_user_by_email(token_data.email)
    if user is None:
        raise credentials_exception

    return User(
        id=user["id"],
        email=user["email"],
        full_name=user["full_name"],
        skills=user.get("skills", ""),
        expertise=user.get("expertise", ""),
        created_at=user["created_at"],
        updated_at=user["updated_at"]
    )
