from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from services.enhanced_resource_service import enhanced_resource_service

router = APIRouter(prefix="/resources", tags=["resources"])

class SearchResourcesRequest(BaseModel):
    topic: str = Field(..., description="Topic or skill to search resources for")
    type: Literal["youtube", "books", "certifications", "courses"] = Field(..., description="Resource type")
    limit: int = Field(20, ge=1, le=50, description="Number of results to return")
    level: Optional[str] = Field(None, description="Optional expertise level for course recommendations")

class ResourceItem(BaseModel):
    title: str
    url: str
    description: Optional[str] = None
    provider: Optional[str] = None
    type: Optional[str] = None

class SearchResourcesResponse(BaseModel):
    results: List[ResourceItem]

@router.post("/search", response_model=SearchResourcesResponse)
async def search_resources(payload: SearchResourcesRequest):
    """
    Search learning resources using REAL YouTube API and Google Gemini AI ONLY
    """
    if not payload.topic or len(payload.topic.strip()) < 2:
        raise HTTPException(status_code=400, detail="Please provide a valid topic to search for resources.")

    print(f"🔥 REAL API SEARCH REQUEST: {payload.type} for '{payload.topic}' (limit: {payload.limit})")
    
    try:
        # Use ONLY our enhanced resource service with REAL APIs
        enhanced_results = enhanced_resource_service.get_enhanced_resources(
            topic=payload.topic,
            resource_type=payload.type,
            limit=payload.limit,
            level=payload.level or "intermediate"
        )
        
        # Convert to ResourceItem format
        results = [
            ResourceItem(
                title=item["title"],
                url=item["url"],
                description=item.get("description", ""),
                provider=item.get("provider", ""),
                type=payload.type
            )
            for item in enhanced_results
        ]
        
        print(f"🎯 REAL API RESULTS: Found {len(results)} resources")
        for i, r in enumerate(results[:3]):
            print(f"  {i+1}. {r.title[:50]}...")
            print(f"      URL: {r.url[:60]}...")
            if 'youtube.com/watch?v=' in r.url:
                print(f"      ✅ REAL YouTube video!")
            elif 'youtube.com/results?' in r.url or 'search_query=' in r.url:
                print(f"      ❌ Search redirect (removing this!)")
            else:
                print(f"      🔗 Direct link")
        
        return SearchResourcesResponse(results=results)
        
    except Exception as e:
        print(f"❌ Enhanced resource service error: {e}")
        import traceback
        traceback.print_exc()
        
        # Only emergency fallback
        raise HTTPException(status_code=500, detail="Resource search temporarily unavailable - please try again")