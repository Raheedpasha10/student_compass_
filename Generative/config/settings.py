import os
from typing import List


class Settings:
    """Application settings and configuration"""

    # API Configuration
    API_TITLE: str = "Student Compass API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "A FastAPI backend service that uses Google's Vertex AI to analyze skills and generate career recommendations for students"

    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8001  # Changed from 8000 to avoid conflict
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",  # React development server
        "http://127.0.0.1:3000",
        "http://localhost:3001",  # Alternative React port
        "http://127.0.0.1:3001",
        "http://localhost:3002",  # Current React port
        "http://127.0.0.1:3002",
        "http://localhost:3005",  # Previous React port
        "http://127.0.0.1:3005",
    ]

    # Google Cloud Configuration
    GOOGLE_CLOUD_PROJECT: str = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")

    # Firestore Configuration
    FIRESTORE_DATABASE: str = os.getenv("FIRESTORE_DATABASE", "(default)")

    # AI Configuration
    AI_MODEL_NAME: str = "gemini-1.0-pro"

    # Authentication Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# Global settings instance
settings = Settings()
