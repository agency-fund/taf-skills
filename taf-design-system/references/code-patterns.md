# TAF PptxGenJS Code Patterns

Complete boilerplate for common slide types. Copy and adapt.

---

## File Bootstrap

```javascript
const pptxgen = require("pptxgenjs");
// Only needed if using icons:
// const React = require("react");
// const ReactDOMServer = require("react-dom/server");
// const sharp = require("sharp");

const C = {
  navy:      "1B2B4B",
  navyMid:   "243860",
  navyDeep:  "0D1E38",
  gold:      "C4922A",
  goldLt:    "EDD68A",
  offWhite:  "F8F5EE",
  white:     "FFFFFF",
  textDark:  "1B2B4B",
  textMid:   "4A5A7A",
  textLt:    "6B7280",
  cardLight: "EEF3FA",
  cardBorder:"C8D8EE",
  iconBox:   "D5E4F5",
};

// Light pastel card palette — 5 color schemes for multi-card layouts
const PASTEL = {
  blue:     { bg: "EEF3FA", border: "C8D8EE", bar: "C4922A", text: "1B2B4B" },
  cream:    { bg: "FEF9EC", border: "EDD68A", bar: "A07020", text: "3A2808" },
  sage:     { bg: "EDF6EE", border: "A8D8AA", bar: "2A7A4A", text: "1A3A1A" },
  lavender: { bg: "F3EEFF", border: "C8A8E8", bar: "6A3A9A", text: "2A0A4A" },
  white:    { bg: "FFFFFF", border: "C8D8EE", bar: "C4922A", text: "1B2B4B" },
};
const PASTEL_ORDER = ["blue", "cream", "sage", "lavender", "white"];

const mkS  = () => ({ type:"outer", blur:8,  offset:3, angle:135, color:"000000", opacity:0.10 });
const mkSm = () => ({ type:"outer", blur:5,  offset:2, angle:135, color:"000000", opacity:0.07 });

function addStripes(s, pres) {
  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0,     w:10, h:0.1,  fill:{color:C.gold}, line:{color:C.gold} });
  s.addShape(pres.shapes.RECTANGLE, { x:0, y:5.525, w:10, h:0.1,  fill:{color:C.gold}, line:{color:C.gold} });
}

// Thin gold separator — used on card-based content slides instead of stripes
function addGoldSep(s, pres, y) {
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.45, y: y || 1.10, w: 9.1, h: 0.022,
    fill: { color: C.gold }, line: { color: C.gold },
  });
}

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
```

---

## Pattern 1: Context / Bullet Slide

White background, gold stripes, split-color title, custom bullet dots.

```javascript
const s = pres.addSlide();
s.background = { color: C.white };
addStripes(s, pres);

// Split-color title
s.addText([
  { text: "Main Title ", options: { color: C.textDark, bold: true } },
  { text: "KeyWord",     options: { color: C.gold,    bold: true } },
], {
  x: 0.5, y: 0.55, w: 9, h: 0.85,
  fontSize: 38, fontFace: "Georgia", align: "left",
});

// Bullet items — last one can be standout (gold)
const items = [
  { text: "First bullet point here.",         standout: false },
  { text: "Second bullet point here.",        standout: false },
  { text: "Third bullet here.",               standout: false },
  { text: "Standout conclusion or warning.",  standout: true  },
];

items.forEach((item, i) => {
  const y = 1.6 + i * 0.82;
  const textH = 0.6;
  // Dot vertically centered: y + textH/2 - dotRadius
  s.addShape(pres.shapes.OVAL, {
    x: 0.5, y: y + textH / 2 - 0.065,
    w: 0.13, h: 0.13,
    fill: { color: item.standout ? C.gold : C.navy },
    line: { color: item.standout ? C.gold : C.navy },
  });
  s.addText(item.text, {
    x: 0.76, y, w: 8.5, h: textH,
    fontSize: 20, fontFace: "Georgia",
    color: item.standout ? C.gold : C.textDark,
    bold: item.standout,
    align: "left", valign: "middle",
  });
});
```

---

## Pattern 2: Horizontal 4-Card (Case Study / Framework)

White background, pill label, split-color title, 4 horizontal cards + arrows.

```javascript
const s = pres.addSlide();
s.background = { color: C.white };
addStripes(s, pres);

// Navy pill (for case study provenance)
s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 0.45, y: 0.26, w: 2.52, h: 0.34,
  fill: { color: C.navy }, line: { color: C.navy },
  rectRadius: 0.5,
});
s.addText("CASE STUDY: FARMER.CHAT", {
  x: 0.45, y: 0.26, w: 2.52, h: 0.34,
  fontSize: 8, fontFace: "Georgia", color: C.white, bold: true,
  align: "center", valign: "middle", charSpacing: 0.8,
});

// Split-color title
s.addText([
  { text: "What This Looks Like ", options: { color: C.textDark, bold: true } },
  { text: "in Practice",           options: { color: C.gold,    bold: true } },
], {
  x: 0.45, y: 0.65, w: 9.1, h: 0.75,
  fontSize: 34, fontFace: "Georgia", align: "left",
});

// Card layout
const cardW  = 2.08;
const arrowW = 0.38;
const cardH  = 3.55;
const cardY  = 1.58;
const startX = (10 - (4 * cardW + 3 * arrowW)) / 2;  // centres on slide

const cards = [
  {
    level: "LEVEL 1", title: "Model",
    desc: "AI gives correct, local farming advice.",
    tag: "Accuracy", tagColor: C.gold,
    cardBg: C.cardLight, borderColor: C.cardBorder,
    levelColor: C.navyMid, titleColor: C.textDark, descColor: C.textMid,
    divColor: C.cardBorder, dark: false,
  },
  {
    level: "LEVEL 2", title: "Product",
    desc: "Farmers come back to ask more questions.",
    tag: "Retention", tagColor: "2A7A4A",
    cardBg: C.cardLight, borderColor: C.cardBorder,
    levelColor: C.navyMid, titleColor: C.textDark, descColor: C.textMid,
    divColor: C.cardBorder, dark: false,
  },
  {
    level: "LEVEL 3", title: "User",
    desc: "Farmers act on the recommendations.",
    tag: "Behavior change", tagColor: "6B4A9A",
    cardBg: C.cardLight, borderColor: C.cardBorder,
    levelColor: C.navyMid, titleColor: C.textDark, descColor: C.textMid,
    divColor: C.cardBorder, dark: false,
  },
  {
    level: "LEVEL 4", title: "Impact",
    desc: "Crop yields and farmer incomes improve.",
    tag: "Outcome", tagColor: C.goldLt,
    cardBg: C.navy, borderColor: C.navy,
    levelColor: C.goldLt, titleColor: C.white, descColor: "CADCFC",
    divColor: C.gold, dark: true,
  },
];

cards.forEach((card, i) => {
  const x = startX + i * (cardW + arrowW);

  s.addShape(pres.shapes.RECTANGLE, {
    x, y: cardY, w: cardW, h: cardH,
    fill: { color: card.cardBg },
    line: { color: card.borderColor, width: 0.75 },
    shadow: mkSm(),
  });

  // Level label — top
  s.addText(card.level, {
    x: x + 0.15, y: cardY + 0.16, w: cardW - 0.3, h: 0.28,
    fontSize: 9, fontFace: "Georgia", color: card.levelColor,
    bold: true, charSpacing: 0.8, align: "left",
  });

  // Title — below level label
  s.addText(card.title, {
    x: x + 0.15, y: cardY + 0.55, w: cardW - 0.3, h: 0.55,
    fontSize: 18, fontFace: "Georgia", color: card.titleColor,
    bold: true, align: "left",
  });

  // [Intentional whitespace here — do not fill]

  // Description — pushed toward bottom
  s.addText(card.desc, {
    x: x + 0.15, y: cardY + 1.9, w: cardW - 0.3, h: 1.0,
    fontSize: 11, fontFace: "Georgia", color: card.descColor,
    align: "left",
  });

  // Divider
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.15, y: cardY + 3.0, w: cardW - 0.3, h: 0.03,
    fill: { color: card.divColor }, line: { color: card.divColor },
  });

  // Status tag
  s.addText(card.tag, {
    x: x + 0.15, y: cardY + 3.12, w: cardW - 0.3, h: 0.32,
    fontSize: 11, fontFace: "Georgia", color: card.tagColor,
    bold: true, align: "left",
  });

  // Arrow to next — use textMid for visibility on light backgrounds
  if (i < 3) {
    s.addShape(pres.shapes.LINE, {
      x: x + cardW + 0.06, y: cardY + cardH / 2,
      w: arrowW - 0.12, h: 0,
      line: { color: C.textMid, width: 1.5 },
    });
  }
});
```

---

## Pattern 3: Dark Statement / Provocation Slide

```javascript
const s = pres.addSlide();
s.background = { color: C.navyDeep };

// Gold left bar (replaces stripes on full-bleed dark slides)
s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:0.18, h:5.625, fill:{color:C.gold}, line:{color:C.gold} });

s.addText("Before we begin...", {
  x: 0.55, y: 0.75, w: 8.5, h: 0.45,
  fontSize: 13, fontFace: "Georgia", color: C.goldLt, align: "left",
});
s.addText("Your AI is live.\nUsers are talking to it right now.", {
  x: 0.55, y: 1.3, w: 9, h: 1.9,
  fontSize: 36, fontFace: "Georgia", color: C.white, bold: true, align: "left",
});
s.addText("How do you know if it's working?", {
  x: 0.55, y: 3.2, w: 9, h: 0.85,
  fontSize: 30, fontFace: "Georgia", color: C.goldLt, align: "left",
});
s.addText("Not just technically — but for the people whose lives it's meant to improve.", {
  x: 0.55, y: 4.25, w: 8.5, h: 0.6,
  fontSize: 14, fontFace: "Georgia", color: "8AACCC", align: "left",
});
```

---

## Pattern 4: Level Transition Slide

```javascript
const s = pres.addSlide();
s.background = { color: C.navyDeep };

// Large faint watermark number
s.addText("01", {
  x: 3.5, y: -0.5, w: 6, h: 6.5,
  fontSize: 280, fontFace: "Georgia", color: C.white, bold: true,
  align: "center", valign: "middle", transparency: 95,
});

// Gold left bar
s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:0.18, h:5.625, fill:{color:C.gold}, line:{color:C.gold} });

s.addText("LEVEL  01", {
  x: 0.45, y: 0.95, w: 7, h: 0.48,
  fontSize: 12, fontFace: "Georgia", color: C.gold, charSpacing: 5, bold: true, align: "left",
});
s.addText("Model\nEvaluation", {
  x: 0.45, y: 1.5, w: 8.5, h: 2.15,
  fontSize: 56, fontFace: "Georgia", color: C.white, bold: true, align: "left",
});
s.addText("Does the AI system perform as intended?", {
  x: 0.45, y: 3.68, w: 8.5, h: 0.72,
  fontSize: 18, fontFace: "Georgia", color: C.goldLt, align: "left",
});
```

---

## Pattern 5: Title Slide

```javascript
const s = pres.addSlide();
s.background = { color: C.navy };

// Decorative circles
s.addShape(pres.shapes.OVAL, { x:6.8, y:-1.2, w:5,   h:5,   fill:{color:C.navyMid, transparency:55}, line:{color:C.navyMid, transparency:55} });
s.addShape(pres.shapes.OVAL, { x:8.0, y:0.4,  w:2.8, h:2.8, fill:{color:C.gold,    transparency:82}, line:{color:C.gold,    transparency:82} });

// Gold top stripe
s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:10, h:0.1, fill:{color:C.gold}, line:{color:C.gold} });

// Left accent bar
s.addShape(pres.shapes.RECTANGLE, { x:0.65, y:1.4, w:0.07, h:2.6, fill:{color:C.gold}, line:{color:C.gold} });

s.addText("AI Evaluation\nfor Social Impact", {
  x: 1.0, y: 1.3, w: 6.5, h: 2.7,
  fontSize: 46, fontFace: "Georgia", color: C.white, bold: true,
  align: "left", valign: "middle",
});
s.addText("A Comprehensive Workshop on the 4-Level Framework", {
  x: 1.0, y: 4.0, w: 7.5, h: 0.55,
  fontSize: 15, fontFace: "Georgia", color: C.goldLt, align: "left",
});
```

---

## Pattern 6: Two-Column Comparison

White background replaced by off-white. Two dark cards with a gap divider.

```javascript
const s = pres.addSlide();
s.background = { color: C.offWhite };
// (No stripes — off-white bg slides use a different visual language)

s.addText("Two worlds. One product.", {
  x: 0.5, y: 0.28, w: 9, h: 0.62,
  fontSize: 28, fontFace: "Georgia", color: C.textDark, bold: true, align: "left",
});

// Left card: navy
s.addShape(pres.shapes.RECTANGLE, { x:0.38, y:1.1, w:3.9, h:3.7, fill:{color:C.navy}, line:{color:C.navy}, shadow:mkS() });
s.addText("What tech teams measure", {
  x: 0.52, y: 1.14, w: 3.6, h: 0.38,
  fontSize: 12, fontFace: "Georgia", color: C.goldLt, bold: true, align: "left",
});
// ... bullet items in "CADCFC"

// Gap divider
s.addShape(pres.shapes.LINE, {
  x: 4.91, y: 1.2, w: 0, h: 3.5,
  line: { color: C.textLt, width: 1, dashType: "dash", transparency: 30 }
});
s.addText("THE\nGAP", {
  x: 4.47, y: 2.6, w: 0.88, h: 0.65,
  fontSize: 9, fontFace: "Georgia", color: C.textLt, bold: true, charSpacing: 2, align: "center",
});

// Right card: L4 deep brown (matches Level 4 color)
s.addShape(pres.shapes.RECTANGLE, { x:5.72, y:1.1, w:3.9, h:3.7, fill:{color:"3A1A0A"}, line:{color:"3A1A0A"}, shadow:mkS() });
s.addText("What governments & funders need", {
  x: 5.86, y: 1.14, w: 3.6, h: 0.38,
  fontSize: 12, fontFace: "Georgia", color: "F0C890", bold: true, align: "left",
});
// ... bullet items in "F0D0A0"
```

---

## Pattern 7: Quote Cards (3+2 Grid)

offWhite background, NO gold stripes, thin gold separator. 5 pastel cards in 3+2 layout. Each card has: gold decorative quote mark, left accent bar, quote text, thin divider, category tag.

```javascript
const s = pres.addSlide();
s.background = { color: C.offWhite };

// Title
s.addText([
  { text: "Voices from the ", options: { color: C.textDark, bold: true } },
  { text: "field.",            options: { color: C.gold,     bold: true } },
], {
  x: 0.45, y: 0.22, w: 9.1, h: 0.52,
  fontSize: 26, fontFace: "Georgia", align: "left",
});

s.addText("What leaders told us about evaluating AI.", {
  x: 0.45, y: 0.76, w: 9.1, h: 0.28,
  fontSize: 11, fontFace: "Georgia", color: C.textMid,
});

addGoldSep(s, pres, 1.08);

// Quote data — 5 quotes with pastel color scheme
const quotes = [
  { text: "Quote text here...", tag: "TRUST",      scheme: PASTEL.blue     },
  { text: "Quote text here...", tag: "METRICS",    scheme: PASTEL.cream    },
  { text: "Quote text here...", tag: "EVIDENCE",   scheme: PASTEL.sage     },
  { text: "Quote text here...", tag: "INVESTMENT", scheme: PASTEL.lavender },
  { text: "Quote text here...", tag: "SCALE",      scheme: PASTEL.white    },
];

// Row 1: 3 cards
const r1W = 2.72, r1H = 1.72, r1Gap = 0.28;
const r1Total = 3 * r1W + 2 * r1Gap;
const r1X0 = (10 - r1Total) / 2;
const r1Y = 1.18;

// Row 2: 2 cards (wider, centered)
const r2W = 3.5, r2H = 1.72, r2Gap = 0.7;
const r2Total = 2 * r2W + r2Gap;
const r2X0 = (10 - r2Total) / 2;
const r2Y = r1Y + r1H + 0.18;

quotes.forEach((q, i) => {
  const isRow2 = i >= 3;
  const col = isRow2 ? i - 3 : i;
  const cW = isRow2 ? r2W : r1W;
  const cH = isRow2 ? r2H : r1H;
  const gap = isRow2 ? r2Gap : r1Gap;
  const x0 = isRow2 ? r2X0 : r1X0;
  const x = x0 + col * (cW + gap);
  const y = isRow2 ? r2Y : r1Y;
  const c = q.scheme;

  // Card background
  s.addShape(pres.shapes.RECTANGLE, {
    x, y, w: cW, h: cH,
    fill: { color: c.bg }, line: { color: c.border, width: 0.75 },
    shadow: mkSm(),
  });

  // Left accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.01, y: y + 0.12, w: 0.05, h: cH - 0.24,
    fill: { color: c.bar }, line: { color: c.bar },
  });

  // Gold decorative quote mark
  s.addText("\u201C", {
    x: x + 0.14, y: y + 0.02, w: 0.35, h: 0.40,
    fontSize: 28, fontFace: "Georgia", color: C.gold, bold: true,
  });

  // Quote text
  s.addText(q.text, {
    x: x + 0.14, y: y + 0.32, w: cW - 0.28, h: cH - 0.78,
    fontSize: 9.5, fontFace: "Georgia", color: c.text, align: "left", valign: "top",
  });

  // Thin divider
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.14, y: y + cH - 0.38, w: cW - 0.28, h: 0.015,
    fill: { color: c.border }, line: { color: c.border },
  });

  // Category tag
  s.addText(q.tag, {
    x: x + 0.14, y: y + cH - 0.35, w: cW - 0.28, h: 0.28,
    fontSize: 7, fontFace: "Georgia", color: c.bar, bold: true,
    charSpacing: 1, align: "left", valign: "middle",
  });
});
```

---

## Pattern 8: Recommendation / Numbered Cards (3 Horizontal)

offWhite background, NO gold stripes, thin gold separator. 3 pastel cards with bold numbers.

```javascript
const s = pres.addSlide();
s.background = { color: C.offWhite };

s.addText([
  { text: "Three things ", options: { color: C.textDark, bold: true } },
  { text: "to remember.", options: { color: C.gold,     bold: true } },
], {
  x: 0.45, y: 0.22, w: 9.1, h: 0.52,
  fontSize: 26, fontFace: "Georgia", align: "left",
});

addGoldSep(s, pres, 0.82);

const recs = [
  { num: "01", title: "Title here", body: "Body text...", tag: "CATEGORY", scheme: PASTEL.blue },
  { num: "02", title: "Title here", body: "Body text...", tag: "CATEGORY", scheme: PASTEL.sage },
  { num: "03", title: "Title here", body: "Body text...", tag: "CATEGORY", scheme: PASTEL.lavender },
];

const cW = 2.88, cH = 3.8, gap = 0.24;
const totalW = 3 * cW + 2 * gap;
const startX = (10 - totalW) / 2;
const cardY = 1.0;

recs.forEach((r, i) => {
  const x = startX + i * (cW + gap);
  const c = r.scheme;

  // Card
  s.addShape(pres.shapes.RECTANGLE, {
    x, y: cardY, w: cW, h: cH,
    fill: { color: c.bg }, line: { color: c.border, width: 0.75 },
    shadow: mkSm(),
  });

  // Left accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.01, y: cardY + 0.12, w: 0.05, h: cH - 0.24,
    fill: { color: c.bar }, line: { color: c.bar },
  });

  // Number — reserve at least 0.75" width to avoid digit splitting
  s.addText(r.num, {
    x: x + 0.14, y: cardY + 0.12, w: 0.75, h: 0.55,
    fontSize: 28, fontFace: "Georgia", color: c.bar, bold: true,
  });

  // Title
  s.addText(r.title, {
    x: x + 0.14, y: cardY + 0.72, w: cW - 0.28, h: 0.42,
    fontSize: 14, fontFace: "Georgia", color: c.text, bold: true,
  });

  // Body
  s.addText(r.body, {
    x: x + 0.14, y: cardY + 1.18, w: cW - 0.28, h: 1.8,
    fontSize: 10, fontFace: "Georgia", color: C.textMid,
  });

  // Divider
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.14, y: cardY + cH - 0.52, w: cW - 0.28, h: 0.015,
    fill: { color: c.border }, line: { color: c.border },
  });

  // Tag
  s.addText(r.tag, {
    x: x + 0.14, y: cardY + cH - 0.48, w: cW - 0.28, h: 0.28,
    fontSize: 7, fontFace: "Georgia", color: c.bar, bold: true,
    charSpacing: 1,
  });
});
```

---

## Pattern 9: North Star / Value Cards (4 Horizontal)

White background, NO gold stripes, thin gold separator. 4 pastel cards with label, bold question in accent color, divider, detail.

Key rule: the question text uses the card's **bar/accent color**, NOT the border color. This ensures readable contrast.

```javascript
const s = pres.addSlide();
s.background = { color: C.white };

s.addText([
  { text: "Our ", options: { color: C.textDark, bold: true } },
  { text: "north star.", options: { color: C.gold, bold: true } },
], {
  x: 0.45, y: 0.22, w: 9.1, h: 0.52,
  fontSize: 26, fontFace: "Georgia", align: "left",
});

addGoldSep(s, pres, 0.82);

const values = [
  { label: "REACH", question: "Can it reach 10x more people?", detail: "Detail text...", scheme: PASTEL.cream },
  { label: "COST", question: "Is it 10x cheaper per person?", detail: "Detail text...", scheme: PASTEL.sage },
  { label: "CAPACITY", question: "Does it free human capacity?", detail: "Detail text...", scheme: PASTEL.blue },
  { label: "ACCESS", question: "Is it always available?", detail: "Detail text...", scheme: PASTEL.lavender },
];

const cW = 2.14, cH = 2.55, gap = 0.2;
const totalW = 4 * cW + 3 * gap;
const startX = (10 - totalW) / 2;
const cardY = 1.0;

values.forEach((v, i) => {
  const x = startX + i * (cW + gap);
  const c = v.scheme;

  s.addShape(pres.shapes.RECTANGLE, {
    x, y: cardY, w: cW, h: cH,
    fill: { color: c.bg }, line: { color: c.border, width: 0.75 },
    shadow: mkSm(),
  });

  // Left accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.01, y: cardY + 0.12, w: 0.05, h: cH - 0.24,
    fill: { color: c.bar }, line: { color: c.bar },
  });

  // Label
  s.addText(v.label, {
    x: x + 0.14, y: cardY + 0.12, w: cW - 0.28, h: 0.24,
    fontSize: 8, fontFace: "Georgia", color: c.bar, bold: true, charSpacing: 1,
  });

  // Question — uses bar color for contrast (NOT border color)
  s.addText(v.question, {
    x: x + 0.14, y: cardY + 0.40, w: cW - 0.28, h: 0.75,
    fontSize: 11, fontFace: "Georgia", color: c.bar, bold: true,
  });

  // Divider
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.14, y: cardY + 1.22, w: cW - 0.28, h: 0.015,
    fill: { color: c.border }, line: { color: c.border },
  });

  // Detail
  s.addText(v.detail, {
    x: x + 0.14, y: cardY + 1.30, w: cW - 0.28, h: 1.1,
    fontSize: 9, fontFace: "Georgia", color: C.textMid,
  });
});
```

---

## Pattern 10: Split-Panel Mindset Shift

offWhite background with dark left panel. Gold left bar. Comparison layout: old way vs. new way.

```javascript
const s = pres.addSlide();
s.background = { color: C.offWhite };

const panelW = 4.2;

// Left dark panel
s.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: panelW, h: 5.625,
  fill: { color: C.navyDeep }, line: { color: C.navyDeep },
});

// Gold left bar
s.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: 0.1, h: 5.625,
  fill: { color: C.gold }, line: { color: C.gold },
});

// LEFT PANEL content
s.addText("UNTIL NOW", {
  x: 0.3, y: 0.35, w: 3.7, h: 0.3,
  fontSize: 8.5, fontFace: "Georgia", color: C.goldLt, bold: true, charSpacing: 2,
});
s.addText("We relied on\nproxy metrics.", {
  x: 0.3, y: 0.68, w: 3.7, h: 0.85,
  fontSize: 22, fontFace: "Georgia", color: C.white, bold: true,
});

// Separator
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.3, y: 1.62, w: 3.6, h: 0.015,
  fill: { color: C.gold }, line: { color: C.gold },
});

// Left items (stacked)
const leftItems = ["Downloads and sign-ups", "Sessions and clicks", "Completion rates"];
leftItems.forEach((item, i) => {
  const y = 1.82 + i * 0.60;
  s.addText(item, {
    x: 0.3, y, w: 3.7, h: 0.28,
    fontSize: 11, fontFace: "Georgia", color: "CADCFC",
  });
  s.addText("Why it misses the point.", {
    x: 0.3, y: y + 0.26, w: 3.7, h: 0.24,
    fontSize: 9, fontFace: "Georgia", color: "8AACCC",
  });
});

// RIGHT PANEL content
const rX = panelW + 0.45;
const rW = 10 - rX - 0.35;

s.addText("THE SHIFT", {
  x: rX, y: 0.35, w: rW, h: 0.3,
  fontSize: 8.5, fontFace: "Georgia", color: C.gold, bold: true, charSpacing: 2,
});
s.addText("What AI\ndemands.", {
  x: rX, y: 0.68, w: rW, h: 0.85,
  fontSize: 22, fontFace: "Georgia", color: C.textDark, bold: true,
});

s.addShape(pres.shapes.RECTANGLE, {
  x: rX, y: 1.62, w: rW, h: 0.015,
  fill: { color: C.gold }, line: { color: C.gold },
});

// Right items
const rightItems = ["Did users change their behaviour?", "Did outcomes actually improve?", "Was the AI safe at scale?"];
rightItems.forEach((item, i) => {
  const y = 1.82 + i * 0.60;
  s.addText(item, {
    x: rX, y, w: rW, h: 0.28,
    fontSize: 11, fontFace: "Georgia", color: C.textDark, bold: true,
  });
  s.addText("What this tells you.", {
    x: rX, y: y + 0.26, w: rW, h: 0.24,
    fontSize: 9, fontFace: "Georgia", color: C.textMid,
  });
});
```

---

## Pattern 11: 2×2 Criteria Grid

White background, NO gold stripes, thin gold separator. 4 pastel cards in 2×2 grid.

```javascript
const s = pres.addSlide();
s.background = { color: C.white };

s.addText([
  { text: "Evaluation ", options: { color: C.textDark, bold: true } },
  { text: "criteria.",   options: { color: C.gold,     bold: true } },
], {
  x: 0.45, y: 0.22, w: 9.1, h: 0.52,
  fontSize: 26, fontFace: "Georgia", align: "left",
});

addGoldSep(s, pres, 0.82);

const criteria = [
  { num: "01", label: "ACCURACY", question: "Is every claim correct?", detail: "Detail...", scheme: PASTEL.blue },
  { num: "02", label: "SAFETY",   question: "Does it avoid harm?",     detail: "Detail...", scheme: PASTEL.cream },
  { num: "03", label: "TRUST",    question: "Do users believe it?",    detail: "Detail...", scheme: PASTEL.sage },
  { num: "04", label: "EQUITY",   question: "Does it serve everyone?", detail: "Detail...", scheme: PASTEL.lavender },
];

const cW = 4.42, cH = 1.62, gapX = 0.2, gapY = 0.18;
const gridW = 2 * cW + gapX;
const startX = (10 - gridW) / 2;
const startY = 0.95;

criteria.forEach((cr, i) => {
  const col = i % 2;
  const row = Math.floor(i / 2);
  const x = startX + col * (cW + gapX);
  const y = startY + row * (cH + gapY);
  const c = cr.scheme;

  // Card
  s.addShape(pres.shapes.RECTANGLE, {
    x, y, w: cW, h: cH,
    fill: { color: c.bg }, line: { color: c.border, width: 0.75 },
    shadow: mkSm(),
  });

  // Left accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.01, y: y + 0.1, w: 0.05, h: cH - 0.2,
    fill: { color: c.bar }, line: { color: c.bar },
  });

  // Number + label
  s.addText(cr.num + "  " + cr.label, {
    x: x + 0.14, y: y + 0.10, w: cW - 0.28, h: 0.24,
    fontSize: 8, fontFace: "Georgia", color: c.bar, bold: true, charSpacing: 0.8,
  });

  // Question — uses bar color (NOT border) for contrast
  s.addText(cr.question, {
    x: x + 0.14, y: y + 0.36, w: cW - 0.28, h: 0.36,
    fontSize: 11, fontFace: "Georgia", color: c.bar, bold: true,
  });

  // Divider
  s.addShape(pres.shapes.RECTANGLE, {
    x: x + 0.14, y: y + 0.78, w: cW - 0.28, h: 0.015,
    fill: { color: c.border }, line: { color: c.border },
  });

  // Detail
  s.addText(cr.detail, {
    x: x + 0.14, y: y + 0.84, w: cW - 0.28, h: 0.68,
    fontSize: 9, fontFace: "Georgia", color: C.textMid,
  });
});
```

---

## Pattern 12: Funnel Visualization

White background, NO gold stripes, thin gold separator. Stacked horizontal bands tapering from wide to narrow. Drop percentages in red between bands.

```javascript
const s = pres.addSlide();
s.background = { color: C.white };

s.addText([
  { text: "Users don't disappear. ", options: { color: C.textDark, bold: true } },
  { text: "They leak.",              options: { color: C.gold,     bold: true } },
], {
  x: 0.45, y: 0.22, w: 9.1, h: 0.52,
  fontSize: 26, fontFace: "Georgia", align: "left",
});

s.addText("At each stage, some stop. Without knowing where — you're guessing.", {
  x: 0.45, y: 0.76, w: 9.1, h: 0.28,
  fontSize: 11, fontFace: "Georgia", color: C.textMid,
});

addGoldSep(s, pres, 1.10);

const stages = [
  { num: "1,000", label: "Heard about it",    tag: "ACQUIRED",  bg: "1B2B4B", bw: 8.8 },
  { num: "620",   label: "Tried it once",     tag: "ACTIVATED", bg: "253A65", bw: 7.4, drop: "\u221238%" },
  { num: "230",   label: "Used it regularly", tag: "ENGAGED",   bg: "33538A", bw: 6.1, drop: "\u221263%" },
  { num: "70",    label: "Came back",         tag: "RETAINED",  bg: "4A6FA0", bw: 5.0, drop: "\u221270%" },
  { num: "12",    label: "Changed behaviour", tag: "IMPACTED",  bg: "658BB5", bw: 4.0, drop: "\u221283%" },
];

const centerX = 5.0;
const bandH   = 0.60;
const gapH    = 0.15;
const startY  = 1.22;

stages.forEach((st, i) => {
  const bx = centerX - st.bw / 2;
  const by = startY + i * (bandH + gapH);

  // Drop % in gap above (except first band)
  if (i > 0) {
    const gapTopY = by - gapH;
    // Thin vertical tick
    s.addShape(pres.shapes.RECTANGLE, {
      x: centerX - 0.005, y: gapTopY + 0.01, w: 0.01, h: gapH - 0.02,
      fill: { color: "AABBD0" }, line: { color: "AABBD0" },
    });
    // Drop % — use wrap: false to prevent line-breaking
    s.addText(st.drop, {
      x: centerX + 0.05, y: gapTopY, w: 0.55, h: gapH,
      fontSize: 8.5, fontFace: "Georgia", color: "B83232",
      bold: true, align: "left", valign: "middle", wrap: false,
    });
  }

  // Band
  s.addShape(pres.shapes.RECTANGLE, {
    x: bx, y: by, w: st.bw, h: bandH,
    fill: { color: st.bg }, line: { color: st.bg },
  });

  // Number — left side
  s.addText(st.num, {
    x: bx + 0.14, y: by, w: 1.15, h: bandH,
    fontSize: 20, fontFace: "Georgia", color: "FFFFFF",
    bold: true, align: "left", valign: "middle",
  });

  // Thin divider inside band
  s.addShape(pres.shapes.RECTANGLE, {
    x: bx + 1.38, y: by + 0.10, w: 0.015, h: bandH - 0.20,
    fill: { color: "FFFFFF" }, line: { color: "FFFFFF" }, transparency: 60,
  });

  // Stage label — center
  const labelX = bx + 1.42;
  const labelW = st.bw - 1.42 - 1.05;
  if (labelW > 0.4) {
    s.addText(st.label, {
      x: labelX, y: by, w: labelW, h: bandH,
      fontSize: 11, fontFace: "Georgia", color: "FFFFFF",
      align: "left", valign: "middle",
    });
  }

  // Tag — right edge (skip if band too narrow for readable tag)
  if (st.bw >= 4.0) {
    s.addText(st.tag, {
      x: bx + st.bw - 1.0, y: by, w: 0.95, h: bandH,
      fontSize: 7.5, fontFace: "Georgia", color: "AACCEE",
      align: "right", valign: "middle", charSpacing: 1.2, wrap: false,
    });
  }
});

// Bottom tagline
const funnelBottom = startY + 5 * bandH + 4 * gapH;
s.addText("Same product. A different problem at every stage. You need to know which one.", {
  x: 0.45, y: funnelBottom + 0.12, w: 9.1, h: 0.32,
  fontSize: 10.5, fontFace: "Georgia", color: C.textDark,
  bold: true, align: "center",
});
```

---

## Pattern 13: Standalone Prompt Slide

Dark background, gold left bar. Full-slide prompt with no cards. Prompts are ALWAYS their own slide — never embedded in content slides.

```javascript
const s = pres.addSlide();
s.background = { color: C.navyDeep };

// Gold left bar
s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:0.18, h:5.625, fill:{color:C.gold}, line:{color:C.gold} });

// Eyebrow
s.addText("REFLECTION", {
  x: 0.45, y: 0.85, w: 7, h: 0.35,
  fontSize: 10, fontFace: "Georgia", color: C.goldLt, charSpacing: 2, bold: true,
});

// Main prompt
s.addText("Map your product\nto this funnel.", {
  x: 0.45, y: 1.35, w: 8.5, h: 2.2,
  fontSize: 46, fontFace: "Georgia", color: C.white, bold: true, align: "left",
});

// Sub-question (optional)
s.addText("Where do users drop off? Where are you guessing?", {
  x: 0.45, y: 3.55, w: 8.5, h: 0.72,
  fontSize: 18, fontFace: "Georgia", color: C.goldLt, align: "left",
});
```

---

## Common Mistakes to Avoid

- **Never** set `italic: true` on anything
- **Never** use Calibri — always Georgia
- **Never** add slide numbers to content slides
- **Never** reuse a shadow object — always call `mkS()` or `mkSm()` fresh
- **Never** prefix hex colors with `#` — PptxGenJS takes bare hex strings
- **Never** use 8-digit hex like `"FFFFFF22"` — use `transparency` property instead
- **Never** fill all 4 framework cards with dark backgrounds — only L4 gets navy
- **Never** use `ROUNDED_RECTANGLE` for overlay accent bars (only for pills/buttons)
- **Never** embed prompts into content slides — prompts are always standalone (Pattern 13)
- **Never** put gold stripes on card-based content slides — use thin gold separator instead
- **Bullet dots**: always calculate `y + textH/2 - 0.065` — don't eyeball it
- **Pill labels**: use `ROUNDED_RECTANGLE` with `rectRadius: 0.5`, not plain `RECTANGLE`
- **Title wrapping**: if a title wraps to 2 lines, reduce font size before adjusting layout
- **Number boxes**: reserve at least 0.75" width for multi-digit numbers (01, 1,000)
- **Arrow colors**: use `textMid` ("4A5A7A"), never `cardBorder` (invisible on light backgrounds)
- **Question text in cards**: use `bar`/accent color, NOT `border` color for readable contrast
- **Short text in narrow boxes**: add `wrap: false` for percentages, tags, and single words
