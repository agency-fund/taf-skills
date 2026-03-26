# Behavioral User Research Guide

This reference supports the **User Research** mode. Read alongside `diagnosis.md` (which
defines the constraint types and diagnostic questions) and `frameworks.md`. User research
in a behavioral context is not about preferences or satisfaction — it is diagnostic work
aimed at understanding *why* behavior is or is not happening, and what a well-designed
intervention would need to do to change it.

---

## The Research Thinking Process

Standard user research asks: *What do people want?*
Behavioral user research asks:

- What do people *actually do* — not what they say they do, intend to do, or wish they did?
- What automatic, contextual, or social forces are shaping behavior outside of conscious awareness?
- What meanings do people hold about themselves, their situation, and whether they belong — and how do those meanings drive behavior?
- What conditions in the environment enable or block the behavior?
- Which moderators explain why behavior varies across subgroups, settings, or moments?

The key methodological principle is: **behavior is observable; motivation and meaning are
not.** Design research that gives you access to both. Use behavioral data, observation, and
reconstruction to understand what people actually do. Use carefully structured qualitative
inquiry to understand the meanings and mechanisms underneath.

---

## Choosing a Method

Research design should serve the diagnostic question. Match method to question:

| Research question | Best method(s) | Behavioral note |
|---|---|---|
| Why isn't a behavior happening? | COM-B cognitive interview | Structure around 6 sub-components; see below |
| What does the behavior sequence actually look like? | Observation / contextual inquiry | Never rely on recall; watch the behavior in situ |
| Are there meaning-based barriers (identity, belonging, attribution)? | Meaning-probing interviews | Requires different question structure; see below |
| What are the physical and social conditions that enable/block? | Site visits + contextual inquiry | Environment reveals friction that people cannot articulate |
| How does the behavior vary across time and context? | Diary studies / ecological momentary assessment | Captures real-time rather than reconstructed experience |
| What norms does the population hold, and what do they believe others do? | Focus groups + descriptive norm elicitation | Triangulate stated norms with behavioral data |
| How does someone navigate a specific decision or product interface? | Think-aloud protocol | Useful for digital products, form design, enrollment flows |
| What do implicit attitudes or associations look like? | Implicit Association Test (IAT) | Specialized; flags System 1 responses that interviews miss |
| Which moderators explain variation in behavior across subgroups? | Purposive sampling + subgroup analysis | Pre-specify moderator hypotheses; sample deliberately |

For most behavioral diagnostics, begin with COM-B cognitive interviews to map constraints,
then use observation or diary studies to validate and deepen. Do not rely on a single method.

---

## Part A: COM-B Diagnostic Interviews

The most productive qualitative method for behavioral diagnosis. Structure each interview
across the six COM-B sub-components — not just the three top-level domains. The precision
matters because the sub-component determines which intervention function is appropriate.

### Framing the interview

Open with behavioral reconstruction, not opinion or attitude:
> "I'm interested in what actually happens when you [target behavior]. Not what you think
> you should do, or what you plan to do — what actually happened. Let's start with the
> last time you [behavior / did not do behavior]. Can you walk me through that day?"

Reconstruction surfaces automatic and contextual barriers that abstract questioning misses.

### Psychological Capability Probes
*Goal: understand comprehension, reasoning, and cognitive processing demands*

- "Walk me through what you have to do to [behavior]. What are the steps?"
- "Is there any part of [product / program / process] that's confusing or unclear?"
- "When you thought about [behavior], what was going through your mind?"
- "Has there been a time when you tried and something got in the way of understanding?"

Listen for: confusion about how something works, literacy or numeracy gaps, decision fatigue,
uncertainty about what constitutes the right action.

### Physical Capability Probes
*Goal: identify physical access, stamina, health, and motor demands*

- "What does it physically require to do this? Can you take me through that?"
- "Is there ever a time your body or health affects whether you can do this?"
- "Are there moments of the day or week when this is easier or harder physically?"

### Physical Opportunity Probes
*Goal: map material conditions — access, friction, time, cost, tools*

- "What would you need to have in place to do this today?"
- "What's the closest / fastest / cheapest way to [behavior]? Have you tried it?"
- "What gets in the way practically — time, distance, money, paperwork?"
- "Walk me through the last time the process didn't work. What happened at each step?"

Listen for: access gaps, friction in the enrollment or usage flow, structural barriers that
will not be solved by motivation-focused interventions.

### Social Opportunity Probes
*Goal: surface norms, community dynamics, family influence, and social permission*

- "What do the people close to you — your partner, family, community — think about this?"
- "Who else in your community is doing this? Who isn't?"
- "Have you ever felt pressure from people around you to do this, or not to do it?"
- "What would people say about someone who did this regularly?"

Listen for: norm misperceptions (pluralistic ignorance), social permission structures,
gender or community role constraints, messenger effects.

### Reflective Motivation Probes
*Goal: assess intention, value, belief, and planning*

- "How important is [behavior] to you personally? Why?"
- "What would need to be different for you to do this more often?"
- "Do you have a plan for when and how you'll do this? Can you describe it?"
- "What are the other things competing for your attention or money right now?"

Listen for: genuine intention with no plan (→ implementation intentions); intention blocked
by competing priorities (→ priority framing, commitment); low value perception (→ persuasion,
value building).

### Automatic Motivation Probes
*Goal: surface habits, emotional associations, and sub-conscious drivers*

- "What's your gut reaction when you think about [behavior]? Any feelings that come up?"
- "When you received income last time, what did you do first — without thinking about it?"
- "Is there a moment in your day when [behavior] comes to mind naturally? What triggers that?"
- "Has anything happened in the past with [similar behavior] that still affects how you feel about it?"

Listen for: fear, shame, distrust, habitual spending or avoidance patterns, negative
associations from prior experience. These are automatic motivation barriers — information
and persuasion will not shift them; cue and environment redesign will.

---

## Part B: Meaning-Probing Interviews (Wise Interventions Diagnostic)

Use this question structure when early signals suggest a meaning-based barrier — identity
mismatch, attribution patterns, belonging uncertainty. These signals often appear in the
automatic motivation probes above (shame, self-doubt, dropout after first setback) but
require a different follow-up inquiry.

**When to switch to meaning-probing:**
- Person expresses doubt about whether "someone like me" can do this
- Person attributes past failures to fixed personal inadequacy ("I'm just not good at this")
- Person disengaged or dropped out after an early setback without a clear structural reason
- Person describes the behavior as appropriate for other people but not themselves

### Identity and Belonging Probes
*Goal: understand whether the person feels the behavior belongs to their identity and social world*

- "Who do you imagine when you think of someone who does this regularly?"
- "Do you feel like you fit in this program? What makes you say that?"
- "When you first joined, was there a moment where you felt uncertain whether this was for you?"
- "Has there been a time when you felt like an outsider in this context? What happened?"

### Attribution and Meaning-Making Probes
*Goal: understand how the person interprets setbacks and early difficulty*

- "When something went wrong in the past with [behavior], what did you think that said about you?"
- "When this has been hard, have you thought of the difficulty as something about you personally, or about the situation?"
- "If you struggled with this, what would that mean to you?"
- "Can you think of someone who overcame early challenges with this? What do you think made the difference for them?"

### Self-Integrity and Values Probes
*Goal: understand whether the behavior is connected to the person's core values and sense of self*

- "What are the things that matter most to you as a person — as a parent, a member of your community?"
- "Where does [behavior] fit with those things?"
- "Is there a gap between how you want to show up and what's actually been happening?"

**Research rule for meaning probes:** Do not challenge or reframe the person's interpretation
during the research phase. The goal is to understand the meaning they hold, not to intervene.
Premature reframing during research contaminates the data and damages rapport.

---

## Part C: Observation and Contextual Inquiry

Go where the behavior happens. Observe actual processes, not reconstructions.

**What to document:**
- The physical environment — what does the space look, feel, and sound like? What are the
  cues present? What friction is visible in the environment?
- The actual sequence of steps the person takes
- Moments of hesitation, friction, confusion, or departure from the expected path
- Social dynamics — who is present, who influences, what is said and not said
- Interruptions and competing demands on attention
- What the person does NOT do that you expected — absence of behavior is data

**During observation:**
- "Can you narrate what you're thinking while you do this?"
- "Is this what normally happens, or is today different in any way?"
- "What would usually happen next if I weren't here?"

**Bias awareness:** Observation is not neutral. Your presence changes behavior (Hawthorne
effect). People perform competence and compliance when being watched. Minimize this by
spending extended time in the context, explaining your role clearly, and triangulating
observations with unobserved behavioral data (admin records, device logs).

---

## Part D: Diary Studies

Captures behavior as it happens — not through post-hoc recall, which is systematically
distorted by Cognitive Bias Codex Cluster 4 effects (rosy retrospection, consistency bias,
peak-end rule).

**Design principles:**
- Use SMS, WhatsApp, or simple app prompts for low-cost daily capture
- Ask about specific behaviors, not feelings: "Did you make a payment today? How much?"
- Maximum 3 questions per prompt; respect cognitive load
- Run for 7–30 days depending on behavior frequency
- Anchor prompts to behavioral events ("After you receive income this week...")
- Close with one synthesis interview for interpretation and context

**Ideal for:** Savings behavior, medication adherence, agricultural decision-making,
consumption patterns, care-seeking behavior — any behavior with meaningful day-to-day variation.

---

## Part E: Moderator Exploration

Most user research focuses on central tendency — what is typical. But the most actionable
behavioral insight often comes from variation: *why does this behavior happen for some
people and not others?*

Pre-specify 2–3 candidate moderators before fieldwork based on the UTOS+A dimensions from
`diagnosis.md`. Then design research to deliberately capture variation:

**Purposive sampling:** Recruit participants who represent meaningful variation on the
hypothesized moderator — not convenience samples. If you believe literacy level moderates
the intervention effect, sample across that dimension deliberately.

**Within-interview moderator probes:**
- "You mentioned you had already done this before — do you think that made a difference?"
- "How do you think this would work for someone who [differs on moderator]?"
- "Is there anything about your situation that you think makes this easier or harder for you than for others?"

**Between-interview comparison:** After each interview, record whether the moderator
was present or absent and how the behavior pattern differed. Build a simple matrix.

This is not quantitative moderator analysis — but it generates hypotheses you can pre-specify
for measurement and test in a larger study.

---

## Synthesizing Across Methods

After completing fieldwork, organize findings against the six COM-B sub-components, then
check for meaning-based barriers before concluding. A synthesis structure:

```
DIAGNOSTIC SYNTHESIS

Target behavior: [specific action]

COM-B constraint map:
  Psychological capability: [finding + evidence source]
  Physical capability:      [finding + evidence source]
  Physical opportunity:     [finding + evidence source]
  Social opportunity:       [finding + evidence source]
  Reflective motivation:    [finding + evidence source]
  Automatic motivation:     [finding + evidence source]

Primary constraint(s): [1–2 sub-components]

Meaning-based barriers present? [yes/no; which family if yes]

Proposed intervention branch: [A / B / both]

Key moderators to test: [2–3 hypotheses]

Generalizability note: [what would need to hold for published evidence to transfer here]
```

---

## Common Research Mistakes (Behavioral Lens)

- **Asking hypothetical questions** — "Would you use this product?" People are systematically poor predictors of their own behavior. Always ask about specific past behavior or observe real choices.
- **Relying solely on stated preferences** — People say they want things they won't use. Triangulate with behavioral data wherever possible.
- **Only probing conscious reasoning** — Automatic motivation barriers (habit, shame, fear, ingrained distrust) live below deliberate awareness. They emerge in reconstruction and observation, not in abstract questioning.
- **Ignoring the physical and social context** — Individual attitudes explain less than context. Map the environment, not just the mindset.
- **Recruiting convenience samples** — The most constrained users have the most to tell you about friction and meaning barriers. Recruit them deliberately.
- **Confirming what you already believe** — Behavioral barriers are often uncomfortable to surface (distrust, shame, competing demands). Do not explain them away or filter them from synthesis.
- **Treating research findings as intervention recommendations** — Research reveals constraints and meanings; diagnosis and mechanism specification convert those into intervention hypotheses. These are separate steps.
