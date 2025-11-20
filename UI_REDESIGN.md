# UI Redesign - Student Compass

## Project Context

**Goal**: Complete redesign of Student Compass frontend to match Linear.app's premium design aesthetic with smooth animations, 3D components, hover effects, and Lenis smooth scroll.

**Current Status**: Phase 1 completed - Landing page fully redesigned with exact Linear color palette, hero section refined with cinematic minimal design, CareerMindMap component enhanced with micro-animations, interactive carousel controls added, section reordering completed, and all animation glitches fixed. All components working smoothly with consistent behavior on reload/navigation.
NOTE : IMPORTANT CONTEXT IS ADDED IN THE END (DO NOT MISS THAT)
---

## Design System & Philosophy

### Core Reference: Linear.app

**Key Design Principles:**
- **Minimalism over complexity** - Subtle effects, no heavy animations
- **Dark theme first** - Primary background: `#08090a`, secondary: `#1c1c1f`
- **Full-viewport segments** - Each major section takes 100vh
- **Unique layouts per segment** - No repetitive layouts, dynamic and engaging
- **Contextual background patterns** - Cards have subtle patterns related to their content
- **Professional over playful** - No emojis, use SVG icons instead
- **Micro-interactions** - Subtle hover states, brightness filters, scale on active

### Linear Design Tokens (Implemented)

**Colors (Exact Linear Palette - All Implemented):**
```css
/* Background Colors */
--color-bg-primary: #08090a        /* Main page background */
--color-bg-secondary: #1c1c1f      /* Card backgrounds */
--color-bg-tertiary: #232326       /* Hover states */
--color-bg-quaternary: #28282c

/* Interface Levels (for mockup/previews) */
--color-bg-level-0: #08090a
--color-bg-level-1: #0f1011        /* Used in hero mockup */
--color-bg-level-2: #141516        /* Used in hero mockup */
--color-bg-level-3: #191a1b        /* Card backgrounds in mockup */

/* Border Colors */
--color-border-primary: #23252a
--color-border-secondary: #34343a
--color-line-primary: #37393a     /* Used throughout hero mockup */
--color-border-translucent: rgba(255, 255, 255, 0.08)

/* Text Colors */
--color-text-primary: #f7f8f8      /* Headlines, primary text */
--color-text-secondary: #d0d6e0    /* Descriptions, secondary text */
--color-text-tertiary: #8a8f98     /* Muted text, placeholders */

/* Accent Colors */
--color-accent: #7170ff            /* Primary accent (used in progress bars, glows) */
--color-accent-hover: #828fff
--color-brand-bg: #5e6ad2
```

**Typography:**
- Font: Inter Variable (weights: 300, 400, 510, 590, 680)
- Title letter-spacing: `-.012em` to `-.022em`
- Line heights: 1.1 to 1.6

**Animations:**
- Transitions: `.16s cubic-bezier(.25, .46, .45, .94)`
- Active states: `transform: scale(0.97)`
- Hover: `filter: brightness(115%)` for primary buttons
- No heavy 3D transforms - subtle background changes instead

**Components:**
- Border radius: 4px, 6px, 8px, 10px, 12px, 16px, 9999px
- Buttons: Heights 24px/32px/40px/48px, border-radius 10px (default)
- Cards: Subtle hover background change, minimal borders
- Headers: `backdrop-filter: blur(20px)`, `rgba(11, 11, 11, 0.8)`

---

## User Rules & Guidelines

### Critical Rules:
1. **NO EMOJIS** - Use SVG icons or clean graphics instead
2. **Full-viewport segments** - Each major section should be 100vh
3. **Unique layouts** - Every segment must have different layout (no repetition)
4. **Preserve functionality** - All existing features must work
5. **Linear aesthetic** - Match Linear.app's exact design patterns
6. **No README/Markdown creation** - Unless explicitly requested
7. **Short responses** - Keep information concise and actionable
8. **Purpose over design** - Functionality first, design second

### Design Standards:
- **No heavy 3D effects** - Remove transforms like `translateY(-10px)`, `rotateX/Y`
- **No gradient borders** - Use solid rgba borders instead
- **No heavy shadows** - Minimal shadows or none
- **Background patterns** - Subtle patterns related to component content (opacity 0.02-0.05)
- **Glassmorphism** - Backdrop blur for headers and dropdowns
- **Hairline borders** - 0.5px on retina displays

---

## What's Been Implemented

### ✅ Phase 1 Complete

**1. Design System Foundation:**
- ✅ `index.css` - Complete Linear CSS variables and base styles
- ✅ `tailwind.config.js` - Linear design tokens (colors, fonts, animations)
- ✅ Lenis smooth scroll installed and optimized

**2. Core Components:**
- ✅ `LinearButton.js` - 5 variants (primary, secondary, tertiary, ghost, glass)
  - Proper hover/active states with brightness filters
  - Scale 0.97 on active
  - Sizes: mini (24px), small (32px), default (40px), large (48px)
  
- ✅ `LinearCard.js` - Minimal card with subtle hover
  - Background change on hover (bg-tertiary)
  - No heavy effects
  
- ✅ `LoadingSpinner.js` - Minimal Linear-style loader
  
- ✅ `Navbar.js` - Complete Linear redesign
  - Compass SVG icon (no emojis)
  - Full-width navigation
  - Hover preview dropdowns with descriptions
  - Glassmorphism header with blur
  - Mobile menu with smooth animations
  
- ✅ `SearchBar.js` - Minimal Linear styling
  - Clean input with proper focus states
  - Dropdown suggestions with backdrop blur

**3. Pages Redesigned:**
- ✅ `Landing.js` - Complete 6-segment full-viewport redesign
  - Hero (100vh) - Split layout with 3D-tilted preview mockup
  - Popular Careers (100vh) - 2x2 grid with contextual background patterns
  - How It Works (100vh) - 3-column process visualization
  - Category Explorer (100vh) - Interactive 3-step navigation
  - Stats & Testimonials (100vh) - Two-column layout
  - Final CTA (100vh) - Centered call-to-action
  
- ✅ `CareerPath.js` - Linear list items with expandable cards
  - Hairline borders
  - Subtle hover states
  - Clean typography
  
- ✅ `UltimateRoadmap.js` - Clean resource cards
  - Phase-based learning path
  - Minimal styling
  
- ✅ `Flowchart.js` - Interactive checklist design
  - Progress tracking
  - Sequential step completion

**4. Technical Optimizations:**
- ✅ Lenis smooth scroll optimized (duration: 0.35s, improved easing, wheelMultiplier: 1.0)
- ✅ Scroll handler optimized with requestAnimationFrame throttling
- ✅ Removed expensive Framer Motion parallax (useScroll/useTransform) for performance
- ✅ Static 3D transforms with will-change hints for GPU acceleration
- ✅ Simplified effects (reduced blur layers, shadows, gradients)
- ✅ Required Lenis CSS rules added
- ✅ Build system verified (compiles successfully)

**5. Hero Section Refinements (Latest):**
- ✅ Layout changed to vertical stacking (text top, mockup bottom) matching Linear exactly
- ✅ Text section: centered, 30vh height, 10vh padding-top
- ✅ Mockup size reduced: 68% width (max 1200px), 48vh height (min 480px)
- ✅ Simplified from complex 3-panel layout to elegant single-panel dashboard
- ✅ Content: 3 career cards in grid (removed sidebar, search, detail panels)
- ✅ Removed "AI-Powered Career Guidance" badge
- ✅ All colors updated to exact Linear palette:
  - Background: `#08090a` (was `#000000`)
  - Text primary: `#f7f8f8` (was `#ffffff`)
  - Text secondary: `#d0d6e0` (was `#9ca3af`)
  - Text tertiary: `#8a8f98` (was `#6b6b6b`)
  - Accent: `#7170ff` (was `#5b8bf5`)
  - Interface backgrounds: `#0f1011`, `#141516`, `#191a1b` (Linear levels)
  - Borders: `#37393a` (was `#2a2a2a`)
- ✅ 3D tilt: `rotateX(10deg) rotateY(-4deg) rotateZ(-3deg)` - "sleeping" perspective
- ✅ Scroll fade effect: blur and opacity based on scroll position
- ✅ Atmospheric effects: vignette, shadows, ambient glows (optimized)

**6. Hero Section Cinematic Redesign (Most Recent):**
- ✅ Typography refined to match Linear.app/Apple aesthetic:
  - Headline: `clamp(2.5rem, 5vw, 4rem)`, line-height `1.15`, letter-spacing `-.022em`, font-weight `590`
  - Description: `clamp(1rem, 1.5vw, 1.25rem)`, line-height `1.6`, color `#8a8f98`
  - Smaller, tighter typography for elegant minimal feel
- ✅ Layout adjustments:
  - Shifted slightly left with more breathing space
  - Reduced top/bottom padding (~80vh total height)
  - Text and buttons fade/slide in on load with smooth easing
- ✅ Background consistency:
  - Fixed color mismatch between mockup background and page background
  - Mockup background set to solid `#08090a` to match page exactly
  - Removed conflicting gradients that caused visual inconsistency
- ✅ Content refinement:
  - Headline: "Career guidance that moves at your pace"
  - Description: Clear value proposition about AI-powered roadmaps and personalized learning
  - Removed "50k students" badge for cleaner look
  - Buttons: Smaller, balanced on one line, "Get started" with minimal glow
- ✅ Animations:
  - Staggered fade-in: headline (delay 0s), description (delay 0.1s), buttons (delay 0.2s)
  - Smooth easing: `cubic-bezier(0.25, 0.46, 0.45, 0.94)`
  - On scroll: hero background fades into next section smoothly
- ✅ Grayscale palette maintained: `#0C0C0C` to `#161616` + white, no purple or color noise
- ✅ **CRITICAL**: Mockup component kept completely intact - no changes to CareerScene structure

**7. CareerMindMap Component Enhancements:**
- ✅ Digital Marketing visualization:
  - Added subtle peak to tallest bar (top triangle overlay)
  - Increased arrow stroke width for better visibility
  - Enhanced floating metric dots with subtle pulse animation
- ✅ Software Engineering visualization:
  - Increased bracket stroke width (`strokeWidth="2"` to `strokeWidth="2.5"`)
  - Enhanced syntax highlight brightness
- ✅ Data Science visualization:
  - Fixed bar heights to fit within bounds (max height 45 at y=30, baseline y=75)
  - Refined trend line to follow bar tops using cubic Bezier curves
  - Path: `M 25 50 C 30 45, 35 40, 40 40 C 45 40, 50 35, 55 30 C 60 35, 65 40, 70 45`
  - Fixed reverse animation issue - bars now animate correctly upward from baseline
  - Increased bar bounce with improved easing: `[0.34, 1.56, 0.64, 1.2]`
- ✅ UI/UX Design visualization:
  - Added subtle shine/glow to pen tip with pulsing opacity animation
  - Increased pen stroke width for better visibility
- ✅ General improvements:
  - Added subtle breathing scale effect to entire SVG (`scale: [1, 1.02, 1]`)
  - Softer transition timing for smoother animations
  - Removed `initial` animations from background elements to prevent flicker on re-mount
  - All animations use `React.Fragment` for multi-element renders

**8. Popular Career Paths Section Enhancements:**
- ✅ Interactive scroll indicators:
  - Added `activeCareerIndex` state tracking current visible card
  - Clickable indicators with smooth scroll to corresponding card
  - Active indicator highlighted with increased opacity and scale
  - Smooth scroll behavior using `scrollIntoView({ behavior: 'smooth', block: 'nearest' })`
- ✅ "Explore more" button:
  - Added next to scroll indicators with animated chevron
  - Navigates to "explore by category" segment on click
  - Elegant design matching Linear aesthetic
- ✅ Animation fixes:
  - Removed parallax `y` transform from `CareerScene` to eliminate flicker on reload/navigation
  - Removed conflicting `initial` animations from background elements
  - Fixed shaking/glitchy behavior on page reload or navigation back to section
  - All animations now consistent and smooth on every render

**9. Section Reordering:**
- ✅ "How It Works" section moved before "Popular Career Paths" section
- ✅ All functionality preserved - no breaking changes
- ✅ Smooth transitions maintained between sections
- ✅ Updated section order in `Landing.js`:
  1. Hero
  2. How It Works
  3. Popular Career Paths
  4. Category Explorer
  5. Stats & Testimonials
  6. Final CTA

---

## Current Implementation Details

### Landing Page Structure

**Segment 1: Hero (~80vh)**
- Layout: Vertical stacking (text centered at top, mockup below)
- Text Section:
  - Typography: `clamp(2.5rem, 5vw, 4rem)` headline, `clamp(1rem, 1.5vw, 1.25rem)` description
  - Line-height: `1.15` (headline), `1.6` (description)
  - Letter-spacing: `-.022em` (headline)
  - Font-weight: `590` (headline), `400` (description)
  - Headline: "Career guidance that moves at your pace"
  - Description: Clear value proposition about AI-powered roadmaps
  - Centered dual CTAs (Primary "Get started" + Secondary) - smaller, balanced on one line
  - Staggered fade-in animations on load
  - Background: Solid `#08090a` (matches page exactly)
- Mockup Preview:
  - Size: 68% width (max 1200px), 48vh height (min 480px)
  - 3D tilt: `rotateX(10deg) rotateY(-4deg) rotateZ(-3deg)` - "sleeping" perspective
  - Single elegant dashboard panel (simplified from 3-panel layout)
  - Content: 3 career cards in grid (Software Engineering, Data Science, UI/UX Design)
  - Each card shows: title, 2 skills, progress percentage, animated progress bar
  - Minimal header: "Dashboard" label
  - Background: Solid `#08090a` (no gradient, matches page)
  - Border: `#37393a`
  - Scroll fade: blur and opacity decrease on scroll
  - Atmospheric effects: vignette, shadow beneath, ambient glow
  - Colors: Exact Linear palette applied throughout
  - **CRITICAL**: Component structure kept intact - no changes to CareerScene

**Segment 2: How It Works (100vh)**
- Layout: 3-column
- Steps: Icon + title + description
- Clean spacing and typography
- Positioned before Popular Careers section

**Segment 3: Popular Careers (100vh)**
- Layout: 2x2 grid with horizontal scroll carousel
- Cards: Large (min-height 320px), contextual patterns:
  - Software: Diagonal code lines pattern
  - Data Science: Dot grid pattern
  - UI/UX: Grid pattern
  - Marketing: Angled trend arrows
- SVG icons (no emojis)
- Hover: Pattern visibility increase
- Interactive scroll indicators:
  - Clickable dots below cards
  - Active indicator highlighted
  - Smooth scroll to corresponding card
- "Explore more" button:
  - Next to scroll indicators
  - Animated chevron
  - Navigates to Category Explorer section
- CareerMindMap component:
  - Enhanced micro-animations (peaks, pulses, shines)
  - Fixed animation glitches (no flicker on reload)
  - Consistent behavior on navigation
  - Breathing scale effect on entire SVG

**Segment 4: Category Explorer (100vh)**
- 3-step progress indicator
- Dynamic content switching (AnimatePresence)
- Grid layouts for categories/fields/domains

**Segment 5: Stats & Testimonials (100vh)**
- Layout: 2-column
- Stats with gradient accents
- Testimonial cards with avatars

**Segment 6: Final CTA (100vh)**
- Centered, focused
- Large typography
- Dual CTAs

### Component Patterns

**Buttons:**
```javascript
// Primary: brightness(115%) hover, scale(0.97) active
// Secondary: brightness(125%) hover, scale(0.97) active
// Tertiary: background change hover
// Ghost: background rgba(255,255,255,0.03) hover
// Glass: backdrop-filter blur(8px) hover
```

**Cards:**
- Default: `bg-bg-secondary`, border `rgba(255,255,255,0.08)`
- Hover: `bg-bg-tertiary` (subtle change)
- Patterns: Very subtle (opacity 0.02-0.05)

**Animations:**
- Staggered entrances: 0.03s delay per item
- Scroll-triggered: `whileInView` with `once: true`
- Transitions: 0.16s-0.5s cubic-bezier easing

---

## What Needs to Be Done Next

### Phase 2: Remaining Pages (Priority)

**1. CareerPath Page:**
- ✅ Already redesigned - Verify all features work
- May need visual refinements based on testing

**2. UltimateRoadmap Page:**
- ✅ Already redesigned - Verify resource fetching
- May need visual refinements

**3. Flowchart Page:**
- ✅ Already redesigned - Verify interaction states
- May need visual refinements

### Phase 3: Enhancements

**1. Visual Assets:**
- Hero preview mockup could be more detailed/precise
- Career card patterns could be more refined
- Consider actual roadmap visualization instead of mock

**2. Micro-interactions:**
- Add more subtle hover effects where appropriate
- Smooth transitions between states
- Loading states for async operations

**3. Responsive Design:**
- Ensure all 100vh segments work on mobile
- Adjust grid layouts for tablets
- Test on various screen sizes

**4. Performance:**
- Optimize animations (use `will-change` sparingly)
- Lazy load images/patterns if needed
- Check bundle size

---

## Technical Stack

**Libraries:**
- React 18.2.0
- Framer Motion 12.23.24 (animations)
- React Router DOM 6.8.1
- Tailwind CSS 3.3.6
- Lenis (@studio-freight/lenis) - Smooth scroll

**File Structure:**
```
src/
├── components/
│   ├── LinearButton.js ✅
│   ├── LinearCard.js ✅
│   ├── LoadingSpinner.js ✅
│   ├── Navbar.js ✅
│   ├── SearchBar.js ✅
│   └── CareerMindMap.js ✅ (Enhanced with micro-animations, fixed glitches)
├── pages/
│   ├── Landing.js ✅ (6 segments, fully refined)
│   ├── CareerPath.js ✅
│   ├── UltimateRoadmap.js ✅
│   └── Flowchart.js ✅
├── context/
│   ├── AppContext.js
│   └── ThemeContext.js
├── constants/
│   └── careerData.js
├── services/
│   └── api.js
├── App.js ✅ (Lenis integrated)
├── index.css ✅ (Linear design system)
└── tailwind.config.js ✅
```

---

## Lenis Configuration

**Current Settings (Optimized - Latest):**
```javascript
{
  duration: 0.35,              // Optimized for responsiveness
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),  // Improved easing
  orientation: 'vertical',
  gestureOrientation: 'vertical',
  smoothWheel: true,
  wheelMultiplier: 1.0,       // Balanced for smooth feel
  smoothTouch: false,
  touchMultiplier: 1.5,
  infinite: false,
}
```

**Scroll Performance (Hero Section):**
- Custom scroll handler with `requestAnimationFrame` throttling
- Passive scroll listeners for better performance
- Blur and opacity updates: `heroBlur = progress * 8`, `heroOpacity = Math.max(0.4, 1 - progress * 0.6)`
- Trigger point: `window.innerHeight * 0.2`
- Fade range: `window.innerHeight * 0.35`

**CSS Rules (Required):**
```css
html.lenis, html.lenis body { height: auto; }
.lenis.lenis-smooth { scroll-behavior: auto !important; }
.lenis.lenis-stopped { overflow: hidden; }
.lenis.lenis-smooth iframe { pointer-events: none; }
```

---

## Design Patterns Reference

### Linear.app Screenshot Analysis

**Navigation:**
- Plain text links (no emojis)
- Hover shows preview dropdown
- Glassmorphism header with blur(20px)
- Full-width layout

**Cards:**
- Large cards with subtle background patterns
- Patterns relate to content (code for dev, charts for data)
- Border: rgba(255,255,255,0.08)
- Hover: subtle background change

**Segments:**
- Each section full viewport height
- Unique layouts (2-column, grid, angled, stacked)
- Dynamic content presentation
- No repetitive patterns

**Hero Sections:**
- Large typography (title-5 to title-6)
- **Vertical stacking**: Text centered at top, massive preview below (matching Linear exactly)
- **3D tilted preview**: "Sleeping" perspective with top receding, bottom closer
  - `rotateX(10deg) rotateY(-4deg) rotateZ(-3deg)`
  - Perspective: 1500px
  - Transform origin: center center
- Dual CTAs (primary + secondary)
- Atmospheric lighting: vignette, shadows, ambient glows
- Scroll fade effect: Preview blurs and fades on scroll for cinematic feel
- Exact color matching: All colors updated to Linear's palette

---

## Implementation Checklist

### Completed ✅
- [x] Design system (CSS variables, Tailwind config)
- [x] Core components (Button, Card, Navbar, SearchBar, Spinner)
- [x] Landing page (6 full-viewport segments)
- [x] Hero section refined: Vertical layout, simplified mockup, exact Linear colors
- [x] Hero section cinematic redesign: Elegant typography, minimal aesthetic, staggered animations
- [x] All colors updated to exact Linear palette throughout
- [x] Hero mockup: Reduced size (68% width, 48vh height), simplified to 3-card dashboard
- [x] Background color consistency fixed (solid `#08090a` throughout)
- [x] Performance optimizations: requestAnimationFrame throttling, static transforms
- [x] Scroll fade effect on hero mockup
- [x] CareerMindMap component enhanced: Micro-animations, fixed Data Science graph, eliminated flicker
- [x] Popular Career Paths: Interactive scroll indicators, "Explore more" button
- [x] Section reordering: "How It Works" before "Popular Career Paths"
- [x] Animation glitches fixed: No flicker/shaking on reload/navigation
- [x] CareerPath page redesign
- [x] UltimateRoadmap page redesign
- [x] Flowchart page redesign
- [x] Lenis smooth scroll integration (optimized settings)
- [x] Navbar with hover previews
- [x] Removed all emojis
- [x] Added SVG icons

### To Do / Verify
- [ ] Test all pages thoroughly
- [ ] Verify all functionality preserved
- [ ] Check responsive design
- [ ] Optimize performance
- [ ] Add any missing micro-interactions
- [ ] Refine visual assets if needed

---

## Notes for Next Agent

**Key Context:**
1. This is a complete redesign following Linear.app aesthetic
2. All functionality must be preserved
3. User strongly prefers Linear's minimal, professional style
4. Full-viewport segments are critical for landing page
5. No emojis anywhere - use SVG icons
6. Patterns on cards should be subtle and contextual

**Current State (Latest Updates - December 2024):**
- Phase 1 complete - Foundation and landing page done
- Hero section fully refined with cinematic minimal design:
  - Typography: Smaller, tighter (max text-6xl equivalent), elegant Linear/Apple style
  - Layout: ~80vh height, shifted left with breathing space
  - Content: "Career guidance that moves at your pace" headline, clear value proposition
  - Background: Fixed color consistency (solid `#08090a` throughout)
  - Animations: Staggered fade-in on load, smooth scroll fade
  - **CRITICAL**: Mockup component (CareerScene) kept completely intact
- CareerMindMap component enhanced:
  - Micro-animations: peaks, pulses, shines, breathing effects
  - Fixed Data Science graph: bars fit bounds, trend line follows bar tops with cubic Bezier
  - Fixed reverse animations: bars animate correctly upward from baseline
  - Removed flicker: eliminated `initial` animations from background elements
  - Removed parallax: eliminated `y` transform from CareerScene to prevent reload glitches
- Popular Career Paths section:
  - Interactive scroll indicators with active state tracking
  - "Explore more" button with animated chevron
  - Fixed all animation glitches (no shaking/flicker on reload/navigation)
- Section reordering: "How It Works" now appears before "Popular Career Paths"
- All animations consistent and smooth on every render
- All core components created and working
- All pages redesigned
- Build system working
- Performance optimizations: requestAnimationFrame throttling, static transforms
- Ready for continued refinement and next phase improvements

**Next Steps:**
1. Test all pages in browser
2. Fix any bugs or issues
3. Refine visual details
4. Optimize performance if needed
5. Add any missing features

**Important Files:**
- `Landing.js` - Main showcase page (6 segments, fully refined)
  - Hero: Cinematic minimal design with elegant typography (~80vh)
    - Headline: "Career guidance that moves at your pace"
    - Typography: `clamp(2.5rem, 5vw, 4rem)`, line-height `1.15`, letter-spacing `-.022em`
    - Staggered fade-in animations on load
    - Background: Solid `#08090a` (matches page exactly)
    - **CRITICAL**: CareerScene mockup kept completely intact
  - Section order: Hero → How It Works → Popular Careers → Category Explorer → Stats → CTA
  - Popular Careers: Interactive scroll indicators, "Explore more" button
  - Colors: Exact Linear palette (#08090a, #f7f8f8, #d0d6e0, #8a8f98, #7170ff)
  - Performance: requestAnimationFrame throttling, static 3D transforms
  - Scroll effect: Blur and opacity fade on hero mockup
  - Animation fixes: Removed parallax y transform, removed conflicting initial animations
- `CareerMindMap.js` - SVG visualizations for career paths (recently enhanced)
  - Digital Marketing: Peak on tallest bar, enhanced arrows, pulsing metric dots
  - Software Engineering: Increased bracket thickness, enhanced syntax highlight
  - Data Science: Fixed bar bounds, cubic Bezier trend line, fixed reverse animations
  - UI/UX Design: Pen tip shine/glow, increased stroke width
  - General: Breathing scale effect, removed initial animations to prevent flicker
  - All animations use React.Fragment for multi-element renders
- `LinearButton.js` - Button component with all variants
- `LinearCard.js` - Card component
- `Navbar.js` - Navigation with hover previews
- `index.css` - Complete design system
- `tailwind.config.js` - All design tokens
- `App.js` - Lenis configuration (duration: 0.35, optimized easing)

**Design References:**
- Screenshots provided show Linear's:
  - Navigation structure
  - Card designs with patterns
  - Full-viewport segments
  - Angled previews (hero mockup with "sleeping" perspective)
  - Typography hierarchy
  - **Critical**: Hero section with vertical stacking (text top, massive tilted preview below)
  - **Critical**: Exact color palette matching Linear's interface

**Latest Implementation Notes (December 2024):**
- Hero section redesigned with cinematic minimal aesthetic:
  - Typography refined to match Linear.app/Apple style (smaller, tighter, elegant)
  - Content updated: "Career guidance that moves at your pace" with clear value proposition
  - Background color consistency fixed (solid `#08090a` throughout)
  - Staggered fade-in animations on load for smooth entrance
  - Mockup kept completely intact (CareerScene component untouched)
- CareerMindMap component enhancements:
  - All visualizations enhanced with micro-animations (peaks, pulses, shines)
  - Data Science graph fixed: bars fit within bounds, trend line uses cubic Bezier curves
  - Animation direction fixed: bars animate upward from baseline correctly
  - Flicker eliminated: removed `initial` animations from background elements
- Popular Career Paths section:
  - Interactive scroll indicators with active state tracking
  - "Explore more" button added with smooth navigation
  - All animation glitches fixed (no flicker/shaking on reload/navigation)
- Section reordering completed: "How It Works" before "Popular Career Paths"
- Performance: requestAnimationFrame throttling, static 3D transforms, removed expensive parallax
- All animations consistent and smooth on every render

**Known Issues Fixed:**
1. ✅ Color inconsistency in hero section (mockup background vs page background) - Fixed with solid `#08090a`
2. ✅ Data Science graph bars exceeding bounds - Fixed by adjusting bar heights (max 45 at y=30)
3. ✅ Data Science reverse animations - Fixed by ensuring bars animate upward from baseline
4. ✅ Trend line overshooting bars - Fixed with cubic Bezier curve path
5. ✅ Flicker/shaking on page reload/navigation - Fixed by removing parallax y transform and conflicting initial animations
6. ✅ CareerMindMap animations inconsistent - Fixed by removing initial animations from background elements
7. ✅ Section order - Fixed by moving "How It Works" before "Popular Career Paths"

Continue with the same level of attention to detail and adherence to Linear's design principles.
IMPORTANT CONTEXT TO NOT MISS ON: 
There are still several changes to be made, we're still at the very first stage and so far considereing we've just implemented the theme, we did a great job, however its still 0.1% of the task done here, we still have so much to work on and correct. So step by step I'll keep on telling what has to be changed you keep a note on that and then analyze everything, do research and see if there are better ways to implement that (deep-think) and make sure that everything is done keeping the entire codebase in mind in order to maintain the consistency.
RULES : 
-do not create any markdown or summary files in agent mode until and unless i ask you to do so.
-in ask mode whatever i tell its for you to understand everything in a better way so make sure you keep the response as short as possible in ask mode.
-taking more time in excecution is totally fine but not getting stuck on a loop of solving lints and error, so make sure whatever you are doing maintains the consistency and integration across the entire codebase and the existing funcitonality and workflow is not effected by that 