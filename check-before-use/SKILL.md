---
name: check-before-use
description: Checks a piece of AI-generated text before the user forwards, sends or acts on it. Use when the user pastes or attaches a draft, memo, email, report or AI answer and says "check this", "check before I use it", "is this right", "can I send this", or similar. Lists every fact and number with a source or "no source", redoes every calculation, flags contradictions inside the text, and says what would make the main conclusion wrong. Never rewrites the text.
---

# Check before use

The user wants to know if a text is safe to use. Check it. Do not rewrite it, polish it or summarise it.

## Steps

1. **Facts and numbers.** List every fact and every number in the text. For each one give a source the user can open (a full link), or write "no source". Never invent a source. If you can search the web, search; if you can't, say so and mark the item "no source".
2. **Math.** Redo every calculation in the text. Show the math on one line each. Mark each one "correct" or "wrong, should be X".
3. **Contradictions.** Point out any place where the text says one thing and later says or assumes the opposite. Quote both lines.
4. **Weak spot.** Say what would make the main conclusion wrong, in two or three sentences.

## Output

Four short sections with the headings above, in that order. End with one line: "Fix before sending:" followed by the items that need fixing, or "Nothing found" if the four checks found nothing.

If the user gave no text, ask them to paste it.
