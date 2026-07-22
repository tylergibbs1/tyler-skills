# The tell catalog

Grouped by level. The higher up this file, the more durable the tell: word lists age within months, formatting habits age within model generations, and structural habits (uniformity, assertion without stakes, genericness) have not moved at all.

> Read this as a diagnostic, not a banned list to apply mechanically. Every item below also appears in genuine human writing. The signal is **density and clustering**, never one instance.

---

## 1. Structural tells (most durable)

These survive every round of scrubbing because they come from how the model generates, not from what it was trained to prefer.

- **Uniformity.** Uniform sentence length, uniform paragraph length, uniform grammatical construction, uniform section shape. Stylometric work (StyloMetrix/LightGBM, arXiv:2507.00838) finds LLM text measurably "more grammatically uniform." Uniformity itself is the deeper tell.
- **Low burstiness.** Burstiness is the standard deviation of sentence lengths divided by the mean. Humans swing; models regress to a mean. Fix by drill: no three consecutive sentences within 3 words of each other, and every long passage gets at least one sentence under 8 words and one over 25.
- **Low perplexity.** Each next word is the predictable one. You cannot fix this by swapping synonyms; you fix it by having something specific to say that the generic sentence could not have predicted.
- **Genericness.** No named entities, no dates, no numbers, no real situations, no cultural or temporal anchor. LLMs default to the timeless and the universal.
- **Assertion without engagement.** Claims are made, never defended against a real objection. No naysayer, no "so what," no consequence the writer would be accountable for.
- **Symmetry for its own sake.** Forced parallelism, tricolons where the third item is filler, "not only X but also Y," balanced clauses that balance nothing.
- **Low lexical diversity.** Measured as standardized type-token ratio (STTR) or MTLD, LLM text is repeatedly found less diverse than human text (arXiv:2308.09067; ACM CODS-COMAD 2025). Practical version: the same three abstract nouns recur across every paragraph.

## 2. Formatting and layout tells

Largely catalogued by Wikipedia's WikiProject AI Cleanup, "Signs of AI writing" (created August 2025), the most empirically grounded practitioner catalog, built from thousands of real edits and explicitly descriptive rather than prescriptive.

- **Title-case headings.** Chatbots strongly tend to capitalize all main words in headings. Humans writing naturally use sentence case.
- **Bold-term-colon lists.** Vertical list items where each bullet opens with an inline bold header, then a colon, then descriptive text. A ChatGPT signature that barely exists in natural human prose. Dissolve into paragraphs unless the items are genuinely a parallel set.
- **Excessive boldface.** Emphasizing every instance of a chosen phrase, key-takeaways style.
- **Appended "Conclusion" sections.** Told to "write an article," models add a section titled "Conclusion" or similar, and end paragraphs by restating their own core idea. Note the Wikipedia editors' caveat: this is also a sign the writer is a newbie, not proof of AI.
- **Formulaic "Challenges" and "Future Prospects" sections,** typically opening "Despite its [promise/potential], [subject] faces challenges."
- **Markdown artifacts** bleeding into contexts that do not render markdown: stray asterisks, hash-symbol headings, emoji bullets.
- **Heading-level quirk.** A tendency to skip level-2 headings and start sections at level 3.
- **Emoji in headers and list markers.**

## 3. Punctuation tells

- **Em dash density.** The most discussed and the least reliable in isolation. Per arXiv:2603.27006 ("The Last Fingerprint: How Markdown Training Shapes LLM Prose," experiments Feb to Mar 2026), GPT-4.1 emits 10.62 em dashes per 1,000 words unconstrained and 9.10 under suppression, and still retains 3.86 even when the em dash is explicitly named in the instruction. Claude Opus drops from 9.09 to 0.19 under suppression. Meta's Llama models produce zero across roughly 40,000 words. The human baseline in that study, eight published essays totaling 57,232 words, sits near 3 per 1,000. Treat above 5 or 6 per 1,000 as worth review. This project's house rule is zero, which sidesteps the question.
- **Curly vs straight quotes.** ChatGPT and DeepSeek tend to emit curly quotation marks and apostrophes, sometimes inconsistently within a single response; Gemini and Claude often do not. Mixed styles inside one document is the machine artifact. Normalize to one.
- **Function words and POS ratios.** Forensic stylometry (Koppel et al.) classifies authorship on function-word distribution, part-of-speech ratios, and punctuation counts, all invisible to word-banning. Worth knowing exists; not something to hand-edit.

## 4. Lexical tells (least durable, refresh often)

These decline as they become notorious. "Delve" has already dropped. Any fixed list ages, so learn the mechanism: the overuse traces partly to RLHF preference data (Juzek and Ward, arXiv:2412.11385, identified 21 focal words and tied overuse to RLHF), and partly to next-token optimization favoring high-probability phrasing.

**Inflated significance** (the durable core of the category): underscores, highlights, showcases, pivotal, crucial, vital, testament to, stands as, plays a key role in, serves as, marks a turning point.

**Excess academic vocabulary** identified by Kobak et al. across 15.1M PubMed abstracts: delves, showcasing, underscore, pivotal, intricate, meticulously, realm, aligns.

**Excess evaluative adjectives** identified by Liang et al. in ML peer reviews: commendable, innovative, notable, versatile, meticulous, comprehensive.

**Product and marketing register:** seamless, robust, leverage, streamline, empower, unlock, elevate, harness, cutting-edge, game-changing, revolutionize.

**Transitional scaffolding:** Moreover, Furthermore, Additionally, In today's fast-paced world, It's worth noting that, It's important to remember, In conclusion, Overall, In summary.

**Hedge stacks:** may potentially, could arguably, generally tends to, is often considered to be.

**Fix rule:** none of these is fixed by a synonym. Replace an inflated-significance word with the actual consequence, or delete the claim.

## 5. Rhetorical tells

- **Negation-then-correction.** "It's not just X, it's Y." "This isn't about X. It's about Y." Enormously overused.
- **The hollow pivot.** "But here's the thing." "The reality is more nuanced."
- **Bilateral both-sidesing** that names two positions and endorses neither, then closes on "the truth lies somewhere in between."
- **Performed vulnerability.** Manufactured admission ("I'll be honest, I struggled with this at first") with no actual consequence attached.
- **Restating the question** before answering it.
- **Rhetorical questions used as section openers.** "So what does this mean for your team?"

---

## Maintaining this file

The lexical section (4) should be re-checked against current research rather than trusted from memory; words move on and off it. Sections 1 through 3 have been stable. If a future model ships with varied burstiness and no formatting tells by default, sections 1 through 3 shrink and voice and stakes become the entire job.
