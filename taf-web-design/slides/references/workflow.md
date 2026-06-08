# Build workflow

## 0. Scaffold the project

```
project/
  index.html            # copy assets/deck_index.html, edit MANIFEST
  slides/
    shared/
      taf.css  anim.css  anim.js  fonts.css  fonts/montserrat-var.woff2
    01-cover.html  02-...   # one file per slide
  assets/logos/           # inline product logos if you name/compare tools
```

Copy `assets/{taf.css,anim.css,anim.js,fonts.css}` and `assets/fonts/` into
`slides/shared/`. Copy `assets/deck_index.html` to the project root as `index.html`
and edit `window.DECK_MANIFEST` to list every slide in order.

## 1. Plan, then write the copy first

Outline the deck (sections, one line per slide, archetype tag). Keep facts in a
`product-facts.md` and verify anything external with a web search before asserting it.
Write the slide copy in the design-system voice (full sentences, no em dashes).

## 2. Showcase before scale

For decks of more than ~5 slides, build 2 slides first that are visually the most
different (e.g. cover + a content/activity slide). Confirm the visual grammar, then
batch-produce the rest. This turns "wrong direction" into a 2-slide redo, not an
N-slide one.

## 3. Batch-produce (optionally with parallel subagents)

Give each agent: this skill's references, the slide copy, the two approved showcase
files as the grammar to match, and a non-overlapping set of slides. Each agent writes
its files and self-verifies with screenshots (animated pass + `?static=1` pass, plus a
clicked-state shot for interactive slides) and fixes overflow before returning.

## 4. Verify

```
npm i playwright pdf-lib && npx playwright install chromium   # once
node scripts/shoot.mjs slides _verify                          # screenshots + overflow + error scan
```

Read the screenshots. Confirm: no overflow at 1920×1080, no console errors, logos
render, copy matches, no em dashes (`grep -n '—\|&mdash;' slides/*.html`, ignoring
`<title>`), interactive defaults look complete. Eyeball `index.html` in a browser:
the overview wall (flat cards on the animated tech background), arrow-key navigation,
click-to-present, and that clicking inside a slide still lets arrow keys page.

## 5. Export PDF

```
node scripts/export_deck_pdf.mjs --slides slides --out deck.pdf
```

Vector, text selectable, one page per slide in `?static=1` rest state.

## 6. Host on GitHub Pages (optional)

Copy `assets/deploy-pages.yml` to `.github/workflows/deploy-pages.yml` and
`assets/nojekyll.txt` to `.nojekyll` at the repo root. Add a `.gitignore` for
`node_modules/` and `_verify/`. Push to `main`; the workflow self-enables Pages
(`enablement: true`) and deploys on every push. Site lands at
`https://<user>.github.io/<repo>/`. All asset paths are relative, so it works from a
subpath with no external dependencies.

## Gotchas already solved (do not reintroduce)

- **Font flash between slides** → fonts are self-hosted with `font-display: block`,
  and the shell reveals a slide only after its fonts report ready (via postMessage).
- **Arrow keys dead after clicking a slide** → each slide forwards reserved keys to the
  shell by postMessage; keep that snippet.
- **Overview tilt / wrong mode** → the overview is pinned to the flat grid
  (`window.DECK_OVERVIEW = 'grid'`); the gallery mode needs pre-rendered thumbnails.
- **PDF showing mid-animation** → export uses `?static=1`; keep `data-reveal` final
  states valid and interactive defaults complete.
