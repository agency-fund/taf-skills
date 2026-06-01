# Components — Copyable Snippets

> Drop-in HTML for the patterns used across the five templates. Every snippet
> assumes `tokens.css` is loaded (either inlined or linked).

---

## Eyebrow + headline + lead

```html
<header>
  <span class="eyebrow">Evaluation · Maternal Health</span>
  <h1>Counseling moves <span class="accent-gold">outcomes</span> in maternal care</h1>
  <p class="lead">Findings from a 2025 evaluation of three TAF-backed organizations across India, Kenya, and Nigeria.</p>
</header>
```

## Poster hero (full-bleed photo)

```html
<section class="hero hero--poster" style="background-image: linear-gradient(180deg, transparent 40%, rgba(11,35,65,0.78) 100%), url('photo.jpg');">
  <div class="container hero__inner">
    <span class="eyebrow">Case Study · India</span>
    <h1>A frontline counselor can <span class="accent-gold">change</span> a family’s trajectory.</h1>
    <p class="lead">How Noora Health is training family caregivers — and what we learned funding them.</p>
    <a href="#read" class="btn btn--primary">Read the case study →</a>
  </div>
</section>
<style>
.hero--poster {
  min-height: 70vh;
  background-size: cover;
  background-position: center;
  color: var(--color-ink-inverse);
  display: flex;
  align-items: flex-end;
  padding: var(--space-4xl) 0;
}
.hero__inner h1, .hero__inner p { color: var(--color-ink-inverse); max-width: 50ch; }
.hero__inner .eyebrow { color: var(--taf-gold-300); }
</style>
```

## Split section header

```html
<section class="section">
  <div class="container grid grid--split">
    <div>
      <span class="eyebrow">Background</span>
      <h2>What we set out to measure</h2>
    </div>
    <div class="prose">
      <p>Three organizations. Twelve months. One core question: does
      structured counseling shift behavior at the household level?</p>
    </div>
  </div>
</section>
```

## Metric panel (navy background)

```html
<section class="section section--navy-deep">
  <div class="container">
    <span class="eyebrow">Investments to Date</span>
    <h2>By the numbers</h2>
    <div class="grid grid--3" style="margin-top: var(--space-2xl)">
      <div class="metric"><div class="metric__value">150</div><div class="metric__label">Grantees</div></div>
      <div class="metric"><div class="metric__value">$38M</div><div class="metric__label">Mobilized</div></div>
      <div class="metric"><div class="metric__value">12</div><div class="metric__label">Sectors</div></div>
      <div class="metric"><div class="metric__value">2021</div><div class="metric__label">Founded</div></div>
    </div>
  </div>
</section>
```

## Capability list (alternating navy/gold bullets)

```html
<section class="section">
  <div class="container grid grid--split">
    <div>
      <span class="eyebrow">Method</span>
      <h2>How we evaluated</h2>
    </div>
    <ul class="capability-list">
      <li><span class="bullet"></span>Semi-structured interviews with 42 frontline counselors</li>
      <li><span class="bullet"></span>Pre/post survey instrument across three sites</li>
      <li><span class="bullet"></span>Administrative data on visit attendance and clinical outcomes</li>
      <li><span class="bullet"></span>Co-analysis workshop with each grantee’s research team</li>
    </ul>
  </div>
</section>
```

## Card grid (3-up)

```html
<section class="section section--subtle">
  <div class="container">
    <span class="eyebrow">Findings</span>
    <h2>What changed for families</h2>
    <div class="grid grid--3" style="margin-top: var(--space-2xl)">
      <article class="card">
        <span class="eyebrow">Finding 01</span>
        <h3>Counseling adherence rose 34%</h3>
        <p>Households with a trained family caregiver completed a full counseling sequence at a substantially higher rate than the control group.</p>
      </article>
      <article class="card">
        <span class="eyebrow">Finding 02</span>
        <h3>Postnatal visits up 21%</h3>
        <p>Caregivers reported faster recognition of warning signs, leading to earlier postnatal visits across all three sites.</p>
      </article>
      <article class="card">
        <span class="eyebrow">Finding 03</span>
        <h3>Sustained at 12 months</h3>
        <p>Behavior change persisted at the 12-month follow-up, suggesting durable household-level practice change.</p>
      </article>
    </div>
  </div>
</section>
```

## Pull quote

```html
<blockquote class="pull-quote">
  When a mother-in-law learns the warning signs, the whole household watches differently. We didn’t just train one person — we changed who the household trusts.
  <cite>Field counselor · Bihar, India</cite>
</blockquote>
```

## Chip shelf (funding tier / grantee row)

```html
<section class="section">
  <div class="container">
    <span class="eyebrow">Cohort 2025 · Maternal Health</span>
    <h2>Organizations in this evaluation</h2>
    <div style="margin-top: var(--space-lg)">
      <span class="chip">Noora Health</span>
      <span class="chip">Jacaranda Health</span>
      <span class="chip">Lwala Community Alliance</span>
      <span class="chip">Living Goods</span>
    </div>
  </div>
</section>
```

## Recommendation panel (navy)

```html
<section class="section section--navy">
  <div class="container">
    <span class="eyebrow">Recommendation</span>
    <h2>Where we’re directing the <span class="accent-gold">next round</span></h2>
    <p class="lead" style="max-width: 60ch">Double down on family-caregiver training as a unit of investment, not just the patient or the counselor. The data is clear; the model travels.</p>
    <a href="#contact" class="btn btn--primary" style="margin-top: var(--space-lg)">Talk to the team →</a>
  </div>
</section>
```

## Footnote list

```html
<section class="section section--tight">
  <div class="container prose">
    <span class="eyebrow">References</span>
    <ol class="footnote-list">
      <li id="fn1">Author, A. (2025). <strong>Title of the source.</strong> Journal, 12(3), 45–67.</li>
      <li id="fn2">TAF (2024). <strong>Evaluation protocol for maternal-health cohort.</strong> Internal methods document.</li>
      <li id="fn3">Organization (2025). <strong>Quarterly report Q3.</strong> Retrieved from organization.org/q3-2025.</li>
    </ol>
  </div>
</section>
```

## Button row

```html
<div style="display: flex; gap: var(--space-md); flex-wrap: wrap; margin-top: var(--space-lg)">
  <a href="#download" class="btn btn--primary">Download the brief →</a>
  <a href="#contact" class="btn btn--dark">Talk to the team</a>
  <a href="#share"   class="btn btn--outline">Share this page</a>
</div>
```

## Navigation bar (minimal, sticky)

```html
<nav class="topnav">
  <div class="container topnav__inner">
    <a href="/" class="topnav__brand">The Agency Fund</a>
    <div class="topnav__links">
      <a href="#summary">Summary</a>
      <a href="#findings">Findings</a>
      <a href="#method">Method</a>
      <a href="#references">References</a>
    </div>
  </div>
</nav>
<style>
.topnav { position: sticky; top: 0; background: rgba(255,255,255,0.92); backdrop-filter: blur(8px); border-bottom: 1px solid var(--color-border-subtle); z-index: 50; }
.topnav__inner { display: flex; align-items: center; justify-content: space-between; padding: var(--space-md) var(--content-padding); }
.topnav__brand { font-weight: var(--fw-heading); color: var(--color-ink-navy); text-decoration: none; }
.topnav__links { display: flex; gap: var(--space-lg); font-size: var(--fs-sm); }
.topnav__links a { color: var(--color-ink-secondary); text-decoration: none; }
.topnav__links a:hover { color: var(--color-gravity); }
</style>
```
