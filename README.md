# Productivity AI Skills

Skills I build and use with Claude. Each folder is one skill: a `SKILL.md` file with the instructions, plus any reference files it needs.

## ai-explain-me

AI can write a whole app or a ten-page contract in minutes, but I need hours to read it, and I don't want to approve things I don't understand. This skill turns large AI output into one artifact that explains it, so the person approving it knows what they are saying yes to.

For code, architecture and automation workflows it builds an interactive page with a clickable diagram. For contracts, policies and long copy it builds a document that follows the original section by section. Both cover the same ground, in this order:

1. What it is, in one sentence, with one analogy for the whole thing
2. What you asked for and what you got
3. A map of the parts
4. Each part in plain words
5. One real example traced from start to finish
6. The decisions the AI made for you
7. The risks, and what wasn't checked

It ends with a glossary, plus a short checklist when you are about to deploy, merge or sign.

Small pieces of work get a short answer in the chat instead, with an analogy and an inline diagram where it helps. Anything large, or anything that touches money, personal data, keys or legal obligations, gets the full artifact whatever its size.

### How to use it

Download the `ai-explain-me` folder and add it as a skill in Claude, or copy it into `~/.claude/skills/` if you use Claude Code. Then ask Claude to explain something an AI built for you ("walk me through what the agent built", "help me understand this contract before I sign"). When Claude writes something large itself, it will offer to explain it.
