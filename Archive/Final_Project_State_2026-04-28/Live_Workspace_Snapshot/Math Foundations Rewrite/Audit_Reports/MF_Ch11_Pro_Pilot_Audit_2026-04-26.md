# Math Foundations Ch11 Pro Pilot Audit

Audit date: 2026-04-26

Source bundle audited:

- `C:\Users\posad\Downloads\mf_ch11_pilot_bundle`

## Executive Finding

Chapter 11 is sound and should be accepted into the Math Foundations pilot after small precision and line-length cleanup. It covers subspaces, column space, row space, null space, left null space, orthogonality among the fundamental subspaces, rank-nullity, and a compact targeting example.

Recommendation: accept the `.tex` source, keep the chapter's current length, and do not ask Pro to redraft Ch11.

## Length And Concision Check

| Unit | Pages | Source lines | Approx. words | Notes |
|---|---:|---:|---:|---|
| Ch11 Subspaces: Column Space, Row Space, and Null Space | about 6 body pages in integrated pilot | 312 | 1,557 | Concise and complete for this source scope. |
| Combined Ch01-Ch11 pilot | 74 total PDF pages | n/a | n/a | Includes title page and table of contents. |

Length interpretation:

- Ch11 is under the 8-10 page target but not underdeveloped.
- The targeting example is compact and does not become a computational notebook.
- No reduction pass is needed.

Conclusion on length: keep Ch11.

## Source Coverage

The draft covers the assigned Math Foundations notes material:

- span, vector space, subspace, and dimension language,
- column space and row space,
- null space and proof that \(\operatorname{Null}(A)\) is a subspace,
- null-space criterion for independent columns,
- left null space,
- orthogonality among row/null and column/left-null spaces,
- four fundamental subspaces and rank-nullity relationships,
- underdetermined targeting example as null-space motivation.

## Required Label QA

Canonical Ch11 registry labels present:

- `mf:subspaces`
- `mf:column-space`
- `mf:row-space`
- `mf:null-space`

No duplicate labels were found.

## Scope QA

The chapter keeps later topics as forward references only:

- full least-squares theory and normal equations remain deferred to Ch12,
- Hessians, quadratic forms, and second-order conditions remain deferred to Ch13.

The Data Analysis bridge is short and appropriate: it connects column space, left null space, and null-space non-identifiability to fitted values, residuals, and exact multicollinearity.

## Cleanups Applied

- Clarified that residual vectors lie in the left null space for least-squares fits, not for arbitrary residuals.
- Shortened one Data Analysis bridge sentence to remove an overfull box.
- Kept all mathematical content and all implemented labels.

## Metadata Finding

Pro's Ch11 metadata update CSVs should not be merged directly.

Reasons:

- The project already has a reproducible implementation-status generator based on current source labels.
- The Pro CSVs are support artifacts for review and may include draft-specific status fields.

Action: regenerate implementation-status metadata from:

- `metadata\MF_Label_Registry.csv`
- `metadata\MF_DA_Crosswalk.csv`
- labels currently present in `Sources\Ch*.tex`

## Technical QA

Checks performed:

- Duplicate label scan: passed.
- Required Ch11 registry-label scan: passed.
- Scope search: passed; later topics are deferred and not developed.
- Ch01-Ch11 wrapper compile: passed after two `pdflatex` runs.

Remaining warnings in the combined pilot build:

- A duplicate `page.i` hyperref warning from the simple pilot wrapper/frontmatter.
- Two hyperref PDF-string warnings from Chapter 2's `R^n` title/bookmark text.

These are existing wrapper/bookmark issues, not Ch11 content issues.

## Actions Recommended

- Accept Ch11 into the pilot source set.
- Keep the concise length.
- Do not redraft Ch11.
- Ask Pro to draft Chapter 12 next: Multivariable Functions, Gradients, and Least Squares.
