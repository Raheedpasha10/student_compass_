import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const LoadingScreen = ({ 
  title = "Generating Your Learning Roadmap",
  subtitle = "Our AI agents are crafting a personalized path for your success...",
  agentStatus = null,
  steps = [
    "Analyzing your skills and background",
    "Matching you with optimal career paths", 
    "Building your personalized roadmap",
    "Curating the best resources"
  ]
}) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [progress, setProgress] = useState(0);
  const [agentActivity, setAgentActivity] = useState({});
  const [currentAgentAction, setCurrentAgentAction] = useState({});

  // Realistic agent activities
  const agentActivities = {
    "Strategic Planner": [
      "Analyzing career market trends...",
      "Mapping skill requirements to roles...",
      "Evaluating salary progression paths...",
      "Identifying industry opportunities...",
      "Cross-referencing job demand data...",
      "Optimizing career trajectory..."
    ],
    "Practical Guide": [
      "Curating hands-on projects...",
      "Selecting portfolio-worthy builds...",
      "Matching tools to skill level...",
      "Finding real-world applications...",
      "Sourcing practical tutorials...",
      "Building project roadmaps..."
    ],
    "Technical Expert": [
      "Evaluating technical depth...",
      "Analyzing framework compatibility...",
      "Reviewing industry standards...",
      "Assessing complexity levels...",
      "Validating learning sequences...",
      "Optimizing technical progression..."
    ]
  };

  useEffect(() => {
    const stepInterval = setInterval(() => {
      setCurrentStep(prev => (prev + 1) % steps.length);
    }, 2000);

    const progressInterval = setInterval(() => {
      setProgress(prev => Math.min(prev + 0.8, 95));
    }, 100);

    // Simulate realistic agent activity
    const activityInterval = setInterval(() => {
      if (agentStatus?.agents) {
        const newActivity = {};
        const newActions = {};
        
        agentStatus.agents.forEach(agent => {
          const activities = agentActivities[agent.name] || ["Processing data..."];
          newActivity[agent.name] = Math.random();
          newActions[agent.name] = activities[Math.floor(Math.random() * activities.length)];
        });
        
        setAgentActivity(newActivity);
        setCurrentAgentAction(newActions);
      }
    }, 1500);

    return () => {
      clearInterval(stepInterval);
      clearInterval(progressInterval);
      clearInterval(activityInterval);
    };
  }, [steps.length, agentStatus]);

  return (
    <div className="min-h-screen flex items-center justify-center p-6 bg-bg-primary">
      
      {/* Subtle background pattern */}
      <div 
        className="absolute inset-0 opacity-5"
        style={{
          backgroundImage: 'radial-gradient(circle at 1px 1px, rgba(255,255,255,0.15) 1px, transparent 0)',
          backgroundSize: '20px 20px'
        }}
      />

      <div className="relative z-10 max-w-2xl w-full">
        
        {/* Main loading container */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-bg-secondary border border-border-primary rounded-12 p-8"
          style={{
            boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)'
          }}
        >
          {/* Header Section */}
          <div className="text-center mb-8">
            <motion.div
              initial={{ scale: 0.8 }}
              animate={{ scale: 1 }}
              transition={{ duration: 0.5 }}
              className="mb-4"
            >
              <div className="flex items-center justify-center gap-3 mb-2">
                <motion.div
                  animate={{ rotate: 360 }}
                  transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
                  className="flex-shrink-0"
                >
                  {/* Your Compass Logo - Animated */}
                  <svg 
                    width="28" 
                    height="28" 
                    viewBox="0 0 24 24" 
                    fill="none" 
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className="text-accent-main"
                  >
                    <circle cx="12" cy="12" r="10"/>
                    <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>
                  </svg>
                </motion.div>
                <h1 className="text-title-2 font-semibold text-text-primary">
                  {agentStatus?.current || title}
                </h1>
              </div>
            </motion.div>
            <p className="text-regular text-text-secondary max-w-lg mx-auto">
              {agentStatus?.agents?.length > 0 
                ? `${agentStatus.agents.length} specialized AI agents are working together to create your personalized roadmap`
                : subtitle
              }
            </p>
          </div>

          {/* Multi-Agent Visualization */}
          {agentStatus?.agents && agentStatus.agents.length > 0 ? (
            <div className="mb-8">
              {/* Agent Grid Header */}
              <div className="text-center mb-6">
                <h3 className="text-regular font-semibold text-text-primary mb-2">
                  AI Agents Collaboration
                </h3>
                <p className="text-small text-text-secondary">
                  Watch our specialized agents work together in real-time
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {agentStatus.agents.map((agent, index) => (
                  <motion.div
                    key={agent.name}
                    initial={{ opacity: 0, y: 30, scale: 0.95 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    transition={{ 
                      delay: index * 0.15, 
                      duration: 0.6,
                      ease: [0.25, 0.46, 0.45, 0.94]
                    }}
                    className="relative group"
                  >
                    {/* Card Container with Enhanced Styling */}
                    <div className="bg-bg-tertiary border border-border-primary rounded-12 p-5 relative overflow-hidden
                                    shadow-lg hover:shadow-xl transition-all duration-300
                                    hover:border-accent-main/20 hover:bg-bg-tertiary/80">
                      
                      {/* Animated Background Gradient */}
                      <motion.div
                        animate={{ 
                          opacity: [0.1, 0.2, 0.1],
                          scale: [1, 1.02, 1]
                        }}
                        transition={{ 
                          duration: 3, 
                          repeat: Infinity,
                          delay: index * 0.4
                        }}
                        className="absolute inset-0 bg-gradient-to-br from-accent-main/5 to-accent-hover/5 rounded-12"
                      />

                      {/* Top Activity Bar */}
                      <motion.div
                        animate={{ 
                          scaleX: [0.8, 1, 0.9, 1],
                          opacity: [0.7, 1, 0.8, 1]
                        }}
                        transition={{ 
                          duration: 2.5, 
                          repeat: Infinity,
                          delay: index * 0.3
                        }}
                        className="absolute top-0 left-0 h-1 bg-gradient-to-r from-accent-main via-accent-hover to-accent-main rounded-t-12"
                        style={{ width: `${60 + (agentActivity[agent.name] || 0) * 40}%` }}
                      />

                      {/* Agent Header */}
                      <div className="relative z-10 flex items-center gap-4 mb-4">
                        {/* Enhanced Agent Avatar */}
                        <motion.div
                          animate={{ 
                            scale: [1, 1.15, 1],
                            rotate: [0, 8, -8, 0],
                            boxShadow: [
                              "0 4px 20px rgba(113, 112, 255, 0.2)",
                              "0 8px 30px rgba(113, 112, 255, 0.4)",
                              "0 4px 20px rgba(113, 112, 255, 0.2)"
                            ]
                          }}
                          transition={{ 
                            duration: 2.5, 
                            repeat: Infinity,
                            delay: index * 0.6
                          }}
                          className="w-12 h-12 bg-gradient-to-br from-accent-main to-accent-hover rounded-10 
                                     flex items-center justify-center text-white text-regular font-bold
                                     border border-accent-main/20 relative overflow-hidden"
                        >
                          {/* Avatar Background Pattern */}
                          <div className="absolute inset-0 opacity-20">
                            <div className="absolute inset-1 rounded-8 border border-white/30"></div>
                          </div>
                          
                          <span className="relative z-10">
                            {agent.name.charAt(0)}
                          </span>

                          {/* Pulsing Ring */}
                          <motion.div
                            animate={{ scale: [1, 1.4, 1], opacity: [0.6, 0, 0.6] }}
                            transition={{ duration: 2, repeat: Infinity, delay: index * 0.3 }}
                            className="absolute inset-0 border-2 border-accent-main rounded-10"
                          />
                        </motion.div>

                        <div className="flex-1">
                          <h3 className="text-small font-bold text-text-primary mb-1 tracking-tight">
                            {agent.name}
                          </h3>
                          <div className="flex items-center gap-2">
                            <div className="flex items-center gap-1">
                              <motion.div
                                animate={{ scale: [1, 1.2, 1] }}
                                transition={{ duration: 1.5, repeat: Infinity, delay: index * 0.2 }}
                                className="w-2 h-2 bg-green-500 rounded-full"
                              />
                              <span className="text-micro text-text-tertiary font-medium">
                                {agent.model || 'AI Model'}
                              </span>
                            </div>
                          </div>
                        </div>

                        {/* Enhanced Spinner */}
                        <motion.div
                          animate={{ rotate: 360 }}
                          transition={{ duration: 1.8, repeat: Infinity, ease: "linear" }}
                          className="relative"
                        >
                          <div className="w-6 h-6 border-2 border-accent-main/30 rounded-full border-t-accent-main"></div>
                          <motion.div
                            animate={{ scale: [0.8, 1.1, 0.8] }}
                            transition={{ duration: 1, repeat: Infinity }}
                            className="absolute inset-1 border border-accent-hover/50 rounded-full"
                          />
                        </motion.div>
                      </div>

                      {/* Current Action Display */}
                      <div className="relative z-10 bg-bg-primary/60 backdrop-blur-sm rounded-8 p-3 border border-border-secondary/50 mb-3">
                        <div className="flex items-center gap-2 mb-1">
                          <motion.div
                            animate={{ opacity: [0.4, 1, 0.4] }}
                            transition={{ duration: 1.5, repeat: Infinity }}
                            className="w-1.5 h-1.5 bg-accent-main rounded-full"
                          />
                          <span className="text-micro font-semibold text-text-primary">Processing</span>
                        </div>
                        
                        <AnimatePresence mode="wait">
                          <motion.p
                            key={currentAgentAction[agent.name]}
                            initial={{ opacity: 0, y: 8, scale: 0.95 }}
                            animate={{ opacity: 1, y: 0, scale: 1 }}
                            exit={{ opacity: 0, y: -8, scale: 0.95 }}
                            transition={{ duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
                            className="text-micro text-text-secondary leading-relaxed"
                          >
                            {currentAgentAction[agent.name] || "Initializing agent systems..."}
                          </motion.p>
                        </AnimatePresence>
                      </div>

                      {/* Enhanced Processing Animation */}
                      <div className="relative z-10 flex items-center justify-between">
                        <div className="flex gap-1.5">
                          {[0, 1, 2, 3].map((dot) => (
                            <motion.div
                              key={dot}
                              animate={{ 
                                scale: [1, 1.4, 1],
                                opacity: [0.4, 1, 0.4]
                              }}
                              transition={{
                                duration: 1.2,
                                repeat: Infinity,
                                delay: dot * 0.15 + index * 0.1
                              }}
                              className="w-1.5 h-1.5 bg-accent-main rounded-full"
                            />
                          ))}
                        </div>

                        {/* Agent Status Indicator */}
                        <div className="flex items-center gap-1">
                          <motion.div
                            animate={{ rotate: [0, 360] }}
                            transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                          >
                            ⚡
                          </motion.div>
                          <span className="text-micro font-medium text-accent-main">Active</span>
                        </div>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>
          ) : (
            // Fallback single loading animation
            <div className="flex items-center justify-center gap-4 mb-8">
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                className="w-8 h-8 border-2 border-accent-main border-t-transparent rounded-full"
              />
              <AnimatePresence mode="wait">
                <motion.span
                  key={currentStep}
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="text-regular text-text-primary font-medium"
                >
                  {steps[currentStep]}
                </motion.span>
              </AnimatePresence>
            </div>
          )}

          {/* Enhanced Progress Section */}
          <div className="bg-bg-primary/40 backdrop-blur-sm rounded-12 p-6 border border-border-secondary/50 relative overflow-hidden">
            {/* Background Pattern */}
            <div className="absolute inset-0 opacity-5">
              <div className="absolute inset-2 rounded-8 border border-accent-main/10"></div>
            </div>

            {/* Progress Header */}
            <div className="relative z-10 flex items-center justify-between mb-4">
              <div className="flex items-center gap-3">
                <motion.div
                  animate={{ rotate: [0, 360] }}
                  transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
                  className="w-5 h-5 text-accent-main"
                >
                  ⚙️
                </motion.div>
                <div>
                  <h4 className="text-small font-bold text-text-primary">Generation Progress</h4>
                  <p className="text-micro text-text-secondary">Creating your personalized roadmap</p>
                </div>
              </div>
              
              <motion.div
                animate={{ scale: [1, 1.05, 1] }}
                transition={{ duration: 2, repeat: Infinity }}
                className="bg-accent-main/10 rounded-8 px-3 py-1 border border-accent-main/20"
              >
                <span className="text-small font-bold text-accent-main">{Math.round(progress)}%</span>
              </motion.div>
            </div>

            {/* Enhanced Progress Bar */}
            <div className="relative z-10 mb-4">
              <div className="w-full bg-bg-tertiary rounded-full h-3 overflow-hidden border border-border-primary/30 relative">
                {/* Progress Background Animation */}
                <motion.div
                  animate={{ x: ['-100%', '100%'] }}
                  transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                  className="absolute inset-0 bg-gradient-to-r from-transparent via-accent-main/10 to-transparent"
                />
                
                {/* Main Progress Bar */}
                <motion.div
                  className="h-full bg-gradient-to-r from-accent-main via-accent-hover to-accent-main rounded-full relative overflow-hidden"
                  initial={{ width: 0 }}
                  animate={{ width: `${progress}%` }}
                  transition={{ duration: 0.5, ease: "easeOut" }}
                >
                  {/* Progress Bar Shine Effect */}
                  <motion.div
                    animate={{ x: ['-100%', '100%'] }}
                    transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                    className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent skew-x-12"
                    style={{ width: '30%' }}
                  />
                </motion.div>
              </div>

              {/* Progress Milestones */}
              <div className="flex justify-between mt-2">
                {['25%', '50%', '75%', '100%'].map((milestone, idx) => (
                  <motion.div
                    key={milestone}
                    animate={{ 
                      scale: progress > (idx + 1) * 25 ? [1, 1.2, 1] : 1,
                      color: progress > (idx + 1) * 25 ? '#7170ff' : undefined
                    }}
                    transition={{ duration: 0.3 }}
                    className="text-micro font-medium"
                    style={{ 
                      color: progress > (idx + 1) * 25 ? '#7170ff' : 'var(--color-text-tertiary)'
                    }}
                  >
                    {milestone}
                  </motion.div>
                ))}
              </div>
            </div>

            {/* Status Indicators */}
            <div className="relative z-10 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <motion.div
                  animate={{ scale: [1, 1.3, 1], opacity: [0.5, 1, 0.5] }}
                  transition={{ duration: 1.5, repeat: Infinity }}
                  className="w-2 h-2 bg-green-500 rounded-full"
                />
                <span className="text-micro text-text-secondary font-medium">
                  {progress < 30 ? 'Initializing agents...' :
                   progress < 60 ? 'Processing data...' :
                   progress < 90 ? 'Generating content...' :
                   'Finalizing roadmap...'}
                </span>
              </div>
              
              <div className="flex items-center gap-1">
                <motion.span
                  animate={{ opacity: [0.5, 1, 0.5] }}
                  transition={{ duration: 1, repeat: Infinity }}
                  className="text-micro text-accent-main font-medium"
                >
                  {agentStatus?.agents?.length > 0 ? 'Multi-Agent Active' : 'AI Processing'}
                </motion.span>
                <motion.div
                  animate={{ rotate: [0, 360] }}
                  transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                  className="text-accent-main"
                >
                  🔄
                </motion.div>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Bottom Info */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          className="mt-6 text-center"
        >
          <div className="flex items-center justify-center gap-2 mb-2">
            <motion.div
              animate={{ scale: [1, 1.1, 1] }}
              transition={{ duration: 2, repeat: Infinity }}
              className="w-2 h-2 bg-accent-main rounded-full"
            />
            <span className="text-small text-text-secondary">
              {agentStatus?.agents?.length > 0 
                ? `Advanced AI collaboration in progress...`
                : `AI analysis in progress...`
              }
            </span>
          </div>
          <p className="text-micro text-text-tertiary">
            💡 This process typically takes 30-60 seconds for optimal results
          </p>
        </motion.div>

      </div>
    </div>
  );
};

export default LoadingScreen;