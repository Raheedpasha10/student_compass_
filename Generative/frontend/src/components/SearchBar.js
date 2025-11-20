import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppContext } from '../context/AppContext';
import { motion, AnimatePresence } from 'framer-motion';
import { quickSelectDomains } from '../constants/careerData';

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [showSuggestions, setShowSuggestions] = useState(false);
  const navigate = useNavigate();
  const { setCurrentSkills, setCurrentExpertise } = useAppContext();

  const handleSearch = (field) => {
    setCurrentSkills(field);
    setCurrentExpertise('Beginner');
    setSearchTerm('');
    setShowSuggestions(false);
    navigate('/simplified-ultimate-roadmap');
  };

  const filteredSuggestions = quickSelectDomains.filter(item =>
    item.field.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="relative w-full md:w-64">
      <div className="relative">
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => {
            setSearchTerm(e.target.value);
            setShowSuggestions(true);
          }}
          onFocus={() => setShowSuggestions(true)}
          onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
          placeholder="Search careers..."
          className="w-full h-10 px-3 pr-10 rounded-8
            bg-bg-secondary border border-border-primary
            text-text-primary text-small
            placeholder-text-quaternary
            transition-regular ease-out-quad
            focus:outline-none focus:border-accent"
          style={{
            transitionProperty: 'border-color, background-color',
            transitionDuration: '.16s',
            transitionTimingFunction: 'cubic-bezier(.25, .46, .45, .94)',
          }}
        />
        <motion.div
          className="absolute right-3 top-1/2 -translate-y-1/2 text-text-quaternary"
          whileHover={{ scale: 1.1 }}
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
        </motion.div>
      </div>

      {/* Suggestions Dropdown */}
      <AnimatePresence>
        {showSuggestions && searchTerm && filteredSuggestions.length > 0 && (
          <motion.div
            initial={{ opacity: 0, scale: 0.98, y: -10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.98, y: -10 }}
            transition={{ duration: 0.16, ease: [0.25, 0.46, 0.45, 0.94] }}
            className="absolute top-full mt-2 w-full rounded-8 overflow-hidden shadow-linear-medium z-50"
            style={{
              backdropFilter: 'blur(20px)',
              WebkitBackdropFilter: 'blur(20px)',
              background: 'rgba(28, 28, 31, 0.95)',
              border: '0.5px solid rgba(255, 255, 255, 0.08)',
            }}
          >
            <div className="max-h-64 overflow-y-auto">
              {filteredSuggestions.slice(0, 8).map((item, index) => (
                <motion.button
                  key={index}
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: index * 0.03 }}
                  onClick={() => handleSearch(item.field)}
                  className="w-full px-3 py-2.5 text-left text-small
                    text-text-secondary hover:text-text-primary
                    hover:bg-bg-translucent
                    transition-regular ease-out-quad
                    border-b border-border-translucent last:border-0"
                  style={{
                    transitionProperty: 'background-color, color',
                    transitionDuration: '.16s',
                  }}
                >
                  <div>
                    <div className="font-medium">{item.field}</div>
                    {item.description && (
                      <div className="text-micro text-text-tertiary mt-0.5">{item.description}</div>
                    )}
                  </div>
                </motion.button>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default SearchBar;
