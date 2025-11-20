import React from 'react';
import { motion } from 'framer-motion';

const LinearCard = ({ 
  children, 
  className = '',
  hover = true,
  onClick,
  style = {},
  ...props 
}) => {
  return (
    <motion.div
      className={`
        bg-bg-secondary border border-border-primary rounded-12
        transition-regular ease-out-quad relative overflow-hidden
        ${className}
      `}
      style={{
        transitionProperty: 'background-color, border-color',
        transitionDuration: '.16s',
        transitionTimingFunction: 'cubic-bezier(.25, .46, .45, .94)',
        ...style
      }}
      whileHover={hover ? {
        backgroundColor: 'rgba(35, 35, 38, 1)', // bg-tertiary
        borderColor: 'rgba(255, 255, 255, 0.12)',
        scale: 1.01,
      } : {}}
      whileTap={hover ? { scale: 0.98 } : {}}
      transition={{
        type: "spring",
        stiffness: 400,
        damping: 30
      }}
      onClick={onClick}
      {...props}
    >
      {/* Subtle hover glow effect */}
      {hover && (
        <motion.div
          className="absolute inset-0 pointer-events-none opacity-0"
          style={{
            background: 'radial-gradient(circle at 50% 50%, rgba(113, 112, 255, 0.05) 0%, transparent 70%)',
          }}
          whileHover={{ opacity: 1 }}
          transition={{ duration: 0.3 }}
        />
      )}
      <div className="relative z-10">
        {children}
      </div>
    </motion.div>
  );
};

export default LinearCard;

