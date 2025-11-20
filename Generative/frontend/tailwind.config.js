/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Linear Brand Colors
        brand: {
          DEFAULT: '#5e6ad2',
          hover: '#828fff',
        },
        accent: {
          DEFAULT: '#7170ff',
          hover: '#828fff',
        },
        // Background Colors
        bg: {
          primary: '#08090a',
          secondary: '#1c1c1f',
          tertiary: '#232326',
          quaternary: '#28282c',
          marketing: '#010102',
          translucent: 'rgba(255, 255, 255, 0.05)',
        },
        // Border Colors
        border: {
          primary: '#23252a',
          secondary: '#34343a',
          tertiary: '#3e3e44',
          translucent: 'rgba(255, 255, 255, 0.05)',
        },
        // Text Colors
        text: {
          primary: '#f7f8f8',
          secondary: '#d0d6e0',
          tertiary: '#8a8f98',
          quaternary: '#62666d',
        },
        // Link Colors
        link: {
          primary: '#828fff',
          hover: '#ffffff',
        },
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      fontWeight: {
        light: '300',
        normal: '400',
        medium: '510',
        semibold: '590',
        bold: '680',
      },
      fontSize: {
        'micro': '.75rem',
        'mini': '.8125rem',
        'small': '.875rem',
        'regular': '.9375rem',
        'large': '1.0625rem',
        'title-1': '1.0625rem',
        'title-2': '1.3125rem',
        'title-3': '1.5rem',
        'title-4': '2rem',
        'title-5': '2.5rem',
        'title-6': '3rem',
        'title-7': '3.5rem',
        'title-8': '4rem',
        'title-9': '4.5rem',
      },
      lineHeight: {
        'tight': '1.1',
        'snug': '1.33',
        'normal': '1.6',
      },
      letterSpacing: {
        'tight': '-.022em',
        'normal': '-.012em',
        'wide': '0',
      },
      borderRadius: {
        '4': '4px',
        '6': '6px',
        '8': '8px',
        '10': '10px',
        '12': '12px',
        '16': '16px',
        'full': '9999px',
      },
      boxShadow: {
        'linear-low': '0px 2px 4px rgba(0, 0, 0, .1)',
        'linear-medium': '0px 4px 24px rgba(0, 0, 0, .2)',
        'linear-high': '0px 7px 32px rgba(0, 0, 0, .35)',
        'none': '0px 0px 0px transparent',
      },
      transitionDuration: {
        'quick': '.1s',
        'regular': '.16s',
        'slow': '.25s',
      },
      transitionTimingFunction: {
        'out-quad': 'cubic-bezier(.25, .46, .45, .94)',
        'out-cubic': 'cubic-bezier(.215, .61, .355, 1)',
        'out-quart': 'cubic-bezier(.165, .84, .44, 1)',
        'in-out-quad': 'cubic-bezier(.455, .03, .515, .955)',
      },
      backdropBlur: {
        'header': '20px',
      },
      animation: {
        'fade-in': 'fadeIn 0.3s cubic-bezier(.25, .46, .45, .94)',
        'scale-in': 'scaleIn 0.16s cubic-bezier(.25, .46, .45, .94)',
        'slide-up': 'slideUp 0.4s cubic-bezier(.165, .84, .44, 1)',
      },
      keyframes: {
        fadeIn: {
          'from': { opacity: '0', transform: 'translateY(10px)' },
          'to': { opacity: '1', transform: 'translateY(0)' }
        },
        scaleIn: {
          'from': { opacity: '0', transform: 'scale(.98)' },
          'to': { opacity: '1', transform: 'scale(1)' }
        },
        slideUp: {
          'from': { opacity: '0', transform: 'translateY(20px)' },
          'to': { opacity: '1', transform: 'translateY(0)' }
        },
      },
    },
  },
  plugins: [],
}
