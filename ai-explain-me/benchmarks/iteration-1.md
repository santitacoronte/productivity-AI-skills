# Benchmark: iteration 1

Run on 4 November 2026 with Claude Opus 5.5. Each test case ran once with the skill and once without it, on the same prompt and the same input files. The full data is in `iteration-1.json`.

This run tested the first draft of the skill, before the size rule was added (the rule that sends small work to a chat answer instead of an artifact).

## Results

| Test case | With skill | Without skill |
|---|---|---|
| Clinic booking app, 9 files, before deploying | 10/10 | 4/10 |
| n8n workflow (Stripe to HubSpot and Slack), for a non-technical manager | 10/10 | 6/10 |
| Freelance services contract, before signing | 12/12 | 9/12 |
| **Total** | **32/32 (100%)** | **19/32 (58%)** |

| | With skill | Without skill |
|---|---|---|
| Average time per run | 394 s | 116 s |
| Average tokens per run | 136,385 | 101,106 |

## What the numbers show

Both versions found the same problems in all three cases: the hardcoded email key and open admin pages in the app, the unprotected webhook and customer data posted to a public Slack channel in the workflow, and the seven one-sided clauses in the contract. The skill did not make Claude find more risks.

The difference is in how the findings reach the reader. With the skill, every result had a diagram or clause map, one analogy carried through the whole explanation, one real example traced from start to finish, a list of the decisions the AI made, and a glossary. Without it, the results were lists of findings that assumed the reader already knew the terms.

The baseline did one thing better. It ended with a clear verdict ("approve the plan, not this version") and concrete changes to ask for. The skill has no instruction to give a go or no-go answer yet.

The skill costs about 3.4 times the time and 35% more tokens per run.
