import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

// Optimized phase display component with expansion toggles - pre-process data to avoid render delays
const OptimizedPhaseDisplay = ({ phases, currentSkills }) => {
  const [expandedPhases, setExpandedPhases] = useState(new Set());

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
  // Pre-process phases to clean data and avoid render-time filtering
  const processedPhases = React.useMemo(() => {
    if (!phases || phases.length === 0) return [];
    
    return phases.filter(phase => phase && phase.name).map(phase => ({
      ...phase,
      goals: (phase.goals || []).filter(g => g && g.trim() && g.length > 3),
      topics: (phase.topics || []).filter(t => t && t.trim() && t.length > 3),
      tools: (phase.tools || []).filter(t => t && t.trim() && t.length > 3),
      projects: (phase.projects || []).filter(pr => pr && (
        typeof pr === 'string' ? pr.trim() && pr.length > 3 : 
        (pr.name || pr.description)
      )),
      resources: (phase.resources || []).filter(r => r && (
        typeof r === 'string' ? r.trim() && r.length > 3 : 
        (r.title || r.url)
      )),
      checkpoints: (phase.checkpoints || []).filter(c => c && c.trim() && c.length > 3)
    }));
  }, [phases]);

  if (processedPhases.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-regular text-text-secondary">
          No learning phases available. The AI agents are still working on your personalized roadmap.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {processedPhases.map((phase, phaseIdx) => {
        const isExpanded = expandedPhases.has(phaseIdx);
        
        // Key points for collapsed view (3-4 items max)
        const keyItems = [...(phase.goals || []), ...(phase.topics || [])].slice(0, 3);
        const totalItems = (phase.goals || []).length + (phase.topics || []).length + (phase.projects || []).length;
        
        return (
          <motion.div 
            key={phaseIdx} 
            className="bg-bg-secondary border border-border-primary rounded-8 overflow-hidden"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: phaseIdx * 0.1 }}
          >
            {/* Phase Header - Always Visible */}
            <div 
              className="p-6 cursor-pointer hover:bg-bg-tertiary transition-colors"
              onClick={() => togglePhaseExpansion(phaseIdx)}
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-4 mb-3">
                    <div 
                      className="flex-shrink-0 w-10 h-10 rounded-8 flex items-center justify-center font-semibold text-regular"
                      style={{
                        background: 'rgba(255, 255, 255, 0.05)',
                        color: 'var(--color-text-primary)',
                        border: '1px solid rgba(255, 255, 255, 0.1)'
                      }}
                    >
                      {phaseIdx + 1}
                    </div>
                    <div className="flex-1">
                      <h4 className="text-large font-semibold text-text-primary mb-1 hover:text-accent transition-colors">
                        {phase.name}
                      </h4>
                      <div className="flex items-center gap-4 text-small text-text-tertiary">
                        {phase.duration_weeks && (
                          <span className="flex items-center gap-1">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                              <circle cx="12" cy="12" r="10"/>
                              <polyline points="12 6 12 12 16 14"/>
                            </svg>
                            {phase.duration_weeks} weeks
                          </span>
                        )}
                        {!isExpanded && (
                          <span className="text-text-quaternary">
                            {totalItems} items total
                          </span>
                        )}
                      </div>
                    </div>
                    <motion.button
                      className="p-2 rounded-4 bg-bg-primary border border-border-secondary hover:border-border-primary transition-colors"
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

                  {/* Overview Text */}
                  {phase.overview && (
                    <p className="text-small text-text-secondary mb-4 leading-relaxed">
                      {phase.overview}
                    </p>
                  )}

                  {/* Collapsed View - Key Points Only */}
                  {!isExpanded && keyItems.length > 0 && (
                    <div className="space-y-2">
                      {keyItems.map((item, i) => (
                        <motion.div 
                          key={`key-${i}`}
                          className="flex items-center gap-2.5 text-small text-text-secondary"
                          initial={{ opacity: 0, x: -10 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: phaseIdx * 0.1 + i * 0.05 }}
                        >
                          <motion.span 
                            className="w-1.5 h-1.5 rounded-full bg-accent flex-shrink-0"
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ delay: phaseIdx * 0.1 + i * 0.05, type: "spring", stiffness: 500 }}
                          ></motion.span>
                          {item}
                        </motion.div>
                      ))}
                      
                      {totalItems > 3 && (
                        <div className="flex items-center gap-2 text-micro text-text-tertiary mt-3">
                          <span className="w-1.5 h-1.5 rounded-full bg-border-primary flex-shrink-0"></span>
                          Click to see all {totalItems} items + projects & resources
                        </div>
                      )}
                    </div>
                  )}
                </div>
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
                    {phase.goals.length > 0 && (
                      <div>
                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                            <path d="M9 11l3 3L22 4"/>
                          </svg>
                          Learning Goals
                        </h4>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                          {phase.goals.map((goal, i) => (
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
                    {phase.topics.length > 0 && (
                      <div>
                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                          </svg>
                          Key Topics
                        </h4>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                          {phase.topics.map((topic, i) => (
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
                    {phase.projects.length > 0 && (
                      <div>
                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                            <polyline points="9 11 12 14 22 4"/>
                            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
                          </svg>
                          Hands-on Projects
                        </h4>
                        <div className="space-y-3">
                          {phase.projects.map((project, i) => (
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
                    {phase.tools.length > 0 && (
                      <div>
                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                          </svg>
                          Tools & Technologies
                        </h4>
                        <div className="flex flex-wrap gap-2">
                          {phase.tools.map((tool, i) => (
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

                    {/* Resources */}
                    {phase.resources.length > 0 && (
                      <div>
                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                          </svg>
                          Recommended Resources
                        </h4>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                          {phase.resources.map((resource, i) => (
                            <motion.div 
                              key={`resource-${i}`}
                              className="flex items-start gap-2 p-3 rounded-6 bg-bg-secondary border border-border-secondary"
                              initial={{ opacity: 0, x: -10 }}
                              animate={{ opacity: 1, x: 0 }}
                              transition={{ delay: i * 0.05 }}
                            >
                              <span className="w-1.5 h-1.5 rounded-full bg-accent flex-shrink-0 mt-1.5"></span>
                              <span className="text-small text-text-secondary">
                                {typeof resource === 'string' 
                                  ? resource 
                                  : `${resource.title || 'Resource'}${resource.provider ? ` (${resource.provider})` : ''}`
                                }
                              </span>
                            </motion.div>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Checkpoints */}
                    {phase.checkpoints.length > 0 && (
                      <div>
                        <h4 className="text-small font-semibold text-text-primary mb-3 flex items-center gap-2">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-accent">
                            <polyline points="9 11 12 14 22 4"/>
                            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
                          </svg>
                          Phase Completion Checklist
                        </h4>
                        <div className="space-y-2">
                          {phase.checkpoints.map((checkpoint, i) => (
                            <motion.div 
                              key={`checkpoint-${i}`}
                              className="flex items-start gap-2 p-3 rounded-6 bg-bg-secondary border border-border-secondary"
                              initial={{ opacity: 0, x: -10 }}
                              animate={{ opacity: 1, x: 0 }}
                              transition={{ delay: i * 0.05 }}
                            >
                              <span className="w-1.5 h-1.5 rounded-full bg-accent flex-shrink-0 mt-1.5"></span>
                              <span className="text-small text-text-secondary">{checkpoint}</span>
                            </motion.div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </motion.div>
        );
      })}
    </div>
  );
};

export default OptimizedPhaseDisplay;