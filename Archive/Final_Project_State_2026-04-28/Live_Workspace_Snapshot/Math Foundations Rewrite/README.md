# Math Foundations Rewrite

This folder is the workspace for turning `MathFoundationsNotes.pdf` into its own textbook while preserving the Data Analysis textbook connections that already depend on it.

## Current Contents

- `MF_Connections_Map.md`: consolidated map of every current Math Foundations source-map entry and integrated connection callout in the Data Analysis textbook.
- `Math_Foundations_Textbook_Rewrite_Plan_v2.md`: current rewrite plan, including chronological chapter structure and length constraints.
- `metadata\MF_Label_Registry.csv`: proposed stable labels and their chronological chapter/section targets.
- `metadata\MF_DA_Crosswalk.csv`: row-level crosswalk from Data Analysis dependencies to future Math Foundations labels.
- `metadata\Old_Page_to_New_Label_Map.csv`: old notes page references grouped to future labels.
- `metadata\Acknowledgments_Name_Audit.csv`: preliminary contributor-name audit from the Math Foundations notes.
- `metadata\MF_Label_Implementation_Status.csv`: label registry with implementation status based on current `Sources\` labels.
- `metadata\MF_DA_Crosswalk_Implementation_Status.csv`: Data Analysis dependency crosswalk with implemented and remaining future labels.
- `Sources\`: current Math Foundations pilot chapter sources plus Appendix A.
- `Builds\Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.pdf`: compiled pilot PDF for acknowledgments, Chapters 1--13, and Appendix A.
- `tools\update_mf_rewrite_metadata.py`: reproducible generator for the map and metadata files.
- `tools\update_mf_implementation_status.py`: reproducible generator for implementation-status metadata based on current pilot sources.
- `Context Handoff - Pro\`: clean copy-only folder containing the current files to upload to Pro for review or archival handoff.

## Source Inputs

- Current Data Analysis textbook sources: `..\0. Current Textbook\Sources`
- Current Math Foundations notes: `..\MathFoundationsNotes.pdf`

## Working Rule

Before rewriting or reorganizing Math Foundations, preserve the concepts listed in `MF_Connections_Map.md`. The rewrite can improve order, explanation, and notation, but it should not orphan the Data Analysis textbook references.

The Math Foundations textbook should remain chronological. Use Appendix A as the Data Analysis bridge index rather than reorganizing the main book around Data Analysis dependencies.

Label cleanup status: the current metadata uses the singular `mf:set-*` convention, includes `mf:null-space` on identifiability-related dependencies, and includes `mf:least-squares-projection-bridge` for Data Analysis projection language.

Pilot drafting status: Chapters 1--13 and Appendix A have been audited, integrated, and compiled. A front-matter acknowledgments page now credits Dr. Bassett and the corrected scribe / highlighted-note-taker list. Chapter 5 was accepted with only minor line-length cleanup; its corrected Earth-geometry formula is retained because it reproduces the numeric answers in the source notes. Chapter 6 was accepted with minor line-length cleanup and remains within the approved scope boundaries. Chapter 7 was accepted with minor line-length cleanup and keeps inverses, rank, subspaces, QR, and least squares as later topics. Chapter 8 was accepted with guardrail wording that keeps QR as a preview and least squares as motivation only. Chapter 9 was accepted with minor QR precision cleanup: thin-QR identities now use \(Q^TQ=I_k\), and the exact QR solve states the consistency condition. Chapter 10 was accepted with minor pseudo-inverse notation and bookmark cleanup while keeping column/row/null subspace geometry deferred to Chapter 11. Chapter 11 was accepted with minor residual-orthogonality precision cleanup and keeps full least-squares theory deferred to Chapter 12. Chapter 12 was accepted with minor pseudo-inverse notation consistency and neural-network derivative-notation cleanup while keeping Hessian and second-order material deferred to Chapter 13. Chapter 13 was accepted with minor second-derivative-test wording cleanup. Appendix A was provisionally accepted as a compact Data Analysis Bridge Index and has received a targeted repeated-section-reference deduplication pass; do not expand it into a teaching chapter. A precision/directness pass has now been integrated for Chapters 5, 8, 9, 12, and 13, with Ch09's independent-column QR-solve condition preserved during integration. All 61 registry labels are implemented, and all 108 current Data Analysis crosswalk rows have their primary labels implemented.

Chapter summary directness status: summary-only trims have been integrated for Chapters 1--13. Ch07 and Ch09 off-scope body differences from the incoming bundle were not accepted; the current source preserves the prior Ch09 independent-column and consistency conditions for the QR triangular-solve discussion. The production pilot now compiles to 92 pages with no unresolved references and no overfull boxes.

High-priority precision status: Pro's Ch01, Ch11, and Ch12 precision fixes have been integrated without rolling back the chapter-summary directness pass. The source now includes the corrected Ch01 logic translation, Ch11 if-and-only-if column-space solvability wording, Ch12 unknown-vector least-squares setup, and Ch12 Jacobian convention note. The production pilot remains 92 pages with no unresolved references and no overfull boxes.

Pedagogical expansion status: Pro's four small clarity additions in Ch08, Ch09, Ch12, and Ch13 have been audited and accepted. The additions cover duplicate-input interpolation, numerical Gram-Schmidt dependence checks, least-squares projection/shadow intuition, and the meaning of an inconclusive semidefinite-but-not-definite second-derivative test. The production pilot remains 92 pages with no unresolved references and no overfull boxes.

Layout status: the adjusted Best Balanced chapter-opening layout has been applied in the wrapper only. Chapter openings, Appendix A, Contents, and Acknowledgments now use compact centered headings near the top text margin. The production pilot now compiles to 91 pages with no unresolved references and no overfull boxes; remaining warnings are the known Ch02 bookmark warnings and cosmetic Appendix A underfull lookup-table lines.

Chapter 2 margin status: Chapter 2 now uses a targeted `0.9269in` bottom margin in the wrapper, the smallest tested reduction that removes its short trailing page. The canonical build PDF and Pro handoff PDF have both been refreshed to the verified 90-page build with no unresolved references and no overfull boxes.

Chapter 9 QR example status: Pro's full \(3\times 3\) Gram-Schmidt-to-QR worked example has been audited and integrated. The example is placed after QR construction and before QR triangular solve, preserves the existing numerical Gram-Schmidt tolerance note, and includes a bookmark-safe optional subsection title. The production pilot now compiles to 93 pages with no unresolved references, no duplicate labels, and no overfull boxes.

Acknowledgments status: the updated acknowledgments page has been audited and integrated. It now credits Dr. Bassett, the scribes / highlighted note takers, Chris Posadas's role in the rewrite, and the human-directed ChatGPT/Codex workflow. The page compiles cleanly and remains one page.

Final targeted fixes status: Pro's final targeted fixes for Chapters 7, 8, 10, 11, 12, and 13 have been audited and integrated by applying the narrow patch to the live sources. The fixes clarify software-facing matrix operations, early column-space notation, full-rank pseudoinverse convention, nonempty subspaces, full-column-rank least-squares assumptions, and second-derivative-test smoothness. The production pilot now compiles to 94 pages with no unresolved references, no duplicate-label warnings, and no overfull boxes.

Release-candidate QA status: Pro completed the full mathematical audit and reported no mathematical issues. A final production QA pass in Here rebuilt the pilot, verified 94 pages, verified zero unresolved references, zero duplicate-label warnings, zero overfull boxes, zero Hyperref warnings, and only the known cosmetic Appendix A underfull lookup-table warnings. PDF bookmarks now include chapter and section numbering, including Appendix A numbering, and the Chapter 2 \(R^n\) bookmark text is warning-free. The Pro handoff PDF and source package have been refreshed from the live build.

Ch06 label guardrail: `mf:orthonormal-basis-note` is only an introductory Ch06 source label. It is not a substitute for the Ch09 labels `mf:orthogonal-bases`, `mf:gram-schmidt`, `mf:qr-factorization`, or `mf:orthogonal-polynomials`.
