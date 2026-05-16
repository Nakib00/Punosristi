---
name: Punosristi Eco-Tech
colors:
  surface: '#f8faf8'
  surface-dim: '#d8dad9'
  surface-bright: '#f8faf8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f2'
  surface-container: '#eceeec'
  surface-container-high: '#e6e9e7'
  surface-container-highest: '#e1e3e1'
  on-surface: '#191c1b'
  on-surface-variant: '#40493f'
  inverse-surface: '#2e3130'
  inverse-on-surface: '#eff1ef'
  outline: '#717a6f'
  outline-variant: '#c0c9bc'
  surface-tint: '#2a6b37'
  primary: '#004317'
  on-primary: '#ffffff'
  primary-container: '#1a5c2a'
  on-primary-container: '#8fd394'
  inverse-primary: '#93d697'
  secondary: '#006e1c'
  on-secondary: '#ffffff'
  secondary-container: '#91f78e'
  on-secondary-container: '#00731e'
  tertiary: '#493617'
  on-tertiary: '#ffffff'
  tertiary-container: '#624c2c'
  on-tertiary-container: '#dcbe95'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#aef3b1'
  primary-fixed-dim: '#93d697'
  on-primary-fixed: '#002108'
  on-primary-fixed-variant: '#0c5221'
  secondary-fixed: '#94f990'
  secondary-fixed-dim: '#78dc77'
  on-secondary-fixed: '#002204'
  on-secondary-fixed-variant: '#005313'
  tertiary-fixed: '#feddb3'
  tertiary-fixed-dim: '#e1c299'
  on-tertiary-fixed: '#281801'
  on-tertiary-fixed-variant: '#584324'
  background: '#f8faf8'
  on-background: '#191c1b'
  surface-variant: '#e1e3e1'
typography:
  headline-xl:
    fontFamily: Poppins
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Poppins
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Poppins
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  body-md:
    fontFamily: Poppins
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Poppins
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  stat-display:
    fontFamily: Poppins
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 80px
  container-max: 1280px
---

## Brand & Style
The brand personality is rooted in environmental stewardship, combining the reliability of modern technology with the organic warmth of nature. It aims to evoke an emotional response of hope and responsibility, positioning the startup as a professional yet approachable leader in the Bangladeshi eco-tech space.

The design style is a blend of **Minimalism** and **Glassmorphism**. It utilizes heavy whitespace to allow high-contrast environmental photography to breathe, while employing translucent, frosted-glass layers to represent the clarity and transparency of green technology. Subtle organic flourishes, such as leaf-inspired motifs and recycling-themed vector details, provide a distinct decorative layer without cluttering the interface.

## Colors
The palette is led by **Deep Forest Green**, representing stability and the depth of nature. **Mint Green** serves as the primary action color, providing a fresh, high-visibility contrast. **Warm Earth Tones** (Tan/Sand) are used for secondary accents, grounding the digital experience in physical reality.

The background is a soft, off-white "Eco-Neutral" (#F9FBF9) to reduce eye strain and provide a more natural feel than pure white. High-contrast photography should use these brand colors as anchors—for example, pairing a desaturated, grey-toned "polluted" image against a vibrantly saturated "clean" image featuring the primary forest green.

## Typography
The system uses **Poppins** exclusively to ensure a clean, geometric, yet friendly aesthetic. Headings are set in Bold (700) to convey authority and impact, particularly for environmental messaging. Body text uses Regular (400) for high legibility in dense information blocks.

For large hero sections, use `headline-xl` with tight letter spacing to create a sense of urgency and importance. A specialized `stat-display` style is reserved for key ecological metrics within stat cards, ensuring data is the focal point of the user's attention.

## Layout & Spacing
The layout follows a **Fluid Grid** model with a 12-column structure on desktop and a 4-column structure on mobile. A generous 80px margin on desktop ensures the content feels curated and premium, rather than crowded.

Spacing follows an 8px base unit. Hero sections should utilize "Negative Space" intentionally, placing text against clean areas of high-contrast photography. Step flows are arranged horizontally on desktop to suggest progress and momentum, reflowing to a vertical stack on mobile devices.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and **Tonal Layers**. Instead of traditional heavy shadows, the system uses "Backdrop Blurs" (12px - 20px) on white semi-transparent surfaces (opacity 60-80%). This creates a "frosted glass" effect that allows the underlying nature photography to peak through.

Interactive elements use a soft, tinted ambient shadow (Primary Green at 10% opacity) to signify elevation without breaking the clean, modern aesthetic. Content "depth" is tiered:
1. **Base:** Photography or neutral background.
2. **Surface:** Frosted glass containers for cards and modules.
3. **Primary:** Solid primary color buttons and active status indicators.

## Shapes
The shape language is **Rounded**, reflecting the soft curves found in the natural world. Standard UI components like buttons and input fields use a 0.5rem radius. 

Larger containers, such as frosted-glass cards and hero image masks, use `rounded-xl` (1.5rem) to emphasize a friendly, non-industrial feel. Decorative elements—like leaf icons or recycling path vectors—should utilize organic, non-geometric curves to contrast against the structured layout.

## Components
### Hero Sections
Large-scale components featuring high-contrast imagery. Text should be left-aligned with a primary call-to-action button. Use a subtle leaf-pattern overlay at 5% opacity to add texture to solid color backgrounds.

### Frosted-Glass Cards
Used for content blocks. These require a `backdrop-filter: blur(16px)` and a thin, 1px white border at 20% opacity to define the edges against complex backgrounds.

### Stat Cards
Clean, minimal cards with a primary focus on numerical data. The number should use the `stat-display` type style in Forest Green, accompanied by a small trend icon (e.g., a green leaf for growth).

### Horizontal Step Flows
A linear progression component for explaining eco-processes. Connected by a thin mint-green dashed line, each step features a circular icon container and a brief descriptor.

### Buttons & Inputs
Buttons are solid Mint (#4CAF50) with white text for maximum contrast. Secondary buttons use a Forest Green outline. Inputs use the "Eco-Neutral" background with a 1px border that turns Mint on focus.