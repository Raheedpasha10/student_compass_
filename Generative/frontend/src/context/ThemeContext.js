import React, { createContext, useContext, useEffect } from 'react';

const ThemeContext = createContext();

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};

export const ThemeProvider = ({ children }) => {
  // Always dark mode - no switching
  const isDark = true;
  const theme = 'dark';

  // Apply dark theme to document body on mount
  useEffect(() => {
    document.body.classList.add('dark');
    document.body.classList.remove('light');
  }, []);

  const value = {
    isDark,
    theme
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};