import React, { useState, useEffect } from 'react';

const FunnelingReport = ({ sessionId, report }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    if (report) {
      setTimeout(() => setIsVisible(true), 100);
    }
  }, [report]);

  if (!report) {
    return (
      <div className="bg-bg-secondary border border-border-primary rounded-8 p-4 mt-4">
        <p className="text-text-secondary">No funneling report available</p>
      </div>
    );
  }

  const formatTimestamp = (timestamp) => {
    return new Date(timestamp * 1000).toLocaleString();
  };

  const getStatusColor = (success) => {
    return success ? 'text-green-600' : 'text-red-600';
  };

  const getConfidenceColor = (confidence) => {
    if (confidence >= 0.8) return 'text-green-600';
    if (confidence >= 0.6) return 'text-yellow-600';
    return 'text-red-600';
  };

  return (
    <div className={`bg-bg-secondary border border-border-primary rounded-8 p-6 mt-6 transition-all duration-500 ease-out transform ${
      isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
    }`}>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-large font-semibold text-text-primary flex items-center gap-2">
          🔍 Multi-Agent Funneling Report
          <span className="text-small font-normal text-text-secondary">
            (Session: {typeof report.session_id === 'string' ? report.session_id : 'Unknown'})
          </span>
        </h3>
        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="text-accent hover:text-accent-hover text-small font-medium transition-all duration-200 flex items-center gap-2"
        >
          {isExpanded ? 'Hide Details' : 'Show Details'}
          <svg 
            className={`w-4 h-4 transition-transform duration-200 ${isExpanded ? 'rotate-180' : 'rotate-0'}`}
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>
      </div>

      {/* Summary Overview */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6"
           style={{ animationDelay: '0.2s' }}>
        <div className="bg-bg-tertiary rounded-6 p-3 border border-border-primary">
          <div className="text-small font-medium text-text-primary mb-1">Agents Used</div>
          <div className="text-title-3 font-semibold text-accent">
            {report.agent_performance?.total_agents || 0}
          </div>
        </div>
        <div className="bg-bg-tertiary rounded-6 p-3 border border-border-primary">
          <div className="text-small font-medium text-text-primary mb-1">Success Rate</div>
          <div className={`text-title-3 font-semibold ${
            (report.agent_performance?.success_rate_percent || 0) >= 70 ? 'text-green-600' : 
            (report.agent_performance?.success_rate_percent || 0) >= 40 ? 'text-yellow-600' : 'text-red-600'
          }`}>
            {report.agent_performance?.success_rate_percent || 0}%
          </div>
          <div className="text-xs text-text-secondary mt-1">
            {report.agent_performance?.successful_agents || 0}/{report.agent_performance?.total_agents || 0} agents
          </div>
        </div>
        <div className="bg-bg-tertiary rounded-6 p-3 border border-border-primary">
          <div className="text-small font-medium text-text-primary mb-1">Best Agent</div>
          <div className="text-regular font-medium text-text-primary">
            {report.funneling_process?.best_agent || 'N/A'}
          </div>
        </div>
        <div className="bg-bg-tertiary rounded-6 p-3 border border-border-primary">
          <div className="text-small font-medium text-text-primary mb-1">Execution Time</div>
          <div className="text-regular font-medium text-text-primary">
            {report.output_metrics?.total_execution_time || 'N/A'}
          </div>
          <div className="text-xs text-text-secondary mt-1">
            {report.output_metrics?.phases_generated || 0} phases generated
          </div>
        </div>
      </div>

      {/* Agent Performance Summary */}
      <div className="mb-6">
        <h4 className="text-regular font-semibold text-text-primary mb-3">Agent Performance</h4>
        <div className="grid gap-3">
          {Array.isArray(report.agent_performance?.individual_results) && 
           report.agent_performance.individual_results
             .filter(agent => agent && typeof agent === 'object')
             .map((agent, idx) => (
            <div key={idx} className="flex items-center justify-between p-3 bg-bg-tertiary rounded-6 border border-border-primary">
              <div className="flex items-center gap-3">
                <div className={`w-3 h-3 rounded-full ${agent.success ? 'bg-green-500' : 'bg-red-500'}`}></div>
                <div>
                  <div className="font-medium text-text-primary">
                    {typeof agent.agent_name === 'string' ? agent.agent_name : 'Agent'}
                  </div>
                  <div className="text-small text-text-secondary">
                    {typeof agent.provider === 'string' ? agent.provider : 'Provider'}/
                    {typeof agent.model === 'string' ? agent.model : 'Model'}
                  </div>
                </div>
              </div>
              <div className="text-right">
                <div className={`font-medium ${getConfidenceColor(agent.confidence_score || 0)}`}>
                  {((agent.confidence_score || 0) * 100).toFixed(1)}%
                </div>
                <div className="text-small text-text-secondary">
                  {typeof agent.response_time === 'string' ? agent.response_time : 'N/A'}
                </div>
                {!agent.success && agent.error && (
                  <div className="text-xs text-red-500 mt-1 max-w-xs truncate" title={agent.error}>
                    {agent.error.includes('rate_limit') ? '⚠️ Rate limit' : 
                     agent.error.includes('leaked') ? '🔒 API key issue' : '❌ Error'}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Expanded Details */}
      {isExpanded && (
        <div className="space-y-6">
          {/* Funneling Decision Process */}
          <div>
            <h4 className="text-regular font-semibold text-text-primary mb-3">Funneling Decision</h4>
            <div className="bg-bg-tertiary rounded-6 p-4 border border-border-primary">
              <div className="mb-3">
                <div className="text-small text-text-secondary mb-2">Selection Method:</div>
                <div className="text-regular text-text-primary font-medium">
                  {typeof report.funneling_process?.method === 'string' ? report.funneling_process.method : 'Confidence-based selection'}
                </div>
              </div>
              <div className="mb-3">
                <div className="text-small text-text-secondary mb-2">Decision Rationale:</div>
                <div className="text-regular text-text-primary">
                  {typeof report.funneling_process?.decision_rationale === 'string' ? report.funneling_process.decision_rationale : 'Selected based on highest confidence score'}
                </div>
              </div>
              <div>
                <div className="text-small text-text-secondary mb-2">Confidence Scores:</div>
                <div className="space-y-2">
                  {Object.entries(report.funneling_process?.confidence_scores || {})
                    .filter(([agent, score]) => agent && typeof score === 'number')
                    .map(([agent, score]) => (
                    <div key={agent} className="flex justify-between items-center">
                      <span className="text-regular text-text-primary">{String(agent)}</span>
                      <span className={`font-medium ${getConfidenceColor(score)}`}>
                        {(score * 100).toFixed(1)}%
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Output Quality Metrics */}
          <div>
            <h4 className="text-regular font-semibold text-text-primary mb-3">Output Quality</h4>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-bg-tertiary rounded-6 p-3 border border-border-primary text-center">
                <div className="text-title-3 font-bold text-accent">
                  {report.output_metrics?.phases_generated || 0}
                </div>
                <div className="text-small text-text-secondary">Phases Generated</div>
              </div>
              <div className="bg-bg-tertiary rounded-6 p-3 border border-border-primary text-center">
                <div className="text-title-3 font-bold text-accent">
                  {report.output_metrics?.content_items || 0}
                </div>
                <div className="text-small text-text-secondary">Content Items</div>
              </div>
              <div className="bg-bg-tertiary rounded-6 p-3 border border-border-primary text-center">
                <div className="text-title-3 font-bold text-accent">
                  {Math.round((report.output_metrics?.roadmap_length || 0) / 1000)}k
                </div>
                <div className="text-small text-text-secondary">Characters Generated</div>
              </div>
            </div>
          </div>

          {/* Timeline */}
          <div>
            <h4 className="text-regular font-semibold text-text-primary mb-3">Execution Timeline</h4>
            <div className="space-y-2 max-h-60 overflow-y-auto">
              {Array.isArray(report.detailed_timeline) && report.detailed_timeline
                .filter(event => event && typeof event === 'object')
                .map((event, idx) => (
                <div key={idx} className="flex items-center gap-3 p-2 bg-bg-tertiary rounded-6 border border-border-primary">
                  <div className="w-2 h-2 bg-accent rounded-full flex-shrink-0"></div>
                  <div className="flex-1">
                    <div className="text-regular text-text-primary">
                      {typeof event.details === 'string' ? event.details : 'Event details'}
                    </div>
                    <div className="text-small text-text-secondary">
                      {event.timestamp ? formatTimestamp(event.timestamp) : 'No timestamp'}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Footer */}
      <div className="mt-4 pt-4 border-t border-border-primary text-center">
        <p className="text-small text-text-secondary">
          This report shows how multiple AI agents collaborated to create your personalized roadmap.
          The system selected the best result based on confidence scores and content quality.
        </p>
      </div>
    </div>
  );
};

export default FunnelingReport;