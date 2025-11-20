# Alternative Free AI API Providers

If you want to explore options beyond Groq + Gemini, here are other free AI API providers you can use for your multi-agent system.

---

## 🏆 Recommended Free Providers

### 1. **Groq** (RECOMMENDED - Currently Used)
- **Models**: Llama 3.3 70B, Llama 3.1 8B, Mixtral 8x7B
- **Free Tier**: 14,400 requests/day (30/min)
- **Speed**: Extremely fast (1000+ tokens/sec)
- **Setup**: Already in your code!
- **Pros**: Best performance, reliable, generous limits
- **Cons**: None for free tier

```python
# Already implemented in multi_agent_service.py
from groq import Groq
client = Groq(api_key="your_groq_key")
```

### 2. **Google Gemini** (Currently Used)
- **Models**: Gemini 1.5 Flash, Gemini 1.5 Pro
- **Free Tier**: 60 requests/min, 1500/day
- **Pros**: Good quality, already integrated
- **Cons**: Slower than Groq

```python
# Already implemented
import google.generativeai as genai
genai.configure(api_key="your_key")
```

### 3. **Cerebras Inference**
- **Models**: Llama 3.3 70B, Llama 3.1 8B/70B
- **Free Tier**: Similar to Groq
- **Pros**: Very fast, alternative to Groq
- **Website**: https://inference.cerebras.ai/

```python
# pip install openai
from openai import OpenAI

client = OpenAI(
    api_key="your_cerebras_key",
    base_url="https://api.cerebras.ai/v1"
)

response = client.chat.completions.create(
    model="llama3.1-70b",
    messages=[{"role": "user", "content": prompt}]
)
```

### 4. **Hyperbolic**
- **Models**: Llama 3.1 70B, Qwen 2.5 72B
- **Free Tier**: $10 free credits on signup
- **Pros**: Multiple model options
- **Website**: https://hyperbolic.xyz/

```python
# Compatible with OpenAI SDK
from openai import OpenAI

client = OpenAI(
    api_key="your_hyperbolic_key",
    base_url="https://api.hyperbolic.xyz/v1"
)
```

### 5. **Together AI**
- **Models**: Llama 3.1, Mixtral, many open source models
- **Free Tier**: $5 free credits on signup
- **Pros**: Many model choices
- **Website**: https://together.ai/

```python
# pip install together
from together import Together

client = Together(api_key="your_together_key")

response = client.chat.completions.create(
    model="meta-llama/Llama-3-70b-chat-hf",
    messages=[{"role": "user", "content": prompt}]
)
```

### 6. **Mistral AI**
- **Models**: Mistral Small, Mistral 7B
- **Free Tier**: Limited free tier
- **Pros**: Good for European users
- **Website**: https://mistral.ai/

```python
# pip install mistralai
from mistralai import Mistral

client = Mistral(api_key="your_mistral_key")

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": prompt}]
)
```

### 7. **HuggingFace Inference API**
- **Models**: Thousands of open source models
- **Free Tier**: Unlimited with rate limits
- **Pros**: Huge variety, truly free
- **Cons**: Can be slow, rate limits

```python
# Already partially implemented
import httpx

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.1-8B-Instruct"
headers = {"Authorization": f"Bearer {hf_token}"}

async with httpx.AsyncClient() as client:
    response = await client.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )
```

**Good HF Models for Your Use Case:**
- `meta-llama/Llama-3.1-8B-Instruct`
- `mistralai/Mixtral-8x7B-Instruct-v0.1`
- `HuggingFaceH4/zephyr-7b-beta`

### 8. **OpenRouter**
- **Models**: Access to 100+ models through one API
- **Free Tier**: Some free models available
- **Pros**: One API for many providers
- **Website**: https://openrouter.ai/

```python
# pip install openai
from openai import OpenAI

client = OpenAI(
    api_key="your_openrouter_key",
    base_url="https://openrouter.ai/api/v1"
)

# Use free models
response = client.chat.completions.create(
    model="google/gemma-2-9b-it:free",
    messages=[{"role": "user", "content": prompt}]
)
```

**Free Models on OpenRouter:**
- `google/gemma-2-9b-it:free`
- `meta-llama/llama-3.1-8b-instruct:free`
- `microsoft/phi-3-mini-128k-instruct:free`

---

## 🎨 Suggested Agent Configurations

### **Budget Setup** (All Free Forever)
```python
self.agents = {
    "agent_1": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile"  # Best free model
    },
    "agent_2": {
        "provider": "gemini",
        "model": "gemini-1.5-flash"  # Fast & free
    },
    "agent_3": {
        "provider": "groq",
        "model": "llama-3.1-8b-instant"  # Fast & free
    }
}
```

### **Quality Setup** (Mix of Free & Paid)
```python
self.agents = {
    "agent_1": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile"  # Free, powerful
    },
    "agent_2": {
        "provider": "gemini",
        "model": "gemini-1.5-pro"  # Free, high quality
    },
    "agent_3": {
        "provider": "cerebras",
        "model": "llama3.1-70b"  # Free, fast
    }
}
```

### **Diverse Setup** (Different Model Families)
```python
self.agents = {
    "agent_1": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile"  # Llama family
    },
    "agent_2": {
        "provider": "gemini",
        "model": "gemini-1.5-flash"  # Google family
    },
    "agent_3": {
        "provider": "openrouter",
        "model": "google/gemma-2-9b-it:free"  # Gemma family
    }
}
```

---

## 🔧 How to Add New Provider to Your Code

### Step 1: Add Provider Method

In `multi_agent_service.py`, add new method:

```python
async def _call_cerebras(self, model: str, prompt: str) -> str:
    """Call Cerebras Inference API"""
    from openai import OpenAI
    
    client = OpenAI(
        api_key=os.getenv("CEREBRAS_API_KEY"),
        base_url="https://api.cerebras.ai/v1"
    )
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert career advisor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.7
    )
    
    return response.choices[0].message.content
```

### Step 2: Update Agent Config

```python
self.agents = {
    # ... existing agents ...
    
    "agent_cerebras": {
        "name": "Strategic Advisor",
        "provider": "cerebras",  # New provider
        "model": "llama3.1-70b",
        "focus": "career strategy and planning"
    }
}
```

### Step 3: Add to Router Logic

In `generate_roadmap_with_agent`:

```python
if agent_config["provider"] == "groq":
    response = await self._call_groq(agent_config["model"], prompt)
elif agent_config["provider"] == "gemini":
    response = await self._call_gemini(prompt)
elif agent_config["provider"] == "cerebras":  # NEW
    response = await self._call_cerebras(agent_config["model"], prompt)
# ... etc
```

### Step 4: Add to .env

```bash
CEREBRAS_API_KEY=your_cerebras_key_here
```

---

## 📊 Provider Comparison Table

| Provider | Free Limit | Speed | Quality | Ease of Use |
|----------|-----------|-------|---------|-------------|
| Groq | 14.4k/day | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Gemini | 1.5k/day | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Cerebras | ~14k/day | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| HuggingFace | Unlimited* | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Together AI | $5 credit | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| OpenRouter | Varies | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Mistral | Limited | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

*Rate limited

---

## 💡 Optimization Tips

### 1. **Use Different Providers for Different Agents**
Don't put all eggs in one basket:
```python
# Agent 1: Groq (fast, good quality)
# Agent 2: Gemini (high quality, slower)
# Agent 3: Cerebras (fast alternative)
```

### 2. **Implement Fallbacks**
```python
try:
    response = await self._call_groq(model, prompt)
except Exception:
    # Fallback to another provider
    response = await self._call_cerebras(model, prompt)
```

### 3. **Cache Common Queries**
```python
import hashlib
import json

def get_cache_key(query, background):
    data = json.dumps({"query": query, "background": background}, sort_keys=True)
    return hashlib.md5(data.encode()).hexdigest()

# Check cache before calling agents
cache_key = get_cache_key(query, background)
if cache_key in cache:
    return cache[cache_key]
```

### 4. **Monitor Usage**
```python
# Track API usage
usage_stats = {
    "groq": {"calls": 0, "tokens": 0},
    "gemini": {"calls": 0, "tokens": 0},
    # ...
}
```

---

## 🚀 Quick Setup Commands

### Install All Clients
```bash
pip install groq google-generativeai openai together mistralai
```

### Get All Keys (5 min setup)
```bash
# 1. Groq (main provider)
echo "1. Visit: https://console.groq.com/keys"
echo "   Sign up → Create API Key → Copy"

# 2. Gemini (already have)
echo "2. Already have GOOGLE_GENAI_API_KEY"

# 3. Cerebras (backup)
echo "3. Visit: https://inference.cerebras.ai/"
echo "   Sign up → API Keys → Create"

# 4. HuggingFace (optional)
echo "4. Visit: https://huggingface.co/settings/tokens"
echo "   Create → Read access → Copy"
```

### Test All Providers
```bash
python -c "
import os
from groq import Groq
import google.generativeai as genai

print('Testing Groq...', end=' ')
try:
    Groq(api_key=os.getenv('GROQ_API_KEY'))
    print('✅')
except: print('❌')

print('Testing Gemini...', end=' ')
try:
    genai.configure(api_key=os.getenv('GOOGLE_GENAI_API_KEY'))
    print('✅')
except: print('❌')
"
```

---

## 🎯 Recommendation for Your Project

**Best Setup (100% Free):**
```
Agent 1: Groq (Llama 3.3 70B) - Strategic planning
Agent 2: Gemini (1.5 Flash) - Practical guidance  
Agent 3: Groq (Llama 3.1 8B) - Quick technical tips
Funneling: Groq (Llama 3.3 70B) - Best synthesis
```

**Why?**
- ✅ Completely free
- ✅ High quality outputs
- ✅ Fast response times
- ✅ Reliable infrastructure
- ✅ Generous rate limits (14k/day)

**Total cost**: $0/month even with heavy usage!

---

Need help setting up any specific provider? Let me know! 🚀
