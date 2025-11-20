import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import LinearButton from './LinearButton';
import LinearCard from './LinearCard';
import LoadingSpinner from './LoadingSpinner';

const AgentInterface = () => {
  const [agentStatus, setAgentStatus] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [skills, setSkills] = useState('');
  const [expertise, setExpertise] = useState('');

  const checkAgentStatus = async () => {
    try {
      const response = await fetch(`${process.env.NODE_ENV === 'production' ? '' : 'http://localhost:8001'}/agents/status`);
      const status = await response.json();
      setAgentStatus(status);
    } catch (error) {
      setAgentStatus({ available: false, message: 'Failed to connect to agent system' });
    }
  };

  const runAgentAnalysis = async () => {
    if (!skills.trim() || !expertise.trim()) {
      alert('Please provide both skills and expertise');
      return;
    }

    setIsLoading(true);
    setAnalysis(null);

    try {
      const response = await fetch(`${process.env.NODE_ENV === 'production' ? '' : 'http://localhost:8001'}/agents/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          skills: skills.trim(),
          expertise: expertise.trim(),
          use_memory: true,
          use_web_search: true
        })
      });

      const result = await response.json();
      setAnalysis(result);
    } catch (error) {
      setAnalysis({
        success: false,
        error: `Failed to run agent analysis: ${error.message}`,
        source: 'error'
      });
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    checkAgentStatus();
  }, []);

  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="max-w-4xl mx-auto p-6"
    >
      <LinearCard className="p-8">
        <h2 className="text-title-2 font-semibold mb-6">🤖 AI Agent System Interface</h2>
        
        {/* Agent Status */}
        <div className="mb-6">
          <h3 className="text-regular font-medium mb-2">Agent Status</h3>
          {agentStatus ? (
            <div className={`p-4 rounded-lg ${agentStatus.available ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'}`}>
              <div className="flex items-center gap-2">
                <div className={`w-3 h-3 rounded-full ${agentStatus.available ? 'bg-green-500' : 'bg-red-500'}`}></div>
                <span className={`font-medium ${agentStatus.available ? 'text-green-800' : 'text-red-800'}`}>
                  {agentStatus.available ? 'Available' : 'Unavailable'}
                </span>
              </div>
              <p className={`mt-1 text-small ${agentStatus.available ? 'text-green-700' : 'text-red-700'}`}>
                {agentStatus.message}
              </p>
            </div>
          ) : (
            <div className="p-4 bg-gray-50 rounded-lg">
              <LoadingSpinner size="sm" text="Checking agent status..." />
            </div>
          )}
          <LinearButton 
            variant="outline" 
            size="small" 
            onClick={checkAgentStatus}
            className="mt-2"
          >
            Refresh Status
          </LinearButton>
        </div>

        {/* Input Form */}
        <div className="mb-6">
          <h3 className="text-regular font-medium mb-4">Test Agent Analysis</h3>
          <div className="space-y-4">
            <div>
              <label className="block text-small font-medium mb-2">Skills</label>
              <textarea
                value={skills}
                onChange={(e) => setSkills(e.target.value)}
                placeholder="e.g., Python programming, web development, data analysis"
                className="w-full p-3 border border-border-primary rounded-lg focus:ring-2 focus:ring-accent focus:border-accent"
                rows={3}
              />
            </div>
            <div>
              <label className="block text-small font-medium mb-2">Expertise</label>
              <textarea
                value={expertise}
                onChange={(e) => setExpertise(e.target.value)}
                placeholder="e.g., Intermediate level with 2 years experience in Python"
                className="w-full p-3 border border-border-primary rounded-lg focus:ring-2 focus:ring-accent focus:border-accent"
                rows={3}
              />
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex gap-3 mb-6">
          <LinearButton
            variant="primary"
            onClick={runAgentAnalysis}
            disabled={isLoading || !agentStatus?.available}
          >
            {isLoading ? <LoadingSpinner size="sm" text="Running Analysis..." /> : '🚀 Run Agent Analysis'}
          </LinearButton>
        </div>

        {/* Analysis Results */}
        {analysis && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="border-t border-border-primary pt-6"
          >
            <h3 className="text-regular font-medium mb-4">Analysis Results</h3>
            
            {analysis.success ? (
              <div className="space-y-4">
                <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                  <div className="flex items-center gap-2 mb-2">
                    <div className="w-3 h-3 bg-green-500 rounded-full"></div>
                    <span className="font-medium text-green-800">Analysis Successful</span>
                    <span className="text-small text-green-600">({analysis.source})</span>
                  </div>
                  
                  {analysis.data && (
                    <div className="mt-4">
                      <h4 className="font-medium mb-2">Career Paths Generated:</h4>
                      <div className="text-small bg-white p-3 rounded border">
                        {analysis.data.career_paths?.length || 0} career paths found
                        {analysis.data.career_paths?.map((path, index) => (
                          <div key={index} className="mt-2 p-2 bg-gray-50 rounded">
                            <strong>{path.title}</strong> - {path.match_percentage}% match
                          </div>
                        ))}
                      </div>
                      
                      <h4 className="font-medium mb-2 mt-4">Roadmap Steps:</h4>
                      <div className="text-small bg-white p-3 rounded border">
                        {analysis.data.roadmap?.length || 0} roadmap steps generated
                      </div>
                      
                      <h4 className="font-medium mb-2 mt-4">Learning Resources:</h4>
                      <div className="text-small bg-white p-3 rounded border">
                        Courses: {analysis.data.courses?.length || 0} | 
                        Certifications: {analysis.data.certifications?.length || 0}
                      </div>
                    </div>
                  )}
                </div>
              </div>
            ) : (
              <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
                <div className="flex items-center gap-2 mb-2">
                  <div className="w-3 h-3 bg-red-500 rounded-full"></div>
                  <span className="font-medium text-red-800">Analysis Failed</span>
                  <span className="text-small text-red-600">({analysis.source})</span>
                </div>
                <p className="text-small text-red-700">{analysis.error}</p>
              </div>
            )}
          </motion.div>
        )}
      </LinearCard>
    </motion.div>
  );
};

export default AgentInterface;