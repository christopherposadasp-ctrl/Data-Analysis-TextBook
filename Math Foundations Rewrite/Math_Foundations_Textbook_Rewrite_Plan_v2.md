# Math Foundations Textbook Rewrite Plan v2

## Purpose

Turn `MathFoundationsNotes.pdf` into a standalone textbook for the next cohort while preserving all Data Analysis textbook dependencies recorded in `MF_Connections_Map.md`.

## Governing Policy

- Keep the Math Foundations textbook chronological, following the current notes order.
- Do not reorganize the main textbook around Data Analysis dependencies.
- Use Appendix A as the Data Analysis Bridge Index.
- Preserve every concept listed in `MF_Connections_Map.md`.
- Do not update Data Analysis references until the Math Foundations labels compile in the new book.

## Length Constraint

- Current notes length: 123 pages.
- Target main body: 128--133 pages.
- Absolute body cap: about 135 pages.
- Front/back buffer: about 6 pages.
- Practical total cap: about 141 pages.

## Chronological Chapter Structure

- Chapter 1. Logic and Deductive Reasoning
- Chapter 2. Vectors in R^n
- Chapter 3. Vector Operations and Linear Combinations
- Chapter 4. Sets, Set Operations, and Quantifiers
- Chapter 5. Dot Products, Norms, Distance, Angles, and Orthogonality
- Chapter 6. Linear Independence, Span, Bases, and Dimension
- Chapter 7. Matrices and Matrix-Vector Multiplication
- Chapter 8. Linear Systems, Polynomial Systems, and Vandermonde Matrices
- Chapter 9. Orthogonal Bases, Gram-Schmidt, and QR
- Chapter 10. Matrix Inverses, Rank, and Pseudoinverses
- Chapter 11. Subspaces: Column Space, Row Space, and Null Space
- Chapter 12. Multivariable Functions, Gradients, and Least Squares
- Chapter 13. Hessians, Quadratic Forms, and Second-Order Conditions
- Appendix A. Data Analysis Bridge Index

## Required Metadata

- `metadata/MF_Label_Registry.csv`
- `metadata/MF_DA_Crosswalk.csv`
- `metadata/Old_Page_to_New_Label_Map.csv`
- `metadata/Acknowledgments_Name_Audit.csv`

## Current Implementation Status

- Future Math Foundations targets have been filled in `MF_Connections_Map.md`.
- Metadata CSVs have been initialized.
- The middle chapter order has been revised so linear systems and Vandermonde matrices precede Gram-Schmidt/QR, and inverses/rank/subspaces follow afterward.
- Set labels are normalized on the singular `mf:set-*` convention.
- Identifiability-related Data Analysis rows now include `mf:null-space` as a future target.
- A short `mf:least-squares-projection-bridge` label has been added for Data Analysis projection language without creating a long new chapter.
- A preliminary acknowledgments name audit was run against `MathFoundationsNotes.pdf` using extracted text. Entries marked unclear need manual page-image verification before final acknowledgments.
