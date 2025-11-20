import React from 'react';
import { motion } from 'framer-motion';

const Enhanced3DCard = ({ 
  children, 
  className = '',
  tiltEffect = true,
  glowEffect = true,
  floatingEffect = false,
  onClick,
  style = {},
  ...props 
}) => {
  return (
    <motion.div
      className={`relative ${className}`}
      whileHover={tiltEffect ? { 
        y: -10,
        rotateX: 5,
        rotateY: 5,
        scale: 1.02
      } : { y: -10 }}
      whileTap={{ scale: 0.98 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      style={{
        transformStyle: 'preserve-3d',
        perspective: '1000px',
        ...(glowEffect && {
          boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)'
        }),
        ...style
      }}
      onClick={onClick}
      {...props}
    >
      {/* Glow effect */}
      {glowEffect && (
        <div 
          className="absolute inset-0 rounded-xl -z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
          style={{
            background: 'radial-gradient(600px circle at var(--mouse-x) var(--mouse-y), rgba(125, 125, 125, 0.1), transparent 40%)',
          }}
        />
      )}
      
      {/* Floating effect */}
      {floatingEffect && (
        <motion.div
          animate={{ y: [0, -10, 0] }}
          transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
        >
          {children}
        </motion.div>
      )}
      
      {/* Card content */}
      <div 
        className={`rounded-xl border transition-all duration-300 ${
          tiltEffect ? 'group' : ''
        }`}
        style={{
          transform: 'translateZ(20px)',
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.7) 100%)',
          border: '1px solid rgba(148, 163, 184, 0.2)',
          boxShadow: glowEffect ? '0 25px 50px -12px rgba(0, 0, 0, 0.25), 0 0 30px rgba(59, 130, 246, 0.1)' : '0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.05)'
        }}
      >
        {floatingEffect ? null : children}
      </div>
    </motion.div>
  );
};

export default Enhanced3DCard;