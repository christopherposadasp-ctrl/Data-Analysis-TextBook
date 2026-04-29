# Data Analysis Expansion Protocol

Use this protocol for adding new course material after the v3 release.

## Active Products

- Active: `Data_Analysis_Textbook_Combined_v3.tex` and `Data_Analysis_Textbook_Combined_v3.pdf`.
- Active: `Coding_and_Software_Cookbook_v3.tex` and `Coding_and_Software_Cookbook_v3.pdf`.
- Stable reference only: `..\Math Foundations Rewrite\Math_Foundations_Ch01_Ch13_AppendixA_Pilot_v1.tex` and its current PDF.
- Inactive: `Data_Analysis_Textbook_Core_Reader_v1.tex` and `Data_Analysis_Textbook_Core_Reader_v1.pdf`.

Do not update the Core Reader unless it is explicitly reactivated.

## Required Context Before New Work

Before planning or implementing new material, read:
- `CURRENT_STATUS.md`
- `DA_EXPANSION_PROTOCOL.md`
- `Data_Analysis_Textbook_Combined_v3.tex`
- `Coding_and_Software_Cookbook_v3.tex`
- relevant files in `Sources\`
- `..\Math Foundations Rewrite\README.md`
- `..\Math Foundations Rewrite\MF_Connections_Map.md`

New lecture material currently enters through:
- `..\1. Lectures-Raw\Unhandled lectures`

## Routing Rules

- Put conceptual, statistical, mathematical, interpretive, and model-building material in the main DA textbook.
- Put package-specific commands, runnable code, software-output workflows, labs, and implementation recipes in the Coding and Software Cookbook.
- For mixed material, split it: keep the concept in the main textbook and move code/software mechanics to the Cookbook.
- Tie new material to Math Foundations only where it genuinely improves understanding; use the completed Math Foundations chapter structure, not old page numbers.

## Earlier-Chapter Change Control

Prefer adding new chapters or forward sections rather than rewriting earlier chapters.

Earlier-chapter edits require explicit approval unless they are one of:
- a mathematical correction,
- a notation-consistency fix,
- a broken-reference/build fix,
- a short prerequisite bridge needed for the new material.

Any earlier-chapter edit should be recorded with:
- file changed,
- reason,
- whether user approval was required,
- whether the change affects existing page flow or references.

## New-Material Workflow

1. Inspect new lecture files and summarize their academic topics.
2. Propose a logical main-text chapter/section placement.
3. Identify cookbook-only material.
4. Identify mixed material that should be split.
5. Identify Math Foundations connections.
6. Ask for approval before editing earlier chapters.
7. Integrate approved LaTeX changes.
8. Rebuild the full DA textbook and Cookbook.
9. Verify references, bookmarks, page counts, and obvious formatting issues.
10. Commit the approved update.

## Handoff Rule

For Pro/editorial review, provide only the current full DA PDF/source, Cookbook PDF/source, relevant new lecture files, Math Foundations PDF or connection map as needed, `CURRENT_STATUS.md`, and this protocol. Do not include the inactive Core Reader unless specifically requested.
