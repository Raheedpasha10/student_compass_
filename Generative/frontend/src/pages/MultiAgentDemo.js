import React, { useState } from 'react';
import { careerAPI } from '../services/api';
import LoadingSpinner from '../components/LoadingSpinner';

const MultiAgentDemo = () => {
  const [query, setQuery] = useState('');
  const [background, setBackground] = useState({
    current_skills: '',
    experience_level: 'Beginner',
    time_available: '',
    goals: ''
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGenerate = async () => {
    if (!query.trim()) {
      setError('Please enter a career goal or question');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await careerAPI.generateMultiAgentRoadmap(
        query,
        {
          current_skills: background.current_skills || undefined,
          experience_level: background.experience_level,
          time_available: background.time_available || undefined,
          goals: background.goals || undefined
        },
        true // include agent details
      );

      setResult(response);
    } catch (err) {
      setError(err.message || 'Failed to generate roadmap');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-blue-50 py-12 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            🤖 Multi-Agent Career Roadmap Generator
          </h1>
          <p className="text-xl text-gray-600">
            Powered by 3 AI agents working in parallel
          </p>
          <div className="mt-4 flex justify-center gap-4 text-sm text-gray-500">
            <span className="bg-purple-100 px-3 py-1 rounded-full">Strategic Planner</span>
            <span className="bg-blue-100 px-3 py-1 rounded-full">Practical Guide</span>
            <span className="bg-green-100 px-3 py-1 rounded-full">Technical Expert</span>
          </div>
        </div>

        {/* Input Form */}
        <div className="bg-white rounded-2xl shadow-xl p-8 mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">Your Career Goal</h2>
          
          <div className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                What do you want to achieve? *
              </label>
              <textarea
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="e.g., I want to become a data scientist, I want to transition to web development, etc."
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                rows="3"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Current Skills (optional)
                </label>
                <input
                  type="text"
                  value={background.current_skills}
                  onChange={(e) => setBackground({...background, current_skills: e.target.value})}
                  placeholder="e.g., Python basics, Excel"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Experience Level
                </label>
                <select
                  value={background.experience_level}
                  onChange={(e) => setBackground({...background, experience_level: e.target.value})}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                >
                  <option value="Beginner">Beginner</option>
                  <option value="Intermediate">Intermediate</option>
                  <option value="Advanced">Advanced</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Time Available (optional)
                </label>
                <input
                  type="text"
                  value={background.time_available}
                  onChange={(e) => setBackground({...background, time_available: e.target.value})}
                  placeholder="e.g., 10 hours per week"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Goals (optional)
                </label>
                <input
                  type="text"
                  value={background.goals}
                  onChange={(e) => setBackground({...background, goals: e.target.value})}
                  placeholder="e.g., Get a job in 12 months"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                />
              </div>
            </div>

            <button
              onClick={handleGenerate}
              disabled={loading}
              className="w-full bg-gradient-to-r from-purple-600 to-blue-600 text-white font-bold py-4 px-8 rounded-lg hover:from-purple-700 hover:to-blue-700 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Generating with AI Agents...' : '🚀 Generate Roadmap'}
            </button>
          </div>
        </div>

        {/* Loading */}
        {loading && (
          <div className="text-center py-12">
            <LoadingSpinner variant="ring" text="Generating with AI Agents..." />
            <p className="mt-4 text-gray-600">
              Our 3 AI agents are working on your personalized roadmap...
            </p>
          </div>
        )}

        {/* Error */}
        {error && (
          <div className="bg-red-50 border-l-4 border-red-500 p-6 rounded-lg mb-8">
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {/* Results */}
        {result && !loading && (
          <div className="space-y-8">
            {/* Agent Insights */}
            {result.agent_insights && (
              <div className="bg-white rounded-2xl shadow-xl p-8">
                <h2 className="text-2xl font-bold text-gray-800 mb-6">
                  🤖 Agent Contributions
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  {result.agent_insights.map((agent, idx) => (
                    <div 
                      key={idx}
                      className="bg-gradient-to-br from-purple-50 to-blue-50 rounded-xl p-6 border border-purple-200"
                    >
                      <h3 className="font-bold text-lg text-gray-800 mb-2">
                        {agent.agent_name}
                      </h3>
                      <div className="mb-3">
                        <div className="flex items-center justify-between mb-1">
                          <span className="text-sm text-gray-600">Confidence</span>
                          <span className="text-sm font-bold text-purple-600">
                            {(agent.confidence * 100).toFixed(0)}%
                          </span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                          <div 
                            className="bg-gradient-to-r from-purple-500 to-blue-500 h-2 rounded-full"
                            style={{width: `${agent.confidence * 100}%`}}
                          />
                        </div>
                      </div>
                      <p className="text-sm text-gray-600 italic">
                        Focus: {agent.focus}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Final Roadmap */}
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <h2 className="text-2xl font-bold text-gray-800 mb-6">
                🗺️ Your Personalized Roadmap
              </h2>
              <div className="prose prose-lg max-w-none">
                <div className="whitespace-pre-wrap text-gray-700">
                  {result.final_roadmap}
                </div>
              </div>
            </div>

            {/* Metadata */}
            {result.metadata && (
              <div className="bg-gray-50 rounded-xl p-6 text-sm text-gray-600">
                <div className="flex justify-between items-center">
                  <span>
                    Generated by {result.metadata.successful_agents} out of {result.metadata.num_agents} agents
                  </span>
                  <span className="text-green-600 font-semibold">
                    ✓ Multi-Agent Analysis Complete
                  </span>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default MultiAgentDemo;
