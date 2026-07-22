# The research base

Read this before making a factual claim about how AI writing differs from human writing. Everything here is directional rather than settled, and the confidence notes at the bottom matter.

## Contents
- How the differences are actually measured (perplexity, surprisal variance, lexical diversity, sentence length, grammar, editing drift)
- The post-ChatGPT vocabulary spike, the decline effect, and convergence
- Punctuation
- Formatting
- Fabricated specifics
- Why detector evasion is the wrong target
- Voice, stance, structure, and revision
- Confidence notes and what would change the guidance

---

## How the differences are actually measured

**Perplexity and burstiness.** The two signals commercial detectors are built on. Perplexity measures how predictable each next word is; burstiness measures how much sentence length and complexity vary across a document, commonly computed as the standard deviation of sentence lengths divided by the mean. Human writing scores higher on both. LLMs sit low on perplexity because they are optimized toward high-probability tokens, and low on burstiness because they regress toward a mean sentence length. GPTZero publishes no official burstiness threshold and has said there is no set threshold; the specific cutoff numbers circulating online come from detector-adjacent commercial sites and are not corroborated.

**Surprisal variance, not just its mean.** Basani and Chen, "Diversity Boosts AI-Generated Text Detection" (DivEye, arXiv:2509.18880), scored matched human and GPT-4-Turbo essays with a fixed evaluator model: human texts show "higher dispersion and heavier tails," while model outputs are "more concentrated and predictable." Their features are the mean, variance, skewness, and kurtosis of the token-level surprisal sequence. Venkatraman, Uchendu and Lee (GPT-who, NAACL Findings 2024, arXiv:2310.06202) reach the same conclusion from uniform-information-density features: "humans distribute information more unevenly and diversely than models." The writing consequence is that unpredictability is a distribution, not an average, so clustering the surprising material beats spreading it. Caveat: both use GPT-2 as the surprisal evaluator, which the GPT-who authors flag as a limit on the psycholinguistic reading.

**Lexical diversity, and why the direction depends on the comparison.** Standardized type-token ratio (STTR) and MTLD. Against pooled human corpora, LLM text measures less diverse (arXiv:2308.09067; an ACM CODS-COMAD 2025 paper found it "longer, more structured, and less lexically diverse"). Against a single target author the direction reverses: impersonation attempts measure as systematically more lexically diverse and less redundant than the author being imitated, which is itself how verifiers catch them. These explain rather than contradict each other, because a pooled corpus stacks many idiolects while any one writer is more repetitive than a model imitating them. When matching a sample, the repetition target is the author's, not the corpus's. Confidence: the reversal rests substantially on recent preprints.

**Sentence length flipped direction between model generations.** Gude et al., "More Aligned, Less Diverse? Analyzing the Grammar and Lexicon of Two Generations of LLMs" (arXiv:2605.06030), parsed NYT news against two LLM generations. 2023 models averaged shorter sentences than human writers; 2025 instruction-tuned models run 15 to 30% longer, and cut short sentences (1 to 15 tokens) by a large factor. Parse coverage is higher for the newer models than for the humans they imitate, so newer output is more grammatically well-formed than the baseline. Single study, news genre only, and it counts parser tokens where a writing agent counts words, so treat the figures as directional. Practical consequence: any humanizing advice written before 2025 has the sentence-length gap backwards.

**Grammar and rhetorical style.** Reinhart, Markey, Laudenbach, Pantusen, Yurko, Weinberg and Brown, "Do LLMs write like humans? Variation in grammatical and rhetorical styles" (PNAS 122, 2025, e2422455122; arXiv:2410.16107). Parallel human and LLM corpora from common prompts, scored on Douglas Biber's feature set. Instruction-tuned models overuse present participial clauses (GPT-4o roughly 5x human), nominalizations (roughly 2x), that-clauses as subject, and phrasal coordination, and underuse the agentless passive (roughly 0.5x). Base Llama 3 models sit near human rates. From the abstract: the differences "are larger for instruction-tuned models than base models." This is the most useful single study in this file, because the features are greppable and survive every word swap. Two caveats: published summaries disagree on some exact effect sizes, so quote multipliers rather than decimals, and the study measures unedited generation, so it establishes that word swaps and formatting cleanup leave these features untouched, not that they survive a deliberate rewrite.

**Stylometric feature sets.** Forensic authorship attribution (Koppel et al.; StyloMetrix/LightGBM work at arXiv:2507.00838) classifies on function-word distributions, part-of-speech ratios, and punctuation counts. That work found LLM text more grammatically uniform. None of these features are touched by banning words.

**Syntactic drift from LLM editing.** Sung, Csuros and Sung, "Comparing human and LLM proofreading in L2 writing" (arXiv:2506.09021, ACL BEA 2025). Human editors and three models proofread the same 656 learner essays. Every model raised nonfinite clauses, nominalizations, and total clause count where human editing held roughly flat. Cross-model correlation on syntactic features ran 0.53 to 0.65, so this is model behavior rather than one model's quirk. Heavy caveat: the corpus is A2 to B2 learner English, and turning ungrammatical text into fluent text legitimately adds these structures. It establishes that editing models reach for them, not that the magnitude transfers to already-fluent prose. Muñoz-Ortiz et al. (arXiv:2308.09067) carries the direction on generated rather than edited text: auxiliaries, subordinate clauses, and verb phrases all above the human baseline.

---

## The post-ChatGPT vocabulary spike

**Kobak et al.**, "Delving into LLM-assisted writing in biomedical publications through excess vocabulary" (Science Advances 2025; arXiv:2406.07016). Analyzed 15.1M PubMed abstracts from 2010 to 2024 using an "excess vocabulary" method modeled on COVID excess-mortality studies. Conclusion: "at least 13.5% of 2024 abstracts were processed with LLMs," reaching 40% for some subcorpora. Excess style words: *delves, showcasing, underscore, pivotal, intricate, meticulously, realm, aligns*.

**Liang et al.** (Stanford, arXiv:2403.07183, ICML 2024). Studied peer reviews at ICLR 2024, NeurIPS 2023, CoRL 2023, EMNLP 2023. Found "between 6.5% and 16.9% of text submitted as peer reviews to these conferences could have been substantially modified by LLMs," with *commendable, innovative, notable, versatile* spiking.

**Juzek and Ward** (FSU, arXiv:2412.11385). Identified 21 focal words and traced the overuse partly to RLHF (reinforcement learning from human feedback), which is the mechanism worth remembering.

**The decline effect.** Several of these words are now falling as writers scrub them; "delve" dropped once it became a known tell. This is why a static banned-word list ages badly and why the mechanism matters more than the list. Geng and Trotta, "Human-LLM Coevolution: Evidence from Academic Writing" (arXiv:2502.09606), put numbers on it: in arXiv abstracts "delve" and "intricate" start dropping after the peer-review studies named them, while unnamed LLM-associated words keep rising and "is" and "are" keep falling. The live markers are always the ones no listicle has named yet, which is why copula avoidance is currently worth more attention than any word on the excess-vocabulary lists.

**The convergence effect: the human baseline is moving toward the model.** Yakura et al., "Empirical evidence of Large Language Model's influence on human spoken communication" (arXiv:2409.01754), find "delve," "showcase," "boast," "intricacies," and "meticulous" rising abruptly in spontaneous human speech after ChatGPT's release, with a synthetic-control analysis over hundreds of thousands of hours of podcast audio linking the shift causally. Punctuation moves the same way: em dashes appear in roughly 4% of medRxiv discussion sections before ChatGPT and about 20% by 2025. Editing consequence: presence of a flagged word is weaker evidence every year, and when the text is someone else's, check the word against their earlier writing before cutting it.

**Voice under revision.** van Nuenen, "Voice Under Revision: Large Language Models and the Normalization of Personal Narrative" (arXiv:2604.22142). 2,700 rewrites of 300 personal narratives by three frontier models under three prompt conditions. All 13 stylometric markers moved the same direction in all three models: contractions, first-person pronouns, and function words down, lexical diversity, word length, and punctuation up. Matching a rewrite back to its source author dropped to a few percent. A voice-preserving prompt reduced the drift by about a third but did not change its direction. This is the empirical case for "edit, do not rewrite." Caveat: single-author preprint on short first-person narrative, so magnitudes may not transfer to argument or docs.

---

## Punctuation

**arXiv:2603.27006**, "The Last Fingerprint: How Markdown Training Shapes LLM Prose" (experiments conducted February to March 2026). GPT-4.1 produces 10.62 em dashes per 1,000 words unconstrained and 9.10 under suppression, and retains 3.86 even when the em dash is named explicitly in the instruction. Claude Opus drops from 9.09 to 0.19 under suppression. Meta's Llama models produce zero in either condition across approximately 40,000 words. Human baseline measured across eight published essays totaling 57,232 words.

Caveat: single preprint, one set of experiments. Treat as indicative. Note also that the em dash is defended as legitimately human by the Washington Post, Rolling Stone, and The Ringer; the real signal is overuse and misplacement, not presence.

---

## Formatting

**Wikipedia WikiProject AI Cleanup, "Signs of AI writing"** (created August 2025). The most empirically grounded practitioner catalog, built from thousands of real edits, self-described as descriptive rather than prescriptive. Source for the title-case headings, bold-term-colon lists, appended "Conclusion" sections, "Challenges"/"Future Prospects" formula, markdown artifacts, and heading-level quirks in `ai-tells.md`. The editors themselves warn that some of these conflate newbie writing with AI writing.

---

## Fabricated specifics

Hallucination arrives wearing the costume good writing wears, which is why the concreteness quota in pass 4 needs a sourcing rule attached. Documented production failures in 2025 include a freelancer published by multiple outlets who did not exist and who invented a town and its sources, a columnist found to have unverifiable AI-generated quotes across a third of his posts, and a local-paper reporter who resigned after seven stories carried fabricated quotes from real public officials including a sitting governor. Press Gazette maintains a running tracker.

Jakesch, Hancock and Naaman, "Human heuristics for AI-generated language are flawed" (PNAS 120(11) e2208839120, 2023; N = 4,600 across six experiments) explains why this is deception rather than colour. Readers judged AI self-presentations at chance (50 to 52%), running on heuristics that associate first-person pronouns, contractions, and family topics with human authorship, all of which models produce readily. The authors conclude the heuristics are manipulable, "allowing AI systems to produce language perceived as more human than human." A fabricated anecdote is therefore not a style choice, it is the most effective available lie. Caveat: the tested genre was short self-presentations, not long-form prose.

Note what this study does to the premise of this whole skill: it is the closest thing here to a reader study, and its result is that readers cannot reliably tell and their instincts run backwards. That argues for optimizing writing quality directly, not for feature-matching against a human distribution.

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

**Stance and polarity.** Herbold et al. (2023), Mizumoto et al. (2024), and Jiang and Hyland (2025) find human writing carries *more* epistemic stance marking (might, can, should, must) than LLM text, not less; Reinhart et al. report reproducing this. Jiang and Hyland further find ChatGPT essays lower on hedges, boosters, and attitude markers together, which reads impersonal rather than cautious. Note the direction before citing any of it: the deficit is commitment, not restraint. This is why the pass-1 hedging rule targets impersonal hedge stacks and explicitly protects first-person doubt.

**Structure and revision.** Kim et al., "Argument Collapse" (arXiv:2606.01736), find LLM essays follow a more fixed arc, opening with a direct claim and moving quickly to proposals, with far less distinct argumentation across a debate than human writers produce. Brei et al., "CASPER in the Machine" (arXiv:2606.22454), classified protagonists across eight narratological dimensions in human and LLM stories and found the human and model profiles differ on exactly one: closure. Heavy caveats on the second (short fiction, LLM-as-judge classification, amateur human baseline), and transfer from fiction to essays is inference, not finding. Sommers, "Revision Strategies of Student Writers and Experienced Adult Writers" (CCC 31(4), 1980), is the founding study on revision: students "are aware of lexical repetition, but not conceptual repetition" and reach for a thesaurus, while experienced writers describe their objective as "finding the form or shape of their argument." Qualitative and small, so it carries no statistical weight.

**Craft canon:** Joseph Williams (*Style*), Steven Pinker (*The Sense of Style*), William Zinsser (*On Writing Well*), Roy Peter Clark (*Writing Tools*), Verlyn Klinkenborg (*Several Short Sentences About Writing*), Gary Provost, Graff and Birkenstein (*They Say / I Say*). Canonical and well attested. Reduced to applicable form in `craft-principles.md`.

---

## Confidence notes

- **High confidence:** the stylometry and detection findings (Kobak; Liang 2023 and 2024; Sadasivan; Krishna; Reinhart PNAS 2025; Jakesch PNAS 2023) are peer-reviewed or widely cited. The craft principles are canonical.
- **Indicative only:** the em dash figures come from a single 2026 preprint. Burstiness threshold numbers from commercial sites are uncorroborated by GPTZero. The syntactic-drift direction replicates across corpora, but the proofreading magnitudes come from L2 learner text and do not transfer to fluent prose. The convergence and voice-under-revision findings are preprints sampling academics, podcasters, and short first-person narrative; directions are supported, magnitudes for general writers are not.
- **Descriptive, not authoritative:** the Wikipedia catalog is a practitioner essay that warns about its own false positives.
- **Moving target:** the entire lexical layer. Re-check rather than trusting memory.

**The gap in all of it.** Every study here is descriptive: it measures how LLM text differs from human text on some feature. None demonstrates that moving a feature toward the human distribution makes the writing better, or that readers notice. Jakesch et al. is the closest thing to a reader study and its result cuts the other way. Treat every feature target in this skill as a proxy, and the pass-7 read as the actual check.

**Second gap.** Almost everything here measures *unedited generation*, while this skill instructs *editing*. Only the L2 proofreading study and the voice-under-revision preprint look at what a model does when it edits, and both are narrow. That these features survive an editing pass is the premise of the skill and it rests on thin evidence.

**What would change the guidance:** if a future model ships with varied burstiness, human-rate participial and nominalization use, and no formatting tells by default, the removal passes shrink toward nothing and voice, structure, and stakes become the whole job. If retrieval or logging-based provenance (as Krishna et al. propose) becomes standard, the evasion-is-futile framing gets stronger still.
