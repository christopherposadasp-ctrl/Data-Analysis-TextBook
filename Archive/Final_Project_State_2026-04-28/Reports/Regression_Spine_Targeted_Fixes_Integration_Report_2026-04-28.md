# Regression Spine Targeted Fixes Integration

Date: 2026-04-28

## Verdict

Accepted with minor local cleanup.

Pro's targeted fixes for Chapters 5, 7, and 12 were integrated into the live Data Analysis sources. The remaining Chapter 11 fixes that Pro could not apply were applied directly against the live source.

## Exact Files Changed

- `Sources/Ch05_Simple_Linear_Regression_Model_Assumptions_Least_Squares_Estimation_v3.tex`
- `Sources/Ch07_Linear_Regression_as_Projection_Design_Matrix_Hat_Matrix_v3.tex`
- `Sources/Ch11_Linear_Models_Beyond_Straight_Lines_Transformations_Linear_in_Parameters_v3.tex`
- `Sources/Ch12_Residual_Analysis_Model_Repair_v3.tex`

## Final Edits

### Chapter 5

- Updated Assumption 2 to use fixed-design conditional language.
- Made the cross-observation covariance condition conditional on the observed predictor values.
- Updated Assumption 3 to the conditional Gaussian vector statement.
- Updated the assumption ladder table to match the clarified conditional wording.

### Chapter 7

- Qualified the Chapter Summary statement about \((p+1)\)-dimensional column space and \((n-p-1)\)-dimensional residual space with the full-column-rank assumption.
- Added the rank-deficient fallback: if \(\operatorname{rank}(\mathbf{X})=r\), use \(r\) and \(n-r\).

### Chapter 11

- Corrected interaction indexing to match the book-wide convention \(x_{ij}\) = predictor \(j\) for observation \(i\).
- Updated the interaction design matrix rows to use \(x_{11},x_{12}\), \(x_{21},x_{22}\), through \(x_{n1},x_{n2}\).
- In the truth-plus-error section, used random response vector \(\mathbf{Y}\) for theoretical expectation and variance derivations.
- Added an explicit computational bridge: the realized data set uses \(\widehat{\boldsymbol{\theta}}=(\mathbf{Z}^T\mathbf{Z})^{-1}\mathbf{Z}^T\mathbf{y}\), while the truth-plus-error expression is for studying estimator behavior because \(\boldsymbol{\theta}\) and \(\boldsymbol{\epsilon}\) are unknown.
- Added a full-column-rank qualifier before the inverse-form estimator in the Chapter Summary.
- Added a compact non-identifiability sentence for singular \(\mathbf{Z}^T\mathbf{Z}\).
- Added a short clarification that the polynomial example's \(\boldsymbol{\beta}\) plays the same transformed-coefficient role as \(\boldsymbol{\theta}\).

### Chapter 12

- Clarified that the leverage-adjusted residual formula is often called an internally studentized residual.
- Distinguished externally studentized residuals as using a leave-one-out estimate of \(\sigma\).
- Applied the same distinction in the Core Reader branch.
- Clarified that \(\mathbf{x}_i^T\) in the leverage formula is the full design row, including intercept, transformed columns, and interaction columns.

## Deviations From Pro Patch

- Chapter 11 was not in Pro's editable source set, so those fixes were applied manually to the live source.
- One Chapter 11 summary sentence was lightly cleaned from "applies, if" to "then, if ..., ordinary least squares uses the inverse form" for readability.
- No other substantive deviations.

## Build QA

- Full reference build: passed after two `pdflatex` passes.
- Full reference page count: 165 pages.
- Core Reader build: passed after two `pdflatex` passes.
- Core Reader page count: 120 pages.
- Undefined references: 0 in both builds.
- Duplicate labels/destinations: 0 in both builds.
- Overfull boxes: 1 in the full reference, from the pre-existing Chapter 4 table warning (`3.27228pt`); 0 in the Core Reader.
- Underfull boxes: 169 in the full reference; 44 in the Core Reader.

## Standalone Chapter PDF Refresh

- `Ch05_Simple_Linear_Regression_Model_Assumptions_Least_Squares_Estimation_v3.pdf`: 15 pages.
- `Ch07_Linear_Regression_as_Projection_Design_Matrix_Hat_Matrix_v3.pdf`: 12 pages.
- `Ch11_Linear_Models_Beyond_Straight_Lines_Transformations_Linear_in_Parameters_v3.pdf`: 15 pages.
- `Ch12_Residual_Analysis_Model_Repair_v3.pdf`: 16 pages.

## Follow-Up Cleanup

After Pro reviewed this integration, Codex agreed with one additional Chapter 11 cleanup: make the realized-data bridge computationally explicit and avoid implying that the truth-plus-error expression is the formula students compute from data.

That cleanup was applied and the full/Core builds were rerun:

- Full reference build: passed, 165 pages.
- Core Reader build: passed, 120 pages.
- Undefined references: 0 in both builds.
- Duplicate labels/destinations: 0 in both builds.
- Overfull boxes: 1 known pre-existing Chapter 4 table warning in the full reference; 0 in the Core Reader.
- Math Foundations sources were not edited.
- Full/Core architecture was not changed.

## Guardrails Confirmed

- Math Foundations sources were not edited.
- Full/Core wrappers and shared source architecture were not changed.
- Chapters 6, 8, and 10 were not edited.
- No Data Analysis chapter reorganization was performed.
- No page-count trimming was performed.
