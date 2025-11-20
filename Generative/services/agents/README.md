# AI Agent System for Career Guidance

This module implements a sophisticated multi-agent system for career guidance using Google ADK (Agent Development Kit) or direct Gemini API calls as fallback.

## Architecture

The system uses a **sequential agent pattern (funneling)** where specialized agents process the career analysis in stages:

1. **Skill Analyzer Agent** - Analyzes user skills, identifies strengths, weaknesses, and skill gaps
2. **Career Matcher Agent** - Matches skills to suitable career paths with detailed analysis
3. **Roadmap Generator Agent** - Creates personalized learning roadmaps based on career goals
4. **Resource Curator Agent** - Curates high-quality learning resources (courses, books, certifications, etc.)

## Features

- **Structured Outputs**: Uses Pydantic schemas for type-safe, validated responses
- **Automatic Fallback**: Falls back to direct Gemini API if Google ADK is unavailable
- **Backward Compatible**: Converts agent results to legacy format for existing API consumers
- **Error Handling**: Robust error handling with graceful fallbacks
- **Session Management**: Supports user sessions for conversation continuity

## Usage

### Basic Usage

```python
from services.agents.orchestrator import CareerGuidanceOrchestrator

orchestrator = CareerGuidanceOrchestrator()
analysis = await orchestrator.analyze_career(
    skills="Python, React, Node.js",
    expertise="Intermediate level with 2 years experience",
    user_id="user123"
)
```

### Integration with FastAPI

The agent system is automatically integrated into the `/analyze` endpoint. It will:
1. Try to use the agent system first
2. Automatically fall back to the standard AI service if agents fail
3. Maintain full backward compatibility

## Configuration

### Environment Variables

- `GOOGLE_GENAI_API_KEY` or `GOOGLE_API_KEY`: Google Gemini API key (required)
- `SERPAPI_API_KEY`: SerpAPI key for web search (optional, but recommended for real-time resource discovery)
- `GOOGLE_CSE_API_KEY`: Google Custom Search API key (optional, alternative to SerpAPI)
- `GOOGLE_CSE_ID`: Google Custom Search Engine ID (optional, required if using Google CSE)

### Dependencies

- `google-adk==0.1.0`: Google Agent Development Kit (optional, will use fallback if not available)
- `google-generativeai`: Google Generative AI SDK (required)
- `pydantic`: For schema validation (required)

## Agent Schemas

### SkillAssessment
- `current_skills`: List of identified skills
- `skill_levels`: Proficiency levels for each skill
- `skill_gaps`: Missing skills needed
- `strengths`: Areas of strength
- `weaknesses`: Areas needing improvement
- `overall_expertise_level`: Overall assessment
- `skill_categories`: Skills grouped by category

### CareerMatchAnalysis
- `career_paths`: List of matched career paths
- `best_match`: Best matching career path
- `alternative_paths`: Alternative options
- `market_trends`: Market insights
- `transition_difficulty`: Difficulty assessment

### LearningRoadmap
- `total_duration`: Total estimated duration
- `steps`: List of roadmap steps
- `milestones`: Key milestones
- `learning_strategy`: Overall strategy
- `estimated_hours_per_week`: Time commitment
- `quick_wins`: Quick wins for momentum

### ResourceCollection
- `courses`: Recommended courses
- `books`: Recommended books
- `certifications`: Recommended certifications
- `videos`: Video resources
- `articles`: Article resources
- `tools`: Tools and software
- `communities`: Communities and forums

## Error Handling

The system includes comprehensive error handling:
- Agent initialization errors → Fallback to direct Gemini API
- Agent execution errors → Fallback to standard AI service
- Schema validation errors → Graceful error messages
- API errors → Automatic retries with exponential backoff

## Performance

- **Agent System**: More thorough analysis, slightly slower (10-30 seconds)
- **Fallback System**: Faster response (5-10 seconds), good quality
- **Caching**: Session-based state management for improved performance

## Features

### ✅ Implemented Features

- **Multi-Agent Sequential Pipeline**: Specialized agents for each stage of analysis
- **Web Search Integration**: Real-time resource discovery using SerpAPI or Google CSE
- **Agent Memory**: Conversation history and user context persistence
- **Structured Outputs**: Type-safe Pydantic schemas for all agent responses
- **Automatic Fallbacks**: Graceful degradation if agents or tools are unavailable
- **Backward Compatibility**: Seamless integration with existing API

### 🔮 Future Enhancements

- [ ] Add parallel agent execution for faster resource curation
- [ ] Implement agentic RAG for personalized knowledge base
- [ ] Add streaming responses for real-time updates
- [ ] Implement user preference learning from interactions
- [ ] Add multi-language support
- [ ] Implement A/B testing for agent prompts

