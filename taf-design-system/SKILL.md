---
name: taf-design-system
description: >
  The Agency Fund (TAF) design system for creating PowerPoint presentations using PptxGenJS.
  Use this skill whenever creating, editing, or extending any slide deck for The Agency Fund,
  including workshop decks, evaluation frameworks, case study slides, context slides, or any
  other presentation material. Also use it when the user asks to "match the TAF design", "keep
  it consistent with Agency Fund style", or "add slides to the eval deck". This skill captures
  both the visual design system AND the explicit design preferences Aman has expressed through
  iteration — not just the color palette but the philosophy of restraint, air, and typographic clarity.
---

# The Agency Fund (TAF) Design System

This skill captures the complete design system for Agency Fund presentations, built through iterative refinement. It covers two things: (1) the technical spec — colors, typography, layout rules — and (2) the *design philosophy* that Aman has consistently expressed. Both matter equally.

Read `references/code-patterns.md` before writing any code. It has ready-to-use PptxGenJS patterns for every common slide type.

---

## Design Philosophy (the non-negotiables)

These are principles distilled from direct feedback. They override intuition.

**One idea per slide, maximum.** Never combine unrelated concepts on the same slide. A recommendation card gets one recommendation. A quote card gets one voice. A prompt gets its own entire slide. If content doesn't fit on one slide at readable font sizes with generous air, split it across two slides rather than shrinking or compressing.

**Typography over decoration.** When in doubt, remove the icon, the badge, the decorative shape. Let hierarchy do the work. Aman's version of the farmer.chat slide had no icons at all — and it was better for it. Clean typographic cards beat visually busy ones every time.

**Air is not empty space — it's structure.** Cards should breathe. Content anchors the top and the bottom; the middle is intentional whitespace. Don't fill gaps with decoration. A card with a level label + title at the top and description + tag at the bottom — with generous space between them — feels considered and calm. A card that fills every inch feels anxious. When content doesn't fit comfortably, increase card height or split across slides — never shrink font below 9pt.

**Pills whisper, they don't shout.** A label like "CASE STUDY: FARMER.CHAT" should feel like a quiet annotation, not a button. Use a light tinted background (soft sage or light navy tint), not a solid filled color. The pill categorizes; it should not compete with the title.

**Emphasis is surgical.** One or two words of a title in gold. Everything else in navy. Never gold the whole title. Never italicize anything. Ever.

**One card gets the spotlight.** When you have a row of 4 cards (L1–L4), only L4 gets the dark navy treatment. L1–L3 stay light. Don't make all cards dark; don't invent new background colors for emphasis. Navy is the spotlight color.

**Status tags are conclusions, not footnotes.** The tag at the bottom of a card (Accuracy, Retention, Behavior Change, Outcome) is the punchline. Size it up. Give it color. Make it readable as a standalone phrase.

**No italics. Ever.** This has been asked for repeatedly. No `italic: true` anywhere in any file.

**No paragraphs on slides.** Text blocks should be 1–3 short lines maximum. If you need more, split across multiple cards or slides. Dense paragraphs are never acceptable — use hierarchy (label → question → detail) instead of prose.

**Prompt slides are ALWAYS standalone.** Audience prompts, reflection questions, and provocations get their own dedicated full slide. Never embed a prompt into a content slide alongside cards or data. This matches the existing deck pattern where every audience question is its own page.

**Introduce concepts gradually.** Don't assume the audience knows jargon. Present the old/familiar framing first (e.g., split-panel comparison), then the concrete example, then the data visualization. Abstract → concrete → data.

**No slide numbers, no presenter names, no watermarks** on content slides. The L1–L4 transition slides can have a large faint watermark number, but content slides are clean.

---

## Color Palette

### Core Palette

```javascript
const C = {
  navy:      "1B2B4B",   // primary — titles, dark cards, strong text
  navyMid:   "243860",   // secondary navy — card headers, level labels on dark
  navyDeep:  "0D1E38",   // deep navy — statement/provocation/transition slide backgrounds
  gold:      "C4922A",   // accent — gold word in title, stripes, dividers, tags
  goldLt:    "EDD68A",   // light gold — body text on dark backgrounds, sub-labels
  offWhite:  "F8F5EE",   // warm off-white — backgrounds for card grid slides, quote grids
  sand:      "E8DFC8",   // sand — rarely used, subtle texture
  white:     "FFFFFF",   // pure white — context slides, case study slides, criteria grids
  textDark:  "1B2B4B",   // = navy, for body text on light backgrounds
  textMid:   "4A5A7A",   // mid blue-grey — secondary body text, arrows between cards
  textLt:    "6B7280",   // light grey — captions, footnotes
  cardLight: "EEF3FA",   // very light blue-tint — L1/L2/L3 card backgrounds
  cardBorder:"C8D8EE",   // card border for light cards
  iconBox:   "D5E4F5",   // icon background within light cards (if icons used)
};
```

### Light Pastel Card Palette (5-color system)

Used for quote cards, recommendation cards, criteria grids, north star cards, and any multi-card layout that needs visual differentiation without heavy color. Each scheme defines a background, border, left accent bar, and text color:

```javascript
const PASTEL = {
  blue:     { bg: "EEF3FA", border: "C8D8EE", bar: "C4922A", text: "1B2B4B" },
  cream:    { bg: "FEF9EC", border: "EDD68A", bar: "A07020", text: "3A2808" },
  sage:     { bg: "EDF6EE", border: "A8D8AA", bar: "2A7A4A", text: "1A3A1A" },
  lavender: { bg: "F3EEFF", border: "C8A8E8", bar: "6A3A9A", text: "2A0A4A" },
  white:    { bg: "FFFFFF", border: "C8D8EE", bar: "C4922A", text: "1B2B4B" },
};
```

Assign colors cyclically: blue → cream → sage → lavender → white. When there are fewer than 5 cards, pick a subset — e.g., 3 cards = blue, sage, lavender. 4 cards = cream, sage, blue, lavender.

### Funnel / Gradient Navy Palette

For progressive data visualizations (funnels, waterfalls) where stages lighten:

```javascript
const FUNNEL_NAVY = ["1B2B4B", "253A65", "33538A", "4A6FA0", "658BB5"];
```

### Functional Colors

```javascript
const FUNC = {
  dropRed:    "B83232",   // drop-off percentages, warning callouts
  subtleBlue: "8AACCC",   // sub-notes on dark slides, quiet annotations
  dividerLt:  "AABBD0",   // light connector/arrow lines between elements
};
```

---

## Typography

**Georgia is the font for everything.** Titles, body text, labels, tags, bullet points, status tags — all Georgia. Do not use Calibri. This is a hard rule.

| Element                  | Size    | Weight | Color              |
|--------------------------|---------|--------|--------------------|
| Main title               | 26–46pt | bold   | Navy + gold accent word |
| Section/card title       | 18–26pt | bold   | Navy (light bg) / White (dark bg) |
| Body / description       | 11–13pt | normal | textMid or textDark |
| Level label (LEVEL 1–4)  | 9–12pt  | bold   | navyMid (light) / goldLt (dark) |
| Eyebrow label            | 7–10pt  | bold   | navyMid or goldLt, charSpacing 1–5 |
| Status tag               | 10–12pt | bold   | varies by level (see palette) |
| Pill label               | 7–8.5pt | bold   | navyMid on light tint bg |
| Caption / footnote       | 8–11pt  | normal | textLt             |
| Card question text       | 10–12pt | bold   | bar/accent color (NOT border color) |
| Drop-off percentage      | 8–9pt   | bold   | B83232 (red), wrap: false |

**Title pattern — always split color:**
```javascript
s.addText([
  { text: "Main Title Words ", options: { color: C.textDark, bold: true } },
  { text: "KeyWord",           options: { color: C.gold,    bold: true } },
], { fontSize: 34, fontFace: "Georgia", ... });
```

---

## Layout Rules

**Slide dimensions:** 10" × 5.625" (LAYOUT_16x9)

### Gold Stripes vs. Gold Left Bar vs. Neither

This is a critical distinction refined through iteration:

**Gold stripes (top + bottom)** — ONLY on these specific slide types:
- Context/bullet slides with white backgrounds
- Title slide
- Horizontal 4-card framework slide (the original L1–L4 overview)

```javascript
s.addShape(pres.shapes.RECTANGLE, { x:0, y:0,     w:10, h:0.1, fill:{color:C.gold}, line:{color:C.gold} });
s.addShape(pres.shapes.RECTANGLE, { x:0, y:5.525, w:10, h:0.1, fill:{color:C.gold}, line:{color:C.gold} });
```

**Gold left bar** — on full-bleed dark slides (transition, provocation, prompt, standalone dark statement):
```javascript
s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:0.18, h:5.625, fill:{color:C.gold}, line:{color:C.gold} });
```

**NO gold stripes or bars** — on card-based content slides. These use a thin gold separator line under the title instead:
- Quote card grids (3+2 layout)
- Recommendation cards
- North star / value cards
- 2×2 criteria grids
- Funnel/data visualizations

```javascript
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.45, y: 1.10, w: 9.1, h: 0.022,
  fill: { color: C.gold }, line: { color: C.gold },
});
```

**Content margins:** Left margin 0.45–0.5". Right margin 0.45–0.5". Title y-position: 0.22–0.28 on card slides, 0.55 on stripe slides.

---

## Slide Types

### 1. Context / Bullet Slide
Background: white (`FFFFFF`). Gold stripes. Title with color-split. Custom bullet dots as OVAL shapes.
See code-patterns.md Pattern 1.

### 2. Horizontal 4-Card (Framework / Case Study)
Background: white. Gold stripes. Pill label + title above. Four cards + arrows. L1–L3 light, L4 dark navy.
See code-patterns.md Pattern 2.

### 3. Dark Statement / Provocation Slide
Background: navyDeep (`0D1E38`). Gold left bar. No stripes. Georgia throughout. Large text, one idea.
See code-patterns.md Pattern 3.

### 4. Level Transition Slide
Background: navyDeep. Gold left bar. Large faint watermark number. Level label + title + question.
See code-patterns.md Pattern 4.

### 5. Title Slide
Background: navy. Decorative circles. Gold top stripe + left accent bar.
See code-patterns.md Pattern 5.

### 6. Two-Column Comparison
Background: offWhite. Two dark cards with gap divider.
See code-patterns.md Pattern 6.

### 7. Quote Cards (3+2 Grid)
Background: offWhite (`F8F5EE`). NO gold stripes — thin gold separator. 5 pastel cards in 3+2 layout (3 top, 2 bottom centered). Each card: decorative gold `"` mark, left accent bar, quote text, divider, category tag.
See code-patterns.md Pattern 7.

### 8. Recommendation / Numbered Cards
Background: offWhite. NO gold stripes — thin gold separator. 3 horizontal pastel cards, each: bold number (01/02/03), title, body, divider, tag.
See code-patterns.md Pattern 8.

### 9. North Star / Value Cards (4 Horizontal)
Background: white. NO gold stripes — thin gold separator. 4 horizontal pastel cards, each: label, bold question in accent color, divider, detail. Key rule: question text uses bar/accent color, NOT border color.
See code-patterns.md Pattern 9.

### 10. Split-Panel Mindset Shift
Background: offWhite with navyDeep left panel. Gold left bar on dark panel. Left = "old way", right = "new way". Each panel: eyebrow → title → separator → stacked items.
See code-patterns.md Pattern 10.

### 11. 2×2 Criteria Grid
Background: white. NO gold stripes — thin gold separator. 4 pastel cards in 2×2 grid. Each: number + label, key question in accent/bar color, divider, detail.
See code-patterns.md Pattern 11.

### 12. Funnel Visualization
Background: white. NO gold stripes — thin gold separator. Stacked horizontal bands tapering from wide to narrow. Each band: number (left), divider, label (center), tag (right). Red drop percentages between bands.
See code-patterns.md Pattern 12.

### 13. Standalone Prompt Slide
Background: navyDeep. Gold left bar. Full-slide question with no cards. Eyebrow label (goldLt, 10pt, charSpacing 2), large title (white, 42–56pt), optional sub-question (goldLt, 18pt). Rule: prompts are ALWAYS their own slide.
See code-patterns.md Pattern 13.

---

## Shadow Helpers

Always create fresh shadow objects — PptxGenJS mutates them if reused:
```javascript
const mkS  = () => ({ type:"outer", blur:8,  offset:3, angle:135, color:"000000", opacity:0.10 });
const mkSm = () => ({ type:"outer", blur:5,  offset:2, angle:135, color:"000000", opacity:0.07 });
```

Use `mkS()` for large standalone cards. Use `mkSm()` for smaller cards within a grid.

---

## Icon Usage

**Default: no icons.** Clean typographic cards are preferred over icon-decorated ones.

If icons are genuinely needed (they carry distinct meaning per card, not just decoration), use `react-icons/fi` + `sharp` to rasterize to base64 PNG:
```javascript
async function iconPng(IconComp, color, size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComp, { color, size: String(size) })
  );
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}
```

Icon box: small square (`D5E4F5` on light cards, `C.navyMid` on dark cards), centered in card.

---

## PptxGenJS Gotchas (critical bugs to avoid)

These are hard-won fixes from production. Each one has caused visible rendering bugs.

1. **8-digit hex is invalid.** PptxGenJS only accepts 6-digit hex strings (no `#` prefix). Never append alpha channels like `"FFFFFF22"`. For semi-transparent elements, use the `transparency` property instead:
   ```javascript
   // WRONG: fill: { color: "FFFFFF22" }
   // RIGHT: fill: { color: "FFFFFF" }, transparency: 85
   ```

2. **Text wrapping in narrow boxes.** Use `wrap: false` for any short text token (percentages like "−38%", tags, single words) in boxes under 0.6" wide. Without this, PptxGenJS breaks text across lines unexpectedly.

3. **Number box minimum width.** For multi-digit numbers (01, 02, "1,000") on cards, reserve at least 0.75" width. Narrower boxes cause digits to split across lines.

4. **Arrow/connector color.** Use `textMid` ("4A5A7A") for arrows and connectors between cards on light backgrounds. Using `cardBorder` makes arrows nearly invisible against pastel card backgrounds.

5. **Title wrapping.** If a title wraps to 2 lines unexpectedly, reduce font size by 2pt before changing layout. Common fix: 28pt → 26pt.

6. **Shadow reuse.** Never assign one shadow object to multiple shapes. PptxGenJS mutates the object. Always call the factory function fresh: `shadow: mkSm()`.

7. **Never prefix hex with `#`.** PptxGenJS takes bare hex: `"1B2B4B"` not `"#1B2B4B"`.

8. **Narrow funnel bands.** For visualization bands narrower than 4", hide the tag or merge it with the label to prevent text overlap. Labels need at least 1" width at 11pt Georgia.

9. **Card question text color.** Key questions inside pastel cards use the card's accent/bar color (e.g., gold, sage green, purple), NOT the lighter border color. Using border color creates low contrast and unreadable text.

---

## QA Process

After generating any `.pptx`, always run:
```bash
libreoffice --headless --convert-to pdf FILE.pptx --outdir /tmp/
pdftoppm -f N -l N -r 150 /tmp/FILE.pdf /tmp/prefix
convert /tmp/prefix-N.ppm /tmp/prefix-N.jpg
# Then Read the jpg to visually inspect
```

Check for:
- Title text wrapping unexpectedly (reduce font size or widen text box)
- Gold stripes/bars correct for slide type (stripes on bullet slides only, left bar on dark slides, neither on card grids)
- No Calibri anywhere
- No italics anywhere
- Bullet dots vertically centered with text
- Card content not overflowing bottom boundary
- Pill rendering as rounded, not rectangular
- Drop percentages rendering on one line (not split)
- Number boxes wide enough for all digits
- Arrow/connector visibility on light backgrounds
- Text boxes not overlapping between elements (especially in gaps between funnel bands)
- Prompt slides contain ONLY the prompt (no cards, no data alongside)

See `references/code-patterns.md` for full boilerplate code.
