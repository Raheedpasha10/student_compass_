import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { useAppContext } from '../context/AppContext';
import SearchBar from './SearchBar';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [hoveredItem, setHoveredItem] = useState(null);
  const location = useLocation();
  const { showGlobalFunnelingReport, toggleFunnelingReport } = useAppContext();

  const navItems = [
    { 
      path: '/', 
      label: 'Home',
      preview: 'Explore career opportunities tailored to your interests'
    },
    { 
      path: '/simplified-ultimate-roadmap', 
      label: 'Roadmap',
      preview: 'View your personalized learning roadmap'
    },
    { 
      path: '/flowchart', 
      label: 'Flowchart',
      preview: 'Track your progress visually step by step'
    },
    { 
      path: '/career-path', 
      label: 'Career Paths',
      preview: 'Discover in-demand career paths and salaries'
    }
  ];

  const isActive = (path) => location.pathname === path;

  return (
    <nav 
      className="fixed top-0 left-0 right-0 z-[100]"
      style={{
        backdropFilter: 'blur(20px)',
        WebkitBackdropFilter: 'blur(20px)',
        background: 'rgba(11, 11, 11, 0.8)',
        borderBottom: '0.5px solid rgba(255, 255, 255, 0.08)',
      }}
    >
      <div className="max-w-full px-6">
        <div className="flex items-center justify-between" style={{ height: '64px' }}>
          {/* Logo with Icon */}
          <Link to="/" className="flex items-center gap-2 group">
            <motion.div 
              className="flex items-center gap-2"
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              {/* Compass Logo Icon */}
              <svg 
                width="24" 
                height="24" 
                viewBox="0 0 24 24" 
                fill="none" 
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="text-white"
              >
                <circle cx="12" cy="12" r="10"/>
                <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>
              </svg>
              
              <span 
                className="text-xl font-semibold text-white"
                style={{ letterSpacing: '-.012em' }}
              >
                StudentCompass
              </span>
            </motion.div>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-1">
            {navItems.map((item) => (
              <div
                key={item.path}
                className="relative"
                onMouseEnter={() => setHoveredItem(item.path)}
                onMouseLeave={() => setHoveredItem(null)}
              >
                <Link to={item.path}>
                  <motion.div
                    className={`
                      px-3 py-1.5 rounded-8 text-small font-medium
                      transition-regular ease-out-quad
                      ${isActive(item.path) 
                        ? 'text-text-primary' 
                        : 'text-text-tertiary hover:text-text-primary'
                      }
                    `}
                    style={{
                      backgroundColor: isActive(item.path) 
                        ? 'rgba(255, 255, 255, 0.05)' 
                        : 'transparent',
                    }}
                    whileHover={{
                      backgroundColor: isActive(item.path) 
                        ? 'rgba(255, 255, 255, 0.05)' 
                        : 'rgba(255, 255, 255, 0.03)',
                    }}
                  >
                    {item.label}
                  </motion.div>
                </Link>

                {/* Hover Preview Dropdown */}
                <AnimatePresence>
                  {hoveredItem === item.path && (
                    <motion.div
                      initial={{ opacity: 0, scale: 0.98, y: -5 }}
                      animate={{ opacity: 1, scale: 1, y: 0 }}
                      exit={{ opacity: 0, scale: 0.98, y: -5 }}
                      transition={{ duration: 0.16, ease: [0.25, 0.46, 0.45, 0.94] }}
                      className="absolute top-full mt-2 left-0 min-w-[240px] rounded-8 p-3 shadow-linear-medium"
                      style={{
                        backdropFilter: 'blur(20px)',
                        WebkitBackdropFilter: 'blur(20px)',
                        background: 'rgba(28, 28, 31, 0.95)',
                        border: '0.5px solid rgba(255, 255, 255, 0.08)',
                      }}
                      onMouseEnter={() => setHoveredItem(item.path)}
                      onMouseLeave={() => setHoveredItem(null)}
                    >
                      <div className="text-small text-text-secondary">
                        {item.preview}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            ))}
          </div>

          {/* Search Bar and Funneling Toggle */}
          <div className="hidden md:flex items-center gap-3">
            <SearchBar />
            
            {/* Funneling Report Toggle */}
            <motion.button
              onClick={toggleFunnelingReport}
              className={`
                px-3 py-1.5 rounded-6 text-micro font-medium
                transition-regular ease-out-quad
                ${showGlobalFunnelingReport 
                  ? 'text-accent bg-accent bg-opacity-10 border border-accent border-opacity-20' 
                  : 'text-text-tertiary hover:text-text-primary hover:bg-white hover:bg-opacity-5'
                }
              `}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              title={showGlobalFunnelingReport ? 'Hide Agent Reports' : 'Show Agent Reports'}
            >
              🔍 AI Report
            </motion.button>
          </div>

          {/* Mobile Menu Button */}
          <motion.button
            className="md:hidden p-2 text-text-tertiary"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            whileTap={{ scale: 0.95 }}
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              {isMenuOpen ? (
                <>
                  <motion.line 
                    x1="18" y1="6" x2="6" y2="18" 
                    strokeWidth="2" 
                    strokeLinecap="round"
                    initial={{ rotate: 0 }}
                    animate={{ rotate: 45 }}
                  />
                  <motion.line 
                    x1="6" y1="6" x2="18" y2="18" 
                    strokeWidth="2" 
                    strokeLinecap="round"
                    initial={{ rotate: 0 }}
                    animate={{ rotate: -45 }}
                  />
                </>
              ) : (
                <>
                  <line x1="3" y1="12" x2="21" y2="12" strokeWidth="2" strokeLinecap="round" />
                  <line x1="3" y1="6" x2="21" y2="6" strokeWidth="2" strokeLinecap="round" />
                  <line x1="3" y1="18" x2="21" y2="18" strokeWidth="2" strokeLinecap="round" />
                </>
              )}
            </svg>
          </motion.button>
        </div>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.2, ease: [0.25, 0.46, 0.45, 0.94] }}
            className="md:hidden border-t border-border-translucent"
            style={{
              backdropFilter: 'blur(32px)',
              WebkitBackdropFilter: 'blur(32px)',
              background: 'rgba(11, 11, 11, 0.95)',
            }}
          >
            <div className="px-6 py-4">
              <div className="flex flex-col gap-1 mb-4">
                {navItems.map((item, index) => (
                  <motion.div
                    key={item.path}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.05 }}
                  >
                    <Link
                      to={item.path}
                      onClick={() => setIsMenuOpen(false)}
                      className={`
                        block px-4 py-3 rounded-8
                        text-regular font-medium transition-regular
                        ${isActive(item.path) 
                          ? 'text-text-primary bg-bg-tertiary' 
                          : 'text-text-tertiary hover:text-text-primary hover:bg-bg-secondary'
                        }
                      `}
                    >
                      <div className="font-medium mb-0.5">{item.label}</div>
                      <div className="text-micro text-text-quaternary">
                        {item.preview}
                      </div>
                    </Link>
                  </motion.div>
                ))}
              </div>
              <div className="mb-4">
                <SearchBar />
              </div>
              
              {/* Mobile Funneling Toggle */}
              <motion.button
                onClick={toggleFunnelingReport}
                className={`
                  w-full px-4 py-3 rounded-8 text-small font-medium
                  transition-regular text-left
                  ${showGlobalFunnelingReport 
                    ? 'text-accent bg-accent bg-opacity-10 border border-accent border-opacity-20' 
                    : 'text-text-tertiary hover:text-text-primary hover:bg-bg-secondary'
                  }
                `}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: navItems.length * 0.05 }}
              >
                <div className="font-medium mb-0.5">🔍 AI Agent Report</div>
                <div className="text-micro text-text-quaternary">
                  {showGlobalFunnelingReport ? 'Hide multi-agent process details' : 'Show how AI agents collaborate'}
                </div>
              </motion.button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
};

export default Navbar;
