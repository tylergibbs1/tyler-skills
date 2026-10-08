# Scholarly retrieval and novelty audit

Use this reference when collecting papers or investigating whether a hypothesis is already known.

## Trustworthy starting points

- OpenAlex (cross-disciplinary works, citations, metadata): https://openalex.org/ ; search guidance https://help.openalex.org/api/searching/
- Europe PMC (life sciences records and a subset of open-access full text): https://europepmc.org/developers
- PubMed and NCBI E-utilities (biomedical records): https://www.ncbi.nlm.nih.gov/books/NBK25501/
- Crossref (DOI metadata and resolution): https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- arXiv (preprints; distinguish from peer-reviewed results): https://info.arxiv.org/help/api/index.html
- Domain-specific repositories and study supplements for data, **only** where access and license permit.

Metadata indexing is not full-text permission. Locate and inspect the original paper or publisher's record for decisive claims. Mark `metadata-only` or `abstract-only` when necessary.

## Search method

1. Define A, B, C, the outcome, moderator/context and competing mechanism. Expand aliases, acronyms, historical terms, gene/chemical variants and neighboring disciplines.
2. Search **each claimed edge** separately (`A B`, `B C`) and direct links (`A C`). Search negations and failure modes (`no effect`, `failed to replicate`, `null result`, `contradictory`), not just positive findings.
3. Track direct citations, backwards references, later citing literature, systematic reviews, and relevant preprints. Trace critical review statements back to primary studies.
4. Include credible independent replication and contradictory/null studies. Normalize DOI/PMID/arXiv IDs and deduplicate preprints vs published copies.
5. Log source name, date/time, exact query/filter, result count if known, screened items, inclusion/exclusion reasons, and access/coverage limitations.
6. Stop at an explicit scope/budget; describe the collection as exploratory unless a systematic review protocol was actually followed.

## Claim ledger fields

| Field | Expected content |
|---|---|
| id + work_id | C01; DOI/PMID/arXiv/persistent URL |
| bibliographic | Title and year (authors when verified) |
| precise_claim | Paraphrased conditional result, measured quantities, direction |
| location + access | Page/section/figure/table, or `abstract-only` |
| context | Organism/cohort/material, scale, instrument, comparator, protocol |
| evidence | Design, sample size, effect and uncertainty **if reported** |
| weakness | Confounds, bias, contradictory findings, limitations |

A→B and B→C are sourced claims; A→C is a **hypothesis** until directly tested.

## Prior-art verdicts

- **Already studied:** A direct test of substantially the same conditional relationship exists.
- **Partial extension:** Similar mechanism studied in another material/population/setting, but the proposed boundary or outcome differs.
- **Not found in scoped search:** Search disclosed, no direct result found; not an assertion of novelty.
- **Unresolved:** Search access, terminology, coverage, or evidence insufficient to decide.

Before a `not found` verdict, check synonymous descriptions, related research communities, reviews, older work, patents where relevant, and negative findings. Cite closest matches and counterexamples. Never infer a discovery from absence of hits.
