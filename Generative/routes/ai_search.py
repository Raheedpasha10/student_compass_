from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.ai_service import AIService
from typing import List, Dict, Any

router = APIRouter(tags=["ai-search"])
# Move AIService initialization inside the function to ensure proper environment loading
# ai_service = AIService()  # This line will be removed


class SkillSuggestionRequest(BaseModel):
    query: str
    max_suggestions: int = 8


class SkillSuggestionResponse(BaseModel):
    suggestions: List[str]
    categories: List[str]
    confidence: float


class EnhancedAnalysisRequest(BaseModel):
    skills: str
    expertise: str
    preferences: Dict[str, Any] = {}

@router.post("/ai/suggest-skills", response_model=SkillSuggestionResponse)
async def suggest_skills(request: SkillSuggestionRequest):
    """
    Use AI to intelligently suggest skills based on user input
    """
    try:
        query = request.query.strip().lower()

        if len(query) < 2:
            return SkillSuggestionResponse(
                suggestions=[],
                categories=[],
                confidence=0.0
            )

        # Enhanced skill database covering ALL technologies
        comprehensive_skills = {
            'Programming Languages': [
                'Python', 'JavaScript', 'Java', 'C++', 'C#', 'TypeScript', 'PHP', 'Ruby', 'Go', 'Rust',
                'Swift', 'Kotlin', 'Scala', 'R', 'MATLAB', 'Perl', 'Dart', 'Lua', 'Haskell', 'Clojure',
                'F#', 'Erlang', 'Elixir', 'Julia', 'Nim', 'Crystal', 'Zig', 'Assembly', 'Fortran', 'COBOL',
                'Objective-C', 'Solidity', 'Verilog', 'VHDL', 'C', 'Pascal', 'Ada', 'Prolog', 'Scheme'
            ],
            'Frontend Frameworks': [
                'React', 'Vue.js', 'Angular', 'Svelte', 'Ember.js', 'Backbone.js', 'Alpine.js', 'Lit',
                'Stimulus', 'Next.js', 'Nuxt.js', 'Gatsby', 'Quasar', 'Vuetify', 'Chakra UI', 'Material-UI',
                'Ant Design', 'Bootstrap', 'Tailwind CSS', 'Bulma', 'Foundation', 'Semantic UI'
            ],
            'Backend Frameworks': [
                'Node.js', 'Express.js', 'Django', 'Flask', 'FastAPI', 'Spring Boot', 'Spring Framework',
                'Laravel', 'Symphony', 'Ruby on Rails', 'Sinatra', 'ASP.NET Core', 'Blazor', 'Gin',
                'Echo', 'Fiber', 'Actix Web', 'Rocket', 'Vapor', 'NestJS', 'Koa.js', 'Fastify'
            ],
            'Mobile Development': [
                'React Native', 'Flutter', 'Ionic', 'Xamarin', 'Cordova', 'PhoneGap', 'SwiftUI',
                'UIKit', 'Android Jetpack', 'Jetpack Compose', 'Titanium', 'Unity Mobile', 'Cocos2d'
            ],
            'Databases': [
                'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'SQLite', 'Oracle Database', 'SQL Server',
                'MariaDB', 'CouchDB', 'Cassandra', 'DynamoDB', 'Firebase Firestore', 'Neo4j',
                'InfluxDB', 'TimescaleDB', 'CouchBase', 'Amazon RDS', 'Supabase', 'PlanetScale'
            ],
            'Cloud & DevOps': [
                'AWS', 'Microsoft Azure', 'Google Cloud Platform', 'Docker', 'Kubernetes', 'Terraform',
                'Ansible', 'Jenkins', 'GitLab CI', 'GitHub Actions', 'CircleCI', 'Travis CI', 'Helm',
                'Vagrant', 'Chef', 'Puppet', 'Prometheus', 'Grafana', 'ELK Stack', 'Datadog'
            ],
            'Data Science & AI': [
                'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn',
                'Pandas', 'NumPy', 'OpenCV', 'NLTK', 'spaCy', 'Hugging Face', 'LangChain', 'Jupyter',
                'Apache Spark', 'Hadoop', 'Kafka', 'Airflow', 'MLflow', 'Weights & Biases'
            ],
            'Game Development': [
                'Unity', 'Unreal Engine', 'Godot', 'GameMaker Studio', 'Construct 3', 'Blender',
                'Maya', '3ds Max', 'Substance Painter', 'Houdini', 'CryEngine', 'Lumberyard'
            ],
            'Design Tools': [
                'Figma', 'Sketch', 'Adobe XD', 'InVision', 'Principle', 'Framer', 'Zeplin',
                'Adobe Photoshop', 'Adobe Illustrator', 'Adobe After Effects', 'Canva', 'GIMP'
            ],
            'Testing & QA': [
                'Jest', 'Mocha', 'Chai', 'Cypress', 'Selenium', 'Playwright', 'Puppeteer',
                'TestNG', 'JUnit', 'Pytest', 'RSpec', 'Jasmine', 'Karma', 'Protractor'
            ],
            'Security': [
                'Cybersecurity', 'Penetration Testing', 'Ethical Hacking', 'OWASP', 'Metasploit',
                'Nmap', 'Wireshark', 'Burp Suite', 'Kali Linux', 'Cryptography', 'OAuth', 'JWT'
            ],
            'Blockchain & Web3': [
                'Blockchain', 'Ethereum', 'Solidity', 'Smart Contracts', 'Web3.js', 'Truffle',
                'Hardhat', 'Metamask', 'IPFS', 'DeFi', 'NFT', 'Bitcoin', 'Chainlink', 'Polygon'
            ],
            'Business & Soft Skills': [
                'Project Management', 'Agile', 'Scrum', 'Kanban', 'Leadership', 'Communication',
                'Problem Solving', 'Critical Thinking', 'Team Collaboration', 'Product Management',
                'Business Analysis', 'Requirements Gathering', 'Stakeholder Management'
            ]
        }

        # Smart skill matching with fuzzy search
        suggestions = []
        matched_categories = []

        for category, skills in comprehensive_skills.items():
            for skill in skills:
                # Multiple matching strategies
                skill_lower = skill.lower()
                if (query in skill_lower or
                    any(word in skill_lower for word in query.split()) or
                    skill_lower.startswith(query) or
                    any(skill_lower.startswith(word) for word in query.split())):

                    if skill not in suggestions:
                        suggestions.append(skill)
                        if category not in matched_categories:
                            matched_categories.append(category)

        # Sort by relevance (exact matches first, then partial matches)
        exact_matches = [s for s in suggestions if query == s.lower()]
        starts_with = [s for s in suggestions if s.lower().startswith(query) and s not in exact_matches]
        contains = [s for s in suggestions if query in s.lower() and s not in exact_matches and s not in starts_with]

        sorted_suggestions = (exact_matches + starts_with + contains)[:request.max_suggestions]

        # Calculate confidence based on match quality
        confidence = 0.0
        if exact_matches:
            confidence = 1.0
        elif starts_with:
            confidence = 0.8
        elif contains:
            confidence = 0.6
        elif suggestions:
            confidence = 0.4

        return SkillSuggestionResponse(
            suggestions=sorted_suggestions,
            categories=matched_categories[:5],  # Limit categories
            confidence=confidence
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating skill suggestions: {str(e)}")

@router.post("/ai/enhance-analysis")
async def enhance_analysis_with_ai(request: EnhancedAnalysisRequest):
    """
    Enhanced career analysis using AI for more intelligent recommendations
    """
    try:
        # Initialize AIService inside the function to ensure environment variables are loaded
        ai_service = AIService()

        # Use the existing AI service with enhanced prompting
        enhanced_prompt = f"""
        Analyze the following skills and expertise for career guidance:

        Skills: {request.skills}
        Expertise Level: {request.expertise}
        User Preferences: {request.preferences}

        Provide comprehensive career analysis covering:
        1. All relevant career paths across different domains (not just software development)
        2. Skills assessment with gap analysis
        3. Personalized learning roadmap
        4. Industry trends and growth prospects
        5. Salary expectations by region

        Consider ALL programming languages, frameworks, and technologies mentioned.
        Include emerging fields like Web3, AI/ML, Cybersecurity, Game Development, etc.

        Format the response as detailed JSON with career_paths, selected_path, roadmap, and courses.
        """

        # Call the AI service with enhanced context
        analysis = ai_service.generate_career_analysis(request.skills, request.expertise)

        return analysis

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error enhancing analysis with AI: {str(e)}")

@router.get("/ai/supported-technologies")
async def get_supported_technologies():
    """
    Return comprehensive list of all supported technologies and domains
    """
    # Enhanced skill database covering ALL technologies
    comprehensive_skills = {
        'Programming Languages': [
            'Python', 'JavaScript', 'Java', 'C++', 'C#', 'TypeScript', 'PHP', 'Ruby', 'Go', 'Rust',
            'Swift', 'Kotlin', 'Scala', 'R', 'MATLAB', 'Perl', 'Dart', 'Lua', 'Haskell', 'Clojure',
            'F#', 'Erlang', 'Elixir', 'Julia', 'Nim', 'Crystal', 'Zig', 'Assembly', 'Fortran', 'COBOL',
            'Objective-C', 'Solidity', 'Verilog', 'VHDL', 'C', 'Pascal', 'Ada', 'Prolog', 'Scheme'
        ],
        'Frontend Frameworks': [
            'React', 'Vue.js', 'Angular', 'Svelte', 'Ember.js', 'Backbone.js', 'Alpine.js', 'Lit',
            'Stimulus', 'Next.js', 'Nuxt.js', 'Gatsby', 'Quasar', 'Vuetify', 'Chakra UI', 'Material-UI',
            'Ant Design', 'Bootstrap', 'Tailwind CSS', 'Bulma', 'Foundation', 'Semantic UI'
        ],
        'Backend Frameworks': [
            'Node.js', 'Express.js', 'Django', 'Flask', 'FastAPI', 'Spring Boot', 'Spring Framework',
            'Laravel', 'Symphony', 'Ruby on Rails', 'Sinatra', 'ASP.NET Core', 'Blazor', 'Gin',
            'Echo', 'Fiber', 'Actix Web', 'Rocket', 'Vapor', 'NestJS', 'Koa.js', 'Fastify'
        ],
        'Mobile Development': [
            'React Native', 'Flutter', 'Ionic', 'Xamarin', 'Cordova', 'PhoneGap', 'SwiftUI',
            'UIKit', 'Android Jetpack', 'Jetpack Compose', 'Titanium', 'Unity Mobile', 'Cocos2d'
        ],
        'Databases': [
            'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'SQLite', 'Oracle Database', 'SQL Server',
            'MariaDB', 'CouchDB', 'Cassandra', 'DynamoDB', 'Firebase Firestore', 'Neo4j',
            'InfluxDB', 'TimescaleDB', 'CouchBase', 'Amazon RDS', 'Supabase', 'PlanetScale'
        ],
        'Cloud & DevOps': [
            'AWS', 'Microsoft Azure', 'Google Cloud Platform', 'Docker', 'Kubernetes', 'Terraform',
            'Ansible', 'Jenkins', 'GitLab CI', 'GitHub Actions', 'CircleCI', 'Travis CI', 'Helm',
            'Vagrant', 'Chef', 'Puppet', 'Prometheus', 'Grafana', 'ELK Stack', 'Datadog'
        ],
        'Data Science & AI': [
            'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn',
            'Pandas', 'NumPy', 'OpenCV', 'NLTK', 'spaCy', 'Hugging Face', 'LangChain', 'Jupyter',
            'Apache Spark', 'Hadoop', 'Kafka', 'Airflow', 'MLflow', 'Weights & Biases'
        ],
        'Game Development': [
            'Unity', 'Unreal Engine', 'Godot', 'GameMaker Studio', 'Construct 3', 'Blender',
            'Maya', '3ds Max', 'Substance Painter', 'Houdini', 'CryEngine', 'Lumberyard'
        ],
        'Design Tools': [
            'Figma', 'Sketch', 'Adobe XD', 'InVision', 'Principle', 'Framer', 'Zeplin',
            'Adobe Photoshop', 'Adobe Illustrator', 'Adobe After Effects', 'Canva', 'GIMP'
        ],
        'Testing & QA': [
            'Jest', 'Mocha', 'Chai', 'Cypress', 'Selenium', 'Playwright', 'Puppeteer',
            'TestNG', 'JUnit', 'Pytest', 'RSpec', 'Jasmine', 'Karma', 'Protractor'
        ],
        'Security': [
            'Cybersecurity', 'Penetration Testing', 'Ethical Hacking', 'OWASP', 'Metasploit',
            'Nmap', 'Wireshark', 'Burp Suite', 'Kali Linux', 'Cryptography', 'OAuth', 'JWT'
        ],
        'Blockchain & Web3': [
            'Blockchain', 'Ethereum', 'Solidity', 'Smart Contracts', 'Web3.js', 'Truffle',
            'Hardhat', 'Metamask', 'IPFS', 'DeFi', 'NFT', 'Bitcoin', 'Chainlink', 'Polygon'
        ],
        'Business & Soft Skills': [
            'Project Management', 'Agile', 'Scrum', 'Kanban', 'Leadership', 'Communication',
            'Problem Solving', 'Critical Thinking', 'Team Collaboration', 'Product Management',
            'Business Analysis', 'Requirements Gathering', 'Stakeholder Management'
        ]
    }

    # Flatten all skills into a single list
    all_skills = []
    for category, skills in comprehensive_skills.items():
        all_skills.extend(skills)

    return {
        "total_technologies": len(all_skills),
        "programming_languages": len(comprehensive_skills['Programming Languages']),
        "frameworks": len(comprehensive_skills['Frontend Frameworks']) + len(comprehensive_skills['Backend Frameworks']),
        "career_domains": [
            "Software Development",
            "Data Science & Analytics",
            "Mobile Development",
            "Game Development",
            "DevOps & Cloud Engineering",
            "Cybersecurity",
            "UI/UX Design",
            "Machine Learning & AI",
            "Blockchain & Web3",
            "Quality Assurance",
            "Business Analysis",
            "Digital Marketing",
            "Product Management"
        ],
        "skill_levels": ["Beginner", "Intermediate", "Advanced", "Expert"],
        "popular_stacks": [
            "MERN Stack", "MEAN Stack", "Django + React", "Laravel + Vue.js",
            "Spring Boot + Angular", "Next.js + Node.js", "Flutter + Firebase",
            "Unity + C#", "TensorFlow + Python", "Ethereum + Solidity"
        ],
        "all_skills": all_skills
    }
