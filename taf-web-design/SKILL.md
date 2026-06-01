---
name: taf-web-design
description: >
  The Agency Fund (TAF) web-design system for turning research artifacts into presentable,
  on-brand websites and single-page HTML deliverables. Use whenever a researcher, program officer,
  or product manager at The Agency Fund asks you to "make a web page", "publish this finding",
  "turn this report into a site", "build a landing page", "wrap this dashboard in a page",
  "share this as HTML", or otherwise wants to ship a research artifact as a vibe-coded web
  interface. Also use when the request mentions agency.fund, TAF, or Agentic Workflows Club
  and the deliverable is HTML/CSS — not a slide deck. Pairs with `agency-fund-design`
  (the parent brand system) but is opinionated for web.
user-invocable: true
---

Read `README.md` for the orientation, then `web-design-rules.md` for the rules. The full
visual token reference lives in `tokens.css` — import it as-is and the system is live.
Five page templates live in `templates/`; pick the closest match and edit, don't
build from scratch.

## The two non-negotiables (carried from the parent brand)

1. **Gold is action. Navy is gravity.** Gold (`#F1B505`) is reserved for verbs, CTAs,
   gold bullets, accent words in a headline. Navy (`#003366` / `#0B2341`) is reserved
   for nouns, logo, dark panels, section labels, the weight of the page. Never a
   gold paragraph. Never a navy CTA — use the dark button instead.
2. **Montserrat only. Two colors. Whitespace.** No second typeface. No third color.
   No gradients, glassmorphism, decorative animation, or emoji. The brand earns
   trust by being plainspoken and confident. Restraint is the brand.

## Web-only rules (carried over from the deck system and adapted)

- **Eyebrow above every major section** — `12px · 600 · UPPERCASE · 0.12em tracking ·
  --color-ink-muted`. Without it, a Montserrat heading stops feeling like TAF.
- **80px between major sections** (`--space-4xl`). When in doubt, add more.
  The brand breathes; cramped pages feel off-brand.
- **Content column caps at 1200px.** Long-form prose caps tighter, at 70ch (≈ 680px),
  for readability.
- **One H1 per page**, always paired with an eyebrow above it.
- **12px radius on cards and photos.** Pill buttons. 6px on form inputs. Never a
  square card with a sharp 0px corner.
- **Navy-tinted shadows only** (`hsl(210 50% 20% / 0.06–0.12)`). Never `rgba(0,0,0,…)`.
- **Documentary photography only.** Real people, natural light. Never stock, never
  AI-generated faces, never illustration. If no real photo is available, use a
  full-bleed navy panel with a gold accent word and skip the image entirely.
- **No italics. Ever.** No `<em>`, no `font-style: italic`. Use `<strong>` or a
  gold accent word for emphasis.
- **Numbers as evidence.** Real numbers stated plainly. "150 grantees." "$38M."
  Render large-format numbers in `--fw-hero` (900) Montserrat in `--color-ink-navy`,
  with the unit/label below in muted gray.

## What this skill is for (audience)

Researchers and PMs at TAF turning a research artifact — a brief, a case study,
a dataset, a methodology, an evaluation finding — into a presentable web page.
**Optimize for vibe-coding**: opinionated templates the user can iterate on
conversationally ("make the hero punchier", "add a citations footer"), not a
component library to be assembled from primitives.

## How to invoke this skill

If the user invokes the skill without specifics, ask **what artifact and which
template**:

1. **research-report.html** — long-form report with hero, summary, sections,
   methodology, references.
2. **briefing-memo.html** — one-pager exec brief; eyebrow, headline, three key
   findings, recommendation.
3. **case-study.html** — narrative case study with photo hero and outcome panel.
4. **insight-dashboard.html** — data-forward overview; metric cards, trend
   charts (Chart.js via CDN), short narrative.
5. **artifact-index.html** — collection landing page linking multiple artifacts
   (cards grid).

Then ask for the **three or four content slots** the template needs (eyebrow,
headline, body, numbers) and produce a complete single-file HTML page. Inline
the tokens.css contents or link to it — do not split into multiple files unless
the user asks for a multi-page site.

## Critical things to never do (carried over from the AWC sub-brand notes)

- Don't introduce a second typeface ("just for the body" — no).
- Don't tint gold to suggest hover; use `--color-action-hover` (the warmer
  `#ECAA00`).
- Don't gold the entire headline. **One or two words.**
- Don't combine navy backgrounds with gold backgrounds in adjacent blocks —
  they will fight. Alternate with `--color-surface` or `--color-surface-subtle`.
- Don't drop in a chart library that brings its own theme. Override Chart.js
  defaults to use Montserrat, `--color-gravity` for primary series, and
  `--color-action` only for the highlight series.
- Don't add scroll-triggered animations or parallax. `150ms` color
  transitions and `250ms` shadow transitions are the only motion.

## QA before shipping

Before handing a page to the user, check:

- One H1, paired with an eyebrow above it
- Every major section has an eyebrow
- Gold appears only on: CTAs, the accent word in headlines, gold bullets, the
  large numbers in metric callouts
- No italics anywhere, no emoji, no gradients
- Section spacing is 80px+
- Photos and cards have `border-radius: 12px`
- Buttons are pill-shaped (`border-radius: 9999px`)
- Shadows render `hsl(210 50% 20% / …)`, not `rgba(0,0,0,…)`
- Body text caps near 70ch for readability
- Logo (if used) is top-right at ~120px wide on hero, or top-left in nav
- No second typeface has snuck in via a chart, code block, or CDN

## Relationship to the parent skill

This skill **extends** `agency-fund-design`. Where the parent system covers
the brand at large (decks, marks, sub-brands, the AWC variant), this skill
narrows in on **web output for research artifacts** and adds the web-specific
patterns the parent doesn't: long-form report layout, sticky table of contents,
citation footnotes, KPI cards, Chart.js theming, responsive breakpoints.

If the user is making a deck, defer to `agency-fund-design` instead.
