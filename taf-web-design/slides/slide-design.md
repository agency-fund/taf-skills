# Slide design on web (Mode B)

The slide-deck half of `taf-web-design`. This is the system formerly carried in the
`my-design-slide` skill, folded in here so one TAF brand covers both web pages and web decks.

Each deck is a folder of standalone 1920×1080 HTML slides plus a shell (`index.html`) that
gives you an overview wall, keyboard navigation, smooth transitions, and print-to-PDF. The
look is navy + gold + Montserrat, restrained and editorial, with deliberate motion and
interactive demos — the same brand as Mode A, but on a fixed canvas with a real motion budget.

## The non-negotiables

These extend the shared brand rules in the top-level `SKILL.md` (gold = action, navy =
gravity, Montserrat only, no italics, no em dashes, documentary photos only, numbers as
evidence). On top of those:

1. **Navy is gravity, gold is action. Montserrat only. Whitespace.** One or two gold accent
   words per headline, never a gold paragraph. No second typeface, no purple, no gradients
   (except one subtle navy radial on dark dividers), no emoji, no italics, no stock or
   AI-generated imagery. No em dashes anywhere.
2. **Multi-file architecture.** One HTML file per slide in `slides/`, sharing
   `slides/shared/{taf.css, anim.css, anim.js, fonts.css, fonts/}`. The root `index.html` is
   the deck shell; its `DECK_MANIFEST` lists every slide.
3. **Self-hosted font, animated reveals, click-only interactivity.** These are wired through
   the shared assets and a small per-slide script — keep that script verbatim.
4. **Verify visually.** Screenshot every slide (animated + `?static=1`), check overflow and
   console errors, before calling it done.

## Quick start

1. Read `references/workflow.md` (the build process) and `references/design-system.md` (the
   look + voice). For per-slide layout patterns, read `references/slide-archetypes.md`.
2. Scaffold: copy `assets/{taf.css,anim.css,anim.js,fonts.css}` and `assets/fonts/` into the
   project's `slides/shared/`; copy `assets/deck_index.html` to `index.html` and edit its
   `DECK_MANIFEST`.
3. Write the slide copy first (full sentences, verified facts), then build slides from
   `assets/slide-template-content.html` and `assets/slide-template-divider.html`. For >5
   slides, do a 2-slide showcase to fix the grammar before scaling.
4. Verify with `scripts/shoot.mjs`, export with `scripts/export_deck_pdf.mjs`, and (optionally)
   host via `assets/deploy-pages.yml` + `assets/nojekyll.txt`.

## What's in this folder

| Path | What |
|------|------|
| `assets/taf.css` | color/type tokens + components (`.slide` locks 1920×1080) |
| `assets/anim.css`, `assets/anim.js` | entrance-animation framework (`data-reveal`, `data-grow-w/h`, `.hoverable`, `?static=1`) |
| `assets/fonts.css` + `assets/fonts/montserrat-var.woff2` | self-hosted Montserrat (no font-swap flash, works offline) |
| `assets/deck_index.html` | the deck shell: flat overview wall on an animated tech background, keyboard nav, transitions, font-ready reveal, print-to-PDF. Copy to `index.html`, edit `DECK_MANIFEST` |
| `assets/slide-template-content.html` | starter light content slide (with the required bottom scripts) |
| `assets/slide-template-divider.html` | starter dark section divider |
| `assets/deploy-pages.yml`, `assets/nojekyll.txt` | GitHub Pages auto-deploy (copy to `.github/workflows/` and `.nojekyll`) |
| `scripts/shoot.mjs` | screenshot every slide at 1920×1080, flag overflow + JS/console errors |
| `scripts/export_deck_pdf.mjs` | render the deck to a vector, text-selectable PDF |
| `references/design-system.md` | colors, type, components, anti-slop rules, writing voice |
| `references/slide-archetypes.md` | the slide types and how to build/animate each |
| `references/workflow.md` | end-to-end build, verification, and hosting workflow (+ solved gotchas) |

## Tooling note

The scripts need `npm i playwright pdf-lib` and a one-time `npx playwright install chromium`.
The deck itself has no runtime dependencies: fonts and logos are local and all paths are
relative, so it opens by double-click, works offline, and hosts on any static server from a
subpath.

## Note on paths

The `references/` files were written for a standalone skill, so they refer to sibling folders
as `assets/…`, `scripts/…`, and `references/…`. Inside this `slides/` folder those paths
resolve correctly (everything sits side by side). When you scaffold an actual deck, the
project layout in `references/workflow.md` still applies verbatim.
