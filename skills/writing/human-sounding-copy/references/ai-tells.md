# The tell catalog

Grouped by level. The higher up this file, the more durable the tell: word lists age within months, formatting habits age within model generations, and structural habits (uniformity, assertion without stakes, genericness) have not moved at all.

> Read this as a diagnostic, not a banned list to apply mechanically. Every item below also appears in genuine human writing. The signal is **density and clustering**, never one instance.

---

## 1. Structural tells (most durable)

These survive every round of scrubbing because they come from how the model generates, not from what it was trained to prefer.

- **Uniformity.** Uniform sentence length, uniform paragraph length, uniform grammatical construction, uniform section shape. Stylometric work (StyloMetrix/LightGBM, arXiv:2507.00838) finds LLM text measurably "more grammatically uniform." Uniformity itself is the deeper tell.
- **Low burstiness.** Burstiness is the standard deviation of sentence lengths divided by the mean. Humans swing; models regress to a mean, and since the 2025 generation that mean runs long. Fix by drill: no three consecutive sentences within 3 words of each other, and at least one sentence in five under 15 words.
- **Low perplexity, and flat surprisal.** Each next word is the predictable one. The subtler half is the distribution: human text is heavy-tailed, flat ordinary stretches punctuated by genuinely unguessable words, while model text sits mid-range everywhere. So clustering the surprising material beats spreading it evenly. You cannot fix either by swapping synonyms.
- **Genericness.** No named entities, no dates, no numbers, no real situations, no cultural or temporal anchor. LLMs default to the timeless and the universal. Time and place adverbials ("last Tuesday," "by then," "upstairs") go missing hardest of all.
- **Assertion without argument.** Claims are made, never defended against a real objection. No naysayer, no "so what," no consequence the writer would be accountable for.
- **Compulsive closure.** Every tension released, every example followed by a sentence explaining what it demonstrated, nothing left open. Of eight narratological dimensions compared between human and LLM stories, closure was the one that diverged.
- **Symmetry for its own sake.** Forced parallelism, tricolons where the third item is filler, "not only X but also Y," balanced clauses that balance nothing.
- **Lexical diversity cuts both ways, and the direction has flipped.** Older measurements (STTR/MTLD; arXiv:2308.09067, ACM CODS-COMAD 2025) found LLM text less diverse than human text across a whole document: the same three abstract nouns carrying every paragraph. Newer models run the other way, and against a single target author they always did. What the extra diversity buys is elegant variation, the fault Fowler named in 1906: one referent renamed down a thesaurus across a passage, the study becoming the research becoming the paper becoming the investigation. Both readings point at one fix. Keep the same name for the same thing, and get variety by having more than three ideas. See `evidence.md`.

## 2. Syntactic tells (durable, invisible to word lists)

Measured on Biber's feature set against matched human corpora (Reinhart et al., PNAS 2025, arXiv:2410.16107). Rates are GPT-4o against the matched human rate. Base Llama 3 models sit near human rates on all of these, so this layer is what instruction tuning added rather than a property of fluent English. The authors: "instruction tuning appears to make the model output less human, not more."

| Feature | GPT-4o vs human | Base models |
|---|---|---|
| Present participial clauses | roughly 5x | at human rate |
| That-clauses as subject | roughly 2.5x | at human rate |
| Nominalizations | roughly 2x | at human rate |
| Phrasal coordination | roughly 2x | at human rate |
| Agentless passive | roughly 0.5x | at human rate |

The last row inverts the folk rule. Models underuse the passive, so "convert to active voice" is not a de-AI edit; that one has already been done to the text. Phrasal coordination is pass 1's doubled adjectives one layer down in the grammar, so fix it there. Ranking within the set shifts with the metric, and published summaries disagree on exact effect sizes, so treat direction and rough magnitude as the finding, not the order or the decimals.

## 3. Formatting and layout tells

Largely catalogued by Wikipedia's WikiProject AI Cleanup, "Signs of AI writing" (created August 2025), the most empirically grounded practitioner catalog, built from thousands of real edits and explicitly descriptive rather than prescriptive.

- **Title-case headings.** Chatbots strongly tend to capitalize all main words in headings. Humans writing naturally use sentence case.
- **Bold-term-colon lists.** Vertical list items where each bullet opens with an inline bold header, then a colon, then descriptive text. A ChatGPT signature that barely exists in natural human prose. Dissolve into paragraphs unless the items are genuinely a parallel set.
- **Excessive boldface.** Emphasizing every instance of a chosen phrase, key-takeaways style.
- **Appended "Conclusion" sections.** Told to "write an article," models add a section titled "Conclusion" or similar, and end paragraphs by restating their own core idea. Note the Wikipedia editors' caveat: this is also a sign the writer is a newbie, not proof of AI.
- **Formulaic "Challenges" and "Future Prospects" sections,** typically opening "Despite its [promise/potential], [subject] faces challenges."
- **Markdown artifacts** bleeding into contexts that do not render markdown: stray asterisks, hash-symbol headings, emoji bullets.
- **Heading-level quirk.** A tendency to skip level-2 headings and start sections at level 3.
- **Emoji in headers and list markers.**

## 4. Punctuation tells

- **Em dash density.** The most discussed and the least reliable in isolation. GPT-4.1 runs near 10 per 1,000 words, the human baseline near 3, and Llama models emit zero. Full figures and caveats in `evidence.md`. This project's house rule is zero, which sidesteps the question.
- **Curly vs straight quotes.** ChatGPT and DeepSeek tend to emit curly quotation marks and apostrophes, sometimes inconsistently within a single response; Gemini and Claude often do not. Mixed styles inside one document is the machine artifact. Normalize to one.
- **Function words and POS ratios.** Forensic stylometry (Koppel et al.) classifies authorship on function-word distribution, part-of-speech ratios, and punctuation counts, all invisible to word-banning. Worth knowing exists. Most of it is not hand-editable, but the specific constructions in section 2 are.

## 5. Lexical tells (least durable, refresh often)

These decline as they become notorious. "Delve" has already dropped. Any fixed list ages, so learn the mechanism: the overuse traces partly to RLHF preference data (Juzek and Ward, arXiv:2412.11385, identified 21 focal words and tied overuse to RLHF), and partly to next-token optimization favoring high-probability phrasing.

**Copula avoidance** (rising, and currently the most useful item in this section). Models replace "X is Y" with "X serves as Y," and likewise "stands as," "functions as," "represents," "marks," "emerges as," "remains." Wikipedia's AI Cleanup catalog covers it under avoidance of basic copulatives, citing a drop of over 10% in "is" and "are" in 2023 academic writing; Geng and Trotta (arXiv:2502.09606) find that decline still continuing in arXiv abstracts while "delve" and "intricate" fall away. Worked example from that catalog: "Gallery 825 is LAAA's exhibition arm" became "Gallery 825 serves as LAAA's exhibition space." This is the one entry here where the fix is a straight swap. Write "is."

**Inflated significance** (the durable core of the category): underscores, highlights, showcases, pivotal, crucial, vital, testament to, stands as, plays a key role in, serves as, marks a turning point.

**Excess academic vocabulary** identified by Kobak et al. across 15.1M PubMed abstracts: delves, showcasing, underscore, pivotal, intricate, meticulously, realm, aligns.

**Excess evaluative adjectives** identified by Liang et al. in ML peer reviews: commendable, innovative, notable, versatile, meticulous, comprehensive.

**Product and marketing register:** seamless, robust, leverage, streamline, empower, unlock, elevate, harness, cutting-edge, game-changing, revolutionize.

**Transitional scaffolding:** Moreover, Furthermore, Additionally, In today's fast-paced world, It's worth noting that, It's important to remember, In conclusion, Overall, In summary.

**Hedge stacks:** may potentially, could arguably, generally tends to, is often considered to be.

**Fix rule:** none of these is fixed by a synonym. Replace an inflated-significance word with the actual consequence, or delete the claim.

## 6. Rhetorical tells

- **Negation-then-correction.** "It's not just X, it's Y." "This isn't about X. It's about Y." Enormously overused.
- **The hollow pivot.** "But here's the thing." "The reality is more nuanced."
- **Bilateral both-sidesing** that names two positions and endorses neither, then closes on "the truth lies somewhere in between."
- **Performed vulnerability.** Manufactured admission ("I'll be honest, I struggled with this at first") with no actual consequence attached.
- **Restating the question** before answering it.
- **Unanswered rhetorical questions as section openers.** "So what does this mean for your team?" The tell is the question the text never returns to, not the question itself.
- **Borrowed authority.** A claim attributed to an unnamed plural: "experts," "observers," "industry reports," "many have argued." Wikipedia's AI Cleanup catalog covers this under vague attributions and overgeneralization of opinions, recording models exaggerating the number of sources and presenting one or two views as widely held. This is confidence inflation rather than hedging, which is why an anti-hedging pass leaves it untouched.

---

## Maintaining this file

The lexical section (5) should be re-checked against current research rather than trusted from memory; words move on and off it. Sections 1 through 4 have been stable. If a future model ships with varied burstiness and no formatting tells by default, those sections shrink and voice, structure, and stakes become the entire job.
