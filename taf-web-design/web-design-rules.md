# Web Design Rules — TAF Research Artifacts

> The complete set of rules for adapting The Agency Fund brand to web output.
> Derived from the parent design system (`agency-fund-design`), informed by
> Claude Design's documented design-system practice, and tuned for the
> research-artifact use case.

These rules are stricter than a generic web design system on purpose. The
fewer choices left to make, the more consistent the output.

---

## 1. Color

### Use

- **Body text** → `--color-ink` (#212529)
- **Secondary text** → `--color-ink-secondary` (#495057)
- **Eyebrows, captions, muted UI** → `--color-ink-muted` (#868E96)
- **Page background** → `--color-surface` (#FFFFFF)
- **Subtle background panels** → `--color-surface-subtle` (#F8F9FA)
- **Dark panels / hero overlays / heavy sections** → `--color-surface-navy` (#003366)
  or `--color-surface-navy-deep` (#0B2341)
- **Primary CTA, accent words in headlines, key numbers** → `--color-action` (#F1B505)
- **Borders** → `--color-border` (#DEE2E6)
- **Links** → `--color-link` (#6699CC), underlined

### Don't use

- A third hue. No teal, no green, no red. (Functional reds — error states —
  are out of scope for research artifacts.)
- Gold for body text. Gold is for verbs, CTAs, accent words. Gold paragraphs
  fail contrast and look like an alert.
- Pure black for shadows or borders. Use `--color-border` for borders and
  the navy-tinted `--taf-shadow-*` for shadows.
- Adjacent navy and gold blocks. Always separate by a neutral block.

---

## 2. Typography

### One typeface

**Montserrat.** Loaded via Google Fonts or self-hosted. System fallbacks in
the stack so the page never breaks if Montserrat fails to load.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
```

### Scale (fluid via `clamp()`)

| Token              | Min      | Max      | Use                          |
|--------------------|----------|----------|------------------------------|
| `--fs-fluid-eyebrow` | 12px   | 13.6px   | Eyebrow labels               |
| `--fs-fluid-body`    | 16px   | 17px     | Body                         |
| `--fs-fluid-lead`    | 18px   | 21px     | Lead paragraph after H1      |
| `--fs-fluid-h3`      | 24px   | 32px     | Subsection title             |
| `--fs-fluid-h2`      | 32px   | 48px     | Section title                |
| `--fs-fluid-h1`      | 44px   | 72px     | Page title                   |
| `--fs-fluid-hero`    | 48px   | 88px     | Poster hero headline         |
| `--fs-fluid-numeric` | 40px   | 72px     | Large metric numbers         |

### Weights

- **400** — body
- **500** — UI labels, button text, chip text
- **600** — eyebrows, subheadings, semibold emphasis
- **700** — H3, H4, card titles, navigation
- **800** — H2, section headlines
- **900** — H1, hero headlines, large metric numbers

### Rules

- **One H1 per page.** Always paired with an eyebrow above it.
- **Body line-length** caps at 70ch (~ 680px) for readability.
- **Body line-height** is 1.5. **Large-body** is 1.7. **Headlines** are 1.15–1.3.
- **Letter-spacing** is tight (`-0.02em`) on H1/hero only; normal elsewhere;
  eyebrow uses `0.12em` tracking, uppercase.
- **No italics.** Replace `<em>` with `<strong>` or a gold accent word.
- **Case.** Sentence case for body. Title Case for page titles, CTAs,
  section headlines. UPPERCASE for eyebrows.

---

## 3. Spacing

**4px base grid.** Every gap, padding, and margin is a multiple of 4px.

- **8px / 12px** — within a component (chip padding, button x-padding tight)
- **16px / 24px** — between elements within a section (card padding, list gap)
- **48px / 64px** — between subsections within a major section
- **80px** — between major sections. **This is the breathing rule.**
- **96px / 128px** — only for hero separations on landing pages

When you doubt the spacing, **add more, not less**. Cramped pages feel
off-brand.

---

## 4. Layout

- **Max content width** 1200px. Set on a `.container` wrapper.
- **Prose width** 70ch (≈ 680px). Apply to long-form text columns.
- **Padding-x** on the container is 24px on mobile, 32px on desktop.
- **Sections** wrap with `<section class="section">` and a 80px vertical
  padding via `--space-4xl`.
- **Grids** use CSS grid with `auto-fit, minmax(N, 1fr)` so they collapse
  responsively without media queries. Avoid hand-picked breakpoints
  except for layout-level changes (sidebar collapse, etc.).

### Six layout patterns (carried from the deck system)

1. **Poster hero** — Full-bleed photo + navy gradient overlay + bottom-aligned
   eyebrow/headline/CTA. One gold accent word in the headline.
2. **Split section header** — Eyebrow + H2 on the left, supporting paragraph
   on the right. Most common section intro.
3. **Capability list** — Vertical list with alternating navy/gold dots, one
   item per line, 1px bottom border between items.
4. **Content cards** — Eyebrow + title + body + optional CTA. 1px border,
   12px radius, navy-tinted hover shadow.
5. **Metric panel** — Three or four large numbers across, each with a small
   eyebrow label below. Usually navy background; numbers in white or gold.
6. **Funding tier / chip shelf** — Navy label block on the left, flex-wrap of
   neutral pill chips on the right.

---

## 5. Components

Each follows the same pattern: minimum chrome, semantic colors, navy-tinted
hover state, no decorative animation.

### Button

Pill-shape. Three variants — primary (gold), dark (navy), outline. Use
`.btn .btn--primary`, `.btn .btn--dark`, `.btn .btn--outline`. Always include
a focus-visible outline (handled globally in `tokens.css`).

### Eyebrow

`<span class="eyebrow">EVALUATION · MATERNAL HEALTH</span>`. Always lives
**above** the headline it labels, never after.

### Card

`<article class="card">` with `<span class="eyebrow">`, `<h3>`, `<p>`,
optional CTA. 12px radius, 1px border, shadow on hover.

### Metric

`<div class="metric"><div class="metric__value">150</div><div class="metric__label">Grantees</div></div>`.
Large number on top in `--fw-hero` Montserrat (or gold on a navy panel),
small uppercase label below.

### Capability list

`<ul class="capability-list">` with `<li><span class="bullet"></span>Text</li>`.
The bullets alternate navy/gold automatically via `:nth-child`.

### Chip

`<span class="chip">Grantee Name</span>`. Pill, neutral background, 1px
border. Use for grantee shelves, tag groups.

### Pull quote

`<blockquote class="pull-quote">"…" <cite>Source · Role</cite></blockquote>`.
Gold left bar, larger type, navy ink, uppercase tracked source.

### Footnote / citation

Inline number `<sup><a href="#fn1">1</a></sup>` linking to an `<ol
class="footnote-list">` at the bottom. APA-style citations preferred.

---

## 6. Photography

- **Documentary only.** Real people, natural light. Never stock, never
  AI-generated faces, never illustration.
- **12px radius** on every photo (matches cards).
- **Full-bleed hero photos** carry a navy linear-gradient overlay
  (`linear-gradient(180deg, transparent 40%, rgba(11,35,65,0.75) 100%)`)
  so white Montserrat reads clearly at the bottom.
- **If no photo exists**, use a navy panel with a gold accent word in the
  headline. Never substitute a generic stock photo or an icon.

---

## 7. Charts (Chart.js theming)

When using Chart.js via CDN, override defaults to fit the system:

```js
Chart.defaults.font.family = "'Montserrat', sans-serif";
Chart.defaults.font.size = 13;
Chart.defaults.color = '#495057';
Chart.defaults.borderColor = '#DEE2E6';
// Primary series: navy #003366
// Highlight series (one only): gold #F1B505
// Neutral comparators: neutral-400 #CED4DA
```

Charts are illustrative, not decorative. Avoid 3D, drop shadows, area
gradients, or multiple highlight colors. One chart per section, sized to fit
the prose column.

---

## 8. Motion

- **150ms** for color transitions (buttons, links).
- **250ms** for shadow transitions (cards on hover).
- **No** scroll parallax. **No** entrance animations. **No** bouncing.
- Respect `prefers-reduced-motion` — handled in `tokens.css` automatically.

---

## 9. Accessibility (WCAG 2.1 AA)

- Body text contrast: 4.5:1 minimum. Navy on white is 12.6:1 (AAA).
- Large text (≥ 24px): 3:1 minimum. White on gold is 1.85:1 — **never use
  gold as a background for white text.** Gold backgrounds take navy or
  near-black ink.
- Focus-visible outlines on every interactive element. 2px navy.
- Heading levels follow document order — never skip from H1 to H4 for
  styling reasons; use class names instead.
- All images need meaningful `alt=""` (or `alt=""` empty if purely
  decorative).
- All links carry visible text — no "click here." Underline links in
  body copy.

---

## 10. Responsive

- **Mobile-first.** Default styles target ~ 360px width.
- **Breakpoints** when needed: 640 / 768 / 1024 / 1280. Available as CSS
  custom properties (`--taf-bp-*`).
- **Most layout** uses `grid-template-columns: repeat(auto-fit, minmax(…))`,
  which collapses without media queries.
- **Type fluidity** via `clamp()` removes the need for media queries on
  most headings.
- **Hero photos** crop with `object-fit: cover; object-position: center;`
  and shrink to 60vh on mobile, 80vh on desktop.

---

## 11. Performance

- **One font** — Montserrat. Preload only the weights actually used
  (400, 600, 700, 800, 900). Skip italic — there are no italics.
- **No JS framework.** Static HTML + Chart.js CDN (only on dashboard
  templates) is enough for every research artifact in this skill.
- **Inline `tokens.css`** in `<style>` for single-file artifacts. Link
  externally only if shipping a multi-page site.
- **Optimize photos** before embedding — 1600px max width, WebP or JPEG
  at quality 80.

---

## 12. Anti-patterns (the "stop and look at agency.fund" check)

If you feel an urge to do any of the following, stop:

- A second sans-serif font, even for body, even "just for code"
- A teal or green accent "to make it more friendly"
- A gradient on the hero
- Glassmorphism, neumorphism, or any other recent design fad
- Scroll-triggered animations or parallax
- Decorative SVG flourishes that aren't the sail mark or alternating dots
- Emoji
- A "Hello 👋" greeting
- Italic anywhere
- Pure-black shadows
- Stock photography
- AI-generated photos of people
- A startup-style "We're revolutionizing X" hero copy

The brand earns trust by **being restrained**. The page should feel like a
research institution that happens to publish well, not a startup chasing
attention.

---

## 13. Final QA before shipping

Run this checklist on every page:

- [ ] One H1, paired with an eyebrow above
- [ ] Every major section has its own eyebrow
- [ ] Gold appears only on CTAs, accent words, gold bullets, and large metric numbers
- [ ] Body line-length ≤ 70ch
- [ ] 80px between major sections
- [ ] 12px radius on cards and photos
- [ ] Pill buttons (`border-radius: 9999px`)
- [ ] Navy-tinted shadows only (`hsl(210 50% 20% / …)`)
- [ ] No italics, no emoji, no gradients (except the navy hero overlay)
- [ ] Photos are documentary or no photo at all (navy panel substitute)
- [ ] Contrast passes WCAG AA
- [ ] Focus-visible outlines work
- [ ] Reduced-motion respected
- [ ] No second typeface has snuck in via a chart or code block
