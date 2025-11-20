"""
Pydantic schemas for agent outputs - structured data models for each agent stage
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class SkillAssessment(BaseModel):
    """Skill assessment output from Skill Analyzer Agent"""
    current_skills: List[str] = Field(..., description="List of identified current skills")
    skill_levels: Dict[str, str] = Field(..., description="Skill level for each skill (Beginner/Intermediate/Advanced/Expert)")
    skill_gaps: List[str] = Field(..., description="Missing skills needed for target career")
    strengths: List[str] = Field(..., description="Strong areas and competencies")
    weaknesses: List[str] = Field(..., description="Areas needing improvement")
    overall_expertise_level: str = Field(..., description="Overall expertise assessment")
    skill_categories: Dict[str, List[str]] = Field(..., description="Skills grouped by category")


class CareerMatch(BaseModel):
    """Career path match output from Career Matcher Agent"""
    title: str = Field(..., description="Career path title")
    description: str = Field(..., description="Detailed career description")
    match_score: float = Field(..., description="Match score (0-100)")
    required_skills: List[str] = Field(..., description="Required skills for this career")
    current_skill_coverage: float = Field(..., description="Percentage of required skills already possessed")
    missing_critical_skills: List[str] = Field(..., description="Critical skills that are missing")
    salary_range: str = Field(..., description="Expected salary range")
    growth_prospect: str = Field(..., description="Career growth prospects")
    reasoning: str = Field(..., description="Explanation for why this career matches")


class CareerMatchAnalysis(BaseModel):
    """Complete career matching analysis"""
    career_paths: List[CareerMatch] = Field(..., description="List of matched career paths (top 3)")
    best_match: CareerMatch = Field(..., description="Best matching career path")
    alternative_paths: List[CareerMatch] = Field(default_factory=list, description="Alternative career options")
    market_trends: Optional[str] = Field(None, description="Current market trends for these careers")
    transition_difficulty: str = Field(..., description="Difficulty level of transitioning to best match")


class RoadmapStep(BaseModel):
    """Individual roadmap step"""
    step_number: int = Field(..., description="Step number in sequence")
    title: str = Field(..., description="Step title")
    description: str = Field(..., description="Detailed description of what to do")
    duration: str = Field(..., description="Expected duration (e.g., '2-3 weeks', '1 month')")
    skills_to_learn: List[str] = Field(..., description="Skills to learn in this step")
    resources_needed: List[str] = Field(..., description="Resources required for this step")
    deliverables: List[str] = Field(..., description="Expected deliverables or outcomes")
    prerequisites: List[str] = Field(default_factory=list, description="Prerequisites for this step")
    difficulty: str = Field(..., description="Difficulty level (Beginner/Intermediate/Advanced)")


class LearningRoadmap(BaseModel):
    """Complete learning roadmap from Roadmap Generator Agent"""
    total_duration: str = Field(..., description="Total estimated duration")
    steps: List[RoadmapStep] = Field(..., description="List of roadmap steps")
    milestones: List[str] = Field(..., description="Key milestones to track progress")
    learning_strategy: str = Field(..., description="Overall learning strategy")
    estimated_hours_per_week: int = Field(..., description="Recommended hours per week")
    quick_wins: List[str] = Field(..., description="Quick wins to build momentum")


class ResourceItem(BaseModel):
    """Individual resource item"""
    title: str = Field(..., description="Resource title")
    type: str = Field(..., description="Resource type (course/book/certification/video/article)")
    provider: str = Field(..., description="Provider or platform")
    url: str = Field(..., description="Resource URL")
    description: str = Field(..., description="Resource description")
    difficulty: str = Field(..., description="Difficulty level")
    duration: Optional[str] = Field(None, description="Duration or length")
    rating: Optional[float] = Field(None, description="Rating if available")
    cost: Optional[str] = Field(None, description="Cost information")
    relevance_score: float = Field(..., description="Relevance score (0-100)")


class ResourceCollection(BaseModel):
    """Resource collection from Resource Curator Agent"""
    courses: List[ResourceItem] = Field(..., description="Recommended courses")
    books: List[ResourceItem] = Field(..., description="Recommended books")
    certifications: List[ResourceItem] = Field(..., description="Recommended certifications")
    videos: List[ResourceItem] = Field(default_factory=list, description="Recommended video resources")
    articles: List[ResourceItem] = Field(default_factory=list, description="Recommended articles")
    tools: List[ResourceItem] = Field(default_factory=list, description="Recommended tools and software")
    communities: List[ResourceItem] = Field(default_factory=list, description="Recommended communities and forums")


class AgentAnalysisResult(BaseModel):
    """Complete analysis result from all agents"""
    skill_assessment: SkillAssessment = Field(..., description="Skill assessment results")
    career_analysis: CareerMatchAnalysis = Field(..., description="Career matching analysis")
    learning_roadmap: LearningRoadmap = Field(..., description="Learning roadmap")
    resources: ResourceCollection = Field(..., description="Curated resources")
    summary: str = Field(..., description="Executive summary of the analysis")
    next_steps: List[str] = Field(..., description="Immediate next steps for the user")

