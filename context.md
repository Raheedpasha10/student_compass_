# Student Compass (Margdarshan) - Complete Context Documentation

## Project Overview

**Student Compass** (also known as Margdarshan) is an AI-powered career guidance platform that analyzes student skills and generates personalized learning roadmaps. The system uses a multi-agent architecture to provide comprehensive career guidance with curated resources, project suggestions, and structured learning paths.

### Core Value Proposition
- Analyze student's current skills and experience level
- Generate personalized career path suggestions
- Create detailed learning roadmaps with phases, projects, tools, and resources
- Provide actionable guidance for career advancement

---

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **AI/ML**: 
  - Google Vertex AI/Gemini (gemini-2.0-flash)
  - Groq (llama-3.3-70b-versatile, llama-3.1-8b-instant)
  - Optional: HuggingFace models
- **Database**: Firestore (with in-memory mock fallback)
- **Authentication**: JWT-based with bcrypt password hashing
- **Environment**: Python 3.11+

### Frontend
- **Framework**: React 18.x
- **Styling**: Tailwind CSS
- **Animations**: Framer Motion
- **HTTP Client**: Axios
- **Build Tool**: Create React App

### Deployment
- **Backend Port**: 8001
- **Frontend Port**: 3000 (also supports 3001, 3002, 3005)
- **CORS**: Configured for multiple localhost ports

---

## Architecture Overview

### Multi-Agent System (Active)
The current active system uses three specialized AI agents:

1. **Strategic Planner** (Groq: llama-3.3-70b-versatile)
   - Focus: Market positioning, salary growth, career ladders, industry timing
   - Role: Career counselor understanding hiring trends and industry evolution

2. **Technical Expert** (Groq: llama-3.1-8b-instant) 
   - Focus: Deep technical skills, modern toolchains, industry-standard practices
   - Role: Senior engineer designing training programs

3. **Practical Guide** (Gemini: gemini-2.0-flash)
   - Focus: Immediate action, hands-on building, proven learning methods
   - Role: Mentor helping students get their first jobs

### Legacy System (Disabled)
- Located: `Generative/services/agents/*`
- Status: Disabled via `ENABLE_AGENT_SYSTEM=false`
- Contains: Orchestrator, AgentService, Tools, Memory components

---

## File Structure & Key Components

### Backend (`Generative/`)

#### Main Application
- `main.py` - FastAPI application entry point, router configuration
- `config/settings.py` - Application configuration
- `models/schemas.py` - Pydantic data models

#### Routes (`routes/`)
- `multi_agent_roadmap.py` - **PRIMARY ACTIVE ENDPOINTS** (`/api/v2/roadmap/*`)
- `analyze.py` - Legacy analysis endpoint with agent toggle
- `auth.py` - Authentication endpoints
- `health.py` - Health check endpoints
- `agents.py` - Direct agent access (legacy, disabled)
- `resources.py` - Resource discovery
- `mock_test.py` - Mock test generation
- `update_skills.py` - Skill extraction and updates

#### Services (`services/`)
- `multi_agent_service.py` - **ACTIVE MULTI-AGENT SYSTEM**
- `ai_service.py` - Legacy monolithic AI service
- `enhanced_resource_service.py` - Resource curation and enhancement
- `auth_service.py` - JWT and authentication logic
- `user_service.py` - Firestore user operations
- `mock_user_service.py` - In-memory user fallback

#### Legacy Agent System (`services/agents/` - DISABLED)
- `orchestrator.py` - High-level agent coordination
- `agent_service.py` - Core agent execution
- `tools.py` - Web search and utilities
- `memory.py` - Session context storage

### Frontend (`Generative/frontend/`)

#### Main Application
- `src/App.js` - Main routing and application structure
- `src/index.js` - React application entry point

#### Pages (`src/pages/`)
- `Landing.js` - Marketing/product overview page
- `UltimateRoadmap.js` - **PRIMARY ROADMAP DISPLAY** with structured phases
- `Flowchart.js` - Visual learning path display
- `MultiAgentDemo.js` - Direct agent interaction interface
- `CareerPath.js` - Career exploration interface

#### Components (`src/components/`)
- `LoadingScreen.js` - **ENHANCED LOADING EXPERIENCE** (matches theme)
- `LoadingSpinner.js` - Basic spinner component (legacy)
- `Enhanced3DCard.js` / `Enhanced3DButton.js` - 3D UI components
- `LinearCard.js` / `LinearButton.js` - Linear design system components
- `AgentInterface.js` - Agent interaction UI
- `Navbar.js` - Navigation component

#### Services & Data
- `src/services/api.js` - **CENTRALIZED API CALLS** (axios-based)
- `src/constants/realResources.js` - Curated resource database
- `src/context/AppContext.js` - Global application state

---

## Active API Endpoints

### Multi-Agent Roadmap (PRIMARY - `/api/v2/roadmap`)
- `POST /api/v2/roadmap/generate` - **MAIN ENDPOINT**
  - Input: `{query: string, background?: object, include_agent_details?: boolean}`
  - Output: `{final_roadmap: string, agent_insights: array, metadata: object}`

- `POST /api/v2/roadmap/generate-async` - Async processing
- `GET /api/v2/roadmap/status/{task_id}` - Async status check
- `GET /api/v2/roadmap/health` - System health and config status
- `POST /api/v2/roadmap/analyze-enhanced` - Legacy compatibility wrapper

### Authentication (`/auth`)
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user
- `PUT /auth/me` - Update user profile

### Utility Endpoints
- `GET /health` - Health check
- `POST /analyze` - Legacy analysis (with agent toggle)
- `POST /mock-test` - Generate practice tests
- `POST /update-skills` - Extract skills from text

---

## Environment Configuration

### Required Environment Variables
```env
# AI Models (Required for full functionality)
GROQ_API_KEY=your_groq_key_here
GOOGLE_GENAI_API_KEY=your_gemini_key_here

# Optional AI Services  
HUGGINGFACE_API_TOKEN=optional_hf_token
SERPAPI_API_KEY=optional_search_key
SERPER_API_KEY=optional_search_key
TAVILY_API_KEY=optional_search_key
YOUTUBE_API_KEY=optional_youtube_key

# Database (Optional - falls back to mock)
GOOGLE_CLOUD_PROJECT=your_project_id
# Firestore credentials via service account

# Authentication
SECRET_KEY=your_jwt_secret_key

# System Toggles
ENABLE_AGENT_SYSTEM=false  # Legacy toggle (not used by V2)
```

### Agent Health Check
The `/api/v2/roadmap/health` endpoint reports:
- `groq_configured`: GROQ_API_KEY present
- `gemini_configured`: GOOGLE_GENAI_API_KEY present  
- `huggingface_configured`: HUGGINGFACE_API_TOKEN present
- `multi_agent_enabled`: Overall system status

---

## Data Flow & User Journey

### 1. User Input
- User selects specialization on Landing page
- Provides skill level (Beginner/Intermediate/Advanced)
- Optional: Additional background information

### 2. Backend Processing
- Frontend calls `/api/v2/roadmap/generate`
- MultiAgentFunnelService coordinates 3 agents in parallel
- Each agent generates structured JSON per specialized role
- Results merged deterministically (no LLM synthesis)
- Final markdown rendered from structured data

### 3. Frontend Display
- LoadingScreen shows during processing (~45 seconds)
- UltimateRoadmap displays structured phases immediately
- No parsing delays - pre-processed data structure
- Clean bullet points with proper formatting

### 4. Structured Output Format
```json
{
  "final_roadmap": "# Overview\n...\n## Complete Learning Roadmap\n...",
  "metadata": {
    "structured_plan": {
      "overview": "string",
      "time_commitment_hours_per_week": 10,
      "phases": [
        {
          "name": "Foundation Building",
          "duration_weeks": 6,
          "goals": ["Learn Python basics", "..."],
          "topics": ["Variables and data types", "..."],
          "tools": ["Python 3.11+", "VS Code", "..."],
          "projects": [
            {"name": "Calculator App", "description": "Build CLI calculator with error handling"}
          ],
          "resources": [
            {"title": "Python for Everybody", "provider": "Coursera", "url": "..."}
          ],
          "checkpoints": ["Complete 10 coding exercises", "..."]
        }
      ],
      "career_milestones": [
        {"timeframe": "Month 3", "outcome": "Junior-ready portfolio"}
      ]
    }
  }
}
```

---

## Recent Improvements & Current State

### Loading Experience (FIXED)
- **Before**: Generic loading spinner, mismatched styling
- **After**: Custom LoadingScreen component with:
  - Theme-matched colors and styling
  - Animated progress indicators
  - Dynamic step descriptions
  - Proper visual hierarchy

### Content Quality (ENHANCED)
- **Agent Prompts**: Highly differentiated roles with specific requirements
- **Strategic Agent**: Salary ranges, job titles, networking strategies
- **Practical Agent**: Step-by-step projects, free resources, debugging tips
- **Technical Agent**: Exact versions, testing frameworks, architecture patterns

### Performance (OPTIMIZED)
- **Pre-processing**: Clean data during API response, not during render
- **No Filtering Delays**: Structured data displays immediately
- **Cache Management**: Version-controlled session storage
- **Text Cleaning**: Remove markdown artifacts (`**bold**`, `- bullets`) during data processing

### Current Issues Resolved
✅ Loading delays eliminated  
✅ Content displays immediately after generation  
✅ Clean formatting without extra characters  
✅ No more "one word" display bugs  
✅ Stable timeout handling (45 seconds)  
✅ Proper theme integration for loading screens  

---

## Development Workflow

### Running the Application
```bash
# Backend
cd Generative
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py

# Frontend  
cd Generative/frontend
npm install
npm start
```

### Key Development Files to Monitor
- `Generative/services/multi_agent_service.py` - Core agent logic
- `Generative/routes/multi_agent_roadmap.py` - API endpoints
- `Generative/frontend/src/pages/UltimateRoadmap.js` - Primary UI
- `Generative/frontend/src/components/LoadingScreen.js` - Loading experience
- `Generative/frontend/src/services/api.js` - API integration

### Testing Strategy
- Manual testing via UI workflow
- Health check endpoint for system status
- Session storage for caching (key: `roadmap_v2-structured-1_${skills}_${expertise}`)

---

## Known Limitations & Future Considerations

### Performance
- Agent generation takes 30-45 seconds (industry standard for quality)
- No streaming responses (could be added)
- In-memory task storage for async (Redis recommended for production)

### Content Quality
- Agents occasionally produce similar content (mitigated by role specialization)
- No automatic resource validation (links/availability)
- Limited personalization beyond basic background info

### Technical Debt
- Legacy agent system still present but disabled
- Multiple API endpoint patterns (V1 vs V2)
- Mixed authentication patterns across routes

---

## Integration Points & Extension Opportunities

### Atlassian Integration (Available)
- Confluence page creation for roadmap documentation
- Jira work item creation for tracking progress
- Available via MCP tools in development environment

### Resource Enhancement
- Integration with `EnhancedResourceService` for verified resources
- Connection to `realResources.js` for instant loading
- Potential API integrations (YouTube, Coursera, GitHub)

### Personalization
- User profile integration for better recommendations
- Progress tracking across sessions
- Skill assessment integration

---

## Critical Success Factors

### User Experience
1. **Fast Loading Feedback** - LoadingScreen provides clear progress indication
2. **Immediate Content Display** - No parsing delays after generation
3. **Clean, Scannable Format** - Structured phases with clear visual hierarchy
4. **Actionable Content** - Specific projects, tools, and resources

### System Reliability  
1. **Fallback Handling** - Graceful degradation when agents fail
2. **Timeout Management** - Reasonable limits preventing infinite waits
3. **Data Validation** - Structured JSON parsing with error handling
4. **Cache Management** - Prevents unnecessary regeneration

### Content Quality
1. **Agent Specialization** - Each agent provides unique perspective
2. **Structured Output** - Consistent format enables reliable processing
3. **Beginner-Friendly** - Accessible language and clear explanations
4. **Actionable Guidance** - Concrete next steps and measurable milestones

---

## Next Agent Instructions

When continuing work on this project:

1. **Always test the core roadmap generation flow** before making changes
2. **Use the working patterns** established in UltimateRoadmap.js and multi_agent_service.py
3. **Maintain backward compatibility** with existing data structures
4. **Test loading experience** to ensure no performance regressions
5. **Verify agent health** via `/api/v2/roadmap/health` endpoint
6. **Use session storage cache key** `roadmap_v2-structured-1_*` for testing
7. **Reference this context** for architectural decisions and known working patterns

### If making changes to agent prompts or data structures:
- Test with small changes first
- Maintain the working JSON schema structure  
- Verify frontend compatibility before complex modifications
- Consider gradual migration rather than wholesale replacement

### If adding new features:
- Follow the established patterns in multi_agent_roadmap.py
- Use the LoadingScreen component for consistent UX
- Integrate with existing API patterns in api.js
- Consider Atlassian integration opportunities for documentation/tracking

---

*Last Updated: Based on working system state after resolving loading delays and content display issues*