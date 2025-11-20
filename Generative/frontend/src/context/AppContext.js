// context/AppContext.js
import React, { createContext, useContext, useReducer } from 'react';

// Initial state
const initialState = {
  user: {
    id: 'user-123',
    email: 'john.smith@example.com',
    fullName: 'John Smith',
    skills: '',
    expertise: 'Beginner'
  },
  analysisResult: null,
  isLoading: false,
  currentSkills: '',
  currentExpertise: 'Beginner',
  showGlobalFunnelingReport: false
};

// Action types
const actionTypes = {
  SET_LOADING: 'SET_LOADING',
  SET_ANALYSIS_RESULT: 'SET_ANALYSIS_RESULT',
  UPDATE_USER_SKILLS: 'UPDATE_USER_SKILLS',
  SET_CURRENT_SKILLS: 'SET_CURRENT_SKILLS',
  SET_CURRENT_EXPERTISE: 'SET_CURRENT_EXPERTISE',
  TOGGLE_FUNNELING_REPORT: 'TOGGLE_FUNNELING_REPORT'
};

// Reducer
const appReducer = (state, action) => {
  switch (action.type) {
    case actionTypes.SET_LOADING:
      return {
        ...state,
        isLoading: action.payload
      };
    case actionTypes.SET_ANALYSIS_RESULT:
      return {
        ...state,
        analysisResult: action.payload,
        isLoading: false
      };
    case actionTypes.UPDATE_USER_SKILLS:
      return {
        ...state,
        user: {
          ...state.user,
          skills: action.payload
        },
        currentSkills: action.payload
      };
    case actionTypes.SET_CURRENT_SKILLS:
      return {
        ...state,
        currentSkills: action.payload
      };
    case actionTypes.SET_CURRENT_EXPERTISE:
      return {
        ...state,
        currentExpertise: action.payload
      };
    case actionTypes.TOGGLE_FUNNELING_REPORT:
      return {
        ...state,
        showGlobalFunnelingReport: !state.showGlobalFunnelingReport
      };
    default:
      return state;
  }
};

// Create context
const AppContext = createContext();

// Context provider
export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  // Actions
  const setLoading = (isLoading) => {
    dispatch({ type: actionTypes.SET_LOADING, payload: isLoading });
  };

  const setAnalysisResult = (result) => {
    dispatch({ type: actionTypes.SET_ANALYSIS_RESULT, payload: result });
  };

  const updateUserSkills = (skills) => {
    dispatch({ type: actionTypes.UPDATE_USER_SKILLS, payload: skills });
  };

  const setCurrentSkills = (skills) => {
    dispatch({ type: actionTypes.SET_CURRENT_SKILLS, payload: skills });
  };

  const setCurrentExpertise = (expertise) => {
    dispatch({ type: actionTypes.SET_CURRENT_EXPERTISE, payload: expertise });
  };

  const toggleFunnelingReport = () => {
    dispatch({ type: actionTypes.TOGGLE_FUNNELING_REPORT });
  };

  const value = {
    ...state,
    setLoading,
    setAnalysisResult,
    updateUserSkills,
    setCurrentSkills,
    setCurrentExpertise,
    toggleFunnelingReport
  };

  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
};

// Custom hook to use the context
export const useAppContext = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  return context;
};