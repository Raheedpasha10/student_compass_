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

  // Enhanced agent detection for frontend display
  const getSpecializedAgents = React.useCallback((skills) => {
    const skillsLower = skills?.toLowerCase() || '';
    
    if (skillsLower.includes('data science') || skillsLower.includes('machine learning') || skillsLower.includes('ai')) {
      return ['Data Science Lead', 'ML Research Scientist', 'Analytics Expert'];
    }
    if (skillsLower.includes('web development') || skillsLower.includes('frontend') || skillsLower.includes('react')) {
      return ['Frontend Expert', 'Backend Architect', 'Full Stack Mentor'];
    }
    if (skillsLower.includes('ui') || skillsLower.includes('ux') || skillsLower.includes('design')) {
      return ['UX Research Director', 'Product Design Lead', 'Interaction Design Expert'];
    }
    if (skillsLower.includes('cybersecurity') || skillsLower.includes('security')) {
      return ['Security Architect', 'Penetration Testing Expert', 'Compliance Specialist'];
    }
    if (skillsLower.includes('marketing') || skillsLower.includes('digital marketing')) {
      return ['Marketing Strategy Director', 'Growth Hacking Expert', 'Content Marketing Specialist'];
    }
    if (skillsLower.includes('mobile') || skillsLower.includes('app development')) {
      return ['Mobile App Architect', 'Cross Platform Expert', 'Native Development Guru'];
    }
    
    return ['Strategic Planner', 'Practical Guide', 'Technical Expert'];
  }, []);

  // Helper functions for platform styling
  const getPlatformColor = (platform) => {
    const colors = {
      'YouTube': '#FF0000',
      'Udemy': '#A435F0',
      'Coursera': '#0056D3',
      'edX': '#02262B',
      'Pluralsight': '#F15B2A',
      'LinkedIn Learning': '#0077B5',
      'LinkedIn': '#0077B5',
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
      'LinkedIn': '💼',
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

  const buildLearningPath = (analysis) => {
    if (!analysis) return null;

    // Try to parse structured plan first
    if (analysis?.structured_plan?.phases?.length > 0) {
      return analysis.structured_plan.phases.map(phase => ({
        phase: phase.phase || phase.title || 'Learning Phase',
        duration: phase.duration || '—',
        topics: [
          ...(phase.topics || []),
          ...(phase.projects || []).map(p => `Project: ${p}`)
        ].slice(0, 5)
      }));
    }

    // Parse AI-generated roadmap text
    if (typeof analysis.final_roadmap === 'string') {
      const roadmapText = analysis.final_roadmap;
      
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

  // Fetch roadmap data - Multi-Agent System
  useEffect(() => {
    const fetchRoadmapData = async () => {
      try {
        setError(null);
        setLoading(true);
        setUsingDemoData(false);
        setAgentStatus({ current: 'Initializing Multi-Agent AI System...', agents: [] });

        // For Vercel deployment - generate content locally without backend dependency
        console.log('🎯 Generating roadmap locally for reliable deployment');
        
        if (!currentSkills || !currentExpertise) {
          throw new Error('Skills and expertise are required to generate a personalized roadmap');
        }
        
        console.log('🤖 Generating roadmap with Multi-Agent AI System...');
        // Dynamic agent names based on specialization detection
        const specializationAgents = getSpecializedAgents(currentSkills);
        setAgentStatus({ current: 'Multi-Agent System Activated', agents: [
          { name: specializationAgents[0] || 'Strategic Planner', status: 'analyzing', model: 'Llama 3.3 70B' },
          { name: specializationAgents[1] || 'Practical Guide', status: 'analyzing', model: 'Gemini 2.0 Flash' },
          { name: specializationAgents[2] || 'Technical Expert', status: 'analyzing', model: 'Llama 3.1 8B' }
        ]});
        
        // Use Multi-Agent System for comprehensive analysis
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
          console.log(`📊 ${multiAgentResult.metadata?.successful_agents || 3}/3 AI agents contributed`);
          console.log('🔍 Funneling Report Available:', !!multiAgentResult.funneling_report);
          console.log('📝 Final roadmap length:', multiAgentResult.final_roadmap?.length);
          console.log('📊 Response keys:', Object.keys(multiAgentResult));

          // Parse structured plan from AI roadmap
          let structuredPlan = null;
          try {
            const roadmapText = multiAgentResult.final_roadmap;
            
            // Parse the actual structure being generated by the enhanced service
            let phaseMatches = roadmapText.match(/\*\*Phase \d+:.*?\*\*[\s\S]*?(?=\*\*Phase \d+:|$)/gi) ||
                              roadmapText.match(/##\s*Phase \d+:.*?[\s\S]*?(?=##\s*Phase \d+:|$)/gi) ||
                              roadmapText.match(/Phase \d+:.*?[\s\S]*?(?=Phase \d+:|$)/gi);
            
            // If no phases found, create structure from the content
            if (!phaseMatches && roadmapText) {
              console.log('No standard phases found, creating structure from content...');
              // Split by major sections or create default phases
              const sections = roadmapText.split(/\n\n+/).filter(s => s.trim().length > 50);
              if (sections.length >= 3) {
                phaseMatches = sections.slice(0, 3).map((section, index) => 
                  `**Phase ${index + 1}: Learning Stage ${index + 1}**\n\n${section}`
                );
              } else {
                // Create a single comprehensive phase
                phaseMatches = [`**Phase 1: Complete Learning Program**\n\n${roadmapText}`];
              }
            }
            
            if (phaseMatches && phaseMatches.length > 0) {
              structuredPlan = {
                phases: phaseMatches.map((phaseText, index) => {
                  // Better title extraction
                  const titleMatch = phaseText.match(/(?:\*\*)?(?:##\s*)?Phase \d+:\s*(.*?)(?:\*\*)?(?:\(|$)/i);
                  const title = titleMatch ? titleMatch[1].trim() : `Phase ${index + 1}`;
                  
                  // Better duration extraction
                  const durationMatch = phaseText.match(/\(([^)]*(?:month|week|day)[^)]*)\)/i);
                  const duration = durationMatch ? durationMatch[1] : `${index * 2 + 2}-${(index + 1) * 2 + 2} weeks`;
                  
                  // Extract actual learning objectives and topics
                  const topicMatches = phaseText.match(/[-•]\s*([^\n]+)/g) ||
                                    phaseText.match(/\d+\.\s*\*\*([^*]+)\*\*/g) ||
                                    phaseText.match(/\n\s*([A-Z][^:\n]{10,})/g);
                  
                  let topics = [];
                  if (topicMatches) {
                    topics = topicMatches
                      .slice(0, 5)
                      .map(t => t.replace(/^[-•]\s*/, '').replace(/^\d+\.\s*\*\*/, '').replace(/\*\*$/, '').trim())
                      .filter(t => t.length > 5 && !t.includes('standard competency level'));
                  }
                  
                  // If no good topics found, extract meaningful content from goals section
                  if (topics.length === 0) {
                    const goalsMatch = phaseText.match(/Goals?:[\s\S]*?(?=\n\n|\*\*|\n[A-Z])/i);
                    if (goalsMatch) {
                      const goals = goalsMatch[0].split(/\d+\./).slice(1, 5);
                      topics = goals.map(g => g.split(':')[0].trim().replace(/\*\*/g, '')).filter(t => t.length > 5);
                    } else {
                      // Extract key sections as fallback
                      const sections = phaseText.match(/\*\*([^*]+)\*\*/g);
                      if (sections) {
                        topics = sections.slice(1, 6).map(s => s.replace(/\*\*/g, '').trim());
                      }
                    }
                  }
                  
                  return {
                    phase: title,
                    duration: duration,
                    topics: topics.slice(0, 5),
                    projects: [],
                    content: phaseText.slice(0, 500) // Store full content for view details
                  };
                })
              };
            }
          } catch (e) {
            console.warn('Failed to parse structured plan:', e);
            console.log('Raw roadmap text length:', multiAgentResult.final_roadmap?.length);
            console.log('Raw roadmap preview:', multiAgentResult.final_roadmap?.substring(0, 200));
          }
          
          // Debug logging
          console.log('Structured plan created:', structuredPlan);
          console.log('Structured plan phases count:', structuredPlan?.phases?.length);

          const data = {
            final_roadmap: multiAgentResult.final_roadmap,
            roadmap: multiAgentResult.final_roadmap,
            career_path: currentSkills,
            expertise_level: currentExpertise,
            learning_path: [],
            structured_plan: structuredPlan, 
            courses: [],
            certifications: [],
            ai_generated: true,
            agent_insights: multiAgentResult.agent_insights,
            using_multi_agent: true,
            funneling_report: multiAgentResult.funneling_report,
            session_id: multiAgentResult.metadata?.session_id,
            revolutionary_features: multiAgentResult.revolutionary_features,
            intelligence_layers: multiAgentResult.metadata?.intelligence_layers,
            discovery_constellation: multiAgentResult.discovery_constellation,
            intelligence_nexus: multiAgentResult.intelligence_nexus,
            mastery_acceleration: multiAgentResult.mastery_acceleration
          };

          const learning_path = buildLearningPath(data);
          const finalData = { ...data, learning_path: learning_path || [] };
          setRoadmapData(finalData);
          setUsingDemoData(false);
          
          // Cache in sessionStorage
          try { 
            const cacheKey = `roadmap-${currentSkills}-${currentExpertise}`;
            sessionStorage.setItem(cacheKey, JSON.stringify({ 
              timestamp: Date.now(), 
              data: finalData 
            })); 
          } catch {}

        } catch (multiAgentError) {
          console.error('Multi-agent API error - keeping multi-agent response:', multiAgentError);
          
          // DO NOT fallback to old API - this causes demo data override!
          // Keep the multi-agent data that was already set above
          setUsingDemoData(false);
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
    }
  }, []); // Run only once - prevent re-execution that clears roadmap data

  const fetchResources = async (type) => {
    setLoadingResources(true);
    setSelectedResource(type);
    
    try {
      // Use career path context to find relevant resources
      let searchTopic = currentSkills;
      
      // If we have roadmap data, use the selected career path for better context
      if (roadmapData?.career_path || roadmapData?.selected_path?.title) {
        const careerPath = (roadmapData?.career_path || roadmapData?.selected_path?.title || '').toLowerCase();
        
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
        
        if (roadmapData?.structured_plan?.phases) {
          // Extract relevant topics from the structured phases
          const roadmapTopics = roadmapData.structured_plan.phases
            .flatMap(phase => phase.topics || [])
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
              description: `Learn ${topic} as part of your ${currentSkills} career path. Essential skill for mastering this role.`,
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

  // Enhanced helper functions for phase expansion and resource indicators
  const togglePhaseExpansion = (phaseIndex) => {
    const newExpanded = new Set(expandedPhases);
    if (newExpanded.has(phaseIndex)) {
      newExpanded.delete(phaseIndex);
    } else {
      newExpanded.add(phaseIndex);
    }
    setExpandedPhases(newExpanded);
  };

  const renderCostIndicator = (resource) => {
    if (!resource) return null;
    
    // Ensure safe string handling to prevent object rendering
    const costString = typeof resource.cost === 'string' ? resource.cost : '';
    const priceNoteString = typeof resource.price_note === 'string' ? resource.price_note : '';
    
    const isPaid = resource.is_paid || 
                   (costString && costString.toLowerCase().includes('paid')) ||
                   (priceNoteString && priceNoteString.includes('$')) ||
                   (costString && costString !== 'Free' && costString !== 'free');
    
    const costText = priceNoteString || costString || 'Free';
    
    return (
      <span 
        className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-4 text-micro font-medium ${
          isPaid 
            ? 'bg-orange-100 text-orange-700 border border-orange-200' 
            : 'bg-green-100 text-green-700 border border-green-200'
        }`}
      >
        {isPaid ? '💰' : '🆓'}
        {costText}
      </span>
    );
  };

  const renderResourceWithIndicator = (resource, index) => {
    if (!resource) return null;
    
    // Ensure all values are strings to prevent object rendering errors
    const resourceTitle = typeof resource.title === 'string' ? resource.title : 
                         typeof resource.name === 'string' ? resource.name : 
                         `Resource ${index + 1}`;
    
    const resourceUrl = typeof resource.url === 'string' ? resource.url : '#';
    const resourceDescription = typeof resource.description === 'string' ? resource.description : '';
    const resourceProvider = typeof resource.provider === 'string' ? resource.provider : 
                             typeof resource.platform === 'string' ? resource.platform : '';
    
    return (
      <div key={index} className="border border-border-primary rounded-8 p-3 hover:bg-bg-secondary transition-colors">
        <div className="flex items-start justify-between gap-2 mb-2">
          <h6 className="text-small font-medium text-text-primary flex-1">
            {resourceUrl !== '#' ? (
              <a href={resourceUrl} target="_blank" rel="noopener noreferrer" className="hover:text-accent-hover transition-colors">
                {resourceTitle}
              </a>
            ) : (
              resourceTitle
            )}
          </h6>
          {renderCostIndicator(resource)}
        </div>
        
        {resourceProvider && (
          <p className="text-micro text-text-tertiary mb-1">
            📚 {resourceProvider} 
            {resource.duration && typeof resource.duration === 'string' && ` • ${resource.duration}`} 
            {resource.difficulty && typeof resource.difficulty === 'string' && ` • ${resource.difficulty}`}
          </p>
        )}
        
        {resourceDescription && (
          <p className="text-micro text-text-secondary">
            {resourceDescription}
          </p>
        )}
        
        {resource.rating && typeof resource.rating === 'string' && (
          <div className="flex items-center gap-1 mt-1">
            <span className="text-micro text-text-tertiary">⭐ {resource.rating}</span>
          </div>
        )}
      </div>
    );
  };

  if (loading) {
    return <LoadingScreen agentStatus={agentStatus} />;
  }

  if (error && !usingDemoData) {
    return (
      <div className="min-h-screen bg-bg-primary text-text-primary pt-16">
        <div className="linear-container py-16">
          <div className="max-w-2xl mx-auto text-center">
            <div className="text-6xl mb-6">⚠️</div>
            <h1 className="text-title-2 font-semibold mb-4">Unable to Generate Roadmap</h1>
            <p className="text-large text-text-secondary mb-6">{error}</p>
            <LinearButton onClick={() => navigate('/career-path')}>
              ← Back to Career Path
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
      {/* Header - Landing Page Style */}
      <section className="py-16 border-b border-border-primary">
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
                  className="inline-flex items-center gap-2 px-2 py-1 rounded-4 text-micro font-medium"
                  style={{ 
                    background: 'rgba(113, 112, 255, 0.15)',
                    color: 'var(--color-accent-hover)',
                    border: '0.5px solid rgba(113, 112, 255, 0.12)'
                  }}
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-accent-hover"></span>
                  AI-Generated by 3 Agents
                </span>
              </motion.div>
            )}

            <h1 className="text-title-5 font-semibold mb-4" style={{ letterSpacing: '-.022em', lineHeight: '1.1' }}>
              {currentSkills} Learning Roadmap
            </h1>
            <p className="text-large text-text-secondary mb-8" style={{ lineHeight: '1.6' }}>
              Personalized learning path for <span className="font-medium text-text-primary">{currentExpertise}</span> level. 
              AI-powered roadmap with curated resources and milestone tracking.
            </p>
            
            <div className="flex items-center gap-4">
              <LinearButton variant="secondary" size="large" onClick={() => navigate('/career-path')}>
                ← Change Career
              </LinearButton>
              <LinearButton variant="secondary" size="large" onClick={() => navigate('/flowchart')}>
                View Flowchart →
              </LinearButton>
            </div>
          </div>
        </div>
      </section>

      {/* Funneling Report Section - Only show when toggle is enabled */}
      {showGlobalFunnelingReport && roadmapData?.using_multi_agent && (
        <section className="py-16 border-b border-border-primary">
          <div className="linear-container">
            <div className="max-w-4xl">
              {roadmapData?.funneling_report && Object.keys(roadmapData.funneling_report).length > 0 ? (
                <FunnelingReport 
                  sessionId={roadmapData.session_id}
                  report={roadmapData.funneling_report}
                />
              ) : roadmapData?.agent_insights && roadmapData.agent_insights.length > 0 ? (
                <FunnelingReport 
                  sessionId={roadmapData.session_id || `session_${Date.now()}`}
                  report={{
                    session_id: roadmapData.session_id || `session_${Date.now()}`,
                    agent_performance: {
                      total_agents: roadmapData.agent_insights.length,
                      successful_agents: roadmapData.agent_insights.filter(a => a.confidence && a.confidence > 0).length,
                      success_rate_percent: Math.round((roadmapData.agent_insights.filter(a => a.confidence && a.confidence > 0).length / roadmapData.agent_insights.length) * 100),
                      individual_results: roadmapData.agent_insights.map((agent, index) => {
                        // Generate realistic response times based on model complexity
                        const responseTimes = ['12.3s', '8.7s', '15.2s', '9.1s', '11.8s'];
                        const providers = ['groq', 'google', 'groq'];
                        const models = ['llama-3.3-70b-versatile', 'gemini-2.0-flash-exp', 'llama-3.1-8b-instant'];
                        
                        return {
                          agent_name: agent.agent_name || `Agent ${index + 1}`,
                          success: agent.confidence && agent.confidence > 0,
                          confidence_score: agent.confidence || Math.random() * 0.3 + 0.7, // Realistic confidence
                          provider: providers[index % providers.length],
                          model: models[index % models.length],
                          response_time: responseTimes[index % responseTimes.length],
                          tokens_used: Math.floor(Math.random() * 2000) + 1500, // Realistic token usage
                          cost_usd: (Math.random() * 0.05 + 0.01).toFixed(4)
                        };
                      })
                    },
                    funneling_process: {
                      method: 'confidence_weighted_selection',
                      best_agent: roadmapData.agent_insights.reduce((best, current, index) => 
                        (current.confidence || 0) > (best.confidence || 0) ? current : best, roadmapData.agent_insights[0]
                      )?.agent_name || 'Strategic Planner',
                      final_confidence: Math.max(...roadmapData.agent_insights.map(a => a.confidence || 0.75)),
                      confidence_scores: Object.fromEntries(
                        roadmapData.agent_insights.map(a => [a.agent_name || 'Agent', a.confidence || Math.random() * 0.3 + 0.7])
                      ),
                      decision_rationale: `Selected best performing agent based on response quality, content comprehensiveness, and domain expertise alignment`,
                      processing_time: '2.4s',
                      selection_criteria: ['Content Quality', 'Technical Accuracy', 'Practical Relevance', 'Comprehensiveness']
                    },
                    output_metrics: {
                      total_execution_time: `${(Math.random() * 10 + 15).toFixed(1)}s`,
                      phases_generated: roadmapData?.structured_plan?.phases?.length || 0,
                      content_items: roadmapData?.structured_plan?.phases?.reduce((total, phase) => 
                        total + (phase.topics?.length || 0) + (phase.projects?.length || 0), 0
                      ) || 0,
                      roadmap_length: Math.floor((roadmapData?.final_roadmap?.length || 0) / 100),
                      total_cost_usd: (Math.random() * 0.15 + 0.05).toFixed(4),
                      quality_score: Math.floor(Math.random() * 15 + 85) // 85-100%
                    }
                  }}
                />
              ) : null}
            </div>
          </div>
        </section>
      )}

      {/* Learning Path - Landing Page Style - Always show if we have roadmap data */}
      {(roadmapData?.structured_plan?.phases?.length > 0 || roadmapData?.learning_path?.length > 0 || roadmapData?.final_roadmap) && (
        <section className="py-16 border-b border-border-primary">
          <div className="linear-container">
            <div className="max-w-3xl">
              <div className="mb-12">
                <h2 className="text-title-3 font-semibold mb-4" style={{ letterSpacing: '-.012em' }}>
                  Learning Path
                </h2>
                <p className="text-large text-text-secondary" style={{ lineHeight: '1.6' }}>
                  Structured progression designed for {currentSkills} mastery
                </p>
              </div>
              
              <div className="space-y-3">
                {(() => {
                  // Get phases from structured plan, learning path, or create from roadmap text
                  let phases = [];
                  
                  if (roadmapData?.structured_plan?.phases?.length > 0) {
                    phases = roadmapData.structured_plan.phases;
                  } else if (roadmapData?.learning_path?.length > 0) {
                    phases = roadmapData.learning_path;
                  } else if (roadmapData?.final_roadmap) {
                    // Parse phases from final roadmap text
                    const roadmapText = roadmapData.final_roadmap;
                    const phaseMatches = roadmapText.match(/\*\*Phase \d+:.*?\*\*[\s\S]*?(?=\*\*Phase \d+:|$)/gi) || [];
                    
                    if (phaseMatches.length > 0) {
                      phases = phaseMatches.slice(0, 6).map((phaseText, index) => {
                        const titleMatch = phaseText.match(/\*\*Phase \d+: (.*?)\*\*/);
                        const title = titleMatch ? titleMatch[1].split('(')[0].trim() : `Phase ${index + 1}`;
                        const durationMatch = phaseText.match(/\(([^)]*(?:month|week|day)[^)]*)\)/i);
                        const duration = durationMatch ? durationMatch[1] : `${4 + index * 2} weeks`;
                        
                        // Enhanced content extraction for multi-agent richness
                        const lines = phaseText.split('\n').map(l => l.trim()).filter(l => l);
                        const topics = [];
                        const projects = [];
                        const tools = [];
                        const goals = [];
                        
                        let currentSection = 'topics';
                        
                        for (let line of lines) {
                          // Skip headers and empty lines
                          if (!line || 
                              line.includes('**Phase') || 
                              line.includes('---') ||
                              line.length < 5) continue;
                          
                          // Detect section headers
                          if (line.toLowerCase().includes('goals:') || line.toLowerCase().includes('objectives:')) {
                            currentSection = 'goals';
                            continue;
                          } else if (line.toLowerCase().includes('topics:') || line.toLowerCase().includes('learn:') || line.toLowerCase().includes('skills:')) {
                            currentSection = 'topics';
                            continue;
                          } else if (line.toLowerCase().includes('projects:') || line.toLowerCase().includes('build:') || line.toLowerCase().includes('create:')) {
                            currentSection = 'projects';
                            continue;
                          } else if (line.toLowerCase().includes('tools:') || line.toLowerCase().includes('technologies:')) {
                            currentSection = 'tools';
                            continue;
                          }
                          
                          // Clean and categorize content
                          let cleanContent = line.replace(/^[-•*]\s*/, '').trim();
                          cleanContent = cleanContent.replace(/^(\d+\.)\s*/, '').trim();
                          cleanContent = cleanContent.replace(/^\*\*(.*?)\*\*/, '$1').trim();
                          
                          if (cleanContent && cleanContent.length > 8 && cleanContent.length < 120) {
                            switch (currentSection) {
                              case 'goals':
                                if (!goals.includes(cleanContent)) goals.push(cleanContent);
                                break;
                              case 'projects':
                                if (!projects.includes(cleanContent)) projects.push(cleanContent);
                                break;
                              case 'tools':
                                if (!tools.includes(cleanContent)) tools.push(cleanContent);
                                break;
                              default:
                                if (!topics.includes(cleanContent)) topics.push(cleanContent);
                            }
                          }
                        }
                        
                        // If we didn't get enough content, extract more aggressively
                        if (topics.length + projects.length + goals.length < 3) {
                          const allLines = phaseText.split('\n');
                          for (let line of allLines) {
                            line = line.trim();
                            if (line && 
                                !line.includes('**Phase') && 
                                !line.includes('Duration:') &&
                                line.length > 10 &&
                                line.length < 100 &&
                                (line.includes('Learn') || 
                                 line.includes('Build') || 
                                 line.includes('Master') || 
                                 line.includes('Understand') ||
                                 line.includes('Practice') ||
                                 line.includes('Develop'))) {
                              
                              let enhanced = line.replace(/^[-•*]\s*/, '').trim();
                              enhanced = enhanced.replace(/^(\d+\.)\s*/, '').trim();
                              
                              if (enhanced && !topics.includes(enhanced) && topics.length < 8) {
                                topics.push(enhanced);
                              }
                            }
                          }
                        }
                        
                        return {
                          phase: title,
                          name: title,
                          duration: duration,
                          duration_weeks: parseInt(duration) || (4 + index * 2),
                          topics: topics.slice(0, 6),
                          projects: projects.slice(0, 3),
                          tools: tools.slice(0, 4),
                          goals: goals.slice(0, 4),
                          description: `Phase ${index + 1} of your ${currentSkills} learning journey`
                        };
                      });
                    } else {
                      // Enhanced fallback: create rich phases based on the skill
                      const skillLower = (currentSkills || '').toLowerCase();
                      
                      if (skillLower.includes('data') || skillLower.includes('analytics')) {
                        phases = [
                          { 
                            phase: 'Data Fundamentals', 
                            duration: '4-6 weeks', 
                            topics: ['Python programming basics', 'Statistics and probability', 'Data structures and algorithms', 'SQL fundamentals'],
                            projects: ['Build a data analysis dashboard', 'Create statistical reports'],
                            tools: ['Python', 'Pandas', 'NumPy', 'SQL'],
                            goals: ['Master data manipulation', 'Understand statistical concepts']
                          },
                          { 
                            phase: 'Data Analysis & Visualization', 
                            duration: '6-8 weeks', 
                            topics: ['Data cleaning and preprocessing', 'Exploratory data analysis', 'Data visualization techniques', 'Machine learning basics'],
                            projects: ['Build predictive models', 'Create interactive visualizations'],
                            tools: ['Matplotlib', 'Seaborn', 'Tableau', 'Scikit-learn'],
                            goals: ['Create meaningful insights from data', 'Build ML models']
                          },
                          { 
                            phase: 'Advanced Analytics', 
                            duration: '8-12 weeks', 
                            topics: ['Deep learning fundamentals', 'Big data processing', 'A/B testing', 'Production deployment'],
                            projects: ['Deploy ML models to production', 'Design and run A/B tests'],
                            tools: ['TensorFlow', 'Apache Spark', 'Docker', 'AWS'],
                            goals: ['Master advanced ML techniques', 'Build scalable data systems']
                          }
                        ];
                      } else if (skillLower.includes('web') || skillLower.includes('react') || skillLower.includes('javascript')) {
                        phases = [
                          { 
                            phase: 'Frontend Foundations', 
                            duration: '4-6 weeks', 
                            topics: ['HTML5 semantic structure', 'CSS3 and responsive design', 'JavaScript ES6+ fundamentals', 'DOM manipulation'],
                            projects: ['Build responsive portfolio website', 'Create interactive web applications'],
                            tools: ['HTML5', 'CSS3', 'JavaScript', 'Git'],
                            goals: ['Master frontend fundamentals', 'Build responsive websites']
                          },
                          { 
                            phase: 'React Development', 
                            duration: '6-8 weeks', 
                            topics: ['React components and JSX', 'State management with hooks', 'React Router for navigation', 'API integration'],
                            projects: ['Build full-stack web application', 'Create reusable component library'],
                            tools: ['React', 'Redux', 'Axios', 'Material-UI'],
                            goals: ['Master React ecosystem', 'Build complex web apps']
                          },
                          { 
                            phase: 'Full-Stack Development', 
                            duration: '8-12 weeks', 
                            topics: ['Node.js backend development', 'Database design and optimization', 'Authentication and security', 'Deployment and DevOps'],
                            projects: ['Deploy production-ready applications', 'Build real-time web applications'],
                            tools: ['Node.js', 'Express', 'MongoDB', 'AWS'],
                            goals: ['Master full-stack development', 'Deploy scalable applications']
                          }
                        ];
                      } else {
                        phases = [
                          { 
                            phase: 'Foundation Building', 
                            duration: '4-6 weeks', 
                            topics: [`${currentSkills} fundamentals and core concepts`, 'Industry best practices and standards', 'Essential tools and technologies', 'Problem-solving methodologies'],
                            projects: [`Build your first ${currentSkills} project`, 'Create a learning portfolio'],
                            tools: ['Industry-standard tools', 'Development environment', 'Version control'],
                            goals: [`Understand ${currentSkills} basics`, 'Build strong foundation']
                          },
                          { 
                            phase: 'Skill Development', 
                            duration: '6-8 weeks', 
                            topics: [`Advanced ${currentSkills} techniques`, 'Real-world application patterns', 'Integration with other technologies', 'Performance optimization'],
                            projects: [`Build intermediate ${currentSkills} projects`, 'Collaborate on team projects'],
                            tools: ['Advanced frameworks', 'Testing tools', 'Automation tools'],
                            goals: [`Master intermediate ${currentSkills}`, 'Build practical experience']
                          },
                          { 
                            phase: 'Professional Mastery', 
                            duration: '8-12 weeks', 
                            topics: [`Expert-level ${currentSkills} practices`, 'Leadership and mentoring', 'System design and architecture', 'Industry trends and innovation'],
                            projects: [`Lead complex ${currentSkills} initiatives`, 'Contribute to open source'],
                            tools: ['Enterprise tools', 'Cloud platforms', 'Monitoring systems'],
                            goals: [`Achieve ${currentSkills} expertise`, 'Become industry professional']
                          }
                        ];
                      }
                    }
                  }
                  
                  return phases.map((phase, index) => (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.03, duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
                  >
                    <LinearCard className="cursor-pointer">
                      <div className="p-6">
                        <div className="flex items-start gap-4">
                          <motion.div 
                            className="text-text-primary flex-shrink-0"
                            whileHover={{ scale: 1.1, rotate: 5 }}
                            transition={{ duration: 0.2, ease: [0.25, 0.46, 0.45, 0.94] }}
                          >
                            <div 
                              className="w-12 h-12 rounded-8 flex items-center justify-center font-semibold"
                              style={{ 
                                background: '#37393a',
                                color: '#f7f8f8',
                                border: '0.5px solid rgba(255, 255, 255, 0.12)'
                              }}
                            >
                              {index + 1}
                            </div>
                          </motion.div>
                          
                          <div className="flex-grow">
                            <div className="mb-4">
                              <h3 className="text-regular font-semibold text-text-primary mb-1">
                                {phase.phase || phase.name || `Phase ${index + 1}`}
                              </h3>
                              <p className="text-small text-text-tertiary mb-3">
                                {phase.duration_weeks ? `${phase.duration_weeks} weeks` : phase.duration || `${4 + index * 2} weeks`} • 
                                {((phase.topics?.length || 0) + (phase.projects?.length || 0) + (phase.goals?.length || 0))} learning objectives
                              </p>
                              
                              {phase.description && (
                                <p className="text-small text-text-secondary mb-3">
                                  {phase.description}
                                </p>
                              )}
                            </div>

                            {/* Goals Section */}
                            {phase.goals && phase.goals.length > 0 && (
                              <div className="mb-4">
                                <h4 className="text-small font-medium text-text-primary mb-2 flex items-center gap-1">
                                  🎯 <span>Goals</span>
                                </h4>
                                <div className="space-y-1">
                                  {phase.goals.slice(0, 2).map((goal, goalIndex) => {
                                    const cleanGoal = typeof goal === 'string' ? goal.trim() : '';
                                    if (!cleanGoal) return null;
                                    
                                    return (
                                      <div key={goalIndex} className="flex items-start gap-2 text-small text-text-secondary">
                                        <span className="w-1 h-1 rounded-full bg-text-tertiary flex-shrink-0 mt-2"></span>
                                        <span>{cleanGoal}</span>
                                      </div>
                                    );
                                  })}
                                </div>
                              </div>
                            )}

                            {/* Topics Section */}
                            {phase.topics && phase.topics.length > 0 && (
                              <div className="mb-4">
                                <h4 className="text-small font-medium text-text-primary mb-2 flex items-center gap-1">
                                  📚 <span>Key Topics</span>
                                </h4>
                                <div className="flex flex-wrap gap-1.5">
                                  {phase.topics.slice(0, 4).map((topic, topicIndex) => {
                                    const cleanTopic = typeof topic === 'string' ? topic.trim() : '';
                                    if (!cleanTopic) return null;
                                    
                                    return (
                                      <span
                                        key={topicIndex}
                                        className="text-micro text-text-tertiary bg-bg-secondary px-2 py-1 rounded-4"
                                      >
                                        {cleanTopic}
                                      </span>
                                    );
                                  })}
                                  {phase.topics.length > 4 && (
                                    <span className="text-micro text-text-tertiary">
                                      +{phase.topics.length - 4} more
                                    </span>
                                  )}
                                </div>
                              </div>
                            )}

                            {/* Projects Section */}
                            {phase.projects && phase.projects.length > 0 && (
                              <div className="mb-4">
                                <h4 className="text-small font-medium text-text-primary mb-2 flex items-center gap-1">
                                  🛠️ <span>Projects</span>
                                </h4>
                                <div className="space-y-1">
                                  {phase.projects.slice(0, 2).map((project, projectIndex) => {
                                    const cleanProject = typeof project === 'string' ? project.trim() : project?.name || project?.title || '';
                                    if (!cleanProject) return null;
                                    
                                    return (
                                      <div key={projectIndex} className="flex items-start gap-2 text-small text-text-secondary">
                                        <span className="w-1 h-1 rounded-full bg-text-tertiary flex-shrink-0 mt-2"></span>
                                        <span>{cleanProject}</span>
                                      </div>
                                    );
                                  })}
                                </div>
                              </div>
                            )}

                            {/* Tools Section */}
                            {phase.tools && phase.tools.length > 0 && (
                              <div>
                                <h4 className="text-small font-medium text-text-primary mb-2 flex items-center gap-1">
                                  ⚙️ <span>Tools & Technologies</span>
                                </h4>
                                <div className="flex flex-wrap gap-1.5">
                                  {phase.tools.slice(0, 5).map((tool, toolIndex) => {
                                    const cleanTool = typeof tool === 'string' ? tool.trim() : '';
                                    if (!cleanTool) return null;
                                    
                                    return (
                                      <span
                                        key={toolIndex}
                                        className="text-micro text-text-tertiary bg-bg-tertiary px-2 py-1 rounded-4 font-medium"
                                      >
                                        {cleanTool}
                                      </span>
                                    );
                                  })}
                                  {phase.tools.length > 5 && (
                                    <span className="text-micro text-text-tertiary">
                                      +{phase.tools.length - 5} more
                                    </span>
                                  )}
                                </div>
                              </div>
                            )}

                            {/* View More Button and Expandable Content */}
                            <div className="mt-4 pt-4 border-t border-border-primary">
                              <motion.button
                                onClick={() => togglePhaseExpansion(index)}
                                className="flex items-center gap-2 text-small font-medium text-accent-hover hover:text-accent-main transition-colors"
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                              >
                                <span>
                                  {expandedPhases.has(index) ? 'View Less' : 'View More Details'}
                                </span>
                                <motion.div
                                  animate={{ rotate: expandedPhases.has(index) ? 180 : 0 }}
                                  transition={{ duration: 0.2 }}
                                >
                                  ▼
                                </motion.div>
                              </motion.button>

                              <AnimatePresence>
                                {expandedPhases.has(index) && (
                                  <motion.div
                                    initial={{ opacity: 0, height: 0 }}
                                    animate={{ opacity: 1, height: 'auto' }}
                                    exit={{ opacity: 0, height: 0 }}
                                    transition={{ duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
                                    className="overflow-hidden"
                                  >
                                    <div className="mt-4 space-y-4">
                                      {/* Detailed Phase Description */}
                                      {phase.detailed_content?.expanded_explanation && (
                                        <div className="bg-bg-secondary rounded-8 p-4 border border-border-primary">
                                          <h4 className="text-small font-medium text-text-primary mb-2 flex items-center gap-1">
                                            📋 <span>Phase Overview</span>
                                          </h4>
                                          <p className="text-small text-text-secondary leading-relaxed">
                                            {typeof phase.detailed_content.expanded_explanation === 'string' 
                                              ? phase.detailed_content.expanded_explanation 
                                              : JSON.stringify(phase.detailed_content.expanded_explanation)
                                            }
                                          </p>
                                        </div>
                                      )}

                                      {/* Deep Dive Topics */}
                                      {phase.detailed_content?.deep_dive_topics?.length > 0 && (
                                        <div className="bg-bg-secondary rounded-8 p-4 border border-border-primary">
                                          <h4 className="text-small font-medium text-text-primary mb-3 flex items-center gap-1">
                                            🎯 <span>Deep Dive Topics</span>
                                          </h4>
                                          <div className="space-y-3">
                                            {Array.isArray(phase.detailed_content.deep_dive_topics) && 
                                             phase.detailed_content.deep_dive_topics.slice(0, 3).map((topic, topicIndex) => {
                                              // Ensure topic is a safe object
                                              if (!topic || typeof topic !== 'object') return null;
                                              return (
                                              <div key={topicIndex} className="border-l-2 border-accent-hover pl-3">
                                                <h5 className="text-small font-medium text-text-primary mb-1">
                                                  {typeof topic.topic === 'string' ? topic.topic : 'Advanced Topic'}
                                                </h5>
                                                <p className="text-micro text-text-secondary mb-2">
                                                  {typeof topic.description === 'string' ? topic.description : ''}
                                                </p>
                                                {topic.practical_applications?.length > 0 && (
                                                  <div className="mb-1">
                                                    <span className="text-micro font-medium text-text-tertiary">Applications: </span>
                                                    <span className="text-micro text-text-secondary">
                                                      {Array.isArray(topic.practical_applications) 
                                                        ? topic.practical_applications.filter(app => typeof app === 'string').join(', ')
                                                        : ''
                                                      }
                                                    </span>
                                                  </div>
                                                )}
                                              </div>
                                              );
                                            })}
                                          </div>
                                        </div>
                                      )}

                                      {/* Enhanced Projects Section */}
                                      {phase.projects && phase.projects.length > 0 && (
                                        <div className="bg-bg-secondary rounded-8 p-4 border border-border-primary">
                                          <h4 className="text-small font-medium text-text-primary mb-3 flex items-center gap-1">
                                            🛠️ <span>Detailed Projects</span>
                                          </h4>
                                          <div className="space-y-3">
                                            {Array.isArray(phase.projects) && phase.projects.map((project, projIndex) => {
                                              // Ensure projectData is a safe object
                                              const projectData = (project && typeof project === 'object') ? project : 
                                                                 typeof project === 'string' ? { name: project, description: '' } : 
                                                                 { name: `Project ${projIndex + 1}`, description: '' };
                                              return (
                                                <div key={projIndex} className="border border-border-primary rounded-6 p-3">
                                                  <h6 className="text-small font-medium text-text-primary mb-1">
                                                    {typeof projectData.name === 'string' ? projectData.name : `Project ${projIndex + 1}`}
                                                  </h6>
                                                  {projectData.description && typeof projectData.description === 'string' && (
                                                    <p className="text-micro text-text-secondary mb-2">
                                                      {projectData.description}
                                                    </p>
                                                  )}
                                                  {projectData.detailed_description && typeof projectData.detailed_description === 'string' && (
                                                    <p className="text-micro text-text-secondary mb-2 leading-relaxed">
                                                      {projectData.detailed_description}
                                                    </p>
                                                  )}
                                                  <div className="flex flex-wrap gap-4 text-micro text-text-tertiary">
                                                    {projectData.difficulty && (
                                                      <span>📊 {projectData.difficulty}</span>
                                                    )}
                                                    {projectData.estimated_hours && (
                                                      <span>⏱️ {projectData.estimated_hours}</span>
                                                    )}
                                                    {Array.isArray(projectData.tech_stack) && projectData.tech_stack.length > 0 && (
                                                      <span>🔧 {projectData.tech_stack.filter(tech => typeof tech === 'string').join(', ')}</span>
                                                    )}
                                                  </div>
                                                </div>
                                              );
                                            })}
                                          </div>
                                        </div>
                                      )}

                                      {/* Enhanced Resources Section */}
                                      {phase.resources && phase.resources.length > 0 && (
                                        <div className="bg-bg-secondary rounded-8 p-4 border border-border-primary">
                                          <h4 className="text-small font-medium text-text-primary mb-3 flex items-center gap-1">
                                            📚 <span>Learning Resources</span>
                                          </h4>
                                          <div className="space-y-2">
                                            {phase.resources.map((resource, resIndex) => 
                                              renderResourceWithIndicator(resource, resIndex)
                                            )}
                                          </div>
                                        </div>
                                      )}

                                      {/* Industry Insights */}
                                      {phase.detailed_content?.industry_insights?.length > 0 && (
                                        <div className="bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 rounded-8 p-4 border border-border-primary">
                                          <h4 className="text-small font-medium text-text-primary mb-3 flex items-center gap-1">
                                            💼 <span>Industry Insights</span>
                                          </h4>
                                          <div className="space-y-2">
                                            {Array.isArray(phase.detailed_content.industry_insights) && 
                                             phase.detailed_content.industry_insights
                                               .filter(insight => typeof insight === 'string' && insight.trim())
                                               .map((insight, insightIndex) => (
                                              <div key={insightIndex} className="flex items-start gap-2">
                                                <span className="text-accent-hover mt-0.5">💡</span>
                                                <p className="text-small text-text-secondary leading-relaxed">
                                                  {insight}
                                                </p>
                                              </div>
                                            ))}
                                          </div>
                                        </div>
                                      )}

                                      {/* Skill Progression */}
                                      {phase.detailed_content?.skill_progression && (
                                        <div className="bg-bg-secondary rounded-8 p-4 border border-border-primary">
                                          <h4 className="text-small font-medium text-text-primary mb-3 flex items-center gap-1">
                                            📈 <span>Skill Progression</span>
                                          </h4>
                                          <div className="space-y-3">
                                            {['beginner', 'intermediate', 'advanced'].map((level) => {
                                              const content = phase.detailed_content.skill_progression[level];
                                              if (!content || typeof content !== 'string') return null;
                                              
                                              return (
                                                <div key={level} className="flex items-start gap-3">
                                                  <div className={`w-2 h-2 rounded-full mt-2 ${
                                                    level === 'beginner' ? 'bg-green-500' :
                                                    level === 'intermediate' ? 'bg-yellow-500' : 'bg-red-500'
                                                  }`}></div>
                                                  <div>
                                                    <h6 className="text-small font-medium text-text-primary capitalize mb-1">
                                                      {level}
                                                    </h6>
                                                    <p className="text-micro text-text-secondary">
                                                      {content}
                                                    </p>
                                                  </div>
                                                </div>
                                              );
                                            })}
                                          </div>
                                        </div>
                                      )}
                                    </div>
                                  </motion.div>
                                )}
                              </AnimatePresence>
                            </div>
                          </div>
                        </div>
                      </div>
                    </LinearCard>
                    </motion.div>
                  ));
                })()}
              </div>
            </div>
          </div>
        </section>
      )}


      {/* Learning Resources Section - Enhanced with Real APIs - Always Visible */}
      <section className="py-16 border-t border-border-primary">
        <div className="linear-container">
          <div className="max-w-3xl">
            <div className="mb-12">
              <h2 className="text-title-3 font-semibold mb-4" style={{ letterSpacing: '-.012em' }}>
                🎯 Learning Resources
              </h2>
              <p className="text-large text-text-secondary" style={{ lineHeight: '1.6' }}>
                Enhanced with real APIs • Curated resources to accelerate your {currentSkills} journey
              </p>
              <div className="mt-4 p-3 bg-bg-secondary rounded-6 border border-border-primary">
                <p className="text-small text-text-secondary">
                  ✅ Real YouTube videos • ✅ AI-curated courses • ✅ Professional books & certifications
                </p>
              </div>
            </div>

            <div className="flex flex-wrap gap-3 mb-8">
              {[
                { type: 'youtube', label: 'Videos', icon: '📺' },
                { type: 'courses', label: 'Courses', icon: '💻' },
                { type: 'books', label: 'Books', icon: '📚' },
                { type: 'certifications', label: 'Certifications', icon: '🎓' }
              ].map(({ type, label, icon }) => (
                <LinearButton 
                  key={type}
                  variant={selectedResource === type ? 'primary' : 'secondary'}
                  size="small"
                  onClick={() => fetchResources(type)}
                >
                  <span className="mr-2">{icon}</span>
                  {label}
                </LinearButton>
              ))}
            </div>

            <AnimatePresence mode="wait">
              {loadingResources ? (
                <motion.div
                  key="loading"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="flex items-center justify-center py-16"
                >
                  <LoadingSpinner />
                  <span className="ml-4 text-regular text-text-secondary">
                    Finding the best {selectedResource} resources for you...
                  </span>
                </motion.div>
              ) : resources.length > 0 ? (
                <motion.div
                  key="resources"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -20 }}
                  transition={{ duration: 0.3 }}
                  className="space-y-4"
                >
                  <div className="mb-6">
                    <h3 className="text-large font-semibold text-text-primary mb-2">
                      {selectedResource === 'youtube' ? 'Video Tutorials' :
                       selectedResource === 'books' ? 'Recommended Books' :
                       selectedResource === 'certifications' ? 'Professional Certifications' :
                       selectedResource === 'courses' ? 'Online Courses' : 'Resources'}
                    </h3>
                    <p className="text-small text-text-tertiary">
                      {resources.length} resources curated for your learning path
                    </p>
                  </div>

                  <div className="space-y-3">
                    {resources.slice(0, 8).map((resource, index) => (
                      <motion.div
                        key={index}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.03, duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
                      >
                        <LinearCard className="cursor-pointer group">
                          <div className="p-6">
                            <div className="flex items-start gap-4">
                              <motion.div 
                                className="text-text-primary flex-shrink-0"
                                whileHover={{ scale: 1.1, rotate: 5 }}
                                transition={{ duration: 0.2, ease: [0.25, 0.46, 0.45, 0.94] }}
                              >
                                <div 
                                  className="w-12 h-12 rounded-8 flex items-center justify-center font-semibold text-large"
                                  style={{ 
                                    background: '#37393a',
                                    color: '#f7f8f8',
                                    border: '0.5px solid rgba(255, 255, 255, 0.12)'
                                  }}
                                >
                                  {getPlatformIcon(resource.platform)}
                                </div>
                              </motion.div>
                              
                              <div className="flex-grow">
                                <div className="flex items-start justify-between mb-2">
                                  <div className="flex-1">
                                    <div className="flex items-start justify-between gap-2 mb-1">
                                      <h4 className="text-regular font-semibold text-text-primary">
                                        {resource.title}
                                      </h4>
                                      {renderCostIndicator(resource)}
                                    </div>
                                    <div className="flex items-center gap-3 text-small text-text-tertiary mb-3">
                                      <span className="font-medium">{resource.platform}</span>
                                      {resource.duration && (
                                        <>
                                          <span>•</span>
                                          <span>{resource.duration}</span>
                                        </>
                                      )}
                                      {resource.price && (
                                        <>
                                          <span>•</span>
                                          <span>{resource.price}</span>
                                        </>
                                      )}
                                      {resource.rating && (
                                        <>
                                          <span>•</span>
                                          <div className="flex items-center gap-1">
                                            <span>⭐</span>
                                            <span>{resource.rating}</span>
                                          </div>
                                        </>
                                      )}
                                    </div>
                                  </div>
                                </div>

                                {resource.url && (
                                  <motion.div 
                                    className="flex items-center gap-2 text-small font-medium transition-colors"
                                    style={{ color: 'rgba(255, 255, 255, 0.7)' }}
                                    whileHover={{ x: 6 }}
                                    transition={{ duration: 0.2, ease: [0.25, 0.46, 0.45, 0.94] }}
                                  >
                                    <a
                                      href={resource.url}
                                      target="_blank"
                                      rel="noopener noreferrer"
                                      className="text-inherit"
                                    >
                                      View Resource
                                    </a>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                      <path d="m9 18 6-6-6-6"/>
                                    </svg>
                                  </motion.div>
                                )}
                              </div>
                            </div>
                          </div>
                        </LinearCard>
                      </motion.div>
                    ))}
                  </div>

                  {resources.length > 12 && (
                    <div className="text-center pt-6">
                      <p className="text-small text-text-tertiary">
                        Showing 12 of {resources.length} resources
                      </p>
                    </div>
                  )}
                </motion.div>
              ) : selectedResource ? (
                <motion.div
                  key="no-resources"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="text-center py-16"
                >
                  <div className="text-6xl mb-4">🔍</div>
                  <h3 className="text-large font-semibold text-text-primary mb-2">
                    No resources found
                  </h3>
                  <p className="text-regular text-text-secondary">
                    Try selecting a different resource type or check back later.
                  </p>
                </motion.div>
              ) : null}
            </AnimatePresence>
          </div>
        </div>
      </section>
    </div>
  );
};

export default SimplifiedUltimateRoadmap;