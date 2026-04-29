# Pro Audit Prompt: Plan B PDF-Only Review

Use this prompt with ChatGPT Pro/editorial review. Attach PDFs only; do not attach LaTeX source files.

## Attachments to provide

Attach:
- `Data_Analysis_Textbook_Combined_v3.pdf`
- `Coding_and_Software_Cookbook_v3.pdf`
- PDF export of `Bassett OA3103 Lecture - Boolean and Categorical Predictors`
- PDF export of `OA3103 Lecture 12 - Residual Diagnostics`
- PDF export of `OA3103 Lecture 13 - Leverage and Interaction of Predictors`
- `CURRENT_STATUS.md`
- `DA_EXPANSION_PROTOCOL.md`

Do not attach:
- LaTeX source files
- Core Reader files
- Math Foundations source files

## Prompt

You are auditing a post-v3 Data Analysis textbook expansion using PDFs only.

Project context:
- The full Data Analysis reference textbook and the Coding and Software Cookbook are active.
- The Core Reader is inactive; do not evaluate it and do not recommend updates to it.
- Math Foundations is a stable reference only; do not recommend editing it.
- Chapters 7 and 8 were intentionally left unchanged.
- Plan B integration was approved after cleaning three lecture decks:
  1. Boolean and categorical predictors
  2. Residual diagnostics
  3. Leverage and interaction of predictors
- The integration added a compact Notation Guide update, a short Chapter 9 bridge, larger Chapter 10-12 updates, and Cookbook support recipes.
- No Chapter 13 was created.

Audit goal:
Evaluate whether the current PDFs correctly and clearly integrate the mathematical, statistical, and pedagogical content from the three lecture decks.

Primary questions:
1. Does the full textbook cover all academically important material from the three lectures?
2. Is the material mathematically and statistically correct?
3. Is the pedagogy clear for students encountering these topics in sequence?
4. Is material routed correctly between the main textbook and the Cookbook?
5. Are there any conceptual gaps, misleading statements, unnecessary duplications, or places where a small clarification would materially improve the text?

Scope:
- Review the full textbook PDF, especially:
  - Notation Guide
  - Chapter 9 bridge
  - Chapter 10 leverage/residual/studentization bridge
  - Chapter 11 categorical predictors, transformations, and interactions
  - Chapter 12 residual diagnostics, leverage/influence, and model repair
- Review the Cookbook PDF, especially:
  - Chapter 11 support recipes
  - Chapter 12 support recipes
- Compare these sections against the three lecture PDFs.
- Do not request source files.
- Do not evaluate LaTeX implementation details unless a problem is visible in the PDFs.

Main-text correctness checks:
- `X` remains the ordinary design matrix and `Z` is used only for engineered/transformed designs.
- Indicator/dummy variables are explained as design-matrix columns.
- For a categorical predictor with `k` levels and an intercept, the text uses `k - 1` indicator columns.
- The dummy-variable trap is explained as rank deficiency/non-identifiability.
- Reference categories and contrasts are explained correctly.
- Mixed numeric/categorical predictors are interpreted correctly.
- Interactions are framed as effect modification, not merely predictor correlation.
- Numeric-by-numeric and numeric-by-categorical interactions are interpreted correctly.
- Interaction hierarchy is explained clearly.
- Residuals versus fitted values, residuals versus predictors, Q-Q plots, and scale-location plots are explained correctly.
- Breusch-Pagan is treated as supporting evidence, not as a standalone decision rule.
- Leverage, average leverage, 2x/3x leverage heuristics, and Cook's distance are described correctly.
- Influential observations are not treated as automatically bad.
- Data-entry error, valid extreme observation, and wrong-model cases are distinguished.
- Model repair language connects to transformations, categorical predictors, and interactions without overpromising.

Cookbook checks:
- The Cookbook supports the main text without replacing conceptual explanation.
- Package-specific mechanics are in the Cookbook rather than the main textbook.
- R and Python recipes shown in the PDF are conceptually correct and pedagogically useful.
- The recipes do not encourage the dummy-variable trap.
- Residual diagnostic plotting, Breusch-Pagan, leverage, Cook's distance, and interaction syntax align with the main text.
- No workflow advice introduces train/test leakage or misleading model-selection practice.

Pedagogy checks:
- The sequence from design matrices to transformed columns, categorical indicators, interactions, diagnostics, and repair is coherent.
- The material from the three lecture decks is covered without forcing students through unnecessary length.
- The IQ/NPS and related curriculum examples are clear enough to support categorical-predictor interpretation.
- The diagnostics hierarchy is understandable:
  - validation/test error for prediction,
  - residual plots for structure,
  - predictor-specific residual plots for locating problems,
  - formal tests as supporting evidence,
  - inference tests only after assumptions are plausible enough.

Output format:
1. Verdict:
   - accept as integrated,
   - accept with minor targeted fixes,
   - reject pending fixes.
2. Coverage map:
   - lecture topic,
   - where it appears in the full textbook,
   - where it appears in the Cookbook,
   - missing or weak coverage if any.
3. Findings table with columns:
   - PDF/product,
   - page or chapter/section,
   - issue,
   - why it matters,
   - smallest recommended fix,
   - severity: blocking / minor / optional.
4. Separate findings into:
   - mathematical/statistical correctness,
   - pedagogical clarity and sequencing,
   - lecture coverage,
   - Cookbook routing/support,
   - visible PDF/layout issues.
5. If no major blockers are found, say explicitly:
   "No major mathematical/statistical blocker was found."

Keep recommendations targeted. Do not propose a broad rewrite, a new Chapter 13, Core Reader work, or Math Foundations edits unless the PDFs reveal a genuine blocker.
