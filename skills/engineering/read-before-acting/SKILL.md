---
name: read-before-acting
description: Read the real code, render, or data before answering or editing. Use before you explain how the system behaves, edit a file, restyle UI, or make claims about data, config, or metrics - especially when tempted to answer from memory or from the prompt alone.
---

# Read Before Acting

Read the actual thing before you act on it or make claims about it. "Look at the code" / "look at the actual component" / "look at the db" is the single most repeated instruction agents get. Pre-empt it.

## Before answering how the system behaves

Read the real implementation: source, schema, config. Do not infer behavior from the prompt text, the file name, or memory. If the user asks whether something works or exists, open it and check rather than reasoning about it.

## Before editing code

Read the surrounding code and the existing patterns first, then match them. Check what already exists so you do not build a duplicate or conflicting version. If the repo has architecture docs (ARCHITECTURE.md, CONTEXT.md, DESIGN.md), read the relevant part before large changes.

## Before UI or design work

Look at the reference: the original component you are mirroring, the existing design system, or the actual rendered output (drive it in a browser or screenshot it). Do not restyle from a mental model of what the UI probably looks like.

## Before claims about data, config, or metrics

Query the real source. Read the DB directly (for example via a Supabase MCP), read live env vars and build status from the platform CLI (for example Vercel), and read the actual logs for errors. Do not state numbers or config values you have not looked up.
