# Voice as idiolect, not register

Picking a register (casual, professional, technical) produces a *plausible* voice. It does not produce a *specific person*, and the gap between those two is most of what makes text read as machine-written.

Forensic linguistics is the useful frame. Individual voice is **idiolectal co-selection**: the combination of many individually unremarkable choices that together form a fingerprint (Coulthard 2004; McMenamin 2002). The canonical case is the Unabomber manifesto, where roughly twelve ordinary linguistic items ("at any rate," "clearly," "presumably," "thereabouts") were enough to tie the text to Ted Kaczynski. No single item was distinctive. The combination was.

---

## With a writing sample

This is the strong case. Extract measurable habits, then match them. Do not paraphrase the sample; take its parameters.

**Measure:**

1. **Sentence length pattern.** Mean, and more importantly the variance and the shape of the swing. Does this writer follow a long sentence with a three-word one, or stay mid-range?
2. **Contraction rate.** Count them. Some writers never use "don't." Matching this one detail moves perceived authorship more than most rewriting.
3. **Paragraph openings.** Do paragraphs open on a subject, a conjunction ("And," "But," "So"), a question, a name?
4. **Paragraph length.** One-sentence paragraphs, or dense blocks.
5. **Punctuation preferences.** Semicolons, parentheses, colons, ellipses, dashes of any kind, exclamation points. Writers are highly consistent here.
6. **Capitalization.** Sentence case, all lowercase, or lowercase with selective caps. This is one of the most visible idiolect markers and one of the most commonly destroyed by editors and models, which normalize it on instinct. Match it exactly and never correct it. (This project's own house voice is all lowercase; see the house rules in `SKILL.md`.)
7. **Recurring word choices and filler.** The small stuff: "basically," "honestly," "sort of," "roughly," "at any rate." These are the idiolect markers.
8. **Metaphor domains.** What does this person reach for, sports, cooking, machinery, war, gardening. People return to the same wells.
9. **Register floor.** Profanity, slang, technical shorthand, and where they refuse to go.
10. **Stance markers.** How they signal opinion: "I think," "obviously," "to be fair," or by flat assertion.
11. **What they notice.** The kind of detail they include and the kind they skip.

**Then match, with two hard rules: do not upgrade, and do not de-duplicate.** If the sample says "stuff," write "stuff." If it says "a bunch of," do not write "numerous." If it says "thing" four times on a page, write "thing" four times. The instinct to improve someone's vocabulary is exactly what destroys the match, and reaching for a synonym on second mention is a reflex an editing model runs automatically.

**Edit, do not rewrite.** Handing a whole passage to a model and asking for it back in someone's voice is the operation that destroys the voice. Across 2,700 rewrites of personal narratives, three frontier models moved every stylometric marker the same direction: contractions down about a third, first-person pronouns and function words down, lexical diversity and word length up, punctuation up sharply. Afterward a matcher could tie a rewrite back to its author only a few percent of the time. Adding "preserve the author's voice" to the prompt cut the drift by about a third without changing its direction. Content survives rewriting. Authorship does not. See `evidence.md`.

So change the one sentence you actually object to and leave every other sentence byte-identical. Then diff. If the diff touched a contraction, a pronoun, a "just" or "really" or "kind of," or punctuation in a sentence you were not fixing, revert that hunk.

**Do not copy content or claims from the sample.** Take the parameters, not the material.

---

## Without a sample

Build a specific person, not a tone.

- **Give them opinions.** What does this writer actually think about the subject, including the part that could be wrong.
- **Give them a refusal.** What would this writer not say, what claim would they push back on. A voice is partly defined by its boundaries.
- **Give them expertise with a shape.** Not "knowledgeable," but specifically what they have done and therefore what examples they reach for.
- **Give them an audience they know.** Writing to someone specific changes syntax more than any style instruction.
- **Give them stakes.** What is at risk for them in being wrong here.

Then write from that, and check whether any sentence could have been written by a different persona. If most could, there is no voice yet.

---

## Voice in constrained surfaces

UI copy, commit messages, error strings, and button labels have very little room for idiolect. Do not force personality into them. There, "human" means specific and plain, not characterful: name the actual thing that happened, use the words the user already uses, skip the apology and the exclamation point.

Voice work belongs to prose: essays, docs, announcements, PR descriptions, anything with paragraphs.

---

## The check

Read the finished piece and ask whether a reader who knows this writer would recognize it. If the answer is "it sounds professional," the voice pass has not been done.
