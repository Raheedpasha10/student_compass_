import axios from 'axios';

// Token management
const TOKEN_KEY = 'career_analyzer_token';

export const tokenManager = {
  setToken: (token) => {
    localStorage.setItem(TOKEN_KEY, token);
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  },
  
  getToken: () => {
    return localStorage.getItem(TOKEN_KEY);
  },
  
  removeToken: () => {
    localStorage.removeItem(TOKEN_KEY);
    delete api.defaults.headers.common['Authorization'];
  },
  
  initializeToken: () => {
    const token = localStorage.getItem(TOKEN_KEY);
    if (token) {
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    }
  }
};

// Initialize token on import
tokenManager.initializeToken();

// Create axios instance with base configuration
const api = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? '' : 'http://localhost:8001', // Use relative URL in production
  timeout: 30000, // 30 seconds timeout for AI requests
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log('🚀 Sending request:', config.method?.toUpperCase(), config.url);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    console.log('✅ Received response:', response.status, response.config.url);
    return response;
  },
  (error) => {
    console.error('❌ Response error:', error);
    
    // Handle different error types
    if (error.response) {
      // Server responded with error status
      const message = error.response.data?.detail || error.response.data?.message || 'Server error';
      console.error(`Server Error (${error.response.status}):`, message);
      throw new Error(`Server Error: ${message}`);
    } else if (error.request) {
      // Request was made but no response received
      console.error('Network Error: No response received', error.request);
      throw new Error('Network Error: Unable to connect to server. Please check if the backend is running.');
    } else {
      // Something else happened
      console.error('Request Error:', error.message);
      throw new Error(`Request Error: ${error.message}`);
    }
  }
);

// API functions
export const careerAPI = {
  // Analyze career paths
  analyzeCareer: async (skills, expertise) => {
    try {
      const requestData = { skills, expertise };
      console.log('Sending request to /analyze:', requestData);
      const response = await api.post('/analyze', requestData);
      
      if (!response.data) {
        throw new Error('Empty response from server');
      }
      
      console.log('Received response from /analyze:', response.data);
      return response.data;
    } catch (error) {
      console.error('analyzeCareer error details:', {
        message: error.message,
        response: error.response,
        request: error.request,
        config: error.config
      });
      throw error;
    }
  },

  // Health check
  healthCheck: async () => {
    try {
      const response = await api.get('/health');
      return response.data;
    } catch (error) {
      console.error('Health check error:', error);
      throw error;
    }
  },

  // Generate mock test
  generateMockTest: async (skills, expertise, topic = null, userId = null) => {
    try {
      const requestData = {
        skills,
        expertise,
      };
      
      if (topic) {
        requestData.topic = topic;
      }
      
      const response = await api.post('/mock-test', requestData, {
        params: userId ? { user_id: userId } : {},
      });
      return response.data;
    } catch (error) {
      console.error('Mock test generation error:', error);
      throw error;
    }
  },

  // Authentication endpoints
  register: async (userData) => {
    try {
      const response = await api.post('/auth/register', userData);
      return response.data;
    } catch (error) {
      console.error('Registration error:', error);
      throw error;
    }
  },

  login: async (credentials) => {
    try {
      const response = await api.post('/auth/login', credentials);
      return response.data;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  },

  getMe: async () => {
    try {
      const response = await api.get('/auth/me');
      return response.data;
    } catch (error) {
      console.error('Get user error:', error);
      throw error;
    }
  },

  updateMe: async (userData) => {
    try {
      const response = await api.put('/auth/me', userData);
      return response.data;
    } catch (error) {
      console.error('Update user error:', error);
      throw error;
    }
  },

  // Skills endpoints
  updateSkills: async (userId, message) => {
    try {
      const response = await api.post('/update-skills', {
        user_id: userId,
        message: message
      });
      return response.data;
    } catch (error) {
      console.error('Update skills error:', error);
      throw error;
    }
  },

 // Multi-Agent Roadmap Generation (NEW V2 Endpoint)
  generateMultiAgentRoadmap: async (query, background = null, includeAgentDetails = true) => {
    try {
      const requestData = {
        query,
        include_agent_details: includeAgentDetails
      };
      
      if (background) {
        requestData.background = background;
      }
      
      console.log('🤖 Generating multi-agent roadmap:', requestData);
      const response = await api.post('/api/v2/roadmap/generate', {
        query: query,
        background: background || {}
      });
      console.log('✅ Multi-agent roadmap generated:', response.data);
      return response.data;
    } catch (error) {
      console.error('Multi-agent roadmap error:', error);
      throw error;
    }
  },

  // Check multi-agent system health
  checkMultiAgentHealth: async () => {
    try {
      const response = await api.get('/health');
      return response.data;
    } catch (error) {
      console.error('Multi-agent health check error:', error);
      throw error;
    }
  },

 // Enhanced AI endpoints
  suggestSkills: async (query, maxSuggestions = 8) => {
    try {
      const response = await api.post('/ai/suggest-skills', {
        query,
        max_suggestions: maxSuggestions
      });
      return response.data;
    } catch (error) {
      console.error('Skill suggestion error:', error);
      throw error;
    }
  },

  enhanceAnalysisWithAI: async (skills, expertise, preferences = {}) => {
    try {
      const response = await api.post('/ai/enhance-analysis', {
        skills,
        expertise,
        preferences
      });
      return response.data;
    } catch (error) {
      console.error('Enhanced analysis error:', error);
      throw error;
    }
  },

  getSupportedTechnologies: async () => {
    try {
      const response = await api.get('/ai/supported-technologies');
      return response.data;
    } catch (error) {
      console.error('Supported technologies error:', error);
      throw error;
    }
  },

  // Resource search (web search backed)
  searchResources: async (type, topic, limit = 20, level = 'intermediate') => {
    try {
      const response = await api.post('/resources/search', {
        type,
        topic,
        limit,
        level,
      });
      return response.data?.results || [];
    } catch (error) {
      console.error('Resource search error:', error);
      // Graceful fallback: empty list
      return [];
    }
  },

  // Root endpoint
  getRoot: async () => {
    try {
      const response = await api.get('/');
      return response.data;
    } catch (error) {
      console.error('Root endpoint error:', error);
      throw error;
    }
  },
};

// Export the analyzeCareer function directly for convenience
export const analyzeCareer = async (skills, expertise) => {
  try {
    const response = await api.post('/analyze', {
      skills,
      expertise,
    });
    return response.data;
  } catch (error) {
    console.error('Career analysis error:', error);
    throw error;
  }
};

// Export the generateMockTest function directly for convenience
export const generateMockTest = async (skills, expertise, topic = null, userId = null) => {
  try {
    const requestData = {
      skills,
      expertise,
    };
    
    if (topic) {
      requestData.topic = topic;
    }
    
    const response = await api.post('/mock-test', requestData, {
      params: userId ? { user_id: userId } : {},
    });
    return response.data;
  } catch (error) {
    console.error('Mock test generation error:', error);
    throw error;
  }
};

// Health check function to verify server connectivity
export const checkServerHealth = async () => {
  try {
    const response = await api.get('/health');
    return { status: 'online', data: response.data };
  } catch (error) {
    console.error('Server health check failed:', error);
    return { status: 'offline', error: error.message };
  }
};

export default api;