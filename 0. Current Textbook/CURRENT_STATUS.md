# Current Textbook Status

This folder contains the live Data Analysis textbook source files and current PDFs.

Current working products in this folder:
- `Data_Analysis_Textbook_Combined_v3.pdf`: full Data Analysis reference textbook.
- `Data_Analysis_Textbook_Core_Reader_v1.pdf`: inactive preserved compressed student reader; do not update unless explicitly reactivated.
- `Coding_and_Software_Cookbook_v3.pdf`: standalone coding/software companion.

Current post-v3 integration status:
- Plan B expansion for the cleaned categorical-predictor, residual-diagnostics, leverage/influence, and interaction lectures has been integrated and committed in `fd1b399`.
- Pro's targeted PDF-only audit fixes were applied and committed in `964cc12`; the current PDFs include those fixes.
- The full reference PDF is current at 171 pages.
- The Cookbook PDF is current at 37 pages.
- Integrated source areas: Notation Guide, a short Chapter 9 bridge, Chapter 10 residual/leverage theory bridge, Chapter 11 categorical predictors/interactions expansion, Chapter 12 diagnostics/model repair expansion, and the Cookbook recipes supporting Chapters 11 and 12.
- Cookbook code fixes after audit: statsmodels formula strings use ASCII quote-safe Python strings, manual pandas dummy creation pins `Other` as the reference category and uses `dtype=float`, and the examples were smoke-tested.
- Main-text targeted fixes after audit: Chapter 12 clarifies that \(p+1\) is the number of fitted coefficients/design columns for average leverage, and Chapter 11's Math Foundations connection now includes Chapter 11 for null-space support.

Distributed release copies are in `Peer Review Release Products\`:
- `Data_Analysis_Textbook_v3.pdf`
- `Data_Analysis_Textbook_Core_Reader_v1.pdf`
- `Coding_and_Software_Cookbook_v3.pdf`
- `Math_Foundations_Textbook.pdf`

Live source locations:
- `Sources\`: shared chapter and cookbook source files.
- `Data_Analysis_Textbook_Combined_v3.tex`: full reference wrapper.
- `Data_Analysis_Textbook_Core_Reader_v1.tex`: inactive Core Reader wrapper, preserved for historical/reference use.
- `Coding_and_Software_Cookbook_v3.tex`: cookbook wrapper.

Future Data Analysis expansion work should target the full reference textbook and the coding/software companion. The Core Reader should not be included in routine builds, Pro handoffs, or new-material integration unless it is explicitly reactivated.

No active Pro handoff folder is maintained here. Recreate a handoff folder only when a new Pro review pass is needed. For the next Plan B audit, prefer a PDF-only Pro review using `Pro_Audit_Prompt_PlanB_PDF_Only_2026-04-29.md`; do not include LaTeX source files unless the user specifically requests a source-level audit.
