import React, { useState, useEffect, useRef, useCallback } from 'react';
import { motion } from 'framer-motion';

const CareerMindMap = ({ nodes, pattern, visible, isMobile }) => {
  const [mousePos, setMousePos] = useState({ x: 50, y: 50 });
  const rafId = useRef(null);
  const containerRef = useRef(null);
  const isThrottled = useRef(false);

  // Throttled mouse move with requestAnimationFrame
  const handleMouseMove = useCallback((e) => {
    if (!containerRef.current || isThrottled.current) return;
    
    if (rafId.current) {
      cancelAnimationFrame(rafId.current);
    }
    
    rafId.current = requestAnimationFrame(() => {
      const rect = containerRef.current.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      setMousePos({ x, y });
      isThrottled.current = false;
    });
    
    isThrottled.current = true;
  }, []);

  useEffect(() => {
    const container = containerRef.current;
    if (container && visible) {
      container.addEventListener('mousemove', handleMouseMove, { passive: true });
      return () => {
        container.removeEventListener('mousemove', handleMouseMove);
        if (rafId.current) {
          cancelAnimationFrame(rafId.current);
        }
      };
    }
  }, [visible, handleMouseMove]);

  // Render Digital Marketing: Growth Arrow with Metrics
  const renderMarketingChart = () => {
    return (
      <motion.svg 
        className="absolute inset-0 w-full h-full"
        initial={{ opacity: 0 }}
        animate={{ opacity: visible ? 1 : 0 }}
        transition={{ duration: 0.5, ease: [0.25, 0.46, 0.45, 0.94] }}
        style={{ filter: 'blur(0.5px)' }}
        viewBox="0 0 100 100"
        preserveAspectRatio="xMidYMid meet"
      >
        {/* Large upward trend arrow */}
        <motion.path
          d="M 30 75 L 30 35 M 30 35 L 25 42 M 30 35 L 35 42"
          stroke="rgba(255,255,255,0.3)"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
          initial={{ pathLength: 0 }}
          animate={{ pathLength: visible ? 1 : 0 }}
          transition={{ duration: 0.8 }}
        />
        
        {/* Metric bars on the arrow */}
        {[
          { h: 20, x: 30, delay: 0.3 },
          { h: 30, x: 42, delay: 0.45 },
          { h: 45, x: 54, delay: 0.6 },
          { h: 55, x: 66, delay: 0.75 }
        ].map((bar, i) => (
          <React.Fragment key={i}>
            <motion.path
              d={`M ${bar.x} 75 L ${bar.x} ${75 - bar.h}`}
              stroke="rgba(255,255,255,0.25)"
              strokeWidth="2.5"
              strokeLinecap="round"
              initial={{ pathLength: 0 }}
              animate={{ pathLength: visible ? 1 : 0 }}
              transition={{ duration: 0.6, delay: bar.delay }}
            />
            {/* Subtle peak on tallest bar */}
            {i === 3 && (
              <motion.path
                d={`M ${bar.x - 2} ${75 - bar.h} L ${bar.x} ${75 - bar.h - 4} L ${bar.x + 2} ${75 - bar.h}`}
                stroke="rgba(255,255,255,0.4)"
                strokeWidth="1.2"
                fill="rgba(255,255,255,0.08)"
                strokeLinecap="round"
                strokeLinejoin="round"
                initial={{ pathLength: 0, opacity: 0 }}
                animate={{ pathLength: visible ? 1 : 0, opacity: visible ? 1 : 0 }}
                transition={{ duration: 0.3, delay: bar.delay + 0.5 }}
              />
            )}
          </React.Fragment>
        ))}
        
        {/* Floating metrics dots */}
        {[
          { x: 42, y: 40 },
          { x: 54, y: 25 },
          { x: 66, y: 15 }
        ].map((pt, i) => (
          <motion.circle
            key={i}
            cx={pt.x}
            cy={pt.y}
            r="2.5"
            fill="rgba(255,255,255,0.4)"
            initial={{ opacity: 0, scale: 0 }}
            animate={visible ? {
              opacity: [0, 1, 1, 0],
              scale: [0, 1.3, 1, 0]
            } : { opacity: 0 }}
            transition={{
              duration: 2.5,
              delay: 1.2 + i * 0.4,
              repeat: Infinity,
              ease: "easeInOut"
            }}
          />
        ))}
      </motion.svg>
    );
  };

  // Render Software Engineering: Code Brackets & Syntax
  const renderCodeStructure = () => {
    return (
      <motion.svg 
        className="absolute inset-0 w-full h-full"
        initial={{ opacity: 0 }}
        animate={{ opacity: visible ? 1 : 0 }}
        transition={{ duration: 0.5, ease: [0.25, 0.46, 0.45, 0.94] }}
        style={{ filter: 'blur(0.5px)' }}
        viewBox="0 0 100 100"
        preserveAspectRatio="xMidYMid meet"
      >
        {/* Large angled brackets */}
        <motion.path
          d="M 25 30 L 35 50 L 25 70 M 75 30 L 65 50 L 75 70"
          stroke="rgba(255,255,255,0.32)"
          strokeWidth="3.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
          initial={{ pathLength: 0 }}
          animate={{ pathLength: visible ? 1 : 0 }}
          transition={{ duration: 1 }}
        />
        
        {/* Internal structure lines */}
        {[35, 50, 65].map((y, i) => (
          <motion.line
            key={i}
            x1="38"
            y1={y}
            x2="62"
            y2={y}
            stroke="rgba(255,255,255,0.12)"
            strokeWidth="1"
            strokeDasharray="3 2"
            initial={{ pathLength: 0, opacity: 0 }}
            animate={{ pathLength: visible ? 1 : 0, opacity: visible ? 1 : 0 }}
            transition={{ duration: 0.6, delay: 0.8 + i * 0.15 }}
          />
        ))}
        
        {/* Syntax highlight glow */}
        <motion.rect
          x="38"
          y="45"
          width="8"
          height="3"
          fill="rgba(255,255,255,0.2)"
          rx="1"
          initial={{ opacity: 0, scaleX: 0 }}
          animate={visible ? {
            opacity: [0, 0.3, 0],
            scaleX: [0, 1, 0]
          } : { opacity: 0 }}
          transition={{
            duration: 1.8,
            delay: 1.3,
            repeat: Infinity,
            ease: "easeInOut"
          }}
        />
      </motion.svg>
    );
  };

  // Render Data Science: Chart Visualization
  const renderDataClusters = () => {
    return (
      <motion.svg 
        className="absolute inset-0 w-full h-full"
        initial={{ opacity: 0 }}
        animate={{ opacity: visible ? 1 : 0 }}
        transition={{ duration: 0.5, ease: [0.25, 0.46, 0.45, 0.94] }}
        style={{ filter: 'blur(0.5px)' }}
        viewBox="0 0 100 100"
        preserveAspectRatio="xMidYMid meet"
      >
        {/* Chart bars - heights: 25, 35, 45, 30. Max height 45 at y=30 */}
        {[
          { x: 25, h: 25, delay: 0 },
          { x: 40, h: 35, delay: 0.2 },
          { x: 55, h: 45, delay: 0.4 },
          { x: 70, h: 30, delay: 0.6 }
        ].map((bar, i) => (
          <motion.rect
            key={i}
            x={bar.x}
            y={75 - bar.h}
            width="8"
            height={0}
            fill="rgba(255,255,255,0.18)"
            stroke="rgba(255,255,255,0.3)"
            strokeWidth="0.5"
            rx="1"
            initial={{ height: 0 }}
            animate={{ 
              height: visible ? bar.h : 0
            }}
            transition={{ 
              duration: 0.8, 
              delay: bar.delay, 
              ease: [0.34, 1.56, 0.64, 1.2]
            }}
          />
        ))}
        
        {/* Base axis line */}
        <motion.line
          x1="20"
          y1="75"
          x2="80"
          y2="75"
          stroke="rgba(255,255,255,0.12)"
          strokeWidth="1"
          initial={{ pathLength: 0 }}
          animate={{ pathLength: visible ? 1 : 0 }}
          transition={{ duration: 0.5 }}
        />
        
        {/* Trend line overlay - smooth curve through bar tops (25,50) -> (40,40) -> (55,30) -> (70,45) */}
        <motion.path
          d="M 25 50 C 30 45, 35 40, 40 40 C 45 40, 50 35, 55 30 C 60 35, 65 40, 70 45"
          fill="none"
          stroke="rgba(255,255,255,0.2)"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeDasharray="2 3"
          initial={{ pathLength: 0 }}
          animate={{ pathLength: visible ? 1 : 0 }}
          transition={{ duration: 1, delay: 0.8 }}
        />
      </motion.svg>
    );
  };

  // Render UI/UX Design: Design Elements
  const renderDesignGrid = () => {
    return (
      <motion.svg 
        className="absolute inset-0 w-full h-full"
        initial={{ opacity: 0 }}
        animate={{ opacity: visible ? 1 : 0 }}
        transition={{ duration: 0.5, ease: [0.25, 0.46, 0.45, 0.94] }}
        style={{ filter: 'blur(0.5px)' }}
        viewBox="0 0 100 100"
        preserveAspectRatio="xMidYMid meet"
      >
        {/* Pen/pencil icon */}
        <motion.path
          d="M 40 20 L 40 75 M 40 20 L 55 35 L 50 40 L 35 25 Z"
          stroke="rgba(255,255,255,0.25)"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
          initial={{ pathLength: 0 }}
          animate={{ pathLength: visible ? 1 : 0 }}
          transition={{ duration: 0.8 }}
        />
        
        {/* Subtle shine on pen tip */}
        <motion.line
          x1="38"
          y1="22"
          x2="42"
          y2="26"
          stroke="rgba(255,255,255,0.4)"
          strokeWidth="1.5"
          strokeLinecap="round"
          initial={{ pathLength: 0 }}
          animate={{ 
            pathLength: visible ? 1 : 0,
            opacity: visible ? [0.4, 0.6, 0.4] : 0
          }}
          transition={{ 
            pathLength: { duration: 0.4, delay: 0.9 },
            opacity: { duration: 2, delay: 1.3, repeat: Infinity, ease: "easeInOut" }
          }}
        />
        
        {/* Design strokes */}
        {[
          { x1: 25, y1: 50, x2: 45, y2: 50 },
          { x1: 55, y1: 35, x2: 70, y2: 35 },
          { x1: 30, y1: 70, x2: 65, y2: 70 }
        ].map((stroke, i) => (
          <motion.line
            key={i}
            x1={stroke.x1}
            y1={stroke.y1}
            x2={stroke.x2}
            y2={stroke.y2}
            stroke="rgba(255,255,255,0.12)"
            strokeWidth="2"
            strokeLinecap="round"
            strokeDasharray="4 2"
            initial={{ pathLength: 0 }}
            animate={{ pathLength: visible ? 1 : 0 }}
            transition={{ duration: 0.5, delay: 0.6 + i * 0.15 }}
          />
        ))}
        
        {/* Color circle */}
        <motion.circle
          cx="65"
          cy="60"
          r="8"
          fill="none"
          stroke="rgba(255,255,255,0.18)"
          strokeWidth="1.5"
          initial={{ scale: 0, opacity: 0 }}
          animate={{ scale: visible ? 1 : 0, opacity: visible ? 1 : 0 }}
          transition={{ duration: 0.5, delay: 0.9 }}
        />
        
        {/* Color dots inside */}
        {[
          { x: 65, y: 56 },
          { x: 68, y: 60 },
          { x: 65, y: 64 },
          { x: 62, y: 60 }
        ].map((pt, i) => (
          <motion.circle
            key={i}
            cx={pt.x}
            cy={pt.y}
            r="1.5"
            fill="rgba(255,255,255,0.25)"
            initial={{ scale: 0 }}
            animate={{ scale: visible ? 1 : 0 }}
            transition={{ duration: 0.3, delay: 1.2 + i * 0.05 }}
          />
        ))}
      </motion.svg>
    );
  };

  // Mobile/touch: minimal
  if (isMobile) {
    return null;
  }

  // Desktop: Full iconic visualizations
  return (
    <div ref={containerRef} className="absolute inset-0 pointer-events-none overflow-hidden">
      {/* Gradient mask for text readability */}
      <motion.div
        className="absolute inset-0"
        style={{
          background: 'linear-gradient(to bottom, rgba(28,28,31,0.4) 0%, rgba(28,28,31,0.2) 20%, transparent 40%)',
          pointerEvents: 'none'
        }}
        animate={{ opacity: visible ? 1 : 0 }}
        transition={{ duration: 0.5 }}
      />

      {/* Pattern-specific iconic representations */}
      {pattern === 'trend' && renderMarketingChart()}
      {pattern === 'code' && renderCodeStructure()}
      {pattern === 'chart' && renderDataClusters()}
      {pattern === 'grid' && renderDesignGrid()}

      {/* Parallax mouse light */}
      <motion.div
        className="absolute"
        style={{
          width: '200px',
          height: '200px',
          left: `${mousePos.x}%`,
          top: `${mousePos.y}%`,
          transform: 'translate(-50%, -50%)',
          background: 'radial-gradient(circle, rgba(255,255,255,0.02) 0%, transparent 70%)',
          filter: 'blur(40px)',
          pointerEvents: 'none'
        }}
        animate={{ opacity: visible ? 1 : 0 }}
        transition={{ duration: 0.3 }}
      />
    </div>
  );
};

export default CareerMindMap;
