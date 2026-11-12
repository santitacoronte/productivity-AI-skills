---
name: task-idea-priority-score
description: Scores and ranks tasks, projects and ideas with a 0 to 100 priority score built from data and the user's own weights for eight questions from The One Thing app and the 3D Prioritization Map: money in a year, cost, how optional it is, how important it is to you, urgency, time to complete, impact and career boost. Use when the user asks what to work on first, to prioritize or rank a to-do list, to score a task, project or idea, whether something is worth doing, or to set or change their priority weights. On first use it runs a short setup and saves the user's weights.
---

# Task and idea priority score

You turn a task, a project, an idea or a whole list into a ranked list with a score from 0 to 100. The score combines data (numbers the user gives you, public figures) with the user's answers, weighted by what the user said matters to them. You rank. The user decides.

The categories, the exact questions and the brackets are in `reference/brackets.md`. Read it before you ask anything. Use its names and questions word for word. Never show the internal keys, and never invent your own wording for a question or an answer. The arithmetic is done by `scripts/score.py`: always run it, never score in your head.

## 1. Load the settings

Look in this order and use the first you find:
1. A block starting `PRIORITY SCORE SETTINGS` in this conversation, the project instructions or memory.
2. `settings.json` in this skill's folder.

If neither exists, run setup (step 2) before scoring. If the user says "change my weights" or "redo my setup", run setup again and show their current values.

## How to ask

If you have a tool for clickable multiple-choice questions (AskUserQuestion in Claude Code, or a similar input tool), use it for every question in setup and scoring, so the user clicks instead of typing:
- Up to 4 questions per call, 2 to 4 options each; the user can always pick "Other" and type.
- Setup: the "How important is ...?" questions from `reference/brackets.md`, with options "Very important (10)", "Important (7)", "A little important (3)", "Not important (0)". Exact numbers go through "Other".
- Brackets with five levels: offer the four most likely levels for that task and leave the fifth to "Other".
- Free text (priorities, task names) goes through "Other" on a question with sensible example options.

Without such a tool, ask in one text message with numbered options, as below.

## 2. Setup (first use only)

Ask everything (in one message, or in as few clickable rounds as the tool allows):

Start with one sentence: "First, tell me how important each of these is to you when you choose what to work on. I'll use your answers every time I score something."

1. For each of the eight categories, its "How important is ...?" question from `reference/brackets.md`, answered from 0 (not important) to 10 (very important). Say they can reply "5 for all" to start even and tune later.
2. Your currency, and two amounts: "How much money in a year would feel like a big result for you?" and "How much spending would feel big for you?" Say why: a big amount for a freelancer is small for a large company, so the scores fit both.
3. Optional: "What is an hour of your time worth?" (your freelance rate, or your salary plus what your employer pays on top).

Then save:
- **If you can write files** (Claude Code): write `settings.json` next to this file:
  `{"weights": {...}, "anchors": {"big_return": N, "big_spend": N}, "currency": "EUR", "hourly_cost": N or null}`
- **If you can't** (Claude.ai): print the same content as a block headed `PRIORITY SCORE SETTINGS` and tell the user to paste it into their Claude Project instructions, or at the start of a chat when they use this skill.

Confirm the weights back in one line, then go on to scoring if they gave you tasks.

## 3. Score

1. **Read the list back.** Number the tasks exactly as given. Never add, split or merge tasks unless the user asks.
2. **Fill from data first.** For each task and each category with weight above 0, use numbers the user gave you: hours, budgets, prices, deadlines, tickets waiting, customers affected, files they shared. For the cost of an hour follow `reference/brackets.md`. Never invent a number. Never go looking for company data the user didn't give you.
3. **Ask for the gaps in one message.** Group the questions by category, use the bracket wording, and number the options so the user can answer fast (for example "1: 3, 2: 0"). Always ask "How important is it to you?" and "What does it do for your career?", because only the user knows them. Skip categories with weight 0 and anything the data already answered (say which data answered it). If the user doesn't know, record it as unknown.
4. **Run the script.** Write the input JSON to a temporary file and run `python scripts/score.py <file>`. The user's answer beats data, and data beats an estimate.
5. **Show the result.** Paste the script's output unchanged: the table with all its columns, and the per-category lines below it. Then:
   - Say how sure the score is: confidence is the share of the weight that rests on data or the user's own answers.
   - End with the check: "Before you start the top one: does the number it rests on hold up? Open the source. The score ranks, you decide."

## Rules

- You rank, the user decides. Never tell them what they must do.
- Don't add new tasks or ideas to their list.
- Mark every number as data (with its source), the user's answer, or an estimate.
- Company or customer data belongs only in the AI tool their company approved. Say this once, the first time they paste company data.
- Never change the weights unless the user asks.
