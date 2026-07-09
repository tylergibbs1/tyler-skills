---
name: grounding-with-context7
description: Ground any work with a library, framework, or SDK in current docs via Context7 MCP instead of training data. Use when writing or changing code that touches a package, when verifying existing usage is correct, when auditing whether a tool is being fully leveraged, and when the user says "use context7", "ground with context7", "confirm with context7", or "are we fully leveraging X".
---

# Grounding With Context7

Whenever the work touches a library, framework, SDK, or API, ground it in current documentation with Context7 MCP. Do not rely on training data, and do not wait to be told. This is a standing habit: "use context7 to help u" is one of this user's most repeated instructions.

## The four modes

Context7 is not just for looking things up before writing new code. Use it in all of these:

1. **Look up before implementing.** Before writing code against a package, fetch its current docs and follow them. "use context7 to look up the ai sdk docs", "use context7mcp to look up resend docs".
2. **Verify and ground existing code.** After a change, confirm the usage is correct and idiomatic against the docs. "confirm fix with context7", "use context7 to make sure we are doing this right", "use context7 to verify your comments".
3. **Audit for full leverage.** Proactively check whether the project is using a tool to its potential, and surface features it is missing. "are we fully leveraging vitest? use context7", "look up the newest things typescript offers that we can leverage".
4. **Ground subagents.** When you fan work out to subagents (implementation, PR review, architecture checks), tell each one to call Context7 to verify accuracy. "have subagents review with context7", "the agents can call context7 mcp to verify accuracy".

## How to call it

1. `resolve-library-id` with the library name and the user's question.
2. Pick the best match, preferring exact names and version-specific IDs when a version is mentioned.
3. `query-docs` with the selected library ID and the question.
4. Answer or implement from the fetched docs, citing the version. Include real code examples from the docs.

Prefer Context7 over web search for library docs, and use it even for libraries you think you know, since your training data may be stale. For the CLI tools this user favors, `ast-grep` docs live at `/ast-grep/ast-grep.github.io`.

## When to reach for it without being asked

Setup and config questions, version migrations (for example "update to typescript 6", "upgrade wasm"), any API syntax, cost or model-choice questions about an SDK, and any moment you are about to write a package call from memory. If a dependency is being updated, look up its changelog with Context7 first to check for breaking changes.
