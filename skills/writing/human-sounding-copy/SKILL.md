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

For short copy (a button, a headline) run passes 1 and 3 and the house rules, then stop. Commit messages and changelog entries are short but fail differently, see the section below. PR descriptions are prose, so run the full sequence.

### Pass 1: Cut

Verbosity is the loudest tell and the most common complaint. Models pad because padding is high-probability text. Delete:

- **Throat-clearing openers.** "It's worth noting that," "It's important to remember," "In today's landscape," "As we all know." Start at the actual first idea.
- **Restating the prompt or the heading** in the first sentence of a section.
- **Announcement sentences** that say what the next sentence will say. "Let's break this down." "There are three reasons for this." Just give the reasons.
- **Summary closers.** The trailing "In short," "Overall," "By doing X, you can Y" paragraph, and any appended "Conclusion" section. If the piece needs a landing, land on something new, not a recap.
- **Doubled adjectives and synonym pairs.** "clear and concise," "robust and scalable," "fast and efficient." Keep one, or neither.
- **Trailing participial tails.** The comma-plus-ing ending: "ensuring consistency across teams," "allowing users to move faster," "highlighting the need for review." It bolts a second thought onto a finished sentence without saying who is doing it. Cut it, or promote it to its own sentence with a real subject.
- **Hedge stacks, but not the writer's own doubt.** Delete impersonal hedges that leave no one accountable: "may potentially," "could arguably help," "generally tends to," "is often considered to be." Replace the stack with a modal that takes a position rather than a flat assertion: "this should hold under about 10k rows," "that can't be the cause." Human writing carries more epistemic modality than LLM writing, not less; the failure is not that models hedge, it is that they never commit. (Pinker: readers fill in the missing hedges themselves.) First-person markers are the opposite move and stay: "I think," "I suspect," "I'm not sure this holds." A stack hedges a claim into ownerlessness; first person puts a writer behind it. Do not fix a hedge stack by deleting the writer, and do not bolt one on where the piece has no narrator.
- **Borrowed authority.** "Experts argue," "studies show," "industry reports suggest," "observers have noted," "it is widely regarded as." Models invent a plural consensus for a claim that has one source or none. Name the source, attribute it to the one person who actually said it, make the claim in your own voice and be accountable for it, or cut it.
- **Qualifiers that erode trust.** "a bit," "sort of," "very," "quite," "really." Zinsser: every little qualifier whittles away some fraction of the reader's trust.
- **Forced tricolons.** The rule-of-three list where the third item is filler. Two is fine. So is one.
- **"Not only X, but also Y"** and other symmetry scaffolding that exists to sound balanced rather than to say something.
- **Repeated ideas, not just repeated words.** Reduce each paragraph to the claim it actually makes, in four or five words. Any two that reduce to the same claim get merged or cut, even when they share no vocabulary. Rewording a repeated idea is not revision. (Sommers 1980: student writers catch lexical repetition and go blind to conceptual repetition, reaching for the thesaurus, while experienced writers find the shape of the argument first and worry about word choice after.)

Target: cut 20 to 30% of a first draft without losing an idea. If the word count barely moved, the pass was not run. Cut inside sentences, not only whole ones. Current models run 15 to 30% longer per sentence than human writers, so a draft can lose a third of its paragraphs and still read as machine-written because every surviving sentence is 27 words long.

### Pass 2: Format and layout

A whole category of tells lives above the sentence. Catalog and sources in `references/ai-tells.md`.

- Title-case headings become sentence case.
- Dissolve bold-term-colon lists into prose where the items are not genuinely parallel items. This is the single strongest ChatGPT formatting signature and it barely exists in natural human writing.
- Delete blanket boldface used as key-takeaway highlighting.
- Delete appended "Conclusion," "Challenges," and "Future Prospects" sections, especially any that open "Despite its promise, X faces challenges."
- Kill markdown artifacts bleeding into prose: stray asterisks, hash headings in plain-text contexts, emoji bullets, emoji in headers.
- Normalize quotation marks and apostrophes to one style throughout. Mixed curly and straight marks inside one document is a machine artifact.
- Vary paragraph length. Uniform four-sentence blocks are as much a tell as uniform sentences.

### Pass 3: Delete the lexical and grammatical tells

The house rules below are absolute. Beyond those, the banned-word list is a moving target, so learn the mechanism instead of memorizing the list: these words are overrepresented because RLHF preference data rewards them, and each one declines once it becomes notorious ("delve" already has). The list ages in both directions: writers scrub these words, and humans absorb them from the models. Presence is weaker evidence every year. Check `references/ai-tells.md` for the current list and refresh it rather than trusting memory.

Inflated significance is the durable category: "underscores," "pivotal," "seamless," "robust," "leverage," "delve," "showcasing," "intricate," "meticulously," "realm," "aligns," "commendable," "testament to," "stands as," "plays a vital role in." The fix is not a synonym. The fix is stating the actual consequence, or deleting the claim.

**Restore the copula.** The same habit shows up as an avoided "is." Models write "serves as," "stands as," "functions as," "represents," "marks," "emerges as," "remains" where the sentence just means "is." This one is still rising while the notorious words fall, because nobody scrubs for it. Unlike the words above, it is fixed by a swap. Try "is," and keep the substitute only where it carries a meaning "is" does not.

The grammatical layer is the more durable half of this pass, because no synonym swap touches a construction. Instruction-tuned models diverge from human grammar in a consistent direction while base models sit at human rates (Reinhart et al., PNAS 2025). Rates and caveats in `references/ai-tells.md`.

- **Trailing participial clauses.** Covered in pass 1, and worth a second grep here. Models emit the comma-plus-ing tail at several times the human rate. One or two in a long piece is ordinary English. Three in a row is a fingerprint.
- **Nominalizations.** The action buried in a noun. "The implementation of the migration" for "we migrated it," "provides visibility into" for "shows," "conduct an analysis of" for "analyze." Scan for "-tion," "-ment," "-ance," "-ity," and "-ness" nouns doing work a verb should do, then put the action in the verb and the person who did it in the subject.
- **Do not hunt passives.** Models use the agentless passive at roughly half the human rate, so stripping passives moves text further from the human baseline, not toward it. Choose voice by cohesion (pass 4).

### Pass 4: Rebuild with craft

This is the pass that makes text human, and it is the one most humanizer guides skip. Full treatment in `references/craft-principles.md`.

- **Structure.** Decide the order of the parts before writing sentences, and be able to name the organizing principle in one line: chronological, a journey that opens in the middle, a set of discrete portraits, two threads braided, one problem chased through three failed fixes. Models default to a single arc on every subject, opening with a direct claim and moving quickly to a proposal. Structure comes out of the material and is not imposed on it, and the reader should no more notice it than they notice someone's bones (McPhee). Test: if your outline would fit a different topic unchanged, you have the default arc, not a structure.
- **Cohesion.** Start sentences with old or familiar information, end with new and complex information, so each new idea becomes the next sentence's anchor. Put the most important word at the end of the sentence. (Williams)
- **Concreteness.** Every abstract claim gets a named entity, a number, a date, a real situation, or a sensory detail. Show the thing rather than characterizing it: "my hands shook," not "I was nervous." LLMs default to the timeless and generic; specificity is expensive to fake. (Zinsser) **Never invent one.** Every anchor traces to the source material, to the user, or to something you verified this session. If you cannot source it, narrow the claim or cut it, and leave `[need: figure]` where the specific is missing. Do not manufacture personal experience the author did not give you ("when I shipped this last year," "a client of mine"), and do not supply a statistic, date, version number, or quotation you have not seen. A missing specific is a research task. A wrong specific costs more than a missing one, because specificity is what buys the reader's trust in the first place. And do not ration the good material one detail per paragraph. Cluster it: let a stretch run plain, then land the odd number, the proper noun, the thing you would only know from having been there. Human writing is lumpy this way and model writing is not. Plain is not vague; a plain sentence still says something, it just says nothing surprising.
- **Situational anchoring.** Concreteness is what you point at. This is where the writer is standing when they point. Models strip time and place adverbials harder than almost anything else, so put them back: "last Tuesday," "back at the old office," "upstairs," "by then," "three deploys later," "still," "already," "halfway through." A named entity satisfies the concreteness rule without satisfying this one. Not a licence to restore the qualifiers cut in pass 1; "very," "quite," and "really" locate nobody anywhere.
- **Rhythm.** Vary sentence length deliberately. No three consecutive sentences within three words of the same length. Then read it aloud: the ear catches what the eye misses. (Provost, Clark, Klinkenborg)
- **Stakes and "so what."** Say why this matters, to whom, and what changes. Real consequence, not the inflated-significance language you deleted in pass 3.
- **Argument, not assertion.** Plant a naysayer: name the strongest objection in the objector's own terms. Answering it is optional. Conceding that it has force and going on anyway is the move models never make. Answer "so what? who cares?" LLM text asserts into a vacuum. (Graff and Birkenstein)
- **Do not force resolution.** Models tie up loose ends: every tension released, every example followed by a sentence explaining what it demonstrated. Cut the sentences that interpret your own material ("this shows that," "what this means is," "the lesson here is"); if an example needs the gloss, replace the example. Where a question the piece raises is genuinely unsettled, say so and leave it there. Do not manufacture uncertainty you do not have, which is the same failure in the other direction.
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

**Make one change no word swap could make.** Cut a section, reorder so the strongest claim does not land where the outline put it, or delete a claim you cannot actually support. An editing round that changed only words and sentences is rewording, not revision, and it leaves the draft in exactly the shape the first pass gave it.

**Find what the draft discovered.** A forward pass states its thesis in the opening and then restates it in new clothes for the rest of the piece. A human draft usually lands somewhere its opening did not promise, because the writer worked out what they thought while writing it. Find the sentence that says more than the opening promised, make that the point, and rewrite the opening so it sets that claim up instead of announcing it. If the best line in the piece is the first line, there is nothing to arrive at. This is for essays, posts, and anything that argues a position; it is wrong for docs and reference material, where the conclusion belongs first.

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
| Sentence-length variance (burstiness) | std dev / mean well above zero, no three consecutive sentences within 3 words | LLMs regress to a mean sentence length, and since the 2025 generation that mean is long. Advice written before 2025 has this backwards |
| Short sentences | At least 1 in 5 under 15 words | Roughly a third of human sentences run 15 words or fewer; current models produce them at a small fraction of that rate. "One short sentence somewhere" does not close a gap that size |
| Em dash density | 0 per 1,000 words (house rule); human baseline is roughly 3, GPT-4.1 runs near 10 | See `references/evidence.md` |
| Referent consistency | One name per thing, used every time | Models rename a single referent down a thesaurus (the study, the research, the paper, the investigation) inside one section. Variety comes from having more ideas, not more names for one |
| Concrete anchors | Present in quantity, clustered rather than one per paragraph on a quota, and every one sourced | Generic text is the default failure; evenly rationed detail is its own, and invented detail is worse than either |
| Self-interpreting sentences | 0 whose only job is to say what the previous sentence demonstrated | Closure is where model text most reliably diverges from human text |
| Word count vs first draft | Down 20 to 30% after pass 1 | Verbosity is the loudest tell |

**Names are exempt from every variation target.** Product names, UI labels, API objects, parameters, error states, and menu paths get one word each, repeated verbatim wherever they appear. Rename a term mid-document and the ideas stop compiling in the reader's head. Same inside a single screen: if the button says "connect," then the empty state, the error, and the confirmation say "connect," not "link," "add," or "set up." Reference docs extend this to the whole vocabulary, where deliberate repetition is the professional standard and the burstiness target does not apply either.

## Commits and changelogs

Run passes 1 and 3 and the house rules, then this.

The tell here is not vocabulary. It is a message that fluently restates the diff and never says why. "refactor: improve readability and maintainability" is the shape to watch for, because it describes the patch to a reader who is already looking at the patch. Sampling about 1,600 commits across five major open-source projects found 44% had quality problems, the largest group being messages carrying the what and not the why.

- **Subject: imperative mood, under 50 characters.** "fix retry loop dropping the last attempt," not "fixed the retry loop" and not "this commit fixes."
- **Body: the problem, not the change.** What was wrong without this patch, and why this fix beats the one you discarded. The diff already shows the how.
- **Anchor it.** An issue number, the error string, a version, the reproduction. If the body names nothing outside the diff, it was written from the diff.
- **No stakes language.** "a critical improvement to reliability" is pass-3 inflation. The issue number is the stakes.
- **A changelog is not a commit log.** Write each entry from the user's side: what they can now do, or what will now break.

## Where the tells are not tells

Density and clustering carry the signal, never a single feature. Em dashes, summary sections, and the rule of three are all legitimate human techniques. Over-correcting damages good writing, and several "AI tells" are equally signs of inexperienced human writing. When editing someone else's work, fix what actually reads badly rather than what pattern-matches to a list.

**The baseline is moving toward the model.** "Delve," "showcase," "boast," "intricacies," and "meticulous" have risen measurably in unscripted human speech since ChatGPT's release, and em dashes went from roughly 4% of medRxiv discussion sections before ChatGPT to about 20% by 2025. People now say and write these things natively. So when the text is someone else's, check a flagged word against their earlier writing before cutting it. If it is already in their prior work it is their voice, and removing it is the same class of error as capitalizing their lowercase. Flag it for them instead of fixing it.

## Reference files

- **`references/ai-tells.md`**: The full catalog, ordered most-durable-first: structural, syntactic, formatting, punctuation, lexical, rhetorical. Includes the Biber-feature rates behind the grammar bullets in pass 3, and a note on which tells are aging out.
- **`references/exemplars.md`**: Writers, blogs, and books worth studying, grouped by genre, each with what to steal from it and what not to borrow. Read one before drafting.
- **`references/craft-principles.md`**: The constructive half. Williams on cohesion, Pinker on the curse of knowledge, Zinsser on concreteness, Clark and Klinkenborg on rhythm, Graff and Birkenstein on argument, each reduced to something applicable.
- **`references/voice-and-idiolect.md`**: How to extract a voice from a writing sample and match it, and how to build one when there is no sample.
- **`references/evidence.md`**: The research base. Stylometry, the post-ChatGPT vocabulary studies, detector reliability, paraphrase attacks, with citations and confidence notes. Read this before making a factual claim about how AI writing differs from human writing.
