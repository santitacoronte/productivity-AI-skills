# Productivity AI Skills

Claude skills I build and use in my own work. Each folder is one skill: a `SKILL.md` file with the instructions Claude follows, plus any reference files it needs.

## ai-explain-me

### Why it exists

AI agents can now write a whole app, an automation or a ten-page contract in minutes, but reading and understanding that work still takes a person hours. So people end up approving things they don't fully understand. They merge the code, switch on the workflow or sign the contract, and trust that it does what they asked.

ai-explain-me puts the person back in the loop. It turns what the AI built into an explanation you can follow even if you aren't technical, so you know what you are approving before you approve it.

It's useful for a developer reviewing AI-written code before a merge, a manager who has to sign off an automation, a freelancer reading a contract a chatbot drafted, or anyone checking that what got built matches what they had in mind.

### What you get

Ask Claude to explain something an AI built or wrote for you ("walk me through what the agent built", "help me understand this contract before I sign"). The explanation gives you:

- a map of the parts and how they connect
- one analogy for the whole thing, kept the same from start to finish: an app as a restaurant, a workflow as an assembly line, a contract as building a house together
- one real example followed step by step through the system, so you see it working
- the decisions the AI made for you without asking, and how hard each one is to change later
- the risks, rated high, medium or low and written in plain words ("anyone with the link could read every patient's details")
- a glossary for every technical or legal term it uses

When you are about to deploy, merge or sign, it also adds a short list of checks you can do yourself before saying yes.

When Claude builds something large on its own, it offers once to explain it. It doesn't build the explanation unless you say yes.

### How it decides the format

The skill answers two questions, in this order.

**1. Is the work small and low-stakes?** It counts as small when it is under about 150 lines of code, a workflow of 5 steps or fewer, under about 2 pages of text, or a question about one part of something bigger. It also has to be low-stakes: nothing about to go live or be signed, and nothing touching money, personal or health data, passwords and keys, or legal obligations.

If both are true, you get a short answer in the chat, with an analogy and an inline diagram where it helps. If either is false, you get a full artifact. A 40-line payment handler going to production gets the full artifact, because what is at stake counts more than size.

**2. If it's an artifact, which kind?** That depends on how a person naturally reads the work.

- Work made of parts that connect (code, apps, architecture, automation workflows, data pipelines) gets an interactive page with a clickable diagram. You understand these by seeing the pieces and the arrows between them.
- Work you read from top to bottom (contracts, policies, proposals, long copy) gets a document that follows the original section by section, like notes in the margin.
- Mixed work, such as an app with its terms of service, gets the diagram page with a document section for the text.

| You ask | You get |
|---|---|
| "What does this 30-line function do?" | A chat answer |
| "Explain the 9-file booking app before I deploy it" | A diagram page |
| "Help me understand this contract before I sign" | A document |
| "What does clause 7 mean?" | A chat answer, or the full document if you are about to sign |

### How it works

Claude follows the same steps every time.

1. It reads the real material: the files, the workflow, the contract and your original request. It explains only what exists, and it marks anything it couldn't verify, like code it didn't run or a clause whose effect depends on local law.
2. It decides the size and the format, as described above.
3. It builds the explanation in seven layers, moving from "what is this" to "what should worry me". You can stop reading after any layer and still come away with something true and useful.
   1. What it is, in one sentence, with the analogy
   2. What you asked for and what you got, including anything added or missing
   3. The map of the parts
   4. Each part in plain words, with technical detail tucked into a collapsed section
   5. One real example traced from start to finish
   6. The decisions made for you
   7. The risks, and what wasn't checked
4. It writes in plain language: short sentences, the plain word first and the technical term after it, numbers instead of adjectives, and no hype or reassurance. It describes what it found and leaves the judgment to you.
5. It checks its own work before handing it over. Every box on the map has to exist in the real work, every term has to be in the glossary, and the traced example has to match the actual logic.

The analogies come from `references/analogy-library.md`, which has ten sets: web apps, APIs, data pipelines, automations, AI agents, databases, infrastructure, contracts, policies and marketing copy. They use experiences that work across countries and industries (restaurants, post offices, libraries, assembly lines), and each set says where the analogy stops being accurate, so it doesn't leave you with a wrong picture.

### How to install it

Download the `ai-explain-me` folder and add it as a skill in Claude, or copy it into `~/.claude/skills/` if you use Claude Code. There is nothing else to set up.

### Tests and benchmarks

The `evals` folder has three test cases: a clinic booking app, an n8n workflow that sends Stripe payments to HubSpot and Slack, and a freelance services contract. Each one lists the checks a good result should pass. The sample app contains deliberate security problems for the skill to find (the email key in it is fake), so don't deploy it.

The `benchmarks` folder has the results of running each test with and without the skill. In the first run the skill passed 32 of 32 checks, against 19 of 32 without it. Both versions found the same risks, but only the skill version made them understandable to someone outside the field. [benchmarks/iteration-1.md](ai-explain-me/benchmarks/iteration-1.md) has the details.
