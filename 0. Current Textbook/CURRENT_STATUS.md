# Current Textbook Status

This folder contains the live Data Analysis textbook source files and current PDFs.

Current working products in this folder:
- `Data_Analysis_Textbook_Combined_v3.pdf`: full Data Analysis reference textbook, visibly titled `Main Reference Textbook v4`.
- `Coding_and_Software_Cookbook_v3.pdf`: standalone coding/software companion.  A v4 Cookbook release is deferred.
- `Data_Analysis_Textbook_Core_Reader_v1.pdf`: inactive preserved compressed student reader; do not update unless explicitly reactivated.

Current v4 release status:
- The full reference textbook is current at 227 pages.
- The live full-reference wrapper is still named `Data_Analysis_Textbook_Combined_v3.tex` to preserve the existing source naming convention, but the rendered title page now says `Main Reference Textbook v4`.
- The full reference includes Chapters 1--17 plus Appendix A, `Regression Assumption Ladder`, and Appendix B, `Math Foundations Source Map`.
- Final Codex source/build audit found no mathematical/statistical blockers, no undefined references, no duplicate labels/destinations, no overfull boxes, and no hyperref/bookmark warnings.
- Known nonblocking LaTeX noise: 18 underfull boxes, including 9 severe underfull boxes, from narrow table/list rows.  These are not currently release blockers.
- Pro's PDF-first audit found no major mathematical/statistical blockers and recommended only targeted cleanup; the version-label and Chapter 16 notation cleanups have been applied.
- Chapter 16 now distinguishes the model-level centered random response `\mathbf{Y}_c` from the observed centered response `\mathbf{y}_c` in the ridge truth-plus-error note, and clarifies that PCA eigenvalues `\lambda_k` are not the ridge/LASSO penalty parameter `\lambda`.

Release folder:
- Current release copy: `Peer Review Release Products\Data_Analysis_Textbook_v4.pdf`.
- Previous v3 release products were moved to `Archive\Peer_Review_Release_Products_v3_2026-04-28\` to avoid mixing old and current release PDFs.
- `Coding_and_Software_Cookbook_v4.pdf` is intentionally not released yet.
- The Core Reader remains inactive and is not part of the v4 release package.
- Math Foundations remains a stable reference product and was not edited for v4.

Live source locations:
- `Sources\`: shared chapter and appendix source files.
- `Data_Analysis_Textbook_Combined_v3.tex`: full reference wrapper.
- `Coding_and_Software_Cookbook_v3.tex`: Cookbook wrapper.
- `Data_Analysis_Textbook_Core_Reader_v1.tex`: inactive Core Reader wrapper, preserved for historical/reference use.

Future Data Analysis expansion work should target the full reference textbook and, when reactivated for release, the coding/software companion.  The Core Reader should not be included in routine builds, Pro handoffs, or new-material integration unless it is explicitly reactivated.

No active Pro handoff folder is maintained here.  Recreate a handoff folder only when a new Pro review pass is needed.
