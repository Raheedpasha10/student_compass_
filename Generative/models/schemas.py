from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class AnalyzeRequest(BaseModel):
    """Request model for career analysis"""
    # Make fields optional to allow route-level validation (prevents 422 for empty payloads)
    skills: Optional[str] = ""
    expertise: Optional[str] = ""


class Certification(BaseModel):
    """Certification recommendation"""
    name: str
    provider: str
    description: str
    difficulty: str
    duration: Optional[str] = "Varies"
    url: str


class CareerPath(BaseModel):
    """Career path information"""
    title: str
    description: str
    required_skills: List[str]
    salary_range: str
    growth_prospect: str


class Course(BaseModel):
    """Course recommendation"""
    title: str
    provider: str
    duration: Optional[str] = "Self-paced"
    difficulty: str
    url: str
    type: Optional[str] = None


class RoadmapStep(BaseModel):
    """Roadmap step information"""
    step: int
    title: str
    description: str
    duration: str
    resources: List[str]


class AnalyzeResponse(BaseModel):
    """Complete analysis response"""
    career_paths: List[CareerPath]
    selected_path: CareerPath
    roadmap: List[RoadmapStep]
    courses: List[Course]
    certifications: List[Certification]


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    service: str


class RootResponse(BaseModel):
    """Root endpoint response"""
    message: str


class MockTestRequest(BaseModel):
    """Request model for mock test generation"""
    skills: str
    expertise: str
    topic: Optional[str] = None


class MockTestQuestion(BaseModel):
    """Mock test question model"""
    question: str
    answer: str


class MockTestResponse(BaseModel):
    """Mock test response model"""
    test_id: str
    questions: List[MockTestQuestion]
    user_id: Optional[str] = None
    created_at: str

# User Authentication Models


class UserCreate(BaseModel):
    """User creation request"""
    email: EmailStr
    password: str
    full_name: str
    skills: Optional[str] = None
    expertise: Optional[str] = None


class UserLogin(BaseModel):
    """User login request"""
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    """User update request"""
    full_name: Optional[str] = None
    skills: Optional[str] = None
    expertise: Optional[str] = None


class User(BaseModel):
    """User response model"""
    id: str
    email: str
    full_name: str
    skills: Optional[str] = None
    expertise: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class Token(BaseModel):
    """JWT token response"""
    access_token: str
    token_type: str
    user: User


class TokenData(BaseModel):
    """Token data for validation"""
    email: Optional[str] = None


class ChatMessage(BaseModel):
    """Chat message model"""
    message: str
    user_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Chat response model"""
    bot_message: str
    extracted_skills: List[str]
    updated_skills: str
    user: Optional[User] = None


class UpdateSkillsRequest(BaseModel):
    """Update skills request model"""
    user_id: str
    message: str


class SkillExtraction(BaseModel):
    """Individual skill extraction model"""
    skill: str
    expertise_level: str


class UpdateSkillsResponse(BaseModel):
    """Update skills response model"""
    extracted_skills: List[SkillExtraction]
    updated_skills_list: List[str]
    user: Optional[User] = None
