import React, { useState, useEffect } from 'react';
import { useAppContext } from '../context/AppContext';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { careerAPI } from '../services/api';
import LinearButton from '../components/LinearButton';
import LinearCard from '../components/LinearCard';
import LoadingSpinner from '../components/LoadingSpinner';
import LoadingScreen from '../components/LoadingScreen';
import { getRealResources } from '../constants/realResources';
import OptimizedPhaseDisplay from '../components/OptimizedPhaseDisplay';
import FunnelingReport from '../components/FunnelingReport';
// import EnhancedResourceCard from '../components/EnhancedResourceCard';

const SimplifiedUltimateRoadmap = () => {
  const ROADMAP_CACHE_VERSION = 'v2-structured-1';
  const [roadmapData, setRoadmapData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedResource, setSelectedResource] = useState(null);
  const [resources, setResources] = useState([]);
  const [loadingResources, setLoadingResources] = useState(false);
  const [usingDemoData, setUsingDemoData] = useState(false);
  const [agentStatus, setAgentStatus] = useState({ current: '', agents: [] });
  const [expandedPhases, setExpandedPhases] = useState(new Set());
  const navigate = useNavigate();
  const { currentSkills, currentExpertise, showGlobalFunnelingReport } = useAppContext();

  // Toggle phase expansion
  const togglePhaseExpansion = (phaseIndex) => {
    setExpandedPhases(prev => {
      const newSet = new Set(prev);
      if (newSet.has(phaseIndex)) {
        newSet.delete(phaseIndex);
      } else {
        newSet.add(phaseIndex);
      }
      return newSet;
    });
  };


  // Helper functions for platform styling
  const getPlatformColor = (platform) => {
    const colors = {
      'YouTube': '#FF0000',
      'Udemy': '#A435F0',
      'Coursera': '#0056D3',
      'edX': '#02262B',
      'Pluralsight': '#F15B2A',
      'LinkedIn Learning': '#0077B5',
      'Skillshare': '#00FF88',
      'GitHub': '#181717',
      'O\'Reilly': '#D3002D',
      'Amazon': '#FF9900',
      'Packt': '#83B81A',
      'Manning': '#D2691E',
      'freeCodeCamp': '#0A0A23',
      'Microsoft': '#5C2D91',
      'AWS': '#FF9900',
      'Google Cloud': '#4285F4',
      'Meta': '#1877F2',
      'Free Online': '#28A745'
    };
    return colors[platform] || '#6366F1';
  };

  const getPlatformIcon = (platform) => {
    const icons = {
      'YouTube': '📺',
      'Udemy': '🎓',
      'Coursera': '📚',
      'edX': '🎯',
      'Pluralsight': '💻',
      'LinkedIn Learning': '💼',
      'Skillshare': '🎨',
      'GitHub': '📝',
      'O\'Reilly': '📖',
      'Amazon': '📚',
      'Packt': '📘',
      'Manning': '📕',
      'freeCodeCamp': '💻',
      'Microsoft': '🏢',
      'AWS': '☁️',
      'Google Cloud': '☁️',
      'Meta': '👥',
      'Free Online': '🌐'
    };
    return icons[platform] || '🔗';
  };

  // Transform backend analysis -> learning_path for UI with detailed descriptions
  // Prefer structured_plan from V2 API to render immediately without regex parsing
  const buildLearningPath = (analysis) => {
    if (!analysis) return null;
    
    // If API provides a structured_plan (preferred), convert to learning_path directly
    if (analysis.structured_plan && analysis.structured_plan.phases) {
      return analysis.structured_plan.phases.map((ph, idx) => ({
        phase: ph.name || `Phase ${idx+1}`,
        duration: ph.duration_weeks ? `${ph.duration_weeks} weeks` : '—',
        topics: Array.isArray(ph.topics) && ph.topics.length ? ph.topics.slice(0, 6) : (Array.isArray(ph.goals) ? ph.goals.slice(0, 6) : [])
      }));
    }

    // If API already provides learning_path, use it
    if (analysis.learning_path && Array.isArray(analysis.learning_path)) {
      return analysis.learning_path;
    }
    
    // Extract detailed phases from AI roadmap
    if (analysis.roadmap?.[0]?.description) {
      const roadmapText = analysis.roadmap[0].description;
      
      // Parse phases from AI-generated roadmap
      const phaseMatches = roadmapText.match(/\*\*Phase \d+:.*?\*\*[\s\S]*?(?=\*\*Phase \d+:|$)/gi);
      
      if (phaseMatches && phaseMatches.length > 0) {
        return phaseMatches.slice(0, 7).map((phaseText, index) => {
          // Extract phase title
          const titleMatch = phaseText.match(/\*\*Phase \d+: (.*?)\*\*/);
          const title = titleMatch ? titleMatch[1].split('(')[0].trim() : `Phase ${index + 1}`;
          
          // Extract duration
          const durationMatch = phaseText.match(/\(([^)]*(?:month|week|day)[^)]*)\)/i);
          const duration = durationMatch ? durationMatch[1] : '—';
          
          // Extract topics (look for bullet points or key topics)
          const topicMatches = phaseText.match(/[-•]\s*([^\n]+)/g);
          const topics = topicMatches 
            ? topicMatches.slice(0, 5).map(t => t.replace(/^[-•]\s*/, '').trim())
            : [`Master ${title}`];
          
          return {
            phase: title,
            duration: duration,
            topics: topics
          };
        });
      }
    }
    
    // Legacy format fallback
    if (Array.isArray(analysis.roadmap)) {
      return analysis.roadmap.map((step) => ({
        phase: step.title || `Step ${step.step || ''}`,
        duration: step.duration || '—',
        topics: Array.isArray(step.resources) && step.resources.length > 0
          ? step.resources.slice(0, 5)
          : (step.description ? [step.description] : []),
      }));
    }
    
    return null;
  };

  // Fetch roadmap data - NOW USING MULTI-AGENT SYSTEM!
  useEffect(() => {
    const fetchRoadmapData = async () => {
      try {
        setError(null);
        setLoading(true);
        setUsingDemoData(false);
        setAgentStatus({ current: 'Initializing Multi-Agent AI System...', agents: [] });

        // Smart session-based caching (1 hour)
        const cacheKey = `roadmap_${ROADMAP_CACHE_VERSION}_${currentSkills}_${currentExpertise}`;
        const cached = sessionStorage.getItem(cacheKey);
        
        if (cached) {
          try {
            const { timestamp, data } = JSON.parse(cached);
            // Use cache if less than 1 hour old
            if (Date.now() - timestamp < 60 * 60 * 1000) {
              console.log('✅ Using cached roadmap (session storage)');
              // Pre-build learning path before setting state to avoid double render
              const learning_path = buildLearningPath(data);
              const finalData = { ...data, learning_path: learning_path || [] };
              setRoadmapData(finalData);
              setUsingDemoData(false);
              setLoading(false);
              return;
            }
          } catch (e) {
            console.log('Cache parse error, generating fresh roadmap');
          }
        }
        
        if (!currentSkills || !currentExpertise) {
          throw new Error('Skills and expertise are required to generate a personalized roadmap');
        }
        
        console.log('🤖 Generating roadmap with Multi-Agent AI System...');
        setAgentStatus({ current: 'Multi-Agent System Activated', agents: [
          { name: 'Strategic Planner', status: 'analyzing', model: 'Llama 3.3 70B' },
          { name: 'Practical Guide', status: 'analyzing', model: 'Gemini 2.0 Flash' },
          { name: 'Technical Expert', status: 'analyzing', model: 'Llama 3.1 8B' }
        ]});
        
        // NEW: Use Multi-Agent System for comprehensive analysis
        try {
          const multiAgentResult = await careerAPI.generateMultiAgentRoadmap(
            `I want to learn ${currentSkills} and become proficient in this field`,
            {
              current_skills: currentSkills,
              experience_level: currentExpertise,
              time_available: '10-15 hours per week',
              goals: `Master ${currentSkills} and build a successful career`
            },
            true // include agent details
          );

          console.log('✅ Multi-Agent AI Analysis Complete!');
          console.log(`📊 ${multiAgentResult.metadata.successful_agents}/${multiAgentResult.metadata.num_agents} AI agents contributed`);
          console.log('🔍 Funneling Report Available:', !!multiAgentResult.funneling_report);
          console.log('📄 Full API Response:', multiAgentResult);
          
          setAgentStatus({ current: 'Synthesizing optimal roadmap...', agents: [
            { name: 'Strategic Planner', status: 'completed', model: 'Llama 3.3 70B' },
            { name: 'Practical Guide', status: 'completed', model: 'Gemini 2.0 Flash' },
            { name: 'Technical Expert', status: 'completed', model: 'Llama 3.1 8B' }
          ]});

          // Parse the AI-generated roadmap and extract structured data
          const aiRoadmap = multiAgentResult.final_roadmap; 
          // Get structured plan (already cleaned by backend)
          const structuredPlan = multiAgentResult?.metadata?.structured_plan || null;
          
          // Create enhanced data structure with pre-built learning path
          const data = {
            career_paths: [
              {
                title: `${currentSkills} Specialist`,
                description: `Expert in ${currentSkills} - AI-generated career path`,
                required_skills: [currentSkills, 'Problem Solving', 'Critical Thinking'],
                salary_range: '₹6-20 lakhs (AI estimated)',
                growth_prospect: 'High - Based on multi-agent AI analysis'
              }
            ],
            selected_path: {
              title: `${currentSkills} Career Path`,
              description: `AI-powered personalized roadmap using 3 specialized agents`,
              required_skills: [currentSkills],
              salary_range: '₹6-20 lakhs',
              growth_prospect: 'High - AI analyzed'
            },
           roadmap: [
             {
               step: 1,
               title: 'AI-Generated Comprehensive Learning Roadmap',
               description: aiRoadmap,
               duration: 'Personalized based on your profile',
               resources: ['Multi-agent AI curated learning path']
             }
           ],
           structured_plan: structuredPlan, 
            courses: [],
            certifications: [],
            ai_generated: true,
            agent_insights: multiAgentResult.agent_insights,
            using_multi_agent: true,
            funneling_report: multiAgentResult.funneling_report,
            session_id: multiAgentResult.metadata?.session_id
          };

          // Pre-build learning path BEFORE setting state to avoid double render
          const learning_path = buildLearningPath(data);
          const finalData = { ...data, learning_path: learning_path || [] };
          setRoadmapData(finalData);
          setUsingDemoData(false);
          
          // Cache in sessionStorage (clears on browser close)
          try { 
            sessionStorage.setItem(cacheKey, JSON.stringify({ 
              timestamp: Date.now(), 
              data 
            })); 
          } catch (e) {
            console.log('SessionStorage full, clearing old entries');
            sessionStorage.clear();
          }
          
        } catch (multiAgentError) {
          console.warn('⚠️ Multi-agent system failed, falling back to standard AI:', multiAgentError);
          
          // Fallback to old system
          const data = await careerAPI.analyzeCareer(currentSkills, currentExpertise);
          const learning_path = buildLearningPath(data);
          const finalData = { ...data, learning_path: learning_path || [] };
          setRoadmapData(finalData);
          setUsingDemoData(false);
          try { sessionStorage.setItem(cacheKey, JSON.stringify({ timestamp: Date.now(), data: finalData })); } catch {}
        }
        
      } catch (err) {
        console.error('❌ Error fetching roadmap data:', err);
        setUsingDemoData(true);
        if (!err.message.includes('Network Error') && !err.message.includes('Unable to connect')) {
          setError(err.message || 'Failed to fetch roadmap data');
        }
      } finally {
        setLoading(false);
      }
    };

    if (currentSkills && currentExpertise) {
      fetchRoadmapData();
    } else {
        setError('Please provide your skills and expertise level to generate a personalized roadmap.');
      setLoading(false);
    }
  }, [currentSkills, currentExpertise]);

  // Fetch resources - Context-aware resource discovery based on career path
  const fetchResources = async (type) => {
    setLoadingResources(true);
    setSelectedResource(type);
    
    try {
      // Use career path context to find relevant resources
      let searchTopic = currentSkills;
      
      // If we have roadmap data, use the selected career path for better context
      if (roadmapData?.selected_path?.title) {
        const careerPath = roadmapData.selected_path.title.toLowerCase();
        
        // Map career paths to relevant topics for resource search
        if (careerPath.includes('data scientist') || careerPath.includes('data analyst')) {
          searchTopic = type === 'youtube' ? 'data science python' : 
                      type === 'courses' ? 'data science machine learning' :
                      type === 'books' ? 'data science statistics' :
                      'data science certification';
        } else if (careerPath.includes('software developer') || careerPath.includes('software engineer')) {
          searchTopic = type === 'youtube' ? `${currentSkills} programming` : 
                      type === 'courses' ? `${currentSkills} development` :
                      type === 'books' ? `${currentSkills} programming guide` :
                      `${currentSkills} developer certification`;
        } else if (careerPath.includes('web developer') || careerPath.includes('frontend')) {
          searchTopic = type === 'youtube' ? 'web development javascript' : 
                      type === 'courses' ? 'frontend web development' :
                      type === 'books' ? 'web development guide' :
                      'web developer certification';
        } else {
          // Use the original skills with career path context
          searchTopic = `${currentSkills} ${careerPath}`;
        }
      }
      
      console.log(`Fetching ${type} resources for: ${searchTopic}`);
      
      // Try API-based resource search with contextual topic
      const apiResources = await careerAPI.searchResources(type, searchTopic, 15, 'intermediate');
      
      if (apiResources && apiResources.length > 0) {
        // Transform API resources to match existing UI
        const transformedResources = apiResources.map(resource => ({
          title: resource.title,
          url: resource.url,
          thumbnail: resource.thumbnail || '',
          channel: resource.channel || resource.instructor || resource.author || '',
          description: resource.description || '',
          provider: resource.provider || resource.platform || '',
          platform: resource.provider || resource.platform || '',
          duration: resource.duration || '',
          views: resource.views || '',
          rating: resource.rating || '',
          students: resource.students || '',
          price: resource.price || '',
          level: resource.level || ''
        }));
        
        setResources(transformedResources);
        setLoadingResources(false);
        return;
      }
    } catch (error) {
      console.warn('API resource search failed, falling back to curated resources:', error);
    }
    
    // Enhanced fallback with career path context
    setTimeout(() => {
      try {
        // Generate contextual resources based on career path and roadmap
        let contextualResources = [];
        
        if (roadmapData?.selected_path?.title && roadmapData?.roadmap) {
          // Extract relevant topics from the roadmap steps
          const roadmapTopics = roadmapData.roadmap
            .flatMap(step => step.resources || [])
            .slice(0, 15);
          
          if (roadmapTopics.length > 0) {
            contextualResources = roadmapTopics.map((topic, index) => ({
              title: `${topic} - ${type === 'youtube' ? 'Video Tutorial' : 
                               type === 'courses' ? 'Complete Course' :
                               type === 'books' ? 'Learning Guide' : 
                               'Certification'}`,
              url: generateContextualUrl(topic, type),
              thumbnail: '',
              channel: getProviderForType(type),
              description: `Learn ${topic} as part of your ${roadmapData.selected_path.title} career path. Essential skill for mastering this role.`,
              provider: getProviderForType(type),
              platform: getProviderForType(type),
              duration: getDurationForType(type),
              rating: '4.5/5',
              price: getPriceForType(type),
              level: 'Intermediate'
            }));
          }
        }
        
        // If no roadmap context, use the original method with better topic matching
        if (contextualResources.length === 0) {
          const realResources = getRealResources(currentSkills, type, 15);
          contextualResources = realResources.map(resource => ({
            title: resource.title,
            url: resource.url,
            thumbnail: resource.thumbnail || '',
            channel: resource.channel || resource.instructor || resource.author || '',
            description: resource.description || '',
            provider: resource.provider || resource.platform || '',
            platform: resource.provider || resource.platform || '',
            duration: resource.duration || '',
            views: resource.views || '',
            rating: resource.rating || '',
            students: resource.students || '',
            price: resource.price || '',
            level: resource.level || ''
          }));
        }
        
        setResources(contextualResources);
      } catch (err) {
        console.error('Error loading contextual resources:', err);
        setResources([]);
      } finally {
        setLoadingResources(false);
      }
    }, 200);
  };

  // Helper functions for contextual resource generation
  const generateContextualUrl = (topic, type) => {
    const encodedTopic = encodeURIComponent(topic);
    const baseUrls = {
      youtube: `https://www.youtube.com/results?search_query=${encodedTopic}+tutorial+2024`,
      courses: `https://www.coursera.org/search?query=${encodedTopic}`,
      books: `https://www.amazon.com/s?k=${encodedTopic}+book`,
      certifications: `https://www.google.com/search?q=${encodedTopic}+certification`
    };
    return baseUrls[type] || '#';
  };

  const getProviderForType = (type) => {
    const providers = {
      youtube: 'YouTube',
      courses: 'Coursera',
      books: 'Amazon',
      certifications: 'Professional'
    };
    return providers[type] || 'Learning Platform';
  };

  const getDurationForType = (type) => {
    const durations = {
      youtube: '2-5 hours',
      courses: '4-8 weeks',
      books: 'Self-paced',
      certifications: '3-6 months'
    };
    return durations[type] || 'Varies';
  };

  const getPriceForType = (type) => {
    const prices = {
      youtube: 'Free',
      courses: '$39-79/month',
      books: '$25-45',
      certifications: '$150-300'
    };
    return prices[type] || 'Varies';
  };

  if (loading) {
    return (
      <LoadingScreen 
        title="Crafting Your Perfect Learning Path"
        subtitle="Our specialized AI agents are working together to create something amazing for you..."
        steps={[
          "🧠 Strategic Advisor analyzing market trends",
          "⚡ Technical Expert mapping skills & tools", 
          "🎯 Practical Coach finding hands-on projects",
          "🔗 Curating premium resources & courses"
        ]}
      />
    );
  }

  if (error && !usingDemoData) {
    return (
      <div className="min-h-screen bg-bg-primary text-text-primary pt-16">
        <div className="linear-container py-16">
          <div className="max-w-2xl mx-auto text-center">
            <div className="text-6xl mb-6">⚠️</div>
            <h2 className="text-title-3 font-semibold mb-4">Unable to load roadmap</h2>
            <p className="text-regular text-text-secondary mb-8">{error}</p>
            <LinearButton variant="primary" onClick={() => navigate('/')}>
              Go back home
            </LinearButton>
          </div>
        </div>
      </div>
    );
  }

  const displayRoadmap = roadmapData || {
    career_path: currentSkills || 'Your Career Path',
    expertise_level: currentExpertise || 'Beginner',
    learning_path: [
      { phase: 'Foundation', duration: '3 months', topics: ['Basics', 'Core Concepts', 'Best Practices'] },
      { phase: 'Intermediate', duration: '6 months', topics: ['Advanced Topics', 'Real Projects', 'Industry Tools'] },
      { phase: 'Expert', duration: '12+ months', topics: ['Specialization', 'Complex Systems', 'Leadership'] }
    ]
  };

  return (
    <div className="min-h-screen bg-bg-primary text-text-primary pt-16">
      {/* Header */}
      <section className="py-12 border-b border-border-primary">
        <div className="linear-container">
          <div className="max-w-3xl">
            {usingDemoData && (
              <motion.div 
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="mb-4"
              >
                <span 
                  className="inline-flex items-center gap-2 px-2 py-1 rounded-6 text-micro font-medium"
                  style={{ 
                    background: 'rgba(252, 120, 64, 0.15)',
                    color: '#fc7840',
                  }}
                >
                  <span className="w-1.5 h-1.5 rounded-full" style={{ background: '#fc7840' }}></span>
                  Using demo data
                </span>
              </motion.div>
            )}

            {/* AI Badge */}
            {roadmapData?.using_multi_agent && (
              <motion.div 
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                className="mb-4"
              >
                <span 
                  className="inline-flex items-center gap-2 px-3 py-1.5 rounded-6 text-mini font-medium"
                  style={{ 
                    background: 'rgba(113, 112, 255, 0.15)',
                    color: 'var(--color-accent-hover)',
                    border: '1px solid rgba(113, 112, 255, 0.3)'
                  }}
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-accent-hover"></span>
                  AI-GENERATED BY 3 AGENTS
                </span>
              </motion.div>
            )}

            <h1 className="text-title-4 font-semibold mb-4" style={{ letterSpacing: '-.022em' }}>
              Learning Roadmap: {currentSkills}
            </h1>
            <p className="text-regular text-text-secondary mb-6">
              Experience Level: <span className="font-medium text-text-primary">{currentExpertise}</span>
            </p>
            
            <div className="flex gap-2 flex-wrap">
              <LinearButton variant="secondary" size="small" onClick={() => navigate('/career-path')}>
                ← Change career
              </LinearButton>
              <LinearButton variant="secondary" size="small" onClick={() => navigate('/flowchart')}>
                View flowchart →
              </LinearButton>
            </div>
          </div>
              </div>
      </section>

      {/* AI-Generated Full Roadmap - Optimized Display */}
      {roadmapData?.structured_plan?.phases?.length > 0 && (
        <section className="py-16 border-b border-border-primary">
          <div className="linear-container">
            <div className="max-w-4xl">
              <div className="text-center mb-12">
                <h2 className="text-title-2 font-semibold mb-4" style={{ letterSpacing: '-.012em' }}>
                  Your Personalized Learning Path
                </h2>
                <p className="text-regular text-text-secondary">
                  Structured phases designed by our AI agents for optimal learning progression
                </p>
              </div>
              
              <OptimizedPhaseDisplay 
                phases={roadmapData.structured_plan.phases}
                currentSkills={currentSkills}
              />
            </div>
          </div>
        </section>
      )}

      {/* Funneling Report Section */}
      {showGlobalFunnelingReport && (
        <section className="py-16 border-b border-border-primary">
          <div className="linear-container">
            <div className="max-w-4xl">
              {roadmapData?.funneling_report && Object.keys(roadmapData.funneling_report).length > 0 ? (
                <FunnelingReport 
                  sessionId={roadmapData.session_id}
                  report={roadmapData.funneling_report}
                />
              ) : roadmapData?.using_multi_agent && roadmapData?.agent_insights && roadmapData.agent_insights.length > 0 ? (
                // Create synthetic funneling report from agent insights
                <FunnelingReport 
                  sessionId={roadmapData.session_id || 'current'}
                  report={{
                    session_id: roadmapData.session_id || 'current',
                    agent_performance: {
                      total_agents: roadmapData.agent_insights.length,
                      successful_agents: roadmapData.agent_insights.filter(a => a.confidence > 0).length,
                      success_rate_percent: Math.round((roadmapData.agent_insights.filter(a => a.confidence > 0).length / roadmapData.agent_insights.length) * 100),
                      individual_results: roadmapData.agent_insights.map(agent => ({
                        agent_name: agent.agent_name,
                        success: agent.confidence > 0,
                        confidence_score: agent.confidence,
                        provider: agent.agent_name.includes('Strategic') ? 'groq' : 
                                 agent.agent_name.includes('Practical') ? 'google' : 'groq',
                        model: agent.agent_name.includes('Strategic') ? 'llama-3.3-70b-versatile' :
                               agent.agent_name.includes('Practical') ? 'gemini-2.0-flash-exp' : 'llama-3.1-8b-instant',
                        response_time: '< 15s'
                      }))
                    },
                    funneling_process: {
                      method: 'confidence_based_selection',
                      best_agent: roadmapData.agent_insights.reduce((best, current) => 
                        current.confidence > best.confidence ? current : best
                      ).agent_name,
                      final_confidence: Math.max(...roadmapData.agent_insights.map(a => a.confidence)),
                      confidence_scores: Object.fromEntries(
                        roadmapData.agent_insights.map(a => [a.agent_name, a.confidence])
                      ),
                      decision_rationale: `Selected ${roadmapData.agent_insights.reduce((best, current) => 
                        current.confidence > best.confidence ? current : best
                      ).agent_name} based on highest confidence score`
                    },
                    output_metrics: {
                      total_execution_time: '< 30s',
                      phases_generated: roadmapData?.structured_plan?.phases?.length || 0,
                      content_items: roadmapData?.structured_plan?.phases?.reduce((total, phase) => 
                        total + (phase.topics?.length || 0) + (phase.projects?.length || 0), 0
                      ) || 0,
                      roadmap_length: roadmapData?.final_roadmap?.length || 0
                    }
                  }}
                />
              ) : (
                <div className="bg-bg-secondary border border-border-primary rounded-8 p-6 text-center">
                  <div className="text-6xl mb-4">🤖</div>
                  <h3 className="text-large font-semibold text-text-primary mb-2">
                    Generate a Multi-Agent Roadmap
                  </h3>
                  <p className="text-regular text-text-secondary mb-4">
                    This roadmap wasn't generated using our advanced multi-agent system.
                  </p>
                  <button 
                    onClick={() => {
                      // Clear cache and regenerate
                      sessionStorage.clear();
                      window.location.reload();
                    }}
                    className="px-4 py-2 bg-accent hover:bg-accent-hover text-white rounded-6 text-small font-medium transition-colors"
                  >
                    Generate New Multi-Agent Roadmap
                  </button>
                </div>
              )}
            </div>
          </div>
        </section>
      )}

      {/* Learning Path Summary - Fixed Rendering */}
      {((roadmapData?.structured_plan?.phases?.length > 0) || (roadmapData?.learning_path?.length > 0)) && (
        <section className="py-12">
          <div className="linear-container">
            <div className="max-w-3xl">
              <h2 className="text-title-2 font-semibold mb-8" style={{ letterSpacing: '-.012em' }}>
                Quick Phase Overview
              </h2>

              <div className="space-y-4 relative">
                {(() => {
                  console.log('🔍 Debug - roadmapData structure:', {
                    has_structured_plan: !!roadmapData?.structured_plan,
                    structured_plan_phases: roadmapData?.structured_plan?.phases?.length || 0,
                    has_learning_path: !!roadmapData?.learning_path,
                    learning_path_length: roadmapData?.learning_path?.length || 0,
                    sample_phase: roadmapData?.structured_plan?.phases?.[0] || roadmapData?.learning_path?.[0]
                  });
                  
                  const phasesData = roadmapData?.structured_plan?.phases || roadmapData?.learning_path || [];
                  console.log('🎯 Using phases data:', phasesData);
                  
                  return phasesData.map((phase, index) => {
                    const isLast = index === phasesData.length - 1;
                    const isExpanded = expandedPhases.has(index);
                    
                    // Enhanced data extraction with proper handling
                    const phaseName = phase.name || phase.phase || `Phase ${index + 1}`;
                    const phaseDuration = phase.duration_weeks ? `${phase.duration_weeks} weeks` : phase.duration || '4-6 weeks';
                    const phaseOverview = phase.overview || phase.description || '';
                    
                    // Key points for collapsed view (3-4 items max)
                    const keyTopics = (phase.topics || phase.goals || []).slice(0, 3);
                    
                    // Full details for expanded view
                    const allTopics = phase.topics || [];
                    const allGoals = phase.goals || [];
                    const projects = phase.projects || [];
                    const tools = phase.tools || [];
                    const resources = phase.resources || [];
                    const checkpoints = phase.checkpoints || [];
                    
                    return (
                      <div key={`phase-${index}`} className="relative">
                        {/* Connecting lines between phases */}
                        {!isLast && (
                          <div className="absolute left-[32px] top-[100px] w-0.5 h-16 bg-border-primary z-0"></div>
                        )}

                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: index * 0.1, duration: 0.4, ease: [0.25, 0.46, 0.45, 0.94] }}
                          className="relative z-10"
                        >
                          <LinearCard className="p-0 group overflow-hidden bg-bg-secondary border border-border-primary">
                            {/* Phase Header - Always Visible */}
                            <div 
                              className="p-6 cursor-pointer hover:bg-bg-tertiary transition-colors"
                              onClick={() => togglePhaseExpansion(index)}
                            >
                              <div className="flex items-start justify-between mb-4">
                                <div className="flex-1">
                                  <div className="flex items-center gap-3 mb-2">
                                    <h3 className="text-regular font-semibold text-text-primary group-hover:text-accent transition-colors">
                                      {phaseName}
                                    </h3>
                                    <motion.button
                                      className="p-1 rounded-4 bg-bg-primary border border-border-secondary hover:border-border-primary transition-colors"
                                      whileHover={{ scale: 1.05 }}
                                      whileTap={{ scale: 0.95 }}
                                    >
                                      <motion.svg 
                                        width="16" 
                                        height="16" 
                                        viewBox="0 0 24 24" 
                                        fill="none" 
                                        stroke="currentColor" 
                                        strokeWidth="2"
                                        className="text-text-tertiary"
                                        animate={{ rotate: isExpanded ? 180 : 0 }}
                                        transition={{ duration: 0.2 }}
                                      >
                                        <polyline points="6 9 12 15 18 9"/>
                                      </motion.svg>
                                    </motion.button>
                                  </div>
                                  
                                  <div className="flex items-center gap-4 text-small text-text-tertiary mb-3">
                                    <span className="flex items-center gap-1.5">
                                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                        <circle cx="12" cy="12" r="10"/>
                                        <polyline points="12 6 12 12 16 14"/>
                                      </svg>
                                      Duration: {phaseDuration}
                                    </span>
                                    {!isExpanded && keyTopics.length > 0 && (
                                      <span className="text-text-quaternary">
                                        {keyTopics.length} key topics
                                      </span>
                                    )}
                                  </div>

                                  {/* Overview Text */}
                                  {phaseOverview && (
                                    <p className="text-small text-text-secondary mb-4 leading-relaxed">
                                      {phaseOverview}
                                    </p>
                                  )}

                                  {/* Collapsed View - Key Points Only */}
                                  {!isExpanded && (
                                    <div className="space-y-2">
                                      {keyTopics.map((topic, i) => (
                                        <motion.div 
                                          key={`key-${i}`}
                                          className="flex items-center gap-2.5 text-small text-text-secondary"
                                          initial={{ opacity: 0, x: -10 }}
                                          animate={{ opacity: 1, x: 0 }}
                                          transition={{ delay: index * 0.1 + i * 0.05, duration: 0.3 }}
                                        >
                                          <motion.span 
                                            className="w-1.5 h-1.5 rounded-full bg-accent flex-shrink-0"
                                            initial={{ scale: 0 }}
                                            animate={{ scale: 1 }}
                                            transition={{ delay: index * 0.1 + i * 0.05, type: "spring", stiffness: 500 }}
                                          ></motion.span>
                                          {typeof topic === 'string' ? topic : topic.name || topic}
                                        </motion.div>
                                      ))}
                                      
                                      {(allTopics.length > 3 || allGoals.length > 3) && (
                                        <div className="flex items-center gap-2 text-micro text-text-tertiary mt-3">
                                          <span className="w-1.5 h-1.5 rounded-full bg-border-primary flex-shrink-0"></span>
                                          Click to see all {Math.max(allTopics.length, allGoals.length)} items + projects & resources
                                        </div>
                                      )}
                                    </div>
                                  )}
                                </div>
                                
                                <motion.span 
                                  className="text-micro font-semibold px-3 py-1 rounded-6 flex items-center gap-1.5 ml-4"
                                  style={{ 
                                    background: 'rgba(255, 255, 255, 0.05)',
                                    color: 'var(--color-text-primary)',
                                    border: '1px solid rgba(255, 255, 255, 0.1)'
                                  }}
                                  whileHover={{ scale: 1.05 }}
                                  transition={{ duration: 0.2 }}
                                >
                                  <span className="w-1.5 h-1.5 rounded-full bg-text-primary"></span>
                                  Phase {index + 1}
                                </motion.span>
                              </div>
                            </div>

                            {/* Expanded Details */}
                            <AnimatePresence>
                              {isExpanded && (
                                <motion.div
                                  initial={{ height: 0, opacity: 0 }}
                                  animate={{ height: 'auto', opacity: 1 }}
                                  exit={{ height: 0, opacity: 0 }}
                                  transition={{ duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
                                  className="border-t border-border-primary bg-bg-primary"
                                >
                                  <div className="p-6 space-y-6">
                                    {/* Learning Goals */}
                                    {allGoals.length > 0 && (
                                      <div>
                                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                                            <path d="M9 11l3 3L22 4"/>
                                          </svg>
                                          Learning Goals
                                        </h4>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                          {allGoals.map((goal, i) => (
                                            <motion.div 
                                              key={`goal-${i}`}
                                              className="flex items-start gap-2 p-3 rounded-6 bg-bg-secondary border border-border-secondary"
                                              initial={{ opacity: 0, x: -10 }}
                                              animate={{ opacity: 1, x: 0 }}
                                              transition={{ delay: i * 0.05 }}
                                            >
                                              <span className="w-1.5 h-1.5 rounded-full bg-accent flex-shrink-0 mt-1.5"></span>
                                              <span className="text-small text-text-secondary">{goal}</span>
                                            </motion.div>
                                          ))}
                                        </div>
                                      </div>
                                    )}

                                    {/* Topics to Learn */}
                                    {allTopics.length > 0 && (
                                      <div>
                                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                                            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                                            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                                          </svg>
                                          Key Topics
                                        </h4>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                          {allTopics.map((topic, i) => (
                                            <motion.div 
                                              key={`topic-${i}`}
                                              className="flex items-start gap-2 p-3 rounded-6 bg-bg-secondary border border-border-secondary"
                                              initial={{ opacity: 0, x: -10 }}
                                              animate={{ opacity: 1, x: 0 }}
                                              transition={{ delay: i * 0.05 }}
                                            >
                                              <span className="w-1.5 h-1.5 rounded-full bg-accent flex-shrink-0 mt-1.5"></span>
                                              <div className="flex-1">
                                                <span className="text-small text-text-primary font-medium">
                                                  {typeof topic === 'string' ? topic : topic.name || topic}
                                                </span>
                                                {typeof topic === 'object' && topic.description && (
                                                  <p className="text-micro text-text-tertiary mt-1">{topic.description}</p>
                                                )}
                                              </div>
                                            </motion.div>
                                          ))}
                                        </div>
                                      </div>
                                    )}

                                    {/* Hands-on Projects */}
                                    {projects.length > 0 && (
                                      <div>
                                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                                            <polyline points="9 11 12 14 22 4"/>
                                            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
                                          </svg>
                                          Hands-on Projects
                                        </h4>
                                        <div className="space-y-3">
                                          {projects.map((project, i) => (
                                            <motion.div 
                                              key={`project-${i}`}
                                              className="p-4 rounded-6 bg-bg-secondary border border-border-secondary"
                                              initial={{ opacity: 0, y: 10 }}
                                              animate={{ opacity: 1, y: 0 }}
                                              transition={{ delay: i * 0.08 }}
                                            >
                                              <h5 className="text-small font-medium text-text-primary mb-1">
                                                {typeof project === 'string' ? project : project.name || project}
                                              </h5>
                                              {typeof project === 'object' && project.description && (
                                                <p className="text-small text-text-secondary mb-2">{project.description}</p>
                                              )}
                                              {typeof project === 'object' && project.deliverables && project.deliverables.length > 0 && (
                                                <div className="flex flex-wrap gap-1 mt-2">
                                                  {project.deliverables.slice(0, 3).map((deliverable, di) => (
                                                    <span key={di} className="text-micro px-2 py-0.5 rounded-4 bg-bg-primary text-text-tertiary">
                                                      {deliverable}
                                                    </span>
                                                  ))}
                                                </div>
                                              )}
                                            </motion.div>
                                          ))}
                                        </div>
                                      </div>
                                    )}

                                    {/* Tools & Technologies */}
                                    {tools.length > 0 && (
                                      <div>
                                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                                            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                                          </svg>
                                          Tools & Technologies
                                        </h4>
                                        <div className="flex flex-wrap gap-2">
                                          {tools.map((tool, i) => (
                                            <motion.span 
                                              key={`tool-${i}`}
                                              className="px-3 py-1.5 rounded-6 bg-bg-secondary border border-border-secondary text-small text-text-primary"
                                              initial={{ opacity: 0, scale: 0.8 }}
                                              animate={{ opacity: 1, scale: 1 }}
                                              transition={{ delay: i * 0.03 }}
                                              whileHover={{ scale: 1.02, borderColor: 'var(--color-accent)' }}
                                            >
                                              {typeof tool === 'string' ? tool : tool.name || tool}
                                            </motion.span>
                                          ))}
                                        </div>
                                      </div>
                                    )}
                                  </div>
                                </motion.div>
                              )}
                            </AnimatePresence>
                          </LinearCard>
                        </motion.div>
                      </div>
                    );
                  });
                })()}
              </div>
            </div>
          </div>
        </section>
      )}

      {/* Resources */}
      <section className="py-12 border-t border-border-primary">
        <div className="linear-container">
          <div className="max-w-3xl">
            <h2 className="text-title-2 font-semibold mb-6" style={{ letterSpacing: '-.012em' }}>
              Learning resources
            </h2>

            <div className="flex flex-wrap gap-2 mb-8">
              {[
                { type: 'youtube', label: 'YouTube Videos', icon: '📺' },
                { type: 'books', label: 'Books', icon: '📚' },
                { type: 'certifications', label: 'Certifications', icon: '🎓' },
                { type: 'courses', label: 'Courses', icon: '💻' }
              ].map(({ type, label, icon }) => (
                <LinearButton
                  key={type}
                  variant={selectedResource === type ? 'secondary' : 'tertiary'}
                  size="small"
                  onClick={() => fetchResources(type)}
                >
                  <span className="mr-1.5">{icon}</span>
                  {label}
                </LinearButton>
                      ))}
                    </div>

            {loadingResources && (
              <div className="py-8">
                <LoadingSpinner size="md" text="Loading resources..." />
                  </div>
                )}

            {!loadingResources && resources.length > 0 && (
              <AnimatePresence mode="wait">
                <motion.div
                  key={selectedResource}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -10 }}
                  transition={{ duration: 0.2 }}
                  className="grid grid-cols-1 md:grid-cols-2 gap-2"
                >
                  {resources.map((resource, index) => (
                    <motion.div
                      key={index} 
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: index * 0.03 }}
                    >
                      <a
                        href={resource.url || '#'}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="block"
                        title={resource.title}
                      >
                        <LinearCard className="p-4 hover:bg-bg-tertiary transition-regular group">
                          <div className="flex items-start gap-3">
                            {/* Icon */}
                            <div className="flex-shrink-0">
                              <div 
                                className="w-12 h-12 rounded-8 flex items-center justify-center text-lg"
                                style={{
                                  background: getPlatformColor(resource.provider),
                                  color: 'white'
                                }}
                              >
                                {getPlatformIcon(resource.provider)}
                              </div>
                            </div>

                            {/* Content */}
                            <div className="flex-1 min-w-0">
                              <h4 className="text-small font-medium text-text-primary mb-1 line-clamp-2 group-hover:text-accent transition-colors">
                                {resource.title}
                              </h4>
                              
                              <div className="flex items-center gap-2 mb-2">
                                <span className="text-micro font-medium px-2 py-0.5 rounded-4" 
                                      style={{ 
                                        background: getPlatformColor(resource.provider) + '20',
                                        color: getPlatformColor(resource.provider)
                                      }}>
                                  {resource.provider}
                                </span>
                                {resource.duration && (
                                  <span className="text-micro text-text-tertiary">
                                    {resource.duration}
                                  </span>
                                )}
                                {resource.rating && (
                                  <span className="text-micro text-text-tertiary">
                                    ⭐ {resource.rating}
                                  </span>
                                )}
                                {resource.price && (
                                  <span className="text-micro font-medium"
                                        style={{ color: resource.price.toLowerCase().includes('free') ? '#10B981' : '#F59E0B' }}>
                                    {resource.price}
                                  </span>
                                )}
                              </div>

                              {resource.description && (
                                <p className="text-micro text-text-secondary line-clamp-2">
                                  {resource.description}
                                </p>
                              )}
                            </div>

                            {/* Action */}
                            <div className="flex-shrink-0">
                              <span className="text-micro text-text-tertiary group-hover:text-accent transition-colors">
                                View →
                              </span>
                            </div>
                          </div>
                        </LinearCard>
                      </a>
                    </motion.div>
                  ))}
                </motion.div>
              </AnimatePresence>
            )}
          </div>
          </div>
      </section>

      {/* CTA */}
      <section className="py-16 border-t border-border-primary">
        <div className="linear-container text-center">
          <h2 className="text-title-3 font-semibold mb-4">
            Ready to start learning?
              </h2>
          <p className="text-regular text-text-secondary mb-8 max-w-2xl mx-auto">
            Follow this roadmap to master {currentSkills} and achieve your career goals
          </p>
          <LinearButton variant="primary" size="large" onClick={() => navigate('/flowchart')}>
            View interactive flowchart
          </LinearButton>
        </div>
      </section>
    </div>
  );
};

export default SimplifiedUltimateRoadmap;
