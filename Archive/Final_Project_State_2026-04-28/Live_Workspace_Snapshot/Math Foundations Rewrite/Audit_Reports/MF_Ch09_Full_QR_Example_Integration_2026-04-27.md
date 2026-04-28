# Math Foundations Chapter 9 Full QR Worked Example Integration

Date: 2026-04-27

## Verdict

Accepted with a minor integration fix.

The Pro-delivered worked \(3\times 3\) QR example is mathematically correct and pedagogically useful. During integration, the existing numerical Gram-Schmidt tolerance note was preserved because the delivered file accidentally removed it. A PDF-bookmark-safe optional subsection title was also added so the visible title keeps \(3\times 3\) while the PDF bookmark uses `3x3`.

## Placement

Inserted in `Sources\Ch09_Orthogonal_Bases_Gram_Schmidt_QR_v1.tex` after:

- `From Gram-Schmidt to QR Factorization`

and before:

- `Using QR to Solve a Linear System`

This preserves the intended flow:

Gram-Schmidt algorithm -> QR construction -> full worked QR example -> QR triangular solve.

## Mathematical QA

Passed.

The example uses

\[
A =
\begin{bmatrix}
1 & 1 & 0\\
1 & 0 & 1\\
0 & 1 & 2
\end{bmatrix}.
\]

Verified:

- \(r_{11}=\sqrt{2}\) and \(\mathbf{q}_1=(1/\sqrt{2})[1,1,0]^T\).
- \(r_{12}=1/\sqrt{2}\), \(\widetilde{\mathbf{q}}_2=[1/2,-1/2,1]^T\), \(r_{22}=\sqrt{6}/2\), and \(\mathbf{q}_2=(1/\sqrt{6})[1,-1,2]^T\).
- \(r_{13}=1/\sqrt{2}\), \(r_{23}=3/\sqrt{6}=\sqrt{6}/2\), \(\widetilde{\mathbf{q}}_3=[-1,1,1]^T\), \(r_{33}=\sqrt{3}\), and \(\mathbf{q}_3=(1/\sqrt{3})[-1,1,1]^T\).
- \(\mathbf{q}_1^T\mathbf{q}_2=0\), \(\mathbf{q}_1^T\mathbf{q}_3=0\), and \(\mathbf{q}_2^T\mathbf{q}_3=0\).
- Each \(\mathbf{q}_i\) has unit norm, so \(Q^TQ=I\).
- The displayed \(R\) entries match the Gram-Schmidt coefficients.
- \(QR=A\) column by column.
- The diagonal entries of \(R\) are positive: \(\sqrt{2}\), \(\sqrt{6}/2\), and \(\sqrt{3}\).

## Pedagogical QA

Passed.

The example improves student clarity because it shows where every \(r_{ij}\) entry comes from, why \(R\) is upper triangular, and how Gram-Schmidt becomes a concrete QR factorization. The length is justified: it is a full hand-executed example, not a software or coding digression.

Visual spot-checks of the Chapter 9 pages showed the layout remains readable.

## Guardrail QA

Passed.

- Chapter 10 still contains `QR^{-T}`.
- Appendix A was not changed or expanded.
- Data Analysis references were not updated.
- Chapter order and wrapper structure were not changed.
- Existing Chapter 9 material on numerical tolerance, QR factorization, QR triangular solve, and orthogonal-polynomial intuition remains present.
- Protected dependency concepts from `MF_Connections_Map.md` were not removed.

## Source / Label QA

Passed.

- Source labels: `227`.
- Duplicate labels: `0`.
- New label: `mf:qr-factorization-worked-example`.
- The new label is local/internal and does not conflict with the existing registry. It can be added to metadata during the next normal metadata regeneration pass if desired.
- No malformed LaTeX or missing-package requirement was introduced.

## Build QA

Production wrapper build:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -output-directory='Builds' 'Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.tex'
pdflatex -interaction=nonstopmode -halt-on-error -output-directory='Builds' 'Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.tex'
```

Result:

- Compile status: passed.
- Output PDF: `Builds\Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.pdf`.
- Page count: `93`.
- Page-count increase: `+3` pages relative to the previous 90-page build.
- Unresolved references: `0`.
- Duplicate-label warnings: `0`.
- Overfull boxes: `0`.
- Underfull boxes: `8`, all known Appendix A lookup-table warnings.
- Hyperref warnings: `2`, both existing Ch02 `R^n` bookmark warnings.

Refreshed:

- `Context Handoff - Pro\Math_Foundations_Textbook_Pilot_CURRENT.pdf`
- `Context Handoff - Pro\Source_Code_CURRENT\Sources\Ch09_Orthogonal_Bases_Gram_Schmidt_QR_v1.tex`
