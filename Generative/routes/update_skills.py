from fastapi import APIRouter, HTTPException
from models.schemas import UpdateSkillsRequest, UpdateSkillsResponse, SkillExtraction, UserUpdate
from services.ai_service import AIService
from services.mock_user_service import user_service
from typing import List

router = APIRouter(tags=["skills"])
# Move AIService initialization inside the function to ensure proper environment loading
# ai_service = AIService()  # This line will be removed

@router.post("/update-skills", response_model=UpdateSkillsResponse)
async def update_skills(request: UpdateSkillsRequest):
    """
    Extract skills from message using Vertex AI and merge into user's Firestore document
    """
    # Initialize AIService inside the function to ensure environment variables are loaded
    ai_service = AIService()

    try:
        # Get current user
        user = await user_service.get_user_by_id(request.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Extract skills using Vertex AI (using the available method)
        extraction_result = ai_service.extract_skills_from_message(request.message, user.skills if user.skills else "")
        extracted_skills_data = extraction_result.get("extracted_skills", [])

        # Convert to Pydantic models
        extracted_skills = [SkillExtraction(**skill_data) for skill_data in extracted_skills_data]

        # Get updated skills list
        updated_skills_string = extraction_result.get("updated_skills", "")

        # Update user skills in database
        user_update = UserUpdate(skills=updated_skills_string)
        updated_user = await user_service.update_user(request.user_id, user_update)

        if not updated_user:
            raise HTTPException(status_code=500, detail="Failed to update user skills")

        # Create skills list for response
        updated_skills_list = [skill.strip() for skill in updated_skills_string.split(",") if skill.strip()] if updated_skills_string else []

        return UpdateSkillsResponse(
            extracted_skills=extracted_skills,
            updated_skills_list=updated_skills_list,
            user=updated_user
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error updating skills: {str(e)}"
        )
