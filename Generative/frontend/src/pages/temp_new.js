import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppContext } from '../context/AppContext';
import { motion, AnimatePresence } from 'framer-motion';
import LinearButton from '../components/LinearButton';
import LinearCard from '../components/LinearCard';
import { categories, fieldsByCategory, domainsByField } from '../constants/careerData';

// Lazy load mind map component
import CareerMindMap from '../components/CareerMindMap';

// Animated Stat Component
const AnimatedStat = ({ stat, index, statsInView, setStatsInView }) => {
  const [displayValue, setDisplayValue] = useState(0);
  
  useEffect(() => {
    if (!statsInView || !stat.isNumber) return;
    
    const duration = 2000;
    const steps = 60;
    const increment = stat.value / steps;
    const stepDuration = duration / steps;
    let current = 0;
    
    const timer = setInterval(() => {
      current += increment;
      if (current >= stat.value) {
        setDisplayValue(stat.value);
        clearInterval(timer);
      } else {
        setDisplayValue(Math.floor(current));
      }
    }, stepDuration);
    
    return () => clearInterval(timer);
  }, [statsInView, stat.value, stat.isNumber]);
  
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-50px" }}
      onViewportEnter={() => setStatsInView(true)}
      transition={{ delay: index * 0.1, duration: 0.5 }}
      className="group"
    >
      <motion.div 
        className="text-title-4 font-semibold text-accent-hover mb-2"
        whileHover={{ scale: 1.05 }}
        transition={{ duration: 0.2 }}
      >
        {stat.isNumber ? `${displayValue}${stat.suffix}` : stat.value}
      </motion.div>
      <div className="text-regular text-text-tertiary group-hover:text-text-secondary transition-colors">
        {stat.label}
      </div>
    </motion.div>
  );
};

// Path maps for mind map nodes
const PATH_MAPS = {
  software: ['React', 'Node.js', 'API', 'System Design', 'Databases', 'DevOps'],
  data: ['Python', 'ML', 'Pandas', 'Data Viz', 'Neural Nets'],
  ux: ['Figma', 'Wireframes', 'Prototyping', 'User Flow', 'Typography'],
  marketing: ['SEO', 'Analytics', 'Branding', 'Growth', 'Campaigns']
};

// Map pattern to path key
const PATTERN_TO_PATH = {
  'code': 'software',
  'chart': 'data',
  'grid': 'ux',
  'trend': 'marketing'
};

const Landing = () => {
  const [activeTab, setActiveTab] = useState('categories');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedField, setSelectedField] = useState('');
  const [animationStage, setAnimationStage] = useState(0);
  const [activeCareerIndex, setActiveCareerIndex] = useState(0);
  const navigate = useNavigate();
  const { setCurrentSkills, setCurrentExpertise } = useAppContext();
  const heroRef = useRef(null);
  const carouselRef = useRef(null);

  // Simple hero fade effect for performance
  const [heroBlur, setHeroBlur] = useState(0);
  const [heroOpacity, setHeroOpacity] = useState(1);
  const [isHovered, setIsHovered] = useState(false);
  const [statsInView, setStatsInView] = useState(false);
  const [activeStep, setActiveStep] = useState(0);
  const [howItWorksScrollProgress, setHowItWorksScrollProgress] = useState(0);
  const howItWorksRef = useRef(null);

  // Career data (must be defined before useEffect that uses it)
  const popularCareers = [
    {
      title: 'Software Engineering',
      subtitle: 'Build the future with code',
      field: 'Software Engineering',
      icon: (
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
          <polyline points="16 18 22 12 16 6"/>
          <polyline points="8 6 2 12 8 18"/>
        </svg>
      ),
      pattern: 'code'
    },
    {
      title: 'Data Science',
      subtitle: 'Transform data into insights',
      field: 'Data Science',
      icon: (
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
          <line x1="12" y1="20" x2="12" y2="10"/>
          <line x1="18" y1="20" x2="18" y2="4"/>
          <line x1="6" y1="20" x2="6" y2="16"/>
        </svg>
      ),
      pattern: 'chart'
    },
    {
      title: 'UI/UX Design',
      subtitle: 'Craft beautiful experiences',
      field: 'User Experience Design',
      icon: (
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
          <rect x="3" y="3" width="7" height="7"/>
          <rect x="14" y="3" width="7" height="7"/>
          <rect x="14" y="14" width="7" height="7"/>
          <rect x="3" y="14" width="7" height="7"/>
        </svg>
      ),
      pattern: 'grid'
    },
    {
      title: 'Digital Marketing',
      subtitle: 'Grow brands strategically',
      field: 'Digital Marketing',
      icon: (
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
          <line x1="18" y1="20" x2="18" y2="10"/>
          <line x1="12" y1="20" x2="12" y2="4"/>
          <line x1="6" y1="20" x2="6" y2="14"/>
        </svg>
      ),
      pattern: 'trend'
    }
  ];

  // Staggered animation sequence
  useEffect(() => {
    const timers = [100, 200, 300, 400].map((delay, i) => 
      setTimeout(() => setAnimationStage(i + 1), delay)
    );
    return () => timers.forEach(clearTimeout);
  }, []);

  // Optimized scroll fade for hero (passive, requestAnimationFrame throttled)
  useEffect(() => {
    let ticking = false;
    const handleScroll = () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const scrollTop = window.scrollY;
          const triggerPoint = window.innerHeight * 0.2;
          const fadeRange = window.innerHeight * 0.35;
          
          const progress = Math.max(0, Math.min(1, (scrollTop - triggerPoint) / fadeRange));
          setHeroBlur(progress * 8);
          setHeroOpacity(Math.max(0.4, 1 - progress * 0.6));
          ticking = false;
        });
        ticking = true;
      }
    };
    
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Track carousel scroll position for indicator
  useEffect(() => {
    const carouselContainer = carouselRef.current;
    if (!carouselContainer) return;

    let ticking = false;
    const handleCarouselScroll = () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const scrollLeft = carouselContainer.scrollLeft;
          const scrollWidth = carouselContainer.scrollWidth - carouselContainer.clientWidth;
          const progress = scrollWidth > 0 ? scrollLeft / scrollWidth : 0;
          const index = Math.round(progress * (popularCareers.length - 1));
          setActiveCareerIndex(Math.min(index, popularCareers.length - 1));
          ticking = false;
        });
        ticking = true;
      }
    };

    carouselContainer.addEventListener('scroll', handleCarouselScroll, { passive: true });
    return () => carouselContainer.removeEventListener('scroll', handleCarouselScroll);
  }, [popularCareers.length]);
