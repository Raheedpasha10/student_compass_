# Multi-Agent Funneling System - Complete Setup Guide

## 🎯 Overview

This guide will help you integrate a multi-agent funneling system into your Student Compass project. The system uses 3 different AI agents working in parallel to generate roadmaps, then intelligently combines their outputs into one optimal result.

## 🏗️ Architecture

```
User Query → [Agent 1: Strategic] ⎤
           → [Agent 2: Practical] ⎬→ Funneling Agent → Final Roadmap
           → [Agent 3: Technical] ⎦
```

**Agents:**
1. **Strategic Planner** (Groq - Llama 3.3 70B): Long-term strategy, industry insights
2. **Practical Guide** (Gemini Pro): Actionable steps, resources, hands-on learning
3. **Technical Expert** (Groq - Llama 3.1 8B): Technical skills, tools, technologies

**Funneling Agent** (Groq - Llama 3.3 70B): Synthesizes all responses into one optimal roadmap

---

## 📦 Step 1: Install Dependencies

Add these to your `requirements.txt`:

```txt
# Existing dependencies
fastapi
uvicorn
pydantic
python-dotenv
google-generativeai

# New dependencies for multi-agent system
groq>=0.4.0
httpx>=0.25.0
asyncio
```

Install them:
```bash
cd Generative
pip install groq httpx
```

---

## 🔑 Step 2: Get Free API Keys

### 2.1 Groq API (Primary Agent Provider)
1. Visit: https://console.groq.com/
2. Sign up (free, no credit card required)
3. Go to "API Keys" → Create new key
4. Copy your API key
5. **Free tier**: 30 requests/minute, 14,400 requests/day

### 2.2 HuggingFace Token (Optional Backup)
1. Visit: https://huggingface.co/
2. Sign up → Settings → Access Tokens
3. Create "Read" token
4. Copy your token
5. **Free tier**: Unlimited (with rate limits)

### 2.3 Google Gemini (You Already Have This)
- Keep your existing `GOOGLE_GENAI_API_KEY`

---

## ⚙️ Step 3: Update Environment Variables

Edit your `.env` file in `Generative/` directory:

```bash
# Existing
GOOGLE_GENAI_API_KEY=your_existing_gemini_key

# New - Add these
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_API_TOKEN=your_huggingface_token_here  # Optional
```

---

## 📁 Step 4: Add New Files

### 4.1 Create the Multi-Agent Service

Create file: `Generative/services/multi_agent_service.py`

Copy the entire content from the first artifact above (Multi-Agent Funneling Service)

### 4.2 Create the New API Route

Create file: `Generative/routes/multi_agent_roadmap.py`

Copy the entire content from the second artifact above (FastAPI Route)

---

## 🔌 Step 5: Register the New Route

Edit `Generative/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Existing imports
from routes import analyze, auth, mock_test, health, ai_search

# NEW: Import the multi-agent route
from routes import multi_agent_roadmap

app = FastAPI(title="Student Compass API")

# CORS configuration (existing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Existing routes
app.include_router(analyze.router)
app.include_router(auth.router)
app.include_router(mock_test.router)
app.include_router(health.router)
app.include_router(ai_search.router)

# NEW: Add multi-agent route
app.include_router(multi_agent_roadmap.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## 🧪 Step 6: Test the System

### 6.1 Start the Backend

```bash
cd Generative
python main.py
```

### 6.2 Test Health Check

Visit: http://localhost:8000/api/v2/roadmap/health

Expected response:
```json
{
  "status": "healthy",
  "multi_agent_enabled": true,
  "configurations": {
    "groq_configured": true,
    "gemini_configured": true,
    "huggingface_configured": false
  },
  "message": "Multi-agent system ready"
}
```

### 6.3 Test Roadmap Generation

Using cURL:
```bash
curl -X POST "http://localhost:8000/api/v2/roadmap/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "I want to transition from marketing to data science",
    "background": {
      "current_skills": "Marketing analytics, Excel, basic SQL",
      "experience_level": "Intermediate",
      "time_available": "10 hours per week",
      "goals": "Get a data science job within 12 months"
    },
    "include_agent_details": true
  }'
```

Or use the Swagger docs: http://localhost:8000/docs

---

## 🎨 Step 7: Update Frontend (Optional)

### Option 1: Keep Existing UI, Update API Call

In your frontend service file (e.g., `frontend/src/services/api.js`):

```javascript
// Add new function
export const generateEnhancedRoadmap = async (query, background) => {
  const response = await fetch('http://localhost:8000/api/v2/roadmap/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query,
      background,
      include_agent_details: true
    })
  });
  
  return await response.json();
};
```

### Option 2: Show Agent Insights in UI

Display which agents contributed and their confidence scores:

```jsx
// In your roadmap display component
{result.agent_insights && (
  <div className="agent-insights">
    <h3>AI Insights</h3>
    {result.agent_insights.map((insight, idx) => (
      <div key={idx} className="agent-card">
        <h4>{insight.agent_name}</h4>
        <p>Focus: {insight.focus}</p>
        <p>Confidence: {(insight.confidence * 100).toFixed(0)}%</p>
      </div>
    ))}
  </div>
)}
```

---

## 🔄 Step 8: Remove Old Agent Implementation

You mentioned wanting to remove the existing agent. Here's how:

1. **Backup first** (just in case):
```bash
cp Generative/services/ai_service.py Generative/services/ai_service.py.backup
```

2. **Option A - Replace completely**:
   - Delete `ai_service.py`
   - Update all imports to use `multi_agent_service.py`

3. **Option B - Keep both** (recommended initially):
   - Keep old service as fallback
   - Add flag in routes to choose which to use
   - Gradually migrate endpoints

---

## 📊 Step 9: Monitor Performance

### Check Agent Performance

Add logging to see which agents perform best:

```python
# In multi_agent_service.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In generate_roadmap_with_agent method, add:
logger.info(f"{agent_config['name']} - Confidence: {confidence:.2f}")
```

### Metrics to Track
- Response time per agent
- Confidence scores
- User satisfaction with funneled results
- API costs (all free, but track usage)

---

## 🚀 Advanced Customization

### Add More Agents

Edit `multi_agent_service.py`:

```python
self.agents = {
    "agent_strategic": {...},
    "agent_practical": {...},
    "agent_technical": {...},
    
    # Add new agent
    "agent_industry": {
        "name": "Industry Insider",
        "provider": "groq",
        "model": "llama-3.1-8b-instant",
        "focus": "current industry trends and job market insights"
    }
}
```

### Customize Agent Focus

Modify the `focus` field to specialize agents:
- "soft skills and communication"
- "interview preparation"
- "project portfolio building"
- "salary negotiation strategies"

### Change Funneling Logic

Edit `funnel_roadmaps()` method to:
- Weight agents differently (e.g., prefer technical over strategic)
- Use voting mechanisms
- Apply custom ranking algorithms

---

## 🐛 Troubleshooting

### Issue: "Groq API key not found"
**Solution**: Double-check `.env` file has `GROQ_API_KEY=...` with no spaces

### Issue: "Rate limit exceeded"
**Solution**: 
- Groq free tier: 30 req/min - add rate limiting
- Implement caching for common queries
- Use async generation with delays

### Issue: "One agent fails, whole system fails"
**Solution**: Already handled! Failed agents return empty responses with confidence 0, won't affect final output

### Issue: "Responses take too long"
**Solution**:
- Use async endpoint: `/api/v2/roadmap/generate-async`
- Shows "processing" status while agents work
- Poll with `/api/v2/roadmap/status/{task_id}`

---

## 💰 Cost Analysis (All FREE!)

| Service | Model | Free Tier | Cost After Free |
|---------|-------|-----------|-----------------|
| Groq | Llama 3.3 70B | 14,400 req/day | $0.59/1M tokens |
| Groq | Llama 3.1 8B | 14,400 req/day | $0.05/1M tokens |
| Google | Gemini Pro | 60 req/min | $0.50/1M tokens |
| HuggingFace | Various | Unlimited* | Free |

*Rate limited, but sufficient for development

**For your use case**: Completely free for development and moderate production use!

---

## 🎯 Next Steps

1. ✅ Set up API keys
2. ✅ Install dependencies
3. ✅ Add service and route files
4. ✅ Test with Swagger docs
5. ✅ Update frontend to use new endpoint
6. 🔄 Monitor performance for 1 week
7. 🔄 Gather user feedback
8. 🚀 Optimize based on results

---

## 📚 API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

All endpoints documented interactively!

---

## 💡 Pro Tips

1. **Start with 2 agents** (Groq + Gemini) if HuggingFace is slow
2. **Cache frequent queries** to save API calls
3. **Use async endpoint** for better UX with loading states
4. **Log everything** during initial testing
5. **Compare old vs new** roadmaps side-by-side before full migration

---

## 🤝 Need Help?

- Check logs: `tail -f Generative/logs/app.log`
- Test individual agents: Use the service directly in Python shell
- Discord/Reddit: Share your setup, get community help
- GitHub Issues: Create issue on the repo

---

**You're all set! 🚀**

Your Student Compass now has a powerful multi-agent system that:
- Uses 3 different AI perspectives
- Generates comprehensive, well-rounded roadmaps
- Costs $0 for development and testing
- Scales easily with more agents or models
