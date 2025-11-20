import React, { useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from "./components/Navbar";
import Landing from "./pages/Landing";
import CareerPath from "./pages/CareerPath";
import SimplifiedUltimateRoadmap from "./pages/UltimateRoadmap";
import Flowchart from "./pages/Flowchart";
import AgentInterface from "./components/AgentInterface";
import MultiAgentDemo from "./pages/MultiAgentDemo";
import { AppProvider } from "./context/AppContext";
import { ThemeProvider } from "./context/ThemeContext";

export default function App() {
  // Initialize Lenis smooth scroll
  useEffect(() => {
    let lenis;
    
    const initLenis = async () => {
      try {
        const Lenis = (await import('@studio-freight/lenis')).default;
        
        lenis = new Lenis({
          duration: 0.35,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          orientation: 'vertical',
          gestureOrientation: 'vertical',
          smoothWheel: true,
          wheelMultiplier: 1.0,
          smoothTouch: false,
          touchMultiplier: 1.5,
          infinite: false,
        });

        function raf(time) {
          lenis.raf(time);
          requestAnimationFrame(raf);
        }

        requestAnimationFrame(raf);
      } catch (error) {
        console.warn('Lenis smooth scroll not available:', error);
      }
    };

    initLenis();

    return () => {
      if (lenis) {
        lenis.destroy();
      }
    };
  }, []);

  return (
    <ThemeProvider>
      <AppProvider>
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/career-path" element={<CareerPath />} />
            <Route path="/simplified-ultimate-roadmap" element={<SimplifiedUltimateRoadmap />} />
            <Route path="/flowchart" element={<Flowchart />} />
            <Route path="/agents" element={<AgentInterface />} />
            <Route path="/multi-agent" element={<MultiAgentDemo />} />
          </Routes>
        </Router>
      </AppProvider>
    </ThemeProvider>
  );
}
