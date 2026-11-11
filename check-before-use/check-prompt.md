# The check prompt

The same four checks as the skill, as a prompt you can paste into any AI. Copy the AI's answer first, then paste this prompt. In a snippet tool, `{clipboard}` drops the copied text in for you.

```
Check the text below before I use it. Don't rewrite it.
1. List every fact and number in it. For each one, give a source I can open, or write "no source".
2. Redo every calculation and show the math.
3. Point out anything that contradicts something else in the text.
4. Tell me what would make the main conclusion wrong.

Text:
{clipboard}
```

## Put it on one shortcut

- **Raycast** (Mac and Windows, needs an install): create a snippet with the keyword `;check` and paste the prompt above. With Raycast Pro you can also make it an AI Command and use `{selection}` in place of `{clipboard}`.
- **Text Blaze** (a browser extension for Chrome and Edge, for work laptops where you can't install software): create a snippet with the shortcut `/check` and paste the prompt above. The free plan supports `{clipboard}`.
- **No tool at all:** save this line in your AI's custom instructions (ChatGPT) or a project's instructions (Claude): "For every fact or number, give a source I can open, or write 'no source'."
