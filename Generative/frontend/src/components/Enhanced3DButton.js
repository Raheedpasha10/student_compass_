import React from 'react';
import { motion } from 'framer-motion';

const Enhanced3DButton = ({ 
  children, 
  className = '',
  variant = 'primary', // primary, secondary, success, danger, warning, info
  size = 'md', // sm, md, lg
  disabled = false,
  loading = false,
  icon,
  onClick,
  ...props 
}) => {
  // Define color variants
  const variants = {
    primary: {
      bg: 'bg-gradient-to-r from-blue-500 to-indigo-600',
      hover: 'hover:from-blue-600 hover:to-indigo-700',
      active: 'active:from-blue-700 active:to-indigo-800',
      shadow: 'shadow-lg shadow-blue-500/30',
      hoverShadow: 'hover:shadow-xl hover:shadow-blue-500/40',
      border: 'border border-blue-600/50'
    },
    secondary: {
      bg: 'bg-gradient-to-r from-gray-700 to-gray-600',
      hover: 'hover:from-gray-600 hover:to-gray-500',
      active: 'active:from-gray-500 active:to-gray-400',
      shadow: 'shadow-lg shadow-gray-700/50',
      hoverShadow: 'hover:shadow-xl hover:shadow-gray-700/70',
      border: 'border border-gray-400/70'
    },
    success: {
      bg: 'bg-gradient-to-r from-green-500 to-emerald-600',
      hover: 'hover:from-green-600 hover:to-emerald-700',
      active: 'active:from-green-700 active:to-emerald-800',
      shadow: 'shadow-lg shadow-green-500/30',
      hoverShadow: 'hover:shadow-xl hover:shadow-green-500/40',
      border: 'border border-green-600/50'
    },
    danger: {
      bg: 'bg-gradient-to-r from-red-500 to-rose-600',
      hover: 'hover:from-red-600 hover:to-rose-700',
      active: 'active:from-red-700 active:to-rose-800',
      shadow: 'shadow-lg shadow-red-500/30',
      hoverShadow: 'hover:shadow-xl hover:shadow-red-500/40',
      border: 'border border-red-600/50'
    },
    warning: {
      bg: 'bg-gradient-to-r from-amber-500 to-orange-600',
      hover: 'hover:from-amber-600 hover:to-orange-700',
      active: 'active:from-amber-700 active:to-orange-800',
      shadow: 'shadow-lg shadow-amber-500/30',
      hoverShadow: 'hover:shadow-xl hover:shadow-amber-500/40',
      border: 'border border-amber-600/50'
    },
    info: {
      bg: 'bg-gradient-to-r from-cyan-500 to-sky-600',
      hover: 'hover:from-cyan-600 hover:to-sky-700',
      active: 'active:from-cyan-700 active:to-sky-800',
      shadow: 'shadow-lg shadow-cyan-500/30',
      hoverShadow: 'hover:shadow-xl hover:shadow-cyan-500/40',
      border: 'border border-cyan-600/50'
    }
  };

  // Define size variants
  const sizes = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };

  const selectedVariant = variants[variant];
  const selectedSize = sizes[size];

  return (
    <motion.button
      className={`
        ${selectedVariant.bg} 
        ${!disabled && !loading ? selectedVariant.hover : ''} 
        ${selectedVariant.border}
        ${selectedVariant.shadow}
        ${!disabled && !loading ? selectedVariant.hoverShadow : ''}
        ${selectedSize}
        ${className}
        rounded-xl font-semibold
        transition-all duration-300
        transform-gpu
        disabled:opacity-50 disabled:cursor-not-allowed
        flex items-center justify-center
        focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-900 focus:ring-blue-500
      `}
      whileHover={!disabled && !loading ? { 
        y: -3,
        scale: 1.03,
        transition: { duration: 0.2 }
      } : {}}
      whileTap={!disabled && !loading ? { 
        y: 0,
        scale: 0.98,
        transition: { duration: 0.1 }
      } : {}}
      onClick={onClick}
      disabled={disabled || loading}
      style={{
        transformStyle: 'preserve-3d',
        perspective: '1000px'
      }}
      {...props}
    >
      {loading ? (
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
          className="w-5 h-5 border-2 border-white border-t-transparent rounded-full"
        />
      ) : (
        <>
          {icon && <span className="mr-2">{icon}</span>}
          {children}
        </>
      )}
    </motion.button>
  );
};

export default Enhanced3DButton;