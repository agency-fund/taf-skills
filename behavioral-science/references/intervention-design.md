# Intervention Design Guide

This reference supports the **Intervention Design** mode. Always read alongside `diagnosis.md`
(for the diagnostic process and Branch A/B distinction) and `frameworks.md` (for framework
details). Design decisions should emerge from diagnosis — never jump to intervention selection
without first establishing the primary constraint and its mechanism.

---

## The Design Thinking Process

Behavioral intervention design is not a lookup exercise. It requires moving through four
types of question, in sequence:

1. **What is actually constraining the behavior?** (COM-B diagnosis — diagnosis.md Part A)
2. **Is this a structural problem or a meaning problem?** (Branch A vs. Branch B — diagnosis.md Step 4)
3. **What mechanism should the intervention activate?** (Step 6 — mechanism specification)
4. **How does the proposed intervention perform against generalizability conditions?** (diagnosis.md Part C)

Only after answering all four should a specific intervention be recommended. The goal is
collaborative reasoning with the user, not matching a constraint label to a named tactic.

---

## Step 1: Confirm the Behavioral Target

Before designing, establish:

- **Who exactly** is the actor? (Not "community members" — "female heads of household aged 25-45 with children under 5 in peri-urban Nairobi")
- **What exactly** is the behavior? (Not "save more" — "make a deposit of KES 50+ into the savings account within 3 days of receiving income")
- **When and where** does the behavior occur or fail to occur?
- **What is already known** — prior attempts, available data, staff observations?

A vague target produces vague interventions. Push for specificity before proceeding.

---

## Step 2: Establish the Primary Constraint and Intervention Branch

Run the full COM-B diagnosis from `diagnosis.md`. Then identify the intervention branch:

**Branch A — Choice Architecture:** The barrier is structural, environmental, or automatic
(capability gaps, physical friction, social norms, cue/default/habit problems). Intervene by
changing conditions external to the person.

**Branch B — Wise Interventions:** The barrier is a maladaptive meaning the person holds
about themselves, their situation, or whether they belong. Intervene by changing how the
person interprets their circumstances.

These often co-occur. Address structural barriers first (they set the floor for what meaning
change can accomplish), then layer meaning-based design where relevant.

---

## Step 3: Specify the Mechanism

Before selecting specific tactics, articulate the causal chain the intervention will activate.
A mechanism specifies:

- What psychological or behavioral process the intervention triggers
- What contextual condition must be true for that process to activate
- What intermediate outcome would indicate the mechanism fired

Without a mechanism, you have a guess. Two examples:

> **Social norms SMS:**
> Mechanism: Descriptive norm update → person revises belief about peer behavior → reduced
> pluralistic ignorance → increased motivation to conform to (newly understood) majority behavior.
> Required condition: The stated norm is accurate and feels credible; the person identifies with
> the reference group; norm is framed as behavior, not gap.

> **Belonging narrative at program onboarding:**
> Mechanism: Early challenges reframed as normal and temporary → reduced belonging uncertainty
> → reduced vigilance and avoidance → sustained engagement when first friction appears.
> Required condition: Person is at a transition point; program has credible voices delivering the
> narrative; structural supports for success exist.

When presenting recommendations to users, always name the mechanism explicitly. This is
what makes the recommendation testable and what enables the user to adapt it to their context.

---

## Step 4: Design the Intervention

### Branch A — Choice Architecture Design

Map from constraint to BCW intervention function, then apply EAST and MINDSPACE as design
refinements:

| COM-B constraint | BCW intervention function | EAST refinement | MINDSPACE lever |
|---|---|---|---|
| Psychological capability | Education, Training, Enablement | Easy (simplify); Attractive (salient examples) | Salience, Messenger |
| Physical capability | Training, Enablement | Easy (remove physical friction) | Affect (confidence) |
| Physical opportunity | Environmental restructuring, Enablement | Easy (defaults, friction reduction) | Defaults |
| Social opportunity | Modelling, Environmental restructuring | Social (norms, visible peers) | Norms, Messenger |
| Reflective motivation | Persuasion, Incentivisation | Attractive (framing, loss); Timely (moments of change) | Incentives, Commitment, Ego |
| Automatic motivation | Environmental restructuring, Modelling, Enablement | Easy (cue design, defaults); Social (visible peer behavior) | Defaults, Priming, Affect |

**Fogg B=MAP diagnostic:** Before finalizing any choice architecture intervention, check:
- Is motivation the bottleneck, or is ability (simplicity)?
- Is there a trigger/prompt at the right moment?
- Which trigger type is needed — spark (build motivation), facilitator (reduce friction), or signal (reminder to someone already ready)?

In most social sector contexts, simplicity and triggers are underdesigned relative to motivation.
Resolve these before adding incentives or persuasion.

### Branch B — Wise Intervention Design

Wise interventions work through a different design logic. They are minimally directive —
they create conditions for people to draw new conclusions themselves, rather than telling
people what to think. This is critical: directive attempts to change beliefs often provoke
reactance and fail (Deci & Ryan; Walton & Wilson).

**For Need to Understand barriers (attribution and meaning-making):**
- Use *prompting with new information* — provide a new frame or fact that implies a different
  interpretation, without imposing the interpretation
- Use *leading questions* — ask questions that assume the adaptive interpretation and invite
  elaboration ("Explain why you were able to handle that challenge")
- Use *saying-is-believing* — ask the person to explain an idea to others in their own words;
  they advocate for and personalize the new meaning

**For Need for Self-Integrity barriers (identity threat):**
- Use *value affirmation* — ask the person to reflect on values they hold that are personally
  important, not related to the threatened domain; this "lowers the heat" and enables
  less defensive engagement
- Use *identity-linking* — connect the target behavior to an identity the person holds or
  aspires to ("people who save regularly are people who plan ahead for their children")
- Confirm: Is the person failing and able to exit easily? If so, value affirmation may
  backfire by providing comfort to disengage. Prioritize identity-linking instead.

**For Need to Belong barriers:**
- Use *social belonging narratives* — share stories from similar peers who experienced the
  same early challenges and found they were temporary and normal
- Use *saying-is-believing* for community contribution — ask the person to articulate how the
  behavior connects to people they care about
- Use *working-together framing* — reposition the behavior as something done collaboratively
  within a community, not a solitary or compliance act

**Wise intervention design rules (all families):**
- Timing matters more than dosage — transition points, first setbacks, and moments of
  uncertainty are the highest-leverage windows
- Keep it brief and experiential — wise interventions are not lectures; they are structured
  exercises of 10–30 minutes that feel chosen and autonomy-supportive
- The structural floor check: ensure physical and social opportunity already exists; meaning
  change cannot substitute for material conditions

---

## Step 5: Check for Durability (SDT Lens)

Before finalizing, ask: *What kind of motivation will this intervention create?*

If the intervention operates primarily through external regulation (incentives, surveillance,
social pressure), behavior will likely stop when the program ends. This is not always wrong —
for one-time or high-stakes behaviors, external regulation may be sufficient. But for behaviors
requiring sustained change, check:

- Does the intervention support autonomy (genuine choice, meaningful rationale) or undermine it?
- Does it build competence (mastery, positive feedback) or create dependency?
- Does it strengthen relatedness (connection to peers, program staff, community) or feel transactional?

If the intervention is primarily external, name this limitation explicitly. Recommend pairing
with autonomy-supportive framing and conditions that support internalization.

---

## Step 6: Prioritize and Run the Generalizability Probe

Rate each candidate intervention:

- **Mechanism specificity** — Is the causal chain articulated? Can it be tested?
- **Contextual fit** — Do the required conditions hold for *this* population, setting, and program?
- **Evidence quality** — Is the evidence from preregistered studies in comparable contexts?
  Adjust for publication bias: effect sizes from non-preregistered nudge literature average
  d = 0.43; preregistered studies average d = 0.23; bias-corrected estimates are often d ≈ 0.07–0.08.
- **Implementation feasibility** — Can this org actually deliver it with fidelity?
- **Risk of backfire** — Could this produce null or negative effects for this population?

Present 2–3 prioritized recommendations. Name the mechanism, the evidence basis, and what
would need to be true for the intervention to work. Tell the user what to test first and what
to measure to know whether the mechanism fired.

---

## Step 7: Write the Intervention Brief

For each recommended intervention:

```
Intervention Name:    [short label]
Intervention Branch:  [Branch A: choice architecture / Branch B: wise intervention / both]
COM-B constraint:     [the sub-component this addresses]
Mechanism:            [the causal chain — what process this triggers, and under what condition]
What it looks like:   [concrete description: exact wording, form redesign, narrative script]
EAST / MINDSPACE:     [which levers this activates]
Durability (SDT):     [what kind of motivation this creates; is it sufficient?]
Evidence:             [1-2 citations; note whether preregistered/bias-corrected]
What to test:         [the specific assumption the mechanism depends on]
Measurement:          [the mediator indicator that shows the mechanism fired]
Risks / backfire:     [when this might fail or produce negative effects]
```

---

## Common Intervention Patterns and Their Mechanisms

The following are well-evidenced in global development contexts. Each entry names the mechanism
explicitly, because the mechanism — not the label — determines whether the pattern transfers.

### Default Enrollment / Opt-Out
**Mechanism:** Ease (reduced effort) + status quo preservation + implied endorsement.
All three must hold: the behavior must be genuinely easier under the default; the institution
must be trusted; people must believe the default is designed for their benefit.
**Generalizability caution:** Default effects vary enormously across contexts (effect sizes
d = 0.2–0.9 in the same intervention; 17% of default studies find no effect; 3.5% show
negative effects). In one colonoscopy study, a pre-scheduled appointment default *reduced*
uptake by 22%. Always test locally before scaling.

### Commitment Devices
**Mechanism:** Hyperbolic discounting + self-binding. The person recognizes their future self
will be tempted; the commitment device removes the temptation decision point.
**Required condition:** The commitment must feel chosen, not coerced; trust in the institution
must be sufficient to tolerate lock-in; the behavior must be one the person genuinely wants to
sustain.

### Social Norms Messaging
**Mechanism:** Descriptive norm updating → reduces pluralistic ignorance → increases motivation
to align with actual peer behavior.
**Required condition:** The stated norm is accurate; the reference group is credible and
proximate; the message communicates what people *do*, not what they *don't* do.
**Generalizability caution:** Norms messaging that inadvertently signals that the undesired
behavior is common can increase it (boomerang effect). Always frame norms as "X% already do
this," never as a gap.

### Simplification and Friction Reduction
**Mechanism:** Fogg Ability axis — reduced cognitive and physical effort required → higher
compliance among motivated people.
**Highest-value application:** When people intend to act but don't. This is an ability problem,
not a motivation problem — adding more motivation will not help.

### Implementation Intentions ("If-Then" Plans)
**Mechanism:** Planning converts vague intention into specific stimulus-response link →
reduces in-the-moment decision-making → higher follow-through.
**Design:** Ask explicitly — "When will you go? What day? What time? What will remind you?"
Not: "Do you plan to go?"

### Loss Framing
**Mechanism:** Loss aversion → losses ~2× more impactful than equivalent gains → re-framing
benefit as avoided loss increases motivational weight.
**Caution:** Can feel manipulative if the framed loss is not genuine. Pair with authentic value.

### Trusted Messenger / Peer Channels
**Mechanism:** MINDSPACE Messenger effect + affect transfer — source credibility and identity
similarity increase persuasion and reduce defensiveness.
**Design implication:** The messenger matters as much as the message for identity-threatened
populations. Community health workers, beneficiary peers, and respected local figures
outperform institutional communications for building trust.

### Social Belonging Narrative
**Mechanism:** Reframes early challenge as normal and temporary → reduces belonging uncertainty
→ prevents early dropout and avoidance triggered by first setback.
**Delivery window:** Most effective at program entry, immediately after a setback, or at a
life transition. Requires authentic peer voices.

---

## Red Flags in Intervention Design

Flag these when they appear in a user's proposed approach:

- **Awareness campaign for a habit problem** — Information does not change automatic motivation. Identify the cue-routine-reward structure instead.
- **Adding more steps or communication** when simplification is needed — Complexity is usually the enemy.
- **Incentives as the first resort** — Incentives create external regulation (SDT); if behavior must persist after the incentive ends, they are insufficient or counterproductive.
- **Designing for System 2** (information, deliberation) when System 1 is driving behavior — Ask whether the decision is even reaching conscious deliberation.
- **Applying norms messaging without knowing the actual norm** — A fabricated or inaccurate social norm can damage trust and backfire.
- **Assuming published effect sizes will replicate locally** — Adjust for WEIRD bias and publication bias; always plan to measure.
- **Scaling before the mechanism has been tested** — Test locally first, even if evidence looks compelling.
- **Using directive, controlling framing** for wise interventions — Wise interventions work through autonomy-supportive, minimally directive exercises. Telling people what to think undermines the mechanism.
