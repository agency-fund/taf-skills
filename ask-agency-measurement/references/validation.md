# Validating measures (Step 3)

Use this to recommend the right checks for the tool chosen. A measure earns trust only when checked. Keep it proportionate — name the cheapest credible step, not a full psychometric program.

## Properties
- **Reliability** — consistent results; a prerequisite for validity.
- **Construct validity** — captures agency as defined, not mood/satisfaction/engagement.
- **Content validity** — covers the parts that matter, not just the easy ones.
- **Criterion validity** — tracks trusted outcomes (concurrent or predictive).
- **Convergent/discriminant** — correlates with the same thing, not different things.

## By tool type (compact)
- **Surveys:** content via expert review + cognitive interviews; reliability via alpha/omega, item-total, test-retest; structure via EFA/CFA (IRT for items). **Comparing groups/cultures:** translate + back-translate; test **measurement invariance** (configural→metric→scalar, usually MGCFA) and check **DIF** before comparing scores; watch response styles.
- **Observation/rubric:** train raters; report **inter-rater reliability** (Cohen's/Fleiss' kappa, Krippendorff's alpha, ICC); pilot and revise anchors.
- **Qualitative:** explicit codebook, second coder on a subset, triangulate.
- **Records:** check data quality and that the agency→outcome link is real and ordered.
- **LLM-as-a-measure (experimental):** validate for *your* prompt/settings/data. (1) Build a stratified human-coded gold standard. (2) Establish human inter-rater agreement first. (3) Compare model to human consensus (kappa/alpha/correlation; leave-one-rater-out for subjective tasks). (4) Examine disagreements for systematic bias. (5) Refine prompt against the labeled set; don't stack one unvalidated LLM to judge another. (6) Be explicit about reach — a transcript shows goal-*forming*, maybe not goal-*following*.

## Questions to recommend on
- Which property matters most for this claim, and what's the cheapest credible check next?
- Comparing groups? Then: invariance tested before comparing scores?
- For LLM measures: what's the gold standard, who builds it, do they agree?

Beyond standard checks, research the method (see `research-queries.md`). Treat validation as ongoing.
