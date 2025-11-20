import React from 'react';
import { motion } from 'framer-motion';

const LinearButton = ({ 
  children, 
  className = '',
  variant = 'primary', // primary, secondary, tertiary, ghost, glass
  size = 'default', // mini, small, default, large
  disabled = false,
  loading = false,
  icon,
  onClick,
  ...props 
}) => {
  // Button size configurations (matching Linear exactly)
  const sizes = {
    mini: {
      height: '24px',
      padding: '0 10px',
      fontSize: '12px',
      iconSize: '12px',
      gap: '4px',
      borderRadius: '6px',
    },
    small: {
      height: '32px',
      padding: '0 12px',
      fontSize: '13px',
      iconSize: '16px',
      gap: '8px',
      borderRadius: '8px',
    },
    default: {
      height: '40px',
      padding: '0 16px',
      fontSize: '15px',
      iconSize: '18px',
      gap: '6px',
      borderRadius: '10px',
    },
    large: {
      height: '48px',
      padding: '0 16px',
      fontSize: '16px',
      iconSize: '18px',
      gap: '6px',
      borderRadius: '8px',
    },
  };

  // Button variant configurations (matching Linear exactly)
  const variants = {
    primary: {
      base: 'bg-brand text-white border-0',
      hover: !disabled && !loading,
      active: !disabled && !loading,
    },
    secondary: {
      base: 'bg-bg-quaternary text-text-primary border border-border-tertiary',
      hover: !disabled && !loading,
      active: !disabled && !loading,
    },
    tertiary: {
      base: 'bg-bg-primary text-text-tertiary border border-bg-secondary',
      hover: !disabled && !loading,
      active: !disabled && !loading,
    },
    ghost: {
      base: 'bg-transparent text-text-tertiary border-0',
      hover: !disabled && !loading,
      active: !disabled && !loading,
    },
    glass: {
      base: 'bg-transparent text-text-primary border-0',
      hover: !disabled && !loading,
      active: !disabled && !loading,
    },
  };

  const selectedSize = sizes[size];
  const selectedVariant = variants[variant];

  return (
    <motion.button
      className={`
        inline-flex items-center justify-center
        font-medium cursor-pointer select-none
        transition-regular ease-out-quad whitespace-nowrap
        ${selectedVariant.base}
        ${disabled || loading ? 'opacity-50 cursor-not-allowed' : ''}
        ${className}
      `}
      style={{
        height: selectedSize.height,
        padding: selectedSize.padding,
        fontSize: selectedSize.fontSize,
        gap: selectedSize.gap,
        borderRadius: selectedSize.borderRadius,
        transitionProperty: 'border, background-color, color, box-shadow, opacity, filter, transform',
        transitionDuration: '.16s',
        transitionTimingFunction: 'cubic-bezier(.25, .46, .45, .94)',
      }}
      whileHover={
        selectedVariant.hover ? {
          filter: variant === 'primary' ? 'brightness(115%)' : variant === 'secondary' ? 'brightness(125%)' : 'none',
          backgroundColor: variant === 'tertiary' ? 'rgba(35, 35, 38, 1)' : 
                          variant === 'ghost' ? 'rgba(40, 40, 44, 1)' : 
                          variant === 'glass' ? 'rgba(255, 255, 255, 0.16)' : undefined,
          boxShadow: variant === 'primary' ? '0 0 20px rgba(255, 255, 255, 0.15)' : undefined,
        } : {}
      }
      whileTap={
        selectedVariant.active ? {
          scale: 0.97,
          filter: variant === 'primary' ? 'brightness(98%)' : variant === 'secondary' ? 'brightness(98%)' : 'none',
        } : {}
      }
      onClick={onClick}
      disabled={disabled || loading}
      {...props}
    >
      {loading ? (
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
          className="border-2 border-current border-t-transparent rounded-full"
          style={{ width: selectedSize.iconSize, height: selectedSize.iconSize }}
        />
      ) : (
        <>
          {icon && <span style={{ width: selectedSize.iconSize, height: selectedSize.iconSize }}>{icon}</span>}
          {children}
        </>
      )}
    </motion.button>
  );
};

export default LinearButton;

