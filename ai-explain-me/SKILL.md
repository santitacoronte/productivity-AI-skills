---
name: ai-explain-me
description: Turn complex work that AI produced (large code changes, multi-file builds, system architectures, automation workflows, data pipelines, long contracts, policies or copy) into an explanation (an interactive diagram page or a document artifact for large or high-stakes work, a short chat answer for small pieces) that lets a human truly understand what was built, what was decided on their behalf, and what they are approving. Use this whenever the user asks to explain, walk through, break down, map, visualize or "help me understand" something an AI agent or chatbot built or wrote, says they feel lost in what was generated, or is about to approve, merge, deploy, sign or publish AI output. Also offer it proactively right after Claude itself produces a large or structurally complex result, even if the user did not ask.
---

# Explain AI Work

AI can produce in minutes what a person needs hours to read. The risk is that people approve work they do not understand. This skill puts the human back in the loop: it turns an AI result into an explanation sized to the work, usually one artifact that shows the shape of the work, explains every part in plain language with analogies, and exposes the decisions and risks hidden inside.

The reader can be anyone: a developer reviewing before a merge, a manager or client who asked for something, a learner, or a person checking whether what they imagined is what got built. Write for the least technical likely reader, and let technical readers go deeper through expandable detail.

## When to use it

- On request: "explain what you built", "walk me through this", "I don't understand this code", "what did the agent actually do", "map this architecture", "break down this contract".
- Proactively: after Claude produces a large result (roughly 150+ lines of code, several files, a system design, a workflow with many steps, or a long legal or business text), end the reply with a one-line offer, for example: "Want me to map out what I built so you can see how it fits together before you approve it?" Do not build the explanation unasked. Offer it once.

## Step 1. Gather the real material

Explain what actually exists, never what probably exists.

- Read the files, the conversation, the diff, the workflow JSON or the document itself. If the work came from another agent or chatbot, ask for it or find it in attachments before writing anything.
- Note the user's original request in their own words. The explanation must connect back to it: what they asked for, and how the result answers it.
- Where something cannot be verified (code that was not run, a dependency not inspected, a clause whose legal effect depends on jurisdiction), mark it as unverified in the artifact. Honesty about limits is part of the job.

## Step 2. Decide the size: chat answer or full artifact

Match the format to the size of the work and what is at stake. A full artifact for a 30-line function wastes the reader's time, and a chat answer for a 20-file system loses them.

**Small: answer in chat.** Use this when all of these are true:
- the work is small: one file or function under about 150 lines, a workflow of 5 steps or fewer, a text under about 2 pages, or a question about one part of something larger ("what does this function do?")
- nothing is about to be deployed, merged, signed or published
- it does not touch money, personal or health data, passwords and keys, or legal obligations

A chat answer keeps the same spirit in a few short paragraphs: what it is in one sentence with an analogy, how it works, any decision or risk worth knowing, and technical terms explained where they appear. Add an inline diagram when the structure helps (the Visualizer, where the session has it). Close with a one-line offer to turn it into a full artifact if they want to share it or keep it.

**Large or high-stakes: build the full artifact.** Use this when any of these is true:
- the work is bigger than the small limits above
- the person is about to deploy, merge, sign, publish or approve it
- it touches money, personal or health data, passwords and keys, or legal obligations, whatever its size
- the person asks for something to share, keep or show someone else, or asks for an artifact, page or document

Stakes beat size: a 40-line payment handler going to production gets the full artifact. When unsure, choose the artifact, because the cost of an unread page is smaller than the cost of approving something misunderstood.

The rest of this skill describes the full artifact. For a chat answer, use the same rules from Steps 5 and 6 (analogies, plain words) at a smaller scale.

## Step 3. Pick the artifact

| What was built | Artifact | Why |
|---|---|---|
| Code, software architecture, APIs, databases, automation workflows, data pipelines, integrations, infrastructure | **Graphic artifact**: an interactive HTML page with a diagram at its center | Structure is spatial. People understand systems by seeing boxes and arrows before reading words. |
| Contracts, policies, terms, proposals, long copy, reports, prompts or text-based specs | **Document artifact**: a Docs artifact (or HTML document if no Docs type exists) with a clause-by-clause or section-by-section breakdown | Text work is read in order. The explanation follows the original's order and annotates it. |
| Mixed (for example an app plus its terms of service) | Graphic artifact, with a document section for the text part | The structure carries the rest. |

Creation mechanics: list the session's Artifact types first. Use the Docs type for document artifacts. For graphic artifacts, load the `artifact-design` and `artifact-diagramming` skills before writing the page, then publish with the Artifact tool. If no artifact tool exists, write a self-contained HTML file and send it.

## Step 4. Build the explanation in layers

Every explanation has the same seven layers, in this order. Layers move from "what is this" to "what should worry me". A reader can stop after any layer and still leave with something true and useful.

1. **In one sentence.** What this is and what it does, with no jargon. Then the anchor analogy (see Step 5) in two or three sentences.
2. **What you asked for vs what you got.** The original request, and how the result meets it. Call out anything added that was not asked for, and anything asked for that is missing or only partly done.
3. **The map.** For graphic artifacts: one diagram of the main parts and how they connect, no more than 7 to 9 boxes at the top level. Group the rest inside them. Each box carries a plain name ("Login checker"), with the technical name underneath ("auth_middleware.py"). For documents: a short outline of the sections with one line each on what they do.
4. **The parts, one by one.** For each part on the map: what it does, its analogy, what it receives and what it hands on, and where it lives (file, node, clause). Clicking a box in the diagram should open its card. Technical detail (function names, key lines, the exact clause wording) goes in a collapsed "For the technical reader" section.
5. **Follow one real example through.** Pick one concrete scenario and trace it step by step through the parts: "Maria signs up with her email. First the form sends... then...". For contracts: "If the client pays 30 days late, clause 7 applies, then clause 12...". This is the layer where understanding clicks, so make the example specific and realistic, and use diverse names and settings.
6. **Decisions made for you.** Every choice the AI made that the user did not explicitly ask for: libraries, frameworks, database type, hosting assumptions, data formats, default values, error handling, pricing terms, liability caps, tone of voice. For each: what was chosen, a plausible alternative, the trade-off in one line, and how hard it is to change later (easy, moderate, hard). These are the hidden approvals, so be thorough.
7. **Risks and blind spots.** What could go wrong and what was not checked: security (passwords, keys, user data), data loss, cost (API calls, cloud bills that scale), performance at larger scale, legal exposure, missing tests, edge cases not handled, assumptions about the user's environment. Rate each as high, medium or low, and say in plain words what the consequence would look like ("anyone with the link could read every customer's address").

Close with a **Glossary**: every technical, legal or domain term used anywhere in the artifact, explained in one plain sentence, ideally with a mini analogy. If a term appears in the artifact, it appears in the glossary. Terms in the body link or point to it.

If the user is about to approve, merge, deploy, sign or publish, add a short **"Before you say yes"** list after layer 7: three to seven concrete checks they can do themselves, phrased as questions ("Did you test signing up with a real email?").

## Step 5. Analogies

Analogies are the core of this skill, not decoration. A good analogy lets a non-expert predict how the system behaves.

- **Choose one anchor analogy for the whole system** and map every major part onto it. A web app as a restaurant: the front end is the dining room, the API is the waiter, the database is the pantry, authentication is the host checking reservations. One consistent world beats a different metaphor per part.
- **Pick from universal experiences** that work across countries and industries: restaurants, post offices, airports, libraries, warehouses, building construction, kitchens, hospital reception desks, train networks. Avoid sports, holidays or pop culture tied to one country.
- **Say where the analogy breaks.** One line per major part if it misleads: "Unlike a real waiter, the API never remembers you between visits." This prevents false understanding.
- **Match the analogy to the risk.** When explaining a security gap, keep using the anchor world: "the pantry door is unlocked" lands harder than "the endpoint lacks authorization".
- See `references/analogy-library.md` for tested analogy sets by type of system and text.

## Step 6. Writing rules

- Short, direct sentences. One idea per sentence.
- Plain words first, technical term second, in brackets or underneath: "a holding area for tasks (a queue)".
- Numbers over adjectives: "calls the payment service 3 times per order", not "calls it frequently".
- No hype and no reassurance. Do not tell the reader the work is great or that they have nothing to worry about. Describe and let them judge.
- Never use em dashes. Use commas, colons or full stops.
- Keep it proportional. A 200-line script needs a short page. A 40-file system needs the full seven layers with grouping. Cut anything that does not help the reader understand or decide.

## Step 7. Check before delivering

- Every box on the map corresponds to something that really exists in the work.
- Every term used is in the glossary.
- The worked example matches the actual logic (trace it against the code or text, do not guess).
- Decisions and risks are specific to this work, not generic advice that would apply to any project.
- The page renders, the diagram is legible in light and dark mode, and clicking parts works.

Then deliver with one or two sentences: what the artifact covers and the one thing the reader should look at first (usually the top risk or the biggest decision made for them).
