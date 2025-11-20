@layer web {
	@layer reset, fonts, base, utils;
}

@layer web.reset {
	*,
	::before,
	::after {
		box-sizing: border-box;
	}

	html,
	body,
	div,
	span,
	applet,
	object,
	iframe,
	h1,
	h2,
	h3,
	h4,
	h5,
	h6,
	p,
	blockquote,
	pre,
	a,
	abbr,
	acronym,
	address,
	big,
	cite,
	code,
	del,
	dfn,
	em,
	img,
	ins,
	kbd,
	q,
	s,
	samp,
	small,
	strike,
	strong,
	sub,
	sup,
	tt,
	var,
	b,
	u,
	i,
	center,
	dl,
	dt,
	dd,
	ol,
	ul,
	li,
	fieldset,
	form,
	label,
	legend,
	table,
	caption,
	tbody,
	tfoot,
	thead,
	tr,
	th,
	td,
	article,
	aside,
	canvas,
	details,
	embed,
	figure,
	figcaption,
	footer,
	header,
	hgroup,
	menu,
	nav,
	output,
	ruby,
	section,
	summary,
	time,
	mark,
	audio,
	video {
		font-size: inherit;
		font-family: inherit;
		font-weight: inherit;
		line-height: inherit;
		vertical-align: baseline;
		border: 0;
		margin: 0;
		padding: 0;
	}

	article,
	aside,
	details,
	figcaption,
	figure,
	footer,
	header,
	hgroup,
	menu,
	nav,
	section {
		display: block;
	}

	body {
		line-height: 1;
	}

	blockquote,
	q {
		quotes: none;
	}

	blockquote::before,
	blockquote::after,
	q::before,
	q::after {
		content: "";
		content: none;
	}

	cite {
		font-style: normal;
	}

	table {
		border-collapse: collapse;
		border-spacing: 0;
	}
}

@layer web.fonts {
	@font-face {
		font-family: Inter Variable;
		font-weight: 100 900;
		font-display: swap;
		font-style: normal;
		src: url("https://static.linear.app/fonts/InterVariable.woff2?v=4.1") format("woff2");
	}

	@font-face {
		font-family: Inter Variable;
		font-weight: 100 900;
		font-display: swap;
		font-style: italic;
		src: url("https://static.linear.app/fonts/InterVariable-Italic.woff2?v=4.1") format("woff2");
	}

	@font-face {
		font-family: Berkeley Mono;
		font-style: normal;
		font-weight: 100 900;
		font-display: swap;
		src: url("https://static.linear.app/fonts/Berkeley-Mono-Variable.woff2?v=3.2") format("woff2");
	}
}

:root {
	--header-height: 64px;
	--header-blur: 20px;
	--page-padding-inline: 24px;
	--page-padding-block: 64px;
	--page-padding-left: max(env(safe-area-inset-left), var(--page-padding-inline));
	--page-padding-right: max(env(safe-area-inset-right), var(--page-padding-inline));
	--page-max-width: 1024px;
	--prose-max-width: 624px;
	--grid-columns: 12;
	--layer-max: 10000;
	--layer-debug: 5100;
	--layer-skip-nav: 5000;
	--layer-context-menu: 1200;
	--layer-tooltip: 1100;
	--layer-toasts: 800;
	--layer-dialog: 700;
	--layer-dialog-overlay: 699;
	--layer-command-menu: 650;
	--layer-popover: 600;
	--layer-overlay: 500;
	--layer-header: 100;
	--layer-scrollbar: 75;
	--layer-footer: 50;
	--layer-3: 3;
	--layer-2: 2;
	--layer-1: 1;
	--radius-4: 4px;
	--radius-6: 6px;
	--radius-8: 8px;
	--radius-12: 12px;
	--radius-16: 16px;
	--radius-24: 24px;
	--radius-32: 32px;
	--radius-rounded: 9999px;
	--radius-circle: 50%;
	--border-hairline: 1px;
	--font-serif-display: "Tiempos Headline", ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
	--font-monospace: "Berkeley Mono", ui-monospace, "SF Mono", "Menlo", monospace;
	--font-regular: "Inter Variable", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", sans-serif;
	--font-emoji: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "Twemoji Mozilla", "Noto Color Emoji", "Android Emoji";
	--font-weight-light: 300;
	--font-weight-normal: 400;
	--font-weight-medium: 510;
	--font-weight-semibold: 590;
	--font-weight-bold: 680;
	--speed-highlightFadeIn: 0s;
	--speed-highlightFadeOut: .15s;
	--speed-quickTransition: .1s;
	--speed-regularTransition: .25s;
	--mask-visible: black;
	--mask-on: black;
	--mask-ease: rgba(0, 0, 0, .2);
	--mask-invisible: transparent;
	--mask-off: transparent;
	--shadow-none: 0px 0px 0px transparent;
	--shadow-tiny: var(--shadow-none);
	--shadow-low: var(--shadow-none);
	--shadow-medium: var(--shadow-none);
	--shadow-high: var(--shadow-none);
	--rounded-full: 9999px;
	--transparent: rgba(255, 255, 255, 0);
	--min-tap-size: 44px;
	--dvh: 1vh;
	--100dvh: calc(100 * var(--dvh));
	--svh: 1vh;
	--100svh: calc(100 * var(--svh));
	--1fr: minmax(0, 1fr);
	--scrollbar-color: rgba(255, 255, 255, .1);
	--scrollbar-color-hover: rgba(255, 255, 255, .2);
	--scrollbar-color-active: rgba(255, 255, 255, .4);
	--scrollbar-size: 6px;
	--scrollbar-size-active: 10px;
	--scrollbar-gap: 4px;
	--ease-in-quad: cubic-bezier(.55, .085, .68, .53);
	--ease-in-cubic: cubic-bezier(.55, .055, .675, .19);
	--ease-in-quart: cubic-bezier(.895, .03, .685, .22);
	--ease-in-quint: cubic-bezier(.755, .05, .855, .06);
	--ease-in-expo: cubic-bezier(.95, .05, .795, .035);
	--ease-in-circ: cubic-bezier(.6, .04, .98, .335);
	--ease-out-quad: cubic-bezier(.25, .46, .45, .94);
	--ease-out-cubic: cubic-bezier(.215, .61, .355, 1);
	--ease-out-quart: cubic-bezier(.165, .84, .44, 1);
	--ease-out-quint: cubic-bezier(.23, 1, .32, 1);
	--ease-out-expo: cubic-bezier(.19, 1, .22, 1);
	--ease-out-circ: cubic-bezier(.075, .82, .165, 1);
	--ease-in-out-quad: cubic-bezier(.455, .03, .515, .955);
	--ease-in-out-cubic: cubic-bezier(.645, .045, .355, 1);
	--ease-in-out-quart: cubic-bezier(.77, 0, .175, 1);
	--ease-in-out-quint: cubic-bezier(.86, 0, .07, 1);
	--ease-in-out-expo: cubic-bezier(1, 0, 0, 1);
	--ease-in-out-circ: cubic-bezier(.785, .135, .15, .86);
	--color-white: #fff;
	--color-black: #000;
	--color-blue: #4ea7fc;
	--color-red: #eb5757;
	--color-green: #4cb782;
	--color-orange: #fc7840;
	--color-yellow: #f2c94c;
	--color-indigo: #5e6ad2;
	--color-linear-plan: #68cc58;
	--color-linear-build: #d4b144;
	--color-linear-security: #7a7fad;
	--focus-ring-color: var(--color-indigo);
	--focus-ring-width: 2px;
	--focus-ring-offset: 2px;
	--focus-ring-outline: var(--focus-ring-width) solid var(--focus-ring-color);
	--pointer: pointer;
	--cursor-pointer: pointer;
	--cursor-disabled: not-allowed;
	--cursor-tooltip: help;
	--font-size-micro: .6875rem;
	--font-size-microPlus: .6875rem;
	--font-size-mini: .75rem;
	--font-size-miniPlus: .75rem;
	--font-size-small: .8125rem;
	--font-size-smallPlus: .8125rem;
	--font-size-regular: .9375rem;
	--font-size-regularPlus: .9375rem;
	--font-size-large: 1.125rem;
	--font-size-largePlus: 1.125rem;
	--font-size-title1: 2.25rem;
	--font-size-title2: 1.5rem;
	--font-size-title3: 1.25rem;
	--title-1: var(--font-weight-semibold) var(--title-1-size) / var(--title-1-line-height) var(--font-regular);
	--title-1-size: 1.0625rem;
	--title-1-line-height: 1.4;
	--title-1-letter-spacing: -.012em;
	--title-2: var(--font-weight-semibold) var(--title-2-size) / var(--title-2-line-height) var(--font-regular);
	--title-2-size: 1.3125rem;
	--title-2-line-height: 1.33;
	--title-2-letter-spacing: -.012em;
	--title-3: var(--font-weight-semibold) var(--title-3-size) / var(--title-3-line-height) var(--font-regular);
	--title-3-size: 1.5rem;
	--title-3-line-height: 1.33;
	--title-3-letter-spacing: -.012em;
	--title-4: var(--font-weight-semibold) var(--title-4-size) / var(--title-4-line-height) var(--font-regular);
	--title-4-size: 2rem;
	--title-4-line-height: 1.125;
	--title-4-letter-spacing: -.022em;
	--title-5: var(--font-weight-semibold) var(--title-5-size) / var(--title-5-line-height) var(--font-regular);
	--title-5-size: 2.5rem;
	--title-5-line-height: 1.1;
	--title-5-letter-spacing: -.022em;
	--title-6: var(--font-weight-semibold) var(--title-6-size) / var(--title-6-line-height) var(--font-regular);
	--title-6-size: 3rem;
	--title-6-line-height: 1.1;
	--title-6-letter-spacing: -.022em;
	--title-7: var(--font-weight-semibold) var(--title-7-size) / var(--title-7-line-height) var(--font-regular);
	--title-7-size: 3.5rem;
	--title-7-line-height: 1.1;
	--title-7-letter-spacing: -.022em;
	--title-8: var(--font-weight-semibold) var(--title-8-size) / var(--title-8-line-height) var(--font-regular);
	--title-8-size: 4rem;
	--title-8-line-height: 1.06;
	--title-8-letter-spacing: -.022em;
	--title-9: var(--font-weight-semibold) var(--title-9-size) / var(--title-9-line-height) var(--font-regular);
	--title-9-size: 4.5rem;
	--title-9-line-height: 1;
	--title-9-letter-spacing: -.022em;
	--text-large: var(--text-large-size) / var(--text-large-line-height) var(--font-regular);
	--text-large-size: 1.0625rem;
	--text-large-line-height: 1.6;
	--text-large-letter-spacing: 0;
	--text-regular: var(--text-regular-size) / var(--text-regular-line-height) var(--font-regular);
	--text-regular-size: .9375rem;
	--text-regular-line-height: 1.6;
	--text-regular-letter-spacing: -.011em;
	--text-small: var(--text-small-size) / var(--text-small-line-height) var(--font-regular);
	--text-small-size: .875rem;
	--text-small-line-height: calc(21 / 14);
	--text-small-letter-spacing: -.013em;
	--text-mini: var(--text-mini-size) / var(--text-mini-line-height) var(--font-regular);
	--text-mini-size: .8125rem;
	--text-mini-line-height: 1.5;
	--text-mini-letter-spacing: -.01em;
	--text-micro: var(--text-micro-size) / var(--text-micro-line-height) var(--font-regular);
	--text-micro-size: .75rem;
	--text-micro-line-height: 1.4;
	--text-micro-letter-spacing: 0;
	--text-tiny: var(--text-tiny-size) / var(--text-tiny-line-height) var(--font-regular);
	--text-tiny-size: .625rem;
	--text-tiny-line-height: 1.5;
	--text-tiny-letter-spacing: -.015em;
	--cursor-none: none !important;
}

@media only screen and (min-device-pixel-ratio: 2), only screen and (-webkit-min-device-pixel-ratio: 2), only screen and (min-resolution: 192dpi) {
	:root {
		--border-hairline: .5px;
	}
}

@media (dynamic-range: high) or (color-gamut: p3) {
	:root {
		--color-blue: #5eb0ff;
	}

	@supports (color: color(display-p3 0 0 0)) {
		:root {
			--color-blue: color(display-p3 .431 .6816 .9988);
		}
	}
}

@supports (height: 1dvh) {
	:root {
		--dvh: 1dvh;
	}
}

@supports (height: 1svh) {
	:root {
		--svh: 1svh;
	}
}

@media (max-width: 768px) {
	:root {
		--page-padding-y: 48px;
		--grid-columns: 8;
	}
}

@media (max-width: 640px) {
	:root {
		--grid-columns: 4;
	}
}

[data-theme="dark"],
[data-theme="light"],
[data-theme="glass"] {
	color: var(--color-text-primary);
}

[data-theme="dark"] {
	--lightningcss-light: ;
	--lightningcss-dark: initial;
	color-scheme: dark;
	--header-bg: rgba(11, 11, 11, .8);
	--header-border: rgba(255, 255, 255, .08);
	--color-bg-primary: #08090a;
	--color-bg-secondary: #1c1c1f;
	--color-bg-tertiary: #232326;
	--color-bg-quaternary: #28282c;
	--color-bg-marketing: #010102;
	--color-bg-translucent: rgba(255, 255, 255, .05);
	--color-bg-quinary: #282828;
	--color-border-primary: #23252a;
	--color-border-secondary: #34343a;
	--color-border-tertiary: #3e3e44;
	--color-border-translucent: rgba(255, 255, 255, .05);
	--color-text-primary: #f7f8f8;
	--color-text-secondary: #d0d6e0;
	--color-text-tertiary: #8a8f98;
	--color-text-quaternary: #62666d;
	--color-link-primary: #828fff;
	--color-link-hover: #fff;
	--color-brand-bg: #5e6ad2;
	--color-brand-text: #fff;
	--color-selection-text: var(--color-white);
	--color-selection-bg: color-mix(in lch, var(--color-brand-bg), black 10%);
	--color-selection-dim: color-mix(in lch, var(--color-brand-bg), transparent 80%);
	--color-overlay-dim-rgb: 255, 255, 255;
	--color-overlay-primary: rgba(0, 0, 0, .9);
	--color-alpha: 255;
	--shadow-low: 0px 2px 4px rgba(0, 0, 0, .1);
	--shadow-medium: 0px 4px 24px rgba(0, 0, 0, .2);
	--shadow-high: 0px 7px 32px rgba(0, 0, 0, .35);
	--shadow-stack-low: 0px 8px 2px 0px transparent, 0px 5px 2px 0px rgba(0, 0, 0, .01), 0px 3px 2px 0px rgba(0, 0, 0, .04), 0px 1px 1px 0px rgba(0, 0, 0, .07), 0px 0px 1px 0px rgba(0, 0, 0, .08);
	--icon-grayscale-image-filter: grayscale(100%) brightness(400%);
	--color-bg-level-0: #08090a;
	--color-bg-level-1: #0f1011;
	--color-bg-level-2: #141516;
	--color-bg-level-3: #191a1b;
	--color-bg-tint: #141516;
	--color-line-primary: #37393a;
	--color-line-secondary: #202122;
	--color-line-tertiary: #18191a;
	--color-line-quaternary: #141515;
	--color-line-tint: #141516;
	--color-fg-primary: #f7f8f8;
	--color-fg-secondary: #d0d6e0;
	--color-fg-tertiary: #8a8f98;
	--color-fg-quaternary: #62666d;
	--color-accent: #7170ff;
	--color-accent-hover: #828fff;
	--color-accent-tint: #18182f;
}

[data-theme="glass"] {
	--lightningcss-light: ;
	--lightningcss-dark: initial;
	color-scheme: dark;
	--header-bg: rgba(11, 11, 11, .8);
	--header-border: rgba(255, 255, 255, .08);
	--color-bg-primary: #000212;
	--color-bg-secondary: rgba(255, 255, 255, .03);
	--color-bg-tertiary: rgba(255, 255, 255, .07);
	--color-bg-quaternary: rgba(255, 255, 255, .15);
	--color-bg-quinary: rgba(255, 255, 255, .2);
	--color-border-primary: rgba(255, 255, 255, .08);
	--color-border-secondary: rgba(255, 255, 255, .12);
	--color-border-tertiary: rgba(255, 255, 255, .15);
	--color-text-primary: #f7f8f8;
	--color-text-secondary: #b4bcd0;
	--color-text-tertiary: rgba(180, 188, 208, .6);
	--color-text-quaternary: rgba(180, 188, 208, .4);
	--color-link-primary: #828fff;
	--color-link-hover: var(--color-text-primary);
	--color-brand-bg: #5e6ad2;
	--color-brand-text: #fff;
	--color-selection-text: var(--color-white);
	--color-selection-bg: color-mix(in lch, var(--color-brand-bg), transparent 30%);
	--color-selection-dim: color-mix(in lch, var(--color-brand-bg), transparent 80%);
	--color-overlay-dim-rgb: 255, 255, 255;
	--color-overlay-primary: rgba(0, 0, 0, .9);
	--color-alpha: 255;
	--color-bg-level-0: #08090a;
	--color-bg-level-1: #0f1011;
	--color-bg-level-2: #141516;
	--color-bg-level-3: #191a1b;
	--color-bg-tint: #141516;
	--shadow-low: 0px 2px 4px rgba(0, 0, 0, .1);
	--shadow-medium: 0px 4px 24px rgba(0, 0, 0, .2);
	--shadow-high: 0px 7px 32px rgba(0, 0, 0, .35);
	--icon-grayscale-image-filter: grayscale(100%) brightness(400%);
}

[data-theme="light"] {
	--lightningcss-light: initial;
	--lightningcss-dark: ;
	color-scheme: light;
	--header-bg: rgba(255, 255, 255, .8);
	--header-border: rgba(0, 0, 0, .08);
	--color-bg-primary: #fff;
	--color-bg-secondary: #f9f8f9;
	--color-bg-tertiary: #f4f2f4;
	--color-bg-quaternary: #eeedef;
	--color-bg-quinary: #e9e8ea;
	--color-bg-translucent: rgba(0, 0, 0, .02);
	--color-border-primary: #e9e8ea;
	--color-border-secondary: #e4e2e4;
	--color-border-tertiary: #dcdbdd;
	--color-border-translucent: rgba(0, 0, 0, .05);
	--color-text-primary: #282a30;
	--color-text-secondary: #3c4149;
	--color-text-tertiary: #6f6e77;
	--color-text-quaternary: #86848d;
	--color-link-primary: #7070ff;
	--color-link-hover: var(--color-text-primary);
	--color-brand-bg: #7070ff;
	--color-brand-text: #fff;
	--color-selection-text: currentColor;
	--color-selection-bg: color-mix(in lch, var(--color-brand-bg), transparent 64%);
	--color-selection-dim: color-mix(in lch, var(--color-brand-bg), transparent 80%);
	--focus-ring-color: rgba(0, 0, 0, .4);
	--focus-ring-width: 2px;
	--focus-ring-offset: 2px;
	--focus-ring-outline: var(--focus-ring-width) solid var(--focus-ring-color);
	--color-overlay-dim-rgb: 0, 0, 0;
	--color-overlay-primary: rgba(255, 255, 255, .65);
	--color-alpha: 0;
	--shadow-tiny: 0px 1px 1px 0px rgba(0, 0, 0, .09);
	--shadow-low: 0px 1px 4px -1px rgba(0, 0, 0, .09);
	--shadow-medium: 0px 3px 12px rgba(0, 0, 0, .09);
	--shadow-high: 0px 7px 24px rgba(0, 0, 0, .06);
	--shadow-stack-low: 0px -1px 1px 0px rgba(0, 0, 0, .11) inset, 0px 8px 2px 0px transparent, 0px 5px 2px 0px rgba(0, 0, 0, .01), 0px 3px 2px 0px rgba(0, 0, 0, .04), 0px 1px 1px 0px rgba(0, 0, 0, .07), 0px 0px 1px 0px rgba(0, 0, 0, .08);
	--font-weight-normal: 400;
	--font-weight-medium: 510;
	--font-weight-semibold: 590;
	--font-weight-bold: 680;
	--scrollbar-color: rgba(0, 0, 0, .1);
	--scrollbar-color-hover: rgba(0, 0, 0, .2);
	--scrollbar-color-active: rgba(0, 0, 0, .3);
	--icon-grayscale-image-filter: grayscale(100%) brightness(0%);
	--color-bg-level-0: #fff;
	--color-bg-level-1: #f8f8f8;
	--color-bg-level-2: #f4f4f4;
	--color-bg-level-3: #f0f0f0;
	--color-bg-tint: #f4f4f5;
	--color-line-primary: #d4d4d6;
	--color-line-secondary: #eaeaeb;
	--color-line-tertiary: #f0f0f0;
	--color-line-quaternary: #f4f4f4;
	--color-line-tint: #f4f4f5;
	--color-fg-primary: #282a2f;
	--color-fg-secondary: #3c4149;
	--color-fg-tertiary: #6f6e77;
	--color-fg-quaternary: #86848d;
	--color-accent: #7170ff;
	--color-accent-hover: #8989f0;
	--color-accent-tint: #f1f1ff;
}

::selection {
	color: var(--color-selection-text);
	background: var(--color-selection-bg);
}

img::selection {
	color: var(--color-selection-text);
	background: var(--color-selection-dim);
}

* {
	outline-color: transparent;
}

:focus:not(:focus-visible) {
	outline: none;
}

:focus-visible {
	outline-style: solid;
	outline-color: var(--focus-ring-color);
	outline-width: var(--focus-ring-width);
	outline-offset: var(--focus-ring-offset);
}

html,
body {
	background: var(--color-bg-primary);
	min-height: 100vh;
	color: var(--color-text-primary);
	-webkit-tap-highlight-color: transparent;
	-webkit-touch-callout: none;
	--font-settings: "cv01", "ss03";
	font-feature-settings: var(--font-settings);
	--font-variations: "opsz" auto;
	font-variation-settings: var(--font-variations);
	margin: 0;
	padding: 0;
}

html {
	font-size: 100%;
	font-weight: var(--font-weight-normal);
	scroll-padding-top: calc(var(--header-height) + 36px);
	scroll-padding-bottom: 32px;
}

body {
	-moz-osx-font-smoothing: grayscale;
	-webkit-font-smoothing: antialiased;
	text-rendering: optimizeLegibility;
	-webkit-text-size-adjust: none;
	-ms-text-size-adjust: none;
	line-height: 1.5;
	overflow-x: hidden;
}

html.logged-in [data-hide="logged-in"],
html:not(.logged-in) [data-show="logged-in"],
html:not(.js) button[data-rmiz-btn-open] {
	display: none;
}

:-webkit-any([data-theme="glass"], [data-theme="dark"]) :-webkit-any(.hide-dark, [data-hide="dark"]) {
	display: none;
}

:-moz-any([data-theme="glass"], [data-theme="dark"]) :-moz-any(.hide-dark, [data-hide="dark"]) {
	display: none;
}

:is([data-theme="glass"], [data-theme="dark"]) :is(.hide-dark, [data-hide="dark"]) {
	display: none;
}

[data-theme="light"] :-webkit-any(.hide-light, [data-hide="light"]) {
	display: none;
}

[data-theme="light"] :-moz-any(.hide-light, [data-hide="light"]) {
	display: none;
}

[data-theme="light"] :is(.hide-light, [data-hide="light"]) {
	display: none;
}

html:not(.js) .show-js {
	display: none;
}

@media (max-width: 640px) {
	[data-hide="mobile"],
	.hide-mobile {
		display: none !important;
	}
}

@media (min-width: 641px) {
	[data-show="mobile"],
	.show-mobile {
		display: none !important;
	}
}

@media (max-width: 768px) {
	[data-hide="tablet"],
	.hide-tablet {
		display: none !important;
	}
}

@media (min-width: 769px) {
	[data-show="tablet"],
	.show-tablet {
		display: none !important;
	}
}

@media (max-width: 1024px) {
	[data-hide="laptop"],
	.hide-laptop {
		display: none !important;
	}
}

@media (min-width: 1025px) {
	[data-show="laptop"],
	.show-laptop {
		display: none !important;
	}
}

@media (max-width: 1280px) {
	[data-hide="desktop"],
	.hide-desktop {
		display: none !important;
	}
}

@media (min-width: 1281px) {
	[data-show="desktop"],
	.show-desktop {
		display: none !important;
	}
}

@media (any-hover: hover) {
	[data-hide="hover"],
	.hide-hover {
		display: none !important;
	}
}

@media not (any-hover: hover) {
	[data-show="hover"],
	.show-hover {
		display: none !important;
	}
}

@layer web.base {
	body,
	html,
	button,
	input,
	optgroup,
	select,
	textarea {
		font-family: var(--font-regular);
	}

	a {
		cursor: pointer;
		color: inherit;
		text-decoration: none;
	}

	a:not([class]) {
		color: var(--color-text-primary);
		text-underline-offset: clamp(2px, .225em, 6px);
		text-decoration: underline;
		text-decoration-thickness: max(1px, min(.1em, 3px));
		-webkit-text-decoration-color: var(--color-text-quaternary);
		text-decoration-color: var(--color-text-quaternary);
		transition: var(--speed-regularTransition);
		transition-property: color, -webkit-text-decoration-color, text-decoration-color, background;
	}

	@media (any-hover: hover) {
		a:not([class]):hover {
			-webkit-text-decoration-color: var(--color-text-primary);
			text-decoration-color: var(--color-text-primary);
		}
	}

	svg,
	img {
		flex-shrink: 0;
	}

	h1,
	h2,
	h3,
	h4,
	h5,
	h6,
	p,
	li {
		margin: 0;
	}

	h1,
	h2,
	h3,
	h4,
	h5,
	h6 {
		font-size: 1rem;
		font-weight: var(--font-weight-semibold);
		color: var(--color-text-primary);
	}

	li {
		margin-bottom: 8px;
		margin-left: 24px;
	}

	hr {
		border: 0;
		border-top: 1px solid var(--color-border-primary);
		height: 0;
	}

	b,
	strong {
		font-weight: var(--font-weight-semibold);
	}

	kbd {
		background: var(--color-bg-primary);
		min-width: 24px;
		box-shadow: var(--shadow-tiny, var(--shadow-none)), 0 0 0 1px var(--color-border-tertiary);
		font-size: .8em;
		line-height: normal;
		font-weight: var(--font-weight-medium);
		text-align: center;
		border-radius: 5px;
		margin: 0 1px;
		padding: 3px 6px;
		display: inline-block;
	}

	kbd:first-letter {
		text-transform: uppercase;
	}

	pre,
	code {
		font-variation-settings: normal;
		font-feature-settings: normal;
		font-family: var(--font-monospace);
	}

	code:not(pre code) {
		-webkit-box-decoration-break: clone;
		box-decoration-break: clone;
		background-color: var(--color-bg-secondary);
		border: 1px solid var(--color-border-secondary);
		border-radius: .3em;
		padding: .1em .25em;
		font-size: .875em;
		line-height: 1.3;
	}

	pre {
		background: var(--color-bg-secondary);
		border: 1px solid var(--color-border-translucent);
		font-family: var(--font-monospace);
		text-align: left;
		-moz-tab-size: 4;
		tab-size: 4;
		-webkit-hyphens: none;
		hyphens: none;
		color: var(--color-text-secondary);
		border-radius: 8px;
		padding: 16px;
		font-size: 14px;
		line-height: 1.5;
		position: relative;
		overflow-x: auto;
	}

	[data-custom-scrollbar]::-webkit-scrollbar {
		width: 12px;
		height: 12px;
	}

	[data-custom-scrollbar]::-webkit-scrollbar-track {
		background: 0 0;
		transition: background .12s;
	}

	[data-custom-scrollbar]::-webkit-scrollbar-thumb {
		background-color: var(--scrollbar-color);
		border-radius: var(--radius-rounded);
		background-clip: content-box;
		border: 3px solid transparent;
	}

	[data-custom-scrollbar]::-webkit-scrollbar-thumb:hover {
		--scrollbar-color: var(--scrollbar-color-hover);
	}

	[data-custom-scrollbar]::-webkit-scrollbar-thumb:active {
		--scrollbar-color: var(--scrollbar-color-active);
	}
}

::view-transition-old(root) {
	mix-blend-mode: normal;
	animation: none;
}

::view-transition-new(root) {
	mix-blend-mode: normal;
	animation: none;
}

@media (prefers-reduced-motion: reduce) {
	::view-transition-group(*) {
		animation: none !important;
	}

	::view-transition-old(*) {
		animation: none !important;
	}

	::view-transition-new(*) {
		animation: none !important;
	}
}
/*# sourceMappingURL=168aee4392f5e1b3.css.map*/
.AshbyApplicationForm-module__AsrU_q__iframeContainer {
	background: var(--color-bg-primary);
	border: 1px solid var(--color-border-primary);
	border-radius: 8px;
	padding: 20px 20px 0;
	overflow: hidden;
}

.AshbyApplicationForm-module__AsrU_q__iframeContainer iframe {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
}

@media (max-width: 640px) {
	.AshbyApplicationForm-module__AsrU_q__iframeContainer {
		padding: 8px;
	}
}

.AshbyApplicationForm-module__AsrU_q__radioGroup {
	padding-top: 12px;
	padding-bottom: 20px;
	display: flex;
}

@media (max-width: 640px) {
	.AshbyApplicationForm-module__AsrU_q__radioGroup {
		padding-bottom: 4px;
	}
}

.AshbyApplicationForm-module__AsrU_q__radio {
	border: 1px solid var(--color-border-primary);
	color: var(--color-text-tertiary);
	font-size: 14px;
	font-weight: var(--font-weight-medium);
	cursor: pointer;
	width: 100%;
	transition: .16s var(--ease-out-quad);
	background: 0 0;
	padding: 16px;
	transition-property: color;
}

.AshbyApplicationForm-module__AsrU_q__radio[data-state="checked"] {
	color: var(--color-text-primary);
	background: var(--color-bg-tertiary);
}

.AshbyApplicationForm-module__AsrU_q__radio:hover {
	color: var(--color-text-primary);
}

.AshbyApplicationForm-module__AsrU_q__radio:first-of-type {
	border-top-left-radius: 6px;
	border-bottom-left-radius: 6px;
}

.AshbyApplicationForm-module__AsrU_q__radio:last-of-type {
	border-top-right-radius: 6px;
	border-bottom-right-radius: 6px;
	margin-left: -1px;
}

@media (max-width: 640px) {
	.AshbyApplicationForm-module__AsrU_q__locationSelector {
		padding-top: 4px;
		padding-left: 4px;
		padding-right: 4px;
	}
}

.Button-module__bZ-sGa__root {
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	cursor: pointer;
	white-space: nowrap;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	max-width: 100%;
	color: inherit;
	font: inherit;
	text-shadow: none;
	background: 0 0;
	border: none;
	flex-shrink: 0;
	justify-content: center;
	align-items: center;
	margin: 0;
	padding: 0;
	display: inline-flex;
	position: relative;
}

.Button-module__bZ-sGa__root:disabled {
	cursor: not-allowed;
}

.Button-module__bZ-sGa__variant {
	font-weight: var(--font-weight-medium);
	font-size: var(--button-font-size);
	line-height: var(--button-height);
	height: var(--button-height);
	gap: var(--button-gap);
	padding: var(--button-padding);
	border-radius: var(--button-corner-radius);
	transition: .16s var(--ease-out-quad);
	transition-property: border, background-color, color, box-shadow, opacity, filter, transform;
}

.Button-module__bZ-sGa__variant:disabled {
	opacity: .5;
}

.Button-module__bZ-sGa__variant:active,
.Button-module__bZ-sGa__variant.Button-module__bZ-sGa__active {
	will-change: transform;
}

.Button-module__bZ-sGa__variant > svg {
	will-change: transform;
	fill: currentColor;
	width: var(--button-icon-size, 16px);
	height: var(--button-icon-size, 16px);
}

.Button-module__bZ-sGa__variant > kbd {
	background: var(--kbd-bg);
	color: var(--kbd-text);
	margin-right: var(--kbd-offset);
	min-width: var(--kbd-size, 20px);
	height: var(--kbd-size, 20px);
	margin-left: var(--kbd-gap, 0px);
	box-shadow: none;
	border: none;
}

@media not (any-hover: hover) {
	.Button-module__bZ-sGa__variant > kbd {
		display: none;
	}
}

@media (max-width: 640px) {
	.Button-module__bZ-sGa__variant > kbd {
		display: none;
	}
}

.Button-module__bZ-sGa__size-mini {
	--button-height: 24px;
	--button-icon-size: 12px;
	--button-font-size: 12px;
	--button-corner-radius: var(--radius-6);
	--button-padding: 0 10px;
	--button-gap: 4px;
	--kbd-size: 16px;
	--kbd-offset: -6px;
}

.Button-module__bZ-sGa__size-small {
	--button-height: 32px;
	--button-icon-size: 16px;
	--button-font-size: 13px;
	--button-corner-radius: var(--radius-8);
	--button-padding: 0 12px;
	--button-gap: 8px;
	--kbd-offset: -5px;
	--kbd-size: 18px;
}

.Button-module__bZ-sGa__size-default {
	--button-height: 40px;
	--button-icon-size: 18px;
	--button-font-size: 15px;
	--button-corner-radius: 10px;
	--button-padding: 0 16px;
	--button-gap: 6px;
	--kbd-offset: -6px;
	--kbd-gap: 6px;
}

.Button-module__bZ-sGa__size-large {
	--button-height: 48px;
	--button-icon-size: 18px;
	--button-font-size: 16px;
	--button-corner-radius: var(--radius-8);
	--button-padding: 0 16px;
	--button-gap: 6px;
	--kbd-offset: -2px;
	--kbd-gap: 6px;
}

.Button-module__bZ-sGa__variant-primary {
	--kbd-bg: var(--color-bg-tertiary);
	color: var(--color-brand-text);
	background: var(--color-brand-bg);
	border: none;
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-primary:not([disabled]):hover {
		color: var(--color-brand-text);
		filter: brightness(115%);
	}
}

.Button-module__bZ-sGa__variant-primary:not([disabled]):active,
.Button-module__bZ-sGa__variant-primary.Button-module__bZ-sGa__active:not([disabled]) {
	filter: brightness(98%);
	transform: scale(.97);
}

.Button-module__bZ-sGa__variant-secondary {
	--kbd-bg: rgba(255, 255, 255, .15);
	background: var(--color-bg-quaternary);
	color: var(--color-text-primary);
	border: var(--border-hairline) solid var(--color-border-tertiary);
}

[data-theme="light"] .Button-module__bZ-sGa__variant-secondary {
	--kbd-bg: rgba(0, 0, 0, .08);
	background: var(--color-bg-primary);
	border: var(--border-hairline) solid rgba(0, 0, 0, .16);
	box-shadow: var(--shadow-low);
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-secondary:not([disabled]):hover {
		filter: brightness(125%);
	}

	[data-theme="light"] .Button-module__bZ-sGa__variant-secondary:not([disabled]):hover {
		filter: brightness(97%);
	}
}

.Button-module__bZ-sGa__variant-secondary:not([disabled]):active,
.Button-module__bZ-sGa__variant-secondary.Button-module__bZ-sGa__active:not([disabled]) {
	filter: brightness(98%);
	transform: scale(.97);
}

.Button-module__bZ-sGa__variant-tertiary {
	border: 1px solid var(--color-bg-secondary);
	background: var(--color-bg-primary);
	color: var(--color-text-tertiary);
}

[data-theme="light"] .Button-module__bZ-sGa__variant-tertiary {
	border: 1px solid var(--color-border-translucent);
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-tertiary:not([disabled]):hover {
		color: var(--color-text-primary);
		border-color: var(--color-bg-tertiary);
		background: var(--color-bg-tertiary);
	}
}

.Button-module__bZ-sGa__variant-tertiary:not([disabled]):active,
.Button-module__bZ-sGa__variant-tertiary.Button-module__bZ-sGa__active:not([disabled]) {
	color: var(--color-text-primary);
	border-color: var(--color-bg-quaternary);
	background: var(--color-bg-quaternary);
	transform: scale(.97);
}

.Button-module__bZ-sGa__variant-invert {
	color: var(--color-bg-primary);
	box-shadow: var(--shadow-stack-low);
	background: #e6e6e6;
	border: 1px solid #e6e6e6;
}

[data-theme="light"] .Button-module__bZ-sGa__variant-invert {
	background: var(--color-text-primary);
	border: 1px solid var(--color-text-primary);
	box-shadow: none;
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-invert:not([disabled]):hover {
		background: #fff;
	}

	[data-theme="light"] .Button-module__bZ-sGa__variant-invert:not([disabled]):hover {
		background: #1f2024;
	}
}

.Button-module__bZ-sGa__variant-invert:not([disabled]):active,
.Button-module__bZ-sGa__variant-invert.Button-module__bZ-sGa__active:not([disabled]) {
	transform: scale(.97);
}

.Button-module__bZ-sGa__variant-invert > kbd {
	--kbd-bg: rgba(0, 0, 0, .08);
	--kbd-text: var(--color-bg-primary);
}

[data-theme="light"] :is(.Button-module__bZ-sGa__variant-invert > kbd) {
	--kbd-bg: #3b3d45;
}

.Button-module__bZ-sGa__variant-ghost {
	color: var(--color-text-tertiary);
	background: 0 0;
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-ghost:not([disabled]):hover {
		color: var(--color-text-primary);
		background: var(--color-bg-quaternary);
	}
}

.Button-module__bZ-sGa__variant-ghost:not([disabled]):active,
.Button-module__bZ-sGa__variant-ghost.Button-module__bZ-sGa__active:not([disabled]) {
	color: var(--color-text-primary);
	background: var(--color-bg-quinary);
	transform: scale(.97);
}

.Button-module__bZ-sGa__variant-glass {
	color: var(--color-text-primary);
	background: 0 0;
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-glass:not([disabled]):hover {
		-webkit-backdrop-filter: blur(8px);
		backdrop-filter: blur(8px);
		background: rgba(255, 255, 255, .16);
	}
}

.Button-module__bZ-sGa__variant-glass:not([disabled]):active,
.Button-module__bZ-sGa__variant-glass.Button-module__bZ-sGa__active:not([disabled]) {
	background: rgba(255, 255, 255, .16);
	transform: scale(.97);
}

.Button-module__bZ-sGa__variant-inline {
	color: var(--color-link-primary);
	background: 0 0;
	margin-left: -8px;
	padding-top: 0;
	padding-bottom: 0;
	padding-left: 8px;
	padding-right: 8px;
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-inline:not([disabled]):hover {
		color: var(--color-text-primary);
	}
}

.Button-module__bZ-sGa__variant-inline:not([disabled]):active,
.Button-module__bZ-sGa__variant-inline.Button-module__bZ-sGa__active:not([disabled]) {
	transform: scale(.97);
}

.Button-module__bZ-sGa__variant-border {
	border: 2px solid var(--color-border-translucent);
	color: var(--color-text-quaternary);
	-webkit-backdrop-filter: blur(8px);
	backdrop-filter: blur(8px);
	background: 0 0;
}

@media (any-hover: hover) {
	.Button-module__bZ-sGa__variant-border:hover {
		color: var(--color-text-primary);
		border-color: var(--color-bg-tertiary);
		background: var(--color-bg-tertiary);
	}
}

.Button-module__bZ-sGa__shape-circle {
	--button-corner-radius: var(--radius-rounded);
}

.Flex-module__A66dmG__root {
	min-width: 0;
	display: flex;
}

.Flex-module__A66dmG__gap {
	gap: var(--gap-initial);
}

@media (min-width: 1536px) {
	.Flex-module__A66dmG__gap {
		gap: var(--gap-wide);
	}
}

@media (max-width: 1280px) {
	.Flex-module__A66dmG__gap {
		gap: var(--gap-desktop);
	}
}

@media (max-width: 1024px) {
	.Flex-module__A66dmG__gap {
		gap: var(--gap-laptop);
	}
}

@media (max-width: 768px) {
	.Flex-module__A66dmG__gap {
		gap: var(--gap-tablet);
	}
}

@media (max-width: 640px) {
	.Flex-module__A66dmG__gap {
		gap: var(--gap-mobile);
	}
}

.Flex-module__A66dmG__inline {
	display: inline-flex;
}

.Flex-module__A66dmG__auto {
	flex: auto;
}

.Flex-module__A66dmG__reverse {
	flex-direction: row-reverse;
}

.Flex-module__A66dmG__column {
	flex-direction: column;
}

.Flex-module__A66dmG__column.Flex-module__A66dmG__reverse {
	flex-direction: column-reverse;
}

.Flex-module__A66dmG__align-flex-start,
.Flex-module__A66dmG__align-start {
	align-items: flex-start;
}

.Flex-module__A66dmG__align-flex-end,
.Flex-module__A66dmG__align-end {
	align-items: flex-end;
}

.Flex-module__A66dmG__align-center {
	align-items: center;
}

.Flex-module__A66dmG__align-baseline {
	align-items: baseline;
}

.Flex-module__A66dmG__align-stretch {
	align-items: stretch;
}

.Flex-module__A66dmG__justify-flex-start,
.Flex-module__A66dmG__justify-start {
	justify-content: flex-start;
}

.Flex-module__A66dmG__justify-flex-end,
.Flex-module__A66dmG__justify-end {
	justify-content: flex-end;
}

.Flex-module__A66dmG__justify-center {
	justify-content: center;
}

.Flex-module__A66dmG__justify-space-between {
	justify-content: space-between;
}

.Flex-module__A66dmG__justify-space-around {
	justify-content: space-around;
}

.Flex-module__A66dmG__justify-space-evenly {
	justify-content: space-evenly;
}

.Flex-module__A66dmG__justify-stretch {
	justify-content: stretch;
}

.Flex-module__A66dmG__wrap {
	flex-wrap: wrap;
}

.Flex-module__A66dmG__center {
	justify-content: center;
	align-items: center;
}

.Flex-module__A66dmG__initial-row {
	flex-direction: row;
}

.Flex-module__A66dmG__initial-column {
	flex-direction: column;
}

.Flex-module__A66dmG__initial-row-reverse {
	flex-direction: row-reverse;
}

.Flex-module__A66dmG__initial-column-reverse {
	flex-direction: column-reverse;
}

@media (max-width: 640px) {
	.Flex-module__A66dmG__mobile-row {
		flex-direction: row;
	}

	.Flex-module__A66dmG__mobile-column {
		flex-direction: column;
	}

	.Flex-module__A66dmG__mobile-row-reverse {
		flex-direction: row-reverse;
	}

	.Flex-module__A66dmG__mobile-column-reverse {
		flex-direction: column-reverse;
	}
}

@media (max-width: 768px) {
	.Flex-module__A66dmG__tablet-row {
		flex-direction: row;
	}

	.Flex-module__A66dmG__tablet-column {
		flex-direction: column;
	}

	.Flex-module__A66dmG__tablet-row-reverse {
		flex-direction: row-reverse;
	}

	.Flex-module__A66dmG__tablet-column-reverse {
		flex-direction: column-reverse;
	}
}

@media (max-width: 1024px) {
	.Flex-module__A66dmG__laptop-row {
		flex-direction: row;
	}

	.Flex-module__A66dmG__laptop-column {
		flex-direction: column;
	}

	.Flex-module__A66dmG__laptop-row-reverse {
		flex-direction: row-reverse;
	}

	.Flex-module__A66dmG__laptop-column-reverse {
		flex-direction: column-reverse;
	}
}

@media (max-width: 1280px) {
	.Flex-module__A66dmG__desktop-row {
		flex-direction: row;
	}

	.Flex-module__A66dmG__desktop-column {
		flex-direction: column;
	}

	.Flex-module__A66dmG__desktop-row-reverse {
		flex-direction: row-reverse;
	}

	.Flex-module__A66dmG__desktop-column-reverse {
		flex-direction: column-reverse;
	}
}

@media (min-width: 1536px) {
	.Flex-module__A66dmG__wide-row {
		flex-direction: row;
	}

	.Flex-module__A66dmG__wide-column {
		flex-direction: column;
	}

	.Flex-module__A66dmG__wide-row-reverse {
		flex-direction: row-reverse;
	}

	.Flex-module__A66dmG__wide-column-reverse {
		flex-direction: column-reverse;
	}
}

.ContextMenu-module__qHrD2W__item {
	cursor: pointer;
	width: 100%;
	min-height: 32px;
	color: var(--color-text-secondary);
	box-shadow: none;
	border-radius: 6px;
	outline: none;
	align-items: center;
	gap: 8px;
	padding: 0 14px;
	font-size: 13px;
	line-height: 32px;
	display: flex;
}

.ContextMenu-module__qHrD2W__item svg {
	fill: var(--color-text-quaternary);
	width: 14px;
	height: 14px;
}

.ContextMenu-module__qHrD2W__item[data-highlighted] {
	background: var(--color-bg-tertiary);
}

.ContextMenu-module__qHrD2W__item[data-highlighted] svg {
	fill: var(--color-text-primary);
}

.ContextMenu-module__qHrD2W__separator {
	background: var(--color-bg-tertiary);
	height: 1px;
	margin: 6px -4px;
}

.ContextMenu-module__qHrD2W__content {
	z-index: var(--layer-context-menu);
	background: var(--color-bg-level-1);
	min-width: 220px;
	box-shadow: var(--shadow-stack-low), var(--shadow-high);
	border: 1px solid var(--color-line-tertiary);
	border-radius: 8px;
	padding: 4px;
	overflow: hidden;
}

@media (prefers-reduced-motion: no-preference) {
	.ContextMenu-module__qHrD2W__content {
		transform-origin: var(--radix-context-menu-content-transform-origin);
	}

	.ContextMenu-module__qHrD2W__content[data-state="open"] {
		animation: ContextMenu-module__qHrD2W__contextMenuIn var(--speed-quickTransition) var(--ease-out-quad);
	}

	.ContextMenu-module__qHrD2W__content[data-state="closed"] {
		animation: ContextMenu-module__qHrD2W__contextMenuOut var(--speed-quickTransition) var(--ease-in-quad);
	}
}

[data-theme="light"] .ContextMenu-module__qHrD2W__content {
	background: var(--color-white);
	box-shadow: var(--shadow-high);
}

@keyframes ContextMenu-module__qHrD2W__contextMenuIn {
	0% {
		opacity: 0;
		transform: scale(.9);
	}

	to {
		opacity: 1;
		transform: scale(1);
	}
}

@keyframes ContextMenu-module__qHrD2W__contextMenuOut {
	0% {
		opacity: 1;
		transform: scale(1);
	}

	to {
		opacity: 0;
		transform: scale(.9);
	}
}

.ContextMenu-module__qHrD2W__icon {
	justify-content: center;
	align-items: center;
	display: flex;
}

.Grid-module__HlBHsa__root {
	--grid-columns: 12;
	--grid-gap: 32px;
	grid-template-columns: repeat(var(--grid-columns), minmax(0, 1fr));
	grid-gap: var(--grid-gap);
	gap: var(--grid-gap);
	grid-template-areas: var(--grid-areas-default);
	display: grid;
}

@media (max-width: 1024px) {
	.Grid-module__HlBHsa__root {
		grid-template-areas: var(--grid-areas-laptop, var(--grid-areas-default));
	}
}

@media (max-width: 768px) {
	.Grid-module__HlBHsa__root {
		--grid-columns: 8;
		grid-template-areas: var(--grid-areas-tablet, var(--grid-areas-default));
	}
}

@media (max-width: 640px) {
	.Grid-module__HlBHsa__root {
		--grid-columns: 4;
		grid-template-areas: var(--grid-areas-mobile, var(--grid-areas-default));
	}
}

.Grid-module__HlBHsa__a {
	margin: var(--grid-a-margin, 0px);
	grid-area: a;
}

.Grid-module__HlBHsa__b {
	margin: var(--grid-b-margin, 0px);
	grid-area: b;
}

.Grid-module__HlBHsa__c {
	margin: var(--grid-c-margin, 0px);
	grid-area: c;
}

.Grid-module__HlBHsa__d {
	margin: var(--grid-d-margin, 0px);
	grid-area: d;
}

.Grid-module__HlBHsa__e {
	margin: var(--grid-e-margin, 0px);
	grid-area: e;
}

.Grid-module__HlBHsa__inline {
	display: inline-grid;
}

.Debug-module___vQtWq__root {
	z-index: var(--layer-debug);
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	animation: Debug-module___vQtWq__fadeIn .48s var(--ease-out-quint) forwards;
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Debug-module___vQtWq__grid {
	--color: var(--color-brand-bg);
	padding-left: var(--page-padding-left);
	padding-right: var(--page-padding-right);
	width: 100%;
	max-width: calc(var(--page-max-width) + var(--page-padding-left) + var(--page-padding-right));
	margin-left: auto;
	margin-right: auto;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

@keyframes Debug-module___vQtWq__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

.Debug-module___vQtWq__cursorLine {
	background: var(--color-orange);
	will-change: transform;
	height: 1px;
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
}

.Debug-module___vQtWq__middleLine {
	background: var(--color-orange);
	opacity: 1;
	width: 1px;
	position: fixed;
	top: 0;
	bottom: 0;
	left: 50%;
	transform: translate(-50%);
}

.Debug-module___vQtWq__column {
	opacity: .6;
	height: 100%;
	box-shadow: -1px 0 0 0 var(--color), 1px 0 0 0 var(--color);
	background: color-mix(in srgb, var(--color), transparent 80%);
	position: relative;
}

.Debug-module___vQtWq__column::after {
	background: var(--color-orange);
	width: 1px;
	position: absolute;
}

.Debug-module___vQtWq__column:first-child::after {
	content: "";
	top: 0;
	bottom: 0;
	left: 24px;
	right: auto;
}

.Debug-module___vQtWq__column:last-child::after {
	content: "";
	top: 0;
	bottom: 0;
	left: auto;
	right: 24px;
}

@media (max-width: 1024px) {
	.Debug-module___vQtWq__column:first-child::after,
	.Debug-module___vQtWq__column:last-child::after {
		content: none;
	}
}

@media (max-width: 768px) {
	.Debug-module___vQtWq__column:nth-child(1n + 9) {
		display: none;
	}
}

@media (max-width: 640px) {
	.Debug-module___vQtWq__column:nth-child(1n + 5) {
		display: none;
	}
}

.Debug-module___vQtWq__viewport {
	font-size: 12px;
	font-weight: var(--font-weight-semibold);
	border-radius: var(--rounded-full);
	background: var(--color-text-primary);
	color: var(--color-bg-primary);
	padding: 4px 8px;
	position: fixed;
	bottom: 16px;
	left: 50%;
	transform: translate(-50%);
}

.ThemeToggle-module__MbFuda__fadeIn {
	animation: .18s ThemeToggle-module__MbFuda__fadeIn;
}

@keyframes ThemeToggle-module__MbFuda__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

.ThemeToggle-module__MbFuda__toggleGroup {
	border: 1px solid var(--color-border-primary);
	margin-left: var(--page-padding-left);
	border-radius: 8px;
	padding: 2px;
	display: flex;
}

.ThemeToggle-module__MbFuda__toggleGroupItem {
	cursor: pointer;
	width: 24px;
	height: 22px;
	color: var(--color-border-tertiary);
	background: 0 0;
	border: none;
	border-radius: 5px;
	justify-content: center;
	align-items: center;
	padding: 0;
	transition: background .2s;
	display: flex;
}

.ThemeToggle-module__MbFuda__toggleGroupItem:hover {
	background: var(--color-bg-primary);
}

.ThemeToggle-module__MbFuda__toggleGroupItem svg {
	width: 14px;
	height: 14px;
}

.ThemeToggle-module__MbFuda__toggleGroupItem[data-state="on"] {
	background: var(--color-bg-quaternary);
	color: var(--color-text-primary);
}

.Image-module__CYTY7q__root {
	max-width: 100%;
	height: auto;
}

@supports (font: -apple-system-body) and ((-webkit-appearance: none) or (-moz-appearance: none) or (appearance: none)) {
	.Image-module__CYTY7q__root[loading="lazy"]:not([data-loaded="true"]) {
		clip-path: inset(.6px);
	}
}

html.js .Image-module__CYTY7q__root[data-fade="true"] {
	opacity: 0;
	-webkit-mask: var(--mask-start);
	-webkit-mask: var(--mask-start);
	mask: var(--mask-start);
	--mask-start: linear-gradient(to right, #000 25%, rgba(0, 0, 0, .9) 50%, transparent) 150% 0 / 400% no-repeat;
	--mask-end: linear-gradient(to right, #000 25%, rgba(0, 0, 0, .9) 50%, transparent) 0 / 400% no-repeat;
}

html.js .Image-module__CYTY7q__root[data-fade="true"][data-loaded="true"] {
	animation: .8s both Image-module__CYTY7q__load;
}

html.js [data-rmiz-modal-content] .Image-module__CYTY7q__root[data-fade="true"] {
	opacity: 1;
	animation: none;
	-webkit-mask: none;
	mask: none;
}

@keyframes Image-module__CYTY7q__load {
	to {
		opacity: 1;
		-webkit-mask: var(--mask-end);
		-webkit-mask: var(--mask-end);
		mask: var(--mask-end);
	}
}

.KBD-module__IfFsRa__root {
	min-width: auto;
	box-shadow: none;
	background: 0 0;
	border: none;
	justify-content: center;
	align-items: stretch;
	margin: 0;
	padding: 0;
	display: inline-flex;
}

.KBD-module__IfFsRa__root .KBD-module__IfFsRa__key {
	text-align: center;
	line-height: normal;
	font-weight: var(--font-weight-medium);
	justify-content: center;
	align-items: center;
	display: inline-flex;
}

:is(.KBD-module__IfFsRa__root .KBD-module__IfFsRa__key) + :is(.KBD-module__IfFsRa__root .KBD-module__IfFsRa__key) {
	margin-left: 4px;
}

.KBD-module__IfFsRa__root .KBD-module__IfFsRa__key[title="Ctrl"] {
	font-size: 10px;
}

.KBD-module__IfFsRa__root .KBD-module__IfFsRa__key.KBD-module__IfFsRa__keyWithPadding {
	padding: 0 4px;
}

.KBD-module__IfFsRa__widthAware .KBD-module__IfFsRa__key[title="Shift"],
.KBD-module__IfFsRa__widthAware .KBD-module__IfFsRa__key[title="Command"],
.KBD-module__IfFsRa__widthAware .KBD-module__IfFsRa__key[title="Control"],
.KBD-module__IfFsRa__widthAware .KBD-module__IfFsRa__key[title="Ctrl"],
.KBD-module__IfFsRa__widthAware .KBD-module__IfFsRa__key[title="Alt"] {
	text-align: left;
	min-width: 48px;
}

.KBD-module__IfFsRa__size-small {
	font-size: 10px;
}

.KBD-module__IfFsRa__size-small .KBD-module__IfFsRa__key {
	border-radius: 4px;
	min-width: 16px;
	min-height: 16px;
}

.KBD-module__IfFsRa__size-normal {
	font-size: 13px;
}

.KBD-module__IfFsRa__size-normal .KBD-module__IfFsRa__key {
	border-radius: 4px;
	min-width: 20px;
	min-height: 20px;
}

.KBD-module__IfFsRa__variant-normal > .KBD-module__IfFsRa__key {
	color: var(--color-text-secondary);
	background: var(--color-bg-quaternary);
	border: 1px solid var(--color-border-primary);
}

.KBD-module__IfFsRa__variant-glass > .KBD-module__IfFsRa__key {
	color: var(--color-text-primary);
	box-shadow: var(--shadow-low);
	background: rgba(255, 255, 255, .16);
	border: none;
}

[data-theme="light"] :is(.KBD-module__IfFsRa__variant-glass > .KBD-module__IfFsRa__key) {
	box-shadow: none;
	background: rgba(0, 0, 0, .08);
}

.Footer-module__Cy4DCa__footer {
	--footer-column-padding: var(--page-padding-inline);
	max-width: 100%;
	z-index: var(--layer-footer);
	background: var(--color-bg-primary);
	border-top: 1px solid var(--color-border-primary);
	position: relative;
}

.Footer-module__Cy4DCa__inner {
	max-width: var(--page-max-width);
	grid-column-gap: 32px;
	-moz-column-gap: 32px;
	grid-row-gap: 40px;
	grid-template-columns: repeat(6, var(--1fr));
	place-items: start;
	gap: 40px 32px;
	margin-left: auto;
	margin-right: auto;
	padding-top: 56px;
	padding-bottom: 56px;
	display: grid;
}

@media (max-width: 1024px) {
	.Footer-module__Cy4DCa__inner {
		grid-template-columns: auto repeat(5, var(--1fr));
	}
}

@media (max-width: 768px) {
	.Footer-module__Cy4DCa__inner {
		-moz-column-gap: 16px;
		grid-template-columns: repeat(3, var(--1fr));
		grid-template-rows: auto repeat(3, auto);
		column-gap: 16px;
	}
}

.Footer-module__Cy4DCa__section {
	padding-left: var(--footer-column-padding);
	padding-right: var(--footer-column-padding);
	width: 100%;
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
}

@media (max-width: 768px) {
	.Footer-module__Cy4DCa__section {
		font-size: var(--text-mini-size);
		line-height: var(--text-mini-line-height);
		letter-spacing: var(--text-mini-letter-spacing);
		padding-left: 0;
	}

	.Footer-module__Cy4DCa__section:nth-child(4) {
		padding-left: var(--footer-column-padding);
	}
}

.Footer-module__Cy4DCa__status {
	grid-column: 2 / -1;
}

@media (max-width: 768px) {
	.Footer-module__Cy4DCa__status {
		grid-column: 1 / -1;
	}
}

.Footer-module__Cy4DCa__logoWrapper {
	display: flex;
}

.Footer-module__Cy4DCa__logoWrapper:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	margin-left: var(--footer-column-padding);
}

.Footer-module__Cy4DCa__logoWrapper:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	margin-left: var(--footer-column-padding);
}

.Footer-module__Cy4DCa__logoWrapper:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	margin-left: var(--footer-column-padding);
}

.Footer-module__Cy4DCa__logoWrapper:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	margin-right: var(--footer-column-padding);
}

.Footer-module__Cy4DCa__logoWrapper:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	margin-right: var(--footer-column-padding);
}

.Footer-module__Cy4DCa__logoWrapper:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	margin-right: var(--footer-column-padding);
}

@media (max-width: 768px) {
	.Footer-module__Cy4DCa__logoWrapper {
		grid-area: 1 / 1 / 1 / -1;
	}
}

.Footer-module__Cy4DCa__sectionTitle {
	font: inherit;
	letter-spacing: inherit;
	font-weight: var(--font-weight-medium);
	color: var(--color-text-primary);
	margin-bottom: 24px;
}

@media (max-width: 768px) {
	.Footer-module__Cy4DCa__sectionTitle {
		margin-bottom: 16px;
	}
}

.Footer-module__Cy4DCa__sectionList {
	flex-direction: column;
	gap: 2px;
	margin: 0;
	padding: 0;
	list-style: none;
	display: flex;
}

.Footer-module__Cy4DCa__sectionItem {
	margin: 0;
}

.Footer-module__Cy4DCa__sectionLink {
	white-space: nowrap;
	align-items: center;
	width: 100%;
	min-height: 28px;
	display: flex;
}

@media (max-width: 768px) {
	.Footer-module__Cy4DCa__sectionLink {
		white-space: normal;
		white-space: initial;
	}
}

.Header-module__PXV_2W__header {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	isolation: isolate;
	top: 0;
	z-index: var(--layer-header);
	transform: translatex(calc(-1 * var(--removed-body-scroll-bar-size, 0px) / 2));
	-webkit-backdrop-filter: blur(var(--header-blur));
	backdrop-filter: blur(var(--header-blur));
	background: var(--header-bg);
	border-bottom: 1px solid var(--header-border);
	margin-left: auto;
	margin-right: auto;
	position: fixed;
	left: 0;
	right: 0;
}

.Header-module__PXV_2W__header::before {
	content: "";
	pointer-events: none;
	background: linear-gradient(180deg, var(--color-bg-primary) 0%, transparent 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

[data-theme="light"] .Header-module__PXV_2W__header::after {
	content: none;
}

.Header-module__PXV_2W__innerWrapper {
	height: var(--header-height);
	width: 100%;
	max-width: var(--page-max-width);
	padding-left: var(--page-padding-left);
	padding-right: var(--page-padding-right);
	align-items: center;
	margin-left: auto;
	margin-right: auto;
	display: flex;
	position: relative;
}

.Header-module__PXV_2W__innerWrapper > div {
	width: 100%;
}

.Header-module__PXV_2W__menuRoot {
	align-items: center;
	height: 100%;
	display: flex;
}

@media (max-width: 768px) {
	.Header-module__PXV_2W__menuRoot {
		flex-direction: column;
	}
}

.Header-module__PXV_2W__list {
	min-height: var(--header-height);
	align-items: center;
	gap: 8px;
	list-style: none;
	display: flex;
}

@media (max-width: 768px) {
	.Header-module__PXV_2W__list {
		justify-content: flex-start;
		gap: 16px;
	}
}

.Header-module__PXV_2W__buttonItem {
	justify-content: center;
	align-items: center;
	display: flex;
}

.Header-module__PXV_2W__buttonItem a,
.Header-module__PXV_2W__buttonItem span {
	width: 100%;
}

.Header-module__PXV_2W__item {
	white-space: nowrap;
	margin: 0;
}

.Header-module__PXV_2W__anchor {
	height: 32px;
	font-size: 13px;
	font-weight: var(--font-weight-medium);
	color: var(--color-text-tertiary);
	border-radius: var(--radius-8);
	transition: var(--speed-quickTransition) var(--ease-out-quad);
	--anchor-glass-bg: rgba(255, 255, 255, .08);
	background: 0 0;
	justify-content: center;
	align-items: center;
	padding: 0 12px;
	transition-property: color, background;
	display: flex;
	position: relative;
}

[data-theme="light"] .Header-module__PXV_2W__anchor {
	--anchor-glass-bg: rgba(0, 0, 0, .08);
}

.Header-module__PXV_2W__anchor[data-state="open"] {
	color: var(--color-text-primary);
	background: var(--anchor-glass-bg);
}

@media (any-hover: hover) {
	.Header-module__PXV_2W__anchor:hover {
		color: var(--color-text-primary);
		background: var(--anchor-glass-bg);
	}
}

.Header-module__PXV_2W__item {
	list-style: none;
}

.Header-module__PXV_2W__item[data-state="open"] {
	color: var(--color-text-primary);
	background: var(--color-bg-quaternary);
}

[data-theme="light"] .Header-module__PXV_2W__item {
	color: rgba(0, 0, 0, .8);
}

.Header-module__PXV_2W__logoItem {
	color: var(--color-text-primary);
	flex: 1;
	justify-content: flex-start;
	display: flex;
}

.Header-module__PXV_2W__buttons {
	flex: 1;
	justify-content: flex-end;
	gap: 8px;
	display: flex;
}

.Header-module__PXV_2W__logoLink {
	border-radius: 6px;
	justify-content: flex-start;
	align-items: center;
	height: 32px;
	margin-left: -8px;
	padding: 0 8px;
	display: flex;
}

.Header-module__PXV_2W__mobileItem {
	display: none;
}

.Header-module__PXV_2W__mobileItem.Header-module__PXV_2W__mobileItem {
	margin-left: calc(-1 * var(--page-padding-right) + 8px);
}

@media (max-width: 768px) {
	.Header-module__PXV_2W__mobileItem {
		display: block;
	}
}

.Header-module__PXV_2W__mobileMenuTrigger {
	height: var(--header-height);
	aspect-ratio: 1;
	outline: none;
	justify-content: center;
	align-items: center;
	margin-right: -24px;
	display: flex;
}

.Header-module__PXV_2W__mobileMenuTrigger[data-state="open"] > svg > rect:first-of-type {
	transform: rotate(45deg) !important;
}

.Header-module__PXV_2W__mobileMenuTrigger[data-state="open"] > svg > rect:last-of-type {
	transform: rotate(-45deg) !important;
}

.Header-module__PXV_2W__mobileMenuContent {
	top: calc(var(--header-height) + 1px);
	height: calc(100 * var(--dvh) - var(--header-height) - 1px);
	background: var(--header-bg);
	-webkit-backdrop-filter: blur(var(--header-blur));
	backdrop-filter: blur(var(--header-blur));
	z-index: var(--layer-dialog);
	outline: none;
	flex-grow: 1;
	padding-top: 32px;
	padding-bottom: 32px;
	padding-left: 24px;
	padding-right: 24px;
	display: none;
	position: fixed;
	left: 0;
	right: 0;
	overflow-y: auto;
}

@media (max-width: 768px) {
	.Header-module__PXV_2W__mobileMenuContent {
		flex-direction: column;
		display: flex;
	}
}

@media (prefers-reduced-motion: no-preference) {
	.Header-module__PXV_2W__mobileMenuContent[data-state="open"] {
		animation: .18s both Header-module__PXV_2W__mobileMenuIn;
	}

	.Header-module__PXV_2W__mobileMenuContent[data-state="closed"] {
		animation: .18s both Header-module__PXV_2W__mobileMenuOut;
	}
}

@keyframes Header-module__PXV_2W__mobileMenuIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes Header-module__PXV_2W__mobileMenuOut {
	0% {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}

.Header-module__PXV_2W__mobileMenuList {
	flex-direction: column;
	gap: 12px;
	margin-top: 20px;
	list-style-type: none;
	display: flex;
}

.Header-module__PXV_2W__mobileMenuList li {
	margin: 0;
}

.Header-module__PXV_2W__mobileMenuList li a:active {
	color: var(--color-text-tertiary);
}

@media (any-hover: hover) {
	.Header-module__PXV_2W__mobileMenuList li a:hover {
		color: var(--color-text-tertiary);
	}
}

.Header-module__PXV_2W__trigger {
	isolation: isolate;
	position: relative;
}

.Header-module__PXV_2W__trigger::before {
	content: "";
	z-index: 0;
	position: absolute;
	top: 0;
	bottom: 0;
	left: -8px;
	right: -8px;
}

.Header-module__PXV_2W__trigger[data-state="open"]::after {
	content: "";
	height: 32px;
	position: absolute;
	top: 100%;
	left: -32px;
	right: -32px;
}

.Header-module__PXV_2W__content {
	transform-origin: top;
	will-change: transform;
	padding: 8px;
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
}

.Header-module__PXV_2W__content.Header-module__PXV_2W__productNav,
.Header-module__PXV_2W__content.Header-module__PXV_2W__resourcesNav {
	width: -moz-fit-content;
	width: fit-content;
	max-width: 693px;
}

.Header-module__PXV_2W__content > div {
	height: 100%;
}

@media (max-width: 640px) {
	.Header-module__PXV_2W__content {
		display: none;
	}
}

@media (prefers-reduced-motion: no-preference) {
	.Header-module__PXV_2W__content {
		animation: var(--duration) var(--ease-in-out-quad) both;
		--duration: .18s;
		--anim-amount: 48px;
	}

	.Header-module__PXV_2W__content[data-motion="from-start"] {
		animation-name: Header-module__PXV_2W__enterFromLeft;
	}

	.Header-module__PXV_2W__content[data-motion="from-end"] {
		animation-name: Header-module__PXV_2W__enterFromRight;
	}

	.Header-module__PXV_2W__content[data-motion="to-start"] {
		animation-name: Header-module__PXV_2W__exitToLeft;
	}

	.Header-module__PXV_2W__content[data-motion="to-end"] {
		animation-name: Header-module__PXV_2W__exitToRight;
	}
}

.Header-module__PXV_2W__dropdownItem {
	--description: var(--color-text-tertiary);
	background: var(--color-bg-tertiary);
	border-radius: 10px;
	align-items: center;
	gap: 8px;
	width: 100%;
	height: 100%;
	padding: 16px;
	line-height: normal;
	display: flex;
}

.Header-module__PXV_2W__dropdownItem > svg {
	fill: currentColor;
	grid-area: icon;
	width: 16px;
	height: 16px;
}

@media (any-hover: hover) {
	.Header-module__PXV_2W__dropdownItem:hover {
		--description: var(--color-text-secondary);
		background: var(--color-bg-quaternary);
	}
}

.Header-module__PXV_2W__dropdownHighlight {
	--description: var(--color-text-tertiary);
	border: 1px solid var(--color-border-translucent);
	width: 100%;
	height: 100%;
	box-shadow: var(--shadow-low);
	transition: var(--speed-regularTransition) ease;
	background: rgba(255, 255, 255, .03);
	border-radius: 8px;
	padding: 16px;
	transition-property: background;
	display: flex;
	position: relative;
	overflow: hidden;
}

@media (any-hover: hover) {
	.Header-module__PXV_2W__dropdownHighlight:hover {
		--description: var(--color-text-secondary);
		background: var(--color-bg-level-3);
	}
}

.Header-module__PXV_2W__viewport {
	height: max(var(--radix-navigation-menu-viewport-height), 252px);
	width: var(--radix-navigation-menu-viewport-width);
	max-width: calc(100vw - var(--page-padding-left) - var(--page-padding-right));
	-webkit-backdrop-filter: blur(32px);
	backdrop-filter: blur(32px);
	transform-origin: top;
	background: rgba(8, 9, 10, .9);
	border: 1px solid rgba(255, 255, 255, .08);
	border-radius: 14px;
	padding: 8px;
	transition: height .22s;
	position: relative;
	overflow: hidden;
	box-shadow: 0 8px 32px #08090a;
}

[data-theme="light"] .Header-module__PXV_2W__viewport {
	background: rgba(255, 255, 255, .9);
	border: 1px solid rgba(0, 0, 0, .08);
	box-shadow: 0 8px 32px rgba(8, 9, 10, .05);
}

.Header-module__PXV_2W__viewport::before {
	content: "";
	background: var(--color-bg-translucent);
	border: 1px solid var(--color-border-translucent);
	border-radius: 6px;
	height: 234px;
	position: absolute;
	top: 8px;
	left: 8px;
	right: 8px;
}

@media (prefers-reduced-motion: no-preference) {
	.Header-module__PXV_2W__viewport {
		animation: .18s both Header-module__PXV_2W__scaleIn;
	}

	.Header-module__PXV_2W__viewport[data-state="closed"] {
		animation: .18s both Header-module__PXV_2W__scaleOut;
	}
}

.Header-module__PXV_2W__viewportPosition {
	width: 100%;
	z-index: var(--layer-max);
	top: calc(var(--header-height) - 8px);
	justify-content: center;
	display: flex;
	position: fixed;
	left: 0;
}

.Header-module__PXV_2W__highlightDescription {
	font-weight: var(--font-weight-normal);
	font-weight: var(--font-weight-normal);
	transition: var(--speed-regularTransition) ease;
	transition-property: color;
}

.Header-module__PXV_2W__contentFooter {
	justify-content: space-between;
	max-width: 100%;
	padding: 16px 16px 11px;
	display: flex;
}

@keyframes Header-module__PXV_2W__enterFromRight {
	0% {
		opacity: 0;
		transform: translatex(var(--anim-amount));
	}

	to {
		opacity: 1;
		transform: translate(0);
	}
}

@keyframes Header-module__PXV_2W__enterFromLeft {
	0% {
		opacity: 0;
		transform: translatex(calc(-1 * var(--anim-amount)));
	}

	to {
		opacity: 1;
		transform: translate(0);
	}
}

@keyframes Header-module__PXV_2W__exitToRight {
	0% {
		opacity: 1;
		transform: translate(0);
	}

	to {
		opacity: 0;
		transform: translatex(var(--anim-amount));
	}
}

@keyframes Header-module__PXV_2W__exitToLeft {
	0% {
		opacity: 1;
		transform: translate(0);
	}

	to {
		opacity: 0;
		transform: translatex(calc(-1 * var(--anim-amount)));
	}
}

@keyframes Header-module__PXV_2W__scaleIn {
	0% {
		opacity: 0;
		transform: scale(.98);
	}

	to {
		opacity: 1;
		transform: scale(1);
	}
}

@keyframes Header-module__PXV_2W__scaleOut {
	0% {
		opacity: 1;
		transform: scale(1);
	}

	to {
		opacity: 0;
		transform: scale(.98);
	}
}

@keyframes Header-module__PXV_2W__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes Header-module__PXV_2W__fadeOut {
	0% {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}

.Header-module__PXV_2W__subnav {
	height: 100%;
}

.Header-module__PXV_2W__subItems {
	padding: 20px 28px 32px;
}

.Header-module__PXV_2W__inlineLink {
	transition: none;
	position: relative;
}

.Header-module__PXV_2W__inlineLink::after,
.Header-module__PXV_2W__inlineLink::before {
	content: "";
	top: -8px;
	bottom: -8px;
	left: -8px;
	right: -8px;
	position: absolute;
	left: -12px;
	right: -12px;
}

.Header-module__PXV_2W__inlineLink::after {
	background: var(--color-bg-translucent);
	opacity: 0;
	border-radius: 8px;
}

@media (any-hover: hover) {
	.Header-module__PXV_2W__inlineLink:hover {
		color: var(--color-text-primary);
	}

	.Header-module__PXV_2W__inlineLink:hover::after {
		opacity: 1;
	}
}

.Header-module__PXV_2W__inlineLink:active::after {
	opacity: 1;
}

.Header-module__PXV_2W__featureGrid {
	grid-template-columns: 236px 1px 440px;
	display: grid;
}

.Header-module__PXV_2W__featureLink {
	padding-left: 18px;
}

.Header-module__PXV_2W__subGrid {
	grid-gap: 16px 28px;
	grid-template-columns: 1fr 1fr;
	gap: 16px 28px;
	display: grid;
}

.Header-module__PXV_2W__divider {
	background: var(--color-border-translucent);
	width: 1px;
	height: 100%;
	display: inline-block;
}

.Header-module__PXV_2W__ghostButton {
	color: var(--color-text-tertiary);
}

@media (any-hover: hover) {
	.Header-module__PXV_2W__ghostButton:hover {
		color: var(--color-text-primary);
	}
}

.IssueLabel-module__mrTEVW__root {
	font-size: var(--font-size-small);
	font-weight: var(--font-weight-medium);
	background: var(--color-bg-primary);
	border-radius: var(--radius-rounded);
	border: 1px solid var(--color-border-secondary);
	align-items: center;
	gap: 6px;
	height: 25px;
	padding: 0 8px;
	display: inline-flex;
	position: relative;
}

.IssueLabel-module__mrTEVW__root::before {
	content: "";
	background: var(--color);
	border-radius: var(--radius-circle);
	flex-shrink: 0;
	width: 9px;
	height: 9px;
}

.page-module__cJlK9G__resources {
	grid-gap: 24px;
	grid-template-columns: 1fr 1fr;
	grid-auto-rows: auto;
	gap: 24px;
	max-width: 840px;
	margin: 0 auto;
	display: grid;
}

@media (max-width: 640px) {
	.page-module__cJlK9G__resources {
		grid-template-columns: 1fr;
	}
}

.page-module__cJlK9G__container {
	max-width: 792px;
	margin-left: auto;
	margin-right: auto;
}

.page-module__cJlK9G__moreResources {
	-moz-column-gap: 88px;
	gap: 40px 88px;
	padding: 0 32px;
}

.page-module__cJlK9G__moreResources > .page-module__cJlK9G__resource {
	padding: 24px 0;
}

@media (max-width: 640px) {
	.page-module__cJlK9G__moreResources {
		gap: 0;
	}

	.page-module__cJlK9G__moreResources > .page-module__cJlK9G__resource:not(:last-child) {
		border-bottom: 1px solid var(--color-border-translucent);
	}
}

.page-module__cJlK9G__card {
	background: rgba(255, 255, 255, .03);
	border: 1px solid rgba(255, 255, 255, .08);
	border-radius: 16px;
	padding: 32px;
}

.Badge-module__3073kG__root {
	--height: 24px;
	height: var(--height);
	vertical-align: middle;
	line-height: normal;
	font-weight: var(--font-weight-semibold);
	font-feature-settings: "tnum";
	font-variant-numeric: tabular-nums;
	border: 1.5px solid transparent;
	border-radius: 4px;
	justify-content: center;
	align-items: center;
	display: inline-flex;
	position: relative;
}

.Badge-module__3073kG__size-small {
	--height: 20px;
	border-radius: 4px;
	padding: 0 4px;
	font-size: 12px;
}

.Badge-module__3073kG__size-regular {
	--height: 24px;
	border-radius: 7px;
	padding: 0 6px;
	font-size: 12px;
}

.Badge-module__3073kG__size-large {
	--height: 28px;
	border-radius: 6px;
	padding: 0 8px;
	font-size: 14px;
}

.Badge-module__3073kG__size-xxx-large {
	--height: 48px;
	font-size: 24px;
	font-weight: var(--font-weight-semibold);
	border-radius: 12px;
	padding: 0 12px;
}

.Badge-module__3073kG__variant-regular {
	color: var(--color-brand-text);
	background: var(--color-brand-bg);
}

.Badge-module__3073kG__variant-secondary {
	color: var(--color-text-secondary);
	border-color: var(--color-border-secondary);
	background: 0 0;
}

.Badge-module__3073kG__variant-tertiary {
	color: var(--color-text-tertiary);
	border-color: var(--color-border-tertiary);
	background: 0 0;
}

.Badge-module__3073kG__variant-basic {
	color: var(--color-text-secondary);
	border-color: var(--color-border-secondary);
	background: 0 0;
}

.Badge-module__3073kG__variant-business {
	--gradientBorder-gradient: linear-gradient(285.49deg, #bac0cb -14.61%, #767caf 106.06%);
	--gradientBorder-size: 2px;
	color: #a1a7c1;
	background: 0 0;
	border: none;
}

.Badge-module__3073kG__variant-enterprise {
	--gradientBorder-gradient: linear-gradient(92.88deg, #be05ff 9.16%, #a954ff 43.89%, #a771ff 64.72%);
	color: #a771ff;
	background: 0 0;
	border: none;
}

.Bleed-module__jzJzda__root {
	width: 100vw;
	margin-left: -50vw;
	margin-right: -50vw;
	position: relative;
	left: 50%;
	right: 50%;
}

.Blockquote-module__x7V-RG__root {
	flex-direction: column;
	gap: 24px;
	padding-left: 24px;
	display: flex;
	position: relative;
}

.Blockquote-module__x7V-RG__root.Blockquote-module__x7V-RG__cite {
	gap: 40px;
}

.Blockquote-module__x7V-RG__root::before {
	content: "";
	background: var(--color-border-secondary);
	border-radius: var(--radius-rounded);
	width: 2px;
	height: 100%;
	position: absolute;
	left: 0;
}

.Blockquote-module__x7V-RG__quotes {
	quotes: "“" "”" "‘" "’";
}

.Blockquote-module__x7V-RG__quotes::before {
	content: open-quote;
}

.Blockquote-module__x7V-RG__quotes::after {
	content: close-quote;
}

.Blockquote-module__x7V-RG__footer {
	margin-top: auto;
}

.Blockquote-module__x7V-RG__cite {}

.CTA-module__MsS1gq__sectionPrefooter {
	-webkit-user-select: text;
	-moz-user-select: text;
	user-select: text;
	padding-top: 96px;
	padding-bottom: 96px;
}

@media (max-width: 640px) {
	.CTA-module__MsS1gq__sectionPrefooter {
		padding-top: 48px;
		padding-bottom: 48px;
	}
}

.CTA-module__MsS1gq__actions {
	justify-content: flex-end;
	align-items: center;
	gap: 8px;
	display: flex;
}

.CTA-module__MsS1gq__actions.CTA-module__MsS1gq__fadeIn {
	opacity: 0;
	animation: .5s .1s forwards CTA-module__MsS1gq__fadeIn;
}

@media (max-width: 640px) {
	.CTA-module__MsS1gq__actions {
		flex-direction: column;
		align-items: stretch;
	}
}

@keyframes CTA-module__MsS1gq__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

.typography-module__c6hvxG__h1,
.typography-module__c6hvxG__h1Responsive {
	letter-spacing: -.0325em;
	font-variation-settings: "opsz" 28;
	font-size: 56px;
	font-weight: 538;
	line-height: 1.1;
}

@media (max-width: 640px) {
	.typography-module__c6hvxG__h1Responsive {
		letter-spacing: -.015em;
		font-size: 40px;
		line-height: 44px;
	}
}

.typography-module__c6hvxG__subtitle {
	letter-spacing: 0;
	font-size: 17px;
	line-height: 24.5px;
	font-weight: var(--font-weight-medium);
	color: var(--color-text-tertiary);
}

.typography-module__c6hvxG__bentoTitle {
	letter-spacing: -.37px;
	font-size: 21px;
	line-height: 28px;
	font-weight: var(--font-weight-medium);
}

.typography-module__c6hvxG__bentoSubtitle {
	letter-spacing: 0;
	color: var(--color-text-tertiary);
	font-size: 17px;
	line-height: 24.5px;
}

.Carousel-module__imM5Ra__content {
	overscroll-behavior-x: contain;
	scroll-snap-stop: always;
	padding-block: calc(var(--focus-ring-width) + var(--focus-ring-offset));
	overflow-x: scroll;
	overflow-y: hidden;
}

.Carousel-module__imM5Ra__content:not(.Carousel-module__imM5Ra__disableSnap) {
	scroll-snap-type: x mandatory;
}

.Carousel-module__imM5Ra__inner {
	grid-gap: var(--Carousel-gap);
	gap: var(--Carousel-gap);
	grid-auto-flow: column;
	min-width: -moz-fit-content;
	min-width: fit-content;
	display: grid;
}

.Carousel-module__imM5Ra__item {
	scroll-snap-align: var(--align);
}

.Carousel-module__imM5Ra__variant-inset {
	--edge: calc((100vw - var(--page-max-width)) / 2);
	--min-edge: calc(var(--edge) - var(--Carousel-gap));
	--min-padding: calc(var(--page-padding-left) - var(--Carousel-gap));
}

.Carousel-module__imM5Ra__variant-inset.Carousel-module__imM5Ra__align-start .Carousel-module__imM5Ra__content {
	scroll-padding-inline-start: max(var(--page-padding-left), var(--edge));
}

.Carousel-module__imM5Ra__variant-inset .Carousel-module__imM5Ra__inner::before,
.Carousel-module__imM5Ra__variant-inset .Carousel-module__imM5Ra__inner::after {
	content: "";
	min-width: max(var(--min-edge), var(--min-padding));
	display: block;
}

.Carousel-module__imM5Ra__variant-normal {
	max-width: 100%;
}

.Carousel-module__imM5Ra__align-center {
	--align: center;
}

.Carousel-module__imM5Ra__align-start {
	--align: start;
}

.Carousel-module__imM5Ra__align-end {
	--align: end;
}

.HomepageCarousel-module__U2qd5W__workflowCard {
	background: var(--color-bg-level-2);
	aspect-ratio: 336 / 469;
	width: 336px;
	max-width: calc(100vw - var(--page-padding-left) - var(--page-padding-right) - 32px);
}

.HomepageCarousel-module__U2qd5W__workflowCard [type="button"] {
	background: 0 0;
}

.HomepageCarousel-module__U2qd5W__workflowCard::after {
	content: "";
	pointer-events: none;
	border: 1px solid var(--color-border-translucent);
	border-radius: inherit;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.partner-page-module__DbzxWq__logoWrapper {
	background: linear-gradient(rgba(255, 255, 255, .05) 0%, rgba(255, 255, 255, 0) 100%);
	border-radius: 24px;
	place-items: center;
	width: 112px;
	height: 112px;
	display: grid;
	position: relative;
}

.partner-page-module__DbzxWq__logoWrapper::after {
	content: "";
	border-radius: inherit;
	pointer-events: none;
	border: 1px solid var(--color-border-translucent);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.partner-page-module__DbzxWq__terms bold,
.partner-page-module__DbzxWq__terms strong {
	color: var(--color-text-primary);
	display: block;
}

.partner-page-module__DbzxWq__grid {
	padding-bottom: 128px;
}

@media (max-width: 640px) {
	.partner-page-module__DbzxWq__grid {
		padding-bottom: 96px;
	}
}

.partner-page-module__DbzxWq__grid .partner-page-module__DbzxWq__heroImageContainer {
	margin: 0 -24px -300px;
}

@media (max-width: 1024px) {
	.partner-page-module__DbzxWq__grid .partner-page-module__DbzxWq__heroImageContainer {
		margin: 0 0 -300px;
	}
}

@media (max-width: 768px) {
	.partner-page-module__DbzxWq__grid .partner-page-module__DbzxWq__heroImageContainer {
		margin: 0;
	}
}

.partner-page-module__DbzxWq__heroImageBackgroundContainer {
	box-shadow: 0px 0px 64px 0px var(--color-bg-primary);
	position: relative;
}

.partner-page-module__DbzxWq__heroImageBackground {
	border: 1px solid var(--color-border-primary);
	-webkit-mask-image: linear-gradient(180deg, var(--mask-visible) 20%, var(--mask-invisible) 100%);
	-webkit-mask-image: linear-gradient(180deg, var(--mask-visible) 20%, var(--mask-invisible) 100%);
	mask-image: linear-gradient(180deg, var(--mask-visible) 20%, var(--mask-invisible) 100%);
	isolation: isolate;
	contain: strict;
	will-change: transform;
	box-shadow: 0px 0px 64px 0px var(--color-bg-primary);
	border-radius: 12px;
}

@media (max-width: 768px) {
	.partner-page-module__DbzxWq__heroImageBackground {
		-webkit-mask-image: linear-gradient(to bottom, var(--mask-visible) 40%, var(--mask-invisible) 80%);
		-webkit-mask-image: linear-gradient(to bottom, var(--mask-visible) 40%, var(--mask-invisible) 80%);
		mask-image: linear-gradient(to bottom, var(--mask-visible) 40%, var(--mask-invisible) 80%);
	}
}

.partner-page-module__DbzxWq__grid .partner-page-module__DbzxWq__heroImageOverlay {
	border: 1px solid var(--color-border-primary);
	isolation: isolate;
	width: 100%;
	max-width: 94%;
	-webkit-mask-image: linear-gradient(to bottom, var(--mask-visible) 30%, var(--mask-invisible) 100%);
	-webkit-mask-image: linear-gradient(to bottom, var(--mask-visible) 30%, var(--mask-invisible) 100%);
	mask-image: linear-gradient(to bottom, var(--mask-visible) 30%, var(--mask-invisible) 100%);
	box-shadow: var(--shadow-high);
	-webkit-backdrop-filter: blur(8px);
	backdrop-filter: blur(8px);
	border-radius: 12px;
	margin-left: auto;
	display: flex;
	transform: translatey(164px);
}

@media (max-width: 768px) {
	.partner-page-module__DbzxWq__grid .partner-page-module__DbzxWq__heroImageOverlay {
		max-width: 100%;
		transform: none;
	}
}

.partner-page-module__DbzxWq__subtitle {
	text-wrap: balance;
	width: 100%;
	max-width: 520px;
	margin: 0 auto;
}

.partner-page-module__DbzxWq__hero {
	position: relative;
}

.partner-page-module__DbzxWq__heroGlow {
	background: var(--color-text-primary);
	filter: blur(64px);
	opacity: .04;
	pointer-events: none;
	width: 100%;
	height: 560px;
	position: absolute;
	top: 65%;
}

.partner-page-module__DbzxWq__quote {
	flex-direction: column;
	align-items: center;
	gap: 8px;
	display: flex;
}

.partner-page-module__DbzxWq__cardsLayout {
	padding-left: 0 !important;
	padding-right: 0 !important;
}

@media (max-width: 640px) {
	.partner-page-module__DbzxWq__cardsLayout {
		padding-inline: var(--page-padding-inline) !important;
	}
}

.partner-page-module__DbzxWq__step {
	border-bottom: 1px solid var(--color-line-tertiary);
	margin-bottom: 24px;
	padding-bottom: 24px;
	margin-left: 0;
	margin-right: 0;
	padding-left: 0;
	padding-right: 0;
}

.partner-page-module__DbzxWq__blockContent {
	display: inline-block;
}

.partner-page-module__DbzxWq__blockContent a {
	color: inherit;
}

.partner-page-module__DbzxWq__fadeLeft::before,
.partner-page-module__DbzxWq__fadeRight::before {
	content: "";
	pointer-events: none;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.partner-page-module__DbzxWq__fadeLeft::before {
	background: linear-gradient(90deg, var(--color-bg-level-1) 0%, transparent 100%);
	left: -1px;
}

.partner-page-module__DbzxWq__fadeRight::before {
	background: linear-gradient(90deg, transparent 0%, var(--color-bg-level-1) 100%);
	right: -1px;
}

.Dialog-module__iW3PxW__document {
	background: var(--color-bg-primary);
	border: 1px solid var(--color-border-translucent);
	border-radius: 8px;
	position: relative;
}

.Dialog-module__iW3PxW__content {
	z-index: var(--layer-dialog);
	position: fixed;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

.Dialog-module__iW3PxW__content.Dialog-module__iW3PxW__variant-video[data-state="open"] {
	animation: .18s Dialog-module__iW3PxW__dialogOpen;
}

.Dialog-module__iW3PxW__content.Dialog-module__iW3PxW__variant-video[data-state="closed"] {
	animation: .18s Dialog-module__iW3PxW__dialogClose;
}

.Dialog-module__iW3PxW__content.Dialog-module__iW3PxW__variant-video {
	width: 100vw;
	max-width: calc(100vw - var(--page-padding-left) - var(--page-padding-right));
	justify-content: center;
	align-items: center;
	max-height: calc(100vh - 48px);
	display: flex;
	pointer-events: none !important;
}

.Dialog-module__iW3PxW__overlay {
	z-index: var(--layer-dialog-overlay);
	background: var(--color-overlay-primary);
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Dialog-module__iW3PxW__overlay[data-state="open"] {
	animation: .18s Dialog-module__iW3PxW__fadeIn;
}

.Dialog-module__iW3PxW__overlay[data-state="closed"] {
	animation: .18s Dialog-module__iW3PxW__fadeOut;
}

.Dialog-module__iW3PxW__body {
	width: 100%;
	height: 100%;
	padding: 24px;
	overflow: auto;
}

@media (max-width: 768px) {
	.Dialog-module__iW3PxW__body {
		padding: 16px;
	}
}

.Dialog-module__iW3PxW__header {
	border-bottom: 1px solid var(--color-border-translucent);
	flex-shrink: 0;
	align-items: center;
	min-height: 56px;
	padding: 0 24px;
	display: flex;
}

@media (max-width: 768px) {
	.Dialog-module__iW3PxW__header {
		padding: 0 16px;
	}
}

.Dialog-module__iW3PxW__footer {
	border-top: 1px solid var(--color-border-translucent);
	flex-shrink: 0;
	align-items: center;
	min-height: 56px;
	padding: 0 24px;
	display: flex;
}

@media (max-width: 768px) {
	.Dialog-module__iW3PxW__footer {
		padding: 0 16px;
	}
}

@keyframes Dialog-module__iW3PxW__dialogOpen {
	0% {
		opacity: 0;
		transform: translate(-50%, -49%) scale(.95);
	}

	to {
		opacity: 1;
		transform: translate(-50%, -50%);
	}
}

@keyframes Dialog-module__iW3PxW__dialogClose {
	0% {
		opacity: 1;
		transform: translate(-50%, -50%);
	}

	to {
		opacity: 0;
		transform: translate(-50%, -49%) scale(.95);
	}
}

@keyframes Dialog-module__iW3PxW__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes Dialog-module__iW3PxW__fadeOut {
	0% {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}

.Collapsibles-module__bBbCPG__root {
	--title-line-height: 24px;
	--padding: 16px;
}

.Collapsibles-module__bBbCPG__root + .Collapsibles-module__bBbCPG__root {
	border-top: 1px solid var(--color-border-translucent);
}

.Collapsibles-module__bBbCPG__root:target {
	--bg: var(--color-bg-tertiary);
	--border: var(--color-border-tertiary);
	animation: Collapsibles-module__bBbCPG__highlight 6s var(--ease-in-out-quad);
}

.Collapsibles-module__bBbCPG__root.Collapsibles-module__bBbCPG__variant-default .Collapsibles-module__bBbCPG__trigger {
	flex-direction: row-reverse;
}

.Collapsibles-module__bBbCPG__root.Collapsibles-module__bBbCPG__variant-default .Collapsibles-module__bBbCPG__chevron {
	margin-left: auto;
	margin-right: 0;
}

.Collapsibles-module__bBbCPG__permalink {
	color: var(--color-text-tertiary);
	opacity: 0;
	place-items: center;
	margin-left: auto;
	transition: opacity .12s;
	display: grid;
}

.Collapsibles-module__bBbCPG__permalink svg {
	fill: currentColor;
}

@media (any-hover: hover) {
	.Collapsibles-module__bBbCPG__permalink:hover {
		color: var(--color-text-primary);
	}

	.Collapsibles-module__bBbCPG__root:hover .Collapsibles-module__bBbCPG__permalink {
		opacity: 1;
		visibility: visible;
	}
}

@media (any-hover: none) {
	.Collapsibles-module__bBbCPG__permalink[data-collapsible-open="true"] {
		opacity: 1;
		visibility: visible;
	}
}

.Collapsibles-module__bBbCPG__permalink:focus-visible {
	opacity: 1;
	visibility: visible;
}

.Collapsibles-module__bBbCPG__header {
	align-items: baseline;
	display: flex;
}

.Collapsibles-module__bBbCPG__trigger {
	width: 100%;
	padding: var(--padding) 0;
	border-radius: var(--radius-8);
	text-align: start;
	color: var(--color-text-primary);
	font-weight: var(--font-weight-medium);
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	flex: 1;
	display: flex;
}

.Collapsibles-module__bBbCPG__trigger[data-state="open"] .Collapsibles-module__bBbCPG__chevron {
	transform: rotate(90deg);
}

.Collapsibles-module__bBbCPG__chevron {
	height: var(--title-line-height);
	color: var(--color-text-quaternary);
	flex-shrink: 0;
	align-items: center;
	margin-right: 8px;
	transition: transform .12s;
	display: flex;
}

.Collapsibles-module__bBbCPG__content {
	color: var(--color-text-secondary);
	overflow: hidden;
}

.Collapsibles-module__bBbCPG__contentOpacity {
	padding-left: 24px;
	padding-bottom: var(--padding);
}

.Collapsibles-module__bBbCPG__contentOpacity.Collapsibles-module__bBbCPG__contentOpacity-default {
	padding-left: 0;
}

@keyframes Collapsibles-module__bBbCPG__highlight {
	20%,
	80% {
		background-color: var(--bg);
		border-color: var(--border);
	}
}

.Table-module__TXelja__root {
	width: 100%;
	padding-top: 12px;
	padding-bottom: 12px;
	overflow-x: auto;
}

.Table-module__TXelja__table {
	border-collapse: separate;
	border-spacing: 0;
	width: 100%;
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
}

.Table-module__TXelja__thead tr {
	border-bottom: none;
}

.Table-module__TXelja__th {
	text-align: left;
	color: var(--color-text-primary);
	font-weight: var(--font-weight-semibold);
	white-space: nowrap;
	border-bottom: 1px solid var(--color-border-primary);
	padding: 8px 0;
}

.Table-module__TXelja__td {
	color: var(--color-text-secondary);
	border-bottom: 1px solid var(--color-bg-tertiary);
	vertical-align: top;
	min-width: 180px;
	padding-top: 12px;
	padding-bottom: 12px;
}

.Table-module__TXelja__td:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-right: 24px;
}

.Table-module__TXelja__td:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-right: 24px;
}

.Table-module__TXelja__td:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-right: 24px;
}

.Table-module__TXelja__td:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 24px;
}

.Table-module__TXelja__td:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 24px;
}

.Table-module__TXelja__td:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 24px;
}

.Table-module__TXelja__tr:last-child .Table-module__TXelja__td {
	border-bottom: none;
}

.Tabs-module__JEJbCa__root {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	padding-top: 12px;
	padding-bottom: 24px;
	overflow: hidden;
}

.Tabs-module__JEJbCa__list {
	white-space: nowrap;
	align-items: center;
	gap: 24px;
	height: 44px;
	display: flex;
	overflow-x: auto;
	overflow-y: hidden;
}

.Tabs-module__JEJbCa__trigger {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	cursor: pointer;
	height: 100%;
	color: var(--color-text-tertiary);
	text-align: center;
	font-weight: var(--font-weight-medium);
	transition: color .18s var(--ease-out-quad);
	align-items: center;
	gap: 8px;
	display: flex;
	position: relative;
}

.Tabs-module__JEJbCa__trigger > svg {
	fill: currentColor;
}

.Tabs-module__JEJbCa__trigger::after {
	content: "";
	background: var(--color-text-primary);
	border-radius: var(--rounded-full);
	opacity: 0;
	height: 1px;
	transition: opacity .18s var(--ease-out-quad);
	position: absolute;
	bottom: 0;
	left: 0;
	right: 0;
}

@media (any-hover: hover) {
	.Tabs-module__JEJbCa__trigger:hover {
		color: var(--color-text-tertiary);
	}
}

.Tabs-module__JEJbCa__trigger[data-state="active"] {
	color: var(--color-text-primary);
}

.Tabs-module__JEJbCa__trigger[data-state="active"]::after {
	opacity: 1;
}

.Tabs-module__JEJbCa__trigger:focus-visible {
	border-radius: var(--radius-8);
	outline-offset: -2px;
}

.Tabs-module__JEJbCa__divider {
	background: var(--color-border-primary);
	width: 100%;
	height: 1px;
	margin-top: -1px;
}

.Tabs-module__JEJbCa__content {
	position: absolute;
	top: 0;
}

.Tabs-module__JEJbCa__content:first-child {
	position: relative;
}

.Tabs-module__JEJbCa__content[data-state="active"] {
	z-index: 1;
}

.Tabs-module__JEJbCa__content:focus-visible {
	padding: calc(var(--padding) / 2);
	margin: calc(var(--padding) / -2);
	border-radius: 6px;
}

.Tabs-module__JEJbCa__contentHeight {
	--padding: 24px;
	position: relative;
	overflow: hidden;
}

.Tabs-module__JEJbCa__contentOpacity {
	padding-top: 32px;
	padding-bottom: 8px;
}

.Input-module__cFnmoq__input {
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	border: 1px solid var(--color-border-translucent);
	background: var(--color-bg-translucent);
	width: 100%;
	height: 40px;
	caret-color: var(--color-brand-bg);
	border-radius: 8px;
	outline: none;
	padding: 0 10px;
	font-size: 14px;
	line-height: 21px;
}

.Input-module__cFnmoq__input::placeholder {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	color: var(--color-text-tertiary);
}

.Input-module__cFnmoq__input:-moz-placeholder-shown {
	text-transform: none !important;
}

.Input-module__cFnmoq__input:placeholder-shown {
	text-transform: none !important;
}

@media (max-width: 640px) {
	.Input-module__cFnmoq__input {
		font-size: 16px;
		line-height: 25px;
	}
}

.Author-module__6uArjW__trigger {
	cursor: help;
	height: -moz-fit-content;
	height: fit-content;
	display: inline-flex;
	position: relative;
}

.Author-module__6uArjW__trigger.Author-module__6uArjW__stacked {
	margin-left: calc(var(--spacing) * -1);
}

.Author-module__6uArjW__trigger.Author-module__6uArjW__stacked::after {
	content: "";
	border: 1px solid var(--color-bg-primary);
	border-radius: 50%;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Author-module__6uArjW__authors {
	--spacing: 8px;
}

.Author-module__6uArjW__content {
	background: var(--color-bg-tertiary);
	border: 1px solid var(--color-border-primary);
	box-shadow: var(--shadow-high);
	z-index: var(--layer-tooltip);
	transform-origin: var(--radix-tooltip-content-transform-origin);
	border-radius: 12px;
	padding: 10px 16px;
}

.Author-module__6uArjW__content[data-state="delayed-open"],
.Author-module__6uArjW__content[data-state="instant-open"] {
	animation: Author-module__6uArjW__open .16s var(--ease-out-quad) forwards;
}

.Author-module__6uArjW__content[data-state="closed"] {
	animation: Author-module__6uArjW__close .16s var(--ease-out-quad) forwards;
}

.Author-module__6uArjW__remaining {
	background-color: var(--color-bg-quaternary);
	width: 18px;
	height: 18px;
	color: var(--color-text-quaternary);
	margin-left: calc(var(--spacing) * -1);
	border-radius: 100%;
	place-items: center;
	font-size: 8px;
	display: grid;
	position: relative;
}

.Author-module__6uArjW__remaining::after {
	content: "";
	border: 1px solid var(--color-bg-primary);
	border-radius: 50%;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

@keyframes Author-module__6uArjW__open {
	0% {
		opacity: 0;
		transform: scale(.9);
	}

	to {
		opacity: 1;
		transform: scale(1);
	}
}

@keyframes Author-module__6uArjW__close {
	0% {
		opacity: 1;
		transform: scale(1);
	}

	to {
		opacity: 0;
		transform: scale(.9);
	}
}

.Select-module__0nG8mq__root {
	position: relative;
}

.Select-module__0nG8mq__select {
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	border: 1px solid var(--color-border-translucent);
	background-color: var(--color-bg-translucent);
	width: 100%;
	height: 40px;
	color: var(--color-text-primary);
	border-radius: 8px;
	padding: 0 10px;
	font-size: 14px;
	line-height: 21px;
}

@media (max-width: 640px) {
	.Select-module__0nG8mq__select {
		font-size: 16px;
		line-height: 24px;
	}
}

.Select-module__0nG8mq__icon {
	top: 0;
	bottom: 0;
	margin-top: auto;
	margin-bottom: auto;
	position: absolute;
	right: 10px;
}

.BlogRenderer-module__Xl7vPq__authorWrapper {
	margin-top: 40px;
	margin-bottom: 8px;
}

.Textarea-module__cOtYBa__textarea {
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	border: 1px solid var(--color-border-translucent);
	background: var(--color-bg-translucent);
	width: 100%;
	caret-color: var(--color-brand-bg);
	resize: vertical;
	border-radius: 8px;
	outline: none;
	padding: 10px 12px;
	scroll-padding-block: 8px;
	font-size: 14px;
	line-height: 21px;
}

.Textarea-module__cOtYBa__textarea::placeholder {
	color: var(--color-text-tertiary);
}

@media (max-width: 640px) {
	.Textarea-module__cOtYBa__textarea {
		font-size: 16px;
		line-height: 24px;
	}
}

.Sidenote-module__Jkohpq__root {
	isolation: isolate;
	margin-right: 8px;
	font-size: 13px;
	line-height: 19px;
	display: block;
	position: relative;
}

.Sidenote-module__Jkohpq__root ~ .Sidenote-module__Jkohpq__root {
	margin-top: 16px;
}

.Sidenote-module__Jkohpq__root[data-hover="true"]::before {
	opacity: 1;
	transform: none;
}

.Sidenote-module__Jkohpq__root::before {
	content: "";
	z-index: -1;
	background: var(--color-bg-tertiary);
	opacity: 0;
	border-radius: 6px;
	transition: opacity .18s, transform .18s;
	position: absolute;
	top: -6px;
	bottom: -6px;
	left: -8px;
	right: -8px;
	transform: scale(.9);
}

@media (max-width: 768px) {
	.Sidenote-module__Jkohpq__root {
		display: none;
	}
}

.Sidenote-module__Jkohpq__button {
	vertical-align: bottom;
	background: var(--color-bg-tertiary);
	border: none;
	width: 24px;
	height: 24px;
	margin-left: 4px;
	padding: 0;
}

.Sidenote-module__Jkohpq__button:not([disabled]):hover {
	background: var(--color-bg-quaternary);
}

.Sidenote-module__Jkohpq__button svg {
	fill: var(--color-text-primary);
	width: 18px;
	height: 18px;
}

.Sidenote-module__Jkohpq__mark {
	--y-offset: 4px;
	--x-offset: 3px;
	padding-top: var(--y-offset);
	padding-bottom: var(--y-offset);
	padding-right: var(--x-offset);
	padding-left: var(--x-offset);
	margin-left: calc(-1 * var(--x-offset));
	margin-right: calc(-1 * var(--x-offset));
	-webkit-text-decoration: underline dashed;
	text-decoration: underline dashed;
	text-decoration-thickness: 1.5px;
	-webkit-text-decoration-color: var(--color-border-tertiary);
	text-decoration-color: var(--color-border-tertiary);
	text-underline-offset: 2.5px;
	--c: transparent;
	background-image: linear-gradient(var(--c), var(--c));
	background-position: 0 calc(100% - 3px);
	background-repeat: no-repeat;
	background-size: 100% 1px;
	transition: background-size .16s, background-position .16s, text-underline-offset .16s, -webkit-text-decoration-color .16s, text-decoration-color .16s;
}

.Sidenote-module__Jkohpq__mark[data-hover="true"] {
	text-underline-offset: 6px;
	--c: var(--color-bg-quaternary);
	background-position: 0 100%;
	background-size: 100% 100%;
	border-radius: 4px;
	-webkit-text-decoration-color: transparent;
	text-decoration-color: transparent;
}

@media (max-width: 1024px) {
	.Sidenote-module__Jkohpq__mark {
		cursor: inherit;
		background: 0 0;
		text-decoration: none;
	}
}

.Sidenote-module__Jkohpq__inlineMark {
	cursor: pointer;
	-webkit-text-decoration-style: solid;
	text-decoration-style: solid;
}

.Sidenote-module__Jkohpq__inlineMark:hover {
	text-underline-offset: 2.5px;
	-webkit-text-decoration-color: var(--color-text-quaternary);
	text-decoration-color: var(--color-text-quaternary);
	background: 0 0;
}

.Sidenote-module__Jkohpq__collapsibleOuter {
	max-width: none;
	max-width: initial;
	background: var(--color-bg-secondary);
	border-top: 1px solid var(--color-border-primary);
	border-bottom: 1px solid var(--color-border-primary);
	height: max-content;
}

.Sidenote-module__Jkohpq__collapsible.Sidenote-module__Jkohpq__collapsible {
	width: 100vw;
	max-width: none;
	margin-bottom: 0;
	margin-left: -50vw;
	margin-right: -50vw;
	display: flex;
	position: relative;
	left: 50%;
	right: 50%;
}

.Sidenote-module__Jkohpq__collapsibleInner.Sidenote-module__Jkohpq__collapsibleInner {
	max-width: var(--prose-max-width);
	width: 100%;
	margin: 24px auto;
}

.Sidenote-module__Jkohpq__collapsibleInner.Sidenote-module__Jkohpq__collapsibleInner.Sidenote-module__Jkohpq__wide {
	max-width: var(--page-max-width);
}

.Sidenote-module__Jkohpq__inlineImage {
	vertical-align: text-top;
	margin-right: 4px;
	display: inline;
}

.Sidenote-module__Jkohpq__sidenoteContainer.Sidenote-module__Jkohpq__container.Sidenote-module__Jkohpq__sidenoteContainer.Sidenote-module__Jkohpq__container {
	max-width: none;
	max-width: initial;
	margin-left: 0;
	margin-right: 0;
}

@media (max-width: 1024px) {
	.Sidenote-module__Jkohpq__sidenoteContainer.Sidenote-module__Jkohpq__container.Sidenote-module__Jkohpq__sidenoteContainer.Sidenote-module__Jkohpq__container {
		max-width: var(--prose-max-width);
		margin-left: auto;
		margin-right: auto;
	}
}

.InlineIcon-module__PdnXIG__root {
	white-space: nowrap;
	display: inline;
}

.LayoutContent-module__ZDjT7G__root {
	padding-left: var(--page-padding-left);
	padding-right: var(--page-padding-right);
	max-width: var(--page-max-width);
	width: 100%;
	margin-left: auto;
	margin-right: auto;
}

.LayoutContent-module__ZDjT7G__page {
	margin: var(--page-padding-block) auto;
}

.LayoutContent-module__ZDjT7G__prose {
	max-width: var(--prose-max-width);
	padding: 0;
}

.LayoutContent-module__ZDjT7G__size-page {
	max-width: var(--page-max-width);
}

.LayoutContent-module__ZDjT7G__size-prose {
	max-width: var(--prose-max-width);
}

.LayoutContent-module__ZDjT7G__size-1 {
	max-width: 448px;
}

.LayoutContent-module__ZDjT7G__size-2 {
	max-width: 688px;
}

.LayoutContent-module__ZDjT7G__size-3 {
	max-width: 880px;
}

.LayoutContent-module__ZDjT7G__size-4 {
	max-width: 1136px;
}

.LayoutContent-module__ZDjT7G__size-full {
	max-width: calc(var(--page-max-width) + var(--page-padding-left) + var(--page-padding-right));
}

.Prose-module__heDPoa__prose {
	font-size: var(--p-size);
	line-height: var(--p-line-height);
	letter-spacing: var(--p-letter-spacing);
	color: var(--color-text-secondary);
}

.Prose-module__heDPoa__prose :-webkit-any(ul, ol) {
	padding-left: var(--list-inset);
	list-style: none;
}

.Prose-module__heDPoa__prose :-moz-any(ul, ol) {
	padding-left: var(--list-inset);
	list-style: none;
}

.Prose-module__heDPoa__prose :is(ul, ol) {
	padding-left: var(--list-inset);
	list-style: none;
}

.Prose-module__heDPoa__prose :-webkit-any(ul, ol) > li {
	margin: 0;
	position: relative;
}

.Prose-module__heDPoa__prose :-moz-any(ul, ol) > li {
	margin: 0;
	position: relative;
}

.Prose-module__heDPoa__prose :is(ul, ol) > li {
	margin: 0;
	position: relative;
}

:-webkit-any(.Prose-module__heDPoa__prose :-webkit-any(ul, ol) > li) + :-webkit-any(.Prose-module__heDPoa__prose :-webkit-any(ul, ol) > li) {
	margin-top: var(--block-spacing-small);
}

:-moz-any(.Prose-module__heDPoa__prose :-moz-any(ul, ol) > li) + :-moz-any(.Prose-module__heDPoa__prose :-moz-any(ul, ol) > li) {
	margin-top: var(--block-spacing-small);
}

:is(.Prose-module__heDPoa__prose :is(ul, ol) > li) + :is(.Prose-module__heDPoa__prose :is(ul, ol) > li) {
	margin-top: var(--block-spacing-small);
}

.Prose-module__heDPoa__prose :-webkit-any(ul, ol) > li > :-webkit-any(ul, ol) {
	margin-top: var(--block-spacing-small);
}

.Prose-module__heDPoa__prose :-moz-any(ul, ol) > li > :-moz-any(ul, ol) {
	margin-top: var(--block-spacing-small);
}

.Prose-module__heDPoa__prose :is(ul, ol) > li > :is(ul, ol) {
	margin-top: var(--block-spacing-small);
}

.Prose-module__heDPoa__prose ul {
	counter-reset: prose-ul 0;
}

.Prose-module__heDPoa__prose ul > li {
	counter-increment: prose-ul 1;
	position: relative;
}

.Prose-module__heDPoa__prose ul > li::before {
	content: counter(prose-ul, disc);
	text-align: center;
	min-width: var(--list-inset);
	right: calc(100% + .0625 * var(--list-inset));
	position: absolute;
}

.Prose-module__heDPoa__prose ul ul > li::before,
.Prose-module__heDPoa__prose ul ul ul ul > li::before {
	content: counter(prose-ul, circle);
}

.Prose-module__heDPoa__prose ul ul ul > li::before,
.Prose-module__heDPoa__prose ul ul ul ul ul > li::before {
	content: counter(prose-ul, disc);
}

.Prose-module__heDPoa__prose ol {
	counter-reset: prose-ol 0;
}

.Prose-module__heDPoa__prose ol[start] {
	counter-reset: prose-ol calc(var(--start, 1) - 1);
}

.Prose-module__heDPoa__prose ol > li {
	counter-increment: prose-ol 1;
	position: relative;
}

.Prose-module__heDPoa__prose ol > li::before {
	content: counter(prose-ol) ". ";
	text-align: end;
	font-feature-settings: "tnum";
	font-variant-numeric: tabular-nums;
	min-width: var(--list-inset);
	right: calc(100% + .25 * var(--list-inset));
	position: absolute;
}

.Prose-module__heDPoa__prose ol ol > li::before {
	content: counter(prose-ol, lower-alpha) ". ";
}

.Prose-module__heDPoa__prose ol ol ol > li::before {
	content: counter(prose-ol, lower-roman) ". ";
}

.Prose-module__heDPoa__prose > * + * {
	margin-top: var(--block-spacing);
}

.Prose-module__heDPoa__prose > figure {
	margin-block: var(--figure-margin);
}

.Prose-module__heDPoa__prose > figure[data-wide="true"]:has(video) {
	margin-inline: calc(var(--wide-inset) / 2 * -1);
	width: calc(100% + var(--wide-inset));
}

@media (max-width: 1280px) {
	.Prose-module__heDPoa__prose > figure[data-wide="true"]:has(video) {
		width: 100%;
		margin-left: 0;
		margin-right: 0;
	}
}

.Prose-module__heDPoa__prose > p + :-webkit-any(ul, ol) {
	margin-top: 12px;
}

.Prose-module__heDPoa__prose > p + :-moz-any(ul, ol) {
	margin-top: 12px;
}

.Prose-module__heDPoa__prose > p + :is(ul, ol) {
	margin-top: 12px;
}

.Prose-module__heDPoa__prose > p:empty {
	display: none;
}

.Prose-module__heDPoa__prose > * + h2 {
	margin-top: 56px;
}

.Prose-module__heDPoa__prose > * + h3 {
	margin-top: 32px;
}

.Prose-module__heDPoa__prose > * + h4 {
	margin-top: 28px;
}

.Prose-module__heDPoa__prose > h1 {
	font-size: var(--h1-size);
	line-height: var(--h1-line-height);
	letter-spacing: var(--h1-letter-spacing);
}

.Prose-module__heDPoa__prose > h2 {
	font-size: var(--h2-size);
	line-height: var(--h2-line-height);
	letter-spacing: var(--h2-letter-spacing);
	margin-top: 56px;
}

.Prose-module__heDPoa__prose > h2 + h3 {
	margin-top: 24px;
}

.Prose-module__heDPoa__prose > h2 + p {
	margin-top: var(--h2-bottom-margin);
}

.Prose-module__heDPoa__prose > h3 + p {
	margin-top: var(--h3-bottom-margin);
}

.Prose-module__heDPoa__prose > h4 + p {
	margin-top: var(--h4-bottom-margin);
}

.Prose-module__heDPoa__prose > h3 {
	font-size: var(--h3-size);
	line-height: var(--h3-line-height);
	letter-spacing: var(--h3-letter-spacing);
	margin-top: 56px;
}

.Prose-module__heDPoa__prose > h4 {
	font-size: var(--h4-size);
	line-height: var(--h4-line-height);
	letter-spacing: var(--h4-letter-spacing);
	margin-top: 56px;
}

.Prose-module__heDPoa__prose b,
.Prose-module__heDPoa__prose strong {
	color: var(--color-text-primary);
	font-weight: var(--font-weight-semibold);
}

.Prose-module__heDPoa__prose > figure:has(img, picture) {
	margin-top: 24px;
	margin-bottom: 24px;
}

@media (max-width: 768px) {
	.Prose-module__heDPoa__prose > figure:has(img, picture) {
		margin-top: 16px;
		margin-bottom: 16px;
	}
}

.Prose-module__heDPoa__prose > figure[data-wide="true"]:has(img, picture) {
	max-width: calc(var(--page-max-width) - var(--page-padding-left) - var(--page-padding-right));
	width: 100%;
}

.Prose-module__heDPoa__prose > figure:has(img, picture) > img {
	border-radius: 8px;
}

.Prose-module__heDPoa__prose > figure:has(img, picture) > figcaption {
	text-wrap: balance;
	max-width: var(--prose-max-width);
	margin-top: 13px;
	font-size: var(--text-micro-size);
	line-height: var(--text-micro-line-height);
	letter-spacing: var(--text-micro-letter-spacing);
	color: var(--color-text-tertiary);
	margin-left: auto;
	margin-right: auto;
}

@media (max-width: 640px) {
	.Prose-module__heDPoa__prose > figure:has(img, picture) > figcaption {
		text-wrap: pretty;
		text-align: left;
	}

	.Prose-module__heDPoa__prose > figure:has(img, picture) > figcaption [data-figure-flex] {
		justify-content: flex-start;
		align-items: flex-start;
	}

	.Prose-module__heDPoa__prose > figure:has(img, picture) > figcaption [data-figure-flex] [data-caption-prefix] {
		transform: translatey(-1px);
	}
}

.Prose-module__heDPoa__prose > blockquote {
	font-size: var(--title-3-size);
	line-height: var(--title-3-line-height);
	letter-spacing: var(--title-3-letter-spacing);
	color: var(--color-text-primary);
	font-weight: var(--font-weight-semibold);
	quotes: "“" "”" "‘" "’";
}

.Prose-module__heDPoa__prose > figure:has(blockquote) blockquote {
	font-size: var(--title-3-size);
	line-height: var(--title-3-line-height);
	letter-spacing: var(--title-3-letter-spacing);
	color: var(--color-text-primary);
	font-weight: var(--font-weight-semibold);
	quotes: "“" "”" "‘" "’";
}

:is(.Prose-module__heDPoa__prose > blockquote, .Prose-module__heDPoa__prose > figure:has(blockquote) blockquote) > p {
	text-indent: -.5em;
	margin: 0;
}

:is(.Prose-module__heDPoa__prose > blockquote, .Prose-module__heDPoa__prose > figure:has(blockquote) blockquote) > p::before {
	content: open-quote;
}

:is(.Prose-module__heDPoa__prose > blockquote, .Prose-module__heDPoa__prose > figure:has(blockquote) blockquote) > p::after {
	content: close-quote;
}

.Prose-module__heDPoa__prose > blockquote > footer {
	color: var(--color-text-tertiary);
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	font-weight: var(--font-weight-normal);
	margin-top: 12px;
}

.Prose-module__heDPoa__prose > figure:has(blockquote) > figcaption {
	color: var(--color-text-tertiary);
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	font-weight: var(--font-weight-normal);
	margin-top: 12px;
}

.Prose-module__heDPoa__prose * {
	word-break: break-word;
}

.Prose-module__heDPoa__center > :not([data-wide="true"]) {
	max-width: var(--prose-max-width);
	margin-left: auto;
	margin-right: auto;
}

.Prose-module__heDPoa__size-defaults {
	--list-inset: 24px;
	--block-spacing-small: 8px;
	--block-spacing: 20px;
	--h1-size: var(--title-5-size);
	--h1-line-height: var(--title-5-line-height);
	--h1-letter-spacing: var(--title-5-letter-spacing);
	--h2-size: var(--title-3-size);
	--h2-line-height: var(--title-3-line-height);
	--h2-letter-spacing: var(--title-3-letter-spacing);
	--h2-bottom-margin: 12px;
	--h3-size: 20px;
	--h3-line-height: 1.6;
	--h3-letter-spacing: 0;
	--h3-bottom-margin: 6px;
	--h4-size: var(--title-1-size);
	--h4-line-height: var(--title-1-line-height);
	--h4-letter-spacing: var(--title-1-letter-spacing);
	--h4-bottom-margin: 10px;
	--figure-margin: 20px;
}

@media (max-width: 768px) {
	.Prose-module__heDPoa__size-defaults {
		--h1-size: var(--title-4-size);
		--h1-line-height: var(--title-4-line-height);
		--h1-letter-spacing: var(--title-4-letter-spacing);
		--h2-size: var(--title-2-size);
		--h2-line-height: var(--title-2-line-height);
		--h2-letter-spacing: var(--title-2-letter-spacing);
		--h3-size: var(--title-1-size);
		--h3-line-height: var(--title-1-line-height);
		--h3-letter-spacing: var(--title-1-letter-spacing);
		--h4-size: var(--text-regular-size);
		--h4-line-height: var(--text-regular-line-height);
		--h4-letter-spacing: var(--text-regular-letter-spacing);
	}
}

.Prose-module__heDPoa__size-small {
	--block-spacing: 14px;
	--p-size: var(--text-small-size);
	--p-line-height: var(--text-small-line-height);
	--p-letter-spacing: var(--text-small-letter-spacing);
}

.Prose-module__heDPoa__size-regular {
	--block-spacing: 16px;
	--p-size: var(--text-regular-size);
	--p-line-height: var(--text-regular-line-height);
	--p-letter-spacing: var(--text-regular-letter-spacing);
}

.Prose-module__heDPoa__size-large {
	--p-size: var(--text-large-size);
	--p-line-height: var(--text-large-line-height);
	--p-letter-spacing: var(--text-large-letter-spacing);
	--h1-size: var(--title-5-size);
	--h1-line-height: var(--title-5-line-height);
	--h1-letter-spacing: var(--title-5-letter-spacing);
	--h2-size: var(--title-3-size);
	--h2-line-height: var(--title-3-line-height);
	--h2-letter-spacing: var(--title-3-letter-spacing);
	--h3-size: var(--title-3-size);
	--h3-line-height: var(--title-3-line-height);
	--h3-letter-spacing: var(--title-3-letter-spacing);
	--h3-bottom-margin: 16px;
	--h4-size: var(--title-1-size);
	--h4-line-height: var(--title-1-line-height);
	--h4-letter-spacing: var(--title-1-letter-spacing);
	--h4-bottom-margin: 18px;
	--wide-inset: calc((var(--page-max-width) - var(--page-padding-left) - var(--page-padding-right) - var(--prose-max-width)));
	--figure-margin: 32px;
}

@media (max-width: 768px) {
	.Prose-module__heDPoa__size-large {
		--p-size: var(--text-regular-size);
		--p-line-height: var(--text-regular-line-height);
		--p-letter-spacing: var(--text-regular-letter-spacing);
		--h2-size: var(--title-3-size);
		--h2-line-height: var(--title-3-line-height);
		--h2-letter-spacing: var(--title-3-letter-spacing);
		--h3-size: var(--title-2-size);
		--h3-line-height: var(--title-2-line-height);
		--h3-letter-spacing: var(--title-2-letter-spacing);
	}
}

.Link-module__TqD7sG__root {
	cursor: pointer;
	text-decoration: none;
}

.Link-module__TqD7sG__variant-none {
	color: currentColor;
}

@media (any-hover: hover) {
	.Link-module__TqD7sG__variant-none:hover {
		color: currentColor;
	}
}

.Link-module__TqD7sG__variant-underline {
	transition: var(--speed-regularTransition);
	color: var(--color-text-primary);
	text-underline-offset: clamp(2px, .225em, 6px);
	text-decoration: underline;
	text-decoration-thickness: max(1px, min(.1em, 3px));
	-webkit-text-decoration-color: var(--color-text-quaternary);
	text-decoration-color: var(--color-text-quaternary);
	transition-property: -webkit-text-decoration-color, text-decoration-color;
}

@media (any-hover: hover) {
	.Link-module__TqD7sG__variant-underline:hover {
		-webkit-text-decoration-color: var(--color-text-tertiary);
		text-decoration-color: var(--color-text-tertiary);
	}
}

.Link-module__TqD7sG__variant-dimmed {
	color: var(--color-text-tertiary);
	transition: color var(--speed-quickTransition);
	text-decoration: none;
}

.Link-module__TqD7sG__variant-dimmed[aria-current="page"] {
	color: var(--color-text-secondary);
	font-weight: var(--font-weight-medium);
}

@media (any-hover: hover) {
	.Link-module__TqD7sG__variant-dimmed:hover {
		color: var(--color-text-primary);
	}
}

.Link-module__TqD7sG__variant-primary {
	font-weight: var(--font-weight-medium);
	color: var(--color-link-primary);
	transition: color var(--speed-quickTransition);
}

@media (any-hover: hover) {
	.Link-module__TqD7sG__variant-primary:hover {
		color: var(--color-link-hover);
	}
}

.Link-module__TqD7sG__variant-fade {
	transition: color var(--speed-quickTransition);
}

@media (any-hover: hover) {
	.Link-module__TqD7sG__variant-fade:hover {
		color: var(--color-text-tertiary);
	}
}

.LinkAnchor-module__xzTXqW__inline {
	transition: opacity .2s, visibility 0s var(--visibility-delay, .2s);
	opacity: 0;
	visibility: hidden;
	margin-left: 8px;
	display: inline;
	position: relative;
}

.LinkAnchor-module__xzTXqW__root {
	display: inline-block;
}

.LinkAnchor-module__xzTXqW__positioner {
	width: 16px;
	height: 16px;
	display: inline-block;
}

.LinkAnchor-module__xzTXqW__icon {
	transition: transform .2s;
	position: absolute;
	top: 50%;
	transform: translatey(-50%) translate(-8px);
}

.LinkAnchor-module__xzTXqW__root:where(:hover, :focus) .LinkAnchor-module__xzTXqW__inline {
	opacity: 1;
	visibility: visible;
	--visibility-delay: 0s;
}

.LinkAnchor-module__xzTXqW__root:where(:hover, :focus) .LinkAnchor-module__xzTXqW__icon {
	transform: translatey(-50%);
}

@layer web.base {
	.Marquee-module__SWfNTW__root {
		--Marquee-gap: 24px;
		--Marquee-duration: 30s;
		--Marquee-shadow-size: 64px;
	}
}

.Marquee-module__SWfNTW__root {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	max-width: 100%;
	-webkit-mask-image: linear-gradient(to right, var(--mask-off) 0%, var(--mask-ease) calc(var(--Marquee-shadow-size) / 2), var(--mask-on) var(--Marquee-shadow-size), var(--mask-on) calc(100% - var(--Marquee-shadow-size)), var(--mask-ease) calc(100% - calc(var(--Marquee-shadow-size) / 2)), var(--mask-off) 100%);
	-webkit-mask-image: linear-gradient(to right, var(--mask-off) 0%, var(--mask-ease) calc(var(--Marquee-shadow-size) / 2), var(--mask-on) var(--Marquee-shadow-size), var(--mask-on) calc(100% - var(--Marquee-shadow-size)), var(--mask-ease) calc(100% - calc(var(--Marquee-shadow-size) / 2)), var(--mask-off) 100%);
	mask-image: linear-gradient(to right, var(--mask-off) 0%, var(--mask-ease) calc(var(--Marquee-shadow-size) / 2), var(--mask-on) var(--Marquee-shadow-size), var(--mask-on) calc(100% - var(--Marquee-shadow-size)), var(--mask-ease) calc(100% - calc(var(--Marquee-shadow-size) / 2)), var(--mask-off) 100%);
	display: flex;
	position: relative;
	overflow: hidden;
}

@media (any-hover: hover) {
	.Marquee-module__SWfNTW__root.Marquee-module__SWfNTW__pauseOnHover:hover .Marquee-module__SWfNTW__content {
		animation-play-state: paused;
	}
}

.Marquee-module__SWfNTW__content {
	align-items: center;
	gap: var(--Marquee-gap);
	flex-shrink: 0;
	flex-direction: var(--flex-direction);
	min-width: 100%;
	display: flex;
}

.Marquee-module__SWfNTW__content:nth-child(2) {
	visibility: hidden;
	position: absolute;
	top: 0;
	left: 0;
}

@media (prefers-reduced-motion: no-preference) {
	.Marquee-module__SWfNTW__content {
		animation: Marquee-module__SWfNTW__scroll var(--Marquee-duration) linear infinite;
	}

	.Marquee-module__SWfNTW__content.Marquee-module__SWfNTW__vertical {
		animation: Marquee-module__SWfNTW__scroll-vertical var(--Marquee-duration) linear infinite;
	}

	.Marquee-module__SWfNTW__content:nth-child(2) {
		visibility: visible;
		animation: Marquee-module__SWfNTW__scroll-abs var(--Marquee-duration) linear infinite;
	}

	.Marquee-module__SWfNTW__content.Marquee-module__SWfNTW__vertical:nth-child(2) {
		animation: Marquee-module__SWfNTW__scroll-abs-vertical var(--Marquee-duration) linear infinite;
	}
}

@media (prefers-reduced-motion: reduced) {
	.Marquee-module__SWfNTW__content[aria-hidden="true"] {
		display: none;
	}
}

@keyframes Marquee-module__SWfNTW__scroll {
	0% {
		transform: translate(0);
	}

	to {
		transform: translatex(calc(-100% - var(--Marquee-gap)));
	}
}

@keyframes Marquee-module__SWfNTW__scroll-vertical {
	0% {
		transform: translatey(0);
	}

	to {
		transform: translatey(calc(-100% - var(--Marquee-gap)));
	}
}

@keyframes Marquee-module__SWfNTW__scroll-abs {
	0% {
		transform: translatex(calc(100% + var(--Marquee-gap)));
	}

	to {
		transform: translate(0);
	}
}

@keyframes Marquee-module__SWfNTW__scroll-abs-vertical {
	0% {
		transform: translatey(calc(100% + var(--Marquee-gap)));
	}

	to {
		transform: translatey(0);
	}
}

.Breadcrumbs-module__n_rU7G__root {
	align-items: center;
	min-width: 0;
	margin: 0;
	padding: 0;
	list-style: none;
	display: flex;
}

.Breadcrumbs-module__n_rU7G__item {
	color: currentColor;
	white-space: nowrap;
	margin: 0;
	padding: 0;
}

.Breadcrumbs-module__n_rU7G__item.Breadcrumbs-module__n_rU7G__truncate {
	text-overflow: ellipsis;
	overflow: hidden;
}

.Breadcrumbs-module__n_rU7G__item:not(:last-child)::after {
	content: "/" / "";
	color: var(--color-text-quaternary);
	alt: " ";
	white-space: nowrap;
	flex-shrink: 0;
	margin-left: 8px;
	margin-right: 8px;
	display: inline-block;
}

.CustomerMarquee-module__SRrtxG__marquee {
	--Marquee-shadow-size: 80px;
}

@media (max-width: 1024px) {
	.CustomerMarquee-module__SRrtxG__marquee {
		--Marquee-shadow-size: 48px;
	}
}

@media (max-width: 768px) {
	.CustomerMarquee-module__SRrtxG__marquee {
		--Marquee-shadow-size: 24px;
	}
}

.CustomerMarquee-module__SRrtxG__logos {
	transition: .2s var(--ease-out-quad);
	max-width: 100%;
	padding-top: 24px;
	padding-bottom: 24px;
	transition-property: filter;
	overflow: hidden;
}

.CustomerMarquee-module__SRrtxG__customerLink {
	grid-template-columns: 1fr;
	place-items: center;
	display: grid;
	position: relative;
}

.CustomerMarquee-module__SRrtxG__customerLink > * {
	grid-area: 1 / 1;
}

@media (any-hover: hover) {
	.CustomerMarquee-module__SRrtxG__customerLink:hover .CustomerMarquee-module__SRrtxG__logos {
		filter: blur(8px);
	}

	.CustomerMarquee-module__SRrtxG__customerLink:hover .CustomerMarquee-module__SRrtxG__customerLinkLabel {
		opacity: 1;
		transform: none;
	}
}

.CustomerMarquee-module__SRrtxG__customerLink:focus-visible .CustomerMarquee-module__SRrtxG__logos {
	filter: blur(8px);
}

.CustomerMarquee-module__SRrtxG__customerLink:focus-visible .CustomerMarquee-module__SRrtxG__customerLinkLabel {
	opacity: 1;
	transform: none;
}

.CustomerMarquee-module__SRrtxG__customerLinkLabel {
	border-radius: var(--radius-rounded);
	background: var(--color-bg-tertiary);
	border: 1px solid var(--color-border-tertiary);
	height: 32px;
	box-shadow: var(--shadow-medium);
	opacity: 0;
	justify-content: center;
	align-items: center;
	gap: 4px;
	padding: 0 8px 0 16px;
	transition: opacity .25s, transform .25s;
	display: inline-flex;
	position: relative;
	transform: scale(.95);
}

.page-module__A5LhwG__content {
	width: 100%;
	max-width: var(--prose-max-width);
}

.page-module__A5LhwG__aside {
	width: 260px;
	min-width: 240px;
	max-width: 260px;
	top: calc(var(--header-height) + 48px);
	position: -webkit-sticky;
	position: sticky;
}

@media (max-width: 768px) {
	.page-module__A5LhwG__aside {
		top: auto;
		top: initial;
		width: 100%;
		max-width: var(--prose-max-width);
		flex-direction: column;
		gap: 16px;
		display: flex;
		position: static;
	}
}

.page-module__A5LhwG__layout {
	align-items: flex-start;
	gap: 80px;
	display: flex;
}

@media (max-width: 768px) {
	.page-module__A5LhwG__layout {
		flex-direction: column-reverse;
		gap: 24px;
	}
}

.page-module__A5LhwG__icon {
	border-radius: var(--radius-8);
	width: 48px;
	height: 48px;
}

.page-module__A5LhwG__specs {
	flex-direction: column;
	gap: 12px;
	margin-top: 16px;
	display: flex;
}

@media (max-width: 768px) {
	.page-module__A5LhwG__specs {
		margin-top: 0;
	}
}

.page-module__A5LhwG__renderer a {
	font-weight: var(--font-weight-normal);
	color: var(--color-text-tertiary);
	text-decoration: none;
}

.page-module__A5LhwG__renderer a:hover {
	color: var(--color-text-primary);
}

.page-module__A5LhwG__related {
	max-width: 1000px;
	margin: 0 auto;
}

.momentum-module__4J82la__wrapper {
	justify-content: space-between;
	align-items: center;
	width: 100%;
	height: 224px;
	display: none;
}

@media (any-hover: hover) {
	.momentum-module__4J82la__wrapper {
		display: flex;
	}

	.momentum-module__4J82la__illustration {
		display: none;
	}
}

.momentum-module__4J82la__bar {
	justify-content: center;
	display: flex;
}

.momentum-module__4J82la__barInner {
	background: var(--color-text-primary);
	width: 1px;
	height: 100%;
}

.DropdownMenu-module__AeEUsW__content {
	z-index: var(--layer-context-menu);
	background: var(--color-bg-level-1);
	min-width: 220px;
	box-shadow: var(--shadow-high);
	border: 1px solid var(--color-border-primary);
	animation: DropdownMenu-module__AeEUsW__enter .1s var(--ease-out-quad);
	transform-origin: var(--radix-popper-transform-origin);
	border-radius: 8px;
	padding: 4px;
	overflow: hidden;
}

[data-theme="light"] .DropdownMenu-module__AeEUsW__content {
	background: var(--color-bg-primary);
}

.DropdownMenu-module__AeEUsW__content[data-state="closed"] {
	animation: DropdownMenu-module__AeEUsW__exit .1s var(--ease-out-quad);
}

.DropdownMenu-module__AeEUsW__item {
	cursor: pointer;
	width: 100%;
	color: var(--color-text-secondary);
	box-shadow: none;
	border-radius: 4px;
	outline: none;
	align-items: center;
	gap: 8px;
	padding: 6px 10px;
	font-size: 13px;
	line-height: 32px;
	display: flex;
}

.DropdownMenu-module__AeEUsW__item .DropdownMenu-module__AeEUsW__icon svg {
	fill: var(--color-text-quaternary);
}

.DropdownMenu-module__AeEUsW__item[data-highlighted] {
	background: var(--color-bg-tertiary);
}

.DropdownMenu-module__AeEUsW__item[data-highlighted] .DropdownMenu-module__AeEUsW__icon svg {
	fill: var(--color-text-primary);
}

.DropdownMenu-module__AeEUsW__separator {
	background: var(--color-bg-tertiary);
	height: 1px;
	margin: 6px -4px;
}

.DropdownMenu-module__AeEUsW__icon {
	place-items: center;
	display: grid;
}

@keyframes DropdownMenu-module__AeEUsW__enter {
	0% {
		opacity: 0;
		transform: scale(.95);
	}

	to {
		opacity: 1;
		transform: scale(1);
	}
}

@keyframes DropdownMenu-module__AeEUsW__exit {
	0% {
		opacity: 1;
		transform: scale(1);
	}

	to {
		opacity: 0;
		transform: scale(.95);
	}
}

.Note-module__gQwJ5W__container {
	background: var(--color-bg-secondary);
	border: 1px solid var(--color-border-translucent);
	border-radius: 8px;
	padding: 12px 16px;
}

.Note-module__gQwJ5W__icon {
	flex-shrink: 0;
	margin-right: 16px;
}

.Note-module__gQwJ5W__icon svg {
	fill: var(--color-text-primary);
	width: 18px;
	height: 18px;
	margin-top: 1px;
}

.Note-module__gQwJ5W__icon img {
	margin-top: 4px;
}

.Note-module__gQwJ5W__content {
	color: var(--color-text-secondary);
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
}

.quoted-tweet-container-module__VxekxW__root {
	border: var(--tweet-border);
	width: 100%;
	margin: var(--tweet-quoted-container-margin);
	cursor: pointer;
	border-radius: 12px;
	transition-property: background-color, box-shadow;
	transition-duration: .2s;
	overflow: hidden;
}

.quoted-tweet-container-module__VxekxW__root:hover {
	background-color: var(--tweet-quoted-bg-color-hover);
}

.quoted-tweet-container-module__VxekxW__article {
	box-sizing: inherit;
	position: relative;
}

.quoted-tweet-header-module__Oefouq__header {
	line-height: var(--tweet-header-line-height);
	font-size: var(--tweet-header-font-size);
	white-space: nowrap;
	overflow-wrap: break-word;
	padding: .75rem .75rem 0;
	display: flex;
	overflow: hidden;
}

.quoted-tweet-header-module__Oefouq__avatar {
	width: 20px;
	height: 20px;
	position: relative;
}

.quoted-tweet-header-module__Oefouq__avatarSquare {
	border-radius: 4px;
}

.quoted-tweet-header-module__Oefouq__author {
	margin: 0 .5rem;
	display: flex;
}

.quoted-tweet-header-module__Oefouq__authorText {
	text-overflow: ellipsis;
	white-space: nowrap;
	font-weight: 700;
	overflow: hidden;
}

.quoted-tweet-header-module__Oefouq__username {
	color: var(--tweet-font-color-secondary);
	text-overflow: ellipsis;
	margin-left: .125rem;
	text-decoration: none;
}

.icons-module__fia-Bq__verified {
	fill: currentColor;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	vertical-align: text-bottom;
	max-width: 20px;
	height: 1.25em;
	max-height: 20px;
	margin-left: .125rem;
}

.verified-badge-module__bnANFa__verifiedOld {
	color: var(--tweet-verified-old-color);
}

.verified-badge-module__bnANFa__verifiedBlue {
	color: var(--tweet-verified-blue-color);
}

.verified-badge-module__bnANFa__verifiedGovernment {
	color: #829aab;
}

.quoted-tweet-body-module__L0Zxsa__root {
	font-size: var(--tweet-quoted-body-font-size);
	font-weight: var(--tweet-quoted-body-font-weight);
	line-height: var(--tweet-quoted-body-line-height);
	margin: var(--tweet-quoted-body-margin);
	overflow-wrap: break-word;
	white-space: pre-wrap;
	padding: 0 .75rem;
}

.tweet-media-module__zaO24W__root {
	margin-top: .75rem;
	position: relative;
	overflow: hidden;
}

.tweet-media-module__zaO24W__rounded {
	border: var(--tweet-border);
	border-radius: 12px;
}

.tweet-media-module__zaO24W__mediaWrapper {
	grid-gap: 2px;
	grid-auto-rows: 1fr;
	gap: 2px;
	width: 100%;
	height: 100%;
	display: grid;
}

.tweet-media-module__zaO24W__grid2Columns {
	grid-template-columns: repeat(2, 1fr);
}

.tweet-media-module__zaO24W__grid3 > a:first-child {
	grid-row: span 2;
}

.tweet-media-module__zaO24W__grid2x2 {
	grid-template-rows: repeat(2, 1fr);
}

.tweet-media-module__zaO24W__mediaContainer {
	justify-content: center;
	align-items: center;
	width: 100%;
	height: 100%;
	display: flex;
	position: relative;
}

.tweet-media-module__zaO24W__mediaLink {
	outline-style: none;
	text-decoration: none;
}

.tweet-media-module__zaO24W__skeleton {
	width: 100%;
	padding-bottom: 56.25%;
	display: block;
}

.tweet-media-module__zaO24W__image {
	-o-object-fit: cover;
	object-fit: cover;
	-o-object-position: center;
	object-position: center;
	width: 100%;
	height: 100%;
	margin: 0;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
}

.tweet-media-video-module__RDIT3a__anchor {
	color: #fff;
	cursor: pointer;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	text-overflow: ellipsis;
	white-space: nowrap;
	border: 1px solid transparent;
	border-radius: 9999px;
	outline-style: none;
	align-items: center;
	padding: 0 1rem;
	font-weight: 700;
	text-decoration: none;
	transition: background-color .2s;
	display: flex;
}

.tweet-media-video-module__RDIT3a__videoButton {
	background-color: var(--tweet-color-blue-primary);
	cursor: pointer;
	border: 4px solid #fff;
	border-radius: 9999px;
	justify-content: center;
	align-items: center;
	width: 67px;
	height: 67px;
	transition-property: background-color;
	transition-duration: .2s;
	display: flex;
	position: relative;
}

.tweet-media-video-module__RDIT3a__videoButton:hover {
	background-color: var(--tweet-color-blue-primary-hover);
}

.tweet-media-video-module__RDIT3a__videoButton:focus-visible {
	background-color: var(--tweet-color-blue-primary-hover);
}

.tweet-media-video-module__RDIT3a__videoButtonIcon {
	color: #fff;
	fill: currentColor;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	width: calc(50% + 4px);
	max-width: 100%;
	height: calc(50% + 4px);
	margin-left: 3px;
}

.tweet-media-video-module__RDIT3a__watchOnTwitter {
	position: absolute;
	top: 12px;
	right: 8px;
}

.tweet-media-video-module__RDIT3a__watchOnTwitter > a {
	-webkit-backdrop-filter: blur(4px);
	backdrop-filter: blur(4px);
	background-color: rgba(15, 20, 25, .75);
	min-width: 2rem;
	min-height: 2rem;
	font-size: .875rem;
	line-height: 1rem;
}

.tweet-media-video-module__RDIT3a__watchOnTwitter > a:hover {
	background-color: rgba(39, 44, 48, .75);
}

.tweet-media-video-module__RDIT3a__viewReplies {
	background-color: var(--tweet-color-blue-primary);
	border-color: var(--tweet-color-blue-primary);
	min-height: 2rem;
	font-size: .9375rem;
	line-height: 1.25rem;
	position: relative;
}

.tweet-media-video-module__RDIT3a__viewReplies:hover {
	background-color: var(--tweet-color-blue-primary-hover);
}

.tweet-link-module__XWT0DG__root {
	font-weight: inherit;
	color: var(--tweet-color-blue-secondary);
	cursor: pointer;
	text-decoration: none;
}

.tweet-link-module__XWT0DG__root:hover {
	-webkit-text-decoration-line: underline;
	text-decoration-line: underline;
	text-decoration-thickness: 1px;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__heroContainer {
		overflow: hidden;
	}
}

.page-module__HPIeYG__cmdkContainer {
	perspective: 900px;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	width: 100%;
	max-width: 720px;
	position: relative;
}

@media (max-width: 1024px) {
	.page-module__HPIeYG__cmdkContainer {
		transform: scale(.85);
	}
}

.page-module__HPIeYG__cmdk {
	transform-origin: top;
	will-change: transform;
	border: 1px solid var(--color-border-tertiary);
	background: linear-gradient(rgba(255, 255, 255, .1) 40%, rgba(8, 9, 10, .1) 100%);
	border-radius: 8px;
	width: 100%;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	box-shadow: inset 0 1.503px 5.261px rgba(255, 255, 255, .04), inset 0 -.752px .752px rgba(255, 255, 255, .1);
}

.page-module__HPIeYG__cmdk::after {
	content: "";
	background: linear-gradient(90deg, transparent 0%, var(--color-text-primary) 50%, transparent 100%);
	opacity: .5;
	height: 1px;
	position: absolute;
	top: -1px;
	left: 0;
	right: 0;
}

.page-module__HPIeYG__cmdk::before {
	content: "";
	background: linear-gradient(180deg, transparent 0%, var(--color-bg-primary) 100%);
	z-index: 1;
	height: 80%;
	position: absolute;
	bottom: -2px;
	left: -180px;
	right: -180px;
}

.page-module__HPIeYG__cmdkItems {
	margin-top: 48px;
}

.page-module__HPIeYG__cmdkItems::after {
	content: "";
	background: linear-gradient(180deg, transparent 0%, var(--color-bg-primary) 100%);
	height: 80%;
	position: absolute;
	bottom: -2px;
	left: -180px;
	right: -180px;
}

.page-module__HPIeYG__cmdkInput {
	border: none;
	border-bottom: 1px solid var(--color-border-primary);
	pointer-events: none;
	background: 0 0;
	outline: none;
	gap: 12px;
	width: 100%;
	height: 54px;
	padding: 0 20px;
	font-size: 17px;
	position: relative;
}

.page-module__HPIeYG__cmdkInput::placeholder {
	color: var(--color-text-tertiary);
}

.page-module__HPIeYG__inputWrapper::after {
	content: "";
	background: var(--color-indigo);
	border-radius: 9999px;
	width: 1.5px;
	height: 22px;
	animation: 1.25s step-end infinite page-module__HPIeYG__blink;
	display: inline-block;
	position: absolute;
	top: 14px;
	left: 16px;
	transform: translatey(1px);
}

.page-module__HPIeYG__cmdkItem {
	align-items: center;
	gap: 12px;
	height: 42px;
	padding-left: 24px;
	padding-right: 24px;
	display: flex;
	position: relative;
}

.page-module__HPIeYG__cmdkItem.page-module__HPIeYG__cmdkItemSelected {
	background: linear-gradient(#343434 0%, #2d2d2d 100%);
	border-radius: 6px;
	height: 48px;
	position: relative;
	box-shadow: inset 0 -2.75px 4.75px rgba(255, 255, 255, .14), inset 0 -.752px .752px rgba(255, 255, 255, .1), 0 54px 73px 3px rgba(0, 0, 0, .5);
}

.page-module__HPIeYG__cmdkItem.page-module__HPIeYG__cmdkItemSelected::after {
	content: "";
	border: 1px solid rgba(255, 255, 255, .1);
	border-radius: 6px;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__HPIeYG__glassEffect {
	opacity: .08;
	filter: blur(1px);
	align-items: center;
	gap: 12px;
	display: flex;
	position: absolute;
	top: 21px;
	left: 24px;
	right: 24px;
	transform: rotatex(20deg);
}

.page-module__HPIeYG__cmdkBadge {
	background-color: var(--color-bg-secondary);
	font-size: 10px;
	font-weight: var(--font-weight-medium);
	color: var(--color-text-tertiary);
	border-radius: 4px;
	padding: 2px 4px;
	position: relative;
}

.page-module__HPIeYG__bentoA {
	position: relative;
}

.page-module__HPIeYG__bentoA::after {
	--border-width: 1px;
	content: "";
	height: 100%;
	width: var(--border-width);
	background: var(--color-border-translucent);
	transform: translatex(calc(var(--grid-gap) / 2 + var(--border-width) / 2));
	position: absolute;
	top: 0;
	bottom: 0;
	right: 0;
}

@media (max-width: 768px) {
	.page-module__HPIeYG__bentoA::after {
		content: none;
	}
}

.page-module__HPIeYG__bentoB {
	padding-bottom: 48px;
	padding-left: 8px;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__bentoB {
		padding-bottom: 24px;
		padding-left: 0;
		overflow: hidden;
	}
}

.page-module__HPIeYG__lastBentoContent {
	padding-left: 8px;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__lastBentoContent {
		padding-left: 0;
	}
}

.page-module__HPIeYG__bentoContent {
	max-width: 410px;
}

.page-module__HPIeYG__maskRightBottom {
	-webkit-mask-image: linear-gradient(to bottom, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 100%), linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 95%);
	-webkit-mask-image: linear-gradient(to bottom, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 100%), linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 95%);
	mask-image: linear-gradient(to bottom, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 100%), linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 95%);
	-webkit-mask-composite: source-in, xor;
	-webkit-mask-composite: source-in;
	mask-composite: intersect;
}

.page-module__HPIeYG__maskRight {
	-webkit-mask-image: linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 95%);
	-webkit-mask-image: linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 95%);
	mask-image: linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 40%, var(--mask-invisible) 95%);
}

.page-module__HPIeYG__cursors {
	flex-wrap: wrap;
	width: 635px;
	height: 100%;
	max-height: 355px;
	display: flex;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-103%) translatey(-25%);
}

@media (max-width: 640px) {
	.page-module__HPIeYG__cursors {
		transform: translate(-95%) translatey(-26%) scale(.84);
	}
}

.page-module__HPIeYG__cursor {
	position: absolute;
}

.page-module__HPIeYG__illustration {
	width: 100%;
	max-width: 100%;
	height: 453px;
	margin: -112px auto 0;
	display: flex;
	position: relative;
}

@media (max-width: 1400px) {
	.page-module__HPIeYG__illustration {
		overflow: hidden;
	}
}

@media (max-width: 640px) {
	.page-module__HPIeYG__illustration {
		margin-top: -196px;
	}
}

.page-module__HPIeYG__illustration::before {
	content: "";
	flex-shrink: 0;
	width: 51vw;
	display: block;
}

.page-module__HPIeYG__illustration::after {
	content: "";
	background: linear-gradient(270deg, var(--color-bg-primary) 0%, transparent 100%);
	width: 50%;
	position: absolute;
	top: 0;
	bottom: 0;
	right: 0;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__illustration::after {
		width: 10%;
	}
}

.page-module__HPIeYG__hand {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	flex-shrink: 0;
	width: auto;
	height: 100%;
	position: relative;
	overflow: hidden;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__hand {
		height: auto;
	}
}

.page-module__HPIeYG__hand img {
	width: 905px;
	height: 100%;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__hand img {
		width: 320px;
		height: auto;
		transform: translatey(193px);
	}
}

.page-module__HPIeYG__hand::after {
	content: "";
	background: linear-gradient(270deg, var(--color-bg-primary) 0%, transparent 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__hand::after {
		content: none;
	}
}

.page-module__HPIeYG__textarea {
	background: var(--color-bg-secondary);
	border: 1px solid var(--color-border-translucent);
	border-radius: 6px;
	width: 380px;
	height: 82px;
	padding: 16px;
}

@media (max-width: 1024px) {
	.page-module__HPIeYG__textarea {
		width: 340px;
	}
}

@media (max-width: 640px) {
	.page-module__HPIeYG__textarea {
		width: 296px;
		-webkit-mask-image: linear-gradient(to left, var(--mask-visible) 0%, var(--mask-invisible) 95%);
		-webkit-mask-image: linear-gradient(to left, var(--mask-visible) 0%, var(--mask-invisible) 95%);
		mask-image: linear-gradient(to left, var(--mask-visible) 0%, var(--mask-invisible) 95%);
		margin-left: -32px;
	}
}

.page-module__HPIeYG__autocompleteUi {
	background: var(--color-bg-quaternary);
	border-radius: 4px;
	align-items: center;
	gap: 2px;
	height: 24px;
	padding: 0 4px;
	display: inline-flex;
}

.page-module__HPIeYG__autocompleteUi::after {
	content: "";
	background: var(--color-indigo);
	border-radius: 9999px;
	width: 1.5px;
	height: 14px;
	animation: 1.25s step-end infinite page-module__HPIeYG__blink;
	display: inline-block;
	transform: translatey(1px);
}

.page-module__HPIeYG__dropdown {
	background: var(--color-bg-secondary);
	border: 1px solid var(--color-border-translucent);
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	border-radius: 8px;
	width: 256px;
	padding: 4px;
	position: absolute;
	top: 52px;
	right: 8px;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__dropdown {
		width: 232px;
		left: 96px;
	}
}

.page-module__HPIeYG__dropdownItem {
	transition: transform .16s var(--ease-out-quad);
	cursor: default;
	will-change: transform;
	background: 0 0;
	border: none;
	border-radius: 8px;
	align-items: center;
	width: 100%;
	padding: 8px;
	display: flex;
}

.page-module__HPIeYG__dropdownItem[data-selected="true"] {
	background: var(--color-bg-quaternary);
	cursor: pointer;
}

.page-module__HPIeYG__dropdownItem[data-selected="true"]:active {
	transform: scale(.97);
}

.page-module__HPIeYG__badge {
	border: 1px solid var(--color-border-secondary);
	height: 17px;
	color: var(--color-text-tertiary);
	border-radius: 4px;
	align-items: center;
	margin-left: 10px;
	padding: 0 4px;
	font-size: 10px;
	display: inline-flex;
}

.page-module__HPIeYG__card {
	background: var(--color-bg-secondary);
	border: 1px solid var(--color-border-translucent);
	-webkit-mask-image: linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 25%, var(--mask-invisible) 100%);
	-webkit-mask-image: linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 25%, var(--mask-invisible) 100%);
	mask-image: linear-gradient(to right, var(--mask-visible) 0%, var(--mask-visible) 25%, var(--mask-invisible) 100%);
	border-radius: 6px;
	padding: 20px 24px;
}

.page-module__HPIeYG__separator {
	background: var(--color-border-primary);
	margin-left: 7px;
	border-radius: 9999px;
	width: 2px;
	height: 12px;
	margin-top: 1px;
	margin-bottom: 1px;
}

.page-module__HPIeYG__textareaContainer {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	position: relative;
}

@media (max-width: 640px) {
	.page-module__HPIeYG__textareaContainer {
		height: 164px;
	}
}

@keyframes page-module__HPIeYG__blink {
	0% {
		visibility: visible;
	}

	50% {
		visibility: hidden;
	}

	to {
		visibility: visible;
	}
}

@media (max-width: 640px) {
	.page-module__HPIeYG__mobileBorder {
		border-top: 1px solid var(--color-line-tertiary);
	}

	.page-module__HPIeYG__title {
		font-size: 38px;
	}
}

.tweet-body-module__537pYW__root {
	font-size: var(--tweet-body-font-size);
	font-weight: var(--tweet-body-font-weight);
	line-height: var(--tweet-body-line-height);
	margin: var(--tweet-body-margin);
	overflow-wrap: break-word;
	white-space: pre-wrap;
}

.page-module__QbE8ja__bentoA {
	position: relative;
}

.page-module__QbE8ja__bentoA::after {
	--border-width: 1px;
	content: "";
	height: 100%;
	width: var(--border-width);
	background: var(--color-border-translucent);
	transform: translatex(calc(var(--grid-gap) / 2 + var(--border-width) / 2));
	position: absolute;
	top: 0;
	bottom: 0;
	right: 0;
}

@media (max-width: 768px) {
	.page-module__QbE8ja__bentoA::after {
		content: none;
	}
}

.page-module__QbE8ja__bentoA,
.page-module__QbE8ja__bentoB {
	padding-top: 48px;
}

@media (max-width: 640px) {
	.page-module__QbE8ja__bentoA,
	.page-module__QbE8ja__bentoB {
		padding-top: 40px;
	}
}

.page-module__QbE8ja__bentoB {
	padding-bottom: 68px;
	padding-left: 24px;
}

@media (max-width: 768px) {
	.page-module__QbE8ja__bentoB {
		padding-bottom: 48px;
		padding-left: 0;
	}
}

@media (max-width: 640px) {
	.page-module__QbE8ja__bentoB {
		padding-bottom: 40px;
	}
}

.page-module__QbE8ja__productIntelligenceIllustration {
	background: var(--color-bg-level-2);
	border: 1px solid var(--color-border-translucent);
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	border-radius: 8px;
	padding: 19px 16px 20px;
}

.page-module__QbE8ja__PIGradient {
	background: linear-gradient(90deg, var(--color-text-primary) 0%, var(--color-text-tertiary) 100%);
	-webkit-text-fill-color: transparent;
	-webkit-background-clip: text;
	background-clip: text;
}

.page-module__QbE8ja__suggestionButton {
	border: dashed 1px var(--color-border-tertiary);
	white-space: nowrap;
	background: 0 0;
	border-radius: 4px;
	align-items: center;
	gap: 6px;
	height: 24px;
	transition: background .1s;
	display: flex;
}

.page-module__QbE8ja__suggestionButton:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 4px;
	padding-right: 6px;
}

.page-module__QbE8ja__suggestionButton:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 4px;
	padding-right: 6px;
}

.page-module__QbE8ja__suggestionButton:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 4px;
	padding-right: 6px;
}

.page-module__QbE8ja__suggestionButton:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 6px;
	padding-right: 4px;
}

.page-module__QbE8ja__suggestionButton:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 6px;
	padding-right: 4px;
}

.page-module__QbE8ja__suggestionButton:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 6px;
	padding-right: 4px;
}

@media (any-hover: hover) {
	.page-module__QbE8ja__suggestionButton:hover {
		background: var(--color-bg-tertiary);
	}
}

.page-module__QbE8ja__dropdown {
	border: 1px solid var(--color-border-translucent);
	-webkit-backdrop-filter: blur(4px);
	backdrop-filter: blur(4px);
	background: rgba(15, 16, 17, .8);
	border-radius: 6px;
	flex-direction: column;
	width: 320px;
	height: 250px;
	padding: 12px 7px 7px;
	display: flex;
	position: absolute;
	top: 83px;
	left: 103px;
	overflow: hidden;
}

@media (max-width: 640px) {
	.page-module__QbE8ja__dropdown {
		left: 17px;
	}
}

.page-module__QbE8ja__dropdown[data-dir="1"] .page-module__QbE8ja__dropdownPanel[data-active="true"] {
	animation-name: page-module__QbE8ja__dropdownInFromRight;
}

.page-module__QbE8ja__dropdown[data-dir="-1"] .page-module__QbE8ja__dropdownPanel[data-active="true"] {
	animation-name: page-module__QbE8ja__dropdownInFromLeft;
}

.page-module__QbE8ja__dropdownViewport {
	flex: 1;
	position: relative;
}

.page-module__QbE8ja__dropdownPanel {
	opacity: 0;
	pointer-events: none;
	flex-direction: column;
	animation-duration: .2s;
	animation-timing-function: ease;
	animation-fill-mode: forwards;
	display: flex;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__QbE8ja__dropdownPanel[data-active="true"] {
	animation-name: page-module__QbE8ja__dropdownInFromRight;
}

.page-module__QbE8ja__dropdownPanel[data-exit="true"][data-exit-dir="-1"] {
	animation-name: page-module__QbE8ja__dropdownOutToLeft;
}

.page-module__QbE8ja__dropdownPanel[data-exit="true"][data-exit-dir="1"] {
	animation-name: page-module__QbE8ja__dropdownOutToRight;
}

.page-module__QbE8ja__dropdownPanel[data-initial="true"][data-active="true"] {
	opacity: 1;
	animation: none;
}

@keyframes page-module__QbE8ja__dropdownInFromRight {
	0% {
		opacity: 0;
		transform: translate(10%);
	}

	to {
		opacity: 1;
		transform: translate(0%);
	}
}

@keyframes page-module__QbE8ja__dropdownInFromLeft {
	0% {
		opacity: 0;
		transform: translate(-10%);
	}

	to {
		opacity: 1;
		transform: translate(0%);
	}
}

@keyframes page-module__QbE8ja__dropdownOutToRight {
	0% {
		opacity: 1;
		transform: translate(0%);
	}

	to {
		opacity: 0;
		transform: translate(10%);
	}
}

@keyframes page-module__QbE8ja__dropdownOutToLeft {
	0% {
		opacity: 1;
		transform: translate(0%);
	}

	to {
		opacity: 0;
		transform: translate(-10%);
	}
}

.page-module__QbE8ja__fadeRight {
	-webkit-mask-image: linear-gradient(270deg, transparent 0%, #000 100%);
	mask-image: linear-gradient(270deg, transparent 0%, #000 100%);
}

.page-module__QbE8ja__dropdownInner {
	padding-left: 8px;
	padding-right: 8px;
}

.page-module__QbE8ja__agentIllustration {
	width: 100%;
	max-width: 432px;
	margin-left: auto;
	position: relative;
}

@media (max-width: 768px) {
	.page-module__QbE8ja__agentIllustration {
		margin-left: 0;
	}
}

.page-module__QbE8ja__agentIllustration::before {
	content: "";
	background: linear-gradient(to right, transparent 0%, var(--color-bg-primary) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__QbE8ja__duplicatesIllustration {
	width: -moz-fit-content;
	width: fit-content;
	position: relative;
}

.page-module__QbE8ja__duplicatesIllustration::before {
	content: "";
	background: linear-gradient(to right, transparent 40%, var(--color-bg-primary) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__QbE8ja__aiPoweredSearchIllustration,
.page-module__QbE8ja__linearMCPIllustration,
.page-module__QbE8ja__pulseIllustration {
	position: relative;
}

.page-module__QbE8ja__aiPoweredSearchIllustration::before,
.page-module__QbE8ja__linearMCPIllustration::before,
.page-module__QbE8ja__pulseIllustration::before {
	content: "";
	background: linear-gradient(to right, transparent 40%, var(--color-bg-primary) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

@media (max-width: 640px) {
	.page-module__QbE8ja__aiPoweredSearchIllustration {
		height: 156px;
	}
}

.page-module__QbE8ja__pulseIllustration {
	align-items: center;
	height: 280px;
	display: flex;
}

@media (max-width: 640px) {
	.page-module__QbE8ja__pulseIllustration {
		height: 172px;
	}
}

.page-module__QbE8ja__pulseIllustration::before {
	background: linear-gradient(to right, transparent 20%, var(--color-bg-primary) 80%);
}

.page-module__QbE8ja__securityIllustration,
.page-module__QbE8ja__agentsIllustration {
	align-items: center;
	width: -moz-fit-content;
	width: fit-content;
	height: 280px;
	display: flex;
	position: relative;
}

.page-module__QbE8ja__securityIllustration::after,
.page-module__QbE8ja__agentsIllustration::after {
	content: "";
	background: radial-gradient(50% 50% at 50% 50%, transparent 0%, var(--color-bg-primary) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__QbE8ja__securityIllustration .page-module__QbE8ja__logoWrapper,
.page-module__QbE8ja__agentsIllustration .page-module__QbE8ja__logoWrapper {
	border-radius: 50%;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

.page-module__QbE8ja__securityIllustration {
	width: 100%;
}

.page-module__QbE8ja__blinkingCursor {
	background: var(--color-indigo);
	border-radius: 2px;
	width: 2px;
	height: 28px;
	animation: 1s step-end infinite page-module__QbE8ja__blink;
	position: absolute;
	top: 5%;
	left: 5%;
}

@media (max-width: 640px) {
	.page-module__QbE8ja__blinkingCursor {
		width: 1px;
		height: 18px;
		top: 6%;
		left: 5.5%;
	}
}

.page-module__QbE8ja__dropdownBadge {
	background: #212324;
	border-radius: 4px;
	height: 20px;
	padding-left: 4px;
	padding-right: 4px;
}

@keyframes page-module__QbE8ja__blink {
	50% {
		visibility: hidden;
	}
}

.page-module__QbE8ja__agentsBento {
	flex-direction: column;
	display: flex;
}

@media (max-width: 640px) {
	.page-module__QbE8ja__agentsBento > div:first-of-type {
		order: 2;
	}

	.page-module__QbE8ja__agentsBento.page-module__QbE8ja__ownAgents {
		padding-bottom: 8px;
	}

	.page-module__QbE8ja__mobileDivider {
		border-top: 1px solid var(--color-line-tertiary);
	}
}

.tweet-container-module__BSo9KW__root {
	width: 100%;
	min-width: 250px;
	max-width: 550px;
	color: var(--tweet-font-color);
	font-family: var(--tweet-font-family);
	box-sizing: border-box;
	border: var(--tweet-border);
	margin: var(--tweet-container-margin);
	background-color: var(--tweet-bg-color);
	border-radius: 12px;
	font-weight: 400;
	transition-property: background-color, box-shadow;
	transition-duration: .2s;
	overflow: hidden;
}

.tweet-container-module__BSo9KW__root:hover {
	background-color: var(--tweet-bg-color-hover);
}

.tweet-container-module__BSo9KW__article {
	box-sizing: inherit;
	padding: .75rem 1rem;
	position: relative;
}

.DifferentCard-module__ZPfTEW__differentCard {
	text-align: left;
	isolation: isolate;
	aspect-ratio: 336 / 360;
	background: var(--color-bg-level-2);
	border-radius: 30px;
	flex-direction: column;
	justify-content: flex-end;
	height: 360px;
	transition: background .2s ease-out;
	display: flex;
	position: relative;
	overflow: hidden;
}

@media (any-hover: hover) {
	.DifferentCard-module__ZPfTEW__differentCard:hover {
		background: var(--color-bg-level-3);
	}

	.DifferentCard-module__ZPfTEW__differentCard:hover .DifferentCard-module__ZPfTEW__iconButton {
		color: var(--color-text-primary);
		border-color: var(--color-bg-tertiary);
		background: var(--color-bg-tertiary);
	}
}

.DifferentCard-module__ZPfTEW__iconButton {
	border-radius: var(--radius-rounded);
	flex-shrink: 0;
	justify-content: center;
	align-items: center;
	width: 40px;
	height: 40px;
	display: flex;
}

.DifferentCard-module__ZPfTEW__image {
	width: 100%;
	display: flex;
	position: absolute;
	top: 0;
	-webkit-mask-image: linear-gradient(#000 70%, transparent 90%);
	mask-image: linear-gradient(#000 70%, transparent 90%);
}

.DifferentCard-module__ZPfTEW__openImage {
	display: flex;
	-webkit-mask-image: linear-gradient(#000 50%, transparent 80%);
	mask-image: linear-gradient(#000 50%, transparent 80%);
}

.DifferentCard-module__ZPfTEW__title {
	padding: 0 24px 32px;
}

.DifferentCard-module__ZPfTEW__drawer {
	background: var(--color-bg-level-1);
	max-width: 960px;
	z-index: var(--layer-dialog);
	contain: strict;
	isolation: isolate;
	border-radius: 30px 30px 0 0;
	outline: none;
	margin-left: auto;
	margin-right: auto;
	position: fixed;
	top: 5vh;
	bottom: 0;
	left: 0;
	right: 0;
}

.DifferentCard-module__ZPfTEW__scrollable {
	padding-left: var(--page-padding-left);
	padding-right: var(--page-padding-right);
}

.DifferentCard-module__ZPfTEW__close.DifferentCard-module__ZPfTEW__close {
	z-index: 1;
	margin-left: auto;
	display: flex;
	position: fixed;
	top: 24px;
	right: 24px;
}

.DifferentCard-module__ZPfTEW__overlay {
	background: var(--color-overlay-primary);
	-webkit-backdrop-filter: blur(24px);
	backdrop-filter: blur(24px);
	z-index: var(--layer-dialog-overlay);
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

@keyframes DifferentCard-module__ZPfTEW__dialogIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes DifferentCard-module__ZPfTEW__dialogOut {
	0% {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}

.DifferentCard-module__ZPfTEW__bottomSpacer {
	min-height: 64px;
}

.Editor-module__8mxfpG__editorContainer {
	width: -moz-fit-content;
	width: fit-content;
	margin-left: auto;
	padding-left: 24px;
	padding-right: 24px;
	position: relative;
	overflow: hidden;
}

@media (max-width: 768px) {
	.Editor-module__8mxfpG__editorContainer {
		margin-left: auto;
		margin-right: auto;
		padding: 0;
	}
}

.Editor-module__8mxfpG__editorContainer::after {
	content: "";
	pointer-events: none;
	background: linear-gradient(to bottom, transparent 80%, var(--color-bg-primary) 97%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Editor-module__8mxfpG__editorContent {
	left: 0;
	right: 0;
	max-width: 360px;
	margin-left: auto;
	margin-right: auto;
	position: absolute;
	top: 100px;
}

@media (max-width: 640px) {
	.Editor-module__8mxfpG__editorContent {
		max-width: 70vw;
		margin-left: 64px;
	}
}

.Editor-module__8mxfpG__remoteSelection {
	pointer-events: none;
	background: var(--selection-bg);
	border: 1px solid var(--selection-border);
	border-radius: 4px 1px 1px 4px;
	margin-left: -2px;
	margin-right: -2px;
	padding-left: 2px;
	padding-right: 2px;
	position: relative;
}

.Editor-module__8mxfpG__remoteCursor {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	pointer-events: none;
	word-break: normal;
	position: relative;
}

.Editor-module__8mxfpG__remoteCursor::before {
	content: "";
	background: var(--cursor-color);
	border-radius: var(--radius-rounded);
	width: 2px;
	position: absolute;
	top: -1px;
	bottom: -1px;
	left: 0;
	right: auto;
}

.Editor-module__8mxfpG__remoteLabel {
	display: block;
	position: absolute;
	top: -14px;
	left: 0;
}

.Editor-module__8mxfpG__remoteName {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	color: #fff;
	white-space: nowrap;
	text-align: center;
	background-color: var(--cursor-color);
	border-radius: 2px 2px 2px 0;
	height: 14px;
	padding: 0 4px;
	font-size: 10px;
	line-height: 14px;
	display: block;
}

.Editor-module__8mxfpG__remoteName::before {
	content: "";
	width: 2px;
	height: 4px;
	box-shadow: 0 -2px 0 0 var(--cursor-color);
	background-color: transparent;
	border-top-left-radius: 2px;
	position: absolute;
	bottom: -4px;
	left: 2px;
}

.Editor-module__8mxfpG__commentMark {
	color: #fff;
	background: #897844;
	border-bottom: 1px solid #c2a955;
	margin-left: -2px;
	margin-right: -2px;
	padding-left: 2px;
	padding-right: 2px;
	position: relative;
	overflow: visible;
}

.Editor-module__8mxfpG__comment {
	color: var(--color-text-primary);
	background: var(--color-bg-tertiary);
	border: 1px solid var(--color-border-secondary);
	min-width: 227px;
	box-shadow: var(--shadow-medium);
	border-radius: 6px;
	position: absolute;
	top: calc(100% + 4px);
	right: 0;
}

.Editor-module__8mxfpG__list > li {
	color: var(--color-text-tertiary);
	height: 24px;
	margin: 0 0 2px 16px;
}

.Editor-module__8mxfpG__issueList {
	flex-direction: column;
	align-items: flex-start;
	gap: 2px;
	min-width: 0;
	display: flex;
}

.Editor-module__8mxfpG__issueList > li {
	background: var(--color-bg-quaternary);
	max-width: 100%;
	color: var(--color-text-tertiary);
	font-weight: var(--font-weight-medium);
	border-radius: 6px;
	align-items: center;
	gap: 6px;
	height: 24px;
	margin: 0;
	padding: 0 6px;
	display: inline-flex;
}

.Editor-module__8mxfpG__listAnimation {
	grid-template-columns: 1fr;
	display: grid;
}

.Editor-module__8mxfpG__listAnimation > * {
	grid-area: 1 / 1;
}

.Editor-module__8mxfpG__listAnimation .Editor-module__8mxfpG__list > li {
	animation: Editor-module__8mxfpG__blurOut .48s var(--ease-in-quad) both;
	animation-delay: calc(.5s + var(--index) * .1s);
}

.Editor-module__8mxfpG__listAnimation .Editor-module__8mxfpG__issueList > li {
	animation: Editor-module__8mxfpG__blurIn .48s var(--ease-in-quad) both;
	animation-delay: calc(.7s + var(--index) * .1s);
}

@keyframes Editor-module__8mxfpG__blurOut {
	0% {
		opacity: 1;
		filter: none;
	}

	to {
		opacity: 0;
		filter: blur(4px);
	}
}

@keyframes Editor-module__8mxfpG__blurIn {
	0% {
		opacity: 0;
		filter: blur(4px);
	}

	to {
		opacity: 1;
		filter: none;
	}
}

.Editor-module__8mxfpG__toggleRoot {
	flex-direction: column;
	gap: 8px;
	display: flex;
}

.Editor-module__8mxfpG__button {
	letter-spacing: -.22px;
	font-size: 17px;
	line-height: 25px;
	font-weight: var(--font-weight-medium);
	color: var(--color-text-quaternary);
	transition: .24s var(--ease-out-quad);
	justify-content: flex-start;
	gap: 12px;
	transition-property: color;
	display: flex;
}

@media (any-hover: hover) {
	.Editor-module__8mxfpG__button:hover {
		color: var(--color-text-tertiary);
	}

	.Editor-module__8mxfpG__button:hover .Editor-module__8mxfpG__bar {
		background: var(--color-bg-quaternary);
	}
}

.Editor-module__8mxfpG__button[data-state="on"] {
	color: var(--color-text-primary);
}

.Editor-module__8mxfpG__button[data-state="on"] .Editor-module__8mxfpG__bar {
	background: #68cc58;
}

.Editor-module__8mxfpG__bar {
	border-radius: var(--radius-rounded);
	background: var(--color-bg-tertiary);
	width: 4px;
	height: 24px;
	transition: .24s var(--ease-out-quad);
	transition-property: background;
}

.Editor-module__8mxfpG__iconContainer {
	background: var(--icon-bg);
	width: 36px;
	height: 36px;
	color: var(--icon-text);
	border-radius: 8px;
	justify-content: center;
	align-items: center;
	display: flex;
}

.Separator-module__ef6YrG__root {
	background: var(--color-line-tertiary);
	border-radius: var(--radius-rounded);
	flex-shrink: 0;
}

.Separator-module__ef6YrG__root[data-orientation="horizontal"] {
	--direction: to right;
	width: 100%;
	height: 1px;
}

.Separator-module__ef6YrG__root[data-orientation="vertical"] {
	--direction: to bottom;
	align-self: stretch;
	width: 1px;
}

.Separator-module__ef6YrG__variant-glass {
	background: rgba(180, 188, 208, .1);
}

.Separator-module__ef6YrG__variant-skeuo {
	background: var(--color-bg-primary);
	box-shadow: 0 1px 0 var(--color-border-secondary);
}

.Separator-module__ef6YrG__variant-fading {
	--color: rgba(var(--color-alpha), var(--color-alpha), var(--color-alpha), .1);
	background: linear-gradient(var(--direction), transparent, var(--color) 50%, transparent);
}

.Separator-module__ef6YrG__variant-border {
	background: var(--color-border-primary);
}

.SkipNav-module__GR_XUG__root {
	top: var(--header-height);
	background: var(--color-brand-bg);
	color: var(--color-brand-text);
	font-size: 14px;
	font-weight: var(--font-weight-medium);
	z-index: var(--layer-skip-nav);
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	opacity: 0;
	justify-content: center;
	align-items: center;
	width: auto;
	height: 32px;
	padding: 0 16px;
	display: flex;
	position: fixed;
	left: 0;
	right: 0;
}

.SkipNav-module__GR_XUG__root:focus {
	box-shadow: 0 0 0 2px var(--color-bg-primary), 0 0 0 4px var(--color-brand-bg);
	pointer-events: all;
	opacity: 1;
	transform: none;
}

.vector-field-module__95koFa__root {
	cursor: pointer;
	width: 100%;
	height: 240px;
	transform: translate(-15px);
}

@media (max-width: 640px) {
	.vector-field-module__95koFa__root {
		transform: translate(-24px);
	}
}

.vector-field-module__95koFa__cursor {
	background: var(--color-text-primary);
	width: 9px;
	height: 9px;
	top: var(--mouse-y);
	left: var(--mouse-x);
	opacity: var(--opacity);
	pointer-events: none;
	border-radius: 50%;
	transition: opacity .3s;
	position: absolute;
	transform: translate(-50%, -50%);
}

.Layout-module__8SDqbq__container {
	flex-direction: column;
	width: 100%;
	display: flex;
}

.Layout-module__8SDqbq__content {
	min-height: calc(100 * var(--dvh));
	flex-direction: column;
	flex: 1;
	display: flex;
}

.Layout-module__8SDqbq__container:not(.Layout-module__8SDqbq__variant-full) [data-header] ~ .Layout-module__8SDqbq__content {
	padding-top: var(--header-height);
}

.Navigation-module__UJDdSq__back {
	font-size: 14px;
	line-height: 19px;
	font-weight: var(--font-weight-normal);
	color: var(--color-text-tertiary);
	align-items: center;
	gap: 4px;
	transition: color .12s;
	display: flex;
}

.Navigation-module__UJDdSq__back svg {
	width: 15px;
	height: 15px;
}

.Navigation-module__UJDdSq__back:hover {
	color: var(--color-text-primary);
}

.Navigation-module__UJDdSq__next,
.Navigation-module__UJDdSq__prev {
	width: 100%;
	min-width: 0;
	transition: var(--speed-regularTransition);
	flex-grow: 1;
	transition-property: background, transform;
	display: block;
}

.Navigation-module__UJDdSq__variant-default {
	border: 1px solid var(--color-border-primary);
	border-radius: 8px;
	padding: 16px;
}

@media (any-hover: hover) {
	.Navigation-module__UJDdSq__variant-default:hover {
		background: var(--color-bg-secondary);
	}
}

.Navigation-module__UJDdSq__variant-default:active {
	transform: scale(.98);
}
/*# sourceMappingURL=9c448383926f7c6e.css.map*/
.Circle-module__aFAW6G__perspective {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	cursor: default;
	perspective: 10000px;
	width: 100%;
	height: 500px;
	position: relative;
	overflow: hidden;
	-webkit-mask-image: linear-gradient(90deg, transparent, #000 20%, #000 80%, transparent 100%);
	mask-image: linear-gradient(90deg, transparent, #000 20%, #000 80%, transparent 100%);
}

@media (max-width: 640px) {
	.Circle-module__aFAW6G__perspective {
		height: 400px;
	}
}

@media (min-width: 1536px) {
	.Circle-module__aFAW6G__perspective {
		-webkit-mask-image: linear-gradient(90deg, transparent 10%, #000 30%, #000 70%, transparent 90%);
		mask-image: linear-gradient(90deg, transparent 10%, #000 30%, #000 70%, transparent 90%);
	}
}

@media (any-hover: hover) {
	.Circle-module__aFAW6G__perspective {
		touch-action: pan-x;
	}
}

.Circle-module__aFAW6G__transform {
	contain: paint style;
	transform-origin: 50% 90%;
	position: absolute;
	bottom: 0;
	left: 50%;
	transform: translate(-50%) rotatex(68deg) translatey(15%) scale(.7);
}

@media (max-width: 640px) {
	.Circle-module__aFAW6G__transform {
		transform: translate(-50%) rotatex(62deg) translatey(14%) scale(.5);
	}
}

.Circle-module__aFAW6G__circle {
	will-change: transform;
	transform-style: preserve-3d;
	-webkit-backface-visibility: hidden;
	backface-visibility: hidden;
}

@media (prefers-reduced-motion: no-preference) {
	.Circle-module__aFAW6G__circle {
		animation: Circle-module__aFAW6G__fadeIn 4s 1s var(--ease-out-quad) both, Circle-module__aFAW6G__circleIn 4s 1s var(--ease-out-circ) backwards;
	}
}

@keyframes Circle-module__aFAW6G__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes Circle-module__aFAW6G__circleIn {
	0% {
		transform: rotate(-.5turn);
	}

	to {
		transform: rotate(0);
	}
}

.Spacer-module__1ERWdW__root {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	width: 1px;
	min-width: 1px;
	height: 1px;
	min-height: 1px;
	margin-top: calc(var(--height, 0px) - 1px);
	margin-left: calc(var(--width, 0px) - 1px);
	display: block;
}

.Spacer-module__1ERWdW__inline {
	display: inline-block;
}

.IconButton-module__JkbYSq__root {
	width: var(--button-height);
}

.Stats-module__0nDXYW__statsGrid {
	grid-gap: 16px;
	grid-template-columns: repeat(2, 1fr);
	gap: 16px;
	margin: 40px -25px;
	display: grid;
}

@media (max-width: 1024px) {
	.Stats-module__0nDXYW__statsGrid {
		grid-template-columns: 1fr;
		margin-left: 0;
		margin-right: 0;
	}
}

@media (max-width: 768px) {
	.Stats-module__0nDXYW__statsGrid {
		grid-template-columns: repeat(2, 1fr);
	}
}

@media (max-width: 640px) {
	.Stats-module__0nDXYW__statsGrid {
		grid-template-columns: 1fr;
	}
}

.Stats-module__0nDXYW__card {
	background: var(--color-bg-level-1);
	border: 1px solid var(--color-border-translucent);
	cursor: pointer;
	border-radius: 8px;
	flex-direction: column;
	justify-content: space-between;
	height: 184px;
	padding: 24px 24px 16px;
	transition: filter .2s ease-out;
	display: flex;
}

.Stats-module__0nDXYW__card:hover {
	filter: brightness(125%);
}

.Stats-module__0nDXYW__card:hover .Stats-module__0nDXYW__cardButton {
	background: var(--color-bg-level-3);
}

.Stats-module__0nDXYW__cardButton {
	background: 0 0;
}

.Stats-module__0nDXYW__statDialog {
	outline: none;
}

.Stats-module__0nDXYW__statDialog[data-state="open"] {
	animation: Stats-module__0nDXYW__scaleIn .175s var(--ease-out-quad);
}

.Stats-module__0nDXYW__statDialog[data-state="closed"] {
	animation: Stats-module__0nDXYW__scaleOut .175s var(--ease-out-quad);
}

.Stats-module__0nDXYW__statDialogBody {
	background: var(--color-bg-level-1);
	border: 1px solid var(--color-border-primary);
	border-radius: 16px;
	padding: 32px;
}

.Stats-module__0nDXYW__legendWrapper {
	cursor: default;
	border: 1px solid var(--color-border-translucent);
	border-radius: 6px;
	padding: 4px 8px;
	transition: opacity .2s;
}

.Stats-module__0nDXYW__marker {
	border-radius: 2px;
	width: 16px;
	height: 16px;
}

.Stats-module__0nDXYW__marker.Stats-module__0nDXYW__markerPrimary {
	background: var(--color-text-secondary);
}

.Stats-module__0nDXYW__marker.Stats-module__0nDXYW__markerSecondary {
	background: var(--color-text-quaternary);
}

.Stats-module__0nDXYW__barContainer {
	pointer-events: none;
	border-radius: 2px;
	width: 56px;
	height: 240px;
	display: flex;
	position: relative;
}

.Stats-module__0nDXYW__bar {
	transition: opacity var(--speed-regularTransition);
	border-radius: 2px;
	position: absolute;
	bottom: 0;
	left: 0;
	right: 0;
}

.Stats-module__0nDXYW__bar.Stats-module__0nDXYW__barSecondary {
	background: var(--color-text-quaternary);
}

.Stats-module__0nDXYW__bar.Stats-module__0nDXYW__barPrimary {
	background: var(--color-text-secondary);
}

.Stats-module__0nDXYW__closeButton {
	background: 0 0;
	order: 3;
	margin-left: auto;
}

.Stats-module__0nDXYW__closeButton:hover {
	background: var(--color-bg-level-3);
}

@keyframes Stats-module__0nDXYW__scaleIn {
	0% {
		opacity: 0;
		transform: translate(-50%, -50%) scale(.96);
	}

	to {
		opacity: 1;
		transform: translate(-50%, -50%) scale(1);
	}
}

@keyframes Stats-module__0nDXYW__scaleOut {
	0% {
		opacity: 1;
		transform: translate(-50%, -50%) scale(1);
	}

	to {
		opacity: 0;
		transform: translate(-50%, -50%) scale(.96);
	}
}

.Stats-module__0nDXYW__question[data-after-legend="true"] {
	order: 2;
}

.GridOverlap-module__WHHxia__root {
	grid-template-rows: 1fr;
	grid-template-columns: 1fr;
	place-items: center;
	display: grid;
}

.GridOverlap-module__WHHxia__root > * {
	grid-area: 1 / 1;
}

.NotificationAsset-module__d0iS0a__root {
	--base-x: 10%;
	--base-z: 180px;
	--y: 0;
	--c: 40;
	--z: 0;
	aspect-ratio: 432 / 320;
	contain: strict;
	isolation: isolate;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	--green: #68cc58;
	--green-dim: rgba(104, 204, 88, .25);
	--orange: #f2994a;
	--orange-dim: rgba(242, 153, 74, .25);
	--red: #c52828;
	--red-dim: rgba(197, 40, 40, .25);
	width: 100%;
	max-width: 100%;
	max-height: 100%;
	position: relative;
	overflow: hidden;
}

.NotificationAsset-module__d0iS0a__root::after {
	content: "";
	pointer-events: none;
	z-index: 1;
	background: linear-gradient(to bottom, var(--color-bg-primary) 0%, transparent 30%), linear-gradient(to right, transparent 60%, var(--color-bg-primary) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.NotificationAsset-module__d0iS0a__cards {
	perspective: 2000px;
	perspective-origin: 50%;
	width: 100%;
	height: 100%;
}

.NotificationAsset-module__d0iS0a__card {
	isolation: isolate;
	contain: paint;
	white-space: nowrap;
	-webkit-backdrop-filter: blur(10px);
	backdrop-filter: blur(10px);
	border: 1px solid rgba(255, 255, 255, .1);
	border-radius: 16px;
	width: 500px;
	height: -moz-fit-content;
	height: fit-content;
	margin: auto;
	padding: 16px;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	overflow: hidden;
}

.NotificationAsset-module__d0iS0a__root .NotificationAsset-module__d0iS0a__card {
	transform: translatez(var(--z)) translatex(var(--x)) translatey(var(--y));
}

.NotificationAsset-module__d0iS0a__root .NotificationAsset-module__d0iS0a__card:first-child {
	--x: 10%;
	--y: -60%;
	--z: 0;
	background: rgba(var(--c), var(--c), var(--c), .2);
}

.NotificationAsset-module__d0iS0a__root .NotificationAsset-module__d0iS0a__card:nth-child(2) {
	--x: 5%;
	--y: -35%;
	--z: 0;
	-webkit-backdrop-filter: blur(16px);
	backdrop-filter: blur(16px);
	background: rgba(var(--c), var(--c), var(--c), .2);
}

.NotificationAsset-module__d0iS0a__root .NotificationAsset-module__d0iS0a__card:last-child {
	--x: 0;
	--y: 0;
	--z: 0;
	background: rgba(var(--c), var(--c), var(--c), .4);
}

.NotificationAsset-module__d0iS0a__root .NotificationAsset-module__d0iS0a__card:last-child .NotificationAsset-module__d0iS0a__cardInner {
	opacity: 1;
	filter: none;
}

.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card {
	transform: skewy(-4deg) rotatex(-14deg) rotatey(20deg) translatez(var(--z)) translatex(var(--x)) translatey(var(--y));
	transform-style: preserve-3d;
	transition: .32s var(--ease-out-quad);
	transition-property: transform, background;
}

.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:first-child {
	--x: calc(var(--base-x) + 3%);
	--y: -15%;
	--z: calc(-1 * var(--base-z));
	background: rgba(var(--c), var(--c), var(--c), .2);
}

.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:nth-child(2) {
	--x: var(--base-x);
	--y: -15%;
	--z: 0;
	-webkit-backdrop-filter: blur(16px);
	backdrop-filter: blur(16px);
	background: rgba(var(--c), var(--c), var(--c), .2);
}

.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:last-child {
	--x: calc(var(--base-x) - 3%);
	--y: -15%;
	--z: var(--base-z);
	background: rgba(var(--c), var(--c), var(--c), .4);
}

.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:last-child .NotificationAsset-module__d0iS0a__cardInner {
	opacity: 1;
	filter: none;
}

@media (any-hover: hover) {
	.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:hover {
		background: rgba(255, 255, 255, .08);
	}

	.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:hover .NotificationAsset-module__d0iS0a__cardInner {
		opacity: 1;
		filter: none;
	}

	.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:hover:first-child {
		--y: -40%;
	}

	.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:hover:nth-child(2) {
		--y: -30%;
	}

	.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso .NotificationAsset-module__d0iS0a__card:hover:last-child {
		--y: -25%;
	}
}

.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso:has(.NotificationAsset-module__d0iS0a__card:hover) > .NotificationAsset-module__d0iS0a__card:not(:hover) {
	background: rgba(var(--c), var(--c), var(--c), .1);
}

.NotificationAsset-module__d0iS0a__root.NotificationAsset-module__d0iS0a__iso:has(.NotificationAsset-module__d0iS0a__card:hover) > .NotificationAsset-module__d0iS0a__card:not(:hover) .NotificationAsset-module__d0iS0a__cardInner {
	filter: grayscale();
	opacity: .2;
}

.NotificationAsset-module__d0iS0a__cardInner {
	opacity: .2;
	filter: grayscale();
	transition: .32s var(--ease-out-quad);
	transition-property: opacity;
}

.CopyButton-module__DqaEuG__check,
.CopyButton-module__DqaEuG__copy {
	transition: var(--speed-regularTransition);
	transition-property: opacity, transform;
}

.CopyButton-module__DqaEuG__check {
	opacity: 0;
}

.CopyButton-module__DqaEuG__root[data-copied="true"] .CopyButton-module__DqaEuG__check {
	opacity: 1;
}

.CopyButton-module__DqaEuG__root[data-copied="true"] .CopyButton-module__DqaEuG__copy,
.CopyButton-module__DqaEuG__root[data-copied="false"] .CopyButton-module__DqaEuG__check {
	opacity: 0;
	transform: scale(.8);
}

.CopyButton-module__DqaEuG__root[data-copied="false"] .CopyButton-module__DqaEuG__copy {
	opacity: 1;
}

.Scrollable-module__hF-PvG__root {
	--scrollbar-size: 16px;
	--scrollbar-gap: 5px;
	width: 100%;
	height: 100%;
	position: relative;
	overflow: hidden;
}

.Scrollable-module__hF-PvG__viewport {
	overscroll-behavior: contain;
	scroll-behavior: auto;
	--s: var(--Scrollable-shadow-start, var(--Scrollable-shadow-size, 0px));
	--e: var(--Scrollable-shadow-end, var(--Scrollable-shadow-size, 0px));
	width: 100%;
	height: 100%;
}

.Scrollable-module__hF-PvG__viewport > div[style]:first-child {
	position: relative;
	display: block !important;
}

.Scrollable-module__hF-PvG__viewport[data-shadow="horizontal"] {
	scroll-padding-inline: var(--s) var(--e);
	padding-inline: var(--s) var(--e);
	-webkit-mask-image: linear-gradient(to right, var(--mask-invisible) 0%, var(--mask-ease) calc(var(--s) / 2), var(--mask-visible) var(--s), var(--mask-visible) calc(100% - var(--e)), var(--mask-ease) calc(100% - calc(var(--e) / 2)), var(--mask-invisible) 100%);
	-webkit-mask-image: linear-gradient(to right, var(--mask-invisible) 0%, var(--mask-ease) calc(var(--s) / 2), var(--mask-visible) var(--s), var(--mask-visible) calc(100% - var(--e)), var(--mask-ease) calc(100% - calc(var(--e) / 2)), var(--mask-invisible) 100%);
	mask-image: linear-gradient(to right, var(--mask-invisible) 0%, var(--mask-ease) calc(var(--s) / 2), var(--mask-visible) var(--s), var(--mask-visible) calc(100% - var(--e)), var(--mask-ease) calc(100% - calc(var(--e) / 2)), var(--mask-invisible) 100%);
}

.Scrollable-module__hF-PvG__viewport[data-shadow="vertical"] {
	scroll-padding-block: var(--s) var(--e);
	padding-block: var(--s) var(--e);
	-webkit-mask-image: linear-gradient(to bottom, var(--mask-invisible) 0%, var(--mask-ease) calc(var(--s) / 2), var(--mask-visible) var(--s), var(--mask-visible) calc(100% - var(--e)), var(--mask-ease) calc(100% - calc(var(--e) / 2)), var(--mask-invisible) 100%);
	-webkit-mask-image: linear-gradient(to bottom, var(--mask-invisible) 0%, var(--mask-ease) calc(var(--s) / 2), var(--mask-visible) var(--s), var(--mask-visible) calc(100% - var(--e)), var(--mask-ease) calc(100% - calc(var(--e) / 2)), var(--mask-invisible) 100%);
	mask-image: linear-gradient(to bottom, var(--mask-invisible) 0%, var(--mask-ease) calc(var(--s) / 2), var(--mask-visible) var(--s), var(--mask-visible) calc(100% - var(--e)), var(--mask-ease) calc(100% - calc(var(--e) / 2)), var(--mask-invisible) 100%);
}

.Scrollable-module__hF-PvG__scrollbar {
	z-index: var(--layer-scrollbar);
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	touch-action: none;
	padding: var(--scrollbar-gap);
	background: 0 0;
	transition: width .12s, height .12s, opacity .12s;
	display: flex;
}

@media (hover: none) {
	.Scrollable-module__hF-PvG__scrollbar {
		--scrollbar-size: 9px;
		--scrollbar-gap: 3px;
	}

	.Scrollable-module__hF-PvG__scrollbar:active {
		--scrollbar-size: 14px;
	}
}

@media (hover: hover) {
	.Scrollable-module__hF-PvG__scrollbar:hover {
		--scrollbar-size: 19px;
	}
}

.Scrollable-module__hF-PvG__scrollbar[data-orientation="vertical"] {
	width: var(--scrollbar-size);
}

.Scrollable-module__hF-PvG__scrollbar[data-state="visible"] {
	animation: .12s ease-in forwards Scrollable-module__hF-PvG__scrollbarIn;
}

.Scrollable-module__hF-PvG__scrollbar[data-state="hidden"] {
	animation: .12s ease-in forwards Scrollable-module__hF-PvG__scrollbarOut;
}

@keyframes Scrollable-module__hF-PvG__scrollbarIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes Scrollable-module__hF-PvG__scrollbarOut {
	0% {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}

.Scrollable-module__hF-PvG__thumb {
	background: var(--scrollbar-color);
	border-radius: var(--scrollbar-size);
	flex: 1;
	transition: background .12s;
	position: relative;
}

@media (hover: none) {
	.Scrollable-module__hF-PvG__thumb {
		--moreHitArea-size: 44px;
	}
}

@media (hover: hover) {
	.Scrollable-module__hF-PvG__thumb {
		--moreHitArea-size: 12px;
	}

	.Scrollable-module__hF-PvG__thumb:hover {
		background: var(--scrollbar-color-hover);
	}
}

.Scrollable-module__hF-PvG__thumb:active {
	background: var(--scrollbar-color-active);
}

.Eyebrow-module__kZTp2W__eyebrowIndicator {
	border-radius: var(--rounded-full);
	width: 14px;
	height: 8px;
}

.Eyebrow-module__kZTp2W__eyebrowIndicator.Eyebrow-module__kZTp2W__outline {
	border: 1px solid var(--color-text-quaternary);
	background: 0 0;
}

.Codeblock-module__NYCDmG__root {
	position: relative;
}

.Codeblock-module__NYCDmG__root pre {
	padding: 0;
	padding-top: 16px;
	padding-bottom: 16px;
}

.Codeblock-module__NYCDmG__root pre [data-line]:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 16px;
	padding-right: 64px;
}

.Codeblock-module__NYCDmG__root pre [data-line]:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 16px;
	padding-right: 64px;
}

.Codeblock-module__NYCDmG__root pre [data-line]:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 16px;
	padding-right: 64px;
}

.Codeblock-module__NYCDmG__root pre [data-line]:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 64px;
	padding-right: 16px;
}

.Codeblock-module__NYCDmG__root pre [data-line]:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 64px;
	padding-right: 16px;
}

.Codeblock-module__NYCDmG__root pre [data-line]:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 64px;
	padding-right: 16px;
}

.Codeblock-module__NYCDmG__root pre [data-line][data-highlighted-line] {
	background: var(--color-bg-quaternary);
}

.Codeblock-module__NYCDmG__root pre [data-line] span {
	color: var(--shiki-light);
}

[data-theme="dark"] :is(.Codeblock-module__NYCDmG__root pre [data-line] span) {
	color: var(--shiki-dark);
}

[data-theme="glass"] :is(.Codeblock-module__NYCDmG__root pre [data-line] span) {
	color: var(--shiki-dark);
}

@media (any-hover: hover) {
	.Codeblock-module__NYCDmG__root pre:hover .Codeblock-module__NYCDmG__copy {
		opacity: 1;
	}
}

@media (hover: none) {
	.Codeblock-module__NYCDmG__root pre .Codeblock-module__NYCDmG__copy {
		opacity: 1;
	}
}

.Codeblock-module__NYCDmG__copy.Codeblock-module__NYCDmG__copy {
	transition: opacity var(--speed-regularTransition);
	position: absolute;
	top: 12px;
	right: 12px;
}

.Codeblock-module__NYCDmG__code[data-line-numbers] {
	counter-reset: line;
}

.Codeblock-module__NYCDmG__code[data-line-numbers] > [data-line]::before {
	counter-increment: line;
	content: counter(line);
	text-align: right;
	color: gray;
	width: .75rem;
	margin-right: 1.25rem;
	display: inline-block;
}

.Codeblock-module__NYCDmG__code[data-line-numbers-max-digits="2"] > [data-line]::before {
	width: 1.25rem;
}

.Codeblock-module__NYCDmG__code[data-line-numbers-max-digits="3"] > [data-line]::before {
	width: 1.75rem;
}

.Codeblock-module__NYCDmG__code[data-line-numbers-max-digits="4"] > [data-line]::before {
	width: 2.25rem;
}

.StatsGrid-module__KWvh1G__statsGrid {
	grid-template-columns: repeat(2, var(--1fr));
	grid-column-gap: 48px;
	-moz-column-gap: 48px;
	grid-row-gap: 40px;
	grid-template-rows: repeat(auto-fill, 1fr);
	place-items: start center;
	gap: 40px 48px;
	display: grid;
}

.StatsGrid-module__KWvh1G__title {
	font-size: 80px;
	line-height: 68px;
	font-weight: var(--font-weight-medium);
}

@media (max-width: 640px) {
	.StatsGrid-module__KWvh1G__title {
		letter-spacing: -.015em;
		font-size: 40px;
		line-height: 44px;
	}
}

.Edit-module__B2dPta__edit {
	border-top: 1px solid var(--color-border-primary);
	margin-top: 32px;
	padding-top: 32px;
	font-size: 14px;
}

.UnderTheHood-module__Dtn-qq__orange {
	fill: #fc7840;
}

@media (dynamic-range: high) or (color-gamut: p3) {
	.UnderTheHood-module__Dtn-qq__orange {
		fill: #ff530e;
		fill: color(display-p3 1.00385 .318351 .0169828);
		fill: lab(61.7078% 78.1977 99.9129);
	}
}

.ImagePreviews-module__PU3wma__mobile {
	overscroll-behavior-x: contain;
	margin-left: calc(-1 * var(--page-padding-left));
	margin-right: calc(-1 * var(--page-padding-right));
	padding-left: var(--page-padding-left);
	scroll-snap-type: x mandatory;
	padding-bottom: 24px;
	overflow-x: auto;
}

.ImagePreviews-module__PU3wma__mobile::after {
	content: "";
	min-height: 1px;
	min-width: var(--page-padding-right);
}

.ImagePreviews-module__PU3wma__mobile img {
	scroll-snap-align: center;
	min-width: 300px;
}

.ImagePreviews-module__PU3wma__mobile figcaption {
	margin-top: 16px;
}

.ImagePreviews-module__PU3wma__desktop {
	flex-direction: column;
	display: flex;
}

@media (max-width: 700px) {
	.ImagePreviews-module__PU3wma__desktop {
		display: none;
	}
}

.ImagePreviews-module__PU3wma__figure {
	width: 100%;
	margin-right: 24px;
}

.ImagePreviews-module__PU3wma__zoom {
	margin-bottom: 12px;
}

.ImagePreviews-module__PU3wma__caption {
	word-break: break-word;
	max-width: 100%;
	font-size: var(--font-size-mini);
	line-height: var(--line-height-mini);
	color: var(--color-text-tertiary);
	-webkit-line-clamp: 2;
	-webkit-box-orient: vertical;
	min-height: 2lh;
	margin-top: 12px;
	padding: 0;
	display: -webkit-box;
	overflow: hidden;
}

.ImagePreviews-module__PU3wma__imageButton {
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	font: inherit;
	color: inherit;
	cursor: pointer;
	transition: box-shadow var(--speed-regularTransition);
	background: 0 0;
	border: none;
	border-radius: 8px;
	justify-content: center;
	align-items: center;
	margin: 0;
	padding: 0;
	display: flex;
}

.ImagePreviews-module__PU3wma__imageButton img {
	max-width: 124px;
}

.ImagePreviews-module__PU3wma__activeImageButton {
	box-shadow: 0 0 0 4px var(--color-bg-primary), 0 0 0 6px var(--color-brand-bg);
}

.Tooltip-module__OLCuMG__content {
	background: var(--color-bg-primary);
	border: 1px solid var(--color-border-primary);
	border-radius: var(--radius-8);
	box-shadow: var(--shadow-high);
	color: var(--color-text-secondary);
	font-weight: var(--font-weight-medium);
	max-width: 280px;
	z-index: var(--layer-tooltip);
	transform-origin: var(--radix-tooltip-content-transform-origin);
	align-items: center;
	padding: 6px 8px;
	font-size: 12px;
	line-height: 17px;
	display: flex;
}

.Tooltip-module__OLCuMG__content[data-state="delayed-open"] {
	animation: Tooltip-module__OLCuMG__tooltipOpen .12s var(--ease-out-quad) forwards;
}

.Tooltip-module__OLCuMG__content[data-state="closed"] {
	animation: Tooltip-module__OLCuMG__tooltipClose .12s var(--ease-out-quad) forwards;
}

.Tooltip-module__OLCuMG__align-center {
	text-align: center;
}

.Tooltip-module__OLCuMG__variant-glass {
	-webkit-backdrop-filter: blur(24px);
	backdrop-filter: blur(24px);
	color: var(--color-text-primary);
	background: rgba(255, 255, 255, .1);
	border: 1px solid rgba(255, 255, 255, .1);
}

@keyframes Tooltip-module__OLCuMG__tooltipOpen {
	0% {
		opacity: 0;
		transform: scale(.9);
	}

	to {
		opacity: 1;
		transform: scale(1);
	}
}

@keyframes Tooltip-module__OLCuMG__tooltipClose {
	0% {
		opacity: 1;
		transform: scale(1);
	}

	to {
		opacity: 0;
		transform: scale(.9);
	}
}

.Toast-module__ZoHshG__toast {
	box-shadow: var(--shadow-medium);
	border: 1px solid var(--color-border-primary);
	box-sizing: border-box;
	background: var(--color-bg-primary);
	border-radius: 6px;
	align-items: center;
	width: 364px;
	margin: auto;
	padding: 16px 24px 16px 16px;
	display: flex;
}

@media (max-width: 640px) {
	.Toast-module__ZoHshG__toast {
		width: 100%;
	}
}

.Toast-module__ZoHshG__iconWrapper {
	flex-shrink: 0;
	width: 16px;
	height: 16px;
	margin-right: 8px;
	display: flex;
}

.Toast-module__ZoHshG__iconWrapper svg {
	color: currentColor;
	width: 100%;
	height: 100%;
}

.Toast-module__ZoHshG__toastWrapper {
	--offset: 16px;
	bottom: var(--offset);
	right: var(--offset);
	height: auto;
	z-index: var(--layer-toasts);
	position: fixed;
}

@media (max-width: 640px) {
	.Toast-module__ZoHshG__toastWrapper {
		--offset: var(--page-padding-right);
	}
}

.VideoPlayer-module__FjptYW__root {
	pointer-events: auto;
	border-radius: var(--radius-8);
}

.VideoPlayer-module__FjptYW__root:-webkit-full-screen {
	width: auto;
	max-width: 100%;
	max-height: 100%;
	width: initial;
	min-width: 0;
	min-width: initial;
	background: #000;
}

.VideoPlayer-module__FjptYW__root:fullscreen {
	width: auto;
	max-width: 100%;
	max-height: 100%;
	width: initial;
	min-width: 0;
	min-width: initial;
	background: #000;
}

.VideoPlayer-module__FjptYW__root:-webkit-full-screen .VideoPlayer-module__FjptYW__videoContainer {
	border-radius: 0;
	margin: auto;
	height: 100% !important;
	max-height: none !important;
	max-height: initial !important;
}

.VideoPlayer-module__FjptYW__root:fullscreen .VideoPlayer-module__FjptYW__videoContainer {
	border-radius: 0;
	margin: auto;
	height: 100% !important;
	max-height: none !important;
	max-height: initial !important;
}

.VideoPlayer-module__FjptYW__root:-webkit-full-screen .VideoPlayer-module__FjptYW__video {
	width: 100%;
	height: 100%;
}

.VideoPlayer-module__FjptYW__root:fullscreen .VideoPlayer-module__FjptYW__video {
	width: 100%;
	height: 100%;
}

.VideoPlayer-module__FjptYW__root::-moz-selection {
	background: var(--color-selection-dim);
}

.VideoPlayer-module__FjptYW__root ::-moz-selection {
	background: var(--color-selection-dim);
}

.VideoPlayer-module__FjptYW__root::selection,
.VideoPlayer-module__FjptYW__root ::selection {
	background: var(--color-selection-dim);
}

.VideoPlayer-module__FjptYW__videoContainer {
	border-radius: var(--radius-8);
	width: 100%;
	position: relative;
	overflow: hidden;
}

.VideoPlayer-module__FjptYW__video {
	max-width: 100%;
	height: auto;
}

.VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__captions) .VideoPlayer-module__FjptYW__video::cue {
	opacity: 0 !important;
	visibility: hidden !important;
	background: 0 0 !important;
	display: none !important;
}

.VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__captions) .VideoPlayer-module__FjptYW__video::-webkit-media-text-track-container {
	opacity: 0 !important;
	visibility: hidden !important;
	background: 0 0 !important;
	display: none !important;
}

.VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__captions) .VideoPlayer-module__FjptYW__video::-webkit-media-text-track-display {
	opacity: 0 !important;
	visibility: hidden !important;
	background: 0 0 !important;
	display: none !important;
}

.VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__captions) .VideoPlayer-module__FjptYW__video::-webkit-media-text-track-display-backdrop {
	opacity: 0 !important;
	visibility: hidden !important;
	background: 0 0 !important;
	display: none !important;
}

.VideoPlayer-module__FjptYW__variant-viewport {
	max-width: var(--width, 1280px);
	width: 100vw;
	min-width: 320px;
}

@media (min-aspect-ratio: 16/9) {
	.VideoPlayer-module__FjptYW__variant-viewport.VideoPlayer-module__FjptYW__aspect-16\:9.VideoPlayer-module__FjptYW__root {
		width: auto;
		position: relative;
	}

	.VideoPlayer-module__FjptYW__variant-viewport.VideoPlayer-module__FjptYW__aspect-16\:9 .VideoPlayer-module__FjptYW__videoContainer {
		width: auto;
		height: 100vh;
		max-height: min(var(--height, 720px), calc(100vh - 16px * 2));
	}

	.VideoPlayer-module__FjptYW__variant-viewport.VideoPlayer-module__FjptYW__aspect-16\:9 .VideoPlayer-module__FjptYW__video {
		width: auto;
		height: 100%;
	}
}

@media (min-aspect-ratio: 4/3) {
	.VideoPlayer-module__FjptYW__variant-viewport.VideoPlayer-module__FjptYW__aspect-4\:3.VideoPlayer-module__FjptYW__root {
		width: auto;
		position: relative;
	}

	.VideoPlayer-module__FjptYW__variant-viewport.VideoPlayer-module__FjptYW__aspect-4\:3 .VideoPlayer-module__FjptYW__videoContainer {
		width: auto;
		height: 100vh;
		max-height: min(var(--height, 720px), calc(100vh - 16px * 2));
	}

	.VideoPlayer-module__FjptYW__variant-viewport.VideoPlayer-module__FjptYW__aspect-4\:3 .VideoPlayer-module__FjptYW__video {
		width: auto;
		height: 100%;
	}
}

.VideoPlayer-module__FjptYW__variant-inline {
	max-width: 100%;
}

.VideoPlayer-module__FjptYW__variant-inline .VideoPlayer-module__FjptYW__videoContainer {
	border: 1px solid var(--color-border-translucent);
}

.VideoPlayer-module__FjptYW__container {
	contain: strict;
	isolation: isolate;
	pointer-events: none;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	container: video-player / size;
}

.VideoPlayer-module__FjptYW__captions {
	pointer-events: none;
	text-wrap: balance;
	left: 0;
	right: 0;
	text-align: center;
	letter-spacing: -.47px;
	width: -moz-fit-content;
	width: fit-content;
	max-width: min(80%, 760px);
	color: var(--color-text-primary);
	font-size: max(16px, min(2cqw, 48px));
	line-height: 1.4;
	font-weight: var(--font-weight-medium);
	transition: .48s var(--ease-out-cubic);
	background: rgba(0, 0, 0, .48);
	border-radius: max(4px, min(1cqw, 8px));
	justify-content: center;
	align-items: center;
	margin-left: auto;
	margin-right: auto;
	padding: 0 8px;
	transition-property: transform;
	display: flex;
	position: absolute;
	bottom: 24px;
}

.VideoPlayer-module__FjptYW__chrome {
	pointer-events: auto;
	transition: var(--speed-regularTransition) var(--ease-out-quad);
	transition-property: opacity;
}

.VideoPlayer-module__FjptYW__controls {
	align-items: center;
	gap: 12px;
	max-width: 1120px;
	margin-left: auto;
	margin-right: auto;
	padding-left: min(80px, 10%);
	padding-right: min(80px, 10%);
	transition-property: opacity, transform;
	display: flex;
	position: absolute;
	bottom: 32px;
	left: 0;
	right: 0;
}

@container video-player (width <= 640px) {
	.VideoPlayer-module__FjptYW__controls {
		gap: 6px;
		padding-left: 12px;
		padding-right: 12px;
		bottom: 10px;
	}
}

:where(.VideoPlayer-module__FjptYW__root[data-idle="true"]:not(:has(.VideoPlayer-module__FjptYW__controls:hover))) {
	cursor: var(--cursor-none) !important;
}

:where(.VideoPlayer-module__FjptYW__root[data-idle="true"]:not(:has(.VideoPlayer-module__FjptYW__controls:hover))) * {
	cursor: var(--cursor-none) !important;
}

:where(.VideoPlayer-module__FjptYW__root[data-idle="true"]:not(:has(.VideoPlayer-module__FjptYW__controls:hover))) .VideoPlayer-module__FjptYW__chrome {
	opacity: 0;
}

:where(.VideoPlayer-module__FjptYW__root[data-idle="true"]:not(:has(.VideoPlayer-module__FjptYW__controls:hover))) .VideoPlayer-module__FjptYW__controls {
	transform: translatey(16px);
}

:where(.VideoPlayer-module__FjptYW__root.VideoPlayer-module__FjptYW__variant-inline[data-status="paused"], .VideoPlayer-module__FjptYW__root[data-idle="false"], .VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__controls:hover)) .VideoPlayer-module__FjptYW__captions {
	transform: translatey(-86px);
}

@container video-player (width <= 640px) {
	:where(.VideoPlayer-module__FjptYW__root.VideoPlayer-module__FjptYW__variant-inline[data-status="paused"], .VideoPlayer-module__FjptYW__root[data-idle="false"], .VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__controls:hover)) .VideoPlayer-module__FjptYW__captions {
		transform: translatey(-32px);
	}
}

:where(.VideoPlayer-module__FjptYW__root.VideoPlayer-module__FjptYW__variant-inline[data-status="paused"], .VideoPlayer-module__FjptYW__root[data-idle="false"], .VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__controls:hover)) .VideoPlayer-module__FjptYW__chrome {
	opacity: 1;
}

:where(.VideoPlayer-module__FjptYW__root.VideoPlayer-module__FjptYW__variant-inline[data-status="paused"], .VideoPlayer-module__FjptYW__root[data-idle="false"], .VideoPlayer-module__FjptYW__root:has(.VideoPlayer-module__FjptYW__controls:hover)) .VideoPlayer-module__FjptYW__controls {
	transform: translatey(0);
}

.VideoPlayer-module__FjptYW__scrim {
	pointer-events: none;
	background-color: rgba(0, 0, 0, .3);
	background-image: linear-gradient(0deg, rgba(0, 0, 0, .3) 0, transparent 120px);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.VideoPlayer-module__FjptYW__track {
	--track-size: 4px;
	--track-active-size: var(--track-size);
	cursor: crosshair;
	border-radius: var(--radius-rounded);
	height: var(--track-size);
	transition: var(--speed-regularTransition) var(--ease-out-quad);
	background: rgba(255, 255, 255, .16);
	flex-grow: 1;
	transition-property: height;
	position: relative;
}

.VideoPlayer-module__FjptYW__track:active {
	height: var(--track-active-size);
}

.VideoPlayer-module__FjptYW__trackMask {
	pointer-events: none;
	border-radius: var(--radius-rounded);
	height: 100%;
	position: relative;
	overflow: hidden;
}

.VideoPlayer-module__FjptYW__progress {
	--track-active-size: 7px;
	--moreHitArea-inset: -24px -8px;
}

.VideoPlayer-module__FjptYW__range {
	pointer-events: none;
	position: absolute;
	top: 0;
	bottom: 0;
}

.VideoPlayer-module__FjptYW__range[data-type="played"] {
	background: var(--color-white);
}

.VideoPlayer-module__FjptYW__range[data-type="played"]:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	left: 0;
	right: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="played"]:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	left: 0;
	right: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="played"]:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	left: 0;
	right: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="played"]:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	right: 0;
	left: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="played"]:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	right: 0;
	left: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="played"]:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	right: 0;
	left: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="buffered"] {
	background: var(--color-white);
	opacity: .16;
}

.VideoPlayer-module__FjptYW__range[data-type="buffered"]:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	left: calc(var(--media-player-range-start) * 1%);
	right: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="buffered"]:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	left: calc(var(--media-player-range-start) * 1%);
	right: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="buffered"]:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	left: calc(var(--media-player-range-start) * 1%);
	right: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="buffered"]:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	right: calc(var(--media-player-range-start) * 1%);
	left: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="buffered"]:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	right: calc(var(--media-player-range-start) * 1%);
	left: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="buffered"]:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	right: calc(var(--media-player-range-start) * 1%);
	left: calc(100% - var(--media-player-range-end) * 1%);
}

.VideoPlayer-module__FjptYW__range[data-type="volume"] {
	background: var(--color-white);
	top: calc(100% - var(--media-player-range-end) * 1%);
	bottom: 0;
	left: 0;
	right: 0;
}

.VideoPlayer-module__FjptYW__glassContainer {
	border-radius: var(--radius-8);
	height: 32px;
	transition: .16s var(--ease-out-quad);
	padding: 0 12px;
	transition-property: border, background-color, color, box-shadow, opacity, filter, transform;
}

@media (any-hover: hover) {
	.VideoPlayer-module__FjptYW__glassContainer:not([disabled]):hover {
		-webkit-backdrop-filter: blur(8px);
		backdrop-filter: blur(8px);
		background: rgba(255, 255, 255, .16);
	}
}

.VideoPlayer-module__FjptYW__glassContainer:not([disabled]):focus,
.VideoPlayer-module__FjptYW__glassContainer:not([disabled]):focus-within,
.VideoPlayer-module__FjptYW__glassContainer.VideoPlayer-module__FjptYW__show {
	-webkit-backdrop-filter: blur(8px);
	backdrop-filter: blur(8px);
	background: rgba(255, 255, 255, .16);
}

.VideoPlayer-module__FjptYW__playbackRate {
	font-size: 13px;
	font-weight: var(--font-weight-medium);
	text-align: center;
	text-align-last: center;
}

@container video-player (width <= 640px) {
	.VideoPlayer-module__FjptYW__playbackRate,
	.VideoPlayer-module__FjptYW__pip {
		display: none;
	}
}

.VideoPlayer-module__FjptYW__mute,
.VideoPlayer-module__FjptYW__sound {
	position: relative;
}

.VideoPlayer-module__FjptYW__volumePositioner {
	--volume-size: 32px;
	min-width: var(--volume-size);
	pointer-events: none;
	border-radius: var(--radius-8);
	visibility: hidden;
	justify-content: center;
	align-items: center;
	padding-top: 12px;
	padding-bottom: 12px;
	display: flex;
	position: absolute;
	bottom: calc(100% + 8px);
	left: 50%;
	transform: translate(-50%);
}

@media (any-hover: hover) {
	.VideoPlayer-module__FjptYW__volumePositioner:hover {
		visibility: visible;
		pointer-events: auto;
	}

	.VideoPlayer-module__FjptYW__root:has([data-sound]:not(:disabled):hover) .VideoPlayer-module__FjptYW__volumePositioner {
		visibility: visible;
		pointer-events: auto;
	}
}

.VideoPlayer-module__FjptYW__volumePositioner:focus {
	visibility: visible;
	pointer-events: auto;
}

.VideoPlayer-module__FjptYW__root:has([data-sound]:not(:disabled):focus-within) .VideoPlayer-module__FjptYW__volumePositioner {
	visibility: visible;
	pointer-events: auto;
}

.VideoPlayer-module__FjptYW__volumePositioner:has([data-state="interacting"]) {
	visibility: visible;
	pointer-events: auto;
}

.VideoPlayer-module__FjptYW__volumePositioner:focus-visible .VideoPlayer-module__FjptYW__volumeThumb {
	outline: var(--focus-ring-outline);
	outline-offset: var(--focus-ring-offset);
}

.VideoPlayer-module__FjptYW__volumePositioner::before {
	content: "";
	position: absolute;
	top: -8px;
	bottom: -12px;
	left: -8px;
	right: -8px;
}

.VideoPlayer-module__FjptYW__volumeTint {
	pointer-events: none;
	border-radius: var(--radius-8);
	-webkit-backdrop-filter: blur(8px);
	backdrop-filter: blur(8px);
	background: rgba(255, 255, 255, .16);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.VideoPlayer-module__FjptYW__volumeControl {
	--track-size: 4px;
	--moreHitArea-inset: -12px -2px;
	cursor: crosshair;
	width: var(--track-size);
	border-radius: var(--radius-rounded);
	background: rgba(255, 255, 255, .16);
	height: 56px;
	position: relative;
}

.VideoPlayer-module__FjptYW__volumeThumb {
	pointer-events: none;
	border-radius: var(--radius-circle);
	background: var(--color-white);
	width: 8px;
	height: 8px;
	left: calc(50% - 4px);
	bottom: calc(var(--media-player-thumb-start) * 1% - 4px);
	position: absolute;
}

.VideoPlayer-module__FjptYW__thumb {
	pointer-events: none;
}

.VideoPlayer-module__FjptYW__previewLineThumb,
.VideoPlayer-module__FjptYW__timestampThumb {
	opacity: 0;
	transition: var(--speed-regularTransition) var(--ease-out-quad);
	transition-property: opacity, background;
}

.VideoPlayer-module__FjptYW__track:hover .VideoPlayer-module__FjptYW__previewLineThumb,
.VideoPlayer-module__FjptYW__track:hover .VideoPlayer-module__FjptYW__timestampThumb {
	opacity: 1;
}

.VideoPlayer-module__FjptYW__previewLineThumb {
	width: 1px;
	top: -16px;
	bottom: -16px;
	left: calc(1% * var(--media-player-thumb-start));
	border-radius: var(--radius-rounded);
	background: rgba(255, 255, 255, .48);
	position: absolute;
}

.VideoPlayer-module__FjptYW__track:active .VideoPlayer-module__FjptYW__previewLineThumb {
	background: var(--color-white);
}

@container video-player (width <= 640px) {
	.VideoPlayer-module__FjptYW__previewLineThumb {
		display: none;
	}
}

.VideoPlayer-module__FjptYW__timestampThumb {
	left: calc(1% * var(--media-player-thumb-start));
	width: -moz-fit-content;
	width: fit-content;
	height: 16px;
	position: absolute;
	bottom: calc(100% + 32px);
	transform: translate(-50%);
}

@container video-player (width <= 640px) {
	.VideoPlayer-module__FjptYW__timestampThumb {
		bottom: calc(100% + 16px);
	}
}

.VideoPlayer-module__FjptYW__kbd {
	background: rgba(255, 255, 255, .16);
	border: none;
	border-radius: 3px;
	justify-content: center;
	align-items: center;
	gap: 4px;
	min-width: 16px;
	padding: 1px 2px;
	font-size: 10px;
	display: inline-flex;
}

.VideoPlayer-module__FjptYW__fallbackPoster {
	z-index: -1;
	background: var(--color-bg-primary);
	flex-direction: column;
	justify-content: center;
	align-items: center;
	display: flex;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.FeatureLockupGrid-module__H4JNxa__featureLockupGrid {
	gap: 40px;
}

@media (max-width: 768px) {
	.FeatureLockupGrid-module__H4JNxa__featureLockupGrid {
		-moz-column-gap: 24px;
		column-gap: 24px;
	}
}

@media (max-width: 640px) {
	.FeatureLockupGrid-module__H4JNxa__featureLockup {
		flex-direction: column;
		align-items: flex-start;
	}
}

.lightbox-module__vwv6YG__overlay {
	z-index: var(--layer-dialog-overlay);
	background: rgba(0, 0, 0, .95);
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.lightbox-module__vwv6YG__lightbox {
	z-index: var(--layer-dialog);
	cursor: zoom-out;
	transition: width .4s ease-out, height .4s ease-out;
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.lightbox-module__vwv6YG__lightbox > div {
	position: absolute;
}

.lightbox-module__vwv6YG__lightbox img {
	width: 100%;
	height: 100%;
}

.lightbox-module__vwv6YG__lightbox [data-fade="true"] {
	opacity: 1 !important;
	animation: none !important;
	-webkit-mask: none !important;
	mask: none !important;
}

.lightbox-module__vwv6YG__wrapper {
	cursor: zoom-in;
	line-height: 0;
	position: relative;
}

.lightbox-module__vwv6YG__wrapper[data-hidden="true"] {
	visibility: hidden;
}

.color-module__UZINAa__primary {
	color: var(--color-text-primary);
}

.color-module__UZINAa__secondary {
	color: var(--color-text-secondary);
}

.color-module__UZINAa__tertiary {
	color: var(--color-text-tertiary);
}

.color-module__UZINAa__quaternary {
	color: var(--color-text-quaternary);
}

.Icon-module__PGbYKa__logotype {
	width: var(--Logotype-width, auto);
	height: auto;
}

.Icon-module__PGbYKa__logotype > * {
	fill: inherit;
}

.launch-module__wQAKhq__wrapper {
	border-top: 1px solid #202122;
	border-bottom: 1px solid #202122;
	flex-direction: column;
	justify-content: space-between;
	width: 100%;
	max-width: 672px;
	height: 240px;
	padding: 40px 0;
	display: flex;
	position: relative;
}

.launch-module__wQAKhq__horizontalBar {
	background-image: linear-gradient(90deg, #2c2d2e 33%, rgba(255, 255, 255, 0) 0%);
	background-position: bottom;
	background-repeat: repeat-x;
	background-size: 6px 1px;
	width: 100%;
	height: 1px;
}

.launch-module__wQAKhq__verticalBarsWrapper {
	justify-content: space-between;
	align-items: flex-end;
	padding-left: 60px;
	padding-right: 60px;
	display: flex;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	overflow: hidden;
}

@media (max-width: 640px) {
	.launch-module__wQAKhq__verticalBarsWrapper {
		gap: 20px;
		padding-left: 16px;
		padding-right: 16px;
	}
}

.launch-module__wQAKhq__verticalBar {
	background: var(--color-bg-primary);
	border-top: 1px solid var(--color-text-primary);
	width: 40px;
	position: relative;
}

.launch-module__wQAKhq__verticalBar::before {
	content: "";
	background: var(--color-bg-primary);
	width: 100%;
	height: 100%;
	position: absolute;
	top: 100%;
}

.launch-module__wQAKhq__verticalBar::after {
	content: "";
	background: #4a4c50;
	height: 1px;
	position: absolute;
	top: 16px;
	left: 0;
	right: 0;
}

@media (max-width: 640px) {
	.launch-module__wQAKhq__verticalBar:first-of-type,
	.launch-module__wQAKhq__verticalBar:last-of-type {
		display: none;
	}
}

.TableOfContents-module__Xtt2xW__aside {
	--color-base: var(--color-text-tertiary);
	--color-hover: var(--color-text-primary);
	--color-active: var(--color-text-primary);
	--color-border: var(--color-border-primary);
	--color-border-active: var(--color-text-primary);
	--font-size: 13px;
	--padding-left: 12px;
	top: calc(var(--header-height) + 32px);
	font-size: var(--font-size);
	flex-shrink: 0;
	max-width: 250px;
	position: -webkit-sticky;
	position: sticky;
}

.TableOfContents-module__Xtt2xW__aside li a {
	display: block;
}

.TableOfContents-module__Xtt2xW__container {
	position: relative;
}

.TableOfContents-module__Xtt2xW__ul {
	padding-left: var(--padding-left);
	border-left: 2px solid transparent;
	position: relative;
}

.TableOfContents-module__Xtt2xW__ul::before {
	content: "";
	border-radius: var(--rounded-full);
	background-color: var(--color-border);
	width: 2px;
	height: 100%;
	position: absolute;
	top: 0;
	left: -2px;
}

.TableOfContents-module__Xtt2xW__ul::after {
	content: "";
	border-radius: var(--rounded-full);
	background-color: var(--color-border-active);
	width: 2px;
	height: var(--height, 24px);
	transform: translatey(calc(var(--top, 0px)));
	position: absolute;
	top: 0;
	left: -2px;
}

@media (prefers-reduced-motion: no-preference) {
	.TableOfContents-module__Xtt2xW__ul::after {
		transition: var(--speed-regularTransition);
		transition-property: transform, height;
	}
}

.TableOfContents-module__Xtt2xW__ul li {
	margin-left: 0;
	padding: 0;
	list-style-type: none;
}

.TableOfContents-module__Xtt2xW__ul li a {
	color: var(--color-base);
}

.TableOfContents-module__Xtt2xW__ul li a span {
	color: inherit;
}

@media (any-hover: hover) {
	.TableOfContents-module__Xtt2xW__ul li a:hover {
		color: var(--color-hover);
	}
}

.TableOfContents-module__Xtt2xW__ul li.TableOfContents-module__Xtt2xW__active a {
	color: var(--color-active);
}

.TableOfContents-module__Xtt2xW__text {
	font-size: var(--font-size);
}

.Workflows-module__CsoIPa__root {
	justify-content: center;
	display: flex;
	position: relative;
}

.Workflows-module__CsoIPa__topRightFade::before {
	content: "";
	pointer-events: none;
	background: linear-gradient(90deg, transparent 0%, var(--color-bg-level-1) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Workflows-module__CsoIPa__topRightFade::after {
	content: "";
	pointer-events: none;
	background: linear-gradient(0deg, transparent 79.32%, var(--color-bg-level-1) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Workflows-module__CsoIPa__bottomRightFade::before {
	content: "";
	pointer-events: none;
	background: linear-gradient(0deg, var(--color-bg-level-1) 16.52%, transparent 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Workflows-module__CsoIPa__bottomRightFade::after {
	content: "";
	pointer-events: none;
	background: linear-gradient(90deg, transparent 0%, var(--color-bg-level-1) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Workflows-module__CsoIPa__bottomFade::before {
	content: "";
	pointer-events: none;
	background: linear-gradient(0deg, var(--color-bg-level-1) 0%, transparent 66.52%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.scope-module__e8E66G__wrapper {
	max-width: var(--prose-max-width);
	position: relative;
}

.scope-module__e8E66G__project {
	border: 1px dashed #4a4c50;
	border-radius: 50%;
	width: 48px;
	height: 48px;
	padding: 3px;
	overflow: hidden;
}

.scope-module__e8E66G__project.scope-module__e8E66G__scopedProject {
	border-style: solid;
}

.scope-module__e8E66G__scopedProjectInner {
	border-radius: 50%;
	justify-content: space-between;
	width: 100%;
	height: 100%;
	padding: 0 2px;
	display: flex;
	overflow: hidden;
	transform: rotate(-45deg);
}

.scope-module__e8E66G__projectsWrapper {
	flex-wrap: wrap;
	gap: 16px;
	display: flex;
}

@media (max-width: 640px) {
	.scope-module__e8E66G__projectsWrapper {
		gap: 8px;
	}
}

.scope-module__e8E66G__scopedProjectsWrapper {
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
}

.scope-module__e8E66G__bar {
	background: #2d2e2f;
	width: 1px;
	height: 100%;
}

.scope-module__e8E66G__draggable {
	border-top: 1px solid var(--color-bg-primary);
	background: var(--color-text-primary);
	width: calc(100% + 24px);
	height: 2px;
	position: absolute;
	left: -12px;
}

.DocsArticle-module__l2XJZa__root {
	isolation: isolate;
	flex-grow: 1;
	width: 100%;
	container: docs / inline-size;
}

.DocsArticle-module__l2XJZa__content {
	max-width: var(--page-max-width);
	padding-left: 48px;
	padding-right: 48px;
	align-items: flex-start;
	gap: 76px;
	margin-left: auto;
	margin-right: auto;
	padding-top: 112px;
	padding-bottom: 48px;
	display: flex;
}

@container docs (width <= 1024px) {
	.DocsArticle-module__l2XJZa__content {
		gap: 32px;
	}
}

@container docs (width <= 768px) {
	.DocsArticle-module__l2XJZa__content {
		padding-top: 112px;
		padding-bottom: 112px;
		padding-left: var(--page-padding-left);
		padding-right: var(--page-padding-right);
	}
}

.DocsArticle-module__l2XJZa__article {
	min-width: 0;
	max-width: 100%;
}

.DocsArticle-module__l2XJZa__toc {
	min-width: 250px;
	max-height: calc(100vh - var(--header-height) - 64px);
	height: max-content;
	padding-right: 8px;
	overflow-y: auto;
}

@container docs (width <= 768px) {
	.DocsArticle-module__l2XJZa__toc {
		display: none;
	}
}

@media (max-width: 1024px) {
	.DocsArticle-module__l2XJZa__toc {
		display: none;
	}
}

.Icon-module__Fu3-Vq__icon,
.Icon-module__Fu3-Vq__avatar {
	width: var(--size);
	height: var(--size);
	border-radius: 4px;
}

.page-module__x5b50W__root {
	--bento-border: var(--color-border-translucent);
	height: 100%;
}

.page-module__x5b50W__planningHeroImageWrapper {
	pointer-events: none;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	display: flex;
	position: relative;
}

.page-module__x5b50W__planningHeroImageWrapper::before {
	content: "";
	margin-top: -8%;
	display: block;
}

@media (max-width: 768px) {
	.page-module__x5b50W__planningHeroImageWrapper::before {
		margin-top: 0;
	}
}

.page-module__x5b50W__planningHeroImageWrapper::after {
	content: "";
	margin-bottom: -3%;
	display: block;
}

.page-module__x5b50W__planningHeroImage {
	display: block;
	-webkit-mask-image: radial-gradient(57% 57% at 50% 35%, #d9d9d9 0%, rgba(115, 115, 115, 0) 100%);
	mask-image: radial-gradient(57% 57% at 50% 35%, #d9d9d9 0%, rgba(115, 115, 115, 0) 100%);
}

.page-module__x5b50W__planningHeroImage.page-module__x5b50W__planningHeroImage {
	max-width: 1600px;
}

@media (max-width: 768px) {
	.page-module__x5b50W__planningHeroImage.page-module__x5b50W__planningHeroImage {
		max-width: none;
		max-width: initial;
		width: 150vw;
		margin-left: 10vw;
		-webkit-mask-image: radial-gradient(90% 50%, #d9d9d9 0%, rgba(115, 115, 115, 0) 100%);
		mask-image: radial-gradient(90% 50%, #d9d9d9 0%, rgba(115, 115, 115, 0) 100%);
	}
}

@media (max-width: 640px) {
	.page-module__x5b50W__planningHeroImage.page-module__x5b50W__planningHeroImage {
		max-width: none;
		max-width: initial;
		width: 250vw;
		margin-left: 40vw;
	}
}

.page-module__x5b50W__trackingHeroImageWrapper {
	pointer-events: none;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	display: flex;
	position: relative;
}

.page-module__x5b50W__trackingHeroImageWrapper::before {
	content: "";
	margin-top: -4%;
	display: block;
}

.page-module__x5b50W__trackingHeroImageWrapper::after {
	content: "";
	margin-bottom: -6%;
	display: block;
}

@media (max-width: 640px) {
	.page-module__x5b50W__trackingHeroImageWrapper::after {
		margin-bottom: -20%;
	}
}

.page-module__x5b50W__trackingHeroImage {
	display: block;
	-webkit-mask-image: radial-gradient(83.83% 83.84% at 50% 16.17%, #d9d9d9 0%, rgba(115, 115, 115, 0) 80%);
	mask-image: radial-gradient(83.83% 83.84% at 50% 16.17%, #d9d9d9 0%, rgba(115, 115, 115, 0) 80%);
}

.page-module__x5b50W__trackingHeroImage.page-module__x5b50W__trackingHeroImage {
	max-width: 1600px;
}

@media (max-width: 768px) {
	.page-module__x5b50W__trackingHeroImage.page-module__x5b50W__trackingHeroImage {
		max-width: none;
		max-width: initial;
		width: 150vw;
		margin-left: -20vw;
	}
}

@media (max-width: 640px) {
	.page-module__x5b50W__trackingHeroImage.page-module__x5b50W__trackingHeroImage {
		max-width: none;
		max-width: initial;
		width: 250vw;
		margin-left: 30vw;
	}
}

@keyframes page-module__x5b50W__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

.page-module__x5b50W__section {
	background: linear-gradient(to bottom, var(--color-bg-translucent), transparent 20%);
}

.page-module__x5b50W__sectionCustomers {
	padding-top: 64px;
	padding-bottom: 64px;
}

@keyframes page-module__x5b50W__heroImage {
	0% {
		filter: blur(10px);
		transform: translate(5%, 10%);
	}

	to {
		filter: none;
		transform: none;
	}
}

.page-module__x5b50W__sectionWhatMakesLinearDifferent {
	background: 0 0;
}

.page-module__x5b50W__sectionWhatMakesLinearDifferent,
.page-module__x5b50W__sectionPlanning,
.page-module__x5b50W__sectionTracking,
.page-module__x5b50W__sectionWorkflows,
.page-module__x5b50W__sectionUnderTheHood {
	isolation: isolate;
	padding: 160px 0;
}

@media (max-width: 640px) {
	.page-module__x5b50W__sectionWhatMakesLinearDifferent,
	.page-module__x5b50W__sectionPlanning,
	.page-module__x5b50W__sectionTracking,
	.page-module__x5b50W__sectionWorkflows,
	.page-module__x5b50W__sectionUnderTheHood {
		padding: 48px 0;
	}
}

.page-module__x5b50W__sectionPlanning,
.page-module__x5b50W__sectionTracking {
	overflow-x: hidden;
}

.page-module__x5b50W__sectionWorkflows {
	background: linear-gradient(to bottom, var(--color-bg-translucent), transparent 20%), linear-gradient(180deg, rgba(97, 106, 115, 0) 0%, rgba(97, 106, 115, .05) 40%, rgba(97, 106, 115, .05) 80%, rgba(97, 106, 115, 0) 100%);
}

.page-module__x5b50W__bentoGrid {
	border-top: 2px solid var(--bento-border);
	border-bottom: 2px solid var(--bento-border);
}

@media (max-width: 640px) {
	.page-module__x5b50W__bentoGrid {
		border-bottom: none;
	}
}

.page-module__x5b50W__bentoGridA,
.page-module__x5b50W__bentoGridB,
.page-module__x5b50W__bentoGridC,
.page-module__x5b50W__bentoGridD {
	padding-top: 56px;
	padding-bottom: 56px;
}

@media (max-width: 768px) {
	.page-module__x5b50W__bentoGridA,
	.page-module__x5b50W__bentoGridB,
	.page-module__x5b50W__bentoGridC,
	.page-module__x5b50W__bentoGridD {
		padding-top: 40px;
		padding-bottom: 40px;
	}
}

.page-module__x5b50W__bentoGridA {
	position: relative;
}

.page-module__x5b50W__bentoGridA:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-right: 48px;
}

.page-module__x5b50W__bentoGridA:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-right: 48px;
}

.page-module__x5b50W__bentoGridA:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-right: 48px;
}

.page-module__x5b50W__bentoGridA:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 48px;
}

.page-module__x5b50W__bentoGridA:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 48px;
}

.page-module__x5b50W__bentoGridA:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 48px;
}

.page-module__x5b50W__bentoGridA::after {
	--border-width: 2px;
	content: "";
	height: 100%;
	width: var(--border-width);
	background: var(--bento-border);
	transform: translatex(calc(var(--grid-gap) / 2 + var(--border-width) / 2));
	position: absolute;
	top: 0;
	bottom: 0;
	right: 0;
}

@media (max-width: 768px) {
	.page-module__x5b50W__bentoGridA::after {
		content: none;
	}

	.page-module__x5b50W__bentoGridA {
		border-bottom: 2px solid var(--bento-border);
	}

	.page-module__x5b50W__bentoGridA:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
		padding-right: 0;
	}

	.page-module__x5b50W__bentoGridA:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
		padding-right: 0;
	}

	.page-module__x5b50W__bentoGridA:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
		padding-right: 0;
	}

	.page-module__x5b50W__bentoGridA:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
		padding-left: 0;
	}

	.page-module__x5b50W__bentoGridA:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
		padding-left: 0;
	}

	.page-module__x5b50W__bentoGridA:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
		padding-left: 0;
	}
}

.page-module__x5b50W__bentoGridB:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 48px;
}

.page-module__x5b50W__bentoGridB:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 48px;
}

.page-module__x5b50W__bentoGridB:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 48px;
}

.page-module__x5b50W__bentoGridB:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-right: 48px;
}

.page-module__x5b50W__bentoGridB:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-right: 48px;
}

.page-module__x5b50W__bentoGridB:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-right: 48px;
}

@media (max-width: 768px) {
	.page-module__x5b50W__bentoGridB:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
		padding-left: 0;
	}

	.page-module__x5b50W__bentoGridB:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
		padding-left: 0;
	}

	.page-module__x5b50W__bentoGridB:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
		padding-left: 0;
	}

	.page-module__x5b50W__bentoGridB:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
		padding-right: 0;
	}

	.page-module__x5b50W__bentoGridB:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
		padding-right: 0;
	}

	.page-module__x5b50W__bentoGridB:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
		padding-right: 0;
	}
}

.page-module__x5b50W__sectionUnderTheHood {
	position: relative;
}

.page-module__x5b50W__underTheHoodAssetWrapper {
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	overflow: hidden;
}

@media (max-width: 768px) {
	.page-module__x5b50W__underTheHoodAssetWrapper {
		display: none;
	}
}

.page-module__x5b50W__underTheHoodAsset {
	top: 0;
	bottom: 0;
	margin-top: auto;
	margin-bottom: auto;
	display: block;
	position: absolute;
	left: 50%;
}

.page-module__x5b50W__insightsImageWrapper {
	pointer-events: none;
	grid-area: 1 / 1 / 1 / -1;
	position: relative;
	overflow: hidden;
}

.page-module__x5b50W__insightsImageWrapper::after {
	content: "";
	background: linear-gradient(to bottom, transparent 70%, var(--color-bg-primary) 100%), linear-gradient(to right, var(--color-bg-primary) 0%, transparent 20%, transparent 80%, var(--color-bg-primary) 100%), linear-gradient(150deg, var(--color-bg-primary) 20%, transparent 30%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__x5b50W__insightsImageWrapper > img:is(.page-module__x5b50W__insightsImageWrapper > img) {
	max-width: none;
	max-width: initial;
	width: 150%;
	height: auto;
	margin-bottom: -25%;
	margin-left: -15%;
}

@media (max-width: 768px) {
	.page-module__x5b50W__insightsImageWrapper {
		grid-row: auto;
	}

	.page-module__x5b50W__insightsImageWrapper > img:is(.page-module__x5b50W__insightsImageWrapper > img) {
		max-width: none;
		max-width: initial;
		width: 250%;
		height: auto;
		margin-left: -100%;
	}
}

.page-module__x5b50W__insightsCopy {
	z-index: 1;
	grid-area: 1 / 1 / 1 / span 6;
}

.page-module__x5b50W__workflowImage {
	margin-left: auto;
	margin-right: auto;
	display: block;
}

.page-module__x5b50W__customersLink {
	grid-template-columns: 1fr;
	place-items: center;
	display: grid;
	position: relative;
}

.page-module__x5b50W__customersLink > * {
	grid-area: 1 / 1;
}

.page-module__x5b50W__customersLink:hover .page-module__x5b50W__logos,
.page-module__x5b50W__customersLink:focus .page-module__x5b50W__logos {
	filter: blur(8px);
}

.page-module__x5b50W__customersLink:hover .page-module__x5b50W__customerLinkLabel,
.page-module__x5b50W__customersLink:focus .page-module__x5b50W__customerLinkLabel {
	opacity: 1;
	transform: none;
}

.page-module__x5b50W__customersLink:focus-visible .page-module__x5b50W__customerLinkLabel {
	outline: var(--focus-ring-outline);
	outline-offset: var(--focus-ring-offset);
}

.page-module__x5b50W__logos {
	transition: .2s var(--ease-out-quad);
	transition-property: filter;
}

.page-module__x5b50W__customerLinkLabel {
	border-radius: var(--radius-rounded);
	background: var(--color-bg-tertiary);
	border: 1px solid var(--color-border-tertiary);
	height: 32px;
	box-shadow: var(--shadow-medium);
	opacity: 0;
	justify-content: center;
	align-items: center;
	gap: 4px;
	padding: 0 8px 0 16px;
	transition: opacity .25s, transform .25s;
	display: inline-flex;
	position: relative;
	transform: scale(.95);
}

.page-module__x5b50W__udhSpecs {
	-moz-column-gap: 48px;
	gap: 40px 48px;
}

.page-module__x5b50W__chevronLink {
	color: var(--color-text-quaternary);
	transition: .2s var(--ease-out-quad);
}

a:hover .page-module__x5b50W__chevronLink {
	color: var(--color-text-primary);
	transform: translate(4px);
}

.page-module__x5b50W__badge {
	padding-top: 32px;
}

.page-module__x5b50W__maskRight {
	--mask-right: linear-gradient(to right, var(--mask-visible) 70%, var(--mask-invisible) 100%);
	-webkit-mask-image: var(--mask-right);
	-webkit-mask-image: var(--mask-right);
	mask-image: var(--mask-right);
}

@media (max-width: 1024px) {
	.page-module__x5b50W__delegationIllustration [data-dir] {
		display: none;
	}
}

.issues-not-stories-module__q66zrW__wrapper {
	grid-gap: 28px;
	grid-template-columns: repeat(5, 1fr);
	gap: 28px;
	display: grid;
}

@media (max-width: 640px) {
	.issues-not-stories-module__q66zrW__wrapper {
		gap: 16px;
	}
}

.issues-not-stories-module__q66zrW__circleWrapper {
	aspect-ratio: 1;
	background: 0 0;
	border: none;
	width: 100%;
	padding: 0;
	position: relative;
}

.issues-not-stories-module__q66zrW__dividedCircles {
	grid-template-columns: repeat(2, 1fr);
	width: 100%;
	height: 100%;
	display: grid;
}

.issues-not-stories-module__q66zrW__dividedCircles[data-level="2"] {
	gap: 16px;
}

@media (max-width: 640px) {
	.issues-not-stories-module__q66zrW__dividedCircles[data-level="2"] {
		gap: 4px;
	}
}

.issues-not-stories-module__q66zrW__dividedCircles[data-level="3"] {
	gap: 4px;
}

@media (max-width: 640px) {
	.issues-not-stories-module__q66zrW__dividedCircles[data-level="3"] {
		gap: 2px;
	}
}

.issues-not-stories-module__q66zrW__circle {
	aspect-ratio: 1;
	background: var(--bg-color-primary);
	border: 1px dashed var(--color-border-tertiary);
	cursor: pointer;
	border-radius: 100%;
	width: 100%;
	transition: color .2s;
	position: relative;
}

.issues-not-stories-module__q66zrW__circle[data-variant="secondary"],
.issues-not-stories-module__q66zrW__circle[data-variant="tertiary"] {
	border-style: solid;
}

.issues-not-stories-module__q66zrW__circle[data-variant="secondary"]::after,
.issues-not-stories-module__q66zrW__circle[data-variant="tertiary"]::after {
	content: "";
	background-image: repeating-linear-gradient(45deg, var(--color-border-tertiary) 0px, var(--color-border-tertiary) 1px, transparent 1px, transparent 5px);
	opacity: .6;
	border-radius: 100%;
	position: absolute;
	top: 3px;
	bottom: 3px;
	left: 3px;
	right: 3px;
}

.issues-not-stories-module__q66zrW__circle[data-variant="tertiary"] {
	border-color: var(--color-text-primary);
}

.issues-not-stories-module__q66zrW__circle:hover {
	background: rgba(255, 255, 255, .01);
}

.page-module__Rbvlqa__cardsGrid {
	display: grid;
}

.page-module__Rbvlqa__cardsGrid[data-size="large"] {
	grid-template-columns: 1fr 80px 1fr;
	gap: 64px 0;
}

@media (max-width: 768px) {
	.page-module__Rbvlqa__cardsGrid[data-size="large"] {
		grid-template-columns: 1fr;
	}
}

.page-module__Rbvlqa__cardsGrid[data-size="large"] .page-module__Rbvlqa__imageWrapper {
	height: 252px;
}

@media (max-width: 1024px) {
	.page-module__Rbvlqa__cardsGrid[data-size="large"] .page-module__Rbvlqa__imageWrapper {
		width: 100%;
		height: auto;
	}
}

@media (max-width: 768px) {
	.page-module__Rbvlqa__cardsGrid[data-size="large"] .page-module__Rbvlqa__imageWrapper {
		height: -moz-fit-content;
		height: fit-content;
	}

	.page-module__Rbvlqa__cardsGrid[data-size="large"] .page-module__Rbvlqa__imageWrapper img {
		width: 100%;
		height: 100%;
	}
}

.page-module__Rbvlqa__cardsGrid[data-size="small"] {
	grid-template-columns: repeat(calc(var(--columns) - 1), 1fr 80px) 1fr;
	gap: 32px 0;
}

@media (max-width: 1024px) {
	.page-module__Rbvlqa__cardsGrid[data-size="small"] {
		grid-template-columns: 1fr 80px 1fr;
	}

	.page-module__Rbvlqa__cardsGrid[data-size="small"] .page-module__Rbvlqa__imageWrapper {
		width: 100%;
		height: auto;
	}
}

@media (max-width: 768px) {
	.page-module__Rbvlqa__cardsGrid[data-size="small"] {
		grid-template-columns: 1fr;
	}

	.page-module__Rbvlqa__cardsGrid[data-size="small"] .page-module__Rbvlqa__imageWrapper {
		width: 100%;
		height: auto;
	}
}

.page-module__Rbvlqa__card {
	border-radius: 6px;
	position: relative;
}

@media (any-hover: hover) {
	.page-module__Rbvlqa__card:hover .page-module__Rbvlqa__arrow,
	.page-module__Rbvlqa__pressCard:hover .page-module__Rbvlqa__arrow {
		opacity: 1;
		transform: none;
	}
}

.page-module__Rbvlqa__description {
	max-width: 500px;
}

.page-module__Rbvlqa__description em {
	font-style: normal;
}

.page-module__Rbvlqa__description a {
	color: inherit;
	font-weight: inherit;
	text-decoration: none;
}

.page-module__Rbvlqa__arrow {
	transition: transform var(--speed-regularTransition), opacity var(--speed-regularTransition);
	transition-timing-function: var(--ease-out-quad);
	opacity: 0;
	margin-left: auto;
	transform: translate(-2px) scale(.98);
}

.page-module__Rbvlqa__meta {
	align-items: center;
	height: 20px;
	display: flex;
}

.page-module__Rbvlqa__imageWrapper {
	aspect-ratio: 16 / 9;
	border-radius: 5px;
	height: 153px;
	position: relative;
	overflow: hidden;
}

.page-module__Rbvlqa__imageWrapper::after {
	content: "";
	border: 1px solid var(--color-border-translucent);
	border-radius: inherit;
	pointer-events: none;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__Rbvlqa__imageWrapper div {
	height: 100%;
}

.page-module__Rbvlqa__cards {
	grid-gap: 32px;
	grid-template-columns: repeat(4, 1fr);
	gap: 32px;
	display: grid;
}

.page-module__Rbvlqa__link svg {
	color: var(--color-text-quaternary);
}

.page-module__Rbvlqa__link:hover svg {
	color: var(--color-text-secondary);
}

.page-module__Rbvlqa__cardIcon {
	border-radius: var(--radius-8);
	background: var(--color);
	border: 1px solid var(--color-border-translucent);
	width: 48px;
	height: 48px;
}

.page-module__Rbvlqa__cardIcon img {
	filter: invert();
}

.page-module__Rbvlqa__gridCard {
	border: 1px solid var(--color-border-translucent);
	background: var(--color-bg-level-2);
	height: 256px;
	transition: filter var(--speed-quickTransition);
	border-radius: 12px;
	flex-direction: column;
	padding: 24px;
	display: flex;
	overflow: hidden;
}

.page-module__Rbvlqa__gridCard:hover {
	filter: brightness(1.1);
}

[data-theme="light"] .page-module__Rbvlqa__gridCard:hover {
	filter: brightness(.98);
}

@media (max-width: 768px) {
	.page-module__Rbvlqa__openSearchButtonWrapper {
		display: none;
	}
}

.page-module__Rbvlqa__openSearchButtonWrapper .page-module__Rbvlqa__openSearchButton {
	color: var(--color-text-tertiary);
	--button-gap: 10px;
	background: var(--color-bg-level-2);
	border: 1px solid var(--color-border-primary);
	justify-content: flex-start;
	width: 232px;
	font-size: 14px;
	font-weight: 400;
}

[data-theme="light"] :is(.page-module__Rbvlqa__openSearchButtonWrapper .page-module__Rbvlqa__openSearchButton) {
	box-shadow: none;
	background: var(--color-bg-primary);
}

.page-module__Rbvlqa__openSearchButtonWrapper .page-module__Rbvlqa__openSearchButton kbd {
	color: var(--color-text-quaternary);
	background: 0 0;
	margin-top: -1px;
	margin-left: auto;
	font-size: 14px;
}

.page-module__Rbvlqa__changelogCard {
	height: 100%;
	padding: 0;
}

.page-module__Rbvlqa__changelogCardDescription {
	border-top: 1px solid var(--color-border-translucent);
	padding: 24px;
}

.page-module__Rbvlqa__categoryLink[data-active="true"] {
	color: var(--color-text-primary);
	font-weight: var(--font-weight-normal);
}

@media (any-hover: hover) {
	.page-module__Rbvlqa__categoryLink:hover {
		color: var(--color-text-primary);
	}
}

@media (max-width: 768px) {
	.page-module__Rbvlqa__categoryLinks {
		margin-inline: calc(var(--page-padding-right) * -1);
		padding-inline: var(--page-padding-right);
		-webkit-mask-image: linear-gradient(to right, transparent, black var(--page-padding-left), black calc(100% - var(--page-padding-right)), transparent);
		-webkit-mask-image: linear-gradient(to right, transparent, black var(--page-padding-left), black calc(100% - var(--page-padding-right)), transparent);
		mask-image: linear-gradient(to right, transparent, black var(--page-padding-left), black calc(100% - var(--page-padding-right)), transparent);
		overflow-x: auto;
	}
}

.page-module__Rbvlqa__pressImageWrapper {
	display: flex;
	position: relative;
}

.page-module__Rbvlqa__pressImageWrapper::after {
	content: "";
	border: 1px solid var(--color-border-translucent);
	pointer-events: none;
	border-radius: 5px;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.page-module__Rbvlqa__copyButton span {
	transition: color var(--speed-regularTransition);
	font-size: 15px;
	font-weight: 400;
}

@media (any-hover: hover) {
	.page-module__Rbvlqa__copyButton:hover span {
		color: var(--color-text-primary);
	}
}

.CopyPageButton-module__hAfYWq__trigger {
	aspect-ratio: 1;
	border: none;
	border-left: 1px solid var(--color-border-translucent);
	background: 0 0;
	background: var(--color-bg-primary);
	cursor: pointer;
	height: 100%;
	color: var(--color-text-tertiary);
	border-top-right-radius: var(--button-corner-radius);
	border-bottom-right-radius: var(--button-corner-radius);
	place-items: center;
	padding: 0;
	transition: inherit;
	display: grid;
	position: relative;
}

.CopyPageButton-module__hAfYWq__trigger::before {
	content: "";
	position: absolute;
	top: -1px;
	bottom: -1px;
	left: -1px;
	right: -1px;
}

.CopyPageButton-module__hAfYWq__trigger:hover,
.CopyPageButton-module__hAfYWq__trigger[data-state="open"] {
	background: var(--color-bg-tertiary);
	border-color: var(--color-bg-tertiary);
	color: var(--color-text-primary);
}

.CopyPageButton-module__hAfYWq__button {
	border: 1px solid var(--color-border-translucent);
	will-change: transform;
	padding-left: 0 !important;
	padding-right: 0 !important;
}

.CopyPageButton-module__hAfYWq__button:active {
	transform: scale(1) !important;
}

.CopyPageButton-module__hAfYWq__button:has(.CopyPageButton-module__hAfYWq__trigger:hover) {
	color: var(--color-text-tertiary);
	background: var(--color-bg-primary);
}

.CopyPageButton-module__hAfYWq__button:has(.CopyPageButton-module__hAfYWq__trigger[data-state="open"]) {
	color: var(--color-text-tertiary);
	background: var(--color-bg-primary);
}

.CopyPageButton-module__hAfYWq__copyButton {
	height: 100%;
	padding: var(--button-padding);
	align-items: center;
	gap: var(--button-gap);
	border-radius: var(--button-corner-radius) 0 0 var(--button-corner-radius);
	color: inherit;
	cursor: pointer;
	font-weight: inherit;
	font-size: inherit;
	background: 0 0;
	border: none;
	display: flex;
}

.CopyPageButton-module__hAfYWq__copyButton:focus-visible {
	z-index: 1;
}

.Card-module__NIWv0q__card {
	background: var(--color-bg-level-1);
	border: 1px solid var(--color-border-translucent);
	height: var(--card-height, 168px);
	outline-offset: -2px;
	border-radius: 12px;
	flex-direction: column;
	padding: 20px;
	transition: background 80ms, border-color 80ms;
	display: flex;
}

@media (any-hover: hover) {
	.Card-module__NIWv0q__card:hover {
		background: var(--color-bg-level-2);
	}
}

.Card-module__NIWv0q__name {
	font-weight: var(--font-weight-medium);
	letter-spacing: -.016em;
	color: var(--color-text-primary);
	text-overflow: ellipsis;
	white-space: nowrap;
	margin-left: 12px;
	font-size: 16px;
	line-height: 1.5;
	display: block;
	overflow: hidden;
}

.Card-module__NIWv0q__description {
	color: var(--color-text-tertiary);
	-webkit-line-clamp: 2;
	-webkit-box-orient: vertical;
	margin-top: auto;
	font-size: 14px;
	line-height: 1.7;
	display: -webkit-box;
	overflow: hidden;
}

.Card-module__NIWv0q__requestButton {
	cursor: pointer;
}

.Card-module__NIWv0q__requestButton svg {
	fill: currentColor;
}

.VideoDialog-module__Errw0G__videoOverlay {
	position: absolute;
	top: 24px;
	bottom: auto;
	left: auto;
	right: 32px;
}

@media (max-width: 640px) {
	.VideoDialog-module__Errw0G__videoOverlay {
		top: 16px;
		bottom: auto;
		left: auto;
		right: 12px;
	}
}

.ChangelogList-module__yvG4Cq__contentWrapper h2:first-of-type {
	display: none;
}

.ChangelogList-module__yvG4Cq__dateBar {
	background: var(--color-border-primary);
	opacity: .6;
	width: 1px;
	height: 100%;
	margin-top: 9px;
	margin-left: 9px;
	position: absolute;
}

@media (max-width: 640px) {
	.ChangelogList-module__yvG4Cq__dateBar {
		display: none;
	}
}

.ChangelogList-module__yvG4Cq__changelogLeft {
	height: -moz-fit-content;
	height: fit-content;
	top: calc(var(--header-height) + 24px);
	padding-left: 24px;
	position: -webkit-sticky;
	position: sticky;
}

@media (max-width: 640px) {
	.ChangelogList-module__yvG4Cq__changelogLeft {
		opacity: .75;
		padding-left: 0;
		position: relative;
		top: 20px;
	}
}

.ChangelogList-module__yvG4Cq__changelogLeft::after {
	content: "";
	background: var(--color-border-tertiary);
	border-radius: 100%;
	width: 6px;
	height: 6px;
	position: absolute;
	top: 50%;
	left: 9px;
	transform: translate(-35%) translatey(-50%);
}

@media (max-width: 640px) {
	.ChangelogList-module__yvG4Cq__changelogLeft::after {
		display: none;
	}
}

.ChangelogList-module__yvG4Cq__changelogLeft[data-index="0"]::after {
	background: var(--color-orange);
}

.ChangelogList-module__yvG4Cq__changelogEntry:last-of-type .ChangelogList-module__yvG4Cq__changelogLeft {
	position: relative;
	top: 0;
}

.ChangelogList-module__yvG4Cq__changelogEntry:last-of-type .ChangelogList-module__yvG4Cq__dateBar {
	display: none;
}

.HeroIllustration-module__LcHIQG__root {
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	--Sidebar-width: 260px;
	width: 100%;
	height: 900px;
}

@media (max-width: 640px) {
	.HeroIllustration-module__LcHIQG__root {
		height: 600px;
	}
}

.HeroIllustration-module__LcHIQG__perspective {
	contain: strict;
	perspective: 4000px;
	perspective-origin: 100% 0;
	width: 100%;
	height: 100%;
	transform-style: preserve-3d;
	position: relative;
}

.HeroIllustration-module__LcHIQG__threeD {
	transform-style: preserve-3d;
}

.HeroIllustration-module__LcHIQG__base {
	background: var(--color-bg-primary);
	transform-origin: 0 0;
	-webkit-backface-visibility: hidden;
	backface-visibility: hidden;
	border: 1px solid #1e1e1e;
	border-radius: 10px;
	width: 1600px;
	height: 900px;
	margin: 280px auto auto;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	transform: translate(2%) scale(1.2) rotatex(47deg) rotatey(31deg) rotate(324deg);
}

@media (max-width: 640px) {
	.HeroIllustration-module__LcHIQG__base {
		margin-top: 100px;
		margin-left: 1%;
		transform: scale(.7) rotatex(47deg) rotatey(21deg) rotate(330deg);
	}
}

.HeroIllustration-module__LcHIQG__sidebar {
	width: var(--Sidebar-width);
	padding: 16px 14px;
}

.HeroIllustration-module__LcHIQG__trafficLights {
	justify-content: center;
	align-items: center;
	gap: 8px;
	display: flex;
}

.HeroIllustration-module__LcHIQG__trafficLights > div {
	background: var(--color-bg-tertiary);
	background: #262626;
	border-radius: 50%;
	width: 12px;
	height: 12px;
}

.HeroIllustration-module__LcHIQG__animateIn {
	display: flex;
}

.HeroIllustration-module__LcHIQG__inbox {
	left: var(--Sidebar-width);
	height: 100%;
	position: absolute;
	top: 8px;
	bottom: 8px;
}

.HeroIllustration-module__LcHIQG__inbox::after {
	content: "";
	pointer-events: none;
	background: linear-gradient(to right, transparent 80%, var(--color-bg-primary) 90%);
	position: absolute;
	top: -8px;
	bottom: -8px;
	left: -8px;
	right: -8px;
}

.users-module__4Q1Dgq__grid {
	grid-gap: 16px;
	grid-template-columns: repeat(10, 1fr);
	gap: 16px;
	display: grid;
}

@media (max-width: 640px) {
	.users-module__4Q1Dgq__grid {
		grid-template-columns: repeat(7, 1fr);
		gap: 12px;
	}
}

.users-module__4Q1Dgq__circle {
	aspect-ratio: 1;
	border: 1px dashed var(--color-border-tertiary);
	cursor: pointer;
	background: 0 0;
	border-radius: 50%;
	height: 48px;
	padding: 0;
}

.users-module__4Q1Dgq__circle:last-of-type {
	display: none;
}

@media (max-width: 640px) {
	.users-module__4Q1Dgq__circle:last-of-type {
		display: block;
	}

	.users-module__4Q1Dgq__circle {
		height: 100%;
	}
}

.users-module__4Q1Dgq__circle:hover {
	background: rgba(255, 255, 255, .02);
}

.ArticlePage-module__Jm_B5G__asset {
	pointer-events: none;
	max-width: calc(var(--page-max-width) * .7);
	justify-content: center;
	align-items: center;
	margin: 48px auto;
	display: flex;
}

.ArticlePage-module__Jm_B5G__asset[data-wide="true"] {
	max-width: calc(var(--page-max-width) - var(--page-padding-left) - var(--page-padding-right));
}

@media (max-width: 640px) {
	.ArticlePage-module__Jm_B5G__asset {
		margin: 32px auto 24px;
	}
}

.ArticlePage-module__Jm_B5G__description {
	font-style: italic;
}

.ArticlePage-module__Jm_B5G__copyButton span {
	transition: color var(--speed-regularTransition);
	font-size: 15px;
	font-weight: 400;
}

@media (any-hover: hover) {
	.ArticlePage-module__Jm_B5G__copyButton:hover span {
		color: var(--color-text-primary);
	}
}

.DocsBreadcrumbs-module___z8VDW__header {
	z-index: var(--layer-header);
	padding-inline: 24px calc(16px + var(--removed-body-scroll-bar-size, 0px));
	background: var(--color-bg-primary);
	border-bottom: 1px solid var(--color-border-primary);
	grid-column: 1 / -1;
	align-items: center;
	gap: 8px;
	min-height: 64px;
	display: flex;
	position: fixed;
	top: 0;
	left: 280px;
	right: 0;
}

.List-module__jlQkFW__listWrapper {
	margin-top: 10px;
	position: relative;
}

.List-module__jlQkFW__list {
	grid-gap: 32px;
	grid-template-columns: repeat(auto-fill, minmax(296px, 1fr));
	list-style-type: none;
	display: grid;
	position: relative;
}

@media (max-width: 640px) {
	.List-module__jlQkFW__list {
		grid-gap: initial;
		margin-top: 0;
		margin-left: calc(-1 * var(--page-padding-left));
		margin-right: calc(-1 * var(--page-padding-right));
		padding-left: calc(1 * var(--page-padding-left));
		flex-direction: column;
		padding-bottom: 8px;
		display: flex;
	}

	.List-module__jlQkFW__list > li + li {
		margin-top: 16px;
	}

	.List-module__jlQkFW__list > li > * {
		max-width: calc(100vw - var(--page-padding-left) - var(--page-padding-right));
	}
}

.List-module__jlQkFW__list li {
	margin: 0;
	padding: 0;
}

.List-module__jlQkFW__showMore {
	margin-top: 24px;
	margin-bottom: -16px;
	padding-left: 20px;
}

@media (max-width: 640px) {
	.List-module__jlQkFW__showMore {
		margin-top: 16px;
		margin-bottom: -6px;
	}
}

.List-module__jlQkFW__categoryHeader {
	padding-left: 20px;
	padding-right: 20px;
}

@media (max-width: 640px) {
	.List-module__jlQkFW__categoryHeader {
		padding-left: 0;
		padding-right: 0;
	}
}

.WorkflowCard-module__yM1mQa__card {
	text-align: left;
	isolation: isolate;
	padding: 32px var(--page-padding-inline);
	background: var(--color-bg-level-1);
	transition: filter .2s ease-out, transform .16s var(--ease-out-quad);
	border-radius: 16px;
	flex-direction: column;
	justify-content: flex-end;
	display: flex;
	position: relative;
	overflow: hidden;
}

.WorkflowCard-module__yM1mQa__card.WorkflowCard-module__yM1mQa__passive {
	cursor: default;
}

.WorkflowCard-module__yM1mQa__card::after {
	content: "";
	pointer-events: none;
	border: 1px solid var(--color-border-translucent);
	border-radius: inherit;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.WorkflowCard-module__yM1mQa__card [type="button"] {
	background: 0 0;
}

@media (any-hover: hover) {
	.WorkflowCard-module__yM1mQa__card:hover:not(.WorkflowCard-module__yM1mQa__passive) {
		filter: brightness(110%);
	}

	.WorkflowCard-module__yM1mQa__card:hover:not(.WorkflowCard-module__yM1mQa__passive) .WorkflowCard-module__yM1mQa__iconButton {
		color: var(--color-text-primary);
		border-color: var(--color-bg-tertiary);
		background: var(--color-bg-tertiary);
	}

	.WorkflowCard-module__yM1mQa__card:active {
		transform: scale(.99);
	}
}

@media (max-width: 768px) {
	.WorkflowCard-module__yM1mQa__card {
		padding: 24px;
	}
}

.WorkflowCard-module__yM1mQa__drawer {
	max-width: 960px;
	z-index: var(--layer-dialog);
	contain: strict;
	isolation: isolate;
	background: #08090a;
	border-radius: 30px 30px 0 0;
	outline: none;
	margin-left: auto;
	margin-right: auto;
	position: fixed;
	top: 5vh;
	bottom: 0;
	left: 0;
	right: 0;
}

.WorkflowCard-module__yM1mQa__scrollable {
	padding-left: var(--page-padding-left);
	padding-right: var(--page-padding-right);
}

.WorkflowCard-module__yM1mQa__close {
	z-index: 1;
	margin-left: auto;
	display: flex;
	position: fixed;
	top: 24px;
	right: 24px;
}

.WorkflowCard-module__yM1mQa__overlay {
	background: var(--color-overlay-primary);
	-webkit-backdrop-filter: blur(24px);
	backdrop-filter: blur(24px);
	z-index: var(--layer-dialog-overlay);
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.WorkflowCard-module__yM1mQa__image {
	z-index: -1;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

@keyframes WorkflowCard-module__yM1mQa__dialogIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes WorkflowCard-module__yM1mQa__dialogOut {
	0% {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}

.WorkflowCard-module__yM1mQa__bottomSpacer {
	min-height: 192px;
}

.WorkflowCard-module__yM1mQa__left {
	max-width: 360px;
	position: relative;
}

@media (max-width: 768px) {
	.WorkflowCard-module__yM1mQa__left {
		max-width: none;
		max-width: initial;
	}
}

.WorkflowCard-module__yM1mQa__yellowStroke {
	offset-path: path("M-1.9 233c22.33-5.895 35.252-14.147 57.582-19.255 22.33-5.109 44.66-9.432 66.991-9.432h133.982c22.33 0 44.66-17.29 66.99-23.578 22.331-6.288 44.661-8.252 66.991-14.147 22.331-5.895 44.661-13.361 66.991-21.22 22.331-7.86 44.661-21.221 66.991-25.937 22.33-4.715 44.661-5.501 66.991-7.073A953.674 953.674 0 01661 110");
	background: #f2be01;
	border-radius: 50%;
	width: 12px;
	height: 12px;
	position: absolute;
}

.WorkflowCard-module__yM1mQa__greyStroke {
	offset-path: path("M.5 184c22.343-6.4 35.272-14 57.614-20 22.343-6 44.686-14.4 67.029-14.4h67.029c22.343 0 44.685-.8 67.028-2.4 22.343-1.6 44.686-10.8 67.029-16.8 22.343-6 44.686-11.6 67.028-19.2 22.343-7.6 44.686-18.4 67.029-26.4 22.343-8 44.686-16 67.029-21.6 22.342-5.6 44.685-12 67.028-12h67.029");
	z-index: 1;
	background: #393a3b;
	border-radius: 50%;
	width: 12px;
	height: 12px;
	position: absolute;
}

.WorkflowCard-module__yM1mQa__svgWrapper {
	margin-top: 32px;
	margin-left: 128px;
	position: relative;
}

@media (max-width: 1024px) {
	.WorkflowCard-module__yM1mQa__svgWrapper {
		transform: scale(.8);
	}
}

.WorkflowCard-module__yM1mQa__svgWrapper::after {
	content: "";
	background: linear-gradient(to right, var(--color-bg-level-1) 0%, var(--color-bg-level-1) 4%, transparent 164px), linear-gradient(to top, var(--color-bg-level-1) 0%, transparent 70%);
	z-index: 10;
	position: absolute;
	top: 0;
	bottom: 0;
	left: -12px;
	right: 0;
}

.WorkflowCard-module__yM1mQa__planningCard {
	min-height: 336px;
}

@media (max-width: 768px) {
	.WorkflowCard-module__yM1mQa__planningCard {
		min-height: 240px;
	}

	.WorkflowCard-module__yM1mQa__planningCard,
	.WorkflowCard-module__yM1mQa__buildCard {
		width: 100%;
		height: 103vw;
	}
}

.WorkflowCard-module__yM1mQa__planFade::after {
	content: "";
	background: linear-gradient(90deg, var(--color-bg-level-1) 0%, transparent 30%), linear-gradient(90deg, transparent 70%, var(--color-bg-level-1) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

@media (max-width: 768px) {
	.WorkflowCard-module__yM1mQa__buildFade::after {
		content: "";
		background: linear-gradient(90deg, var(--color-bg-level-1) 0%, transparent 50%);
		position: absolute;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
	}
}

.CategoryPage-module__PyL83q__cards {
	grid-gap: 24px;
	grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
	gap: 24px;
	display: grid;
}

.CategoryPage-module__PyL83q__card {
	border-radius: var(--radius-12);
	border: 1px solid var(--color-border-translucent);
	background: var(--color-bg-translucent);
	transition: var(--speed-regularTransition);
	flex-direction: column;
	transition-property: background-color, border-color;
	display: flex;
	overflow: hidden;
}

@media (any-hover: hover) {
	.CategoryPage-module__PyL83q__card:hover {
		background-color: var(--color-bg-secondary);
		--border: var(--color-border-secondary);
	}
}

.CategoryPage-module__PyL83q__cardBody {
	border-top: 1px solid var(--color-border-translucent);
	flex-direction: column;
	flex-grow: 1;
	padding: 24px;
	display: flex;
}

.CategoryPage-module__PyL83q__cardAsset {
	justify-content: center;
	align-items: center;
	width: 100%;
	height: 240px;
	display: flex;
	overflow: hidden;
}

.CategoryPage-module__PyL83q__cardImage.CategoryPage-module__PyL83q__cardImage {
	width: auto;
	height: 35%;
}

.CategoryPage-module__PyL83q__cardButton.CategoryPage-module__PyL83q__cardButton {
	border-color: var(--color-border-primary);
	color: var(--color-text-tertiary);
	background: 0 0;
}

@media (any-hover: hover) {
	.CategoryPage-module__PyL83q__card:hover .CategoryPage-module__PyL83q__cardButton.CategoryPage-module__PyL83q__cardButton {
		color: var(--color-text-primary);
		border-color: var(--color-bg-tertiary);
		background: var(--color-bg-tertiary);
	}
}

.CategoryPage-module__PyL83q__row {
	isolation: isolate;
	align-items: center;
	min-height: 56px;
	display: flex;
	position: relative;
}

.CategoryPage-module__PyL83q__row::before {
	content: "";
	pointer-events: none;
	inset: -1px calc(-1 * var(--page-padding-inline));
	background: var(--color-bg-translucent);
	opacity: 0;
	z-index: -1;
	transition: opacity var(--speed-quickTransition);
	border-radius: 12px;
	position: absolute;
}

.CategoryPage-module__PyL83q__row + .CategoryPage-module__PyL83q__row {
	border-top: 1px solid var(--color-bg-translucent);
}

@media (any-hover: hover) {
	.CategoryPage-module__PyL83q__row:hover::before {
		opacity: 1;
	}

	.CategoryPage-module__PyL83q__row:hover,
	.CategoryPage-module__PyL83q__row:hover + .CategoryPage-module__PyL83q__row {
		border-color: transparent;
	}
}

.CategoryPage-module__PyL83q__symbol {
	justify-content: center;
	align-items: center;
	width: 32px;
	height: 32px;
	margin-left: -6px;
	display: flex;
}

.CategoryPage-module__PyL83q__symbol > img {
	transition: filter var(--speed-quickTransition);
	filter: brightness(50%);
}

@media (any-hover: hover) {
	.CategoryPage-module__PyL83q__row:hover .CategoryPage-module__PyL83q__symbol > img {
		filter: brightness();
	}
}

.manage-design-projects-module__XD1sQW__grid {
	grid-gap: 16px;
	--cell-size: 48px;
	grid-template-columns: repeat(10, 1fr);
	gap: 16px;
	display: grid;
}

@media (max-width: 640px) {
	.manage-design-projects-module__XD1sQW__grid {
		--cell-size: 44px;
		gap: 12px;
		position: absolute;
		left: 50%;
		transform: translate(-50%);
	}
}

.manage-design-projects-module__XD1sQW__wrapper {
	height: 240px;
	position: relative;
}

@media (max-width: 640px) {
	.manage-design-projects-module__XD1sQW__wrapper {
		-webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 5%, #000 95%, transparent 100%);
		mask-image: linear-gradient(90deg, transparent 0%, #000 5%, #000 95%, transparent 100%);
	}
}

.manage-design-projects-module__XD1sQW__circle {
	height: var(--cell-size);
	aspect-ratio: 1;
	border: 1px dashed var(--color-border-tertiary);
	opacity: .75;
	border-radius: 50%;
}

.manage-design-projects-module__XD1sQW__shape {
	width: 100%;
	height: 100%;
	position: absolute;
}

.manage-design-projects-module__XD1sQW__rectangle {
	border: 1px solid var(--color-border-secondary);
	--stripes-radius: 8px;
	border-radius: 12px;
}

.manage-design-projects-module__XD1sQW__circleShape {
	border: 1px solid var(--color-border-secondary);
	--stripes-radius: 9999px;
	border-radius: 50%;
}

.manage-design-projects-module__XD1sQW__smallCircles,
.manage-design-projects-module__XD1sQW__smallRectangles {
	grid-gap: 4px;
	grid-template-columns: repeat(2, 1fr);
	gap: 4px;
	display: grid;
}

.manage-design-projects-module__XD1sQW__smallRectangle {
	border: 1px solid var(--color-border-secondary);
	--stripes-radius: 8px;
	border-radius: 8px;
	width: 100%;
	position: relative;
}

.manage-design-projects-module__XD1sQW__smallRectangle .manage-design-projects-module__XD1sQW__stripes {
	background-image: repeating-linear-gradient(45deg, var(--color-border-tertiary) 0px, var(--color-border-tertiary) 1px, transparent 1px, transparent 5px);
}

.manage-design-projects-module__XD1sQW__smallCircle {
	border: 1px solid var(--color-border-secondary);
	--stripes-radius: 9999px;
	border-radius: 50%;
	width: 100%;
	position: relative;
}

.manage-design-projects-module__XD1sQW__smallCircle .manage-design-projects-module__XD1sQW__stripes {
	background-image: repeating-linear-gradient(45deg, var(--color-border-tertiary) 0px, var(--color-border-tertiary) 1px, transparent 1px, transparent 5px);
}

.manage-design-projects-module__XD1sQW__semiCircle {
	border: 1px solid var(--color-border-secondary);
	--stripes-radius: 24px 24px 2px 2px;
	border-radius: 24px 24px 4px 4px;
}

.manage-design-projects-module__XD1sQW__semiCircle.manage-design-projects-module__XD1sQW__semiCircleRotated {
	transform: rotate(180deg);
}

.manage-design-projects-module__XD1sQW__halfCircle {
	border: 1px solid var(--color-border-secondary);
	width: 50%;
	height: 100%;
	display: inline-block;
	position: relative;
}

.manage-design-projects-module__XD1sQW__halfCircle.manage-design-projects-module__XD1sQW__halfCircleRight,
.manage-design-projects-module__XD1sQW__halfCircle.manage-design-projects-module__XD1sQW__halfCircleInwards:first-of-type {
	--stripes-radius: 0 24px 24px 0;
	border-radius: 0 24px 24px 0;
}

.manage-design-projects-module__XD1sQW__halfCircle.manage-design-projects-module__XD1sQW__halfCircleInwards:last-of-type {
	--stripes-radius: 24px 0 0 24px;
	border-radius: 24px 0 0 24px;
}

.manage-design-projects-module__XD1sQW__halfCircle .manage-design-projects-module__XD1sQW__stripes {
	top: 3px;
	left: 3px;
}

.manage-design-projects-module__XD1sQW__stripes {
	background-image: repeating-linear-gradient(45deg, var(--color-border-tertiary) 0px, var(--color-border-tertiary) 1px, transparent 1px, transparent 6px);
	border-radius: var(--stripes-radius);
	opacity: .6;
	position: absolute;
	top: 4px;
	bottom: 4px;
	left: 4px;
	right: 4px;
}

.manage-design-projects-module__XD1sQW__shapeWrapper {
	width: var(--cell-size);
	height: var(--cell-size);
	cursor: pointer;
	background: 0 0;
	border: none;
	border-radius: 6px;
	margin: 0 auto;
	padding: 0;
	transition: filter .2s;
	position: relative;
}

.manage-design-projects-module__XD1sQW__shapeWrapper:hover {
	filter: brightness(200%);
}

.manage-design-projects-module__XD1sQW__shapeWrapper > div {
	width: 100%;
	height: 100%;
}

.CommandMenu-module__cRGR4q__dialog {
	--transition-duration: .1s;
	--input-height: 62px;
	background: var(--color-bg-level-1);
	border: 1px solid var(--color-border-translucent);
	width: 100%;
	max-width: 600px;
	max-height: min(73vh, 500px);
	z-index: var(--layer-dialog);
	animation: CommandMenu-module__cRGR4q__scaleIn .175s var(--ease-out-quad);
	border-radius: 8px;
	position: fixed;
	top: 15%;
	left: 50%;
	transform: translate(-50%);
}

.CommandMenu-module__cRGR4q__dialog[data-state="closed"] {
	animation: CommandMenu-module__cRGR4q__scaleOut .175s var(--ease-out-quad);
}

.CommandMenu-module__cRGR4q__dialog[data-bounce="true"] {
	animation: .15s CommandMenu-module__cRGR4q__dialogBounce;
}

.CommandMenu-module__cRGR4q__combobox {
	max-height: min(450px, calc(var(--height, 9999px) + var(--input-height)));
	flex-direction: column;
	transition: max-height 80ms;
	display: flex;
}

.CommandMenu-module__cRGR4q__groupHeading {
	height: 30px;
	color: var(--color-text-tertiary);
	align-items: center;
	padding-left: 14px;
	padding-right: 14px;
	font-size: 12px;
	display: flex;
}

.CommandMenu-module__cRGR4q__overlay {
	background: var(--color-overlay-primary);
	z-index: var(--layer-dialog-overlay);
	animation: CommandMenu-module__cRGR4q__fadeIn .175s var(--ease-out-quad);
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.CommandMenu-module__cRGR4q__overlay[data-state="closed"] {
	animation: CommandMenu-module__cRGR4q__fadeOut .175s var(--ease-out-quad);
}

.CommandMenu-module__cRGR4q__input {
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	font-size: inherit;
	height: 62px;
	color: var(--color-text-primary);
	border: none;
	border-bottom: 1px solid var(--color-border-translucent);
	background: 0 0;
	width: 100%;
	margin: 0;
	padding: 20px;
	font-size: 18px;
}

.CommandMenu-module__cRGR4q__input:focus-visible {
	outline: none;
}

.CommandMenu-module__cRGR4q__empty {
	color: var(--color-text-tertiary);
	justify-content: center;
	align-items: center;
	gap: 4px;
	height: 100%;
	margin: 0;
	padding-top: 20px;
	padding-bottom: 20px;
	font-size: 14px;
	display: flex;
}

.CommandMenu-module__cRGR4q__detail mark {
	font-weight: var(--font-weight-semibold);
	color: var(--color-text-primary);
	background: 0 0;
}

.CommandMenu-module__cRGR4q__list {
	margin: 0;
	padding: 0;
	list-style-type: none;
	overflow-y: auto;
}

.CommandMenu-module__cRGR4q__item {
	align-items: center;
	gap: 12px;
	min-height: 46px;
	padding: 12px 20px;
	font-size: 14px;
	display: flex;
}

.CommandMenu-module__cRGR4q__item,
.CommandMenu-module__cRGR4q__hit {
	cursor: pointer;
	min-height: 48px;
	margin: 0;
	scroll-margin-block: 4px;
	position: relative;
}

.CommandMenu-module__cRGR4q__item .CommandMenu-module__cRGR4q__icon,
.CommandMenu-module__cRGR4q__hit .CommandMenu-module__cRGR4q__icon {
	flex-shrink: 0;
	place-items: center;
	width: 16px;
	height: 16px;
	display: grid;
}

.CommandMenu-module__cRGR4q__item .CommandMenu-module__cRGR4q__icon.CommandMenu-module__cRGR4q__iconWithDetail,
.CommandMenu-module__cRGR4q__hit .CommandMenu-module__cRGR4q__icon.CommandMenu-module__cRGR4q__iconWithDetail {
	width: 32px;
	height: 32px;
}

.CommandMenu-module__cRGR4q__item .CommandMenu-module__cRGR4q__icon svg,
.CommandMenu-module__cRGR4q__hit .CommandMenu-module__cRGR4q__icon svg {
	width: 16px;
	height: 16px;
}

.CommandMenu-module__cRGR4q__item .CommandMenu-module__cRGR4q__icon svg:not(.CommandMenu-module__cRGR4q__iconStroke),
.CommandMenu-module__cRGR4q__hit .CommandMenu-module__cRGR4q__icon svg:not(.CommandMenu-module__cRGR4q__iconStroke) {
	fill: var(--color-text-tertiary);
}

.CommandMenu-module__cRGR4q__item .CommandMenu-module__cRGR4q__icon svg.CommandMenu-module__cRGR4q__iconStroke,
.CommandMenu-module__cRGR4q__hit .CommandMenu-module__cRGR4q__icon svg.CommandMenu-module__cRGR4q__iconStroke {
	stroke: var(--color-text-tertiary);
}

.CommandMenu-module__cRGR4q__item kbd,
.CommandMenu-module__cRGR4q__hit kbd {
	align-items: center;
	display: flex;
	transform: translate(5px);
}

.CommandMenu-module__cRGR4q__item kbd span,
.CommandMenu-module__cRGR4q__hit kbd span {
	width: 20px;
	height: 20px;
	font-size: 13px;
}

.CommandMenu-module__cRGR4q__item[aria-selected="true"] .CommandMenu-module__cRGR4q__icon svg:not(.CommandMenu-module__cRGR4q__iconStroke),
.CommandMenu-module__cRGR4q__hit[aria-selected="true"] .CommandMenu-module__cRGR4q__icon svg:not(.CommandMenu-module__cRGR4q__iconStroke) {
	fill: var(--color-text-primary);
	--icon-color: var(--color-text-primary) !important;
}

.CommandMenu-module__cRGR4q__item[aria-selected="true"] .CommandMenu-module__cRGR4q__icon svg.CommandMenu-module__cRGR4q__iconStroke,
.CommandMenu-module__cRGR4q__hit[aria-selected="true"] .CommandMenu-module__cRGR4q__icon svg.CommandMenu-module__cRGR4q__iconStroke {
	stroke: var(--color-text-primary);
}

.CommandMenu-module__cRGR4q__item[aria-selected="true"] img,
.CommandMenu-module__cRGR4q__hit[aria-selected="true"] img {
	filter: brightness();
	opacity: 1;
}

.CommandMenu-module__cRGR4q__item[aria-selected="true"]::after,
.CommandMenu-module__cRGR4q__hit[aria-selected="true"]::after {
	content: "";
	background: var(--color-bg-level-3);
	z-index: -1;
	border-radius: 6px;
	position: absolute;
	top: 2px;
	bottom: 2px;
	left: 6px;
	right: 6px;
}

.CommandMenu-module__cRGR4q__shortcut {
	margin-left: auto;
}

.CommandMenu-module__cRGR4q__symbol {
	justify-content: center;
	align-items: center;
	width: 16px;
	height: 16px;
	display: flex;
}

.CommandMenu-module__cRGR4q__symbol > img {
	filter: brightness(50%);
	transform: scale(1.5);
}

@keyframes CommandMenu-module__cRGR4q__scaleIn {
	0% {
		opacity: 0;
		transform: translate(-50%) scale(.96);
	}

	to {
		opacity: 1;
		transform: translate(-50%) scale(1);
	}
}

@keyframes CommandMenu-module__cRGR4q__scaleOut {
	0% {
		opacity: 1;
		transform: translate(-50%) scale(1);
	}

	to {
		opacity: 0;
		transform: translate(-50%) scale(.96);
	}
}

@keyframes CommandMenu-module__cRGR4q__fadeIn {
	0% {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes CommandMenu-module__cRGR4q__fadeOut {
	0% {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}

@keyframes CommandMenu-module__cRGR4q__dialogBounce {
	50% {
		transform: translate(-50%) scale(.98);
	}
}

.ImageCard-module__55CvQq__img {
	-o-object-fit: cover;
	object-fit: cover;
	width: 100%;
	height: 100%;
	overflow: hidden;
}

.ImageCard-module__55CvQq__anchor {
	--border: var(--color-border-translucent);
	border: 1px solid var(--border);
	background-color: var(--color-bg-translucent);
	min-height: 280px;
	transition: var(--speed-regularTransition);
	border-radius: 8px;
	flex-direction: column;
	transition-property: background-color, border-color;
	display: flex;
	overflow: hidden;
}

@container docs (width <= 768px) {
	.ImageCard-module__55CvQq__anchor {
		min-height: 0;
		min-height: initial;
	}
}

@media (any-hover: hover) {
	.ImageCard-module__55CvQq__anchor:hover {
		background-color: var(--color-bg-tertiary);
		--border: var(--color-border-secondary);
	}
}

.ImageCard-module__55CvQq__header {
	padding: 24px 20px;
}

.ImageCard-module__55CvQq__content {
	border-top: 1px solid var(--border);
	margin-top: auto;
	padding: 20px;
	transition: inherit;
}

.ImageCard-module__55CvQq__subtitle {
	min-height: 3lh;
}

@media (max-width: 640px) {
	.ImageCard-module__55CvQq__subtitle {
		min-height: 0;
	}
}

.ShareButton-module__eyI0uW__button {
	font-weight: var(--font-weight-normal);
	color: var(--color-text-tertiary);
}

.ShareButton-module__eyI0uW__button:hover {
	color: var(--color-text-primary);
}

.ShareButton-module__eyI0uW__button svg {
	width: 16px;
	height: 16px;
}

@layer web.utils {
	.reset-module__RLQqCG__reset-a {
		cursor: pointer;
		text-decoration: none;
	}

	.reset-module__RLQqCG__reset-a,
	.reset-module__RLQqCG__reset-button,
	.reset-module__RLQqCG__reset-select {
		color: inherit;
		outline: none;
	}

	.reset-module__RLQqCG__reset-button {
		cursor: var(--cursor-pointer);
		-webkit-user-select: none;
		-moz-user-select: none;
		user-select: none;
		-webkit-appearance: none;
		-moz-appearance: none;
		appearance: none;
		font: inherit;
		-webkit-tap-highlight-color: transparent;
		background: 0 0;
		border: none;
		margin: 0;
		padding: 0;
	}

	.reset-module__RLQqCG__reset-heading {
		margin: 0;
	}

	.reset-module__RLQqCG__reset-ol,
	.reset-module__RLQqCG__reset-ul {
		margin: 0;
		padding: 0;
		list-style: none;
	}

	.reset-module__RLQqCG__reset-ol > li,
	.reset-module__RLQqCG__reset-ul > li {
		margin: 0;
		padding: 0;
	}

	.reset-module__RLQqCG__reset-li {
		margin: 0;
		padding: 0;
		list-style: none;
	}

	.reset-module__RLQqCG__reset-textarea,
	.reset-module__RLQqCG__reset-input {
		-webkit-appearance: none;
		-moz-appearance: none;
		appearance: none;
		background: 0 0;
		border: none;
		outline: none;
		width: 100%;
	}

	.reset-module__RLQqCG__reset-textarea {
		resize: none;
	}

	.reset-module__RLQqCG__reset-cite {
		font-style: normal;
	}

	.reset-module__RLQqCG__reset-select {
		-webkit-user-select: none;
		-moz-user-select: none;
		user-select: none;
		-webkit-appearance: none;
		-moz-appearance: none;
		appearance: none;
		font: inherit;
		-webkit-tap-highlight-color: transparent;
		background: 0 0;
		border: none;
		margin: 0;
		padding: 0;
	}
}

.utils-module__ZJnBSW__smooth-scroll {
	scroll-behavior: smooth;
}

.utils-module__ZJnBSW__truncate {
	white-space: nowrap;
	text-overflow: ellipsis;
	overflow: hidden;
}

.utils-module__ZJnBSW__truncateMultiline {
	-webkit-line-clamp: var(--lines, 1);
	overflow-wrap: anywhere;
	-webkit-box-orient: vertical;
	display: -webkit-box;
	overflow: hidden;
}

.utils-module__ZJnBSW__hideScrollbars {
	-ms-overflow-style: none !important;
	overflow: -moz-scrollbars-none !important;
	scrollbar-width: none !important;
}

.utils-module__ZJnBSW__hideScrollbars::-webkit-scrollbar {
	display: none;
}

.utils-module__ZJnBSW__gradientBorder {
	position: relative;
}

.utils-module__ZJnBSW__gradientBorder::before {
	content: "";
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	border-radius: inherit;
	padding: var(--gradientBorder-size, 1px);
	background: var(--gradientBorder-gradient);
	-webkit-mask-composite: xor;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	-webkit-mask-image: linear-gradient(#000, #000), linear-gradient(#000, #000);
	mask-image: linear-gradient(#000, #000), linear-gradient(#000, #000);
	-webkit-mask-position: 0 0, 0 0;
	mask-position: 0 0, 0 0;
	-webkit-mask-size: auto, auto;
	mask-size: auto, auto;
	-webkit-mask-repeat: repeat, repeat;
	mask-repeat: repeat, repeat;
	-webkit-mask-clip: content-box, border-box;
	mask-clip: content-box, border-box;
	-webkit-mask-origin: content-box, border-box;
	mask-origin: content-box, border-box;
	-webkit-mask-composite: xor;
	mask-composite: exclude;
	-webkit-mask-source-type: auto, auto;
	mask-mode: match-source, match-source;
}

.utils-module__ZJnBSW__gradientText {
	-webkit-box-decoration-break: clone;
	box-decoration-break: clone;
	text-fill-color: transparent;
	-webkit-text-fill-color: transparent;
	color: inherit;
	-webkit-background-clip: text;
	background-clip: text;
}

.utils-module__ZJnBSW__moreHitArea {
	position: relative;
}

.utils-module__ZJnBSW__moreHitArea::before {
	content: "";
	inset: var(--moreHitArea-inset);
	position: absolute;
}

.utils-module__ZJnBSW__visuallyOffscreen {
	position: absolute;
	top: -9999px;
	left: -9999px;
}

.utils-module__ZJnBSW__visuallyHidden {
	clip: rect(0, 0, 0, 0);
	white-space: nowrap;
	border-width: 0;
	width: 1px;
	height: 1px;
	margin: -1px;
	padding: 0;
	position: absolute;
	overflow: hidden;
}

.utils-module__ZJnBSW__inert {
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
}

.utils-module__ZJnBSW__contents {
	display: contents;
}

.utils-module__ZJnBSW__noSelect {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
}

.utils-module__ZJnBSW__relative {
	position: relative;
}

.utils-module__ZJnBSW__flex {
	display: flex;
}

.page-module__Byfrrq__content {
	width: 100%;
	max-width: var(--prose-max-width);
	margin: 0 auto;
}

.page-module__Byfrrq__layout {
	align-items: flex-start;
	gap: 80px;
	display: flex;
}

@media (max-width: 768px) {
	.page-module__Byfrrq__layout {
		flex-direction: column-reverse;
		gap: 24px;
	}
}

.page-module__Byfrrq__nav {
	gap: 32px;
}

@media (max-width: 1024px) {
	.page-module__Byfrrq__nav {
		gap: 24px;
	}
}

.page-module__Byfrrq__heroImage {
	border-radius: 8px;
	width: 100%;
}

.page-module__Byfrrq__iconMono {
	border-radius: var(--radius-8);
	background: var(--color-text-primary);
	width: 48px;
	height: 48px;
	transition: var(--speed-regularTransition) var(--ease-out-quad);
	flex-shrink: 0;
	transition-property: background;
	position: relative;
	overflow: hidden;
}

.page-module__Byfrrq__iconMono > img {
	filter: invert();
}

.page-module__Byfrrq__infoBlockInnerWrapper {
	gap: 80px;
	margin-top: 32px;
	margin-bottom: 32px;
}

@media (max-width: 640px) {
	.page-module__Byfrrq__infoBlockInnerWrapper {
		gap: 16px;
		margin-top: 28px;
		margin-bottom: 28px;
	}
}

.page-module__Byfrrq__infoBlockWrapper {
	margin-top: 14px;
	margin-bottom: 28px;
}

@media (max-width: 640px) {
	.page-module__Byfrrq__infoBlockWrapper {
		margin: 0;
	}
}

.page-module__Byfrrq__intro {
	margin-bottom: 32px;
}

@media (max-width: 640px) {
	.page-module__Byfrrq__intro {
		order: 2;
		margin-bottom: 0;
	}
}

.page-module__Byfrrq__headline {
	text-align: center;
}

@media (max-width: 640px) {
	.page-module__Byfrrq__headline {
		text-align: left;
	}
}

.page-module__Byfrrq__breadcrumbs {
	justify-content: center;
}

@media (max-width: 640px) {
	.page-module__Byfrrq__breadcrumbs {
		justify-content: flex-start;
	}
}

.Hero-module__QQJnga__sectionHero {
	padding-top: 72px;
	position: relative;
}

@media (max-width: 640px) {
	.Hero-module__QQJnga__sectionHero {
		padding-top: 24px;
	}
}

.Hero-module__QQJnga__heroSubtitle {
	max-width: 70%;
}

@media (max-width: 768px) {
	.Hero-module__QQJnga__heroSubtitle {
		max-width: none;
		max-width: initial;
	}
}

.Hero-module__QQJnga__heroImageContainer {
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	position: relative;
}

.Hero-module__QQJnga__heroImageContainer::before {
	content: "";
	background: red;
	margin-top: -140px;
	display: block;
}

@media (max-width: 1024px) {
	.Hero-module__QQJnga__heroImageContainer::before {
		margin-top: -18%;
	}
}

@media (max-width: 640px) {
	.Hero-module__QQJnga__heroImageContainer::before {
		margin-top: 0;
	}
}

.Hero-module__QQJnga__heroImageContainer::after {
	content: "";
	pointer-events: none;
	z-index: 2;
	background: linear-gradient(to bottom, transparent 50%, var(--color-bg-primary) 100%);
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Hero-module__QQJnga__homepageHero {
	z-index: 1;
}

@media (max-width: 640px) {
	.Hero-module__QQJnga__homepageHero h1 {
		width: 100%;
	}
}

.page-module__0ia9pq__content article {
	position: relative;
}

@media (max-width: 1024px) {
	.page-module__0ia9pq__content {
		display: block;
	}
}

.page-module__0ia9pq__category {
	color: var(--color-text-tertiary);
	font-size: 13px;
	line-height: 19px;
}

.page-module__0ia9pq__meta {
	color: var(--color-text-tertiary);
	margin: 0;
	font-size: 13px;
	line-height: 19px;
}

.page-module__0ia9pq__metaDivider {
	color: var(--color-border-primary);
	margin: 0 8px;
}

.page-module__0ia9pq__pagination {
	max-width: var(--prose-max-width);
	justify-content: space-between;
	gap: 16px;
	width: 100%;
	margin: 64px auto 0;
	display: flex;
}

.page-module__0ia9pq__pagination > * {
	flex: 1;
}

.page-module__0ia9pq__paginationLink {
	flex-direction: column;
	display: flex;
}

.page-module__0ia9pq__paginationLink[data-next="true"] {
	align-items: flex-end;
}

.page-module__0ia9pq__paginationLink span {
	transition: color .2s;
}

.page-module__0ia9pq__paginationLink:hover span:last-of-type {
	color: var(--color-text-primary);
}

.Article-module__dyo5Na__backLink {
	font-size: 14px;
	line-height: 19px;
	font-weight: var(--font-weight-normal);
	color: var(--color-text-tertiary);
	align-items: center;
	gap: 4px;
	transition: color .12s;
	display: flex;
}

.Article-module__dyo5Na__backLink svg {
	width: 15px;
	height: 15px;
}

.Article-module__dyo5Na__backLink:hover {
	color: var(--color-text-primary);
}

.ChangelogEntry-module__YvquGq__styledPostBody h2:first-of-type {
	display: none;
}

@media (max-width: 640px) {
	.ChangelogEntry-module__YvquGq__post {
		margin: 0 0 24px;
		display: block;
	}

	.ChangelogEntry-module__YvquGq__left {
		width: auto;
		width: initial;
		margin-bottom: 16px;
		position: static;
	}
}

.ChangelogEntry-module__YvquGq__contentHeader {
	border-bottom: 1px solid var(--color-border-primary);
	justify-content: space-between;
	align-items: center;
	margin-bottom: 40px;
	display: flex;
}

.GridSection-module__MrUUVW__grid {
	grid-template-columns: repeat(4, var(--1fr));
	margin-inline: calc(-1 * var(--page-padding-left)) calc(-1 * var(--page-padding-right));
	grid-gap: 16px;
	gap: 16px;
	padding-left: 4px;
	padding-right: 4px;
	display: grid;
}

@container docs (width <= 768px) {
	.GridSection-module__MrUUVW__grid {
		grid-template-columns: repeat(2, var(--1fr));
		margin-left: 0;
		margin-right: 0;
		padding-left: 0;
		padding-right: 0;
	}
}

@container docs (width <= 540px) {
	.GridSection-module__MrUUVW__grid {
		grid-template-columns: var(--1fr);
	}
}

@media (max-width: 640px) {
	.GridSection-module__MrUUVW__grid {
		grid-template-columns: var(--1fr);
	}
}

@media (max-width: 640px) {
	.OpenCommandMenuButton-module__MtQ3cq__openSearchButtonWrapper {
		display: none;
	}
}

.OpenCommandMenuButton-module__MtQ3cq__openSearchButtonWrapper .OpenCommandMenuButton-module__MtQ3cq__openSearchButton {
	color: var(--color-text-tertiary);
	--button-gap: 10px;
	background: var(--color-bg-level-2);
	border: 1px solid var(--color-border-primary);
	justify-content: flex-start;
	width: 224px;
	font-size: 14px;
	font-weight: 400;
}

.OpenCommandMenuButton-module__MtQ3cq__openSearchButtonWrapper .OpenCommandMenuButton-module__MtQ3cq__openSearchButton kbd {
	color: var(--color-text-quaternary);
	background: 0 0;
	margin-top: -1px;
	margin-left: auto;
	font-size: 14px;
}

.Verified-module__aYMhbW__badge {
	transform-origin: 50%;
	animation: 6s linear infinite paused Verified-module__aYMhbW__rotate;
}

.Verified-module__aYMhbW__root:hover .Verified-module__aYMhbW__badge {
	animation-play-state: running;
}

@keyframes Verified-module__aYMhbW__rotate {
	0% {
		transform: rotate(0);
	}

	to {
		transform: rotate(1turn);
	}
}

.Icon-module__IjVUvq__root {
	filter: var(--icon-grayscale-image-filter);
	margin-right: 12px;
}

.Collapsible-module__xbaWDW__li {
	z-index: 1;
	flex-direction: column;
	gap: 1px;
	display: flex;
	position: relative;
}

button.Collapsible-module__xbaWDW__button {
	--height: 36px;
}

button.Collapsible-module__xbaWDW__button:not(:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 8px;
	padding-right: 4px;
}

button.Collapsible-module__xbaWDW__button:not(:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 8px;
	padding-right: 4px;
}

button.Collapsible-module__xbaWDW__button:not(:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi))) {
	padding-left: 8px;
	padding-right: 4px;
}

button.Collapsible-module__xbaWDW__button:-webkit-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 4px;
	padding-right: 8px;
}

button.Collapsible-module__xbaWDW__button:-moz-any(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 4px;
	padding-right: 8px;
}

button.Collapsible-module__xbaWDW__button:is(:lang(ae), :lang(ar), :lang(arc), :lang(bcc), :lang(bqi), :lang(ckb), :lang(dv), :lang(fa), :lang(glk), :lang(he), :lang(ku), :lang(mzn), :lang(nqo), :lang(pnb), :lang(ps), :lang(sd), :lang(ug), :lang(ur), :lang(yi)) {
	padding-left: 4px;
	padding-right: 8px;
}

a.Collapsible-module__xbaWDW__button {
	--height: 32px;
	padding-left: 10px;
	padding-right: 10px;
}

@media (max-width: 768px) {
	a.Collapsible-module__xbaWDW__button {
		--height: 36px;
	}
}

.Collapsible-module__xbaWDW__button {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	cursor: pointer;
	width: 100%;
	height: var(--height);
	color: var(--color-text-tertiary);
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	font-weight: var(--font-weight-medium);
	border-radius: 8px;
	align-items: center;
	transition: none;
	display: flex;
}

.Collapsible-module__xbaWDW__button img {
	opacity: .45;
}

@media (any-hover: hover) {
	.Collapsible-module__xbaWDW__button:hover {
		color: var(--color-text-secondary);
	}

	.Collapsible-module__xbaWDW__button:hover img {
		opacity: .68;
	}
}

.Collapsible-module__xbaWDW__button[aria-current="page"] {
	color: var(--color-text-primary);
}

.Collapsible-module__xbaWDW__button[aria-current="page"] img {
	opacity: 1;
}

.Collapsible-module__xbaWDW__button[data-active="true"] {
	color: var(--color-text-primary);
}

@keyframes Collapsible-module__xbaWDW__slideDown {
	0% {
		opacity: 0;
		height: 0;
		transform: translatey(-8px);
	}

	to {
		opacity: 1;
		height: var(--radix-collapsible-content-height);
		transform: none;
	}
}

@keyframes Collapsible-module__xbaWDW__slideUp {
	0% {
		opacity: 1;
		height: var(--radix-collapsible-content-height);
		transform: none;
	}

	to {
		opacity: 0;
		height: 0;
		transform: translatey(-8px);
	}
}

.Collapsible-module__xbaWDW__ul {
	flex-direction: column;
	gap: 1px;
	padding-top: 8px;
	padding-bottom: 12px;
	display: flex;
}

.Collapsible-module__xbaWDW__animation {
	overflow: hidden;
}

@media (prefers-reduced-motion: no-preference) {
	.Collapsible-module__xbaWDW__animation[data-state="closed"] {
		animation: Collapsible-module__xbaWDW__slideUp .18s var(--ease-out-quad) forwards;
	}

	.Collapsible-module__xbaWDW__animation[data-state="open"] {
		animation: Collapsible-module__xbaWDW__slideDown .18s var(--ease-out-quad) forwards;
	}
}

.Collapsible-module__xbaWDW__chevron {
	fill: currentColor;
	width: 14px;
	height: 14px;
	margin-left: auto;
}

[data-state="closed"] .Collapsible-module__xbaWDW__chevron {
	transform: rotate(-90deg);
}

@media (prefers-reduced-motion: no-preference) {
	.Collapsible-module__xbaWDW__chevron {
		transition: transform .12s var(--ease-in-out-quad);
		transform-origin: 50%;
	}
}

.Item-module__R8N7ta__link {
	outline-offset: -2px;
}

.Item-module__R8N7ta__li {}

.Footnote-module__xKWguq__ref {
	font-feature-settings: "numr";
	vertical-align: baseline;
	vertical-align: initial;
	top: auto;
	top: initial;
}

.Footnote-module__xKWguq__link {
	vertical-align: inherit;
	color: currentColor;
	text-underline-offset: -.28em;
}

.Footnote-module__xKWguq__note {
	color: var(--color-text-quaternary);
	display: block;
	position: relative;
}

.Footnote-module__xKWguq__note:target {
	animation: Footnote-module__xKWguq__highlight 3s var(--ease-in-out-quad);
}

@keyframes Footnote-module__xKWguq__highlight {
	50% {
		color: var(--color-text-primary);
	}
}

.Footnote-module__xKWguq__container {
	background: var(--color-bg-primary);
	border-top: 1px solid var(--color-border-primary);
	padding-top: 64px;
	padding-bottom: 64px;
}

.Footnote-module__xKWguq__list {}

.Bento-module__a1IKYq__bento {
	border-top: 1px solid var(--color-border-primary);
	border-bottom: 1px solid var(--color-border-primary);
}

.Bento-module__a1IKYq__bentoA,
.Bento-module__a1IKYq__bentoB {
	padding-top: 48px;
	padding-bottom: 56px;
}

@media (max-width: 768px) {
	.Bento-module__a1IKYq__bentoA,
	.Bento-module__a1IKYq__bentoB {
		padding-top: 32px;
		padding-bottom: 32px;
	}
}

.Bento-module__a1IKYq__bentoA {
	position: relative;
}

.Bento-module__a1IKYq__bentoA::after {
	--border-width: 1px;
	content: "";
	height: 100%;
	width: var(--border-width);
	background: var(--color-border-primary);
	transform: translatex(calc(var(--grid-gap) / 2 + var(--border-width) / 2));
	position: absolute;
	top: 0;
	bottom: 0;
	right: 0;
}

@media (max-width: 768px) {
	.Bento-module__a1IKYq__bentoA::after {
		content: none;
	}
}

.Bento-module__a1IKYq__bentoB {
	padding-bottom: 96px;
	padding-left: 24px;
}

@media (max-width: 640px) {
	.Bento-module__a1IKYq__bentoB {
		padding-bottom: 72px;
		padding-left: 0;
		overflow: hidden;
	}
}

.Bento-module__a1IKYq__bentoContent {
	max-width: 360px;
}

.Bento-module__a1IKYq__insetImage {
	margin-left: -4px;
}

@media (max-width: 640px) {
	.Bento-module__a1IKYq__insetImage {
		margin-left: 0;
	}
}

.Bento-module__a1IKYq__insetImage.Bento-module__a1IKYq__insetImageB {
	width: 472px;
	max-width: 472px;
}

@media (max-width: 640px) {
	.Bento-module__a1IKYq__insetImage.Bento-module__a1IKYq__insetImageB {
		width: 100%;
		max-width: 100%;
	}
}

.UseCases-module__n8-8Oq__card {
	text-align: start;
	background: var(--color-bg-level-1);
	border-radius: var(--radius-12);
	border: 1px solid var(--color-line-secondary);
	min-height: 240px;
	transition: var(--speed-quickTransition) var(--ease-out-quad);
	flex-direction: column;
	flex: 1 0 320px;
	justify-content: space-between;
	align-items: stretch;
	gap: 16px;
	padding-top: 32px;
	padding-bottom: 32px;
	padding-left: 24px;
	padding-right: 24px;
	transition-property: background, border-color, transform;
	display: flex;
}

.UseCases-module__n8-8Oq__card:active {
	transform: scale(.97);
}

@media (any-hover: hover) {
	.UseCases-module__n8-8Oq__card:hover {
		background: var(--color-bg-level-2);
	}

	.UseCases-module__n8-8Oq__card:hover .UseCases-module__n8-8Oq__iconButton {
		color: var(--color-text-primary);
		border-color: var(--color-bg-tertiary);
		background: var(--color-bg-tertiary);
	}
}

@media (max-width: 1024px) {
	.UseCases-module__n8-8Oq__card {
		min-height: 0;
	}
}

.UseCases-module__n8-8Oq__close.UseCases-module__n8-8Oq__close {
	z-index: 1;
	margin-left: auto;
	display: flex;
	position: fixed;
	top: 24px;
	right: 24px;
}

.UseCases-module__n8-8Oq__dialogContent {
	max-width: var(--page-max-width);
	background: var(--color-bg-level-1);
	box-shadow: var(--shadow-high);
	z-index: var(--layer-dialog);
	border-radius: var(--radius-8);
	border: 1px solid var(--color-border-translucent);
	contain: strict;
	isolation: isolate;
	outline: none;
	margin-left: auto;
	margin-right: auto;
	position: fixed;
	top: 5vh;
	bottom: 5vh;
	left: 0;
	right: 0;
}

.UseCases-module__n8-8Oq__dialogContent[data-state="open"] {
	animation: .18s UseCases-module__n8-8Oq__dialogOpen;
}

.UseCases-module__n8-8Oq__dialogContent[data-state="closed"] {
	animation: .18s UseCases-module__n8-8Oq__dialogClose;
}

.UseCases-module__n8-8Oq__scrollable {
	padding-left: 32px;
	padding-right: 32px;
}

@keyframes UseCases-module__n8-8Oq__dialogOpen {
	0% {
		opacity: 0;
		transform: scale(.95);
	}

	to {
		opacity: 1;
		transform: scale(1);
	}
}

@keyframes UseCases-module__n8-8Oq__dialogClose {
	0% {
		opacity: 1;
		transform: scale(1);
	}

	to {
		opacity: 0;
		transform: scale(.95);
	}
}

.Comparison-module__CFcWcq__table {
	--bottom-cell-height: 125px;
	--table-bg: var(--color-bg-primary);
	background: var(--table-bg);
	grid-template-columns: 1fr;
	grid-auto-rows: auto;
	display: grid;
	position: relative;
}

@media (max-width: 768px) {
	.Comparison-module__CFcWcq__table {
		--bottom-cell-height: 104px;
	}
}

.Comparison-module__CFcWcq__sticky {
	top: calc(var(--header-height) - 10px);
	margin-bottom: var(--bottom-cell-height);
	z-index: var(--layer-1);
	border-bottom: 1px solid var(--color-line-secondary);
	background: var(--table-bg);
	position: -webkit-sticky;
	position: sticky;
}

.Comparison-module__CFcWcq__body {
	margin-top: calc(-1 * var(--bottom-cell-height));
}

.Comparison-module__CFcWcq__select {
	border-radius: var(--radius-8);
	letter-spacing: -.47px;
	font-size: 24px;
	line-height: 32px;
	font-weight: var(--font-weight-semibold);
	background: 0 0;
	border: none;
}

@media (any-hover: hover) {
	.Comparison-module__CFcWcq__select:hover {
		background: var(--color-bg-tertiary);
	}
}

.Comparison-module__CFcWcq__select:active {
	background: var(--color-bg-tertiary);
}

.Comparison-module__CFcWcq__selectCell {
	padding: 18px 8px 8px;
}

:where(.Comparison-module__CFcWcq__table) :where(table, thead, tbody, th, td, tr) {
	display: block;
}

.Comparison-module__CFcWcq__row {
	grid-template-columns: repeat(4, var(--1fr));
	width: 100%;
	display: grid;
}

.Comparison-module__CFcWcq__row + .Comparison-module__CFcWcq__row {
	border-top: 1px solid var(--color-line-secondary);
}

@media (max-width: 768px) {
	.Comparison-module__CFcWcq__row {
		grid-template-columns: var(--1fr);
	}

	.Comparison-module__CFcWcq__table:has(option[value="free"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 2) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="free"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 3) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="free"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 4) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="basic"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 1) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="basic"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 3) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="basic"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 4) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="business"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 1) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="business"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 2) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="business"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 4) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="enterprise"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 1) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="enterprise"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 2) {
		display: none;
	}

	.Comparison-module__CFcWcq__table:has(option[value="enterprise"]:checked) .Comparison-module__CFcWcq__row > :where(.Comparison-module__CFcWcq__featureCell, .Comparison-module__CFcWcq__ctaCell):nth-child(4n + 3) {
		display: none;
	}
}

@media not (max-width: 768px) {
	.Comparison-module__CFcWcq__row > * {
		border-left: 1px solid transparent;
		border-right: 1px solid transparent;
	}

	.Comparison-module__CFcWcq__row:last-of-type > :nth-child(3) {
		border-bottom: 1px solid var(--color-line-secondary);
		border-radius: 0 0 12px 12px;
	}

	.Comparison-module__CFcWcq__row > :nth-child(4n + 3),
	.Comparison-module__CFcWcq__row > :nth-child(4n + 5) {
		background: var(--color-bg-level-2);
		border-color: var(--color-line-secondary);
	}
}

.Comparison-module__CFcWcq__planHeaderContainer {
	padding: 28px 24px 20px;
}

@media not (max-width: 768px) {
	.Comparison-module__CFcWcq__planHeaderContainer:nth-child(3) {
		border-top: 1px solid var(--color-line-secondary);
		border-radius: 12px 12px 0 0;
	}
}

.Comparison-module__CFcWcq__subtitleCell {
	padding: 24px;
}

.Comparison-module__CFcWcq__featureCell {
	align-items: center;
	min-height: 42px;
	padding: 16px 24px;
	display: flex;
	position: relative;
}

.Comparison-module__CFcWcq__tooltip {
	color: var(--color-text-tertiary);
	transition: color .12s var(--ease-out-quad);
}

.Comparison-module__CFcWcq__tooltip:hover {
	color: var(--color-text-primary);
}

.Comparison-module__CFcWcq__cta {
	width: 100%;
}

.Comparison-module__CFcWcq__ctaCell {
	padding: 32px 20px;
}

.Comparison-module__CFcWcq__businessCell {
	padding-bottom: 16px;
}

.Comparison-module__CFcWcq__checkContainer {
	width: 20px;
	height: 20px;
}

.Jobs-module__fNHnxW__job {
	background-image: linear-gradient(to right, var(--color-border-primary) 50%, rgba(255, 255, 255, 0) 0%);
	background-position: bottom;
	background-repeat: repeat-x;
	background-size: 8px 1px;
	align-items: center;
	width: 100%;
	min-height: 80px;
	padding-top: 12px;
	padding-bottom: 12px;
	display: flex;
}

.Jobs-module__fNHnxW__job > div {
	width: 100%;
}

.Jobs-module__fNHnxW__job:focus-visible {
	border-radius: 16px;
}

.Jobs-module__fNHnxW__applyButton {
	color: var(--color-link-primary);
	transition: color .16s var(--ease-out-quad);
}

.Jobs-module__fNHnxW__department {
	border-bottom: 1px solid var(--color-border-primary);
	margin-top: 40px;
	padding-top: 16px;
	padding-bottom: 16px;
}

.Jobs-module__fNHnxW__section:first-of-type .Jobs-module__fNHnxW__department {
	margin-top: 48px;
}

@media (max-width: 768px) {
	.Jobs-module__fNHnxW__section:first-of-type .Jobs-module__fNHnxW__department {
		margin-top: 24px;
	}
}
/*# sourceMappingURL=1e28d81ca9712914.css.map*/
.SpecList-module__lJ2DKG__root {
	grid-template-columns: auto var(--1fr);
	display: grid;
}

@media (max-width: 640px) {
	.SpecList-module__lJ2DKG__root {
		grid-template-columns: 1fr;
	}
}

.SpecList-module__lJ2DKG__item {
	display: contents;
}

@media (max-width: 640px) {
	.SpecList-module__lJ2DKG__item {
		flex-direction: column;
		gap: 8px;
		display: flex;
	}
}

.SpecList-module__lJ2DKG__label {
	letter-spacing: -.18px;
	font-size: 14px;
	line-height: 21px;
	font-weight: var(--font-weight-medium);
}

.SpecList-module__lJ2DKG__value {
	letter-spacing: -.18px;
	color: var(--color-text-tertiary);
	text-wrap: pretty;
	font-size: 14px;
	line-height: 21px;
}
/*# sourceMappingURL=57cf602a88c4fb38.css.map*/
.GlassContainer-module__WDhx3G__outer {
	--gradientBorder-size: 1px;
	--gradientBorder-gradient: linear-gradient(to bottom right, rgba(255, 255, 255, .07), transparent);
	border-radius: 18px;
	width: 100%;
	height: 100%;
	padding: 8px;
}

.GlassContainer-module__WDhx3G__inner {
	isolation: isolate;
	--gradientBorder-size: 1px;
	--gradientBorder-gradient: linear-gradient(to bottom right, rgba(255, 255, 255, .17), transparent);
	background: linear-gradient(134deg, rgba(255, 255, 255, .08), rgba(255, 255, 255, .02), rgba(255, 255, 255, 0) 55%);
	border-radius: 10px;
	position: relative;
	overflow: hidden;
}

.GlassContainer-module__WDhx3G__inner::after {
	content: "";
	pointer-events: none;
	filter: url("#noiseFilter");
	mix-blend-mode: overlay;
	opacity: .1;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

.Cycles-module__XX6nRa__root {
	pointer-events: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	--mask-bottom: linear-gradient(to bottom, var(--mask-visible) 30%, var(--mask-invisible) 80%);
	--mask-right: linear-gradient(to right, var(--mask-visible) 40%, var(--mask-invisible) 90%);
	-webkit-mask-image: var(--mask-bottom), var(--mask-right);
	-webkit-mask-image: var(--mask-bottom), var(--mask-right);
	mask-image: var(--mask-bottom), var(--mask-right);
	-webkit-mask-composite: source-in;
	-webkit-mask-composite: source-in;
	mask-composite: intersect;
}

.Cycles-module__XX6nRa__glass {
	padding: 16px 24px;
}

.Cycles-module__XX6nRa__box {
	background: currentColor;
	border-radius: 1px;
	width: 6px;
	height: 6px;
}

.Logos-module__9HC_Ua__logoGrid {
	grid-gap: 24px;
	grid-template-columns: repeat(4, var(--1fr));
	grid-row-gap: 48px;
	place-items: center;
	gap: 48px 24px;
	width: 100%;
	margin-top: 16px;
	display: grid;
}

.Logos-module__9HC_Ua__logoGridItem {
	aspect-ratio: 8 / 2;
	flex-direction: column;
	width: 100%;
	height: 100%;
	display: flex;
	position: relative;
	overflow: hidden;
}

.Logos-module__9HC_Ua__logoItem {
	justify-content: center;
	align-items: center;
	gap: 24px;
	min-height: 100%;
	display: flex;
}

.ProjectOverview-module__C0ELRa__root {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	aspect-ratio: 432 / 320;
	--mask-bottom: linear-gradient(to bottom, var(--mask-visible) 50%, var(--mask-invisible) 100%);
	--mask-right: linear-gradient(to right, var(--mask-visible) 20%, var(--mask-invisible) 100%);
	width: 100%;
	max-width: 100%;
	max-height: 100%;
	-webkit-mask-image: var(--mask-bottom), var(--mask-right);
	-webkit-mask-image: var(--mask-bottom), var(--mask-right);
	mask-image: var(--mask-bottom), var(--mask-right);
	-webkit-mask-composite: source-in;
	overflow: hidden;
	-webkit-mask-composite: source-in;
	mask-composite: intersect;
}

.ProjectOverview-module__C0ELRa__dd {
	white-space: nowrap;
	padding-left: 6px;
}

.ProjectOverview-module__C0ELRa__inner {
	height: 100%;
	padding: 32px 24px;
}

.ProjectOverview-module__C0ELRa__column {
	min-width: 108px;
}

.ProjectOverview-module__C0ELRa__btn {
	background: var(--color-bg-tertiary);
	white-space: nowrap;
	border-radius: 6px;
	align-items: center;
	gap: 4px;
	padding: 2px 6px;
	display: flex;
}

.Triage-module__Xuer_q__root {
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	position: relative;
}

.Triage-module__Xuer_q__glass {
	padding: 16px 24px;
}

.Triage-module__Xuer_q__mask {
	--mask-bottom: linear-gradient(to bottom, var(--mask-visible) 30%, var(--mask-invisible) 80%);
	--mask-right: linear-gradient(to right, var(--mask-visible) 40%, var(--mask-invisible) 90%);
	-webkit-mask-image: var(--mask-bottom), var(--mask-right);
	-webkit-mask-image: var(--mask-bottom), var(--mask-right);
	mask-image: var(--mask-bottom), var(--mask-right);
	-webkit-mask-composite: source-in;
	-webkit-mask-composite: source-in;
	mask-composite: intersect;
}

.Triage-module__Xuer_q__item {
	border: 1px solid transparent;
	border-radius: 6px;
	padding: 10px;
	position: relative;
}

.Triage-module__Xuer_q__item[data-selected="true"] {
	background: rgba(255, 255, 255, .05);
	border-color: rgba(255, 255, 255, .1);
}

.Triage-module__Xuer_q__menu {
	-webkit-backdrop-filter: blur(12px);
	backdrop-filter: blur(12px);
	min-width: 180px;
	box-shadow: var(--shadow-high);
	border-radius: var(--radius-8);
	background: rgba(255, 255, 255, .1);
	border: 1px solid rgba(255, 255, 255, .1);
	padding: 4px;
	position: absolute;
	top: 103px;
	left: 120px;
}

.Triage-module__Xuer_q__menu > div {
	height: 32px;
	color: var(--color-text-tertiary);
	cursor: default;
	transition: .16s var(--ease-out-quad);
	border-radius: 6px;
	padding: 0 8px;
	transition-property: transform;
}

@media (any-hover: hover) {
	.Triage-module__Xuer_q__menu > div:hover {
		color: var(--color-text-primary);
		background: rgba(255, 255, 255, .1);
	}
}

.Triage-module__Xuer_q__menu > div:active {
	will-change: transform;
	background: rgba(255, 255, 255, .08);
	transition-property: transform, background;
	transform: scale(.97);
}

.CenteredQuote-module__-xja6a__cite {
	max-height: 46px;
	display: flex;
}
/*# sourceMappingURL=0fc1ea3fc88c2727.css.map*/
.fMHvBv {
	font-size: var(--title-8-size);
	line-height: var(--title-8-line-height);
	letter-spacing: var(--title-8-letter-spacing);
	text-wrap: balance;
	text-align: start;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

@media (max-width: 768px) {
	.fMHvBv {
		font-size: var(--title-6-size);
		line-height: var(--title-6-line-height);
		letter-spacing: var(--title-6-letter-spacing);
	}
}

/*!sc*/

@media (max-width: 640px) {
	.fMHvBv {
		font-size: var(--title-5-size);
		line-height: var(--title-5-line-height);
		letter-spacing: var(--title-5-letter-spacing);
	}
}

/*!sc*/

u.fMHvBv {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.fMHvBv {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.fMHvBv {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.fMHvBv {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

u.jZyIgO {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.jZyIgO {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.jZyIgO {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.jZyIgO {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.bVOqCN {
	text-align: center;
}

/*!sc*/

u.bVOqCN {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.bVOqCN {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.bVOqCN {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.bVOqCN {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.hOchjZ {
	font-size: var(--text-large-size);
	line-height: var(--text-large-line-height);
	letter-spacing: var(--text-large-letter-spacing);
	color: var(--color-text-tertiary);
	text-align: start;
}

/*!sc*/

u.hOchjZ {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.hOchjZ {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.hOchjZ {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.hOchjZ {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.fRLGfF {
	text-wrap: balance;
}

/*!sc*/

u.fRLGfF {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.fRLGfF {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.fRLGfF {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.fRLGfF {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.eOGXTn {
	background: linear-gradient(to right, var(--color-text-primary), transparent 80%), var(--color-text-tertiary);
	-webkit-box-decoration-break: clone;
	box-decoration-break: clone;
	-webkit-box-decoration-break: clone;
	-webkit-background-clip: text;
	background-clip: text;
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
	text-fill-color: transparent;
	-webkit-text-fill-color: transparent;
	color: unset;
	padding-bottom: 0.13em;
}

/*!sc*/

.eOGXTn::selection,
.eOGXTn *::selection {
	background: var(--color-selection-dim);
}

/*!sc*/

u.eOGXTn {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.eOGXTn {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.eOGXTn {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.eOGXTn {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.cStvXx {
	font-size: var(--title-2-size);
	line-height: var(--title-2-line-height);
	letter-spacing: var(--title-2-letter-spacing);
	color: var(--color-text-tertiary);
	text-align: center;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.cStvXx {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.cStvXx {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.cStvXx {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.cStvXx {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.bitCO {
	color: var(--color-text-primary);
}

/*!sc*/

u.bitCO {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.bitCO {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.bitCO {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.bitCO {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.eZsIvj {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--color-text-tertiary);
	text-wrap: balance;
	text-align: center;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.eZsIvj {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.eZsIvj {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.eZsIvj {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.eZsIvj {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.iltGqm {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.iltGqm {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.iltGqm {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.iltGqm {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.iltGqm {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.ezvLzw {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--color-text-tertiary);
	text-wrap: balance;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.ezvLzw {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.ezvLzw {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.ezvLzw {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.ezvLzw {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.jMizkN {
	font-size: var(--title-2-size);
	line-height: var(--title-2-line-height);
	letter-spacing: var(--title-2-letter-spacing);
	text-wrap: balance;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.jMizkN {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.jMizkN {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.jMizkN {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.jMizkN {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.hOuzMt {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	color: var(--color-text-secondary);
}

/*!sc*/

u.hOuzMt {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.hOuzMt {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.hOuzMt {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.hOuzMt {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.kAVYhy {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-primary);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.kAVYhy {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.kAVYhy {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.kAVYhy {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.kAVYhy {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.jNXKas {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-secondary);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.jNXKas {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.jNXKas {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.jNXKas {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.jNXKas {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.hcrjwi {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.hcrjwi {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.hcrjwi {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.hcrjwi {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.hcrjwi {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.dzzsBK {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	color: var(--color-text-tertiary);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.dzzsBK {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.dzzsBK {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.dzzsBK {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.dzzsBK {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.cypvFY {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	color: var(--color-text-secondary);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.cypvFY {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.cypvFY {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.cypvFY {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.cypvFY {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.kWuiTk {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	color: var(--color-text-tertiary);
	font-family: var(--font-monospace);
	font-feature-settings: normal;
	font-variation-settings: normal;
	letter-spacing: normal;
}

/*!sc*/

u.kWuiTk {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.kWuiTk {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.kWuiTk {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.kWuiTk {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.iEbDtO {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	color: var(--color-text-tertiary);
	white-space: nowrap;
	font-family: var(--font-monospace);
	font-feature-settings: normal;
	font-variation-settings: normal;
	letter-spacing: normal;
}

/*!sc*/

u.iEbDtO {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.iEbDtO {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.iEbDtO {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.iEbDtO {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.gwcUhO {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	color: var(--color-text-secondary);
	white-space: nowrap;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.gwcUhO {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.gwcUhO {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.gwcUhO {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.gwcUhO {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.cfFSQT {
	font-size: var(--text-mini-size);
	line-height: var(--text-mini-line-height);
	letter-spacing: var(--text-mini-letter-spacing);
	color: var(--color-text-tertiary);
}

/*!sc*/

u.cfFSQT {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.cfFSQT {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.cfFSQT {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.cfFSQT {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.piDjS {
	color: var(--color-text-tertiary);
}

/*!sc*/

u.piDjS {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.piDjS {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.piDjS {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.piDjS {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.lmmAOC {
	font-size: var(--title-2-size);
	line-height: var(--title-2-line-height);
	letter-spacing: var(--title-2-letter-spacing);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.lmmAOC {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.lmmAOC {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.lmmAOC {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.lmmAOC {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.bLUfgQ {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-tertiary);
	font-weight: var(--font-weight-normal);
}

/*!sc*/

u.bLUfgQ {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.bLUfgQ {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.bLUfgQ {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.bLUfgQ {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.jutaCz {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-tertiary);
}

/*!sc*/

u.jutaCz {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.jutaCz {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.jutaCz {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.jutaCz {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.fYfDkp {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-secondary);
}

/*!sc*/

u.fYfDkp {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.fYfDkp {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.fYfDkp {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.fYfDkp {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.dSNvwJ {
	color: var(--color-text-tertiary);
	font-weight: var(--font-weight-normal);
}

/*!sc*/

u.dSNvwJ {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.dSNvwJ {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.dSNvwJ {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.dSNvwJ {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.jZFcUM {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--red);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.jZFcUM {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.jZFcUM {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.jZFcUM {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.jZFcUM {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.iozooe {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
}

/*!sc*/

u.iozooe {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.iozooe {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.iozooe {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.iozooe {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.cHSTto {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--color-text-quaternary);
}

/*!sc*/

u.cHSTto {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.cHSTto {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.cHSTto {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.cHSTto {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.vEiJb {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--orange);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.vEiJb {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.vEiJb {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.vEiJb {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.vEiJb {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.jkolvI {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--green);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.jkolvI {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.jkolvI {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.jkolvI {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.jkolvI {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.bpBBlQ {
	font-size: var(--title-3-size);
	line-height: var(--title-3-line-height);
	letter-spacing: var(--title-3-letter-spacing);
	color: var(--color-text-primary);
	text-wrap: balance;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.bpBBlQ {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.bpBBlQ {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.bpBBlQ {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.bpBBlQ {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.eEqsx {
	font-size: var(--title-1-size);
	line-height: var(--title-1-line-height);
	letter-spacing: var(--title-1-letter-spacing);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.eEqsx {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.eEqsx {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.eEqsx {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.eEqsx {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.geMxYu {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--color-text-tertiary);
}

/*!sc*/

u.geMxYu {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.geMxYu {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.geMxYu {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.geMxYu {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.hrBGyM {
	color: var(--color-text-quaternary);
}

/*!sc*/

u.hrBGyM {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.hrBGyM {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.hrBGyM {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.hrBGyM {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.fYCtHf {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.fYCtHf {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.fYCtHf {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.fYCtHf {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.fYCtHf {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.jlsnDv {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-tertiary);
	display: -webkit-box;
	-webkit-box-orient: vertical;
	-webkit-line-clamp: 1;
	overflow: hidden;
	overflow-wrap: anywhere;
}

/*!sc*/

u.jlsnDv {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.jlsnDv {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.jlsnDv {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.jlsnDv {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.hZTiA {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-quaternary);
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.hZTiA {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.hZTiA {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.hZTiA {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.hZTiA {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.ctGxyj {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
}

/*!sc*/

u.ctGxyj {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.ctGxyj {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.ctGxyj {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.ctGxyj {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.kqDwdU {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	text-wrap: balance;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.kqDwdU {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.kqDwdU {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.kqDwdU {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.kqDwdU {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.coozSp {
	font-size: var(--text-regular-size);
	line-height: var(--text-regular-line-height);
	letter-spacing: var(--text-regular-letter-spacing);
	color: var(--color-text-tertiary);
	text-wrap: balance;
}

/*!sc*/

u.coozSp {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.coozSp {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.coozSp {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.coozSp {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.ggmmFt {
	font-size: var(--text-small-size);
	line-height: var(--text-small-line-height);
	letter-spacing: var(--text-small-letter-spacing);
	color: var(--color-text-quaternary);
}

/*!sc*/

u.ggmmFt {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.ggmmFt {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.ggmmFt {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.ggmmFt {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

.ffhGVm {
	font-size: var(--title-5-size);
	line-height: var(--title-5-line-height);
	letter-spacing: var(--title-5-letter-spacing);
	text-wrap: balance;
	font-weight: var(--font-weight-medium);
}

/*!sc*/

u.ffhGVm {
	-webkit-text-decoration: underline;
	text-decoration: underline;
	text-decoration-style: solid;
	text-decoration-thickness: 1.5px;
	text-decoration-color: var(--color-text-quaternary);
	text-underline-offset: 2.5px;
}

/*!sc*/

sup.ffhGVm {
	position: relative;
	vertical-align: initial;
	top: -0.5em;
	font-size: 0.6em;
}

/*!sc*/

code.ffhGVm {
	font-family: var(--font-monospace);
	font-size: 0.9em;
	background: none;
	padding: 0;
}

/*!sc*/

label.ffhGVm {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/*!sc*/

data-styled.g1[id="Text-sc-111816cf-0"] {
	content: "fMHvBv,jZyIgO,bVOqCN,hOchjZ,fRLGfF,eOGXTn,cStvXx,bitCO,eZsIvj,iltGqm,ezvLzw,jMizkN,hOuzMt,kAVYhy,jNXKas,hcrjwi,dzzsBK,cypvFY,kWuiTk,iEbDtO,gwcUhO,cfFSQT,piDjS,lmmAOC,bLUfgQ,jutaCz,fYfDkp,dSNvwJ,jZFcUM,iozooe,cHSTto,vEiJb,jkolvI,bpBBlQ,eEqsx,geMxYu,hrBGyM,fYCtHf,jlsnDv,hZTiA,ctGxyj,kqDwdU,coozSp,ggmmFt,ffhGVm,";
}

/*!sc*/

.hQMHUV {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	position: relative;
	-webkit-align-items: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	-webkit-justify-content: center;
	justify-content: center;
	line-height: 0;
	-webkit-flex-shrink: 0;
	-ms-flex-negative: 0;
	flex-shrink: 0;
	aspect-ratio: 1 / 1;
	width: 24px;
	height: 24px;
}

/*!sc*/

.dvuLBl {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	position: relative;
	-webkit-align-items: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	-webkit-justify-content: center;
	justify-content: center;
	line-height: 0;
	-webkit-flex-shrink: 0;
	-ms-flex-negative: 0;
	flex-shrink: 0;
	aspect-ratio: 1 / 1;
	width: 16px;
	height: 16px;
}

/*!sc*/

.jMPhQF {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	position: relative;
	-webkit-align-items: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	-webkit-justify-content: center;
	justify-content: center;
	line-height: 0;
	-webkit-flex-shrink: 0;
	-ms-flex-negative: 0;
	flex-shrink: 0;
	aspect-ratio: 1 / 1;
	width: 18px;
	height: 18px;
}

/*!sc*/

data-styled.g5[id="AvatarContainer-sc-d02e8e43-0"] {
	content: "hQMHUV,dvuLBl,jMPhQF,";
}

/*!sc*/

.feHLNu {
	border-radius: 50%;
	width: 100%;
	height: 100%;
	pointer-events: none;
	object-fit: cover;
}

/*!sc*/

data-styled.g6[id="Avatar__AvatarImg-sc-3c9cd143-0"] {
	content: "feHLNu,";
}

/*!sc*/

.jmdqzM {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-flex: initial;
	-ms-flex: initial;
	flex: initial;
	-webkit-flex-direction: row;
	-ms-flex-direction: row;
	flex-direction: row;
	-webkit-align-items: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
}

/*!sc*/

data-styled.g10[id="Flex-sc-9512dbf9-0"] {
	content: "jmdqzM,";
}

/*!sc*/

.etbfoe {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	max-width: 24px;
	max-height: 24px;
}

/*!sc*/

.etbfoe:not(:first-child) {
	margin-left: -6px;
}

/*!sc*/

.etbfoe > * {
	-webkit-mask: radial-gradient(104% 72.5% at calc(200% - 100% * var(--mask-overlap, 0)) 50%, rgba(0, 0, 0, 0) 98.5%, rgba(0, 0, 0, 1) 100%);
	mask: radial-gradient(104% 72.5% at calc(200% - 100% * var(--mask-overlap, 0)) 50%, rgba(0, 0, 0, 0) 98.5%, rgba(0, 0, 0, 1) 100%);
}

/*!sc*/

data-styled.g12[id="IconPile__ItemWrapper-sc-cec4b27c-0"] {
	content: "etbfoe,";
}

/*!sc*/
/* Start Project Wallace extracted inline styles */
div {
	position: relative;
}

span {
	-webkit-touch-callout: none;
	display: flex;
}

rect {
	transform-origin: center;
	transition: 160ms var(--ease-out-quad);
	transform: translatey(-3.5px);
}

rect {
	transform-origin: center;
	transition: 160ms var(--ease-out-quad);
	transform: translatey(3.5px);
}

div.hide-tablet.Spacer-module__1ERWdW__root {
	--height: 80px;
}

div.show-tablet.Spacer-module__1ERWdW__root {
	--height: 56px;
}

div.hide-tablet.Spacer-module__1ERWdW__root {
	--height: 32px;
}

span.Text-sc-111816cf-0.jZyIgO {
	display: block;
	max-width: 900px;
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span.show-mobile {
	display: inline-block;
	text-align: center;
}

span.Text-sc-111816cf-0.bVOqCN {
	display: inline;
	max-width: 450px;
	margin: 0 auto;
	width: 100%;
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

div.Spacer-module__1ERWdW__root {
	--height: 20px;
}

span.hide-mobile.Hero-module__QQJnga__heroSubtitle {
	display: inline-block;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span.show-mobile {
	display: inline-block;
	text-wrap: balance;
	text-align: center;
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

div.hide-mobile.Spacer-module__1ERWdW__root {
	--height: 30px;
}

div.show-mobile.Spacer-module__1ERWdW__root {
	--height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 16px;
}

div {
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

div {
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span.Text-sc-111816cf-0.eOGXTn {
	padding: 0;
}

svg {
	--icon-color: var(--color-text-quaternary);
}

div.show-mobile {
	width: 100%;
}

div.Spacer-module__1ERWdW__root {
	--height: 8px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column.Flex-module__A66dmG__center {
	width: 100%;
	gap: 16px;
}

div {
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

div {
	opacity: 0;
	filter: blur(10px);
	transform: translatey(20%);
}

span.Text-sc-111816cf-0.eOGXTn {
	padding: 0;
}

svg {
	--icon-color: var(--color-text-quaternary);
}

div.hide-mobile.Spacer-module__1ERWdW__root {
	--height: -64px;
}

div.show-mobile.Spacer-module__1ERWdW__root {
	--height: -32px;
}

div.HeroIllustration-module__LcHIQG__threeD.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center.Flex-module__A66dmG__justify-space-between {
	padding-inline: 4px;
}

div {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn.HeroIllustration-module__LcHIQG__trafficLights.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.Spacer-module__1ERWdW__root {
	--height: 14px;
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.Spacer-module__1ERWdW__root {
	--height: 12px;
}

div.HeroIllustration-module__LcHIQG__threeD.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 16px;
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.HeroIllustration-module__LcHIQG__threeD.HeroIllustration-module__LcHIQG__animateIn {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

div.HeroIllustration-module__LcHIQG__inbox {
	opacity: 0;
	filter: blur(10px);
	transform: translatez(300px) translatex(50px);
}

g {
	mix-blend-mode: lighten;
}

div.Spacer-module__1ERWdW__root {
	--height: 32px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 160px;
}

svg {
	--icon-color: #9c9da1;
}

div.Marquee-module__SWfNTW__root.Flex-module__A66dmG__root {
	--Marquee-shadow-size: 16px;
	--Marquee-duration: 60s;
	--flex-direction: row;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

svg.Icon-module__PGbYKa__logotype.color-module__UZINAa__primary {
	--Logotype-width: 120px;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a b b b b b b";
	--grid-areas-laptop: "a a a a a a a a a a a a" "b b b b b b b b . . . .";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Grid-module__HlBHsa__b {
	align-self: end;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center.Flex-module__A66dmG__inline {
	gap: 4px;
}

svg.page-module__x5b50W__chevronLink {
	--icon-color: var(--color-text-primary);
}

div.Spacer-module__1ERWdW__root {
	--height: 48px;
}

div.Carousel-module__imM5Ra__variant-inset.Carousel-module__imM5Ra__align-center {
	--Carousel-gap: 8px;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.DifferentCard-module__ZPfTEW__title.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	width: 100%;
	gap: 16px;
}

svg {
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.DifferentCard-module__ZPfTEW__title.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	width: 100%;
	gap: 16px;
}

svg {
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.DifferentCard-module__ZPfTEW__title.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	width: 100%;
	gap: 16px;
}

svg {
	--icon-color: #9c9da1;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a a a a a a . ." "b b b b b b b . . . . . .";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Eyebrow-module__kZTp2W__eyebrowIndicator {
	background-color: #02B8CC;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

svg.page-module__x5b50W__chevronLink {
	--icon-color: currentColor;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

p.Text-sc-111816cf-0.jZyIgO.typography-module__c6hvxG__subtitle {
	max-width: 400px;
}

div.Spacer-module__1ERWdW__root {
	--height: 24px;
}

svg {
	--icon-color: #9c9da1;
}

div.hide-mobile.Spacer-module__1ERWdW__root {
	--height: 72px;
}

div.show-mobile.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.page-module__HPIeYG__cmdk {
	transform: translatey(0%) rotatex(30deg) scale(1.15);
}

div.page-module__HPIeYG__cmdkItems {
	transform: rotatex(30deg) translatey(3%) scale(1.29);
}

div {
	position: relative;
}

div.page-module__HPIeYG__cmdkItem.page-module__HPIeYG__cmdkItemSelected {
	transform: scale(1.04) rotatex(17deg);
}

img.Image-module__CYTY7q__root {
	color: transparent;
	border-radius: 50%;
}

svg {
	margin-left: auto;
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
	border-radius: 50%;
}

svg {
	margin-left: auto;
	--icon-color: #9c9da1;
}

div {
	position: relative;
}

div.page-module__HPIeYG__cmdkItem {
	transform: scale(1);
}

img.Image-module__CYTY7q__root {
	color: transparent;
	border-radius: 50%;
}

div {
	position: relative;
}

div.page-module__HPIeYG__cmdkItem {
	transform: scale(1);
}

img.Image-module__CYTY7q__root {
	color: transparent;
	border-radius: 50%;
}

div {
	position: relative;
}

div.page-module__HPIeYG__cmdkItem {
	transform: scale(1);
}

img.Image-module__CYTY7q__root {
	color: transparent;
	border-radius: 50%;
}

div {
	position: relative;
}

div.page-module__HPIeYG__cmdkItem {
	transform: scale(1);
}

img.Image-module__CYTY7q__root {
	color: transparent;
	border-radius: 50%;
}

div {
	position: relative;
}

div.page-module__HPIeYG__cmdkItem {
	transform: scale(1);
}

img.Image-module__CYTY7q__root {
	color: transparent;
	border-radius: 50%;
}

div.hide-mobile.Spacer-module__1ERWdW__root {
	--height: 128px;
}

div.show-mobile.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.page-module__x5b50W__bentoGrid.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a b b b b b b";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.hide-mobile.Spacer-module__1ERWdW__root {
	--height: 48px;
}

div.show-mobile.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.page-module__x5b50W__delegationIllustration {
	position: relative;
	user-select: none;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

svg {
	--icon-color: #9c9da1;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 16px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 12px;
}

span.Text-sc-111816cf-0.dzzsBK {
	width: 76px;
	display: inline-block;
}

div.Flex-module__A66dmG__root {
	gap: 6px;
}

svg {
	--icon-color: var(--color-brand-bg);
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	width: 16px;
	height: 16px;
}

div {
	height: 9px;
	width: 9px;
	background: #EC6A5E;
	border-radius: 50%;
	margin-right: -1px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 12px;
}

span.Text-sc-111816cf-0.dzzsBK {
	width: 76px;
	display: inline-block;
	white-space: nowrap;
	flex-shrink: 0;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	padding-left: 4px;
	gap: 6px;
}

svg {
	--icon-color: var(--color-text-quaternary);
}

span.Text-sc-111816cf-0.kWuiTk {
	white-space: nowrap;
}

span.Text-sc-111816cf-0.cypvFY {
	white-space: nowrap;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 12px;
}

span.Text-sc-111816cf-0.dzzsBK {
	width: 76px;
	display: inline-block;
	white-space: nowrap;
	flex-shrink: 0;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	padding-left: 4px;
	gap: 6px;
}

svg {
	--icon-color: var(--color-text-quaternary);
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

div.Separator-module__ef6YrG__root {
	margin: 13px 0 6px;
}

span.Text-sc-111816cf-0.jNXKas {
	font-size: 12px;
}

p.Text-sc-111816cf-0.cfFSQT {
	font-size: 12px;
	margin-top: 4px;
}

div.Separator-module__ef6YrG__root {
	margin: 9px 0 6px;
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.Flex-module__A66dmG__root {
	gap: 6px;
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

svg {
	--icon-color: var(--color-brand-bg);
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

div.Spacer-module__1ERWdW__root {
	--height: 6px;
}

div.Flex-module__A66dmG__root {
	gap: 12px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

svg.color-override {
	--icon-color: var(--color-yellow);
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

div.Separator-module__ef6YrG__root {
	margin: 13px 0 6px;
}

span.Text-sc-111816cf-0.cypvFY {
	font-size: 12px;
}

p.Text-sc-111816cf-0.cfFSQT {
	font-size: 12px;
	margin-top: 4px;
}

div.Separator-module__ef6YrG__root {
	margin: 10px 0 6px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

svg.color-override {
	--icon-color: #6b6b6b;
}

svg {
	--icon-color: var(--color-text-tertiary);
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

div {
	height: 9px;
	width: 9px;
	border-radius: 50%;
	background: #EC6D60;
}

div.Separator-module__ef6YrG__root {
	margin: 10px 0 6px;
}

span.Text-sc-111816cf-0.jNXKas {
	font-size: 12px;
}

li {
	color: var(--color-text-tertiary);
	margin-bottom: 3px;
}

li {
	color: var(--color-text-tertiary);
}

div.page-module__QbE8ja__dropdownBadge.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	display: inline-flex;
	transform: translatey(3px);
	gap: 4px;
}

svg {
	--icon-color: var(--color-brand-bg);
}

span {
	color: var(--color-text-secondary);
}

div.page-module__QbE8ja__dropdownBadge.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	display: inline-flex;
	gap: 4px;
}

span {
	color: var(--color-text-secondary);
}

button.Button-module__bZ-sGa__root.Button-module__bZ-sGa__variant-secondary.Button-module__bZ-sGa__size-small.Button-module__bZ-sGa__variant {
	width: 100%;
	border-radius: 5px;
	background: #181A1A;
	border-color: #262728;
	margin-top: auto;
	font-size: 12px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center.Flex-module__A66dmG__justify-center {
	gap: 6px;
}

svg {
	height: 14px;
	width: 14px;
	--icon-color: var(--color-text-quaternary);
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.hide-mobile.Spacer-module__1ERWdW__root {
	--height: 72px;
}

div.show-mobile.Spacer-module__1ERWdW__root {
	--height: 32px;
}

img.page-module__x5b50W__maskRight.Image-module__CYTY7q__root {
	color: transparent;
}

div.show-mobile.Spacer-module__1ERWdW__root {
	--height: -40px;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a a a . . . . ." "b b b b b . . . . . . . .";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Eyebrow-module__kZTp2W__eyebrowIndicator {
	background-color: #68CC58;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

svg.page-module__x5b50W__chevronLink {
	--icon-color: currentColor;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

img.inert.page-module__x5b50W__planningHeroImage.Image-module__CYTY7q__root {
	color: transparent;
}

div.page-module__x5b50W__bentoGrid.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a b b b b b b";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.Spacer-module__1ERWdW__root {
	--height: 22px;
}

dl.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 16px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 16px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

div.IconPile__ItemWrapper-sc-cec4b27c-0.etbfoe {
	--mask-overlap: 0.25;
	opacity: 1;
	margin-right: 0px;
	transform: none;
}

div.IconPile__ItemWrapper-sc-cec4b27c-0.etbfoe {
	--mask-overlap: 0.25;
	opacity: 1;
	margin-right: 0px;
	transform: none;
}

div.IconPile__ItemWrapper-sc-cec4b27c-0.etbfoe {
	--mask-overlap: 0.25;
	opacity: 1;
	margin-right: 0px;
	transform: none;
}

div.IconPile__ItemWrapper-sc-cec4b27c-0.etbfoe {
	--mask-overlap: -0.04;
	opacity: 1;
	margin-right: 0px;
	transform: none;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

svg {
	--icon-color: #68CC58;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	margin-top: 2px;
	gap: 16px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

svg {
	overflow: hidden;
	--icon-color: var(--red);
}

path {
	fill: var(--icon-color);
}

div.Spacer-module__1ERWdW__root {
	--height: 8px;
}

div.Spacer-module__1ERWdW__root {
	--height: 12px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

svg {
	overflow: hidden;
	--icon-color: var(--orange);
}

path {
	fill: var(--icon-color);
}

div.Spacer-module__1ERWdW__root {
	--height: 8px;
}

div.Spacer-module__1ERWdW__root {
	--height: 12px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

svg {
	overflow: hidden;
	--icon-color: var(--green);
}

path {
	fill: var(--icon-color);
}

div.Spacer-module__1ERWdW__root {
	--height: 8px;
}

div.Spacer-module__1ERWdW__root {
	--height: 12px;
}

div.Spacer-module__1ERWdW__root {
	--height: 56px;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a b b b b b b b b";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Spacer-module__1ERWdW__root {
	--height: 64px;
}

div.Spacer-module__1ERWdW__root {
	--height: 24px;
}

div.Editor-module__8mxfpG__toggleRoot {
	outline: none;
}

div.Editor-module__8mxfpG__iconContainer {
	--icon-text: rgba(104, 204, 88, 1);
	--icon-bg: rgba(34, 54, 32, 0.5);
}

svg {
	--icon-color: currentColor;
}

div.Spacer-module__1ERWdW__root {
	--height: 32px;
}

span.Editor-module__8mxfpG__remoteSelection {
	--selection-bg: rgba(104, 204, 88, 0.2);
	--selection-border: rgba(44, 144, 28, 1);
}

span.Editor-module__8mxfpG__remoteCursor {
	--cursor-color: rgba(44, 144, 28, 1);
}

div.Spacer-module__1ERWdW__root {
	--height: 12px;
}

span.Editor-module__8mxfpG__remoteCursor {
	--cursor-color: rgba(94, 106, 210, 1);
}

div.Spacer-module__1ERWdW__root {
	--height: 24px;
}

div.Separator-module__ef6YrG__root {
	background: var(--bento-border);
	margin: 48px 0;
}

div.FeatureLockupGrid-module__H4JNxa__featureLockupGrid.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a b b b c c c d d d";
	--grid-areas-tablet: "a a a a b b b b" "c c c c d d d d";
	--grid-areas-mobile: "a a b b" "c c d d";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

svg {
	--icon-color: var(--color-text-secondary);
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

svg {
	--icon-color: var(--color-text-secondary);
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

svg {
	--icon-color: var(--color-text-secondary);
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a a a . . . . ." "b b b b b . . . . . . . .";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Eyebrow-module__kZTp2W__eyebrowIndicator {
	background-color: #D4B144;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

svg.page-module__x5b50W__chevronLink {
	--icon-color: currentColor;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

img.inert.page-module__x5b50W__trackingHeroImage.Image-module__CYTY7q__root {
	color: transparent;
}

div.page-module__x5b50W__bentoGrid.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a b b b b b b";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.Spacer-module__1ERWdW__root {
	--height: 8px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 16px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Cycles-module__XX6nRa__box {
	color: #91959C;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Cycles-module__XX6nRa__box {
	color: #DEB949;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Cycles-module__XX6nRa__box {
	color: #6771C5;
}

div.Spacer-module__1ERWdW__root {
	--height: 20px;
}

div.Spacer-module__1ERWdW__root {
	--height: 48px;
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 6px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 6px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 6px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Spacer-module__1ERWdW__root {
	--height: 64px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

svg {
	--icon-color: currentColor;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

svg {
	--icon-color: currentColor;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

svg {
	--icon-color: currentColor;
}

div.Spacer-module__1ERWdW__root {
	--height: 32px;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a b b b b b b";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Spacer-module__1ERWdW__root {
	--height: 4px;
}

div.Spacer-module__1ERWdW__root {
	--height: 24px;
}

svg {
	--icon-color: #9c9da1;
}

img.inert.Image-module__CYTY7q__root {
	color: transparent;
}

div.Separator-module__ef6YrG__root {
	background: var(--bento-border);
	margin: 24px 0;
}

div.FeatureLockupGrid-module__H4JNxa__featureLockupGrid.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a b b b c c c d d d";
	--grid-areas-tablet: "a a a a b b b b" "c c c c d d d d";
	--grid-areas-mobile: "a a b b" "c c d d";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

svg {
	--icon-color: var(--color-text-secondary);
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

svg {
	--icon-color: var(--color-text-secondary);
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

svg {
	--icon-color: var(--color-text-secondary);
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 8px;
}

span.FeatureLockupGrid-module__H4JNxa__featureLockup.Flex-module__A66dmG__root.Flex-module__A66dmG__align-start {
	gap: 8px;
}

span.Flex-module__A66dmG__root.Flex-module__A66dmG__center {
	min-height: 1lh;
	flex-shrink: 0;
}

svg {
	--icon-color: var(--color-text-secondary);
}

h4.Text-sc-111816cf-0.jNXKas {
	line-height: 24px;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a a . b b b b b";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Eyebrow-module__kZTp2W__eyebrowIndicator {
	background-color: #B59AFF;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

div.Grid-module__HlBHsa__b {
	align-self: end;
}

div.Spacer-module__1ERWdW__root {
	--height: 48px;
}

div.Carousel-module__imM5Ra__variant-inset.Carousel-module__imM5Ra__align-center {
	--Carousel-gap: 8px;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	gap: 20px;
}

div.WorkflowCard-module__yM1mQa__left.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	width: 100%;
	gap: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

div {
	width: 100%;
	height: 1px;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	gap: 20px;
}

div.WorkflowCard-module__yM1mQa__left.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	gap: 20px;
}

div.WorkflowCard-module__yM1mQa__left.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	gap: 20px;
}

div.WorkflowCard-module__yM1mQa__left.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	gap: 20px;
}

div.WorkflowCard-module__yM1mQa__left.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-end.Flex-module__A66dmG__justify-space-between {
	gap: 20px;
}

div.WorkflowCard-module__yM1mQa__left.Flex-module__A66dmG__root.Flex-module__A66dmG__column {
	gap: 4px;
}

svg {
	--icon-color: #9c9da1;
}

div.hide-tablet.Spacer-module__1ERWdW__root {
	--height: 48px;
}

div.hide-tablet.show-js.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center.Flex-module__A66dmG__justify-center {
	gap: 8px;
}

svg {
	--icon-color: #9c9da1;
}

svg {
	--icon-color: #9c9da1;
}

div.Grid-module__HlBHsa__root {
	--grid-areas-default: "a a a a a . . . . . ." "b b b b b . . . . . ." "c c c c c . . . . . .";
	--grid-areas-tablet: "a a a a a a a a" "b b b b b b b b" "c c c c c c c c";
	--grid-areas-mobile: "a a a a" "b b b b" "c c c c";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 8px;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

div.Spacer-module__1ERWdW__root {
	--height: 24px;
}

div.Spacer-module__1ERWdW__root {
	--height: 16px;
}

div.Separator-module__ef6YrG__root {
	background: var(--bento-border);
}

div.Spacer-module__1ERWdW__root {
	--height: 24px;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 6px;
}

svg.page-module__x5b50W__chevronLink {
	--icon-color: currentColor;
}

div.Spacer-module__1ERWdW__root {
	--height: 40px;
}

div.Separator-module__ef6YrG__root {
	background: var(--bento-border);
}

div.Grid-module__HlBHsa__root {
	justify-content: space-around;
	gap: 8px;
	grid-template-columns: repeat(5, auto);
	grid-template-rows: repeat(1, auto);
	grid-template-areas: unset;
}

div.page-module__x5b50W__badge.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center.Flex-module__A66dmG__column {
	gap: 16px;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

div.Separator-module__ef6YrG__root {
	background: var(--bento-border);
}

div.page-module__x5b50W__badge.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center.Flex-module__A66dmG__column {
	gap: 16px;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

div.Separator-module__ef6YrG__root {
	background: var(--bento-border);
}

div.page-module__x5b50W__badge.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center.Flex-module__A66dmG__column {
	gap: 16px;
}

img.Image-module__CYTY7q__root {
	color: transparent;
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-center {
	gap: 4px;
}

div.Grid-module__HlBHsa__root {
	align-items: center;
	--grid-areas-default: "a a a a a a a a b b b b";
	--grid-areas-tablet: "a a a a b b b b";
	--grid-areas-mobile: "a a a a" "b b b b";
}

div.Flex-module__A66dmG__root.Flex-module__A66dmG__align-flex-start.Flex-module__A66dmG__justify-space-between.Flex-module__A66dmG__column {
	height: 100%;
}

svg {
	display: none;
}
/** End Project Wallace extracted inline styles */