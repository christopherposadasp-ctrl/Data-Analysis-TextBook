# Coding and Software Cookbook Audit

Date: 2026-04-28

## Verdict

Accepted for current textbook folder as the standalone coding companion.

The live source already uses student-facing "cookbook" and "companion" terminology. The only cleanup applied was wrapper-level formatting so the standalone PDF no longer presents itself as "Chapter 1" of another book.

## Files Restored / Built

- `Coding_and_Software_Cookbook_v3.tex`: restored standalone wrapper in `0. Current Textbook`.
- `Coding_and_Software_Cookbook_v3.pdf`: rebuilt standalone cookbook companion in `0. Current Textbook`.
- `Sources/Appendix_Coding_and_Software_Cookbook_v3.tex`: used as the live content source; content was not edited.

## Audit Checks

- Standalone build passed after two `pdflatex` passes.
- Page count: 34 pages.
- Undefined references: 0.
- Duplicate labels/destinations: 0.
- Overfull boxes: 0.
- Underfull boxes: 15, not visually concerning for code-heavy material.
- Source labels: 33, with 0 duplicates.
- Verbatim environments: 85 `\begin{verbatim}` and 85 `\end{verbatim}`.
- Visible stale appendix wording in extracted PDF text: 0 hits for "appendix" or "Appendix."
- Placeholder markers: 0 hits for visible `??`.

## Structure Check

The cookbook is organized as a workflow companion:

- project setup and reproducibility,
- general setup patterns,
- data quality and cleaning,
- EDA summaries and visuals,
- SLR workflow,
- fit quality and hypothesis testing,
- regression geometry and design matrices,
- MLR workflow,
- estimator behavior and residual objects,
- transformations and linear-in-parameters models,
- residual diagnostics and model repair,
- end-to-end mini workflow,
- troubleshooting,
- cookbook habits.

This matches the intended companion-document role: concepts remain in the textbook, while package-specific Python/R implementation patterns live here.

## Wrapper-Only Cleanup

The standalone wrapper was adjusted so the PDF does not label the cookbook as "Chapter 1." Section numbering now starts at `1`, `2`, `3`, etc. instead of `1.1`, `1.2`, `1.3`, etc.

No cookbook content, code recipes, labels, or source-map references were changed.
