---
name: closing-the-loop
description: Verify an action actually succeeded before reporting it done. Use whenever you start or change something - a dev server, build, migration, script, deploy, CI run, or PR merge - and are about to say it works, it's running, it's deployed, or it's fixed.
---

# Closing The Loop

Never report an action as successful based on the fact that you launched it. A completion claim must cite an observed result.

The most common failure this prevents: saying "done", "it works", or "server running at localhost:3000" while the underlying command actually exited non-zero, the page is still broken, or the deploy never landed.

## The rule

After any action that starts or changes something, observe the actual outcome before you report it.

| You did | Before claiming success, observe |
|---------|----------------------------------|
| Ran a command | Its exit status and output. Exit code 1, 137, 143, 255 is a failure. |
| Started a server or made a UI change | It actually serves and renders correctly: drive it, screenshot it, or read the log |
| Triggered a deploy / CI / PR | The run result is green (`gh run list`, the platform build), not just that it was triggered |
| Fixed a bug | The original failure path is reproduced and now passes; read the relevant log or console |

## When you have not observed it yet

Say so plainly. "Launched, not yet verified" is honest and useful. "Done" is a claim about what you saw, not about what you initiated.

Root cause to remember: treating the act of *launching* something as equivalent to it having *succeeded* is the same bug behind almost every false completion claim. Close the loop before you speak.
