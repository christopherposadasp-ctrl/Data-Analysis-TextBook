# Final Tiny Product-Readiness Cleanup

Date: 2026-04-28

## Changes Made

- `Sources/Appendix_Coding_and_Software_Cookbook_v3.tex`
  - Normalized the Chapter 10 Python residual/Q-Q code block to straight double quotes:
    - `ax.axhline(0, linestyle="--")`
    - `ax.set_xlabel("Fitted values")`
    - `ax.set_ylabel("Residuals")`
    - `ax.set_title("Residuals vs fitted values")`
    - `sm.qqplot(resid, line="45")`
- `Data_Analysis_Textbook_Core_Reader_v1.tex`
  - Replaced the title-page subtitle:
    - from `Proof-of-concept core build from the live shared textbook sources`
    - to `Compressed student reader from the live shared textbook sources`

## Validation

- Full reference build: passed, 165 pages.
- Core Reader build: passed, 120 pages.
- Coding and Software Cookbook build: passed, 34 pages.
- Undefined references: 0 in all three builds.
- Duplicate labels/destinations: 0 in all three builds.
- Overfull boxes:
  - Full reference: 1 known pre-existing Chapter 4 table warning.
  - Core Reader: 0.
  - Cookbook: 0.
- Smart quotes inside cookbook verbatim code blocks: 0.
- Extracted cookbook PDF text for the targeted Python residual/Q-Q code lines shows straight double quotes.

## Guardrails

- Math Foundations sources were not edited.
- Data Analysis chapter organization was not changed.
- Page count was not intentionally trimmed.
- No external links were added.
- Shared full/core architecture was not changed.
