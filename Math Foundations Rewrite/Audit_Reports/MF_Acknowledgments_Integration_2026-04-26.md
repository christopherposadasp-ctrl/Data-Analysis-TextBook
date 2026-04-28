# Math Foundations Acknowledgments Integration

Date: 2026-04-26

## Decision

Added a front-matter acknowledgments page to the Math Foundations pilot now that the contributor names have been corrected.

## Files changed

- `Sources\FrontMatter_Acknowledgments_v1.tex`
- `Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.tex`
- `metadata\Acknowledgments_Name_Audit.csv`
- `tools\update_mf_rewrite_metadata.py`

## Content added

The acknowledgments page credits:

- Dr. Bassett for the course structure, mathematical direction, and original instructional framing.
- The corrected scribe / highlighted-note-taker list from the acknowledgments audit.

The page also clarifies that any remaining errors in the rewritten textbook belong to the textbook project, not to the original contributors.

## Metadata cleanup

The corrected names were reflected in the active acknowledgments audit and in the metadata-generation script so future regeneration does not restore stale uncertainty markers or older name variants.

Corrected entries include:

- Brandon De La Rosa
- Paul Deist
- Camille Herman
- Ryan Berry
- Katerina Franco

## Build result

Rebuilt `Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.tex` successfully with two `pdflatex` passes.

- PDF: `Builds\Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.pdf`
- Page count: 96 pages
- Acknowledgments appears in the table of contents.
- No unresolved references.
- No overfull-box warnings.

Remaining warnings are the known Ch02 PDF-string warnings and cosmetic underfull lines in Appendix A lookup entries.
