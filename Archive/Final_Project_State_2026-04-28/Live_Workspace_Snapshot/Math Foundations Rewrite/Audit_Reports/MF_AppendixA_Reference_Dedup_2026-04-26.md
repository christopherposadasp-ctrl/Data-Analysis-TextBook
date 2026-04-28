# Appendix A Reference Deduplication

Date: 2026-04-26

## Decision

Applied Pro's targeted cleanup request for Appendix A. This was a reference-list deduplication pass only; Appendix A was not expanded or redrafted.

## What changed

Removed redundant nearby `\ref{...}` calls that rendered to the same section number within the same Appendix A lookup entry.

Examples of cleaned duplicate rendered references:

- `3.2` repeated within vector/centering entries.
- `5.8` repeated within the correlation entry.
- `12.11` repeated within the normal-equations entry.
- `12.12` repeated within projection and residual-diagnostics entries.
- `10.5` repeated within full-column-rank and Data Analysis Chapters 7--8 entries.

## Guardrails preserved

- Appendix A remains a compact Data Analysis Bridge Index.
- The source still uses labels and `\ref{...}` rather than hard-coded section numbers.
- Conceptual content was not expanded.
- The full `MF_Connections_Map` rows were not reproduced.
- Data Analysis textbook references were not updated.

## QA result

- Duplicate rendered section references inside Appendix A lookup entries: 0.
- Hard-coded section-number references in Appendix A: 0.
- Full pilot compiles successfully.
- PDF remains 96 pages.
- No unresolved references.
- No overfull-box warnings.

Remaining warnings are unchanged: Ch02 bookmark warnings plus cosmetic underfull lines in dense Appendix A lookup entries.
