# Pro Context: Data Analysis Final Audit Phase

Date prepared: 2026-04-28

## Current Project State

The Data Analysis textbook is in final audit before peer review by classmates.

The Math Foundations textbook is complete and should be treated as stable reference material only. Do not reopen, rewrite, expand, or trim the Math Foundations textbook unless Chris explicitly asks.

## Current Data Analysis Products

- `Data_Analysis_Textbook_Combined_v3.pdf`: main reference textbook, 165 pages.
- `Data_Analysis_Textbook_Core_Reader_v1.pdf`: compressed student Core Reader, 120 pages.
- `Coding_and_Software_Cookbook_v3.pdf`: standalone coding/software companion, 34 pages.
- `Source_Code_CURRENT/`: optional source-code package for source-level checking.

The Data Analysis project still uses one shared source architecture for the full reference and Core Reader. Do not change that architecture unless explicitly asked.

## Current Math Foundations Reference

- `Math_Foundations_Textbook_Pilot_CURRENT.pdf`: complete 94-page Math Foundations release-candidate textbook.
- `MF_Connections_Map.md`: preservation/crosswalk map from the Math Foundations rewrite work.

Math Foundations chapter structure:

1. Logic and Deductive Reasoning
2. Vectors in R^n
3. Vector Operations and Linear Combinations
4. Sets, Set Operations, and Quantifiers
5. Dot Products, Norms, Distance, Angles, and Orthogonality
6. Linear Independence, Span, Bases, and Dimension
7. Matrices and Matrix-Vector Multiplication
8. Linear Systems, Polynomial Systems, and Vandermonde Matrices
9. Orthogonal Bases, Gram-Schmidt, and QR
10. Matrix Inverses, Rank, and Pseudoinverses
11. Subspaces: Column Space, Row Space, and Null Space
12. Multivariable Functions, Gradients, and Least Squares
13. Hessians, Quadratic Forms, and Second-Order Conditions
Appendix A. Data Analysis Bridge Index

## Most Recent Codex Audit

### Final Tiny Product-Readiness Cleanup

See `Final_Tiny_Product_Readiness_Cleanup_Report_2026-04-28.md`.

Codex applied a final small cleanup:

- Cookbook Chapter 10 Python residual/Q-Q code block now uses straight double quotes in the displayed code.
- Core Reader title-page subtitle now says `Compressed student reader from the live shared textbook sources` instead of `Proof-of-concept core build...`.

Build QA after cleanup:

- Full reference: compiled, 165 pages.
- Core Reader: compiled, 120 pages.
- Cookbook companion: compiled, 34 pages.
- Undefined references: 0 in all three.
- Duplicate labels/destinations: 0 in all three.
- Overfull boxes: one known minor Chapter 4 table warning in the full reference; none in Core or Cookbook.

### Regression Spine Targeted Fixes

See `Codex_Integration_Regression_Spine_Targeted_Fixes_2026-04-28.md`.

Codex accepted and integrated Pro's targeted regression-spine fixes. Files changed:

- Chapter 5: fixed-design conditional assumption wording for the SLR assumption ladder.
- Chapter 7: full-column-rank qualifier and rank-deficient fallback for projection dimensions.
- Chapter 11: interaction indexing convention, random \(\mathbf{Y}\) in truth-plus-error theory, explicit realized-data estimator formula using observed \(\mathbf{y}\), full-rank qualifier in summary, and polynomial-example coefficient clarification.
- Chapter 12: standardized/internally/externally studentized residual terminology and full-design-row leverage clarification.

Build QA after integration:

- Full reference: compiled, 165 pages.
- Core Reader: compiled, 120 pages.
- Undefined references: 0.
- Duplicate labels/destinations: 0.
- Overfull boxes: one known minor Chapter 4 table warning in the full reference; none in the Core Reader.

### Coding and Software Cookbook Audit

See `Coding_and_Software_Cookbook_Audit_Report_2026-04-28.md`.

Codex restored the cookbook to the current textbook folder as a standalone companion product and rebuilt it from the live source.

Build QA:

- Cookbook companion: compiled, 34 pages.
- Undefined references: 0.
- Duplicate labels/destinations: 0.
- Overfull boxes: 0.
- Visible stale "appendix" wording in extracted PDF text: 0.

Only the standalone wrapper was adjusted: the PDF no longer presents the cookbook as "Chapter 1." The cookbook content source was not edited.

### Math Foundations Connection Paragraph Alignment

See `Codex_Audit_DA_MF_Connection_Paragraph_Alignment_2026-04-28.md`.

Codex accepted and integrated Pro's targeted Data Analysis / Math Foundations connection-paragraph alignment pass. Only six Data Analysis source files were edited:

- Chapter 3: first Math Foundations Connection paragraph now points to Math Foundations Chapters 2, 4, and 7.
- Chapter 8: added null-space/subspace ideas and Math Foundations Chapter 11.
- Chapter 9: added Math Foundations Chapter 12 for least-squares projection, residual orthogonality, and normal-equation logic.
- Chapter 10: added column-space/residual-space geometry and Math Foundations Chapter 11.
- Chapter 11: added full-column-rank inverse-like formulas and Math Foundations Chapter 10.
- Chapter 12: added column-space/residual-space geometry and Math Foundations Chapter 11.

Build QA after integration:

- Full reference: compiled, 165 pages.
- Core Reader: compiled, 120 pages.
- Undefined references: 0.
- Duplicate labels/destinations: 0.
- Overfull boxes: one known minor Chapter 4 table warning in the full reference; none in the Core Reader.
- Stale old-notes citation patterns in Data Analysis chapter sources: 0.

## Constraints For Pro

- Do not reopen the Math Foundations textbook.
- Do not add 3Blue1Brown links.
- Do not make broad rewrites.
- Do not trim for page count.
- Do not reorganize Data Analysis chapters.
- Do not change the shared full/core source architecture.
- Recommend only changes that materially improve correctness, clarity, teachability, or dependency preservation.

## Recommended Upload Order

For the first Pro task in the new thread, upload only:

1. `PRO_CONTEXT_CURRENT.md`
2. `Codex_Audit_DA_MF_Connection_Paragraph_Alignment_2026-04-28.md`
3. `Data_Analysis_Textbook_Combined_v3.pdf`
4. `Math_Foundations_Textbook_Pilot_CURRENT.pdf`

Upload `MF_Connections_Map.md` if Pro is checking source-map or dependency preservation details.

Upload `Data_Analysis_Textbook_Core_Reader_v1.pdf` only if Pro is checking whether the Core Reader still reflects the same source architecture.

Upload `Source_Code_CURRENT/` only if Pro asks for source-level review or exact LaTeX references. Do not start with source files unless needed; the first audit task is conceptual agreement/disagreement with Codex's audit.

## Suggested First Pro Response Target

Ask Pro to return:

1. Verdict: agree / agree with minor caveat / disagree.
2. Smallest required fix, if any.
3. Next final-audit step before sending the Data Analysis textbook to classmates.
4. Concise Codex handoff prompt if an implementation pass is needed.
