---
name: human-sounding-copy
description: Makes writing read as a specific human wrote it, not a model. Cuts AI verbosity, strips lexical and formatting tells, and rebuilds with the craft techniques (cohesion, rhythm, concreteness, stakes, idiolect) that AI text most reliably lacks. Use when writing or editing any prose, UI copy, headings, docs, essays, commit or PR text, or video text, and whenever asked to "make this sound human," "humanize this," "de-AI this," "this reads like ChatGPT," or "less AI-sounding."
---

# Human-Sounding Copy

Make the text read as though a specific person with specific knowledge wrote it.

**The goal is quality and authenticity for human readers, not evading detectors.** Detector evasion is a losing target: it is an arms race, it is ethically fraught where authorship must be disclosed, and the detectors themselves are unreliable (Liang et al. 2023 found 7 detectors falsely flagged 61.3% of TOEFL essays by non-native writers as AI). Scrubbing words moves the signal without removing it. Adding what only a real writer can supply, specific knowledge, real stakes, a particular voice, is the only durable strategy. See `references/evidence.md`.

## Run the passes in order

Removal first (passes 1 to 3) is fast and mechanical. The rebuild (passes 4 to 6) is where the writing actually becomes human. Do not stop after pass 3: over-scrubbed prose is its own recognizable register.

When drafting from scratch rather than editing, run pass 5 first. Reading a real writer before you start is worth more than fixing a generic draft afterward.

For short copy (a button, a headline, a commit message) run passes 1 and 3 and the house rules, then stop.

### Pass 1: Cut

Verbosity is the loudest tell and the most common complaint. Models pad because padding is high-probability text. Delete:

- **Throat-clearing openers.** "It's worth noting that," "It's important to remember," "In today's landscape," "As we all know." Start at the actual first idea.
- **Restating the prompt or the heading** in the first sentence of a section.
- **Announcement sentences** that say what the next sentence will say. "Let's break this down." "There are three reasons for this." Just give the reasons.
- **Summary closers.** The trailing "In short," "Overall," "By doing X, you can Y" paragraph, and any appended "Conclusion" section. If the piece needs a landing, land on something new, not a recap.
- **Doubled adjectives and synonym pairs.** "clear and concise," "robust and scalable," "fast and efficient." Keep one, or neither.
- **Hedge stacks.** "may potentially," "could arguably help," "generally tends to." One hedge maximum, and only when the uncertainty is real. (Pinker: readers fill in the missing hedges themselves.)
- **Qualifiers that erode trust.** "a bit," "sort of," "very," "quite," "really." Zinsser: every little qualifier whittles away some fraction of the reader's trust.
- **Forced tricolons.** The rule-of-three list where the third item is filler. Two is fine. So is one.
- **"Not only X, but also Y"** and other symmetry scaffolding that exists to sound balanced rather than to say something.

Target: cut 20 to 30% of a first draft without losing an idea. If the word count barely moved, the pass was not run.

### Pass 2: Format and layout

A whole category of tells lives above the sentence. Catalog and sources in `references/ai-tells.md`.

- Title-case headings become sentence case.
- Dissolve bold-term-colon lists into prose where the items are not genuinely parallel items. This is the single strongest ChatGPT formatting signature and it barely exists in natural human writing.
- Delete blanket boldface used as key-takeaway highlighting.
- Delete appended "Conclusion," "Challenges," and "Future Prospects" sections, especially any that open "Despite its promise, X faces challenges."
- Kill markdown artifacts bleeding into prose: stray asterisks, hash headings in plain-text contexts, emoji bullets, emoji in headers.
- Normalize quotation marks and apostrophes to one style throughout. Mixed curly and straight marks inside one document is a machine artifact.
- Vary paragraph length. Uniform four-sentence blocks are as much a tell as uniform sentences.

### Pass 3: Delete the lexical tells

The house rules below are absolute. Beyond those, the banned-word list is a moving target, so learn the mechanism instead of memorizing the list: these words are overrepresented because RLHF preference data rewards them, and each one declines once it becomes notorious ("delve" already has). Check `references/ai-tells.md` for the current list and refresh it rather than trusting memory.

Inflated significance is the durable category: "underscores," "pivotal," "seamless," "robust," "leverage," "delve," "showcasing," "intricate," "meticulously," "realm," "aligns," "commendable," "testament to," "stands as," "plays a vital role in." The fix is not a synonym. The fix is stating the actual consequence, or deleting the claim.

### Pass 4: Rebuild with craft

This is the pass that makes text human, and it is the one most humanizer guides skip. Full treatment in `references/craft-principles.md`.

- **Cohesion.** Start sentences with old or familiar information, end with new and complex information, so each new idea becomes the next sentence's anchor. Put the most important word at the end of the sentence. (Williams)
- **Concreteness.** Every abstract claim gets a named entity, a number, a date, a real situation, or a sensory detail. Show the thing rather than characterizing it: "my hands shook," not "I was nervous." LLMs default to the timeless and generic; specificity is expensive to fake. (Zinsser)
- **Rhythm.** Vary sentence length deliberately. No three consecutive sentences within three words of the same length. Include at least one sentence under 8 words and one over 25 in any long passage. Then read it aloud: the ear catches what the eye misses. (Provost, Clark, Klinkenborg)
- **Stakes and "so what."** Say why this matters, to whom, and what changes. Real consequence, not the inflated-significance language you deleted in pass 3.
- **Argument, not assertion.** Plant a naysayer: name the strongest objection and answer it. Answer "so what? who cares?" LLM text asserts into a vacuum. (Graff and Birkenstein)
- **Model the reader.** Counter the curse of knowledge: name what the reader does not yet know, and do not explain what they already do. Trust them enough to leave things out. (Pinker, Klinkenborg)

### Pass 5: Ground in an exemplar

Before drafting anything longer than a paragraph, put a real human's prose in mind. This is the writing equivalent of studying a reference repo, and it does more than any checklist: a model with a specific writer's moves in view produces something specific, while a model with only rules in view produces the averaged register.

Pick the entry from `references/exemplars.md` closest to the genre, read an actual piece of it (fetch it if you can), and name two or three concrete moves to borrow: how they open, how long their sentences run, what they do instead of a conclusion. Then draft, and compare the draft against that piece rather than against a rule list.

One exemplar, not five. Blending voices averages back into the generic.

### Pass 6: Voice

Register is not voice. "Professional" or "casual" produces a plausible register; a human produces a specific person. Method in `references/voice-and-idiolect.md`.

- **With a writing sample:** extract and match the author's actual habits. Sentence-length pattern, contraction rate, how paragraphs open, punctuation preferences, recurring words and metaphor domains. Do not upgrade their vocabulary. If they write "stuff," write "stuff."
- **Without a sample:** build a persona with opinions and a stance, not just a tone. What does this writer think, what would they refuse to say, what do they notice that others do not.

### Pass 7: Self-critique

Mechanically applying any checklist, including this one, creates its own uniformity. Over-scrubbed prose (mandatory contractions, mandatory short sentences, sprinkled fake imperfections) is a recognizable de-AI'd register. Never add typos or noise; that is the mark of bad humanizer tools.

Final read, one question: does this sound like a specific person with something to lose, or like a template that passed a checklist? If nothing in the piece could be wrong, nobody wrote it.

## House rules (absolute)

These are project standards, applied regardless of what the research says about any one of them in isolation.

- **No capital letters.** Write in all lowercase, including the first word of a sentence, proper nouns, headings, and "i". This is the house voice and it is the strongest single marker of it. Exceptions, and only these: code, identifiers, file paths, API and product names inside code or commands, and direct quotations from someone else. Applies to prose, UI copy, headings, commit and PR text. Never "fix" existing lowercase text to sentence case.
- **No em dashes (—)** anywhere: prose, UI copy, commit and PR text, comments. Use periods, commas, or colons, and rephrase so it reads naturally rather than just swapping the punctuation.
- **No hyphens or colons as sentence separators.** Rewrite into real sentences.
- **No emojis in video content.** They look cheap.
- **No all-caps labels or eyebrows** above headings.
- **No jargon or obscure words** most people do not know. If a reader would have to look it up, replace it.
- **Minimal icons.** Only when they carry meaning.

Before finishing, grep the output for `—` and scan against the pass-2 and pass-3 lists.

## Checkable targets

Use these when a piece is long enough to measure, and treat them as directional rather than settled.

| Signal | Target | Why |
|---|---|---|
| Sentence-length variance (burstiness) | std dev / mean well above zero, no three consecutive sentences within 3 words | LLMs regress to a mean sentence length |
| Em dash density | 0 per 1,000 words (house rule); human baseline is roughly 3, GPT-4.1 runs near 10 | See `references/evidence.md` |
| Lexical diversity | Vary vocabulary, do not reuse the same abstract nouns across paragraphs | LLM text measures as less lexically diverse |
| Concrete anchors | At least one named entity, number, or specific detail per paragraph of claim | Generic text is the default failure |
| Word count vs first draft | Down 20 to 30% after pass 1 | Verbosity is the loudest tell |

## Where the tells are not tells

Density and clustering carry the signal, never a single feature. Em dashes, summary sections, and the rule of three are all legitimate human techniques. Over-correcting damages good writing, and several "AI tells" are equally signs of inexperienced human writing. When editing someone else's work, fix what actually reads badly rather than what pattern-matches to a list.

## Reference files

- **`references/ai-tells.md`**: The full catalog. Lexical, punctuation, formatting, and structural tells, with the mechanism behind each and a note on which ones are aging out.
- **`references/exemplars.md`**: Writers, blogs, and books worth studying, grouped by genre, each with what to steal from it and what not to borrow. Read one before drafting.
- **`references/craft-principles.md`**: The constructive half. Williams on cohesion, Pinker on the curse of knowledge, Zinsser on concreteness, Clark and Klinkenborg on rhythm, Graff and Birkenstein on argument, each reduced to something applicable.
- **`references/voice-and-idiolect.md`**: How to extract a voice from a writing sample and match it, and how to build one when there is no sample.
- **`references/evidence.md`**: The research base. Stylometry, the post-ChatGPT vocabulary studies, detector reliability, paraphrase attacks, with citations and confidence notes. Read this before making a factual claim about how AI writing differs from human writing.
