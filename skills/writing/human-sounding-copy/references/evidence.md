# The research base

Read this before making a factual claim about how AI writing differs from human writing. Everything here is directional rather than settled, and the confidence notes at the bottom matter.

---

## How the differences are actually measured

**Perplexity and burstiness.** The two signals commercial detectors are built on. Perplexity measures how predictable each next word is; burstiness measures how much sentence length and complexity vary across a document, commonly computed as the standard deviation of sentence lengths divided by the mean. Human writing scores higher on both. LLMs sit low on perplexity because they are optimized toward high-probability tokens, and low on burstiness because they regress toward a mean sentence length. GPTZero publishes no official burstiness threshold and has said there is no set threshold; the specific cutoff numbers circulating online come from detector-adjacent commercial sites and are not corroborated.

**Lexical diversity.** Standardized type-token ratio (STTR) and MTLD (Measure of Textual Lexical Diversity). A human-vs-LLM news text study (arXiv:2308.09067) found humans use a richer vocabulary; an ACM CODS-COMAD 2025 paper found LLM text "longer, more structured, and less lexically diverse."

**Stylometric feature sets.** Forensic authorship attribution (Koppel et al.; StyloMetrix/LightGBM work at arXiv:2507.00838) classifies on function-word distributions, part-of-speech ratios, and punctuation counts. That work found LLM text more grammatically uniform. None of these features are touched by banning words.

---

## The post-ChatGPT vocabulary spike

**Kobak et al.**, "Delving into LLM-assisted writing in biomedical publications through excess vocabulary" (Science Advances 2025; arXiv:2406.07016). Analyzed 15.1M PubMed abstracts from 2010 to 2024 using an "excess vocabulary" method modeled on COVID excess-mortality studies. Conclusion: "at least 13.5% of 2024 abstracts were processed with LLMs," reaching 40% for some subcorpora. Excess style words: *delves, showcasing, underscore, pivotal, intricate, meticulously, realm, aligns*.

**Liang et al.** (Stanford, arXiv:2403.07183, ICML 2024). Studied peer reviews at ICLR 2024, NeurIPS 2023, CoRL 2023, EMNLP 2023. Found "between 6.5% and 16.9% of text submitted as peer reviews to these conferences could have been substantially modified by LLMs," with *commendable, innovative, notable, versatile* spiking.

**Juzek and Ward** (FSU, arXiv:2412.11385). Identified 21 focal words and traced the overuse partly to RLHF (reinforcement learning from human feedback), which is the mechanism worth remembering.

**The decline effect.** Several of these words are now falling as writers scrub them; "delve" dropped once it became a known tell. This is why a static banned-word list ages badly and why the mechanism matters more than the list.

---

## Punctuation

**arXiv:2603.27006**, "The Last Fingerprint: How Markdown Training Shapes LLM Prose" (experiments conducted February to March 2026). GPT-4.1 produces 10.62 em dashes per 1,000 words unconstrained and 9.10 under suppression, and retains 3.86 even when the em dash is named explicitly in the instruction. Claude Opus drops from 9.09 to 0.19 under suppression. Meta's Llama models produce zero in either condition across approximately 40,000 words. Human baseline measured across eight published essays totaling 57,232 words.

Caveat: single preprint, one set of experiments. Treat as indicative. Note also that the em dash is defended as legitimately human by the Washington Post, Rolling Stone, and The Ringer; the real signal is overuse and misplacement, not presence.

---

## Formatting

**Wikipedia WikiProject AI Cleanup, "Signs of AI writing"** (created August 2025). The most empirically grounded practitioner catalog, built from thousands of real edits, self-described as descriptive rather than prescriptive. Source for the title-case headings, bold-term-colon lists, appended "Conclusion" sections, "Challenges"/"Future Prospects" formula, markdown artifacts, and heading-level quirks in `ai-tells.md`. The editors themselves warn that some of these conflate newbie writing with AI writing.

---

## Why detector evasion is the wrong target

This is the strategically important part.

**Detectors are unreliable and biased.** Liang et al. (2023, *Patterns* 4(7), art. 100779) tested 7 detectors on 91 TOEFL essays and 88 US student essays. The detectors incorrectly labeled more than half the TOEFL essays as AI-generated (average false-positive rate 61.3%), and at least one detector flagged 97.8% of them, versus near-zero for native-speaker essays. Non-native writing shares low-perplexity features with AI text. Any workflow that optimizes for detector scores is optimizing against a broken instrument that already harms real writers.

**Paraphrase attacks defeat detectors outright.** Krishna et al. (arXiv:2303.13408, NeurIPS 2023) built DIPPER, an 11B paraphrase model, and report it "drops the detection accuracy of DetectGPT from 70.3% to 4.6% (at a constant false positive rate of 1%), without appreciably modifying the input semantics." Sadasivan et al. make the broader theoretical case that reliable detection is not achievable as models approach human text distributions.

**Word-swapping does not change what detectors measure.** Synonym substitution changes vocabulary while leaving the perplexity and burstiness pattern intact. A thesaurus with extra steps.

**The scrubbed style is becoming its own tell.** Once a marker becomes notorious its usage collapses, and mechanically de-AI'd prose (mandatory contractions, mandatory short sentences, sprinkled imperfections) forms a recognizable register of its own.

**Therefore:** the objective is quality and authenticity for human readers. Specificity, stakes, cohesion, and voice are the only durable strategy, and they happen to be what actually makes writing good.

**Ethics.** Detector evasion is ethically fraught in academic and disclosure-required contexts. There is a real difference between editing AI-assisted text to be better writing and misrepresenting authorship. This skill is for the first.

---

## Voice and emotion

**Coulthard (2004); McMenamin (2002).** Forensic linguistics on idiolect and co-selection. The Unabomber attribution rested on roughly twelve unremarkable linguistic items appearing together.

**Al Hosni,** literature review on authorial voice in the AI era (*Arab World English Journal*, September 2025). Found AI text "grammatically polished and structurally coherent" but lacking "emotional nuance, subtlety, rhetorical richness, and distinct linguistic markers."

**Craft canon:** Joseph Williams (*Style*), Steven Pinker (*The Sense of Style*), William Zinsser (*On Writing Well*), Roy Peter Clark (*Writing Tools*), Verlyn Klinkenborg (*Several Short Sentences About Writing*), Gary Provost, Graff and Birkenstein (*They Say / I Say*). Canonical and well attested. Reduced to applicable form in `craft-principles.md`.

---

## Confidence notes

- **High confidence:** the stylometry and detection findings (Kobak; Liang 2023 and 2024; Sadasivan; Krishna) are peer-reviewed or widely cited preprints. The craft principles are canonical.
- **Indicative only:** the em dash figures come from a single 2026 preprint. Burstiness threshold numbers from commercial sites are uncorroborated by GPTZero.
- **Descriptive, not authoritative:** the Wikipedia catalog is a practitioner essay that warns about its own false positives.
- **Moving target:** the entire lexical layer. Re-check rather than trusting memory.

**What would change the guidance:** if a future model ships with varied burstiness and no formatting tells by default, the removal passes shrink toward nothing and voice and stakes become the whole job. If retrieval or logging-based provenance (as Krishna et al. propose) becomes standard, the evasion-is-futile framing gets stronger still.
