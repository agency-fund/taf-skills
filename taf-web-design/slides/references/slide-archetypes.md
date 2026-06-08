# Slide archetypes

Each slide is one standalone HTML file at `slides/NN-name.html`, canvas locked to
1920×1080 by `taf.css`, px units only, nothing overflowing. Start from
`assets/slide-template-content.html` or `slide-template-divider.html`.

Pick the archetype per slide, then compose from the shared vocabulary:

- **hero / cover** — `body.dark`, full-bleed navy, wordmark, eyebrow, big title with
  one gold accent phrase, subtitle, hairline-divided footer. Stage the entrance.
- **divider** — dark, subtle navy radial, wordmark, gold "PART N" eyebrow, a short
  declarative assertion that scales in. (`slide-template-divider.html`)
- **explainer / orientation / framework** — light; eyebrow + title + one clear
  arrangement (2–3 columns, a horizontal flow with CSS-arrow connectors, or a single
  annotated diagram). High data-ink, real geometry, not icon soup.
- **timeline** — a horizontal rule that grows in (`data-grow-w`), nodes revealing
  left-to-right, the final node emphasized.
- **chart / data** — CSS bars with `data-grow-h`, tabular numerals, a caption that
  says what the axis measures, semantic colors (gold baseline / navy good / brick bad).
  Always define terms in a subhead; never leave numbers unexplained.
- **warning / privacy / equity** — light slide plus one navy-deep panel carrying the
  key rule or quote, with the load-bearing phrase in gold.
- **tool grid / spotlight** — cards with a 92px navy `.logo-wrap` chip (inline,
  recolored-white SVG), name, one line. Make it interactive: clicking a card selects
  it and updates a caption strip; clicking a citation reveals a source passage; a
  "Run the example" button replays a schematic agent trace.
- **decision / comparison** — two cards with navy headers and gold bullets, or rows
  of condition → recommendation with small logo chips; close with a navy caveat strip.
- **activity** — gold-warm "ACTIVITY N · NN MIN" eyebrow, big title, a goal line, a
  left column of numbered steps (gold 900 numerals, hairline dividers) and a right
  column with a debrief card (gold left border) and/or a navy caveat strip.
  Top-align the side column with the steps (`justify-content: flex-start`).
- **synthesis / takeaways** — three equal cards, gold numerals, short title + body;
  rebuild with explicit gaps, never absolute positioning (prevents overlap).
- **closing** — dark like the cover; the core message as the hero element; a contact
  row with links (`target="_blank" rel="noopener"`; `mailto:` for email).

## Animation (framework in `assets/anim.css` + `anim.js`, auto-wired)

- `data-reveal` on an element → fades/rises in, auto-staggered in DOM order.
  Variants `data-reveal="left|right|scale"`. Override timing with
  `style="--reveal-delay:.8s"`.
- Growing bars/rules: set the final size inline (`style="width:62%"`) plus
  `data-grow-w` (or `data-grow-h`); it animates from zero and stays correct for PDF.
- `.hoverable` adds a gentle lift on cards.
- `?static=1` (and printing) renders the settled final state with no motion — this
  is what PDF export captures, so every interactive default must already read complete.

## Interactivity rules

- **Click only.** Arrow keys, Space, digits, Home/End, Esc, and P are reserved by the
  deck shell. Each slide ends with a postMessage snippet that forwards those keys and
  the font-ready signal to the shell — keep it verbatim, never `preventDefault` clicks.
- Self-contained vanilla JS, unique names. Pre-select the first option so the default
  (and the PDF) reads complete. Make affordances obvious (cursor pointer, an uppercase
  hint, hover feedback). Transition state changes in 0.2–0.4s.
