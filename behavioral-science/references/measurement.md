# Behavioral Measurement Guide

This reference supports the **Measurement** mode. Read alongside `diagnosis.md` (for the
constraint and mechanism identified) and `frameworks.md`. Measurement design should be
derived from the intervention theory of change — specifically from the mechanism specified
in Step 6 of the diagnostic process.

---

## The Measurement Thinking Process

The most common measurement error in social sector programs is measuring *distal outcomes*
while skipping the behavioral layer. If an intervention works, something had to change in
the person's psychology or environment *before* the outcome shifted. If you don't measure
that intermediate layer, you cannot learn whether the intervention worked *as designed* —
or accidentally, for unrelated reasons.

The second most common error is treating self-report data as reliable evidence of behavior
change without accounting for the cognitive biases that systematically distort recall and
reporting (Bias Codex Cluster 4 — memory compression, consistency bias, peak-end distortion,
rosy retrospection). Self-report and behavioral data should be triangulated whenever possible.

Good behavioral measurement captures:
1. **The target behavior itself** — did the person do the thing?
2. **Behavioral mediators** — did the mechanism the intervention was meant to activate actually fire?
3. **Proximal outcomes** — what immediately followed the behavior change?
4. **Distal outcomes** — ultimate program goals
5. **Moderators** — which population or context characteristics shaped the effect?

The last two are typically what funders want. The first three are what you need to learn,
improve, and generalize.

---

## Step 1: Operationalize the Target Behavior

Turn the behavioral target into a measurable construct with these five decisions:

| Decision | Question | Example |
|---|---|---|
| Observable action | What exactly counts as the behavior? | "Made a deposit into savings account" |
| Threshold | What magnitude counts as success? | "KES 200+ per deposit" |
| Frequency | How often should it occur? | "At least once per month" |
| Verification | How will you confirm it happened? | "Admin records from MFI system" |
| Window | Over what time period? | "Months 1–3 post-enrollment" |

Push for behavioral specificity. "Adoption" is not measurable. "Made a second loan repayment
on time" is. "Improved health-seeking behavior" is not. "Attended at least one postnatal visit
within 6 weeks of delivery" is.

---

## Step 2: Map the Mechanism to Measurable Mediators

The mechanism specified during diagnosis determines which mediators to measure. This is the
step that enables you to answer "did it work the way we expected?" — not just "did it work?"

### Branch A — Choice Architecture Mediators

For each BCW intervention function, there is a corresponding mediator layer:

| Mechanism | What must shift | How to measure it |
|---|---|---|
| Ease / friction reduction | Perceived effort; actual steps completed | Behavioral tracking (steps completed); self-report effort scale |
| Social norms update | Perceived prevalence of behavior among peers | Descriptive norm items: "What % of people like you do X?" |
| Default / endorsement | Perceived institutional recommendation; trust | Trust battery; perceived endorsement item |
| Loss aversion / incentive | Perceived value of maintaining behavior | Willingness to continue without incentive; stated vs. revealed preference |
| Implementation intention | Specificity of plan (when/where/how) | Implementation intention item: "On what day and time will you do X?" |
| Habit formation | Automaticity; behavioral frequency trend | Self-Report Habit Index (Verplanken & Orbell); weekly frequency tracking |
| Messenger / trust | Trust in source; identification with messenger | Messenger credibility items; in-group identification |

**Signal that a choice architecture mechanism fired:** The mediator shifts in the expected
direction *and* the behavioral outcome shifts. If the outcome shifts without the mediator
shifting, the mechanism may not be what you thought — something else is driving the change.

### Branch B — Wise Intervention Mediators

Wise interventions work through subjective meanings. These are harder to measure but essential
to track if you want to know whether the intervention is working as intended.

| Mechanism / family | What must shift | How to measure it |
|---|---|---|
| Need to Understand — attribution | Attributions for setbacks (fixed vs. malleable) | Attribution retraining probe: "If you struggled, what would that mean?" (open-ended + coded) |
| Need to Understand — growth mindset | Belief that ability develops with effort | Implicit Theories of Intelligence Scale (Dweck; 4-item version) |
| Need for Self-Integrity — value affirmation | Psychological security and openness | Post-task self-affirmation measure; reduced defensiveness in feedback task |
| Need for Self-Integrity — identity-behavior link | Perceived alignment between identity and target behavior | "People like me do X" identity-congruence item |
| Need to Belong — belonging uncertainty | Confidence of being accepted; sense of fit | Walton & Cohen belonging uncertainty scale; dropout intentions item |
| Meaning / purpose | Perceived meaningfulness of the behavior | Autonomy and purpose subscale from SDT measures |

**Signal that a wise intervention mechanism fired:** Belonging uncertainty decreases,
attribution style shifts toward malleable, or identity-behavior congruence increases —
*and* behavioral engagement follows. Meaning changes precede behavior changes; if you only
measure at endline, you will miss the causal pathway.

---

## Step 3: Measure Motivation Quality (SDT Lens)

For any behavior that must be sustained after program support ends, measure motivation
quality — not just motivation level. The SDT continuum from `frameworks.md` predicts
whether behavior will persist:

**Items to distinguish regulation types:**
- External: "I do this because I'll get a reward / avoid a problem"
- Introjected: "I do this because I'd feel guilty if I didn't"
- Identified: "I do this because it's personally important to me"
- Integrated: "Doing this is part of who I am"

Use the Treatment Self-Regulation Questionnaire (TSRQ) or adapted motivational regulation
items aligned to the target behavior. A shift from external to identified motivation across
program waves is a strong predictor of sustained behavior after the program ends.

---

## Step 4: Assess Self-Report Validity

Before relying on survey data, consider which Cognitive Bias Codex (Cluster 4) threats apply:

| Bias | What it distorts | Mitigation |
|---|---|---|
| Rosy retrospection | Positive over-recall of past experiences | Ask about *specific, recent, concrete* events not general patterns |
| Consistency bias | People recall past behavior as consistent with current behavior | Ask about behavior at a precise moment ("the last time..."), not generally |
| Peak-end rule | Recall dominated by peak moment and most recent experience | Measure at multiple time points, not just endline |
| Telescoping | Recent events feel further away; distant events feel more recent | Anchor to fixed external events ("since Ramadan ended..."; "since the rains began") |
| Social desirability | Reports align with perceived experimenter expectations | Use behavioral validation where possible; randomize sensitive items; use list experiments for stigmatized behaviors |

**Triangulation principle:** When administrative or observational data is available for the
target behavior, treat self-report as a mediator measure only — not as the primary outcome.
Self-report and behavioral data disagreeing is itself an important finding.

---

## Step 5: Measure Moderators

This is the step most programs skip. Szaszi et al. (2025) demonstrate that effect
heterogeneity — not average effect size — is the main thing you need to understand to learn
whether an intervention can generalize. Measuring moderators is how you accumulate that
understanding.

For each intervention, identify 2–3 candidate moderators drawn from the UTOS+A dimensions:

| Dimension | Example moderators to pre-specify | Why it matters |
|---|---|---|
| Unit (population) | Gender, age, prior experience with program type, literacy level, household income | Effect sizes often vary dramatically across subgroups |
| Treatment | Channel (in-person vs. SMS), agent delivering intervention, implementation fidelity | Same intervention delivered differently often produces different effects |
| Setting | Urban vs. rural, high-trust vs. low-trust institutional context, seasonal moment | Context shapes whether the mechanism can activate |
| Outcome | Behavioral frequency vs. quality; short-term vs. sustained | Interventions often improve proximal behavior without shifting distal outcomes |

Pre-specify moderator hypotheses before data collection. Even if you lack power to test
interactions, collecting the moderator data enables future meta-analyses and secondary
analyses. Report what you measured even if effects are null.

---

## Step 6: Construct the Indicator Framework

Organize indicators into a logical hierarchy tied to the theory of change:

```
MEASUREMENT FRAMEWORK

Target behavior:     [specific action + threshold + window]
         ↑
Behavioral mediators (mechanism indicators):
         ↑
Intervention:        [Branch A / Branch B / both]

INDICATOR TABLE

Level       | Indicator                        | Type        | Source           | Timing
------------|----------------------------------|-------------|------------------|------------------
Behavior    | % made deposit in past 30 days   | Admin       | MFI records      | Monthly
Behavior    | Avg deposit amount               | Admin       | MFI records      | Monthly
Mediator    | Perceived savings norm (peers)   | Survey      | Endline survey   | Baseline + endline
Mediator    | Implementation intention score   | Survey      | Enrollment survey| At enrollment
Mediator    | Motivation regulation type       | Survey      | TSRQ items       | Baseline + endline
Mediator    | Belonging uncertainty (if B2)    | Survey      | 3-item scale     | Baseline + 30 days
Proximal    | Account balance at 90 days       | Admin       | MFI records      | 90 days
Distal      | Household asset index            | Survey      | 12-month follow-up| 12 months
Moderator   | Literacy level                   | Admin/Survey | Enrollment data  | Baseline
Moderator   | Trust in institution             | Survey      | Baseline survey  | Baseline
```

---

## Validated Scales and Instruments

| Construct | Instrument | Notes |
|---|---|---|
| Habit strength | Self-Report Habit Index — SRHI (Verplanken & Orbell) | 12 items; shorten to 4 for survey brevity |
| Motivation quality | Treatment Self-Regulation Questionnaire (TSRQ) | Adapt subscales to target behavior |
| Belonging uncertainty | Walton & Cohen belonging scale | 3–5 items; validated in marginalized populations |
| Implicit theories (growth mindset) | Dweck Implicit Theories of Intelligence Scale | 4-item version for field use |
| Self-efficacy (domain-general) | Schwarzer & Jerusalem General Self-Efficacy Scale | 10 items; cross-culturally validated |
| Financial self-efficacy | Lown Financial Self-Efficacy Scale (2011) | 6 items; validated in low-income populations |
| Social norms | Cialdini descriptive/injunctive items | 2–4 items; adapt to specific behavior |
| Institutional trust | Afrobarometer trust items | Adapt for organizational context |
| Risk preferences | Eckel & Grossman gamble task | Incentivized; simple for field settings |
| Time preferences | Andreoni & Sprenger format | Requires incentivized task; not survey-only |
| Attribution style | ASQ-SF (Attributional Style Questionnaire — short form) | 6-item for locus of control and stability |

When no validated scale exists for a construct, write items that ask about *specific, concrete
behaviors or beliefs*, not abstract attitudes. Cognitive pretesting (think-aloud with 3–5
respondents) before deployment catches misunderstanding and translation issues.

---

## Common Measurement Mistakes

- **Measuring knowledge instead of behavior** — Knowing ≠ doing. Measure both, separately, as distinct constructs.
- **No baseline** — You cannot measure change without a starting point. Collect mediator and moderator data at enrollment.
- **Single time-point measurement** — Behavior change unfolds over time; a single endline misses trajectory information and decay effects.
- **Measuring satisfaction instead of mediators** — Program satisfaction predicts nothing reliably about behavior change. Replace or supplement with mechanism indicators.
- **Conflating enrollment with sustained use** — Measure the target behavior at 30, 60, and 90 days post-enrollment, not just at program end.
- **Skipping moderator measurement** — Without moderators, a null result tells you nothing and a positive result cannot be generalized.
- **Over-relying on self-report for behavioral outcomes** — Triangulate with administrative or observational data wherever possible.
- **Ignoring context effects** — Seasonal shocks, political events, or economic disruptions can swamp behavioral change effects; record them as covariates.
