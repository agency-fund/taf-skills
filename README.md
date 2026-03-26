# The Agency Fund Skills Repository

## Why We're Building This
At The Agency Fund, we have developed deep expertise in behavioral science, evaluation, and intervention design — expertise that took years to develop through our AI4GD Accelerator, our playbooks, and our partnerships with NGOs.

The problem is that this expertise lives in scattered documents, in people's heads, and in one-off workshops. It does not travel well. When a partner is making a product design decision at 11pm, they do not have access to our behavioral scientists. When a new product manager is designing a product solution, they may not know which behavioral science frameworks typically apply to our contexts.

An AI skills repository changes this. It embeds our repeatable motions directly into the AI tools our team and partners already use in a structured manner.

## What a Skill Is
Skills are folders of instructions, scripts, and resources that AI tools like Claude or ChatGPT or Coding Agents (e.g., Claude Code) loads dynamically to improve performance on specialized tasks. Skills teach your default AI how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

**Read more about SKILLS [here](https://github.com/anthropics/skills)**

A good skill explains:

- When to use this approach
- How to move through it step by step
- What a strong output looks like
- What to avoid

Skills are not comprehensive literature reviews. They are actionable decision-support tools. The behavioral science skill already in this repository is a useful model: it walks an AI system through diagnosis before intervention design, names the causal mechanism behind each recommendation, and distinguishes structural from meaning-based barriers. That level of specificity is the target.

## What We Should Build First
Our immediate priority is a small set of skills that reflect our highest-leverage frameworks. These map directly to the playbooks and tools we've already built through AI4GD, for instance, user funnels, behavioral science, AI evaluation, etc.

## How We Build Them
We convert existing materials — playbooks, workshop guides, tacit knowledge — into draft skills quickly. AI can help structure and clean these drafts, but speed matters more than polish at this stage. A usable rough draft is better than a delayed perfect one.

We then refine through use. As team members and partners apply skills in real projects, we learn what is missing or misleading. We update accordingly.

The most important test for any skill: **Can someone without the necessary domain knowledge apply it to a real partner situation without additional guidance?** If not, it needs more specificity.

## Who Contributes
This is not a side project for one person. Behavioral scientists, product managers, researchers, and program staff all hold relevant knowledge. Each should be able to add or edit skills directly, without a heavy review process. The goal is to create a collective, maintained knowledge for dogfooding and external share.

---

## How to Contribute a Skill

### Background Reading

Before building a skill, read [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf). It covers how skills are structured, how Claude loads them, and what makes a skill well-formed.

The short version: a skill is a folder with a `SKILL.md` file and optional supporting files. Claude loads the skill dynamically based on trigger phrases in the frontmatter, without requiring you to re-explain the workflow each time.

### Step 1: Build Your Skill with skill-creator

The easiest way to create a new skill is using the built-in **skill-creator** in Claude.ai:

1. Open [Claude.ai](https://claude.ai)
2. Go to **Customize → Skills → skill-creator**
3. Describe your use case in plain language. skill-creator will walk you through defining the trigger, steps, expected output, and generate a properly formatted `SKILL.md` draft
4. Iterate with skill-creator until the skill handles edge cases correctly

You can also write `SKILL.md` manually — see the file structure below.

### Step 2: Understand the File Structure

Each skill lives in its own kebab-case folder with the following structure:

```
your-skill-name/
├── SKILL.md              # Required — the main skill file (exact spelling, case-sensitive)
├── scripts/              # Optional — executable code (Python, Bash, etc.)
├── references/           # Optional — supporting documentation loaded on demand
└── assets/               # Optional — templates or other resources used in output
```

**Rules:**
- The folder name must be kebab-case (e.g. `behavioral-science`, not `Behavioral Science` or `behavioral_science`)
- The folder name must match the `name` field in the `SKILL.md` frontmatter
- Do **not** add a `README.md` inside the skill folder — all instructions go in `SKILL.md` or `references/`
- Keep `SKILL.md` under 5,000 words; move lengthy reference material to `references/`

**`SKILL.md` frontmatter format:**

```yaml
---
name: your-skill-name
description: What this skill does and when Claude should use it (under 1024 characters, no < or > characters)
license: MIT
metadata:
  author: Your Name
  version: 1.0.0
---
```

The `description` field drives when the skill activates — it must state both what the skill does *and* what phrases or contexts should trigger it.

### Step 3: Test Your Skill

Before submitting, verify that:
- The skill triggers on relevant queries (test 10–20 phrasings that should activate it)
- The skill does **not** trigger on unrelated queries
- The output matches what the skill promises

### Step 4: Submit to This Repository

1. Fork this repository and create a branch
2. Add your skill as a new folder at the top level of the repo (e.g. `your-skill-name/`)
3. Include all skill files: `SKILL.md`, any `scripts/`, `references/`, and `assets/` as needed
4. If you built the skill in Claude.ai, export the `.skill` file and include it in your folder as well — this lets others import it directly
5. Open a pull request with a short description of what the skill does and who it's for

### Installing a Skill from This Repo

To use a skill from this repository in Claude.ai:

1. Download or clone the repo
2. Zip the skill folder (e.g. `behavioral-science.zip`)
3. Go to **Claude.ai → Settings → Capabilities → Skills → Upload skill**
4. Select the zipped folder
5. Enable the skill, then test it by asking Claude to perform the target task

For Claude Code, place the skill folder in your Claude Code skills directory.