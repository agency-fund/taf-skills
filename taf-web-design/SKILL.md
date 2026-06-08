---
name: taf-web-design
description: >
  The Agency Fund (TAF) web-design system for shipping on-brand HTML — both research-artifact
  web pages and presentation slide decks that run in the browser. Use whenever a researcher,
  program officer, or product manager at The Agency Fund asks you to "make a web page",
  "publish this finding", "turn this report into a site", "build a landing page", "wrap this
  dashboard in a page", "share this as HTML", OR to "make a slide deck", "build a talk",
  "make a presentation", "build a lecture/workshop deck", or wants "the usual deck" / "my
  slide style" rendered as HTML slides (1920x1080, animated, keyboard-navigable, PDF-exportable)
  rather than PPTX or Google Slides. Also use when the request mentions agency.fund, TAF, or
  Agentic Workflows Club and the deliverable is HTML/CSS — whether a page or a deck. Pairs with
  `agency-fund-design` (the parent brand system) but is opinionated for web output.
user-invocable: true
---

# taf-web-design

One TAF brand, two web deliverables. This skill ships both:

- **Mode A — web pages.** Single-page HTML artifacts: research reports, briefing memos,
  case studies, insight dashboards, collection landing pages. Long-form, responsive,
  vibe-codeable. Files at the top level of this skill (`web-design-rules.md`,
  `components.md`, `tokens.css`, `templates/`).
- **Mode B — slide decks on web.** Animated, multi-file HTML decks — one 1920×1080 HTML
  file per slide plus a deck shell with an overview wall, keyboard navigation, smooth
  transitions, click-to-explore interactive demos, vector PDF export, and one-command
  GitHub Pages hosting. Everything for this mode lives under `slides/`.

Both modes descend from the same brand (The Agency Fund / Agentic Workflows Club): navy +
gold, Montserrat, generous whitespace, restraint. The look is identical; only the output
shape and the motion budget differ.

## Routing — which mode?

| The user wants… | Mode | Start with |
|---|---|---|
| a web page, site, landing page, report, dashboard, "publish this as HTML" | **A — pages** | `README.md` → `web-design-rules.md`, then pick a `templates/*.html` |
| a slide deck, talk, lecture, workshop, presentation, "the usual deck", 1920×1080 slides | **B — slides** | `slides/slide-design.md`, then `slides/references/workflow.md` |

If it's genuinely ambiguous ("turn this into something I can present"), ask: a **scrolling
web page** or a **slide deck**? They diverge on layout (flow vs. fixed 1920×1080 canvas) and
motion (near-static vs. staged entrance animations), so the answer changes everything
downstream. If the user is making a deck destined for **PowerPoint or Google Slides** rather
than HTML, this skill is the wrong tool — defer to `agency-fund-design`.

## The shared non-negotiables (both modes)

1. **Gold is action. Navy is gravity.** Gold (`#F1B505`) is reserved for verbs, CTAs, gold
   bullets, accent words in a headline, key numbers. Navy (`#003366` / `#0B2341`) is reserved
   for nouns, logo, dark panels, section labels, the weight of the page. Never a gold
   paragraph. Never a navy CTA — use the dark button instead. One or two gold accent words per
   headline, never a gold sentence.
2. **Montserrat only. Two colors. Whitespace.** No second typeface. No third color (the one
   exception: link blue `#6699CC` for inline web links). No gradients (the lone exception is a
   navy hero/divider overlay), glassmorphism, decorative animation, or emoji. Restraint is the
   brand.
3. **No italics, ever.** No `<em>`, no `font-style: italic`. Use `<strong>` or a gold accent
   word for emphasis.
4. **No em dashes, ever.** Commas, colons, periods, or parentheses instead. Target zero.
5. **Documentary photography only.** Real people, natural light. Never stock, never
   AI-generated faces, never illustration. If no real photo is available, use a full-bleed
   navy panel with a gold accent word and skip the image entirely.
6. **Numbers as evidence.** Real numbers stated plainly. "150 grantees." "$38M." Large-format
   numbers in 900-weight Montserrat navy, with the unit/label below in muted gray.

---

# Mode A — web pages

The web companion for turning a research artifact into a presentable single-page HTML
deliverable. **Optimize for vibe-coding**: opinionated templates the user iterates on
conversationally ("make the hero punchier", "add a citations footer"), not a component
library to be assembled from primitives.

Read `README.md` for orientation, then `web-design-rules.md` for the full rules. The visual
token reference lives in `tokens.css` — inline it (or link it) and the system is live. Five
page templates live in `templates/`; pick the closest match and edit, don't build from scratch.

## Web-only rules

- **Eyebrow above every major section** — `12px · 600 · UPPERCASE · 0.12em tracking ·
  --color-ink-muted`. Without it, a Montserrat heading stops feeling like TAF.
- **80px between major sections** (`--space-4xl`). When in doubt, add more. The brand breathes.
- **Content column caps at 1200px.** Long-form prose caps tighter, at 70ch (≈ 680px).
- **One H1 per page**, always paired with an eyebrow above it.
- **12px radius on cards and photos.** Pill buttons. 6px on form inputs. Never a sharp 0px corner.
- **Navy-tinted shadows only** (`hsl(210 50% 20% / 0.06–0.12)`). Never `rgba(0,0,0,…)`.
- **Motion budget:** `150ms` color transitions and `250ms` shadow transitions only. No
  scroll-triggered animation, no parallax.

## How to invoke Mode A

If the user invokes the skill without specifics, ask **what artifact and which template**:

1. **research-report.html** — long-form report with hero, summary, sections, methodology,
   references.
2. **briefing-memo.html** — one-pager exec brief; eyebrow, headline, three key findings,
   recommendation.
3. **case-study.html** — narrative case study with photo hero and outcome panel.
4. **insight-dashboard.html** — data-forward overview; metric cards, trend charts (Chart.js
   via CDN), short narrative.
5. **artifact-index.html** — collection landing page linking multiple artifacts (cards grid).

Then ask for the **three or four content slots** the template needs (eyebrow, headline, body,
numbers) and produce a complete single-file HTML page. Inline the `tokens.css` contents or
link to it — do not split into multiple files unless the user asks for a multi-page site.

## Critical things to never do (web)

- Don't introduce a second typeface ("just for the body" — no).
- Don't tint gold to suggest hover; use `--color-action-hover` (the warmer `#ECAA00`).
- Don't gold the entire headline. **One or two words.**
- Don't combine navy backgrounds with gold backgrounds in adjacent blocks — they fight.
  Alternate with `--color-surface` or `--color-surface-subtle`.
- Don't drop in a chart library that brings its own theme. Override Chart.js defaults to use
  Montserrat, `--color-gravity` for primary series, and `--color-action` only for the highlight series.

## QA before shipping a page

- One H1, paired with an eyebrow above it
- Every major section has an eyebrow
- Gold appears only on: CTAs, accent words in headlines, gold bullets, large metric numbers
- No italics anywhere, no emoji, no gradients (except the navy hero overlay)
- Section spacing is 80px+
- Photos and cards have `border-radius: 12px`; buttons are pill-shaped (`border-radius: 9999px`)
- Shadows render `hsl(210 50% 20% / …)`, not `rgba(0,0,0,…)`
- Body text caps near 70ch for readability
- Logo (if used) is top-right at ~120px wide on hero, or top-left in nav
- Contrast passes WCAG AA; focus-visible outlines work; reduced-motion respected
- No second typeface has snuck in via a chart, code block, or CDN

---

# Mode B — slide decks on web

A deck is a folder of standalone 1920×1080 HTML slides plus a shell (`index.html`) that gives
you an overview wall, keyboard navigation, smooth transitions, and print-to-PDF. The look is
the same navy + gold + Montserrat, restrained and editorial, but with deliberate motion and
interactive demos that the page mode does not use.

Everything for this mode lives under **`slides/`**:

| Path | What |
|------|------|
| `slides/slide-design.md` | Mode-B orientation: the non-negotiables, quick start, file map |
| `slides/references/design-system.md` | colors, type, components, anti-slop rules, writing voice |
| `slides/references/slide-archetypes.md` | the slide types and how to build/animate each |
| `slides/references/workflow.md` | end-to-end build, verification, and hosting workflow |
| `slides/assets/taf.css` | color/type tokens + components (`.slide` locks 1920×1080) |
| `slides/assets/anim.css`, `slides/assets/anim.js` | entrance-animation framework (`data-reveal`, `data-grow-w/h`, `.hoverable`, `?static=1`) |
| `slides/assets/fonts.css` + `slides/assets/fonts/montserrat-var.woff2` | self-hosted Montserrat (no swap-flash, works offline) |
| `slides/assets/deck_index.html` | the deck shell: overview wall on an animated tech background, keyboard nav, transitions, print-to-PDF. Copy to `index.html`, edit `DECK_MANIFEST` |
| `slides/assets/slide-template-content.html` | starter light content slide (with the required bottom scripts) |
| `slides/assets/slide-template-divider.html` | starter dark section divider |
| `slides/assets/deploy-pages.yml`, `slides/assets/nojekyll.txt` | GitHub Pages auto-deploy |
| `slides/scripts/shoot.mjs` | screenshot every slide at 1920×1080, flag overflow + JS/console errors |
| `slides/scripts/export_deck_pdf.mjs` | render the deck to a vector, text-selectable PDF |

## Mode-B non-negotiables (in addition to the shared brand rules above)

1. **Multi-file architecture.** One HTML file per slide in `slides/`, sharing
   `slides/shared/{taf.css, anim.css, anim.js, fonts.css, fonts/}`. The root `index.html` is
   the deck shell; its `DECK_MANIFEST` lists every slide.
2. **Self-hosted font, animated reveals, click-only interactivity.** These are wired through
   the shared assets and a small per-slide script — keep that script verbatim. Arrow keys,
   Space, digits, Home/End, Esc, and P are reserved by the deck shell.
3. **Verify visually.** Screenshot every slide (animated + `?static=1`), check overflow and
   console errors, before calling it done.

## Quick start (Mode B)

1. Read `slides/slide-design.md`, then `slides/references/workflow.md` (build process) and
   `slides/references/design-system.md` (look + voice). For per-slide layout patterns, read
   `slides/references/slide-archetypes.md`.
2. Scaffold: copy `slides/assets/{taf.css,anim.css,anim.js,fonts.css}` and
   `slides/assets/fonts/` into the project's `slides/shared/`; copy
   `slides/assets/deck_index.html` to `index.html` and edit its `DECK_MANIFEST`.
3. Write the slide copy first (full sentences, verified facts), then build slides from
   `slides/assets/slide-template-content.html` and `slides/assets/slide-template-divider.html`.
   For >5 slides, do a 2-slide showcase to fix the grammar before scaling.
4. Verify with `slides/scripts/shoot.mjs`, export with `slides/scripts/export_deck_pdf.mjs`,
   and (optionally) host via `slides/assets/deploy-pages.yml` + `slides/assets/nojekyll.txt`.

### Tooling note

The scripts need `npm i playwright pdf-lib` and a one-time `npx playwright install chromium`.
The deck itself has no runtime dependencies: fonts and logos are local and all paths are
relative, so it opens by double-click, works offline, and hosts on any static server from a
subpath.

---

## Relationship to the parent skill

This skill **extends** `agency-fund-design`. Where the parent system covers the brand at large
(decks for PowerPoint/Google Slides, marks, sub-brands, the AWC variant), this skill narrows in
on **web output** and adds the web-specific patterns the parent doesn't: long-form report
layout, sticky table of contents, citation footnotes, KPI cards, Chart.js theming, responsive
breakpoints (Mode A), and a complete animated HTML-slide deck system (Mode B). For decks that
must end up as PPTX or Google Slides, defer to `agency-fund-design`.
