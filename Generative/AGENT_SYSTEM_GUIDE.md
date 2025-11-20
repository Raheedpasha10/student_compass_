# AI Agent System Implementation Guide

## 🎉 What's New

Your Student Compass project now includes a **sophisticated multi-agent AI system** that provides intelligent, personalized career guidance through specialized AI agents working together.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd Generative
pip install -r requirements.txt
```

### 2. Set Up API Keys

Add to your `.env` file:

```env
# Required
GOOGLE_GENAI_API_KEY=your_gemini_api_key_here

# Optional but Recommended (for real-time resource discovery)
SERPAPI_API_KEY=your_serpapi_key_here

# Alternative to SerpAPI (choose one)
GOOGLE_CSE_API_KEY=your_google_cse_key_here
GOOGLE_CSE_ID=your_google_cse_id_here
```

### 3. Run the Application

```bash
python main.py
```

The agent system will automatically:
- Try to use Google ADK if available
- Fall back to direct Gemini API if ADK is not installed
- Fall back to standard AI service if agents fail
- Use web search for real-time resources if API keys are configured
- Save conversation history to memory if user_id is provided

## 🏗️ Architecture

### Agent Pipeline (Sequential/Funneling Pattern)

```
User Input (Skills + Expertise)
    ↓
[1] Skill Analyzer Agent
    → Analyzes skills, identifies gaps, strengths, weaknesses
    ↓
[2] Career Matcher Agent
    → Matches skills to career paths, calculates match scores
    ↓
[3] Roadmap Generator Agent
    → Creates personalized learning roadmap
    ↓
[4] Resource Curator Agent
    → Curates courses, books, certifications (with web search)
    ↓
Final Result (Legacy Format for API Compatibility)
```

### Components

1. **Agent Service** (`services/agents/agent_service.py`)
   - Main agent orchestration
   - Supports Google ADK and fallback to direct Gemini API
   - Handles schema validation and error recovery

2. **Orchestrator** (`services/agents/orchestrator.py`)
   - High-level interface for agent system
   - Integrates memory and web search
   - Manages conversation context

3. **Memory System** (`services/agents/memory.py`)
   - Conversation history persistence
   - User context management
   - Skill evolution tracking
   - Career progress monitoring

4. **Web Search Tools** (`services/agents/tools.py`)
   - Real-time resource discovery
   - Course, book, and certification search
   - SerpAPI and Google CSE support

5. **Schemas** (`services/agents/schemas.py`)
   - Pydantic models for structured outputs
   - Type-safe data validation
   - Consistent response formats

## 📊 Features

### 1. Multi-Agent Analysis
- **Skill Analyzer**: Comprehensive skill assessment with gap analysis
- **Career Matcher**: Intelligent career path matching with scoring
- **Roadmap Generator**: Personalized learning roadmaps
- **Resource Curator**: Curated learning resources with real-time discovery

### 2. Web Search Integration
- Real-time course discovery
- Book recommendations
- Certification finding
- Learning resource search

### 3. Agent Memory
- Conversation history
- User preferences
- Skill evolution tracking
- Career exploration progress
- Context-aware recommendations

### 4. Error Handling
- Automatic fallbacks
- Graceful degradation
- Comprehensive logging
- Error recovery

## 🔧 Usage

### Basic Usage (Automatic)

The agent system is automatically integrated into the `/analyze` endpoint:

```python
POST /analyze
{
    "skills": "Python, React, Node.js",
    "expertise": "Intermediate level with 2 years experience"
}
```

### Advanced Usage (Programmatic)

```python
from services.agents.orchestrator import CareerGuidanceOrchestrator

orchestrator = CareerGuidanceOrchestrator()

# Analyze with all features
analysis = await orchestrator.analyze_career(
    skills="Python, React, Node.js",
    expertise="Intermediate",
    user_id="user123",
    use_agents=True,
    use_memory=True,
    use_web_search=True
)
```

### Memory Management

```python
from services.agents.memory import memory

# Get user context
context = memory.get_context_for_agent("user123")

# Get conversation history
history = memory.get_conversation_history("user123", limit=5)

# Get career progress
progress = memory.get_career_progress("user123")
```

### Web Search Tools

```python
from services.agents.tools import resource_discovery_tool

# Discover courses
courses = resource_discovery_tool.discover_courses_for_skill(
    "Data Science", level="intermediate"
)

# Discover certifications
certs = resource_discovery_tool.discover_certifications_for_career(
    "Software Engineer"
)
```

## 📈 Benefits

### For Users
- **More Accurate Analysis**: Specialized agents provide deeper insights
- **Personalized Recommendations**: Memory system learns from interactions
- **Real-time Resources**: Web search provides up-to-date information
- **Better Roadmaps**: Step-by-step analysis creates more detailed plans

### For Developers
- **Modular Architecture**: Easy to extend and modify
- **Type Safety**: Pydantic schemas ensure data consistency
- **Error Resilience**: Multiple fallback layers
- **Backward Compatible**: Works with existing API

## 🐛 Troubleshooting

### Agent System Not Working

1. **Check API Keys**: Ensure `GOOGLE_GENAI_API_KEY` is set
2. **Check Dependencies**: Run `pip install -r requirements.txt`
3. **Check Logs**: Look for error messages in logs
4. **Fallback Behavior**: System will automatically fall back to standard AI service

### Web Search Not Working

1. **Check API Keys**: Ensure `SERPAPI_API_KEY` or Google CSE keys are set
2. **Install Dependencies**: `pip install google-search-results`
3. **Check Logs**: Web search errors are logged but don't break the system
4. **Graceful Degradation**: System continues without web search if it fails

### Memory Not Persisting

1. **Check User ID**: Memory requires a valid `user_id`
2. **Check Permissions**: Ensure write permissions for memory storage
3. **Check Logs**: Memory errors are logged but don't break the system

## 📝 API Keys Setup

### Google Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Add to `.env`: `GOOGLE_GENAI_API_KEY=your_key_here`

### SerpAPI Key (Optional)
1. Go to [SerpAPI](https://serpapi.com/)
2. Sign up for a free account (100 searches/month free)
3. Get your API key
4. Add to `.env`: `SERPAPI_API_KEY=your_key_here`

### Google Custom Search (Alternative)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable Custom Search API
3. Create a Custom Search Engine
4. Add to `.env`:
   - `GOOGLE_CSE_API_KEY=your_key_here`
   - `GOOGLE_CSE_ID=your_cse_id_here`

## 🎯 Next Steps

1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Set API Keys**: Add to `.env` file
3. **Test the System**: Make a request to `/analyze` endpoint
4. **Monitor Logs**: Check for any warnings or errors
5. **Optional**: Configure web search for real-time resources

## 📚 Additional Resources

- [Agent System README](services/agents/README.md)
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Gemini API Reference](https://ai.google.dev/docs)
- [SerpAPI Documentation](https://serpapi.com/search-api)

## 🤝 Support

If you encounter any issues:
1. Check the logs for error messages
2. Verify API keys are set correctly
3. Ensure all dependencies are installed
4. The system will automatically fall back if agents fail

---

**Happy Coding! 🚀**

