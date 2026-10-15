# Running the workshop (phase 10)

The technical setup exists to serve one meeting: experts looking together at where they read the
same conversation differently, and deciding what the rubric should say. This is a short guide to
that meeting and the loop around it. The agenda is a template; adjust it to the group.

## The loop

```
draft rubric -> raters label on their own -> AI judge labels -> dashboard
      ^                                                            |
      +---- revise rubric <- decisions <- discussion in the room <-+
```

Noora's rounds followed it: Workshop 1 labelled Bangladesh conversations from before and after AI
assistance was introduced; Workshop 2 used 12 Yes/No questions on 200 Hindi conversations; Workshops 3 and 4
cut that to 7 questions with four answer options on 25 conversations each (hand-picked by experts
for 3, random for 4), assigned to the same group of raters. Each round was set up by copying the previous one and
changing what the last discussion decided.

## Roles

- **Owner**: decides the questions the workshop must answer, approves data use (export,
  translation, hosting). Often the program lead.
- **Facilitator**: runs the session, keeps time, records decisions. Should not be a rater.
- **Raters**: 4 to 6 people who know the work (clinicians, supervisors, program staff). An odd
  number avoids some ties.
- **Setup person** (with Claude): everything in phases 0 to 9.

## Timeline

| When | What |
|---|---|
| 2 weeks before | Owner signs off on data use and the rubric draft. Raters invited to Calibrate if they need accounts (labeling links don't need one). |
| 10 days before | Task created and checked by two people on the task page. |
| 1 week before | Links sent, each to its owner, with the briefing below. Labeling window opens. |
| 2 days before | `status` to see who's behind; nudge. Labeling closes the day before. |
| Day before | AI judge run; export downloaded; dashboard built and checked; facilitator picks the conversations to discuss. |
| After | Decisions written into `evaluators.json`; next round planned. |

## Briefing for raters (adapt and send with each link)

> You'll read [25] WhatsApp conversations between [patients and nurses] and answer [7] questions
> about each, for the conversation as a whole. Each message shows the original text and an English
> translation. Answer on your own, without discussing with others; disagreements are what we want
> to find. If a question doesn't fit a conversation, use "Not Applicable"; if the conversation
> doesn't show enough to decide, use "Not enough Information". A one-line reason for any answer
> you hesitated over helps the discussion a lot. This link is yours alone: it records answers
> under your name and opens without a login. It takes about [N] minutes per conversation; please
> finish by [date].

## Agenda (75 to 90 minutes)

1. **Why we're here (5 min).** What the rubric is for, what decisions today feeds.
2. **Overview tab (10 min).** Which questions people agreed on, and which they didn't. Don't
   dwell on the numbers; agree which 2 or 3 questions need the most time.
3. **Conversations, worst first (45 to 60 min).** Sort by most disagreement. For each chosen
   conversation: read the transcript aloud or give two minutes to read; open "Where raters part
   ways"; ask the dissenters to explain first, then the majority. Use the question focus filter to
   stay on one question across several conversations. Splits (ties) before single dissents.
4. **The AI (10 min).** Sort by "AI off the majority". Is the judge wrong, or is the question
   ambiguous in the same way it was for people? Judge-vs-human agreement can't be expected to beat
   human-vs-human agreement on the same question.
5. **Decisions (10 min).** Read back each change; assign who writes it into the rubric.

Ground rules worth saying out loud: disagreement is the point, not a mistake; nobody's agreement
rate is a score; the conversation is the evidence, not who said what.

## Recording decisions

Keep a short change log next to the rubric (a doc or `decisions.md` in the workshop folder). For
each question: what was unclear, the example conversation id, the change (new wording, new or
merged option, made optional, dropped), and who decided. These become the edits to
`evaluators.json` for the next round.

Typical changes:
- The question mixes two ideas: split it.
- An option is used for two different situations: define it on the option, or add an option.
- "Not Applicable" is the most common answer: narrow when the question applies, or make it optional.
- People need an external definition (a triage policy, a protocol): paste it into the options.
- The AI misreads the same thing every time: adjust `focus` or the option descriptions, then
  `update-evaluators` and rerun the judge on the same task to compare.

## Is it good enough?

There's no single bar. Rough guide for alpha (agreement corrected for chance) among humans: 0.8+
the rubric is ready to use; 0.67 to 0.8 usable with care; below that, keep iterating before
trusting anyone's labels, human or AI. When humans agree well, the AI's match rate with the human
majority tells you how far the judge can stand in for them on that question. Calibrate's
`calibrate-evaluator` skill (`setup.md`) helps tune a judge against the final human labels.

## The next round

See "Next workshop from the last one" in `SKILL.md`: copy settings, new prefix and task name,
apply the decisions, draw new conversations, same raters.
