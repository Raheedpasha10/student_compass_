from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer
from models.schemas import MockTestRequest, MockTestResponse, MockTestQuestion, User
from services.ai_service import AIService
from dependencies import get_current_user
from typing import Optional

router = APIRouter(prefix="/mock-test", tags=["mock-test"])
# Move AIService initialization inside the function to ensure proper environment loading
# ai_service = AIService()  # This line will be removed
security = HTTPBearer()

@router.post("", response_model=MockTestResponse)
async def generate_mock_test(
    request: MockTestRequest,
    current_user: Optional[User] = Depends(get_current_user)
):
    """
    Generate a mock test based on skills and expertise using Vertex AI
    and save it to Firestore. Requires authentication.
    """
    # Initialize AIService inside the function to ensure environment variables are loaded
    ai_service = AIService()

    try:
        # Use skills and expertise from request or user profile
        skills = request.skills or (current_user.skills if current_user else "")
        expertise = request.expertise or (current_user.expertise if current_user else "")

        if not skills or not expertise:
            raise HTTPException(
                status_code=400,
                detail="Skills and expertise are required. Please provide them in the request or update your profile."
            )

        # Generate mock test using Vertex AI
        test_data = ai_service.generate_mock_test(
            skills=skills,
            expertise=expertise,
            topic=request.topic or "",
            user_id=current_user.id if current_user else ""
        )

        # Convert questions to Pydantic models
        questions = [MockTestQuestion(**q) for q in test_data["questions"]]

        return MockTestResponse(
            test_id=test_data["test_id"],
            questions=questions,
            user_id=test_data["user_id"],
            created_at=test_data["created_at"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating mock test: {str(e)}")
