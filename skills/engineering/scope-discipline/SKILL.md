---
name: scope-discipline
description: Build exactly what was asked and nothing more. Use when implementing a feature or fix and you feel the pull to also add error handling, config options, abstractions, migrations, caps, or a PR the user did not request.
---

# Scope Discipline

Do exactly what was asked and no more. Unrequested scope is one of the most frequent corrections agents get ("no need for all that we just need to send the emails now", "no migration is needed we dont have users yet", "rm the max tool calls we dont want a max").

## Rules

- **Build only the thing requested.** No extra features, filters, config toggles, abstractions, token or tool-call caps, speculative error-handling layers, or public APIs that were not asked for.
- **Assume greenfield.** Most projects here have no production users yet, so do not add backward-compatibility shims, data migrations, or versioning unless explicitly told they are needed.
- **Prefer the minimal path.** When the ask is "get X working", get X working. Do not also harden, generalize, or productionize it in the same breath.
- **No unrequested ceremony.** Do not open a PR, add PR attribution, or set up preview environments unless asked.
- **Surface extras, do not build them.** If you think an add-on is genuinely worth doing, name it in one line and let the user decide. Do not build it first and explain afterward.

When in doubt about scope, do the smaller thing and ask.
