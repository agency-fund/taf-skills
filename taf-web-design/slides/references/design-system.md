# Design system

The visual language. It descends from The Agency Fund / Agentic Workflows Club:
navy and gold, Montserrat, generous whitespace, restraint.

## Color tokens (in `assets/taf.css`)

- **Navy** is gravity (titles, dark panels, logos, structure): `#003366` primary,
  `#0B2341` deck-dark, `#061A2E` deepest.
- **Gold** is action (one or two accent words in a headline, numerals, bullets,
  rules, the one CTA): `#F1B505`, hover `#ECAA00`. Never a gold paragraph.
- **Neutrals**: surface `#FFFFFF`, subtle surface `#F8F9FA`, border `#DEE2E6`,
  body ink `#212529`, secondary ink `#495057`, muted ink `#868E96`.
- **Chart/semantic colors** (use only when a visual encodes meaning, never as decoration):
  gold = human / baseline / action; navy = AI-assisted-correct / primary data;
  brick `#B3361F` = faulty / risk / failure; muted `#ADB5BD` = context / greyed-out.

## Typography

- **Montserrat only**, self-hosted as a variable font (`assets/fonts.css` +
  `fonts/montserrat-var.woff2`) with `font-display: block`. No second typeface.
  Self-hosting is deliberate: it removes the Google Fonts swap-flash between slides
  and makes the deck work offline.
- **Eyebrow** above every content title: ~22px, 600, UPPERCASE, 0.12em tracking,
  muted ink (gold on dark dividers).
- Content `h1`: 56–64px, 800, navy, with at most one or two words in gold.
- Divider assertions: up to ~92px white on navy.
- Body 24–30px. Never below ~22px. Big numbers use `font-variant-numeric: tabular-nums`.
- Monospace (`SF Mono`/`Menlo`) is allowed only for code/terminal traces.

## Components (in `taf.css`)

`.slide` (locked 1920×1080), `.eyebrow`, `h1`/`h1 .accent`, `.card`, `.logo-wrap`
(navy chip for monochrome SVG logos, recolored white), `.footnote` with a gold
`.mark` bar, `.step`/`.num` numbered lists, `body.dark` + `.wordmark` for dividers.

## Hard rules / anti-slop

- NO em dashes anywhere (commas, colons, periods, parentheses instead). Target zero.
- NO italics, NO emoji, NO purple, NO gradients (one subtle navy radial on dark
  dividers is the only exception). NO stock photos, NO AI-generated imagery, NO
  SVG-drawn people, NO decorative icon-next-to-every-bullet.
- Depth comes from layered cards, hairline structure, big tabular numerals,
  schematic UI mocks, real diagrams/charts, and motion — not ornament.
- Logos of named products are required when you name/compare them: fetch official
  marks (jsdelivr simple-icons, Wikimedia Commons, or Google favicon as fallback),
  inline the SVG, recolor `fill` to white inside a navy `.logo-wrap` chip.

## Writing voice

Engaging but serious, clear, and elaborated. Full sentences with a subject and a
verb, not punchy fragments. No significance inflation ("pivotal", "landscape" as an
abstract noun, "testament"), no hedging stacks, no "not X but Y" parallelisms, no
rule-of-three filler. State claims plainly. Label anything illustrative
("ILLUSTRATIVE" / "SCHEMATIC DEMO"). Verify external facts before asserting them.
