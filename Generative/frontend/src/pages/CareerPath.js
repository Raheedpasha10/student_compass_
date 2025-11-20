import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppContext } from '../context/AppContext';
import { motion, AnimatePresence } from 'framer-motion';
import LinearButton from '../components/LinearButton';
import LinearCard from '../components/LinearCard';

const CareerPath = () => {
  const navigate = useNavigate();
  const { currentSkills, setCurrentSkills, setCurrentExpertise } = useAppContext();
  const [selectedCareer, setSelectedCareer] = useState(null);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  // Career data structure
  const careerPaths = {
    'Artificial Intelligence': {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="4" y="2" width="16" height="20" rx="2" ry="2"/>
          <line x1="9" y1="6" x2="15" y2="6"/>
          <line x1="9" y1="10" x2="15" y2="10"/>
          <line x1="9" y1="14" x2="13" y2="14"/>
          <circle cx="17" cy="18" r="2"/>
        </svg>
      ),
      description: 'Build intelligent systems that learn and adapt',
      averageSalary: '₹8,00,000 - ₹20,00,000',
      growthRate: '+43%',
      demandLevel: 'Extremely High',
      trending: true,
      specializations: [
        { name: 'Machine Learning Engineering', difficulty: 'Expert', timeToMaster: '24-36 months' },
        { name: 'Computer Vision', difficulty: 'Expert', timeToMaster: '20-30 months' },
        { name: 'Natural Language Processing', difficulty: 'Expert', timeToMaster: '24-30 months' },
        { name: 'AI Research', difficulty: 'Expert', timeToMaster: '36-48 months' }
      ],
      skills: ['Deep Learning', 'Python/PyTorch', 'Neural Networks', 'Research'],
      companies: ['TCS', 'Infosys', 'Wipro', 'Accenture', 'Microsoft India'],
      dayInLife: [
        '9:00 AM - Research paper review and model architecture design',
        '11:00 AM - Training and fine-tuning AI models',
        '1:00 PM - Data preprocessing and feature engineering',
        '3:00 PM - Model evaluation and performance optimization',
        '5:00 PM - Documentation and research collaboration'
      ]
    },
    'Blockchain Technology': {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="3" y="3" width="7" height="7" rx="1"/>
          <rect x="14" y="3" width="7" height="7" rx="1"/>
          <rect x="14" y="14" width="7" height="7" rx="1"/>
          <rect x="3" y="14" width="7" height="7" rx="1"/>
          <path d="M10 6.5h4M10 17.5h4M6.5 10v4M17.5 10v4"/>
        </svg>
      ),
      description: 'Build decentralized systems and smart contracts',
      averageSalary: '₹6,00,000 - ₹15,00,000',
      growthRate: '+67%',
      demandLevel: 'Very High',
      trending: true,
      specializations: [
        { name: 'Smart Contract Development', difficulty: 'Advanced', timeToMaster: '18-24 months' },
        { name: 'DeFi Development', difficulty: 'Expert', timeToMaster: '24-30 months' },
        { name: 'Blockchain Security', difficulty: 'Expert', timeToMaster: '20-28 months' },
        { name: 'NFT Development', difficulty: 'Intermediate', timeToMaster: '12-18 months' }
      ],
      skills: ['Solidity', 'Web3', 'Cryptography', 'Distributed Systems'],
      companies: ['CoinDCX', 'WazirX', 'ZebPay', 'Unocoin', 'Bitbns'],
      dayInLife: [
        '9:00 AM - Smart contract architecture design',
        '11:00 AM - Coding and testing blockchain applications',
        '1:00 PM - Security audits and testing',
        '3:00 PM - Community collaboration and research',
        '5:00 PM - Documentation and deployment'
      ]
    },
    'Cloud Computing': {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>
        </svg>
      ),
      description: 'Build and manage scalable cloud infrastructure',
      averageSalary: '₹5,00,000 - ₹14,00,000',
      growthRate: '+29%',
      demandLevel: 'Very High',
      trending: true,
      specializations: [
        { name: 'AWS Solutions Architecture', difficulty: 'Advanced', timeToMaster: '15-20 months' },
        { name: 'Azure Engineering', difficulty: 'Advanced', timeToMaster: '15-20 months' },
        { name: 'Google Cloud Platform', difficulty: 'Advanced', timeToMaster: '15-20 months' },
        { name: 'Multi-Cloud Strategy', difficulty: 'Expert', timeToMaster: '24-30 months' }
      ],
      skills: ['Cloud Architecture', 'Containerization', 'Microservices', 'Infrastructure as Code'],
      companies: ['Amazon India', 'Microsoft India', 'Google India', 'IBM India', 'Oracle India'],
      dayInLife: [
        '9:00 AM - Infrastructure monitoring and optimization',
        '11:00 AM - Cloud architecture design sessions',
        '1:00 PM - Cost optimization and resource management',
        '3:00 PM - Security compliance and governance',
        '5:00 PM - Team mentoring and knowledge sharing'
      ]
    },
    'Software Engineering': {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
          <line x1="8" y1="21" x2="16" y2="21"/>
          <line x1="12" y1="17" x2="12" y2="21"/>
        </svg>
      ),
      description: 'Build the digital future with cutting-edge technology',
      averageSalary: '₹4,00,000 - ₹18,00,000',
      growthRate: '+22%',
      demandLevel: 'Very High',
      specializations: [
        { name: 'Full-Stack Development', difficulty: 'Intermediate', timeToMaster: '12-18 months' },
        { name: 'DevOps Engineering', difficulty: 'Advanced', timeToMaster: '18-24 months' },
        { name: 'Mobile Development', difficulty: 'Intermediate', timeToMaster: '10-15 months' },
        { name: 'AI/ML Engineering', difficulty: 'Expert', timeToMaster: '24-36 months' }
      ],
      skills: ['Programming', 'Problem Solving', 'System Design', 'Debugging'],
      companies: ['TCS', 'Infosys', 'Wipro', 'Tech Mahindra', 'HCL'],
      dayInLife: [
        '9:00 AM - Review code and plan daily tasks',
        '10:00 AM - Collaborate with team on new features',
        '12:00 PM - Development and coding',
        '3:00 PM - Code reviews and testing',
        '5:00 PM - Documentation and planning tomorrow'
      ]
    },
    'Web Development': {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <circle cx="12" cy="12" r="10"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
      ),
      description: 'Create dynamic websites and web applications',
      averageSalary: '₹3,00,000 - ₹10,00,000',
      growthRate: '+15%',
      demandLevel: 'High',
      specializations: [
        { name: 'Frontend Development', difficulty: 'Intermediate', timeToMaster: '10-15 months' },
        { name: 'Backend Development', difficulty: 'Intermediate', timeToMaster: '12-18 months' },
        { name: 'Full-Stack Development', difficulty: 'Advanced', timeToMaster: '18-24 months' },
        { name: 'Progressive Web Apps', difficulty: 'Advanced', timeToMaster: '15-20 months' }
      ],
      skills: ['HTML/CSS/JavaScript', 'React/Vue/Angular', 'Node.js', 'Database Design'],
      companies: ['Zoho', 'Freshworks', 'Postman', 'Hasura', 'Druva'],
      dayInLife: [
        '9:00 AM - Design review and wireframe analysis',
        '11:00 AM - Frontend component development',
        '1:00 PM - API integration and backend work',
        '3:00 PM - Testing and debugging',
        '5:00 PM - Performance optimization and deployment'
      ]
    },
    'Mobile Development': {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="5" y="2" width="14" height="20" rx="2" ry="2"/>
          <line x1="12" y1="18" x2="12.01" y2="18"/>
        </svg>
      ),
      description: 'Build native and cross-platform mobile applications',
      averageSalary: '₹4,00,000 - ₹12,00,000',
      growthRate: '+19%',
      demandLevel: 'High',
      specializations: [
        { name: 'iOS Development', difficulty: 'Intermediate', timeToMaster: '12-18 months' },
        { name: 'Android Development', difficulty: 'Intermediate', timeToMaster: '12-18 months' },
        { name: 'React Native', difficulty: 'Intermediate', timeToMaster: '10-15 months' },
        { name: 'Flutter Development', difficulty: 'Intermediate', timeToMaster: '10-15 months' }
      ],
      skills: ['Swift/Kotlin', 'React Native/Flutter', 'UI/UX Design', 'Mobile Architecture'],
      companies: ['OLA', 'Swiggy', 'Zomato', 'BYJUS', 'Hotstar'],
      dayInLife: [
        '9:00 AM - App performance monitoring and bug fixes',
        '11:00 AM - Feature development and UI implementation',
        '1:00 PM - Testing on multiple devices',
        '3:00 PM - App store optimization and deployment',
        '5:00 PM - User feedback analysis and planning'
      ]
    }
  };

  const handleCareerSelect = (careerName) => {
    setSelectedCareer(selectedCareer === careerName ? null : careerName);
  };

  const startLearningJourney = (careerName) => {
    setCurrentSkills(careerName);
    setCurrentExpertise('Beginner');
    navigate('/simplified-ultimate-roadmap');
  };

  const selectedData = selectedCareer ? careerPaths[selectedCareer] : null;

  return (
    <div className="min-h-screen bg-bg-primary text-text-primary pt-16">
      {/* Header */}
      <section className="py-16 border-b border-border-primary">
        <div className="linear-container">
          <div className="max-w-3xl">
            {currentSkills && (
              <motion.div 
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="mb-4"
              >
                <span 
                  className="inline-flex items-center gap-2 px-2 py-1 rounded-6 text-micro font-medium"
                  style={{ 
                    background: 'rgba(113, 112, 255, 0.15)',
                    color: 'var(--color-accent-hover)',
                  }}
                >
                  <span className="w-1.5 h-1.5 rounded-full bg-accent-hover"></span>
                  Current path: {currentSkills}
                </span>
              </motion.div>
            )}

            <h1 className="text-title-5 font-semibold mb-4" style={{ letterSpacing: '-.022em', lineHeight: '1.1' }}>
              Explore career paths
            </h1>
            <p className="text-large text-text-secondary" style={{ lineHeight: '1.6' }}>
              Discover high-demand careers with real salary data, growth projections, and personalized learning paths.
            </p>
          </div>
        </div>
      </section>

      {/* Career List */}
      <section className="py-8">
        <div className="linear-container">
          <div className="max-w-5xl">
            {Object.entries(careerPaths).map(([careerName, career], index) => (
              <motion.div
                key={careerName}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.03, duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
              >
                <LinearCard
                  onClick={() => handleCareerSelect(careerName)}
                  className="mb-3 cursor-pointer"
                >
                  <div className="p-6">
                    <div className="flex items-start gap-4">
                      <motion.div 
                        className="text-text-primary flex-shrink-0"
                        style={{ color: 'var(--color-accent-hover)' }}
                        whileHover={{ scale: 1.1, rotate: 5 }}
                        transition={{ duration: 0.2, ease: [0.25, 0.46, 0.45, 0.94] }}
                      >
                        {career.icon}
                      </motion.div>
                      <div className="flex-grow">
                        <div className="flex items-start justify-between mb-2">
                          <div>
                            <h3 className="text-regular font-semibold text-text-primary mb-1">
                              {careerName}
                            </h3>
                            <p className="text-small text-text-tertiary mb-3">
                              {career.description}
                            </p>
                          </div>
                          <motion.svg 
                            width="20" 
                            height="20" 
                            viewBox="0 0 24 24" 
                            fill="none" 
                            stroke="currentColor" 
                            strokeWidth="2" 
                            className="text-text-quaternary flex-shrink-0 ml-4"
                            animate={{ rotate: selectedCareer === careerName ? 180 : 0 }}
                            transition={{ duration: 0.16, ease: [0.25, 0.46, 0.45, 0.94] }}
                          >
                            <path d="m6 9 6 6 6-6" />
                          </motion.svg>
                        </div>

                        <div className="flex flex-wrap gap-3 text-micro">
                          <span className="text-text-tertiary">
                            <span className="text-text-secondary font-medium">{career.averageSalary}</span> salary
                          </span>
                          <span className="text-border-tertiary">•</span>
                          <span className="text-text-tertiary">
                            <span className="text-accent-hover font-medium">{career.growthRate}</span> growth
                          </span>
                          <span className="text-border-tertiary">•</span>
                          <span className="text-text-tertiary">
                            <span className="text-text-secondary font-medium">{career.demandLevel}</span> demand
                          </span>
                        </div>
                      </div>
                    </div>

                    {/* Expanded Details */}
                    <AnimatePresence>
                      {selectedCareer === careerName && (
                        <motion.div
                          initial={{ opacity: 0, height: 0 }}
                          animate={{ opacity: 1, height: 'auto' }}
                          exit={{ opacity: 0, height: 0 }}
                          transition={{ duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
                          className="mt-6 pt-6 border-t border-border-translucent"
                        >
                          <motion.div
                            initial={{ y: -10, opacity: 0 }}
                            animate={{ y: 0, opacity: 1 }}
                            transition={{ duration: 0.3, delay: 0.1 }}
                          >
                          {/* Specializations */}
                          <div className="mb-6">
                            <h4 className="text-small font-semibold text-text-primary mb-3">Specializations</h4>
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                              {selectedData.specializations.map((spec, i) => (
                                <div 
                                  key={i}
                                  className="p-3 rounded-6 border border-border-translucent"
                                  style={{ background: 'rgba(255, 255, 255, 0.02)' }}
                                >
                                  <div className="text-small font-medium text-text-primary">{spec.name}</div>
                                  <div className="text-micro text-text-tertiary mt-1">
                                    {spec.difficulty} • {spec.timeToMaster}
                                  </div>
                                </div>
                              ))}
                            </div>
                          </div>

                          {/* Skills */}
                          <div className="mb-6">
                            <h4 className="text-small font-semibold text-text-primary mb-3">Key Skills</h4>
                            <div className="flex flex-wrap gap-2">
                              {selectedData.skills.map((skill, i) => (
                                <span 
                                  key={i}
                                  className="px-2 py-1 rounded-6 text-micro font-medium"
                                  style={{ 
                                    background: 'rgba(255, 255, 255, 0.05)',
                                    color: 'var(--color-text-secondary)'
                                  }}
                                >
                                  {skill}
                                </span>
                              ))}
                            </div>
                          </div>

                          {/* Companies */}
                          <div className="mb-6">
                            <h4 className="text-small font-semibold text-text-primary mb-3">Top Companies</h4>
                            <div className="flex flex-wrap gap-2">
                              {selectedData.companies.map((company, i) => (
                                <span 
                                  key={i}
                                  className="text-small text-text-tertiary"
                                >
                                  {company}{i < selectedData.companies.length - 1 ? ',' : ''}
                                </span>
                              ))}
                            </div>
                          </div>

                          {/* CTA */}
                          <motion.div 
                            className="pt-4"
                            initial={{ y: 10, opacity: 0 }}
                            animate={{ y: 0, opacity: 1 }}
                            transition={{ duration: 0.3, delay: 0.2 }}
                          >
                            <LinearButton
                              variant="primary"
                              size="default"
                              onClick={() => startLearningJourney(careerName)}
                            >
                              Start learning path →
                            </LinearButton>
                          </motion.div>
                          </motion.div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                </LinearCard>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default CareerPath;
