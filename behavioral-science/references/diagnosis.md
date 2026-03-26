# Behavioral Diagnosis Guide

This reference supports the **Diagnosis** mode. Read alongside `frameworks.md` for the full
COM-B/BCW framework, framework selection guidance, and the Wise Interventions section.

---

## Purpose

Behavioral diagnosis answers two questions:
1. *Why isn't the target behavior happening at the rate we want?*
2. *Which type of intervention is most likely to work here — and in this specific context?*

Both must be answered before designing anything. The most common failure modes in social sector
programs are: (a) treating the wrong constraint (e.g., applying information campaigns to a habit
problem); and (b) assuming an evidence base from elsewhere will transfer without testing it.

---

## Part A: COM-B Diagnostic Process

### Step 1: Specify the Behavior Gap

Define precisely what you're seeing vs. what you want:

- **Current state:** "Only 23% of enrolled clients made a second savings deposit"
- **Target state:** "80% of enrolled clients make at least one deposit per month for 3 months"
- **The gap:** 57 percentage points over 3 months

Write this out. Vague problem statements produce vague diagnoses. Push for specificity about
*who* does *what* *when* and *how often*.

---

### Step 2: Map the Six COM-B Sub-Components

The BCW identifies six sub-components across the three domains. Diagnose at this level of
precision — the top-level labels (Capability / Opportunity / Motivation) are too coarse to
reliably select the right intervention.

Use data where available; use structured field knowledge and qualitative insights where not.
The key is to be explicit about what you know vs. what you're assuming.

---

#### Psychological Capability
*Capacity to engage in the necessary thought processes — comprehension, reasoning, memory, decision-making.*

- Do people understand what the behavior is and how to do it?
- Do they have the literacy, language, or numeracy required?
- Do they understand *why* it matters — the value and consequences?
- Can they reason through the relevant decision even under cognitive load?
- Have they successfully done it before? (Prior experience builds psychological capability.)

---

#### Physical Capability
*Physical capacity to perform the behaviour — strength, stamina, motor skills, physical health.*

- Is there a physical demand that the population may not meet?
- Does disability, illness, or physical fatigue create a barrier?
- Are there motor or sensory requirements (e.g., using a mobile interface, travelling on foot)?

*Physical capability barriers are often underestimated in low-income or elderly populations,
and in contexts where health infrastructure is weak.*

---

#### Physical Opportunity
*All factors in the external environment that make the behaviour materially possible.*

- Is the behavior physically accessible? (Distance, opening hours, documentation required, cost)
- Do people have the materials, tools, or resources needed?
- Is there sufficient time in their day to perform the behavior?
- What happens if the environment changes — does the behavior become impossible?

---

#### Social Opportunity
*The cultural milieu — norms, language, social roles, and shared concepts that shape what feels
possible, appropriate, or normal.*

- What do peers, family, community leaders, or reference groups do and endorse?
- What is perceived as "what people like me do"?
- Does the social environment actively support or block the behavior?
- Are there stigma, shame, or honor dynamics at play?
- Does the available language and framing make the behavior conceivable and discussable?

*Social opportunity is distinct from reflective motivation. Someone may personally want to do
something but be constrained by what their social environment permits or normalizes.*

---

#### Reflective Motivation
*Conscious evaluations, plans, and intentions — the deliberate, goal-directed side of motivation.*

- Do people intend to do the behavior?
- Do they believe it's worth the effort or cost?
- Do they believe it will work (outcome expectancy)?
- Do they have concrete plans for *when*, *where*, and *how* they'll do it?
- Are there competing priorities or goals that crowd it out?

---

#### Automatic Motivation
*Emotions, impulses, habits, and drives that arise below conscious awareness — from associative
learning, prior experience, and innate dispositions.*

- Is there an existing habit that competes with or conflicts with the target behavior?
- Are there emotional responses — fear, shame, disgust, distrust — that generate avoidance?
- Is the target behavior associated with positive or negative affect?
- Does the environment contain cues that trigger competing automatic responses?
- Is the target behavior itself emotionally rewarding or aversive?

> **This sub-component is the most frequently missed in program diagnosis.** Most interventions
> assume reflective motivation is the driver and design accordingly (awareness, persuasion,
> incentives). When the true barrier is automatic — habit, ingrained emotional avoidance, conditioned
> association — these interventions fail. Ask explicitly: *even if someone wanted to do this, would
> their automatic response still block it?*

---

### Step 3: Rate and Rank Constraints

For each of the six sub-components, rate: **Primary constraint / Secondary constraint / Not a barrier**.

- Be explicit about which sub-component, not just the top-level domain.
- Document your evidence or reasoning for each rating.
- Most behavior gaps have 1–2 primary constraints. Focus intervention design there first.
- Resist the impulse to address everything at once — this dilutes effect and wastes resources.

---

### Step 4: Identify the Intervention Class

Before selecting specific intervention functions, determine which *class* of intervention the
diagnosis points to. This step prevents a critical error: applying choice architecture thinking
to a meaning-based problem, or applying wise intervention thinking to a structural problem.

**Two diagnostic branches:**

| If the primary barrier is... | Go to... |
|---|---|
| Physical, environmental, or structural (access, friction, capability, cues, defaults) | **Branch A: Choice Architecture / BCW** |
| How people *interpret themselves or their situation* (shame, identity threat, belonging, self-doubt, maladaptive attribution) | **Branch B: Wise Interventions** |

These branches are not mutually exclusive — a well-designed program often needs both. But
they require different diagnostic questions, different intervention designs, and different
evidence bases. Confusing them is one of the most common design errors.

---

### Step 5: Select Intervention Functions (Branch A — Choice Architecture / BCW)

The BCW maps COM-B sub-components to nine intervention functions. Use the table below
to identify which function(s) address your primary constraint.

| Primary constraint | Appropriate intervention functions |
|---|---|
| Psychological capability | Education, Training, Enablement |
| Physical capability | Training, Enablement |
| Physical opportunity | Environmental restructuring, Restriction (reduce competing behaviour), Enablement |
| Social opportunity | Environmental restructuring, Modelling, Restriction |
| Reflective motivation | Education, Persuasion, Incentivisation, Coercion |
| Automatic motivation | Persuasion, Environmental restructuring, Modelling, Enablement, Incentivisation, Coercion |

**Intervention function definitions (from Michie et al., 2011):**
- **Education** — Increasing knowledge or understanding
- **Persuasion** — Communication to induce positive/negative feelings or stimulate action
- **Incentivisation** — Creating expectation of reward
- **Coercion** — Creating expectation of punishment or cost
- **Training** — Imparting skills
- **Restriction** — Rules to reduce opportunity to engage in competing behaviour
- **Environmental restructuring** — Changing the physical or social context
- **Modelling** — Providing an example to aspire to or imitate
- **Enablement** — Increasing means/reducing barriers beyond education and training

---

### Step 6: Specify the Mechanism

Once you've selected an intervention function, go one level deeper: *what is the specific
causal chain between the intervention and the behavior change?*

This step is required by Szaszi et al. (2025), who demonstrate that without specifying the
mechanism, practitioners cannot assess whether evidence from another context actually transfers
to their own.

A mechanism specifies:
- What psychological or behavioral process the intervention triggers
- What must be true about the context for that process to activate
- What intermediate outcome would indicate the mechanism fired

**Example — default enrollment:**

> *Mechanism:* Reduced effort required to enroll (ease mechanism) → fewer people are deterred
> by inertia → higher uptake.
>
> *Required contextual conditions:* Trust in the institution offering the default; low perceived
> cost of opting out if desired; the default option is genuinely appropriate for most people.
>
> *Indicator that mechanism fired:* Uptake rate rises AND opt-out rate stays low (not just that
> fewer people are enrolled by confusion).

If you cannot specify the mechanism, you do not yet have a hypothesis — you have a guess.

**Common mechanisms for social sector interventions:**

| Intervention function | Likely mechanisms | Key condition that must hold |
|---|---|---|
| Defaults / environmental restructuring | Ease, endorsement, status quo preservation | Trust in choice architect; default is genuinely good for most |
| Social norms messaging | Descriptive norm updating; social proof | The stated norm must be accurate; framing must emphasize desirable behavior |
| Commitment devices | Hyperbolic discounting + self-binding | Person wants to commit; mechanism feels chosen not imposed |
| Simplification | Reduced cognitive load; reduced friction | Barrier is effort, not motivation; format is appropriate to literacy level |
| Messenger/modelling | Trust transfer; social proof; identity mirroring | Messenger is credible to this specific audience |

---

### Step 7: Formulate Hypotheses

Turn the diagnosis into specific, testable hypotheses that name the constraint, mechanism,
and expected outcome:

> "We believe low deposit rates are primarily driven by **automatic motivation** — clients have
> formed habits of spending income immediately upon receipt. **Reflective motivation is not the
> primary barrier** (most clients express genuine intent to save). Secondary barrier is **social
> opportunity**: saving is not visible or normalized among peers.
>
> *Mechanism:* Pre-commitment (lock-in savings account) removes the habitual spend decision point;
> modelling from peer savers shifts the perceived social norm.
>
> *Required contextual condition:* Clients must trust the financial institution; lock-in must be
> perceived as voluntary; stories must feature genuinely similar peers.
>
> *Measurement:* Track deposit frequency AND opt-out rates AND survey-measured social norms at
> baseline and follow-up. If deposit frequency rises but norms don't shift, the social mechanism
> hasn't fired and the intervention is only addressing automatic motivation."

---

## Part B: Diagnostic Branch — Wise Interventions (Meaning-Based Barriers)

**Source:** Walton, G.M. & Wilson, T.D. (2018). *Wise Interventions.* Psychological Review.

Wise interventions are a categorically different intervention class from choice architecture.
They do not modify the physical or social environment. They target the *subjective meanings*
people hold about themselves, others, or social situations — the working hypotheses through
which people interpret their circumstances and which drive behavior below the level of rational
deliberation.

**Choice architecture** asks: *How can we change the environment to make the right behavior easier?*
**Wise interventions** ask: *How can we change the meaning people make of their situation so that
the behavior becomes possible for them?*

---

### When to Suspect a Meaning-Based Barrier

Run through these diagnostic questions. If several are true, a wise intervention approach is
warranted alongside (or instead of) choice architecture:

**Identity and belonging:**
- Does the person seem to believe the target behavior is not "for people like me"?
- Is there evidence of identity threat — fear of being judged, stereotyped, or seen as
  inadequate?
- Does the person express doubt about whether they belong in the program, community, or
  role this behavior implies?
- Are there signs of social exclusion anxiety — fear of standing out, being exposed, or
  losing face?

**Attribution and meaning-making:**
- When the behavior fails, does the person attribute it to fixed personal inadequacy
  rather than changeable circumstances?
- Does the person interpret ambiguous events (e.g., critical feedback, early setbacks)
  as evidence that they cannot succeed — rather than as normal challenges?
- Is there a maladaptive narrative — a story the person tells about why change is
  impossible for them specifically?

**Self-integrity and motivation:**
- Does the person seem disconnected from the personal value of the behavior?
- Does externally prompted motivation (incentives, reminders, compliance requirements)
  produce engagement while active but collapse when removed?
- Is there shame, guilt, or self-blame associated with past failures to maintain the behavior?

**Structural clearance check (required before proceeding):**
> A meaning-based barrier is only the primary constraint if structural conditions for the behavior
> already exist. Wise interventions cannot substitute for access, resources, or capability.
> Confirm: Is the behavior structurally possible? Are opportunity and basic capability in place?
> If not, address structural barriers first. Wise interventions and structural reforms can and
> should be pursued simultaneously — but meaning-change will not work where structural
> affordances are absent.

---

### Three Diagnostic Families (Wise Interventions)

If meaning-based barriers are confirmed, identify which family:

**Family 1 — Need to Understand (attribution and belief)**

The person is drawing maladaptive inferences from their experiences — reasonable conclusions
given their context, but ones that generate self-defeating behavior.

Diagnostic signals:
- Person attributes setbacks to fixed personal inability, not to changeable circumstances
- Critical feedback or early failure produces disengagement, not renewed effort
- Person holds fixed beliefs about their competence, intelligence, or likelihood of success

Target: Change the specific meaning of the experience (e.g., reframe struggle as normal
and solvable, not as evidence of incapacity). Do not target intelligence or competence
directly — target the *interpretation* of events.

**Family 2 — Need for Self-Integrity (identity and self-adequacy)**

The person experiences threats to their sense of being a worthy, competent, coherent person —
which produces defensive responding, denial, or avoidance.

Diagnostic signals:
- Person becomes defensive or disengaged when confronted with information that implies failure
- There is a discrepancy between the behavior implied by the program and how the person sees
  themselves (e.g., "people like me don't do that")
- Health or behavior information is rejected rather than integrated

Target: Value affirmation (helping the person reconnect with core values beyond the threatened
domain), commitment through action, or identity-linking approaches. Note: value affirmation
can backfire if people are failing and can easily exit — confirm that engagement costs are high
before applying.

**Family 3 — Need to Belong (connection and social fit)**

The person is uncertain whether they belong, are valued, or are accepted within the context
in which the behavior is required. This uncertainty generates vigilance and withdrawal.

Diagnostic signals:
- Person drops out or disengages after early setbacks without apparent external barrier
- Person appears to interpret normal challenges (friction, initial failures) as signals of
  social rejection or exclusion
- Belonging uncertainty is especially likely at transition points — new programs, new roles,
  new relationships with institutions

Target: Social belonging interventions (normalizing early uncertainty; providing evidence
that challenges are temporary and universal for people in similar positions); link the
behavior to community contribution and social connection.

---

### Key Properties of Wise Interventions That Affect Diagnosis

**Recursive change:** Wise interventions are not one-shot information transfers. They work
by altering a self-fulfilling cycle — a new interpretation produces new behavior, which
produces new experiences, which reinforce the new interpretation. This means:
- Brief, well-targeted interventions can produce lasting effects
- The timing matters enormously — transition points (entering a program, recovering from a
  setback) are disproportionately effective windows
- Delivery should feel chosen and autonomy-supportive, not imposed (see SDT)

**Specificity requirement:** Wise interventions target specific meanings, not general
dispositions. "Think positive" does not work. Identifying the precise interpretation driving
the behavior does. The intervention must be wise to *what specific question* the person is
trying to answer about themselves or their situation.

**Systems check:** Meanings operate within complex systems. A meaning change will only
generate lasting behavior change if the social and structural environment affords opportunities
to act on the new meaning. If someone's sense of belonging improves but the program still
treats them as deficient, the meaning cannot take root.

---

## Part C: Generalizability Probe — Before Applying External Evidence

**Source:** Szaszi, Goldstein, Soman & Michie (2025). *Generalizability of Choice Architecture
Interventions.* Nature Reviews Psychology.

Before applying published evidence from other contexts, run this probe. The Szaszi et al.
review demonstrates that: (a) average nudge effects after bias correction are much smaller
than usually assumed (d ≈ 0.07–0.23 vs. commonly cited d = 0.43); (b) heterogeneity is
enormous — 95% of effect sizes range from d = −0.92 to 1.08; and (c) even experts cannot
reliably predict whether an intervention that worked elsewhere will work here.

**The five dimensions to check (Unit, Treatment, Outcome, Setting, Analysis — UTOS+A):**

| Dimension | Key questions to ask |
|---|---|
| **Unit (population)** | Is the evidence base from a similar population? WEIRD populations (Western, Educated, Industrialized, Rich, Democratic) systematically over-represent nudge effects. Are the literacy levels, economic conditions, institutional trust, and cultural norms comparable to your target population? |
| **Treatment (implementation)** | Is the proposed implementation materially the same as in the evidence base? Wording, channel, timing, salience, and mode of delivery all moderate effects significantly. The same letter sent by post vs. delivered by a health worker can produce different results. |
| **Outcome** | Is the measured outcome the same? An intervention that improves attitudes may not change behavior. Short-term uptake differs from sustained use. Proxy measures (intention, knowledge) are weak predictors of behavioral outcomes. |
| **Setting** | Is the physical, social, and institutional context comparable? A default that works in one country may fail or backfire in another — the colonoscopy default *reduced* uptake by 22% in one study where pre-scheduled appointments removed patient agency. |
| **Analysis** | Are the reported effect sizes from preregistered studies with transparent analysis? Non-preregistered studies average ~d = 0.43; preregistered studies average ~d = 0.23; bias-corrected meta-analyses suggest d = 0.07–0.08. Adjust your expectations accordingly. |

**Practical rules:**

- **If you cannot confirm mechanism + context match across at least 3 of 5 dimensions,
  treat the external evidence as hypothesis-generating, not confirmatory.** Run your own
  pilot before committing to scale.
- **Expect small average effects, high variance.** A promising intervention will often
  produce no effect or even backfire in a proportion of implementations. Build in
  measurement from Day 1.
- **Moderators interact.** The effectiveness of an intervention is shaped by the
  simultaneous interaction of population characteristics, implementation details, contextual
  factors, and outcome measures. Adding even one new moderator exponentially increases
  the number of possible interactions. This is not a reason to despair — it is a reason
  to test iteratively rather than scaling prematurely.
- **Emerging moderators change over time.** Societal values, norms, and technologies shift.
  An intervention that worked five years ago in a similar context may not work today because
  the social landscape has changed. This is especially relevant for social norm interventions,
  which depend on accurate readings of current peer behavior.

---

## Quick Diagnostic Red Flags

Use this table to rapidly identify the most likely constraint and the corresponding diagnostic
branch.

| Observed Pattern | Most likely constraint | Diagnostic branch | Implication |
|---|---|---|---|
| High enrollment, low follow-through | Automatic motivation (habit) or Reflective motivation (intention-action gap) | Branch A | Environmental restructuring, commitment devices, cue design |
| Low enrollment despite awareness | Social opportunity (norm blocking) or Automatic motivation (avoidance/distrust) | Branch A | Modelling, messenger change, norm messaging |
| People disengage after early setbacks without external barrier | Belonging uncertainty or fixed-ability attribution | Branch B | Wise intervention — normalize challenge, reframe setback meaning |
| High variation by gender | Social opportunity (gender norms) or Physical opportunity (access) | Branch A | Targeted environmental or social restructuring |
| High variation by geography | Physical opportunity (access) | Branch A | Enablement, service delivery redesign |
| People say they want it but don't do it | Automatic motivation (habit, emotional barrier) | Branch A | Not a persuasion/information problem — redesign environment or cues |
| Behavior occurs once but not repeatedly | Automatic motivation (habit not formed) | Branch A | Habit formation design, repetition structures, cue-routine-reward |
| Behavior varies by who delivers the message | Social opportunity + Automatic motivation (trust/affect) | Branch A or B | Messenger selection; consider belonging/identity dynamics |
| Behavior declines when program support ends | Automatic motivation (habit never formed) or Social opportunity | Branch A | Plan for habit formation and social anchoring from the start |
| Engagement is high during program but outcomes don't persist | SDT: external regulation, not internalization | Branch A + SDT | Redesign for autonomy support; see SDT in frameworks.md |
| Similar program worked elsewhere but not here | Generalizability failure | Generalizability probe | Check UTOS+A dimensions; specify mechanism; test before scaling |
| Defensive rejection of program information or feedback | Need for self-integrity (identity threat) | Branch B | Value affirmation or identity-linking approach; avoid controlling framing |
| "This program isn't for people like me" | Meaning — identity mismatch | Branch B | Need to Belong or Self-Integrity family; social belonging intervention |
| Shame or self-blame following failure | Need for self-integrity + Automatic motivation | Branch B + Branch A | Affirmation + environmental friction reduction |
