# Core Behavioral Science Frameworks

This file is the shared knowledge base for all modes. It contains the frameworks, theories,
and evidence sources that inform behavioral science reasoning across diagnosis, intervention
design, measurement, and user research.

**How to use these frameworks:** No single framework is maximally useful for any given problem.
Each one illuminates a different aspect of behavior — COM-B asks what is constraining action,
EAST asks how to redesign the path of least resistance, MINDSPACE asks which psychological
mechanism to activate, SDT asks whether motivation will outlast the program. The frameworks
work best in combination, as overlapping lenses, not as a decision tree that terminates at a
single answer. The job is to help users think through their specific problem, population, and
context — not to match a question to a label and stop there.

**The diagnostic principle (from Szaszi et al., 2025):** Behavioral interventions have much
smaller average effects than the published literature suggests, and their effects vary enormously
across populations, implementation details, settings, and outcomes. This means no framework
or intervention type should be recommended with high confidence until the mechanism has been
specified and the contextual conditions for that mechanism have been verified. Treat framework
recommendations as hypotheses to test, not solutions to deploy.

**The two intervention classes:** Most frameworks in this file apply to *choice architecture* —
changing the environment, cues, defaults, or information context to shift behavior. The Wise
Interventions framework (Section 10) is categorically different: it targets how people
*interpret themselves and their situation*, not the environment around them. Before selecting
frameworks, establish which class of problem you're facing. See `diagnosis.md` for the full
diagnostic process, including the Branch A / Branch B distinction.

---

## 1. COM-B Model and the Behaviour Change Wheel (BCW)

**Source:** Michie, van Stralen & West (2011). *The behaviour change wheel: A new method for
characterising and designing behaviour change interventions.* Implementation Science, 6:42.

COM-B is the diagnostic hub of the **Behaviour Change Wheel (BCW)** — a three-layer framework:
- **Hub:** COM-B (the behaviour system — what must change for the behaviour to occur)
- **Middle ring:** 9 Intervention Functions (types of activities that address COM-B deficits)
- **Outer ring:** 7 Policy Categories (actions that enable or support those interventions)

### The COM-B Behaviour System

Behaviour occurs when Capability, Opportunity, and Motivation are sufficient and aligned. These
components interact — opportunity shapes motivation, motivation shapes capability, and performing the
behaviour itself feeds back to alter all three. The system is bidirectional, not linear.

**Capability** — The individual's psychological and physical *capacity* to engage in the behaviour:
- **Psychological capability:** Capacity to engage in necessary thought processes (comprehension,
  reasoning, memory, decision-making). Includes knowledge and cognitive/emotional skills.
- **Physical capability:** Physical capacity to perform the behaviour (strength, stamina, motor
  skills, physical health).

**Opportunity** — All factors *outside* the individual that make the behaviour possible or prompt it:
- **Physical opportunity:** Afforded by the environment — resources, tools, time, access, materials.
- **Social opportunity:** Afforded by the cultural milieu — norms, language, social cues, the concepts
  available to people for making sense of the world.

**Motivation** — All brain processes that *energize and direct* behaviour. This is broader than
"intentions" — it includes both conscious and unconscious drivers:
- **Reflective motivation:** Conscious evaluations and plans — intentions, goals, perceived value,
  beliefs about outcomes, decision-making.
- **Automatic motivation:** Emotions and impulses arising from associative learning and/or innate
  dispositions — habits, emotional responses, desires, drives, inhibitions. These operate largely
  below conscious awareness.

> **Critical nuance:** Most social programs assume behavior is reflective (people decide, then act).
> In reality, automatic motivation — habit, emotion, conditioned response — often dominates.
> An intervention that addresses only reflective motivation (e.g., awareness campaigns, information)
> will fail when the true barrier is automatic (e.g., ingrained habit, emotional avoidance).

### The 9 Intervention Functions

Once the COM-B constraint is identified, select from these nine functions. A given intervention
may combine more than one.

| Function | Definition | Primary COM-B target |
|---|---|---|
| **Education** | Increasing knowledge or understanding | Psychological capability, Reflective motivation |
| **Persuasion** | Communication to induce positive/negative feelings or stimulate action | Reflective motivation, Automatic motivation |
| **Incentivisation** | Creating expectation of reward | Reflective motivation, Automatic motivation |
| **Coercion** | Creating expectation of punishment or cost | Reflective motivation, Automatic motivation |
| **Training** | Imparting skills | Physical capability, Psychological capability |
| **Restriction** | Rules to reduce opportunity for competing behaviours | Physical opportunity, Social opportunity |
| **Environmental restructuring** | Changing the physical or social context | Physical opportunity, Social opportunity, Automatic motivation |
| **Modelling** | Providing an example to aspire to or imitate | Automatic motivation, Social opportunity |
| **Enablement** | Increasing means/reducing barriers beyond education and training | Psychological capability, Physical opportunity |

### The 7 Policy Categories (Outer Ring)

Policies enable interventions but do not change behaviour directly:
Communication/Marketing, Guidelines, Fiscal measures, Regulation, Legislation,
Environmental/social planning, Service provision.

**When to use COM-B/BCW:** Start here for any diagnostic question. The BCW is most powerful
when you need to move systematically from diagnosis → intervention type → policy enabler.
The most common mistake in program design is treating a motivation or opportunity problem
with education (a capability fix). COM-B prevents this by forcing constraint identification first.

---

## 2. EAST Framework

**Source:** Behavioural Insights Team (BIT), 2014. *EAST: Four Simple Ways to Apply Behavioural Insights.*

EAST is a practitioner-facing design rule: **if you want to change a behavior, make it Easy,
Attractive, Social, and Timely.** It is intentionally pragmatic — a quick-start diagnostic
checklist for applying behavioral science to real-world policies, products, and programs. It is
not a comprehensive theory of behavior, and the BIT explicitly stresses that interventions should
always be tested and adapted to context. Use EAST alongside COM-B (for diagnosis) and MINDSPACE
(for psychological levers) — EAST tells you *which bottleneck to target*; the other frameworks
tell you *why that bottleneck exists*.

---

### Easy — Reduce Effort, Mental and Physical

The central insight: people often fully intend to act but don't, because of friction. Tiny barriers
have disproportionately large effects. The target is effort reduction — both cognitive (how hard it
is to decide) and physical (how many steps it takes to act).

**Key tactics:**
- **Defaults** — Pre-set the desired option. People strongly tend to stick with whatever requires
  no active choice. Opt-out pension enrollment dramatically outperforms opt-in because doing nothing
  becomes the path to the desired outcome.
- **Reduce friction** — Every additional step costs action. Shorten forms, pre-fill information,
  eliminate unnecessary documentation, compress the path to the behavior.
- **Simplify messaging** — Short, clear, single-action messages outperform comprehensive information.
  Tell people exactly what to do, not everything they might want to know.

---

### Attractive — Make the Behavior Noticeable and Appealing

People act on what grabs attention and feels rewarding. This goes well beyond incentive size —
framing and design determine whether a behavior registers as worth doing.

**Key tactics:**
- **Salience and framing** — How something is presented matters as much as what it is. Put the
  most important information where it will actually be seen. Lead with consequences that feel real.
- **Personalization** — "This specifically applies to you" increases engagement far more than
  generic messaging. Use names, relevant data, and personal stakes.
- **Behaviorally designed incentives** — Incentives are more effective when:
  - Framed as *avoiding a loss* rather than *gaining a benefit* (loss aversion: losses hurt ~2x
    more than equivalent gains feel good)
  - Tied to identity or social image ("people like you do this")
  - Structured with gamification elements (streaks, milestones, visible progress)

> The key insight is that it's not about *adding* more incentives — it's about how existing
> incentives and information are *designed and framed*.

---

### Social — Use Norms and Networks

People are heavily influenced by what others around them do and approve of. Behaviors also spread
through social networks, meaning interventions can have multiplier effects beyond direct recipients.

**Key tactics:**
- **Descriptive norms** — "Most people like you do X." Communicating what is normal and common
  is one of the most reliable levers in behavioral science. Effective examples: social norm
  letters for tax compliance, energy use comparisons with neighbors.
- **Social networks** — Behaviors spread through connections. Design for contagion: if one person
  changes, consider how that flows to peers. Recruit change within existing networks.
- **Commitment and reciprocity** — Public commitments increase follow-through. Reciprocity norms
  (people return favors) can be activated through small prior acts of support or trust.

**Critical caveat — the boomerang effect:** Poorly framed norm messages can backfire. If the
message implies that the *undesired* behavior is normal ("many people don't comply"), it can
*increase* non-compliance. Always message the *desired* norm, not the gap. Norm messages work
when they tell people the right behavior is already widespread, not when they inadvertently
announce that deviance is common.

---

### Timely — Intervene When People Are Most Receptive

Even a well-designed intervention will fail if delivered at the wrong moment. Timing is often
the difference between behavior change and behavior ignored.

**Key tactics:**
- **Moments of change** — Life transitions (new job, new child, moving, illness, graduation)
  destabilize existing habits and make people more open to new behaviors. These "fresh start"
  moments are disproportionately effective intervention windows.
- **Present bias** — People overweight immediate costs and benefits relative to future ones.
  Make immediate rewards salient and immediate costs of inaction visible. The further away a
  benefit feels, the less it motivates.
- **Planning prompts** — Help people bridge the gap between intention and action by asking them
  to make a concrete plan: when, where, and how they will do the behavior. This converts
  vague intention into specific commitment (implementation intentions).

---

### Using EAST as a Diagnostic Checklist

When a behavior isn't happening at the rate you want, work through EAST as a quick diagnostic:

| Question | EAST lever | If yes, try... |
|---|---|---|
| Is it too hard or too many steps? | Easy | Simplify, add defaults, reduce friction |
| Is it going unnoticed or feeling unappealing? | Attractive | Salient framing, loss framing, personalization |
| Is it socially unsupported or invisible? | Social | Norm messaging, peer channels, network activation |
| Is the timing wrong or too abstract? | Timely | Intervene at moments of change, use planning prompts |

**When to use EAST:** Intervention design, communications, and choice architecture — especially
when you need a fast, structured way to audit an existing touchpoint or brief a non-specialist team.
EAST complements COM-B (which identifies *why* the behavior isn't happening) and MINDSPACE
(which identifies *which* psychological mechanisms to target). Use them together.

---

## 3. MINDSPACE

**Source:** Dolan, Hallsworth, Halpern, King & Vlaev (2010). *MINDSPACE: Influencing Behaviour
through Public Policy.* Cabinet Office / Institute for Government, UK.

MINDSPACE is a policy-oriented behavioral checklist. Its core argument is that governments and
programs typically try to change behavior through laws, incentives, and information — but people
do not respond as fully rational actors. Behavior is also shaped by context, social cues, defaults,
emotions, and identity in ways that operate largely below conscious awareness. MINDSPACE names
nine of the most robust such influences and asks practitioners to actively design around them.

**What MINDSPACE is not:** A standalone formula or a replacement for conventional policy tools.
The report is explicit that these levers should *complement* — not fully substitute for — structural
and regulatory approaches. It also stresses that many governments are *already* shaping behavior
through these channels unintentionally, so MINDSPACE is equally useful for auditing existing
policies as it is for designing new ones.

---

### The Nine Influences

| Letter | Influence | What it means in practice |
|---|---|---|
| **M** | **Messenger** | Who delivers a message shapes how it is received, often more than the content itself. Authority, peer identity, and trust determine credibility. A health message from a community health worker may land differently than the same message from a government poster. |
| **I** | **Incentives** | Our responses to rewards and penalties are distorted by cognitive biases. Loss aversion means losses feel roughly twice as painful as equivalent gains feel good. Incentives should be framed around avoiding losses, not just earning rewards. Size alone is less important than framing and timing. |
| **N** | **Norms** | We are strongly influenced by what we perceive others to do and approve of. Descriptive norms ("most people in your area do X") are powerful even when people are unaware of their influence. Social proof is one of the most replicated findings in behavioral science. |
| **D** | **Defaults** | We tend to stick with pre-set options, especially under uncertainty or complexity. Changing a default — from opt-in to opt-out, or from blank to pre-filled — can have larger effects than any incentive or information campaign. |
| **S** | **Salience** | We notice and respond to what is novel, simple, and personally relevant. Information competes for attention; design for the message that will actually be seen and felt, not just communicated. |
| **P** | **Priming** | Subconscious cues in the environment can shape subsequent behavior and choices, often without people's awareness. The words, images, and symbols present at a decision point influence what mental associations become active. |
| **A** | **Affect** | Emotions and affective associations drive decisions. People respond to how things *feel*, not just what they rationally imply. An emotionally resonant message or cue often outperforms a more logically complete one. |
| **C** | **Commitments** | We are motivated to behave consistently with prior commitments and to reciprocate acts of trust or generosity. Public commitments, written pledges, and commitment devices increase follow-through by activating consistency norms. Reciprocity can also be leveraged: small prior acts of support from a program build a felt obligation. |
| **E** | **Ego** | We act in ways that protect or enhance our self-image. People are more likely to adopt behaviors that are consistent with how they see themselves or aspire to be seen. Identity-based framing ("be a voter" vs. "vote") can be more effective than behavioral instruction alone. |

---

### How to Use MINDSPACE

The report pairs MINDSPACE with a complementary implementation framework — the **6 Es** — which
gives the *process* for using these levers within a broader policy cycle:

| Step | What it means |
|---|---|
| **Explore** | Understand the behavioral context before designing anything |
| **Enable** | Ensure structural conditions are in place for the behavior to occur |
| **Encourage** | Apply MINDSPACE levers to make the behavior more likely |
| **Engage** | Involve communities and stakeholders in design |
| **Exemplify** | Use government/institutional behavior itself as a signal |
| **Evaluate** | Test and measure rigorously — especially through RCTs where possible |

MINDSPACE identifies *what* psychological levers to pull. The 6 Es describe *how* to put them
into practice within an accountable policy or program process.

---

### Important Cautions

- **Ethics and legitimacy:** The report is candid that some MINDSPACE applications — especially
  priming, affect, and ego — can feel manipulative if not transparent. Behavior change policies
  require public permission and should be disclosed. The question is not just "does it work?" but
  "is it legitimate here?"
- **Personal responsibility:** These tools can be perceived as removing agency. The report
  recommends defaulting to interventions that preserve choice rather than restrict it.
- **Context dependency:** None of the nine levers work universally. Effects vary by population,
  channel, and local context. Always test before scaling.

**When to use MINDSPACE:** Designing and auditing communications, messaging, and touchpoints —
especially when you need to move beyond information and ask which *psychological mechanism* is
being engaged. MINDSPACE is strongest for identifying the lever; COM-B is stronger for first
establishing which behavioral constraint that lever needs to address. Use them in sequence.

---

## 4. Fogg Behavior Model (FBM / B = MAP)

**Source:** Fogg, B.J. (2009). *A Behavior Model for Persuasive Design.*
Persuasive Technology Lab, Stanford University.

For a target behavior to occur, three factors must be present *at the same moment*:
**Motivation**, **Ability**, and a **Trigger** (sometimes called Prompt). If any one is missing,
the behavior will not happen regardless of how strong the other two are.

> **Core diagnostic principle:** When a behavior isn't occurring, ask in sequence:
> Are they sufficiently motivated? Is the behavior simple enough to do? Is there a trigger at the
> right moment? The answer tells you exactly where to intervene.

---

### Factor 1: Motivation

Motivation places a person higher or lower on the FBM's vertical axis. Three core motivators,
each with two sides:

| Motivator | Positive side | Negative side | Notes |
|---|---|---|---|
| **Pleasure / Pain** | Pleasure | Pain | Immediate, primitive response. Operates in the moment without deliberation. |
| **Hope / Fear** | Hope | Fear | Anticipation of a future outcome. Fear (anticipated loss) is often more powerful than pleasure/pain. |
| **Social Acceptance / Rejection** | Acceptance | Rejection | Deeply wired social drive. Much of social behavior is governed by the desire to belong and avoid ostracism. |

**Design implication:** When motivation is the deficit, identify *which* motivator is most
relevant to the audience and context. Hope is generally the most ethical and empowering choice.
Fear and pain carry higher risk of psychological harm or reactance.

---

### Factor 2: Ability (Simplicity)

Ability is not about teaching or training — it is about *simplicity*. People resist learning
new things because it requires effort. The path to increasing ability is making the behavior easier,
not building capacity. The right question is: *What resource is scarcest for this person at the
moment the trigger fires?*

Six elements of simplicity, which function like links in a chain — if any one breaks, the
behavior is no longer simple:

| Element | What breaks it | Practitioner implication |
|---|---|---|
| **Time** | The behavior takes more time than the person has available | Shorten steps; compress time required |
| **Money** | The financial cost is prohibitive for this person | Reduce or remove cost barriers |
| **Physical effort** | The behavior demands physical exertion beyond what's feasible | Remove physical barriers; create access |
| **Brain cycles** | The behavior requires more cognitive effort than available | Simplify decisions; reduce options; use defaults |
| **Social deviance** | Performing the behavior requires going against norms | Normalize the behavior; use social proof |
| **Non-routine** | The behavior is unfamiliar and not yet habitual | Build on existing routines; anchor to existing habits |

**Key insight:** *Simplicity is a function of a person's scarcest resource at the moment a
behavior is triggered.* What is simple for one person is not simple for another. Always assess
simplicity relative to this specific population and this specific context. In low-income contexts,
brain cycles and money are frequently the binding constraints — not motivation.

**Motivation and ability trade off:** People with lower motivation may still perform a behavior
if it is simple enough. Conversely, people with high motivation will sometimes find ways to
overcome low ability. This means: before adding more motivation (which is difficult and often
resisted), ask whether making the behavior simpler would cross the activation threshold.
*In most cases, simplicity interventions are faster, cheaper, and more effective.*

---

### Factor 3: Triggers

A trigger tells a person to perform the behavior *now*. Without a trigger, even people with
sufficient motivation and ability will not act — they simply never get the cue. The FBM identifies
three types, each suited to a different motivaton-ability profile:

| Trigger type | When to use | What it does | Examples |
|---|---|---|---|
| **Spark** | Person has ability but low motivation | Pairs the trigger with a motivating element (hope, fear, social acceptance) | Emotionally resonant message, loss-framing reminder, story |
| **Facilitator** | Person has motivation but low ability | Triggers the behavior *and* makes it easier simultaneously | "One click," pre-filled form, address book uploader, "it only takes 2 minutes" |
| **Signal** | Person has both motivation and ability | Simply reminds — no motivation or simplification needed | SMS reminder, notification, calendar prompt, traffic light |

**Critical principle:** Mismatch between trigger type and user profile creates negative
experience. A spark sent to someone who is already motivated but unable to act is frustrating.
A facilitator sent to someone who has no motivation is ineffective. Always diagnose the
motivation-ability profile *first*, then design the trigger type accordingly.

**Successful triggers must:** (1) be noticed by the person, (2) be associated with the target
behavior, and (3) arrive when the person is both motivated and able to act.

---

### Using FBM as a Diagnostic Tool

When a behavior isn't happening:

1. **Motivation deficit?** → Use a spark trigger. Identify which core motivator (hope, fear,
   social) is most relevant and design around it.
2. **Ability deficit?** → Use a facilitator trigger. Identify which simplicity element is the
   bottleneck (often brain cycles or time) and reduce it.
3. **Trigger missing?** → Add a signal trigger. If motivation and ability are already sufficient,
   a simple reminder may be all that's needed.

The FBM can also guide **behavior prevention**: to stop an unwanted behavior, remove or weaken
one of the three factors — reduce motivation, increase friction (reduce ability), or remove the trigger.

**When to use FBM:** Product and service design, digital flows, onboarding, habit formation,
SMS-based programs, and any context where behavior change requires repeated action through
technology-mediated touchpoints. Especially useful when simplification (not motivation) is the
primary lever — which is more common than practitioners assume. Pairs well with COM-B: use
COM-B to diagnose whether the barrier is capability, opportunity, or motivation; then use FBM
to precision-design the trigger and simplicity approach.

---

## 5. Dual-Process Theory (System 1 / System 2)

**Sources:** Kahneman, D. (2011). *Thinking, Fast and Slow.* Building on: Stanovich & West (2000);
Evans (1984, 2008); Sloman (1996); Strack & Deutsch (2004).

Dual-process theory holds that human cognition operates through two qualitatively different
processes. The System 1 / System 2 terminology was coined by Stanovich and West (2000) and
popularized by Kahneman — but the underlying idea traces back to William James and has been
independently developed across social psychology, cognitive psychology, and behavioral economics.

---

### System 1 — Automatic, Implicit Processing

System 1 operates continuously, in parallel with everything else, requiring little or no effort.

**Core characteristics:**
- **Fast and automatic** — Responses are generated immediately, without deliberate initiation
- **Associative** — Works by activating networks of associations, patterns, and prior experience
- **High capacity** — Can process many streams of information simultaneously
- **Emotionally bonded** — Strongly integrated with affect; feelings shape System 1 outputs
- **Habit-driven** — Learned behaviors become automatic and are very difficult to consciously change
- **Implicit and unconscious** — The process itself is not accessible to introspection; only its outputs surface in awareness

**What System 1 produces:**
Impressions, intuitions, feelings, and impulses. These outputs are offered to System 2, which
typically endorses them without scrutiny. The vast majority of everyday decisions — where to
look, how to feel about a person, whether something seems risky — are System 1 outputs.

**When System 1 is accurate:**
System 1 is not inherently unreliable. In domains of genuine expertise with fast, consistent
feedback (e.g., expert clinicians, social dynamics, skilled craftwork), System 1 intuitions can
be highly accurate. System 1 fails predictably when patterns from the past don't match the
current situation — which is common in novel, high-stakes, or statistically complex contexts.

---

### System 2 — Controlled, Explicit Processing

System 2 is engaged when a situation demands effortful reasoning.

**Core characteristics:**
- **Slow and deliberate** — Requires consciously directing attention and working through steps
- **Serial** — Can only process one demanding task at a time; easily overloaded
- **Capacity-limited** — Depends on working memory, which is finite and depletes with use
- **Explicit and conscious** — Reasoning is accessible; people can report on it
- **Flexible** — Can apply rules, consider counterfactuals, and override System 1 when it detects an error
- **Volatile and changeable** — Subject to persuasion, learning, and attitude change

**The lazy supervisor problem:**
System 2 is the system people *think* is in charge. In reality, it functions more as a
lazy endorser — it tends to accept System 1's outputs with minimal checking unless something
triggers suspicion. This is why people can be highly confident in incorrect intuitions and
why interventions targeting rational deliberation often fail to change behavior.

---

### How the Two Systems Interact

The *default-interventionist* model (Kahneman, Evans & Stanovich) best describes their
relationship: System 1 continuously generates default responses; System 2 can intervene and
override, but usually doesn't.

**Cognitive ease vs. cognitive strain:**
- When processing feels *easy* (familiar stimuli, fluent presentation, relaxed state), System 1
  dominates — people rely on intuition and heuristics.
- When processing feels *strained* (unfamiliar, complex, ambiguous, or emotionally disrupted),
  System 2 is recruited — but this is effortful and cognitively costly.
- The implication: making a message harder to process does *not* automatically trigger better
  reasoning. It often triggers disengagement instead.

**Ego depletion:**
System 2 is a limited resource. After effortful decision-making, people have less capacity for
deliberate reasoning and revert more heavily to System 1. This is especially important in
contexts of poverty and stress, where cognitive load is chronically elevated.

---

### System 1 Heuristics and Systematic Biases

Because System 1 operates on pattern-matching and association, it generates predictable errors
in specific classes of situations:

| Heuristic/Bias | Mechanism | Design implication |
|---|---|---|
| **Availability heuristic** | Frequency judged by ease of recall, not actual rate | Vivid, recent, emotionally charged examples feel more probable than they are |
| **Representativeness heuristic** | Probability judged by resemblance to a prototype | Stereotyping; ignoring base rates |
| **Anchoring** | Initial number anchors all subsequent estimates | First number in a negotiation or form shapes all responses |
| **Affect heuristic** | Overall feeling toward an object shapes judgments of its risks and benefits | Liked things feel safe; disliked things feel risky |
| **Framing effects** | Logically identical choices feel different when described differently | "90% survival rate" vs. "10% mortality rate" produce different choices |

---

### Key Nuances and Limitations

**It is a useful simplification, not a literal brain architecture.** Kahneman himself described
System 1 and System 2 as "useful fictions" — characters that help organize observations about
cognition, not distinct brain regions or independent modules. Critics (notably Gigerenzer et al.)
argue that many System 1 heuristics are ecologically rational — they work well in real environments
even if they fail in laboratory tasks designed to expose their limits.

**The systems are not fully separable.** Research suggests many cognitive processes involve both
types of processing simultaneously or in rapid alternation. The clean binary is a
pedagogically useful simplification of a more continuous reality.

---

### Design Applications

**When to design for System 1:**
- Routine behaviors, repeated choices, habit formation
- Situations of low cognitive resources (stress, poverty, fatigue, time pressure)
- When you want the desired behavior to be automatic — use defaults, environmental cues,
  social norms, simplification, and habit anchoring
- Most behavior change targets in social sector programs fall here

**When to design for System 2:**
- High-stakes, one-time, or irreversible decisions where deliberation genuinely matters
- Contexts where System 1 biases are producing specific, identifiable errors
- When the goal is attitude or belief change over time (persuasion, education)

**The diagnostic question:** Before designing any intervention, ask: *Is this behavior primarily
System 1 or System 2? Am I designing for the system that actually controls it?* Most programs
over-invest in System 2 interventions (information, awareness, attitude change) for behaviors
that are fundamentally System 1 (habit, impulse, social default).

---

## 6. Cognitive Bias Codex — Four-Cluster Model

**Source:** Benson, B. (category model); Manoogian III, J. (visualization, 2016).
Based on Wikipedia's list of cognitive biases (~188 biases organized into four functional clusters).

The Codex organizes all known cognitive biases under four root problems the brain is solving.
Understanding which cluster a bias belongs to tells you *why* it exists and *what kind of
intervention can address it.* The four clusters form a closed system — each is a response to
a real constraint, and the solutions they produce create the next constraint.

> **One-line summary:** We filter → we fill in → we shortcut → we compress.

---

### Cluster 1: Too Much Information → We Filter

The brain cannot process everything in the environment, so it selects what to attend to.
This is adaptive — but it introduces systematic blind spots.

**What the brain does:**
- Pays disproportionate attention to what is **vivid, recent, novel, or emotionally striking**
- Notices information that **confirms existing beliefs** and discounts what contradicts them
- Is drawn by **salience, familiarity, and contrast** rather than statistical importance

**Key biases in this cluster:**

| Bias | Meaning | Applied example |
|---|---|---|
| **Confirmation bias** | We seek and remember information that confirms what we already believe | Program staff interpret ambiguous data as evidence the intervention is working |
| **Availability heuristic** | We judge frequency by how easily examples come to mind | Vivid stories of success distort perceived impact rates |
| **Salience bias** | Prominent, novel, or emotionally charged information gets weighted too heavily | A dramatic failure story overrides years of positive data |
| **In-group bias** | We favor and trust people from our own group | Messenger credibility varies sharply by perceived identity |
| **Negativity bias** | Negative events register more strongly than equivalent positive ones | Fear appeals can dominate even when positive framing would serve better |
| **Attentional bias** | Attention gravitates toward stimuli related to existing concerns or fears | People under financial stress attend to cost information disproportionately |

**Design implication:** You cannot rely on people noticing your message just because you sent it.
Salience must be deliberately engineered. The information that gets processed is the information
that is personally relevant, emotionally resonant, or contextually prominent — not the most
objectively important.

---

### Cluster 2: Not Enough Meaning → We Fill In

The world is incomplete, ambiguous, and full of gaps. The brain constructs a coherent story
from partial information — but the story it builds is shaped by existing beliefs, mental models,
and the need for things to make sense.

**What the brain does:**
- **Sees patterns** even when evidence is thin or random
- **Makes quick causal explanations** that may not reflect actual causation
- **Assumes its own perspective is the obvious or correct one**
- Fills gaps using **stereotypes, prior experience, and plausible-sounding narratives**

**Key biases in this cluster:**

| Bias | Meaning | Applied example |
|---|---|---|
| **Narrative bias** | We organize experience into stories even when causality is unclear | Program attribution errors: crediting an intervention for coincidental improvements |
| **Stereotyping** | We apply group-level characteristics to individuals | Beneficiary assumptions about willingness or ability based on demographic categories |
| **Halo effect** | Positive impression in one domain spreads to unrelated domains | Charismatic field staff rated as more effective regardless of actual outcomes |
| **Just-world bias** | We believe people get what they deserve | Blame directed at beneficiaries for poor program uptake instead of design failure |
| **Projection bias** | We assume others share our knowledge, preferences, or perspective | Designers assume beneficiaries find a product intuitive because they do |
| **Clustering illusion** | Random sequences are perceived as containing meaningful patterns | Misreading random variation in pilot data as evidence of real effects |

**Design implication:** The stories people tell themselves about your program — why it works,
who it's for, whether outcomes are fair — matter as much as the program mechanics. Reframing
the narrative around a behavior is a legitimate and often underused intervention lever.

---

### Cluster 3: Need to Act Fast → We Shortcut

Decisions often must be made under time pressure, incomplete information, and competing
demands. The brain uses fast rules of thumb that work well in familiar environments but
produce systematic errors in novel or complex ones.

**What the brain does:**
- **Prefers immediate rewards** over larger but delayed ones (present bias, hyperbolic discounting)
- **Sticks with defaults** and avoids the effort of active choice (status quo bias)
- **Avoids losses more strongly** than it seeks equivalent gains (loss aversion)
- Makes **overconfident or emotion-driven decisions** under pressure

**Key biases in this cluster:**

| Bias | Meaning | Applied example |
|---|---|---|
| **Present bias** | Immediate costs/benefits are overweighted relative to future ones | Savings: the immediate friction of depositing outweighs the abstract future benefit |
| **Loss aversion** | Losses feel ~2× as painful as equivalent gains feel good | Frame as "don't lose your subsidy" rather than "earn a bonus" |
| **Status quo bias** | We prefer the current state and resist change | Opt-out enrollment dramatically outperforms opt-in |
| **Hyperbolic discounting** | We are inconsistent over time, preferring smaller sooner over larger later | Commitment devices work by binding the future self to the present self's intentions |
| **Anchoring** | Initial numbers or information shape all subsequent estimates | First number in a loan offer anchors perception of what is normal or affordable |
| **Overconfidence** | We systematically overestimate our ability and the accuracy of our beliefs | Beneficiaries over-estimate their likelihood of following through on intentions |
| **Scarcity mindset** | Cognitive bandwidth is reduced when resources are scarce | Low-income populations face a persistent cognitive tax that simplification can partially offset |
| **Risk aversion / risk-seeking asymmetry** | We are risk-averse for gains but risk-seeking to avoid losses | Loss framing can motivate action even among otherwise risk-averse populations |

**Design implication:** This cluster is where most behavioral interventions operate — defaults,
loss framing, commitment devices, simplification, and timely prompts all directly counter
Cluster 3 biases. When behavior is not happening despite awareness and intention, a Cluster 3
shortcut is usually the primary barrier.

---

### Cluster 4: Limited Memory → We Compress

Memory is reconstructive, not reproductive. The brain does not store full records of
experience — it stores edited highlights, shaped by emotion, meaning, identity, and what
it expected to find.

**What the brain does:**
- **Remembers highlights** (the peak and the end) rather than duration or full detail
- **Edits memories retrospectively** to fit current beliefs and self-image
- **Recalls things that fit identity, expectations, or existing beliefs** more readily
- **Simplifies complex experiences** into clean, coherent narratives

**Key biases in this cluster:**

| Bias | Meaning | Applied example |
|---|---|---|
| **Peak-end rule** | We judge an experience by its most intense moment and how it ended | A difficult enrollment process is remembered by its worst friction point, not its average |
| **Rosy retrospection** | Past experiences are remembered more positively than they were | Clients recall program benefits more favorably over time, complicating self-report data |
| **Consistency bias** | We misremember our past beliefs as more similar to current ones than they were | Baseline recall is often distorted by current behavior — undermines retrospective surveys |
| **Self-serving bias** | Successes are attributed internally; failures externally | Beneficiaries credit themselves for outcomes the intervention caused; or vice versa |
| **Fading affect bias** | Negative emotions attached to memories fade faster than positive ones | Recall of past barriers to behavior is systematically underestimated over time |
| **Telescoping effect** | Recent events feel more distant; distant events feel more recent | Recall-based measurement of behavior frequency is systematically distorted |

**Design implication:** Self-report measurement is vulnerable to Cluster 4 biases across the
board. Time-stamped administrative data outperforms recall wherever possible. Where surveys
are necessary, anchor questions to specific recent events ("in the last 7 days") rather than
general patterns.

---

### Using the Four Clusters as a Diagnostic

When a behavior or program is not performing as expected, use the clusters to locate the
cognitive failure:

| Symptom | Most likely cluster | Response |
|---|---|---|
| People aren't noticing or engaging with the intervention | Cluster 1 (filtering) | Increase salience, relevance, emotional resonance |
| People misunderstand the program or draw wrong conclusions | Cluster 2 (filling in) | Reframe narrative, address stereotypes, reduce ambiguity |
| People intend to act but don't follow through | Cluster 3 (shortcuts) | Defaults, simplification, loss framing, commitment devices |
| Outcome data or self-reports don't add up | Cluster 4 (compression) | Switch to administrative data, anchor recall to specific events |

Biases from different clusters often co-occur. A program failure can involve salience failures
(Cluster 1), a misconceived beneficiary narrative (Cluster 2), present bias (Cluster 3), and
distorted outcome recall (Cluster 4) simultaneously. Use this framework to systematically
consider all four rather than stopping at the first plausible explanation.

---

## 7. Self-Determination Theory (SDT)

**Source:** Ryan, R.M. & Deci, E.L. (2000). *Self-Determination Theory and the Facilitation of
Intrinsic Motivation, Social Development, and Well-Being.* American Psychologist, 55(1), 68–78.
Building on: Deci & Ryan (1985).

SDT is a theory of human motivation and personality that studies the social and contextual
conditions that facilitate — versus forestall — the natural human tendencies toward growth,
self-motivation, and psychological integration. Its central claim: people can be proactive and
engaged, or passive and alienated, largely as a function of the social environments in which they
develop and function. This makes SDT directly relevant to the design of programs, services, and
institutional contexts that aim to support sustained behavior change.

---

### The Three Basic Psychological Needs

SDT posits three innate psychological needs that function like nutrients: when satisfied, they
support well-being and self-motivation; when thwarted, they produce diminished motivation,
alienation, and ill-being. All three must be met — a context that satisfies two but thwarts
the third still produces impoverishment.

**Competence** — The need to feel effective and capable in one's interactions with the environment.
People need to experience mastery, efficacy, and growth. Optimal challenges and positive
effectance-promoting feedback satisfy competence; demeaning evaluation, repeated failure, and
tasks beyond or far below one's capabilities thwart it.

**Autonomy** — The need to feel volitional — that one's behavior originates from one's own values
and sense of self rather than from external pressure.

> **Critical nuance:** Autonomy does NOT mean independence, individualism, or detachment.
> It refers to the *feeling of volition* that can accompany any act, whether collectivist or
> individualist, whether dependent or independent. Research in Korean and US samples found a
> more positive relation between autonomy and collectivistic attitudes than between autonomy
> and individualistic attitudes. In global development contexts, autonomy is fully compatible
> with communal, family-centered, or collectivist cultures.

**Relatedness** — The need to feel connected to and cared for by others — to belong, to matter,
and to contribute positively to the lives of others. A secure relational base is especially
important for supporting the expression of both intrinsic motivation and the internalization
of externally prompted behaviors.

---

### The Motivation Continuum (Organismic Integration Theory)

SDT rejects the idea that motivation is a single quantity (more vs. less). Instead, motivation
varies in *type* — in how self-determined or externally controlled it is. This is the most
practically important insight for program design: the *kind* of motivation a program creates
predicts whether behavior will persist after the program ends.

The continuum runs from non-self-determined to fully self-determined:

| Type | What it means | Program design implication |
|---|---|---|
| **Amotivation** | No intention to act; person doesn't value the behavior, feels incompetent, or doesn't expect it to yield results | Don't assume motivation exists; address the need that is most thwarted |
| **External regulation** | Acts to get rewards or avoid punishment; fully controlled; external locus of causality | Compliance while rewards exist; stops when they end; can feel controlling and alienating |
| **Introjected regulation** | Behavior is internally driven but not genuinely accepted; motivated by guilt avoidance, shame, or ego-protection | Unstable; produces anxiety and poor coping with failure; effort without engagement |
| **Identified regulation** | Consciously values the behavior and sees it as personally important; more autonomous | More engagement, better coping, higher quality performance; behavior more likely to persist |
| **Integrated regulation** | Behavior is fully assimilated to the self and congruent with personal values and identity | Most autonomous form of extrinsic motivation; durable, high-quality, authentic |
| **Intrinsic motivation** | Done for the inherent satisfaction of the activity itself; naturally self-determined | Highest quality learning, creativity, vitality, and persistence; requires supportive conditions |

**The key practitioner implication:** Externally regulated behaviors (driven by incentives,
surveillance, pressure) *reliably undermine* intrinsic motivation when those controls are
removed. Programs built on control and compliance produce behavior that stops when the program
does. Programs that support autonomy, competence, and relatedness produce behavior that persists.

---

### What Undermines Motivation

The paper is specific about what thwarts the needs and diminishes motivation:

- **Tangible rewards contingent on task performance** — a comprehensive meta-analysis confirmed
  that all expected, contingent, tangible rewards reliably undermine intrinsic motivation
- **Threats, deadlines, directives, and pressured evaluations** — shift locus of causality external
- **Imposed goals and surveillance** — undermine autonomy even when well-intentioned
- **Controlling teaching, parenting, or program delivery styles** — students/beneficiaries
  taught with controlling approaches show diminished initiative and lower quality learning
- **Cold, uncaring, or unresponsive relational contexts** — thwart relatedness and undermine
  intrinsic motivation even when autonomy and competence are nominally supported

---

### What Supports Motivation and Internalization

For behaviors that are *not* intrinsically interesting (most program-target behaviors), the goal
is *internalization* — moving the person from external regulation toward identified or integrated
regulation. Three conditions facilitate this:

- **Autonomy support** — Provide meaningful rationale for the behavior, acknowledge feelings,
  offer choice wherever possible, minimize pressure and control. Even for non-optional behaviors,
  framing and tone matter: "you can" and "if you choose" outperform "you should" and "you must."
- **Competence support** — Offer optimal challenges (not too easy, not too hard), provide
  positive and informational (not controlling) feedback, avoid demeaning evaluations.
- **Relatedness support** — Ensure the person feels genuinely connected to and cared for by
  program staff, community members, or peers. People internalize values and behaviors promoted
  by people to whom they feel (or want to feel) attached.

Providing a meaningful rationale + autonomy support + relatedness support, together, predict
the deepest form of internalization (integrated regulation).

---

### Needs Are Universal, Expression Is Cultural

The three needs are theorized to be universal and essential across cultures and developmental
stages. However, *how* they are expressed and satisfied varies. In more collectivist cultures,
autonomy may be satisfied through contribution to family or community goals rather than
individual choice. Competence may be expressed through shared mastery rather than individual
achievement. Relatedness may take different forms of connection and belonging. This means SDT
applies cross-culturally, but program design must be culturally sensitive to how each need can
be meaningfully supported in the local context.

---

### Applied Evidence Across Domains

The paper reviews SDT evidence across health care, education, work, sport, and community
settings. Key findings directly relevant to social sector programs:

- Greater internalization of health behavior regulation predicts better medication adherence,
  better long-term weight maintenance, improved glucose control, and greater attendance in
  addiction treatment
- In education, autonomy-supportive instructors produce more intrinsic motivation, curiosity,
  better learning quality, and lower dropout
- In the workplace, satisfaction of all three needs independently predicts performance and
  well-being
- Within-person daily fluctuations in autonomy, competence, and relatedness satisfaction
  directly predict same-day mood, vitality, and self-esteem

**When to use SDT:** Any time you are concerned with motivation that outlasts the intervention
itself — when incentives will end, when staff will leave, when the program concludes. SDT
provides both a diagnostic (which need is being thwarted?) and a design toolkit (how do we
create conditions that support need satisfaction?). It is especially relevant when beneficiaries
seem apathetic, disengaged, or dependent — these are often symptoms of thwarted needs, not
character deficits. Use alongside COM-B to first confirm which type of motivational barrier
is operative.

---

## 8. BASIC Framework (Behaviour, Analysis, Strategies, Intervention, Change)

**Source:** OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit.*

A full policy cycle framework for applying behavioral insights from problem definition through scaled implementation. Five stages:

- **Behaviour** — Define the specific behavioral problem. Use a *behavioral reduction* to map all relevant behaviors; apply a *priority filter* to select the highest-leverage target behavior. Define a SMART outcome.
- **Analysis** — Diagnose why the behavior is or isn't happening using the **ABCD sub-framework** (see below). Use process maps, user journey maps, and behavioral flowcharts to understand the actual context.
- **Strategies** — Translate the diagnosis into specific behavioral interventions, organized around the ABCD constraints.
- **Intervention** — Design and run a rigorous test (ideally an RCT or quasi-experiment) before scaling.
- **Change** — Scale what works, monitor for unintended consequences, and sustain behavior over time.

**ABCD Diagnostic Sub-Framework:**

| Dimension | What it means | Policy example |
|---|---|---|
| **Attention** | People's attention is limited and easily distracted; they often miss or forget key information | Forgetting medical appointments; defaulting to status quo because they don't notice alternatives |
| **Belief Formation** | People rely on heuristics and often over/underestimate probabilities; confirmation bias distorts reasoning | Overconfidence, planning fallacy, misperception of social norms |
| **Choice** | Choices are shaped by framing, context, and social influences — not just rational preference maximization | Being swayed by default options, anchoring effects, peer behavior |
| **Determination** | Even people with good intentions struggle to sustain behavior; present bias and self-control failures are widespread | Intention-action gap; failing to follow through on savings, health, commitments |

**Guiding questions per ABCD dimension:**
- *Attention:* Is the intervention well-timed? What's capturing attention in this context? Is there a default if people are inattentive?
- *Belief formation:* What are people's prior beliefs? How does context interact with belief formation?
- *Choice:* What makes a choice attractive? How is it framed? What social context is shaping it?
- *Determination:* What are the friction points? Do people have concrete plans? Is there feedback?

**When to use:** BASIC is the strongest choice when working within public sector or policy contexts, or when you need a full project methodology (not just a framework for analysis). It integrates ethical guidelines at every stage — a major advantage when working with vulnerable populations. The ABCD sub-framework complements COM-B: use ABCD when you need to connect diagnosis to specific intervention strategies quickly in a policy context.

**Ethical guidelines are built in:** BASIC includes specific ethical checkpoints at each stage covering privacy, consent, unintended consequences, and equity of impact. Flag these when designing interventions with low-income or marginalized populations.

---

## 9. Wise Interventions Framework

**Source:** Walton, G.M. & Wilson, T.D. (2018). *Wise Interventions: Psychological Remedies for Social and Personal Problems.* Psychological Review, 125(5), 617–655.

A social-psychological framework for designing brief, theory-driven interventions that target the *subjective meanings* people draw about themselves, others, and social situations. Unlike nudges (which change choice architecture) or skill-building (which changes capacity), wise interventions change how people *interpret* their circumstances — often with outsized, recursive effects.

**Core insight:** Many social problems persist not because people lack resources or ability, but because they've developed maladaptive meanings — about their competence, their belonging, or their circumstances — that generate self-defeating cycles. A well-targeted meaning change, delivered at the right moment, can break this cycle and produce lasting gains.

**Three families of wise interventions:**

| Family | Addresses | Core techniques | Examples |
|---|---|---|---|
| **Need to Understand** | Maladaptive attributions and beliefs about self, others, or situations | Attribution retraining, growth mindset, implementation intentions, leading questions | "People like me belong here" — social belonging intervention; growth mindset; reframing teacher feedback |
| **Need for Self-Integrity** | Threat to one's sense of being adequate, moral, and competent | Value affirmation exercises, precommitment, hypocrisy induction, saying-is-believing | Value affirmation closing racial achievement gaps; commitment devices; invoking voter identity |
| **Need to Belong** | Threats to social connection and feelings of acceptance | Bolstering social connectedness, social norms, linking goals to community | Social belonging interventions; working-together norms; prosocial purpose framing |

**Five defining principles:**

1. **Specificity** — Target a specific meaning, not a general disposition. "Think positive" doesn't work; identifying the precise interpretation driving behavior does.
2. **Systems thinking** — Meanings operate within complex systems. An intervention only helps if the structural conditions to act on the new meaning are already in place.
3. **Recursive change** — Initial meaning shifts can become self-sustaining: new interpretations drive new behaviors, which create new environments, which reinforce the new interpretation. Brief interventions can produce multi-year gains.
4. **Methodological rigor** — Start small with RCTs. Scale only after field evidence. Poorly understood interventions can backfire.
5. **Ethical care** — Because these interventions work "below the radar," they require particular attention to autonomy, consent, and potential for harm.

**Change techniques:**
- *Direct labeling* — Provide a positive identity label the person internalizes
- *Prompting new meanings* — Offer new facts, leading questions, or changed situations that imply a new interpretation without imposing it
- *Saying-is-believing* — Ask people to explain an idea to others, so they advocate for it and personalize it
- *Active reflection exercises* — Open-ended writing prompts (value affirmation, expressive writing, mental contrasting)
- *Commitment through action* — Precommitment, effort justification, hypocrisy induction

**When to use:** Wise interventions are most powerful when the primary barrier to behavior change is a *psychological meaning* rather than a structural constraint or capability gap — particularly when identity threat, self-doubt, or belonging uncertainty are in play. They are especially relevant for social sector programs working with stigmatized or marginalized populations, or for any context where behavior change needs to be durable after the program ends. Combine with COM-B to first confirm that a meaning-based barrier is actually the primary constraint.

**Caution on value affirmation:** Strong evidence shows value affirmation works when threat is high and exit is costly. But it can backfire when people are failing at a task and can easily disengage — allowing them to accept failure without self-threat.

---

## Framework Selection Guide

This guide is a starting point for collaborative reasoning, not a lookup table. The right
combination of frameworks for any problem depends on what the behavior actually is, who the
population is, what constraints are operative, and what context the intervention will live in.
Use this to orient the conversation, then go deeper with the relevant framework sections.

---

### Phase 1 — Diagnose First

Before any framework selection, establish what the behavior gap actually is and which
constraint is primary. The full diagnostic process lives in `diagnosis.md`. The key
branching question:

> *Is the primary barrier structural/environmental (capability, access, friction, cues,
> defaults, norms) — or is it meaning-based (how people interpret themselves, their
> circumstances, or whether they belong)?*

- **Structural/environmental barrier → Branch A (choice architecture frameworks)**
- **Meaning-based barrier → Branch B (Wise Interventions)**
- **Both → design for both; address structural conditions first**

---

### Phase 2 — Select Frameworks as Overlapping Lenses

No single framework covers the full design space. The most useful combinations depend
on the problem type:

**Understanding why the behavior isn't happening:**
Start with **COM-B/BCW** to map which of the six sub-components (psychological capability,
physical capability, physical opportunity, social opportunity, reflective motivation, automatic
motivation) is the primary constraint. This tells you which *type* of intervention is
warranted before you consider any specific tactic.

**Diagnosing within motivation (what kind of motivation problem?):**
- If the barrier is about present bias, habit, or impulse → **Dual-Process** + **Bias Codex (Cluster 3)**
- If the behavior needs to outlast incentives or program support → **SDT** (what kind of
  motivation is being created — external regulation or genuine internalization?)
- If the meaning people make of their situation is the barrier → **Wise Interventions**

**Designing the intervention:**
- For choice environment redesign → **EAST** (which friction/salience/social/timing lever?)
  combined with **MINDSPACE** (which psychological mechanism within that lever?)
- For full policy or program design → **BASIC/ABCD** (which stage of the policy cycle?
  what ABCD barrier?)
- For digital or product contexts → **Fogg B=MAP** (is the bottleneck motivation, ability,
  or trigger?)
- For meaning-based barriers → **Wise Interventions** (which family — understanding,
  self-integrity, or belonging?)

**Communicating or messaging:**
- **MINDSPACE** for identifying which psychological influence to leverage (messenger,
  incentive framing, norms, defaults, salience, priming, affect, commitment, ego)
- **Bias Codex (Cluster 1)** for understanding which filtering and salience dynamics
  are shaping whether the message registers at all

**Sustaining behavior over time:**
- **SDT** to assess whether the program is building genuine internalization or dependence
  on external regulation — and what social conditions would support the former
- **Dual-Process** to assess whether the behavior has become automatic (System 1) or
  still requires deliberate effort (System 2)

**Designing measurement:**
- **COM-B** for indicator mapping (what behavioral mediators should be measured?)
- **Bias Codex (Cluster 4)** for assessing threats to self-report validity (memory
  compression, retrospective distortion, consistency bias)

---

### Phase 3 — Check Generalizability Before Committing

Once frameworks and candidate interventions are identified, run the generalizability probe
from `diagnosis.md` (Part C) before recommending deployment:

- Can the mechanism be specified precisely — what causal chain is expected?
- Are the contextual conditions for that mechanism present here?
- Does the evidence base match across population, treatment, outcome, setting, and analysis?
- What is the realistic effect size after adjusting for publication bias and WEIRD-sample
  inflation?
- What would indicate the mechanism fired (not just that the outcome changed)?

If the mechanism cannot be specified, or if fewer than 3 of 5 generalizability dimensions
match the evidence base, treat the intervention as a hypothesis and build in local testing
before scaling.

---

### Quick Orientation — Which Frameworks Are Most Relevant?

Use this as a starting point for conversation, not a terminal answer:

| Problem type | Primary frameworks to engage | Secondary lenses |
|---|---|---|
| Why isn't behavior happening at all? | COM-B / BCW | BASIC/ABCD, Dual-Process |
| Behavior happens once but doesn't persist | SDT, Dual-Process (habit) | COM-B (automatic motivation) |
| People intend to act but don't follow through | Fogg B=MAP, EAST (Easy) | Bias Codex (Cluster 3), COM-B |
| Environmental or structural design | EAST, MINDSPACE | BASIC, BCW intervention functions |
| Communication and messaging strategy | MINDSPACE, EAST (Attractive) | Bias Codex (Cluster 1) |
| Digital product or mobile flow | Fogg B=MAP | EAST, Dual-Process |
| Full policy or program design | BASIC / ABCD | COM-B, EAST |
| Behavior change for stigmatized or marginalized populations | Wise Interventions + COM-B | SDT |
| Identity, belonging, or self-doubt as the barrier | Wise Interventions | SDT (autonomy + relatedness) |
| Motivation that must outlast the program | SDT | Wise Interventions, Dual-Process |
| Understanding a specific cognitive distortion | Cognitive Bias Codex | Dual-Process |
| Behavior varies dramatically across contexts | Generalizability probe + COM-B | BASIC (ABCD moderators) |
| Measurement design for a behavior change program | COM-B | Bias Codex (Cluster 4), SDT |

The most important habit is to resist stopping at one framework. Every problem benefits
from at least two lenses: one that explains the *mechanism of constraint*, and one that
guides *how the intervention should be designed*.
