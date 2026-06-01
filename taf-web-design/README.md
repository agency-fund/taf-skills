# TAF Web Design — Research Artifact Skill

> A vibe-codeable web design system for The Agency Fund. Turn research briefs,
> case studies, dashboards, and findings into presentable single-page HTML —
> on-brand, accessible, and ready to share.

This skill is the **web companion** to `agency-fund-design`. The parent skill
covers the whole brand (decks, marks, sub-brands). This one is narrower: it
exists so a researcher or PM can say "publish this finding as a web page" and
get a polished, on-brand page back in one shot.

---

## Who this is for

- **Researchers** turning an evaluation finding, methodology brief, or
  literature review into a shareable web page.
- **Program officers** publishing a case study or grantee story.
- **Product managers** wrapping a dashboard or KPI snapshot in a presentable
  page for a stakeholder.
- **Anyone at TAF** who wants their artifact to *look like it came from
  The Agency Fund* without thinking about CSS.

If you can describe your artifact in one sentence — "an evaluation brief about
maternal-health outcomes in three states" — you can produce the page through
conversation. The skill picks a template, fills the slots, and you iterate.

---

## Files at a glance

| Path | What it is |
|---|---|
| `SKILL.md` | Skill entry point. The two non-negotiables, web-only rules, QA checklist. |
| `README.md` | This file — orientation and how to use. |
| `web-design-rules.md` | The full set of web-specific rules, derived from the parent brand and Claude Design best practices. |
| `tokens.css` | Drop-in stylesheet. Three-layer CSS variables (`--taf-*` primitives → `--color-*` semantic → component tokens). Mirrors the parent design system. |
| `components.md` | Snippet library — hero, eyebrow section, card, callout, footnote, metric, capability list, button row. |
| `templates/research-report.html` | Long-form report. Hero · sticky TOC · sections · methodology · references. |
| `templates/briefing-memo.html` | One-pager exec brief. Eyebrow + headline + 3 findings + recommendation. |
| `templates/case-study.html` | Narrative case study. Photo hero · outcome panel · grantee chip shelf. |
| `templates/insight-dashboard.html` | KPI-forward dashboard. Metric cards · trend charts (Chart.js) · short narrative. |
| `templates/artifact-index.html` | Landing/collection page. Hero · cards grid · capability list. |

---

## How to use it (vibe-coding workflow)

The skill is built for conversational iteration. The intended flow:

1. **You** describe the artifact in one or two sentences.
   *"A short brief on what we learned from the AI4D Collaborative evaluation —
   three findings, one recommendation, a methodology footer."*
2. **Claude** picks the closest template (`briefing-memo.html`), asks for the
   eyebrow, headline, three findings, and recommendation, then produces a
   complete single-file HTML page with the tokens inlined.
3. **You** iterate conversationally:
   *"make the recommendation panel navy", "swap finding 2 for this one",
   "add a sources footer with five citations".*
4. **Claude** edits the file in place. You preview, then save the final HTML
   to your folder or push it to your static host.

The templates are **opinionated on purpose** — researchers shouldn't have
to choose between a 2-column and 3-column grid. The system has already chosen.

---

## The visual thesis

**Institutional credibility with field-grounded optimism.** Not a glossy
startup landing page; a research-backed social-impact institution that
understands product. Plainspoken, evidence-forward, confident.

The whole visual vocabulary is small:

- **One typeface.** Montserrat. 400/600/700 covers 95% of the work; 800/900
  for hero headlines.
- **Two colors with meaning.** Gold (`#F1B505`) for action verbs and CTAs.
  Navy (`#003366` / `#0B2341`) for impact nouns and gravity. Plus neutrals.
- **One accent.** Link blue `#6699CC`. That's it.
- **One radius for cards, one for buttons.** 12px and 9999px.
- **Navy-tinted shadows only.** Never pure black.
- **Documentary photography only.** Never stock, never illustration.

If you ever feel the urge to add a teal, a gradient, a second sans-serif,
or a friendly emoji — that's the signal you're drifting off brand. Stop and
look at agency.fund. The page is calmer than you remember.

---

## Reference best practices (Claude Design + 2026 web)

The templates align with current web design practice:

- **Fluid typography.** Type scale uses `clamp()` so headings resize between
  mobile and desktop without media queries.
- **8px / 4px spacing grid.** Every gap is a multiple of the base unit.
- **70ch max line length** for long-form prose; 1200px max page width.
- **WCAG 2.1 AA contrast.** Navy on white and white on navy both clear AAA;
  gold-on-white only passes large-text AA, so gold is reserved for accent
  words and CTAs (not body text).
- **System font stack as Montserrat fallback** for offline reliability.
- **No JS required.** Charts use Chart.js via CDN; everything else is HTML/CSS.
- **Three-layer token system.** Primitives → semantic aliases → components,
  matching the parent design system and Claude Design's documented approach.

---

## Working with Claude Design

When generating a site via Claude Design (claude.ai/design), upload this
skill's `tokens.css` and `web-design-rules.md` as design system assets — they
are written in the format Claude Design expects (colors, typography, spacing,
components, layout patterns). Claude Design will then apply the system to
every project under your organization automatically.

---

## What's intentionally not here

- **A React component library.** This skill outputs single-file HTML the
  researcher can open, share, or host on GitHub Pages. If you want a React
  setup, fork the tokens and rebuild in your stack — `tokens.css` is
  framework-agnostic.
- **A CMS.** Sites generated by this skill are static. For anything that
  needs editing-after-publish, hand off to a developer.
- **Multi-page navigation patterns.** The templates each stand alone.
  Multi-page sites are out of scope; ask a designer.

---

## Iteration notes

- If a real designer is producing the artifact, defer to them — this skill
  is for the *gap* where the user has no designer.
- If the page is for **external audiences** (funders, partner orgs), QA it
  against the checklist in `SKILL.md` and against the live agency.fund
  homepage before shipping.
- For **AWC artifacts** specifically, override the action/gravity aliases
  locally to use Club Blue `#6699CC` instead of gold — see the AWC variant
  notes in the parent skill.
