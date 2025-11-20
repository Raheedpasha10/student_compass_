import json
import os
import requests
from typing import Dict, Any, List
from datetime import datetime
import re
import random

# Handle optional imports with try/except blocks
VERTEX_AI_AVAILABLE = False
GOOGLE_GENAI_AVAILABLE = False

try:
    from google.cloud import aiplatform as aiplatform_module
    from google.cloud import firestore as firestore_module
    from vertexai.generative_models import GenerativeModel as GenerativeModelClass
    VERTEX_AI_AVAILABLE = True
except ImportError:
    print("Warning: Vertex AI not available. Using fallback AI services.")
    # Create dummy modules to prevent NameError
    class DummyAiplatform:
        @staticmethod
        def init(*args, **kwargs):
            pass

    class DummyFirestore:
        class Client:
            def __init__(self, *args, **kwargs):
                pass

    class GenerativeModelClass:
        def __init__(self, *args, **kwargs):
            pass

        def generate_content(self, *args, **kwargs):
            class DummyResponse:
                def __init__(self):
                    self.text = ""
            return DummyResponse()

    aiplatform_module = DummyAiplatform()
    firestore_module = DummyFirestore()

try:
    import google.generativeai as genai_module
    GOOGLE_GENAI_AVAILABLE = True
except ImportError:
    print("Warning: Google Generative AI not available.")
    # Create dummy module to prevent NameError
    class DummyGenai:
        @staticmethod
        def configure(*args, **kwargs):
            pass

        class GenerativeModel:
            def __init__(self, *args, **kwargs):
                pass

            def generate_content(self, *args, **kwargs):
                class DummyResponse:
                    def __init__(self):
                        self.text = ""
                return DummyResponse()

    genai_module = DummyGenai()

from models.schemas import CareerPath, Course, RoadmapStep, MockTestQuestion

# Currency conversion utility


def convert_usd_to_inr(usd_range: str) -> str:
    """
    Convert USD salary range to INR
    Args:
        usd_range: String like '$60,000 - $120,000'
    Returns:
        String like '₹49.80 lakhs - ₹99.60 lakhs'
    """
    # Exchange rate: 1 USD = 88.09 INR (current rate)
    USD_TO_INR = 88.09

    # Extract numbers from USD range - use proper regex
    numbers = re.findall(r'\$([0-9,]+)', usd_range)
    if len(numbers) >= 2:
        try:
            # Remove commas and convert to int
            usd_min = int(numbers[0].replace(',', ''))
            usd_max = int(numbers[1].replace(',', ''))

            # Convert to INR
            inr_min = usd_min * USD_TO_INR
            inr_max = usd_max * USD_TO_INR

            # Format as Indian currency (with lakhs format)
            def format_inr(amount):
                # Convert to lakhs format for better readability
                if amount >= 10000000:  # 1 crore or more
                    crores = amount // 10000000
                    lakhs = (amount % 10000000) // 100000
                    if lakhs > 0:
                        return f"₹{crores}.{lakhs:02d} crores"
                    else:
                        return f"₹{crores} crores"
                elif amount >= 100000:  # 1 lakh or more
                    lakhs = amount // 100000
                    thousands = (amount % 100000) // 1000
                    if thousands > 0:
                        return f"₹{lakhs}.{thousands:02d} lakhs"
                    else:
                        return f"₹{lakhs} lakhs"
                else:
                    # Format with commas for amounts less than 1 lakh
                    return f"₹{amount:,}"

            return f"{format_inr(inr_min)} - {format_inr(inr_max)}"

        except ValueError:
            return usd_range  # Return original if conversion fails

    return usd_range  # Return original if parsing fails


class AIService:
    """Service for handling AI-related operations with multiple AI provider fallbacks"""

    def __init__(self):
        """Initialize the AI service with Vertex AI as primary and fallbacks"""
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")
        self.vertex_ai_available = VERTEX_AI_AVAILABLE
        self.model = None
        self.firestore_client = None

        # Initialize Vertex AI if available
        if self.vertex_ai_available:
            try:
                aiplatform_module.init(project=self.project_id)
                self.model = GenerativeModelClass("gemini-1.0-pro")
                print("✅ Vertex AI initialized successfully")
            except Exception as e:
                print(f"Warning: Could not initialize Vertex AI: {e}")
                self.vertex_ai_available = False

        # Initialize Firestore client with error handling
        if self.vertex_ai_available:
            try:
                self.firestore_client = firestore_module.Client(project=self.project_id)
            except Exception as e:
                print(f"Warning: Could not initialize Firestore client: {e}")
                self.firestore_client = None

        # Initialize fallback AI services
        self.fallback_apis = {
            'google_genai': self._init_google_genai(),
            'huggingface': self._init_huggingface(),
            'ollama': self._init_ollama(),
            'openai_free': self._init_openai_free(),
            'groq': self._init_groq()
        }

        print(f"🤖 AI Service initialized. Vertex AI: {'✅' if self.vertex_ai_available else '❌'}")
        available_fallbacks = [name for name, available in self.fallback_apis.items() if available]
        print(f"📡 Available fallback AI services: {available_fallbacks if available_fallbacks else 'None - using static responses'}")

        # If no AI services are available, inform user about setup options
        if not self.vertex_ai_available and not any(self.fallback_apis.values()):
            print("\n⚠️  No AI services configured!")
            print("To enable AI features, you can:")
            print("1. Use Google Generative AI (Gemini): Add GOOGLE_GENAI_API_KEY to .env")
            print("2. Use Hugging Face: Add HUGGINGFACE_API_KEY to .env")
            print("3. Use Ollama: Install from https://ollama.com/ and run locally")
            print("4. Use Groq: Add GROQ_API_KEY to .env")
            print("5. Use OpenAI-compatible services: Add OPENAI_FREE_API_URL and OPENAI_FREE_API_KEY to .env")

    def _init_google_genai(self) -> bool:
        """Initialize Google Generative AI API (Gemini)"""
        try:
            # Try both the SDK and direct REST API approach
            api_key = os.getenv('GOOGLE_GENAI_API_KEY', '')
            if not api_key or api_key == 'your_google_gemini_api_key_here':
                print("⚠️  Google Generative AI API key not found or not configured in .env file")
                return False

            # Set up for direct REST API calls
            self.google_genai_api_key = api_key
            self.google_genai_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

            if GOOGLE_GENAI_AVAILABLE:
                # Also set up the SDK if available
                genai_module.configure(api_key=api_key)
                self.genai_model = genai_module.GenerativeModel('gemini-1.5-flash')
                print("✅ Google Generative AI (Gemini) initialized successfully with SDK")
            else:
                print("✅ Google Generative AI (Gemini) initialized for direct REST API calls")

            return True
        except Exception as e:
            print(f"Warning: Could not initialize Google Generative AI: {e}")
            return False

    def _init_huggingface(self) -> bool:
        """Initialize Hugging Face API (free tier available)"""
        try:
            # Hugging Face provides free API access
            self.hf_api_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
            # You can also use: facebook/blenderbot-400M-distill, microsoft/DialoGPT-medium
            self.hf_headers = {
                "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY', '')}",
                "Content-Type": "application/json"
            }
            return True
        except Exception as e:
            print(f"Warning: Could not initialize Hugging Face API: {e}")
            return False

    def _init_ollama(self) -> bool:
        """Initialize Ollama (local AI models - completely free)"""
        try:
            # Check if Ollama is running locally
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            if response.status_code == 200:
                self.ollama_url = "http://localhost:11434/api/generate"
                print("✅ Ollama detected locally")
                return True
        except:
            pass
        return False

    def _init_groq(self) -> bool:
        """Initialize Groq API (fast and free)"""
        try:
            self.groq_api_key = os.getenv('GROQ_API_KEY', '')
            self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
            return bool(self.groq_api_key)
        except:
            return False

    def _init_openai_free(self) -> bool:
        """Initialize OpenAI-compatible free APIs"""
        try:
            # Free OpenAI-compatible APIs like Together AI, Groq, etc.
            self.openai_free_url = os.getenv('OPENAI_FREE_API_URL', '')
            self.openai_free_key = os.getenv('OPENAI_FREE_API_KEY', '')
            return bool(self.openai_free_url and self.openai_free_key)
        except:
            return False

    def _generate_with_fallback_ai(self, prompt: str) -> str:
        """Try different AI services as fallbacks with enhanced Gemini integration"""

        # Try Google Generative AI first (Gemini) - Primary service
        if self.fallback_apis['google_genai']:
            try:
                # Try SDK first if available
                if hasattr(self, 'genai_model'):
                    # Enhanced configuration for better responses
                    generation_config = {
                        "temperature": 0.7,
                        "top_p": 0.9,
                        "top_k": 40,
                        "max_output_tokens": 1000,
                    }

                    response = self.genai_model.generate_content(
                        prompt,
                        generation_config=generation_config
                    )
                    if response.text:
                        print("✅ Generated personalized content using Google Generative AI (Gemini SDK)")
                        return response.text

                # Fallback to direct REST API call with enhanced configuration
                elif hasattr(self, 'google_genai_url'):
                    payload = {
                        "contents": [{
                            "parts": [{
                                "text": prompt
                            }]
                        }],
                        "generationConfig": {
                            "temperature": 0.7,
                            "topP": 0.9,
                            "topK": 40,
                            "maxOutputTokens": 1000,
                            "stopSequences": []
                        },
                        "safetySettings": [
                            {
                                "category": "HARM_CATEGORY_HARASSMENT",
                                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                            },
                            {
                                "category": "HARM_CATEGORY_HATE_SPEECH",
                                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                            },
                            {
                                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                            },
                            {
                                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                            }
                        ]
                    }
                    response = requests.post(
                        self.google_genai_url,
                        json=payload,
                        headers={"Content-Type": "application/json"},
                        timeout=45  # Increased timeout for better responses
                    )
                    if response.status_code == 200:
                        result = response.json()
                        if 'candidates' in result and result['candidates']:
                            text = result['candidates'][0]['content']['parts'][0]['text']
                            print("✅ Generated personalized content using Google Generative AI (REST API)")
                            return text
                    else:
                        print(f"Gemini API error: {response.status_code} - {response.text}")

            except Exception as e:
                print(f"Google Generative AI request failed: {e}")

        # Try Ollama second (local, completely free)
        if self.fallback_apis['ollama']:
            try:
                response = requests.post(
                    self.ollama_url,
                    json={
                        "model": "llama2",  # or "mistral", "codellama", etc.
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=30
                )
                if response.status_code == 200:
                    result = response.json()
                    if 'response' in result:
                        print("✅ Generated content using Ollama (local AI)")
                        return result['response']
            except Exception as e:
                print(f"Ollama request failed: {e}")

        # Try Hugging Face API
        if self.fallback_apis['huggingface']:
            try:
                # Use a better model for generation
                hf_generation_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
                response = requests.post(
                    hf_generation_url,
                    headers=self.hf_headers,
                    json={
                        "inputs": prompt,
                        "parameters": {
                            "max_length": 1000,
                            "temperature": 0.7,
                            "do_sample": True
                        }
                    },
                    timeout=30
                )
                if response.status_code == 200:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0:
                        print("✅ Generated content using Hugging Face API")
                        return result[0].get('generated_text', '')
            except Exception as e:
                print(f"Hugging Face request failed: {e}")

        # Try Groq API (fast and free)
        if self.fallback_apis['groq']:
            try:
                response = requests.post(
                    self.groq_url,
                    headers={
                        "Authorization": f"Bearer {self.groq_api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "mixtral-8x7b-32768",
                        "messages": [{"role": "user", "content": prompt}],
                        "max_tokens": 1000,
                        "temperature": 0.7
                    },
                    timeout=30
                )
                if response.status_code == 200:
                    result = response.json()
                    if 'choices' in result and len(result['choices']) > 0:
                        print("✅ Generated content using Groq API")
                        return result['choices'][0]['message']['content']
            except Exception as e:
                print(f"Groq request failed: {e}")

        # Try OpenAI-compatible free API
        if self.fallback_apis['openai_free']:
            try:
                response = requests.post(
                    f"{self.openai_free_url}/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.openai_free_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "gpt-3.5-turbo",  # or whatever model the service provides
                        "messages": [{"role": "user", "content": prompt}],
                        "max_tokens": 1000,
                        "temperature": 0.7
                    },
                    timeout=30
                )
                if response.status_code == 200:
                    result = response.json()
                    if 'choices' in result and len(result['choices']) > 0:
                        print("✅ Generated content using OpenAI-compatible API")
                        return result['choices'][0]['message']['content']
            except Exception as e:
                print(f"OpenAI-compatible API request failed: {e}")

        # If all AI services fail, return empty string (caller handles fallback)
        print("⚠️ All AI services failed, using static fallback")
        return ""

    def generate_personalized_roadmap(self, user_skills: str, career_goal: str, experience_level: str) -> str:
        """
        Generate a personalized career roadmap using Gemini AI
        """
        roadmap_prompt = f"""
Create a detailed, personalized career roadmap for someone with the following profile:

Current Skills: {user_skills or "Beginner level"}
Career Goal: {career_goal}
Experience Level: {experience_level}

Provide a comprehensive roadmap that includes:

1. **Immediate Actions (Next 30 days):**
   - 2-3 specific tasks they should start immediately
   - Skills to focus on first
   - Resources to begin with

2. **Short-term Goals (3-6 months):**
   - Key milestones to achieve
   - Skills to develop
   - Projects to build
   - Certifications to pursue

3. **Medium-term Goals (6-12 months):**
   - Advanced skills to master
   - Portfolio projects
   - Networking opportunities
   - Job search preparation

4. **Long-term Vision (1-2 years):**
   - Career advancement opportunities
   - Leadership skills development
   - Specialization areas

5. **Specific Resources:**
   - Recommended courses (with platforms)
   - Books to read
   - Tools to learn
   - Communities to join

6. **Success Metrics:**
   - How to measure progress
   - Key performance indicators
   - Portfolio pieces to create

Make this roadmap actionable, specific, and tailored to their current skill level. Include realistic timelines and practical next steps.
Make the tone friendly and encouraging, like a helpful mentor guiding a friend through their career journey.
        """

        ai_response = self._generate_with_fallback_ai(roadmap_prompt)

        if ai_response:
            return ai_response

        # Fallback roadmap if AI is unavailable
        return f"""
🗺️ **Your Personalized Career Roadmap**

Hey there, future rockstar! 👋 I'm so excited to help guide you on your journey to becoming a {career_goal}! Let's break this down into manageable steps that will set you up for success.

**Current Status:** {experience_level} with skills in {user_skills or "foundational areas"}
**Target Goal:** {career_goal}

**🚀 Immediate Actions (Next 30 days):**
1. Assess your current skill gaps - we'll figure out exactly where you are and where you want to go!
2. Set up a dedicated learning schedule (1-2 hours daily) - consistency is key to success! 💪
3. Create accounts on key learning platforms - time to get access to all those amazing resources!

**🎯 Short-term Goals (3-6 months):**
1. Complete 2-3 foundational courses - you've got this! 📚
2. Build your first portfolio project - this will be something you'll be proud to show off!
3. Join relevant online communities - connect with others on the same journey!
4. Start following industry leaders - get inspired by those who've walked this path before you!

**📈 Medium-term Goals (6-12 months):**
1. Complete an advanced certification - level up your skills! 🏆
2. Build 3-5 portfolio projects - create a showcase of your amazing work!
3. Start networking in your field - make friends and connections in the industry!
4. Apply for relevant positions - you'll be ready to take on the world!

**🌟 Long-term Vision (1-2 years):**
1. Secure your target role - your dream job is waiting for you!
2. Develop leadership skills - inspire and guide others as you've been guided!
3. Consider specialization areas - become the go-to expert in your niche!
4. Mentor others in your journey - pay it forward and help the next generation!

**📚 Recommended Resources:**
- Online platforms: Coursera, Udemy, freeCodeCamp - so many great options!
- Books: Industry-specific bestsellers - knowledge is power! 📖
- Tools: Popular industry software - get hands-on experience!
- Communities: LinkedIn groups, Discord servers - connect with your tribe!

**📉 Track Your Progress:**
- Weekly skill assessments - celebrate your growth every week!
- Monthly portfolio updates - see how far you've come!
- Quarterly goal reviews - adjust and optimize as you learn more about yourself!

Remember, every expert was once a beginner. You've got this, and I'm cheering you on every step of the way! 🌈✨
        """

    def generate_career_analysis(self, skills: str, expertise: str) -> Dict[str, Any]:
        """Generate career analysis using available AI services with fallbacks"""

        prompt = f"""
        Create a career analysis for someone with these skills: {skills} and expertise: {expertise}
        
        You MUST respond with ONLY valid JSON in this exact format (no markdown, no extra text):

        {{
            "career_paths": [
                {{
                    "title": "Data Scientist",
                    "description": "Analyze data to drive business decisions", 
                    "required_skills": ["Python", "Statistics", "Machine Learning"],
                    "salary_range": "₹15-30 lakhs",
                    "growth_prospect": "High - Growing demand"
                }},
                {{
                    "title": "ML Engineer", 
                    "description": "Build machine learning systems",
                    "required_skills": ["Python", "TensorFlow", "Docker"],
                    "salary_range": "₹18-35 lakhs", 
                    "growth_prospect": "Very High - AI boom"
                }},
                {{
                    "title": "Backend Developer",
                    "description": "Develop server-side applications", 
                    "required_skills": ["Python", "Django", "PostgreSQL"],
                    "salary_range": "₹12-25 lakhs",
                    "growth_prospect": "High - Always in demand"
                }}
            ],
            "selected_path": {{
                "title": "Data Scientist",
                "description": "Best match for your skills",
                "required_skills": ["Python", "Statistics", "Machine Learning"], 
                "salary_range": "₹15-30 lakhs",
                "growth_prospect": "High - Growing field"
            }},
            "roadmap": [
                {{
                    "step": 1,
                    "title": "Master Python Fundamentals", 
                    "description": "Strengthen your Python programming skills",
                    "duration": "2-3 months",
                    "resources": ["Python Crash Course by Eric Matthes", "Automate the Boring Stuff with Python", "Python.org official tutorial"]
                }},
                {{
                    "step": 2,
                    "title": "Learn Data Science Libraries",
                    "description": "Master pandas, numpy, and matplotlib", 
                    "duration": "2-3 months",
                    "resources": ["Python for Data Analysis by Wes McKinney", "Pandas documentation", "Kaggle Learn Data Visualization course"]
                }}
            ],
            "courses": [
                {{
                    "title": "Complete Python Bootcamp From Zero to Hero",
                    "provider": "Udemy",
                    "duration": "22 hours", 
                    "difficulty": "Beginner",
                    "url": "https://www.udemy.com/course/complete-python-bootcamp/"
                }},
                {{
                    "title": "Python for Data Science and Machine Learning",
                    "provider": "Coursera", 
                    "duration": "6 weeks",
                    "difficulty": "Intermediate", 
                    "url": "https://www.coursera.org/learn/python-for-applied-data-science-ai"
                }}
            ],
            "certifications": [
                {{
                    "name": "Microsoft Certified: Azure Data Scientist Associate",
                    "provider": "Microsoft",
                    "description": "Industry-recognized data science certification",
                    "difficulty": "Intermediate",
                    "duration": "3-4 months", 
                    "url": "https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist/"
                }}
            ]
        }}

        Generate realistic recommendations based on the user's skills: {skills} and expertise level: {expertise}
        """

        # Try Vertex AI first if available
        if self.vertex_ai_available and self.model:
            try:
                response = self.model.generate_content(prompt)
                response_text = response.text

                # Extract JSON from response
                start_idx = response_text.find('{')
                end_idx = response_text.rfind('}') + 1

                if start_idx != -1 and end_idx != -1:
                    json_str = response_text[start_idx:end_idx]
                    result = json.loads(json_str)
                    print("✅ Generated career analysis using Vertex AI")
                    return result

            except Exception as e:
                print(f"Vertex AI generation failed: {e}")

        # Try fallback AI services
        ai_response = self._generate_with_fallback_ai(prompt)
        if ai_response:
            print(f"🔍 AI Response received (length: {len(ai_response)})")
            print(f"🔍 First 300 chars: {ai_response[:300]}...")
            try:
                # Try to extract JSON from AI response
                start_idx = ai_response.find('{')
                end_idx = ai_response.rfind('}') + 1

                if start_idx != -1 and end_idx != -1:
                    json_str = ai_response[start_idx:end_idx]
                    print(f"🔍 Extracted JSON (length: {len(json_str)})")
                    # Try to fix common JSON issues
                    try:
                        result = json.loads(json_str)
                        print("✅ Successfully parsed AI-generated JSON!")
                        return result
                    except json.JSONDecodeError as e:
                        print(f"❌ JSON parsing error: {e}")
                        # Try to fix common JSON issues
                        fixed_json = self._fix_json_format(json_str)
                        if fixed_json:
                            result = json.loads(fixed_json)
                            print("✅ Successfully parsed fixed JSON!")
                            return result
                        else:
                            print(f"❌ Could not fix JSON format")
                            print(f"JSON string: {json_str[:200]}...")  # Print first 200 chars for debugging
                else:
                    print("❌ No JSON structure found in AI response")
            except Exception as e:
                print(f"❌ Error parsing AI response: {e}")
                if 'ai_response' in locals():
                    print(f"Response preview: {ai_response[:200] if ai_response else 'No response'}...")
        else:
            print("❌ No AI response received")

        # Fallback to static response
        print("📊 Using enhanced static career analysis")
        return self._create_enhanced_fallback_response(skills, expertise)

    def _fix_json_format(self, json_str: str) -> str:
        """Attempt to fix common JSON formatting issues"""
        try:
            # Remove any text before the first {
            first_brace = json_str.find('{')
            if first_brace > 0:
                json_str = json_str[first_brace:]

            # Remove any text after the last }
            last_brace = json_str.rfind('}')
            if last_brace > 0 and last_brace < len(json_str) - 1:
                json_str = json_str[:last_brace + 1]

            # Fix common issues
            import re

            # Fix trailing commas
            json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)

            # Try to fix unquoted keys (this is a simple approach)
            json_str = re.sub(r'([{,]\s*)([a-zA-Z_][a-zA-Z0-9_]*)\s*:', r'\1"\2":', json_str)

            # Try to fix single quotes around strings
            # This is a simplified approach - a full JSON parser would be better
            parts = json_str.split('"')
            for i in range(1, len(parts) - 1, 2):
                # Skip even indices (they're outside quotes)
                continue
            # For odd indices, they're inside quotes, so we don't modify them

            return json_str
        except Exception as e:
            print(f"Error fixing JSON format: {e}")
            return ""

    def _create_enhanced_fallback_response(self, skills: str, expertise: str) -> Dict[str, Any]:
        """Create an enhanced fallback response that adapts to user's skills"""

        skills_lower = skills.lower()

        # Enhanced domain detection with comprehensive skill mapping
        domain_keywords = {
            'software_development': [
                'programming', 'coding', 'software', 'web development', 'app development',
                'python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'swift',
                'react', 'vue', 'angular', 'node.js', 'django', 'flask', 'spring', 'laravel',
                'frontend', 'backend', 'fullstack', 'full-stack', 'api', 'microservices'
            ],
            'data_science': [
                'data science', 'data analysis', 'machine learning', 'artificial intelligence',
                'deep learning', 'neural networks', 'statistics', 'analytics', 'big data',
                'pandas', 'numpy', 'tensorflow', 'pytorch', 'scikit-learn', 'r', 'tableau',
                'power bi', 'sql', 'data visualization', 'predictive modeling', 'nlp',
                'computer vision', 'data mining', 'business intelligence'
            ],
            'mobile_development': [
                'mobile', 'android', 'ios', 'react native', 'flutter', 'xamarin', 'ionic',
                'swift', 'kotlin', 'objective-c', 'mobile app', 'app store', 'play store',
                'mobile ui', 'responsive design', 'cross-platform'
            ],
            'game_development': [
                'game development', 'unity', 'unreal engine', 'godot', 'game design',
                'graphics programming', 'shader', '3d modeling', 'animation', 'blender',
                'c++', 'c#', 'lua', 'gamemaker', 'indie game', 'aaa game'
            ],
            'devops_cloud': [
                'devops', 'cloud', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform',
                'ansible', 'jenkins', 'ci/cd', 'infrastructure', 'deployment', 'monitoring',
                'microservices', 'containers', 'serverless', 'cloud architecture'
            ],
            'cybersecurity': [
                'cybersecurity', 'security', 'penetration testing', 'ethical hacking',
                'network security', 'information security', 'vulnerability assessment',
                'security analysis', 'cryptography', 'firewall', 'malware analysis'
            ],
            'design_ux': [
                'ui/ux', 'design', 'user experience', 'user interface', 'graphic design',
                'web design', 'figma', 'sketch', 'adobe', 'photoshop', 'illustrator',
                'wireframing', 'prototyping', 'design thinking', 'visual design'
            ],
            'business_analysis': [
                'business analysis', 'product management', 'project management', 'scrum',
                'agile', 'requirements analysis', 'stakeholder management', 'process improvement',
                'business intelligence', 'market research', 'strategy'
            ],
            'digital_marketing': [
                'digital marketing', 'seo', 'sem', 'social media', 'content marketing',
                'email marketing', 'google analytics', 'facebook ads', 'google ads',
                'marketing automation', 'lead generation', 'conversion optimization'
            ],
            'blockchain_web3': [
                'blockchain', 'cryptocurrency', 'bitcoin', 'ethereum', 'smart contracts',
                'defi', 'nft', 'web3', 'solidity', 'dapp', 'decentralized', 'crypto'
            ],
            'ai_ml_engineering': [
                'ai engineering', 'ml engineering', 'mlops', 'model deployment',
                'ai infrastructure', 'model optimization', 'edge ai', 'production ml',
                'ai scalability', 'model monitoring'
            ],
            'quality_assurance': [
                'qa', 'quality assurance', 'testing', 'test automation', 'selenium',
                'cypress', 'jest', 'unit testing', 'integration testing', 'performance testing',
                'manual testing', 'bug tracking', 'test planning'
            ],
            'engineering_hardware': [
                'hardware', 'embedded systems', 'circuit design', 'pcb design', 'vhdl', 'verilog',
                'fpga', 'microcontroller', 'arduino', 'raspberry pi', 'electronics', 'iot'
            ],
            'medicine_general': [
                'medicine', 'medical', 'patient care', 'diagnosis', 'treatment', 'healthcare',
                'clinical', 'hospital', 'doctor', 'physician'
            ],
            'medicine_surgery': [
                'surgery', 'surgical', 'operation', 'operative', 'anatomy', 'surgeon'
            ],
            'medicine_pediatrics': [
                'pediatrics', 'child', 'children', 'baby', 'infant', 'toddler'
            ],
            'medicine_psychiatry': [
                'psychiatry', 'mental health', 'psychology', 'therapy', 'counseling'
            ],
            'medicine_dermatology': [
                'dermatology', 'skin', 'hair', 'nails', 'cosmetic'
            ],
            'medicine_cardiology': [
                'cardiology', 'heart', 'cardiac', 'cardiovascular', 'ecg', 'echocardiography'
            ],
            'medicine_neurology': [
                'neurology', 'brain', 'nervous system', 'neuroscience', 'neurosurgery'
            ],
            'medicine_orthopedics': [
                'orthopedics', 'bones', 'joints', 'muscles', 'spine', 'sports medicine'
            ],
            'medicine_ophthalmology': [
                'ophthalmology', 'eye', 'vision', 'optometry', 'optometrist'
            ],
            'medicine_gynecology': [
                'gynecology', 'women', 'reproductive', 'obstetrics', 'pregnancy'
            ],
            'medicine_radiology': [
                'radiology', 'x-ray', 'mri', 'ct scan', 'imaging', 'radiologist'
            ],
            'medicine_anesthesiology': [
                'anesthesiology', 'anesthesia', 'pain management', 'critical care'
            ],
            'business_finance': [
                'finance', 'financial', 'accounting', 'investment', 'banking', 'corporate finance'
            ],
            'business_marketing': [
                'marketing', 'advertising', 'branding', 'campaign', 'seo', 'sem'
            ],
            'business_hr': [
                'human resources', 'hr', 'recruitment', 'talent', 'employee', 'staffing'
            ],
            'business_operations': [
                'operations', 'supply chain', 'logistics', 'process', 'optimization', 'quality'
            ],
            'creative_design': [
                'graphic design', 'illustration', 'photoshop', 'adobe', 'creative', 'art'
            ],
            'creative_writing': [
                'writing', 'content', 'copywriting', 'author', 'journalism', 'editor'
            ],
            'creative_video': [
                'video', 'filmmaking', 'editing', 'cinematography', 'youtube', 'tiktok'
            ],
            'creative_music': [
                'music', 'audio', 'sound', 'instrument', 'composition', 'performance'
            ],
            'education_teaching': [
                'teaching', 'education', 'teacher', 'tutor', 'classroom', 'instruction'
            ],
            'education_training': [
                'training', 'corporate training', 'workshop', 'facilitation', 'instructional'
            ],
            'education_research': [
                'research', 'academic', 'phd', 'thesis', 'data collection', 'methodology'
            ],
            'legal_corporate': [
                'corporate law', 'contract', 'merger', 'acquisition', 'compliance'
            ],
            'legal_criminal': [
                'criminal law', 'court', 'prosecution', 'defense', 'criminal justice'
            ],
            'legal_family': [
                'family law', 'divorce', 'custody', 'marriage', 'child support'
            ]
        }

        # Determine primary domain based on comprehensive keyword matching
        domain_scores = {}
        for domain, keywords in domain_keywords.items():
            score = sum(1 for keyword in keywords if keyword in skills_lower)
            if score > 0:
                domain_scores[domain] = score

        # Get the domain with highest keyword matches, default to a random domain from all options
        if domain_scores:
            primary_domain = max(domain_scores.keys(), key=lambda k: domain_scores[k])
        else:
            # If no matches, randomly select from all domains to ensure variety
            all_domains = list(domain_keywords.keys())
            primary_domain = random.choice(all_domains)

        # Enhanced comprehensive domain responses for ALL career fields
        domain_responses = {
            'software_development': {
                'career_paths': [
                    {
                        'title': 'Software Engineer',
                        'description': 'Design and develop software systems and applications. As a friendly guide, I\'d say this is an exciting path where you get to build amazing things that can impact millions of lives! 🚀',
                        'required_skills': ['Programming Languages', 'Data Structures', 'System Design', 'Testing'],
                        'salary_range': convert_usd_to_inr('$80,000 - $150,000'),
                        'growth_prospect': 'High - Technology sector continues to grow rapidly'
                    },
                    {
                        'title': 'DevOps Engineer',
                        'description': 'Automate and optimize software delivery pipelines. This role is like being the bridge between development and operations - making sure everything runs smoothly! 🌉',
                        'required_skills': ['Docker', 'Kubernetes', 'CI/CD', 'Infrastructure as Code', 'Monitoring'],
                        'salary_range': convert_usd_to_inr('$85,000 - $140,000'),
                        'growth_prospect': 'Very High - Critical for modern software delivery'
                    },
                    {
                        'title': 'Technical Lead',
                        'description': 'Lead development teams and guide technical decisions. As a leader, you\'ll be mentoring others and making important technology choices - it\'s both challenging and rewarding! 🌟',
                        'required_skills': ['Leadership', 'Architecture', 'Project Management', 'Mentoring'],
                        'salary_range': convert_usd_to_inr('$100,000 - $180,000'),
                        'growth_prospect': 'High - Leadership roles are in high demand'
                    }
                ]
            },
            'data_science': {
                'career_paths': [
                    {
                        'title': 'Data Scientist',
                        'description': 'Extract insights from data to drive business decisions. You\'ll be like a detective, uncovering hidden patterns in data to help companies make better decisions! 🔍',
                        'required_skills': ['Python', 'Statistics', 'Machine Learning', 'SQL', 'Data Visualization'],
                        'salary_range': convert_usd_to_inr('$90,000 - $160,000'),
                        'growth_prospect': 'High - Data-driven decision making is crucial'
                    },
                    {
                        'title': 'Machine Learning Engineer',
                        'description': 'Build and deploy machine learning models. This is where you get to create intelligent systems that can learn and improve over time - like teaching computers to think! 🤖',
                        'required_skills': ['Python', 'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch'],
                        'salary_range': convert_usd_to_inr('$95,000 - $170,000'),
                        'growth_prospect': 'Very High - AI and ML are transforming industries'
                    },
                    {
                        'title': 'Data Engineer',
                        'description': 'Design and build data pipelines and infrastructure. You\'ll be the architect behind the scenes, making sure data flows smoothly to where it\'s needed! 🏗️',
                        'required_skills': ['SQL', 'Data Warehousing', 'ETL', 'Big Data Technologies'],
                        'salary_range': convert_usd_to_inr('$85,000 - $150,000'),
                        'growth_prospect': 'High - Data infrastructure is essential'
                    }
                ]
            },
            'mobile_development': {
                'career_paths': [
                    {
                        'title': 'Mobile Developer',
                        'description': 'Build mobile applications for iOS and Android',
                        'required_skills': ['Swift', 'Kotlin', 'Java', 'React Native', 'Flutter'],
                        'salary_range': convert_usd_to_inr('$75,000 - $140,000'),
                        'growth_prospect': 'High - Mobile app usage is growing'
                    },
                    {
                        'title': 'Mobile UI/UX Designer',
                        'description': 'Design user interfaces and experiences for mobile apps',
                        'required_skills': ['UI/UX Design', 'Wireframing', 'Prototyping', 'User Research'],
                        'salary_range': convert_usd_to_inr('$70,000 - $130,000'),
                        'growth_prospect': 'High - User experience is key'
                    },
                    {
                        'title': 'Mobile Game Developer',
                        'description': 'Create games for mobile platforms',
                        'required_skills': ['Unity', 'Unreal Engine', 'C#', 'Game Design'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - Mobile gaming is popular'
                    }
                ]
            },
            'game_development': {
                'career_paths': [
                    {
                        'title': 'Game Developer',
                        'description': 'Create video games',
                        'required_skills': ['Unity', 'Unreal Engine', 'C#', 'Game Design'],
                        'salary_range': convert_usd_to_inr('$75,000 - $140,000'),
                        'growth_prospect': 'High - Gaming industry is expanding'
                    },
                    {
                        'title': 'Game Designer',
                        'description': 'Design game mechanics and experiences',
                        'required_skills': ['Game Design', 'Storyboarding', 'Prototyping', 'User Research'],
                        'salary_range': convert_usd_to_inr('$70,000 - $130,000'),
                        'growth_prospect': 'High - Creative design is essential'
                    },
                    {
                        'title': 'Game Artist',
                        'description': 'Create visual assets for games',
                        'required_skills': ['3D Modeling', 'Animation', 'Blender', 'Photoshop'],
                        'salary_range': convert_usd_to_inr('$75,000 - $140,000'),
                        'growth_prospect': 'High - Visuals are key'
                    }
                ]
            },
            'devops_cloud': {
                'career_paths': [
                    {
                        'title': 'DevOps Engineer',
                        'description': 'Automate and optimize software delivery pipelines',
                        'required_skills': ['Docker', 'Kubernetes', 'CI/CD', 'Infrastructure as Code', 'Monitoring'],
                        'salary_range': convert_usd_to_inr('$85,000 - $140,000'),
                        'growth_prospect': 'Very High - Critical for modern software delivery'
                    },
                    {
                        'title': 'Cloud Engineer',
                        'description': 'Design and manage cloud infrastructure',
                        'required_skills': ['AWS', 'Azure', 'GCP', 'Networking', 'Security'],
                        'salary_range': convert_usd_to_inr('$90,000 - $160,000'),
                        'growth_prospect': 'High - Cloud computing is essential'
                    },
                    {
                        'title': 'Site Reliability Engineer',
                        'description': 'Ensure system reliability and performance',
                        'required_skills': ['Linux', 'Monitoring', 'Automation', 'Incident Response'],
                        'salary_range': convert_usd_to_inr('$95,000 - $170,000'),
                        'growth_prospect': 'High - Reliability is critical'
                    }
                ]
            },
            'cybersecurity': {
                'career_paths': [
                    {
                        'title': 'Cybersecurity Analyst',
                        'description': 'Identify and mitigate security threats',
                        'required_skills': ['Network Security', 'Vulnerability Assessment', 'Security Analysis'],
                        'salary_range': convert_usd_to_inr('$75,000 - $140,000'),
                        'growth_prospect': 'High - Security is a top priority'
                    },
                    {
                        'title': 'Penetration Tester',
                        'description': 'Test systems for security vulnerabilities',
                        'required_skills': ['Penetration Testing', 'Ethical Hacking', 'Security Analysis'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - Testing is essential'
                    },
                    {
                        'title': 'Security Engineer',
                        'description': 'Design and implement security solutions',
                        'required_skills': ['Security Engineering', 'Networking', 'Security Analysis'],
                        'salary_range': convert_usd_to_inr('$90,000 - $160,000'),
                        'growth_prospect': 'High - Solutions are critical'
                    }
                ]
            },
            'design_ux': {
                'career_paths': [
                    {
                        'title': 'UI/UX Designer',
                        'description': 'Design user interfaces and experiences',
                        'required_skills': ['UI/UX Design', 'Wireframing', 'Prototyping', 'User Research'],
                        'salary_range': convert_usd_to_inr('$70,000 - $130,000'),
                        'growth_prospect': 'High - User experience is key'
                    },
                    {
                        'title': 'Graphic Designer',
                        'description': 'Create visual designs for various media',
                        'required_skills': ['Graphic Design', 'Photoshop', 'Illustrator', 'Adobe'],
                        'salary_range': convert_usd_to_inr('$75,000 - $140,000'),
                        'growth_prospect': 'High - Visuals are essential'
                    },
                    {
                        'title': 'Product Designer',
                        'description': 'Design products from concept to launch',
                        'required_skills': ['Product Design', 'User Research', 'Prototyping', 'Collaboration'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - Products are key'
                    }
                ]
            },
            'business_analysis': {
                'career_paths': [
                    {
                        'title': 'Business Analyst',
                        'description': 'Analyze business processes and data',
                        'required_skills': ['Business Analysis', 'Requirements Analysis', 'Stakeholder Management'],
                        'salary_range': convert_usd_to_inr('$70,000 - $130,000'),
                        'growth_prospect': 'High - Analysis is essential'
                    },
                    {
                        'title': 'Product Manager',
                        'description': 'Manage product development and launch',
                        'required_skills': ['Product Management', 'Agile', 'Stakeholder Management'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - Products are key'
                    },
                    {
                        'title': 'Project Manager',
                        'description': 'Manage projects from start to finish',
                        'required_skills': ['Project Management', 'Agile', 'Stakeholder Management'],
                        'salary_range': convert_usd_to_inr('$85,000 - $140,000'),
                        'growth_prospect': 'High - Projects are essential'
                    }
                ]
            },
            'digital_marketing': {
                'career_paths': [
                    {
                        'title': 'Digital Marketing Specialist',
                        'description': 'Plan and execute digital marketing campaigns',
                        'required_skills': ['SEO', 'SEM', 'Social Media', 'Content Marketing'],
                        'salary_range': convert_usd_to_inr('$70,000 - $130,000'),
                        'growth_prospect': 'High - Digital marketing is essential'
                    },
                    {
                        'title': 'SEO Specialist',
                        'description': 'Optimize websites for search engines',
                        'required_skills': ['SEO', 'Keyword Research', 'On-page Optimization', 'Technical SEO'],
                        'salary_range': convert_usd_to_inr('$75,000 - $140,000'),
                        'growth_prospect': 'High - SEO is critical'
                    },
                    {
                        'title': 'Content Marketing Specialist',
                        'description': 'Create and distribute content',
                        'required_skills': ['Content Marketing', 'Copywriting', 'SEO', 'Social Media'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - Content is key'
                    }
                ]
            },
            'blockchain_web3': {
                'career_paths': [
                    {
                        'title': 'Blockchain Developer',
                        'description': 'Build blockchain applications',
                        'required_skills': ['Solidity', 'Blockchain', 'Smart Contracts', 'DApps'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - Blockchain is growing'
                    },
                    {
                        'title': 'Blockchain Analyst',
                        'description': 'Analyze blockchain technologies and applications',
                        'required_skills': ['Blockchain', 'Smart Contracts', 'Cryptocurrency', 'Security'],
                        'salary_range': convert_usd_to_inr('$75,000 - $140,000'),
                        'growth_prospect': 'High - Analysis is essential'
                    },
                    {
                        'title': 'Blockchain Consultant',
                        'description': 'Advise on blockchain adoption and implementation',
                        'required_skills': ['Blockchain', 'Smart Contracts', 'Cryptocurrency', 'Consulting'],
                        'salary_range': convert_usd_to_inr('$90,000 - $160,000'),
                        'growth_prospect': 'High - Consulting is critical'
                    }
                ]
            },
            'ai_ml_engineering': {
                'career_paths': [
                    {
                        'title': 'AI Engineer',
                        'description': 'Build and deploy AI systems',
                        'required_skills': ['AI Engineering', 'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch'],
                        'salary_range': convert_usd_to_inr('$95,000 - $170,000'),
                        'growth_prospect': 'Very High - AI is transforming industries'
                    },
                    {
                        'title': 'ML Engineer',
                        'description': 'Build and deploy machine learning models',
                        'required_skills': ['Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch'],
                        'salary_range': convert_usd_to_inr('$90,000 - $160,000'),
                        'growth_prospect': 'Very High - ML is essential'
                    },
                    {
                        'title': 'Data Scientist',
                        'description': 'Extract insights from data to drive business decisions',
                        'required_skills': ['Python', 'Statistics', 'Machine Learning', 'SQL', 'Data Visualization'],
                        'salary_range': convert_usd_to_inr('$90,000 - $160,000'),
                        'growth_prospect': 'Very High - Data-driven decision making is crucial'
                    },
                    {
                        'title': 'Data Analyst',
                        'description': 'Analyze data to identify trends and create reports',
                        'required_skills': ['SQL', 'Excel', 'Tableau/PowerBI', 'Statistics', 'Business Intelligence'],
                        'salary_range': convert_usd_to_inr('$60,000 - $100,000'),
                        'growth_prospect': 'High - Every company needs data insights'
                    },
                    {
                        'title': 'ML Engineer',
                        'description': 'Deploy and maintain machine learning models in production',
                        'required_skills': ['Python', 'TensorFlow/PyTorch', 'MLOps', 'Cloud Platforms', 'Docker'],
                        'salary_range': convert_usd_to_inr('$100,000 - $180,000'),
                        'growth_prospect': 'Very High - AI/ML adoption is accelerating'
                    }
                ]
            },
            'mobile_development': {
                'career_paths': [
                    {
                        'title': 'Mobile App Developer',
                        'description': 'Create mobile applications for iOS and Android platforms',
                        'required_skills': ['Swift/Kotlin', 'React Native/Flutter', 'Mobile UI/UX', 'API Integration'],
                        'salary_range': convert_usd_to_inr('$75,000 - $135,000'),
                        'growth_prospect': 'High - Mobile usage continues to grow globally'
                    },
                    {
                        'title': 'iOS Developer',
                        'description': 'Specialize in creating applications for Apple devices',
                        'required_skills': ['Swift', 'Xcode', 'SwiftUI', 'Core Data', 'App Store Guidelines'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - iOS market has high revenue potential'
                    },
                    {
                        'title': 'Android Developer',
                        'description': 'Build applications for the Android ecosystem',
                        'required_skills': ['Kotlin/Java', 'Android Studio', 'Jetpack Compose', 'Firebase'],
                        'salary_range': convert_usd_to_inr('$70,000 - $130,000'),
                        'growth_prospect': 'High - Largest mobile platform globally'
                    }
                ]
            },
            'devops_cloud': {
                'career_paths': [
                    {
                        'title': 'DevOps Engineer',
                        'description': 'Automate and optimize software delivery pipelines',
                        'required_skills': ['Docker', 'Kubernetes', 'CI/CD', 'Infrastructure as Code', 'Monitoring'],
                        'salary_range': convert_usd_to_inr('$85,000 - $140,000'),
                        'growth_prospect': 'Very High - Critical for modern software delivery'
                    },
                    {
                        'title': 'Cloud Architect',
                        'description': 'Design and implement cloud infrastructure solutions',
                        'required_skills': ['AWS/Azure/GCP', 'Architecture Design', 'Security', 'Cost Optimization'],
                        'salary_range': convert_usd_to_inr('$110,000 - $180,000'),
                        'growth_prospect': 'Very High - Cloud adoption is accelerating'
                    },
                    {
                        'title': 'Site Reliability Engineer',
                        'description': 'Ensure system reliability, performance, and scalability',
                        'required_skills': ['System Administration', 'Monitoring', 'Incident Response', 'Automation'],
                        'salary_range': convert_usd_to_inr('$95,000 - $160,000'),
                        'growth_prospect': 'High - Reliability is crucial for digital services'
                    }
                ]
            },
            'cybersecurity': {
                'career_paths': [
                    {
                        'title': 'Cybersecurity Analyst',
                        'description': 'Monitor and protect systems from security threats',
                        'required_skills': ['Network Security', 'Threat Analysis', 'SIEM Tools', 'Incident Response'],
                        'salary_range': convert_usd_to_inr('$70,000 - $120,000'),
                        'growth_prospect': 'Very High - Cyber threats are increasing rapidly'
                    },
                    {
                        'title': 'Ethical Hacker',
                        'description': 'Test systems for vulnerabilities through authorized penetration testing',
                        'required_skills': ['Penetration Testing', 'Vulnerability Assessment', 'Security Tools', 'Compliance'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'Very High - Proactive security testing is essential'
                    },
                    {
                        'title': 'Security Engineer',
                        'description': 'Design and implement security systems and protocols',
                        'required_skills': ['Security Architecture', 'Cryptography', 'Access Control', 'Risk Assessment'],
                        'salary_range': convert_usd_to_inr('$90,000 - $150,000'),
                        'growth_prospect': 'Very High - Security by design is critical'
                    }
                ]
            },
            'design_ux': {
                'career_paths': [
                    {
                        'title': 'UX Designer',
                        'description': 'Create intuitive and engaging user experiences',
                        'required_skills': ['User Research', 'Wireframing', 'Prototyping', 'Usability Testing', 'Design Tools'],
                        'salary_range': convert_usd_to_inr('$65,000 - $120,000'),
                        'growth_prospect': 'High - User experience is crucial for product success'
                    },
                    {
                        'title': 'UI Designer',
                        'description': 'Design beautiful and functional user interfaces',
                        'required_skills': ['Visual Design', 'Design Systems', 'Typography', 'Color Theory', 'Design Tools'],
                        'salary_range': convert_usd_to_inr('$60,000 - $110,000'),
                        'growth_prospect': 'High - Visual design skills are always in demand'
                    },
                    {
                        'title': 'Product Designer',
                        'description': 'Lead design strategy for digital products',
                        'required_skills': ['Product Strategy', 'User Research', 'Design Leadership', 'Cross-functional Collaboration'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'High - Product-focused design is essential for business success'
                    }
                ]
            },
            'engineering_hardware': {
                'career_paths': [
                    {
                        'title': 'Hardware Engineer',
                        'description': 'Design and develop computer hardware components and systems',
                        'required_skills': ['Circuit Design', 'Embedded Systems', 'PCB Design', 'VHDL/Verilog'],
                        'salary_range': convert_usd_to_inr('$75,000 - $130,000'),
                        'growth_prospect': 'High - IoT and embedded systems growth'
                    },
                    {
                        'title': 'FPGA Engineer',
                        'description': 'Design and implement digital circuits using Field-Programmable Gate Arrays',
                        'required_skills': ['Digital Logic', 'VHDL/Verilog', 'FPGA Design', 'Signal Processing'],
                        'salary_range': convert_usd_to_inr('$85,000 - $145,000'),
                        'growth_prospect': 'High - Specialized skills in demand'
                    },
                    {
                        'title': 'Embedded Systems Engineer',
                        'description': 'Develop software and hardware for embedded systems in various devices',
                        'required_skills': ['C/C++', 'Microcontrollers', 'RTOS', 'Hardware-Software Integration'],
                        'salary_range': convert_usd_to_inr('$80,000 - $140,000'),
                        'growth_prospect': 'Very High - IoT and smart devices proliferation'
                    }
                ]
            },
            'medicine_general': {
                'career_paths': [
                    {
                        'title': 'General Practitioner',
                        'description': 'Provide primary healthcare services to patients of all ages',
                        'required_skills': ['Patient Care', 'Diagnosis', 'Treatment Planning', 'Medical Ethics'],
                        'salary_range': convert_usd_to_inr('$150,000 - $250,000'),
                        'growth_prospect': 'Stable - Essential healthcare services'
                    },
                    {
                        'title': 'Medical Specialist',
                        'description': 'Specialize in a particular area of medicine after general practice',
                        'required_skills': ['Advanced Diagnostics', 'Specialized Treatment', 'Continuing Education'],
                        'salary_range': convert_usd_to_inr('$200,000 - $400,000'),
                        'growth_prospect': 'High - Specialization increases demand'
                    },
                    {
                        'title': 'Medical Researcher',
                        'description': 'Conduct research to advance medical knowledge and treatments',
                        'required_skills': ['Research Methodology', 'Data Analysis', 'Clinical Trials', 'Publication'],
                        'salary_range': convert_usd_to_inr('$80,000 - $150,000'),
                        'growth_prospect': 'High - Medical research is critical for advancement'
                    }
                ]
            },
            'medicine_surgery': {
                'career_paths': [
                    {
                        'title': 'General Surgeon',
                        'description': 'Perform surgical procedures to treat injuries, diseases, and deformities',
                        'required_skills': ['Surgical Techniques', 'Anatomy', 'Operative Procedures', 'Patient Monitoring'],
                        'salary_range': convert_usd_to_inr('$250,000 - $500,000'),
                        'growth_prospect': 'High - Surgical skills always in demand'
                    },
                    {
                        'title': 'Specialized Surgeon',
                        'description': 'Focus on specific surgical areas like cardiac, neuro, or orthopedic surgery',
                        'required_skills': ['Advanced Surgical Techniques', 'Specialized Anatomy', 'Precision', 'Decision Making'],
                        'salary_range': convert_usd_to_inr('$350,000 - $700,000'),
                        'growth_prospect': 'Very High - Specialized skills command premium'
                    },
                    {
                        'title': 'Surgical Educator',
                        'description': 'Teach and train the next generation of surgeons',
                        'required_skills': ['Surgical Expertise', 'Teaching', 'Curriculum Development', 'Mentoring'],
                        'salary_range': convert_usd_to_inr('$200,000 - $400,000'),
                        'growth_prospect': 'Stable - Education is essential for profession'
                    }
                ]
            },
            'medicine_pediatrics': {
                'career_paths': [
                    {
                        'title': 'Pediatrician',
                        'description': 'Provide medical care specifically for infants, children, and adolescents',
                        'required_skills': ['Child Development', 'Pediatric Diagnostics', 'Treatment Planning', 'Family Communication'],
                        'salary_range': convert_usd_to_inr('$180,000 - $300,000'),
                        'growth_prospect': 'High - Growing focus on child health'
                    },
                    {
                        'title': 'Pediatric Specialist',
                        'description': 'Specialize in areas like pediatric cardiology, neurology, or oncology',
                        'required_skills': ['Advanced Pediatrics', 'Specialized Diagnostics', 'Child Psychology', 'Family Support'],
                        'salary_range': convert_usd_to_inr('$250,000 - $450,000'),
                        'growth_prospect': 'Very High - Specialized pediatric care is in demand'
                    },
                    {
                        'title': 'Neonatologist',
                        'description': 'Care for newborn infants, especially those who are premature or critically ill',
                        'required_skills': ['Neonatal Care', 'Intensive Care', 'Life Support', 'Family Counseling'],
                        'salary_range': convert_usd_to_inr('$300,000 - $500,000'),
                        'growth_prospect': 'High - Critical care for newborns'
                    }
                ]
            },
            'medicine_psychiatry': {
                'career_paths': [
                    {
                        'title': 'Psychiatrist',
                        'description': 'Diagnose, treat, and help prevent disorders related to mental health',
                        'required_skills': ['Mental Health Diagnosis', 'Psychotherapy', 'Medication Management', 'Crisis Intervention'],
                        'salary_range': convert_usd_to_inr('$200,000 - $350,000'),
                        'growth_prospect': 'Very High - Increasing awareness of mental health'
                    },
                    {
                        'title': 'Child and Adolescent Psychiatrist',
                        'description': 'Specialize in mental health issues affecting children and teenagers',
                        'required_skills': ['Child Psychology', 'Developmental Disorders', 'Family Therapy', 'Behavioral Interventions'],
                        'salary_range': convert_usd_to_inr('$250,000 - $400,000'),
                        'growth_prospect': 'Very High - Growing need for youth mental health services'
                    },
                    {
                        'title': 'Addiction Psychiatrist',
                        'description': 'Specialize in treating substance abuse and addictive behaviors',
                        'required_skills': ['Addiction Medicine', 'Behavioral Therapy', 'Rehabilitation', 'Dual Diagnosis Treatment'],
                        'salary_range': convert_usd_to_inr('$220,000 - $380,000'),
                        'growth_prospect': 'High - Increasing focus on addiction treatment'
                    }
                ]
            },
            'medicine_dermatology': {
                'career_paths': [
                    {
                        'title': 'Dermatologist',
                        'description': 'Diagnose and treat conditions related to the skin, hair, and nails',
                        'required_skills': ['Skin Pathology', 'Dermatologic Surgery', 'Cosmetic Procedures', 'Dermatologic Diagnostics'],
                        'salary_range': convert_usd_to_inr('$300,000 - $500,000'),
                        'growth_prospect': 'High - Growing demand for cosmetic and medical dermatology'
                    },
                    {
                        'title': 'Dermatologic Surgeon',
                        'description': 'Perform surgical procedures to treat skin conditions and cosmetic concerns',
                        'required_skills': ['Surgical Techniques', 'Laser Surgery', 'Reconstructive Surgery', 'Aesthetic Procedures'],
                        'salary_range': convert_usd_to_inr('$350,000 - $550,000'),
                        'growth_prospect': 'High - Cosmetic and reconstructive procedures'
                    },
                    {
                        'title': 'Pediatric Dermatologist',
                        'description': 'Specialize in skin conditions affecting children and adolescents',
                        'required_skills': ['Pediatric Dermatology', 'Skin Conditions in Children', 'Family Education', 'Developmental Considerations'],
                        'salary_range': convert_usd_to_inr('$280,000 - $450,000'),
                        'growth_prospect': 'High - Specialized pediatric skin care'
                    }
                ]
            },
            'medicine_cardiology': {
                'career_paths': [
                    {
                        'title': 'Cardiologist',
                        'description': 'Diagnose and treat diseases and conditions of the cardiovascular system',
                        'required_skills': ['Cardiac Diagnostics', 'Echocardiography', 'Cardiac Catheterization', 'Electrophysiology'],
                        'salary_range': convert_usd_to_inr('$350,000 - $600,000'),
                        'growth_prospect': 'High - Heart disease is a leading cause of death'
                    },
                    {
                        'title': 'Interventional Cardiologist',
                        'description': 'Perform minimally invasive procedures to treat heart conditions',
                        'required_skills': ['Cardiac Catheterization', 'Angioplasty', 'Stent Placement', 'Minimally Invasive Techniques'],
                        'salary_range': convert_usd_to_inr('$400,000 - $700,000'),
                        'growth_prospect': 'Very High - Advanced cardiac procedures'
                    },
                    {
                        'title': 'Cardiac Surgeon',
                        'description': 'Perform surgical procedures on the heart and major blood vessels',
                        'required_skills': ['Cardiac Surgery', 'Open Heart Surgery', 'Bypass Surgery', 'Heart Transplantation'],
                        'salary_range': convert_usd_to_inr('$500,000 - $800,000'),
                        'growth_prospect': 'High - Complex cardiac surgical procedures'
                    }
                ]
            },
            'medicine_neurology': {
                'career_paths': [
                    {
                        'title': 'Neurologist',
                        'description': 'Diagnose and treat disorders of the nervous system',
                        'required_skills': ['Neurological Diagnostics', 'Brain Imaging', 'Neuromuscular Disorders', 'Neuropharmacology'],
                        'salary_range': convert_usd_to_inr('$280,000 - $500,000'),
                        'growth_prospect': 'High - Growing understanding of neurological conditions'
                    },
                    {
                        'title': 'Neurosurgeon',
                        'description': 'Perform surgical procedures on the brain and nervous system',
                        'required_skills': ['Neurosurgery', 'Brain Tumor Removal', 'Spinal Surgery', 'Microsurgery'],
                        'salary_range': convert_usd_to_inr('$450,000 - $750,000'),
                        'growth_prospect': 'Very High - Complex neurological surgical procedures'
                    },
                    {
                        'title': 'Clinical Neurophysiologist',
                        'description': 'Study the function of the brain and nervous system',
                        'required_skills': ['EEG', 'EMG', 'Evoked Potentials', 'Sleep Studies', 'Neurodiagnostics'],
                        'salary_range': convert_usd_to_inr('$250,000 - $400,000'),
                        'growth_prospect': 'High - Specialized neurological testing'
                    }
                ]
            },
            'medicine_orthopedics': {
                'career_paths': [
                    {
                        'title': 'Orthopedic Surgeon',
                        'description': 'Diagnose and treat disorders of the musculoskeletal system',
                        'required_skills': ['Orthopedic Surgery', 'Joint Replacement', 'Fracture Repair', 'Sports Medicine'],
                        'salary_range': convert_usd_to_inr('$400,000 - $650,000'),
                        'growth_prospect': 'High - Aging population increases orthopedic needs'
                    },
                    {
                        'title': 'Sports Medicine Physician',
                        'description': 'Treat sports-related injuries and promote athletic performance',
                        'required_skills': ['Sports Injuries', 'Rehabilitation', 'Performance Enhancement', 'Injury Prevention'],
                        'salary_range': convert_usd_to_inr('$250,000 - $450,000'),
                        'growth_prospect': 'High - Growing sports and fitness industry'
                    },
                    {
                        'title': 'Hand Surgeon',
                        'description': 'Specialize in surgical treatment of hand and upper extremity conditions',
                        'required_skills': ['Hand Surgery', 'Microsurgery', 'Nerve Repair', 'Reconstructive Surgery'],
                        'salary_range': convert_usd_to_inr('$450,000 - $700,000'),
                        'growth_prospect': 'High - Specialized surgical expertise'
                    }
                ]
            },
            'medicine_ophthalmology': {
                'career_paths': [
                    {
                        'title': 'Ophthalmologist',
                        'description': 'Diagnose and treat eye diseases and perform eye surgery',
                        'required_skills': ['Eye Examination', 'Cataract Surgery', 'Glaucoma Treatment', 'Retinal Surgery'],
                        'salary_range': convert_usd_to_inr('$300,000 - $550,000'),
                        'growth_prospect': 'High - Vision care needs increase with age'
                    },
                    {
                        'title': 'Optometrist',
                        'description': 'Examine eyes for vision problems and eye diseases',
                        'required_skills': ['Vision Testing', 'Prescription Lenses', 'Eye Health Assessment', 'Contact Lens Fitting'],
                        'salary_range': convert_usd_to_inr('$120,000 - $200,000'),
                        'growth_prospect': 'High - Primary eye care providers'
                    },
                    {
                        'title': 'Oculoplastic Surgeon',
                        'description': 'Specialize in plastic and reconstructive surgery of the eye and surrounding areas',
                        'required_skills': ['Oculoplastic Surgery', 'Reconstructive Surgery', 'Cosmetic Surgery', 'Orbital Surgery'],
                        'salary_range': convert_usd_to_inr('$350,000 - $600,000'),
                        'growth_prospect': 'High - Specialized eye and facial surgery'
                    }
                ]
            },
            'medicine_gynecology': {
                'career_paths': [
                    {
                        'title': 'Gynecologist',
                        'description': 'Provide medical care for women\'s reproductive health',
                        'required_skills': ['Women\'s Health', 'Reproductive Medicine', 'Preventive Care', 'Gynecologic Surgery'],
                        'salary_range': convert_usd_to_inr('$250,000 - $450,000'),
                        'growth_prospect': 'High - Essential women\'s healthcare'
                    },
                    {
                        'title': 'Obstetrician',
                        'description': 'Provide care for pregnant women and deliver babies',
                        'required_skills': ['Prenatal Care', 'Labor and Delivery', 'High-Risk Pregnancy', 'Neonatal Care'],
                        'salary_range': convert_usd_to_inr('$280,000 - $500,000'),
                        'growth_prospect': 'High - Maternal and newborn care'
                    },
                    {
                        'title': 'Reproductive Endocrinologist',
                        'description': 'Specialize in fertility and hormonal disorders',
                        'required_skills': ['Fertility Treatment', 'IVF', 'Hormonal Disorders', 'Reproductive Surgery'],
                        'salary_range': convert_usd_to_inr('$350,000 - $600,000'),
                        'growth_prospect': 'High - Growing demand for fertility treatments'
                    }
                ]
            },
            'medicine_radiology': {
                'career_paths': [
                    {
                        'title': 'Radiologist',
                        'description': 'Interpret medical images to diagnose and treat diseases',
                        'required_skills': ['Medical Imaging', 'MRI', 'CT Scans', 'X-rays', 'Image Interpretation'],
                        'salary_range': convert_usd_to_inr('$350,000 - $550,000'),
                        'growth_prospect': 'High - Medical imaging is essential for diagnosis'
                    },
                    {
                        'title': 'Interventional Radiologist',
                        'description': 'Perform minimally invasive procedures guided by imaging',
                        'required_skills': ['Image-Guided Procedures', 'Angiography', 'Biopsy Techniques', 'Minimally Invasive Surgery'],
                        'salary_range': convert_usd_to_inr('$400,000 - $650,000'),
                        'growth_prospect': 'High - Minimally invasive treatments'
                    },
                    {
                        'title': 'Radiation Oncologist',
                        'description': 'Use radiation therapy to treat cancer',
                        'required_skills': ['Radiation Therapy', 'Cancer Treatment', 'Treatment Planning', 'Patient Care'],
                        'salary_range': convert_usd_to_inr('$400,000 - $600,000'),
                        'growth_prospect': 'High - Cancer treatment demand'
                    }
                ]
            },
            'medicine_anesthesiology': {
                'career_paths': [
                    {
                        'title': 'Anesthesiologist',
                        'description': 'Administer anesthesia and monitor patients during surgery',
                        'required_skills': ['Anesthesia Administration', 'Patient Monitoring', 'Pain Management', 'Critical Care'],
                        'salary_range': convert_usd_to_inr('$350,000 - $550,000'),
                        'growth_prospect': 'High - Essential for surgical procedures'
                    },
                    {
                        'title': 'Pain Management Specialist',
                        'description': 'Diagnose and treat chronic pain conditions',
                        'required_skills': ['Pain Diagnostics', 'Interventional Procedures', 'Medication Management', 'Patient Education'],
                        'salary_range': convert_usd_to_inr('$300,000 - $500,000'),
                        'growth_prospect': 'High - Growing need for pain treatment'
                    },
                    {
                        'title': 'Critical Care Anesthesiologist',
                        'description': 'Provide intensive care for critically ill patients',
                        'required_skills': ['Critical Care Medicine', 'Life Support', 'Ventilator Management', 'Emergency Medicine'],
                        'salary_range': convert_usd_to_inr('$380,000 - $600,000'),
                        'growth_prospect': 'High - Critical care expertise'
                    }
                ]
            },
            'business_finance': {
                'career_paths': [
                    {
                        'title': 'Financial Analyst',
                        'description': 'Analyze financial data to guide business investment decisions',
                        'required_skills': ['Financial Analysis', 'Investment Management', 'Risk Assessment', 'Corporate Finance'],
                        'salary_range': convert_usd_to_inr('$60,000 - $120,000'),
                        'growth_prospect': 'High - Financial insights crucial for business success'
                    },
                    {
                        'title': 'Investment Banker',
                        'description': 'Help companies raise capital and provide financial advisory services',
                        'required_skills': ['Corporate Finance', 'Valuation', 'Mergers & Acquisitions', 'Client Relations'],
                        'salary_range': convert_usd_to_inr('$100,000 - $300,000'),
                        'growth_prospect': 'High - High earning potential in financial services'
                    },
                    {
                        'title': 'Chief Financial Officer',
                        'description': 'Lead the financial strategy and operations of an organization',
                        'required_skills': ['Strategic Planning', 'Financial Management', 'Leadership', 'Regulatory Compliance'],
                        'salary_range': convert_usd_to_inr('$200,000 - $500,000'),
                        'growth_prospect': 'Very High - Executive leadership roles in demand'
                    }
                ]
            },
            'business_marketing': {
                'career_paths': [
                    {
                        'title': 'Digital Marketing Specialist',
                        'description': 'Create and manage online marketing campaigns across various channels',
                        'required_skills': ['Digital Marketing', 'SEO', 'Content Strategy', 'Analytics'],
                        'salary_range': convert_usd_to_inr('$50,000 - $90,000'),
                        'growth_prospect': 'Very High - Digital marketing is essential for business growth'
                    },
                    {
                        'title': 'Marketing Manager',
                        'description': 'Lead marketing teams and develop comprehensive marketing strategies',
                        'required_skills': ['Brand Management', 'Campaign Strategy', 'Team Leadership', 'Budget Management'],
                        'salary_range': convert_usd_to_inr('$80,000 - $150,000'),
                        'growth_prospect': 'High - Leadership roles in marketing are in demand'
                    },
                    {
                        'title': 'Chief Marketing Officer',
                        'description': 'Drive the overall marketing vision and strategy for an organization',
                        'required_skills': ['Strategic Thinking', 'Brand Leadership', 'Innovation', 'Executive Management'],
                        'salary_range': convert_usd_to_inr('$150,000 - $400,000'),
                        'growth_prospect': 'High - C-suite marketing leadership roles'
                    }
                ]
            },
            'creative_design': {
                'career_paths': [
                    {
                        'title': 'Graphic Designer',
                        'description': 'Create visual concepts to communicate ideas and information',
                        'required_skills': ['Adobe Photoshop', 'Illustrator', 'Branding', 'Typography'],
                        'salary_range': convert_usd_to_inr('$45,000 - $80,000'),
                        'growth_prospect': 'Stable - Design skills always in demand'
                    },
                    {
                        'title': 'Creative Director',
                        'description': 'Lead creative teams and guide the artistic direction of projects',
                        'required_skills': ['Creative Leadership', 'Artistic Vision', 'Team Management', 'Brand Strategy'],
                        'salary_range': convert_usd_to_inr('$90,000 - $180,000'),
                        'growth_prospect': 'High - Leadership in creative industries'
                    },
                    {
                        'title': 'Brand Designer',
                        'description': 'Develop and maintain brand identities for companies and products',
                        'required_skills': ['Brand Strategy', 'Visual Identity', 'Logo Design', 'Brand Guidelines'],
                        'salary_range': convert_usd_to_inr('$60,000 - $120,000'),
                        'growth_prospect': 'High - Branding is crucial for business success'
                    }
                ]
            }
        }

        # Get appropriate response or randomly select from available domains to ensure variety
        if primary_domain in domain_responses:
            response_data = domain_responses[primary_domain]
        else:
            # If domain not in our predefined responses, randomly select one to ensure variety
            available_domains = list(domain_responses.keys())
            random_domain = random.choice(available_domains)
            response_data = domain_responses[random_domain]

        # Randomly select one of the career paths as the selected path to ensure variety
        selected_path_index = random.randint(0, len(response_data['career_paths']) - 1)
        selected_path = response_data['career_paths'][selected_path_index]

        # Personalize the roadmap based on expertise level
        expertise_level = expertise.lower()
        if 'beginner' in expertise_level:
            duration_multiplier = 1.5
            difficulty_modifier = 'Beginner'
        elif 'intermediate' in expertise_level:
            duration_multiplier = 1.0
            difficulty_modifier = 'Intermediate'
        elif 'advanced' in expertise_level:
            duration_multiplier = 0.7
            difficulty_modifier = 'Advanced'
        else:
            duration_multiplier = 1.0
            difficulty_modifier = 'Intermediate'

        # Adjust roadmap steps based on expertise
        personalized_roadmap = [
            {
                'step': 1,
                'title': 'Skill Assessment and Gap Analysis',
                'description': f'Evaluate your current {skills} skills and identify areas for improvement based on your {expertise} level',
                'duration': f'{int(2*duration_multiplier)}-{int(4*duration_multiplier)} weeks',
                'resources': [f'{skills} assessments', 'Portfolio review', f'{skills} industry research']
            },
            {
                'step': 2,
                'title': f'Learn Core {skills.title()} Technologies',
                'description': f'Master the fundamental {skills} technologies appropriate for your {expertise} level',
                'duration': f'{int(3*duration_multiplier)}-{int(6*duration_multiplier)} months',
                'resources': [f'{skills} online courses', f'{skills} documentation', f'{skills} practice projects']
            },
            {
                'step': 3,
                'title': 'Build Portfolio Projects',
                'description': f'Create impressive {skills} projects that demonstrate your {expertise} level skills to employers',
                'duration': f'{int(2*duration_multiplier)}-{int(4*duration_multiplier)} months',
                'resources': ['GitHub', 'Personal website', f'{skills} case studies']
            },
            {
                'step': 4,
                'title': 'Network and Gain Experience',
                'description': f'Connect with {skills} professionals and gain real-world experience appropriate for your {expertise} level',
                'duration': f'{int(3*duration_multiplier)}-{int(6*duration_multiplier)} months',
                'resources': ['LinkedIn', f'{skills} meetups', 'Open source contributions', 'Internships']
            },
            {
                'step': 5,
                'title': 'Job Search and Interview Preparation',
                'description': f'Prepare for {skills} interviews and start applying to positions matching your {expertise} level',
                'duration': f'{int(1*duration_multiplier)}-{int(3*duration_multiplier)} months',
                'resources': [f'{skills} interview practice', 'Resume optimization', f'{skills} job boards', 'Referrals']
            }
        ]

        # Personalize courses based on skills and expertise
        personalized_courses = [
            {
                'title': f'Complete {skills.title()} Course for {difficulty_modifier}s',
                'provider': 'YouTube',
                'duration': f'{int(12*duration_multiplier)} weeks',
                'difficulty': difficulty_modifier,
                'type': 'Free',
                'url': f'https://www.youtube.com/results?search_query={skills.replace(" ", "+")}+course+for+{difficulty_modifier}'
            },
            {
                'title': f'{skills.title()} Fundamentals Tutorial',
                'provider': 'YouTube',
                'duration': f'{int(8*duration_multiplier)} weeks',
                'difficulty': difficulty_modifier,
                'type': 'Free',
                'url': f'https://www.youtube.com/results?search_query={skills.replace(" ", "+")}+fundamentals+tutorial'
            },
            {
                'title': f'Advanced {skills.title()} Techniques',
                'provider': 'YouTube',
                'duration': f'{int(10*duration_multiplier)} weeks',
                'difficulty': 'Advanced' if difficulty_modifier != 'Beginner' else 'Intermediate',
                'type': 'Free',
                'url': f'https://www.youtube.com/results?search_query=advanced+{skills.replace(" ", "+")}+techniques'
            },
            {
                'title': f'{skills.title()} Best Practices Guide',
                'provider': 'YouTube',
                'duration': f'{int(6*duration_multiplier)} weeks',
                'difficulty': difficulty_modifier,
                'type': 'Free',
                'url': f'https://www.youtube.com/results?search_query={skills.replace(" ", "+")}+best+practices'
            },
            {
                'title': f'{skills.title()} Certification Preparation',
                'provider': 'YouTube',
                'duration': f'{int(4*duration_multiplier)} weeks',
                'difficulty': 'Intermediate' if difficulty_modifier != 'Advanced' else 'Advanced',
                'type': 'Free',
                'url': f'https://www.youtube.com/results?search_query={skills.replace(" ", "+")}+certification+preparation'
            }
        ]

        # Add some free courses from other platforms
        free_platforms = [
            {
                'title': f'Introduction to {skills.title()} - Free Course',
                'provider': 'Coursera',
                'duration': f'{int(6*duration_multiplier)} weeks',
                'difficulty': difficulty_modifier,
                'type': 'Free',
                'url': f'https://www.coursera.org/search?query={skills.replace(" ", "%20")}'
            },
            {
                'title': f'{skills.title()} Fundamentals - Free Specialization',
                'provider': 'edX',
                'duration': f'{int(8*duration_multiplier)} weeks',
                'difficulty': difficulty_modifier,
                'type': 'Free',
                'url': f'https://www.edx.org/search?q={skills.replace(" ", "%20")}'
            },
            {
                'title': f'Learn {skills.title()} - Free Code Camp',
                'provider': 'FreeCodeCamp',
                'duration': f'{int(10*duration_multiplier)} weeks',
                'difficulty': difficulty_modifier,
                'type': 'Free',
                'url': f'https://www.freecodecamp.org/learn'
            }
        ]

        # Combine YouTube courses with other free courses
        personalized_courses.extend(free_platforms)

        # Personalize certifications based on skills
        # Map real certification providers based on user skills
        skill_based_certifications = {
            'python': [
                {
                    'name': 'Python Institute Certified Associate in Python Programming (PCAP)',
                    'provider': 'Python Institute',
                    'description': 'Validate your fundamental knowledge of Python programming',
                    'difficulty': 'Beginner',
                    'duration': '3-6 months',
                    'url': 'https://pythoninstitute.org/certification/pcep-pcp/pcap/'
                },
                {
                    'name': 'Microsoft Certified: Azure Developer Associate',
                    'provider': 'Microsoft',
                    'description': 'Demonstrate your expertise in designing, building, testing, and maintaining cloud applications using Azure',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://learn.microsoft.com/en-us/certifications/azure-developer/'
                },
                {
                    'name': 'Google Professional Python Developer',
                    'provider': 'Google Cloud',
                    'description': 'Prove your ability to build scalable, highly available, and reliable applications using Python on Google Cloud',
                    'difficulty': 'Advanced',
                    'duration': '6-9 months',
                    'url': 'https://cloud.google.com/certification/cloud-developer'
                }
            ],
            'javascript': [
                {
                    'name': 'JavaScript Developer Certification',
                    'provider': 'W3Schools',
                    'description': 'Validate your knowledge of JavaScript and web development',
                    'difficulty': 'Beginner',
                    'duration': '2-4 months',
                    'url': 'https://www.w3schools.com/cert/default.asp'
                },
                {
                    'name': 'Front-End Web Developer Certification',
                    'provider': 'FreeCodeCamp',
                    'description': 'Demonstrate your skills in HTML, CSS, JavaScript, and front-end frameworks',
                    'difficulty': 'Intermediate',
                    'duration': '6-12 months',
                    'url': 'https://www.freecodecamp.org/'
                },
                {
                    'name': 'React Developer Certification',
                    'provider': 'HackerRank',
                    'description': 'Prove your expertise in building user interfaces with React',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://www.hackerrank.com/skills-verification/react_basic'
                }
            ],
            'java': [
                {
                    'name': 'Oracle Certified Associate, Java SE Programmer',
                    'provider': 'Oracle',
                    'description': 'Validate your fundamental knowledge of Java programming',
                    'difficulty': 'Beginner',
                    'duration': '3-6 months',
                    'url': 'https://education.oracle.com/java-se-11-developer/pexam_1Z0-819'
                },
                {
                    'name': 'Spring Professional Certification',
                    'provider': 'VMware',
                    'description': 'Demonstrate your expertise in building applications with Spring Framework',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://tanzu.vmware.com/training/certification/spring-professional-certification'
                },
                {
                    'name': 'Oracle Certified Professional, Java SE Developer',
                    'provider': 'Oracle',
                    'description': 'Prove your advanced skills in Java application development',
                    'difficulty': 'Advanced',
                    'duration': '6-12 months',
                    'url': 'https://education.oracle.com/java-se-11-developer/pexam_1Z0-819'
                }
            ],
            'data science': [
                {
                    'name': 'IBM Data Science Professional Certificate',
                    'provider': 'IBM',
                    'description': 'Begin your journey in data science with IBM tools and technologies',
                    'difficulty': 'Beginner',
                    'duration': '3-6 months',
                    'url': 'https://www.coursera.org/professional-certificates/ibm-data-science'
                },
                {
                    'name': 'Google Data Analytics Professional Certificate',
                    'provider': 'Google',
                    'description': 'Learn data analytics foundations and tools used by Google professionals',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://grow.google/dataanalytics/'
                },
                {
                    'name': 'Microsoft Certified: Azure Data Scientist Associate',
                    'provider': 'Microsoft',
                    'description': 'Demonstrate your expertise in applying data science and machine learning techniques',
                    'difficulty': 'Advanced',
                    'duration': '6-9 months',
                    'url': 'https://learn.microsoft.com/en-us/certifications/azure-data-scientist/'
                }
            ],
            'aws': [
                {
                    'name': 'AWS Certified Cloud Practitioner',
                    'provider': 'Amazon Web Services',
                    'description': 'Validate your understanding of AWS Cloud fundamentals',
                    'difficulty': 'Beginner',
                    'duration': '3-6 months',
                    'url': 'https://aws.amazon.com/certification/certified-cloud-practitioner/'
                },
                {
                    'name': 'AWS Certified Solutions Architect – Associate',
                    'provider': 'Amazon Web Services',
                    'description': 'Prove your ability to design and deploy scalable systems on AWS',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://aws.amazon.com/certification/certified-solutions-architect-associate/'
                },
                {
                    'name': 'AWS Certified Solutions Architect – Professional',
                    'provider': 'Amazon Web Services',
                    'description': 'Demonstrate your expertise in distributed applications and systems on AWS',
                    'difficulty': 'Advanced',
                    'duration': '6-12 months',
                    'url': 'https://aws.amazon.com/certification/certified-solutions-architect-professional/'
                }
            ],
            'cybersecurity': [
                {
                    'name': 'CompTIA Security+',
                    'provider': 'CompTIA',
                    'description': 'Validate your baseline skills in cybersecurity',
                    'difficulty': 'Beginner',
                    'duration': '3-6 months',
                    'url': 'https://www.comptia.org/certifications/security'
                },
                {
                    'name': 'Certified Ethical Hacker (CEH)',
                    'provider': 'EC-Council',
                    'description': 'Demonstrate your knowledge of ethical hacking and penetration testing',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/'
                },
                {
                    'name': 'Certified Information Systems Security Professional (CISSP)',
                    'provider': 'ISC2',
                    'description': 'Prove your expertise in designing and managing cybersecurity programs',
                    'difficulty': 'Advanced',
                    'duration': '6-12 months',
                    'url': 'https://www.isc2.org/Certifications/CISSP'
                }
            ],
            'devops': [
                {
                    'name': 'Docker Certified Associate',
                    'provider': 'Docker',
                    'description': 'Validate your skills in containerization and Docker technologies',
                    'difficulty': 'Beginner',
                    'duration': '2-4 months',
                    'url': 'https://www.docker.com/certification/'
                },
                {
                    'name': 'Certified Kubernetes Administrator (CKA)',
                    'provider': 'Cloud Native Computing Foundation',
                    'description': 'Demonstrate your ability to manage Kubernetes clusters',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://www.cncf.io/certification/cka/'
                },
                {
                    'name': 'HashiCorp Certified: Terraform Associate',
                    'provider': 'HashiCorp',
                    'description': 'Prove your expertise in infrastructure as code with Terraform',
                    'difficulty': 'Intermediate',
                    'duration': '3-6 months',
                    'url': 'https://www.hashicorp.com/certification/terraform-associate'
                }
            ]
        }

        # Get certifications based on skills
        certifications_list = []
        skills_lower = skills.lower()

        # Check for specific skill matches
        for skill_key, certs in skill_based_certifications.items():
            if skill_key in skills_lower:
                certifications_list = certs
                break

        # If no specific match found, use generic certifications
        if not certifications_list:
            certifications_list = [
                {
                    'name': f'{skills.title()} Fundamentals Certification',
                    'provider': 'Coursera',
                    'description': f'Build fundamental knowledge in {skills} appropriate for your {expertise} level',
                    'difficulty': difficulty_modifier,
                    'duration': f'{int(3*duration_multiplier)} months',
                    'url': f'https://www.coursera.org/search?query={skills.replace(" ", "%20")}%20certification'
                },
                {
                    'name': f'Professional {skills.title()} Certification',
                    'provider': 'Udemy',
                    'description': f'Demonstrate your expertise in {skills} appropriate for your {expertise} level',
                    'difficulty': 'Intermediate' if difficulty_modifier != 'Advanced' else 'Advanced',
                    'duration': f'{int(4*duration_multiplier)} months',
                    'url': f'https://www.udemy.com/courses/search/?q={skills.replace(" ", "%20")}'
                },
                {
                    'name': f'Advanced {skills.title()} Certification',
                    'provider': 'Pluralsight',
                    'description': f'Prove your advanced skills in {skills} design and implementation',
                    'difficulty': 'Advanced',
                    'duration': f'{int(5*duration_multiplier)} months',
                    'url': f'https://www.pluralsight.com/search?q={skills.replace(" ", "%20")}'
                }
            ]

        personalized_certifications = certifications_list

        return {
            'career_paths': response_data['career_paths'],
            'selected_path': selected_path,
            'roadmap': personalized_roadmap,
            'courses': personalized_courses,
            'certifications': personalized_certifications
        }

    def generate_mock_test(self, skills: str, expertise: str, topic: str = "", user_id: str = "") -> Dict[str, Any]:
        """Generate a mock test using available AI services with fallbacks"""

        # Build the prompt
        topic_text = f" focusing on {topic}" if topic else ""
        prompt = f"""
        Generate a 5-question mock test for a user with skills {skills} and expertise {expertise}{topic_text}.
        Include questions and answers in JSON format:
        [
          {{"question": "...", "answer": "..."}}`,
          {{"question": "...", "answer": "..."}}`,
          {{"question": "...", "answer": "..."}}`,
          {{"question": "...", "answer": "..."}}`,
          {{"question": "...", "answer": "..."}}`
        ]

        Make the questions challenging but appropriate for the specified skill level.
        Provide detailed answers that explain the concepts.
        """

        questions = None

        # Try Vertex AI first if available
        if self.vertex_ai_available and self.model and hasattr(self.model, 'generate_content'):
            try:
                response = self.model.generate_content(prompt)
                response_text = response.text

                # Try to find JSON in the response
                start_idx = response_text.find('[')
                end_idx = response_text.rfind(']') + 1

                if start_idx != -1 and end_idx != -1:
                    json_str = response_text[start_idx:end_idx]
                    questions_data = json.loads(json_str)

                    # Convert to MockTestQuestion objects
                    questions = [MockTestQuestion(**q) for q in questions_data]
                    print("✅ Generated mock test using Vertex AI")

            except Exception as e:
                print(f"Vertex AI mock test generation failed: {e}")

        # Try fallback AI services if Vertex AI failed
        if not questions:
            ai_response = self._generate_with_fallback_ai(prompt)
            if ai_response:
                try:
                    # Try to extract JSON from AI response
                    start_idx = ai_response.find('[')
                    end_idx = ai_response.rfind(']') + 1

                    if start_idx != -1 and end_idx != -1:
                        json_str = ai_response[start_idx:end_idx]
                        questions_data = json.loads(json_str)
                        questions = [MockTestQuestion(**q) for q in questions_data]
                except Exception as e:
                    print(f"Error parsing AI response: {e}")

        # If all AI services fail, create a fallback response
        if not questions:
            print("Using static mock test fallback")
            questions = [
                MockTestQuestion(
                    question="What is the importance of continuous learning in your field?",
                    answer="Continuous learning is essential in today's rapidly evolving professional landscape. It helps professionals stay updated with the latest technologies, methodologies, and industry best practices. This ongoing education ensures competitiveness, adaptability, and career growth."
                ),
                MockTestQuestion(
                    question="How do you approach problem-solving in your domain?",
                    answer="Effective problem-solving involves several key steps: 1) Clearly defining the problem, 2) Gathering relevant information, 3) Generating multiple potential solutions, 4) Evaluating each option, 5) Selecting and implementing the best solution, and 6) Reviewing the results. This systematic approach ensures thorough analysis and better outcomes."
                ),
                MockTestQuestion(
                    question="What role does collaboration play in professional success?",
                    answer="Collaboration is crucial for professional success as it enables knowledge sharing, diverse perspectives, and collective problem-solving. Working effectively with others enhances creativity, improves decision-making, and leads to more innovative solutions. Strong collaboration skills also build professional networks and career opportunities."
                ),
                MockTestQuestion(
                    question="How do you stay current with industry trends and developments?",
                    answer="Staying current requires a multi-faceted approach: following industry publications and blogs, participating in professional associations, attending conferences and webinars, engaging in online communities, taking continuing education courses, and networking with peers. Regularly dedicating time to these activities ensures ongoing professional development."
                ),
                MockTestQuestion(
                    question="What strategies do you use for career planning and goal setting?",
                    answer="Effective career planning involves: 1) Self-assessment of skills, interests, and values, 2) Researching career paths and opportunities, 3) Setting SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound), 4) Creating actionable development plans, 5) Building relevant networks, 6) Regularly reviewing and adjusting plans based on progress and changing circumstances. This structured approach provides direction and motivation."
                )
            ]

        return {
            "questions": questions,
            "generated_at": datetime.now().isoformat()
        }

    def extract_skills_from_message(self, message: str, current_skills: str = "") -> Dict[str, Any]:
        """
        Extract skills from a chat message and update the user's skill list.

        Args:
            message: The chat message to analyze
            current_skills: The user's current skills list

        Returns:
            Dict containing extracted skills and updated skills list
        """
        # Keywords that indicate skill mentions
        skill_indicators = [
            'learned', 'learning', 'studying', 'know', 'experience',
            'worked with', 'using', 'familiar with', 'proficient in',
            'skilled in', 'expert in', 'mastered', 'practiced'
        ]

        # Check if the message contains skill indicators
        if not any(indicator in message.lower() for indicator in skill_indicators):
            return {
                "extracted_skills": [],
                "updated_skills": current_skills
            }

        # Use AI to extract skills if available
        prompt = f"""
        Extract specific technical skills from this message: "{message}"

        Current skills: {current_skills or "None"}

        Please provide a JSON response with this structure:
        {{
            "extracted_skills": [
                {{
                    "skill": "skill name",
                    "expertise_level": "Beginner/Intermediate/Advanced"
                }}
            ]
        }}

        Only include skills that are explicitly mentioned or strongly implied.
        For expertise level, use:
        - Beginner: Basic knowledge or just started learning
        - Intermediate: Some practical experience
        - Advanced: Strong proficiency or professional experience
        """

        # Try to extract skills using AI
        ai_response = self._generate_with_fallback_ai(prompt)
        if ai_response:
            try:
                # Try to extract JSON from AI response
                start_idx = ai_response.find('{')
                end_idx = ai_response.rfind('}') + 1

                if start_idx != -1 and end_idx != -1:
                    json_str = ai_response[start_idx:end_idx]
                    result = json.loads(json_str)

                    if "extracted_skills" in result:
                        # Update skills list
                        current_skills_list = [s.strip() for s in current_skills.split(',')] if current_skills else []
                        new_skills = [skill["skill"] for skill in result["extracted_skills"]]

                        # Add new skills to current skills, avoiding duplicates
                        for skill in new_skills:
                            if skill not in current_skills_list:
                                current_skills_list.append(skill)

                        updated_skills = ', '.join(current_skills_list) if current_skills_list else ""

                        return {
                            "extracted_skills": result["extracted_skills"],
                            "updated_skills": updated_skills
                        }
            except Exception as e:
                print(f"Error parsing skill extraction response: {e}")

        # Fallback: Simple keyword-based extraction
        # This is a simplified approach - a more sophisticated NLP approach would be better
        common_skills = [
            'Python', 'JavaScript', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'Rust', 'Swift', 'Kotlin',
            'React', 'Vue', 'Angular', 'Node.js', 'Django', 'Flask', 'Spring', 'Express',
            'SQL', 'MongoDB', 'PostgreSQL', 'MySQL', 'Redis',
            'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'Terraform',
            'Git', 'Jenkins', 'CI/CD', 'Agile', 'Scrum',
            'TensorFlow', 'PyTorch', 'Pandas', 'NumPy', 'Scikit-learn',
            'Figma', 'Photoshop', 'Illustrator', 'Sketch',
            'SEO', 'SEM', 'Google Analytics', 'Social Media Marketing'
        ]

        extracted_skills = []
        message_lower = message.lower()

        for skill in common_skills:
            if skill.lower() in message_lower:
                # Determine expertise level based on context
                if any(word in message_lower for word in ['expert', 'proficient', 'professional', 'years']):
                    level = 'Advanced'
                elif any(word in message_lower for word in ['intermediate', 'comfortable', 'working']):
                    level = 'Intermediate'
                else:
                    level = 'Beginner'

                extracted_skills.append({
                    "skill": skill,
                    "expertise_level": level
                })

        # Update skills list
        current_skills_list = [s.strip() for s in current_skills.split(',')] if current_skills else []
        new_skills = [skill["skill"] for skill in extracted_skills]

        # Add new skills to current skills, avoiding duplicates
        for skill in new_skills:
            if skill not in current_skills_list:
                current_skills_list.append(skill)

        updated_skills = ', '.join(current_skills_list) if current_skills_list else ""

        return {
            "extracted_skills": extracted_skills,
            "updated_skills": updated_skills
        }
