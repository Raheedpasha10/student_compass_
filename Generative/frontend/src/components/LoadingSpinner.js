import React from 'react';
import { motion } from 'framer-motion';

const LoadingSpinner = ({ size = 'md', text = '', variant = 'ring', fullscreen = false }) => {
  const sizes = {
    sm: 16,
    md: 24,
    lg: 32,
  };

  const spinnerSize = sizes[size];

  return (
    <div className={(fullscreen ? 'fixed inset-0 z-40 ' : '') + 'flex flex-col items-center justify-center gap-4 py-8'}>
      {fullscreen && (
        <div
          className="absolute inset-0 pointer-events-none"
          style={{ background: 'radial-gradient(ellipse at center, rgba(113,112,255,0.08) 0%, transparent 70%)' }}
        />
      )}

      {variant === 'ring' && (
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
          style={{
            width: spinnerSize,
            height: spinnerSize,
            border: '2px solid rgba(255,255,255,0.12)',
            borderTopColor: 'var(--color-accent)',
            borderRadius: '50%'
          }}
        />
      )}

      {variant === 'dots' && (
        <div className="flex items-center gap-2">
          {[0,1,2].map(i => (
            <motion.span
              key={i}
              className="block rounded-full"
              style={{ width: spinnerSize/5, height: spinnerSize/5, background: 'var(--color-accent)'}}
              animate={{ y: [0, -6, 0] }}
              transition={{ duration: 0.6, repeat: Infinity, delay: i * 0.12 }}
            />
          ))}
        </div>
      )}

      {variant === 'bar' && (
        <div className="w-48 h-1.5 rounded-full overflow-hidden bg-[rgba(255,255,255,0.08)]">
          <motion.div
            className="h-full rounded-full"
            style={{ background: 'linear-gradient(90deg, rgba(113,112,255,0.0), rgba(113,112,255,0.8), rgba(113,112,255,0.0))' }}
            animate={{ x: ['-100%', '100%'] }}
            transition={{ duration: 1.2, repeat: Infinity, ease: 'easeInOut' }}
          />
        </div>
      )}

      {text && (
        <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-small text-text-secondary font-medium">
          {text}
        </motion.p>
      )}
    </div>
  );
};

export default LoadingSpinner;
