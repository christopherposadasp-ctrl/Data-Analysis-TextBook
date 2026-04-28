from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(r"C:\Users\posad\OneDrive\Desktop\DataAnalysis\Lectures")
REWRITE = ROOT / "Math Foundations Rewrite"
SOURCES = ROOT / "0. Current Textbook" / "Sources"
METADATA = REWRITE / "metadata"


CHAPTER_TITLES = {
    "01": "Logic and Deductive Reasoning",
    "02": "Vectors in R^n",
    "03": "Vector Operations and Linear Combinations",
    "04": "Sets, Set Operations, and Quantifiers",
    "05": "Dot Products, Norms, Distance, Angles, and Orthogonality",
    "06": "Linear Independence, Span, Bases, and Dimension",
    "07": "Matrices and Matrix-Vector Multiplication",
    "08": "Linear Systems, Polynomial Systems, and Vandermonde Matrices",
    "09": "Orthogonal Bases, Gram-Schmidt, and QR",
    "10": "Matrix Inverses, Rank, and Pseudoinverses",
    "11": "Subspaces: Column Space, Row Space, and Null Space",
    "12": "Multivariable Functions, Gradients, and Least Squares",
    "13": "Hessians, Quadratic Forms, and Second-Order Conditions",
    "A": "Data Analysis Bridge Index",
}


LABEL_ROWS = [
    ("mf:logic-statements", "Ch01", "Mathematical statements and truth values", "pp. 1--3", "Supports assumptions, hypotheses, and defensible conclusions."),
    ("mf:logic-negation", "Ch01", "Negation and alternatives", "pp. 1--5", "Supports null/alternative hypotheses and quantified cleaning rules."),
    ("mf:logic-implication", "Ch01", "Implication, biconditional reasoning, and De Morgan rules", "pp. 1--5", "Supports reasoning from assumptions to conclusions."),
    ("mf:vectors-rn", "Ch02", "Vectors in R^n", "pp. 6--7", "Core vector notation dependency."),
    ("mf:vectors-as-data", "Ch02", "Vectors as structured collections of quantities", "pp. 6--7", "Bridge from vectors to data columns, observations, and feature vectors."),
    ("mf:vector-entries-subvectors", "Ch02", "Entries, coordinates, and subvectors", "pp. 6--8", "Supports row/column selection and vector coordinates."),
    ("mf:ones-vector", "Ch02", "Special vectors, including the ones vector", "pp. 6--7", "Supports mean-only vectors and intercept columns."),
    ("mf:probability-vectors", "Ch02", "Probability vectors as weighted collections", "p. 7", "Supports expectation as weighted average / inner product."),
    ("mf:vector-arithmetic", "Ch03", "Vector addition, subtraction, and centering", "pp. 8--10", "Supports residuals and centered variables."),
    ("mf:scalar-multiplication", "Ch03", "Scalar multiplication", "pp. 8--10", "Supports weighted predictors and scaled vectors."),
    ("mf:linear-combinations", "Ch03", "Linear combinations", "pp. 9--10", "Supports fitted values, columns, and parameterized models."),
    ("mf:centered-vectors", "Ch03", "Centered vectors and deviations", "pp. 8--10", "Supports spread, covariance, correlation, and sums of squares."),
    ("mf:set-membership", "Ch04", "Set membership and common number systems", "pp. 11--15", "Supports variable domains and valid values."),
    ("mf:set-operations", "Ch04", "Set operations, complements, and differences", "pp. 11--15", "Supports filtering, row selection, and cleaning rules."),
    ("mf:subsets", "Ch04", "Subsets and families of sets", "pp. 11--15", "Supports selected rows/columns and data-cleaning subsets."),
    ("mf:quantifiers", "Ch04", "Universal and existential quantifiers", "pp. 11--15", "Supports precise cleaning predicates and assumptions."),
    ("mf:quantifier-negation", "Ch04", "Negating quantified statements", "pp. 11--15", "Supports defensive data-cleaning logic."),
    ("mf:dot-product", "Ch05", "Dot products", "p. 16", "Supports weighted sums, inner products, covariance, and normal equations."),
    ("mf:inner-product-weighted-sums", "Ch05", "Inner products as weighted sums", "p. 16", "Supports expectation, means, and linear predictors."),
    ("mf:norms-euclidean", "Ch05", "Euclidean norm and squared length", "pp. 16--18", "Supports RSS, TSS, MSE, RMSE, and least-squares geometry."),
    ("mf:vector-distance", "Ch05", "Distance between vectors", "pp. 17--18", "Supports residual length and prediction error."),
    ("mf:angles", "Ch05", "Angles between vectors", "p. 18", "Supports correlation as geometric alignment."),
    ("mf:orthogonality", "Ch05", "Orthogonality and zero dot products", "p. 18", "Supports residual orthogonality and projection geometry."),
    ("mf:linear-independence", "Ch06", "Linear independence", "pp. 20--21", "Supports rank, degrees of freedom, and identifiability."),
    ("mf:span", "Ch06", "Span", "pp. 20--22", "Supports column-space and fitted-value interpretations."),
    ("mf:bases", "Ch06", "Bases and coordinates", "pp. 20--22", "Supports dimension and unique linear-combination representations."),
    ("mf:dimension", "Ch06", "Dimension and maximum independent sets", "pp. 20--21", "Supports degrees of freedom."),
    ("mf:matrices-dimensions", "Ch07", "Matrix notation and dimensions", "pp. 23--24", "Supports design matrices and data tables."),
    ("mf:transpose", "Ch07", "Transpose notation", "pp. 23--25", "Supports X^T e and normal-equation notation."),
    ("mf:identity-matrix", "Ch07", "Identity matrices and symmetry", "pp. 23--24", "Supports hat matrices and matrix algebra."),
    ("mf:matrix-vector-row-view", "Ch07", "Matrix-vector multiplication as row inner products", "p. 25", "Supports X beta as fitted values."),
    ("mf:matrix-vector-column-view", "Ch07", "Matrix-vector multiplication as a linear combination of columns", "pp. 25--26", "Supports fitted values as column-space combinations."),
    ("mf:submatrix-extraction", "Ch07", "Submatrices and slicing notation", "pp. 23--24", "Supports filtering rows and selecting columns."),
    ("mf:computational-matrix-operations", "Ch07", "Computational matrix operations and array shapes", "pp. 37--38", "Supports Python/NumPy matrix-operation bridges."),
    ("mf:linear-systems", "Ch08", "Linear systems", "pp. 28--31", "Supports transformed systems and coefficient solving."),
    ("mf:vandermonde-matrices", "Ch08", "Polynomial systems and Vandermonde matrices", "p. 31", "Supports polynomial design matrices."),
    ("mf:orthogonal-bases", "Ch09", "Orthogonal and orthonormal bases", "pp. 34--36", "Supports orthogonal-polynomial intuition."),
    ("mf:gram-schmidt", "Ch09", "Gram-Schmidt orthogonalization", "pp. 34--36", "Supports orthogonal basis construction."),
    ("mf:qr-factorization", "Ch09", "QR factorization", "pp. 34--36", "Supports stable least-squares background if retained chronologically."),
    ("mf:orthogonal-polynomials", "Ch09", "Orthogonal polynomial intuition", "pp. 34--36", "Supports transformed-regression interpretation."),
    ("mf:matrix-inverse", "Ch10", "Matrix inverses", "pp. 59--62", "Supports inverse and left-inverse intuition."),
    ("mf:left-inverse", "Ch10", "Left inverses", "pp. 59--62", "Supports identifiability and full column rank."),
    ("mf:rank", "Ch10", "Rank", "pp. 59--62, 67--69", "Supports full-rank conditions."),
    ("mf:full-column-rank", "Ch10", "Full column rank", "pp. 59--62, 67--69", "Supports unique regression coefficients."),
    ("mf:ata-invertibility", "Ch10", "Invertibility of A^T A under full column rank", "p. 122", "Supports normal-equation coefficient uniqueness."),
    ("mf:column-space", "Ch11", "Column space", "pp. 67--69", "Supports fitted-value spaces and projections."),
    ("mf:row-space", "Ch11", "Row space", "pp. 67--69", "Part of the subspace framework."),
    ("mf:null-space", "Ch11", "Null space", "pp. 67--69", "Supports identifiability and non-identifiability."),
    ("mf:subspaces", "Ch11", "Column, row, and null subspaces", "pp. 67--69", "Supports Big Four subspace language."),
    ("mf:multivariable-functions", "Ch12", "Multivariable functions", "pp. 104--105", "Supports optimization setup."),
    ("mf:gradient", "Ch12", "Gradients", "pp. 104--105", "Supports normal-equation derivations."),
    ("mf:stationary-points", "Ch12", "Stationary points", "pp. 104--105", "Supports least-squares minimization."),
    ("mf:least-squares-objective", "Ch12", "Least-squares objective", "pp. 104--105", "Supports regression loss minimization."),
    ("mf:least-squares-normal-equations", "Ch12", "Normal equations", "pp. 104--105, 120--122", "Supports X^T X beta = X^T y."),
    ("mf:least-squares-residual-orthogonality", "Ch12", "Residual orthogonality in least squares", "pp. 104--105", "Supports X^T e = 0."),
    ("mf:least-squares-projection-bridge", "Ch12", "Least squares as an orthogonal-projection bridge", "pp. 104--105", "Short bridge label for Data Analysis projection language; do not expand into a long new chapter."),
    ("mf:hessian", "Ch13", "Hessians", "pp. 120--122", "Supports second-order least-squares arguments."),
    ("mf:quadratic-forms", "Ch13", "Quadratic forms", "pp. 120--122", "Supports A^T A arguments."),
    ("mf:positive-semidefinite", "Ch13", "Positive semidefinite matrices", "pp. 120--122", "Supports convexity and uniqueness checks."),
    ("mf:second-order-conditions", "Ch13", "Second-order conditions", "pp. 120--122", "Supports classifying stationary points."),
    ("mf:data-analysis-bridge-index", "Appendix A", "Data Analysis Bridge Index", "Derived from MF_Connections_Map.md", "Index layer that points Data Analysis dependencies back to chronological sections."),
]
LABEL_MAP = {row[0]: row for row in LABEL_ROWS}


def clean_latex(text: str) -> str:
    text = re.sub(r"\\chapter(?:\[[^\]]*\])?\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:emph|textbf|section|subsection\*?|paragraph)\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:CoreCompress|FullOnly|CoreOnly)\{", "", text)
    text = text.replace("~", " ").replace(r"\%", "%").replace(r"\\", "")
    return re.sub(r"\s+", " ", text).strip()


def md_cell(text: str) -> str:
    return clean_latex(text).replace("|", "&#124;")


def add(labels: list[str], label: str) -> None:
    if label not in labels:
        labels.append(label)


def assign_labels(context: str, pages: str) -> list[str]:
    t = f"{context} {pages}".lower()
    labels: list[str] = []

    if re.search(r"logic|truth|hypothes|assumption|conclusion|negation|null-versus-alternative|alternative", t):
        add(labels, "mf:logic-statements")
        add(labels, "mf:logic-negation")
    if re.search(r"implication|biconditional|de morgan", t):
        add(labels, "mf:logic-implication")
    if re.search(r"quantif|predicate", t):
        add(labels, "mf:quantifiers")
        add(labels, "mf:quantifier-negation")
    if re.search(r"set membership|set difference|set operation|subset|complement|number systems|domain|row set|column set|subsetting", t):
        add(labels, "mf:set-membership")
        add(labels, "mf:set-operations")
        add(labels, "mf:subsets")
    if "probability vector" in t:
        add(labels, "mf:probability-vectors")
    if re.search(r"vector notation|mathbb|vector in|vectors in|response vector|predictor vector|residual vector|feature vector|data vector|variable column|observation-space|mean-only fitted vector|numeric variable|data rows|entries|coordinates|subvectors|ones vector", t):
        add(labels, "mf:vectors-rn")
    if re.search(r"data|feature|observation|variable|response|predictor|residual|numeric variable|data table|data columns", t):
        add(labels, "mf:vectors-as-data")
    if re.search(r"entries|coordinates|subvectors|subvector|slice", t):
        add(labels, "mf:vector-entries-subvectors")
    if re.search(r"ones vector|mathbf\{1\}|mean-only|intercept", t):
        add(labels, "mf:ones-vector")
    if re.search(r"subtraction|centered|centering|deviations|residual vector|vector subtraction", t):
        add(labels, "mf:vector-arithmetic")
    if "centered" in t:
        add(labels, "mf:centered-vectors")
    if "scalar" in t:
        add(labels, "mf:scalar-multiplication")
    if re.search(r"linear combination|weighted|finite-parameter|fitted values|candidate directions|span/column-space", t):
        add(labels, "mf:linear-combinations")
    if re.search(r"dot product|inner product|weighted sum|sample mean|sum_i|sum a_i|expectation|1\}\^t", t):
        add(labels, "mf:dot-product")
        add(labels, "mf:inner-product-weighted-sums")
    if re.search(r"norm|squared length|distance|mse|rmse|rss|tss|least squares objective|sums of squared|prediction error", t):
        add(labels, "mf:norms-euclidean")
    if re.search(r"distance|mse|rmse|prediction error|outlier", t):
        add(labels, "mf:vector-distance")
    if re.search(r"angle|alignment|correlation", t):
        add(labels, "mf:angles")
    if re.search(r"orthogonal|orthogonality|zero-dot-product|residual-space", t):
        add(labels, "mf:orthogonality")
    if re.search(r"projection|project|hat-matrix|column-space interpretation|fitted-value spaces|least-squares normal-equation bridge|normal equations and orthogonality|residual orthogonality|sum-of-squares decomposition", t):
        add(labels, "mf:least-squares-projection-bridge")
    if re.search(r"linear independence|independent|linearly independent", t):
        add(labels, "mf:linear-independence")
    if "span" in t:
        add(labels, "mf:span")
    if re.search(r"basis|bases|unique linear-combination|coordinates", t):
        add(labels, "mf:bases")
    if re.search(r"degrees of freedom|leftover|dimension claim|basis size|maximum size|leftover dimension", t):
        add(labels, "mf:dimension")
    if re.search(r"matrix notation|matrix size|matrix dimensions|matrix-vector|design matrix|data table|matrix expressions|tall|wide|sparse|symmetry|submatrix|transpose|identity|hat-matrix", t):
        add(labels, "mf:matrices-dimensions")
    if "transpose" in t:
        add(labels, "mf:transpose")
    if re.search(r"identity|symmetry|hat-matrix", t):
        add(labels, "mf:identity-matrix")
    if "row inner product" in t:
        add(labels, "mf:matrix-vector-row-view")
    if re.search(r"column linear combination|linear combination of columns|column-space combinations|fitted values as", t):
        add(labels, "mf:matrix-vector-column-view")
    if "matrix-vector multiplication" in t:
        add(labels, "mf:matrix-vector-row-view")
        add(labels, "mf:matrix-vector-column-view")
    if re.search(r"submatrix|slice|selecting columns|filtering rows", t):
        add(labels, "mf:submatrix-extraction")
    if re.search(r"python|numpy|computational|arrays|shapes|@", t):
        add(labels, "mf:computational-matrix-operations")
    if re.search(r"linear systems|solving transformed systems|solving", t):
        add(labels, "mf:linear-systems")
    if re.search(r"vandermonde|polynomial", t):
        add(labels, "mf:vandermonde-matrices")
    if re.search(r"inverse|invertibility", t):
        add(labels, "mf:matrix-inverse")
    if "left inverse" in t or "left-inverse" in t:
        add(labels, "mf:left-inverse")
    if re.search(r"rank|full-rank|full column", t):
        add(labels, "mf:rank")
        add(labels, "mf:full-column-rank")
    if re.search(r"positive-semidefinite|full column rank and invertibility|equivalence between full column rank and invertibility|invertibility of .*a\^t.*a", t):
        add(labels, "mf:ata-invertibility")
    if "column space" in t or "column-space" in t:
        add(labels, "mf:column-space")
    if "row space" in t:
        add(labels, "mf:row-space")
    if "null space" in t or "null-space" in t or "non-identifiability" in t or "identifiability" in t or "unique coefficients" in t:
        add(labels, "mf:null-space")
    if "subspace" in t or "big four" in t:
        add(labels, "mf:subspaces")
    if re.search(r"orthonormal|orthogonal basis|orthogonal-basis", t):
        add(labels, "mf:orthogonal-bases")
    if "gram-schmidt" in t:
        add(labels, "mf:gram-schmidt")
    if re.search(r"\bqr\b", t):
        add(labels, "mf:qr-factorization")
    if "orthogonal polynomial" in t:
        add(labels, "mf:orthogonal-polynomials")
    if "multivariable" in t:
        add(labels, "mf:multivariable-functions")
    if "gradient" in t:
        add(labels, "mf:gradient")
    if "stationary" in t:
        add(labels, "mf:stationary-points")
    if re.search(r"least squares|least-squares|minimizing", t):
        add(labels, "mf:least-squares-objective")
    if "normal equation" in t:
        add(labels, "mf:least-squares-normal-equations")
    if re.search(r"x\^t e|residual orthogonality|least-squares residual", t):
        add(labels, "mf:least-squares-residual-orthogonality")
    if "hessian" in t:
        add(labels, "mf:hessian")
    if "quadratic" in t:
        add(labels, "mf:quadratic-forms")
    if "positive-semidefinite" in t or "semidefinite" in t:
        add(labels, "mf:positive-semidefinite")
    if "second-order" in t:
        add(labels, "mf:second-order-conditions")

    # Page-based fallback for sparse rows.
    if not labels:
        if re.search(r"1--5|1--3", pages):
            add(labels, "mf:logic-statements")
        if re.search(r"6--7|6--8|p\. 7", pages):
            add(labels, "mf:vectors-rn")
        if re.search(r"8--10|9--10", pages):
            add(labels, "mf:linear-combinations")
        if "11--15" in pages:
            add(labels, "mf:set-operations")
        if re.search(r"p\. 16|16--17|16--18", pages):
            add(labels, "mf:dot-product")
        if re.search(r"17--18|16--18", pages):
            add(labels, "mf:norms-euclidean")
            add(labels, "mf:orthogonality")
        if re.search(r"20--21|20--22", pages):
            add(labels, "mf:linear-independence")
            add(labels, "mf:bases")
            add(labels, "mf:dimension")
        if re.search(r"23--24|23--25|23--26|25--26", pages):
            add(labels, "mf:matrices-dimensions")
            add(labels, "mf:matrix-vector-column-view")
        if "28--31" in pages:
            add(labels, "mf:linear-systems")
        if "34--36" in pages:
            add(labels, "mf:gram-schmidt")
        if "37--38" in pages:
            add(labels, "mf:computational-matrix-operations")
        if re.search(r"59--62|59--60|67--69", pages):
            add(labels, "mf:rank")
            add(labels, "mf:full-column-rank")
        if re.search(r"104--105|120--122", pages):
            add(labels, "mf:least-squares-normal-equations")

    add(labels, "mf:data-analysis-bridge-index")
    return labels


def format_target(labels: list[str]) -> str:
    grouped: dict[str, list[str]] = defaultdict(list)
    for label in labels:
        row = LABEL_MAP.get(label)
        if row and label not in grouped[row[1]]:
            grouped[row[1]].append(label)
    order = [f"Ch{i:02d}" for i in range(1, 14)] + ["Appendix A"]
    parts = []
    for chapter in order:
        if chapter not in grouped:
            continue
        title = CHAPTER_TITLES["A"] if chapter == "Appendix A" else CHAPTER_TITLES[chapter[2:]]
        labels_text = ", ".join(f"`{label}`" for label in grouped[chapter])
        parts.append(f"{chapter} {title}: {labels_text}")
    return "; ".join(parts)


def get_chapter_title(lines: list[str], fallback: str) -> str:
    for line in lines:
        match = re.search(r"\\chapter(?:\[[^\]]*\])?\{(.+)\}", line)
        if match:
            return clean_latex(match.group(1))
    return fallback


def current_section(lines: list[str], index: int) -> str:
    for i in range(index, -1, -1):
        match = re.search(r"^\\(?:section|subsection\*?)\{(.+)\}", lines[i])
        if match:
            return clean_latex(match.group(1))
    return ""


def extract_rows() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    source_rows = []
    callout_rows = []
    for file in sorted(SOURCES.glob("Ch*.tex")):
        lines = file.read_text(encoding="utf-8", errors="ignore").splitlines()
        ch_match = re.match(r"Ch(\d+)", file.name)
        chapter = int(ch_match.group(1)) if ch_match else 0
        chapter_title = get_chapter_title(lines, file.stem)

        for i, line in enumerate(lines):
            if re.search(r"\\textbf\{Chapter\s+\d+\s+use\}", line):
                j = i + 1
                while j < len(lines) and not re.search(r"\\end\{tabular\}", lines[j]):
                    row_line = lines[j].strip()
                    if " & " in row_line and row_line.endswith(r"\\") and r"\textbf" not in row_line:
                        parts = re.sub(r"\\\\$", "", row_line).split("&", 2)
                        if len(parts) == 3:
                            use = clean_latex(parts[0])
                            support = clean_latex(parts[1])
                            pages = clean_latex(parts[2])
                            labels = assign_labels(f"{use} {support}", pages)
                            source_rows.append({
                                "SourceType": "Source Map",
                                "DataAnalysisChapter": str(chapter),
                                "DataAnalysisContext": chapter_title,
                                "DataAnalysisUse": use,
                                "MathFoundationsSupport": support,
                                "CurrentNotesPages": pages,
                                "SourceFile": file.name,
                                "SourceLine": str(j + 1),
                                "FutureMFLabels": "; ".join(labels),
                                "FutureMFTarget": format_target(labels),
                            })
                    j += 1

            if r"\paragraph{Math Foundations Connection.}" in line:
                text_lines = []
                j = i + 1
                while j < len(lines):
                    stripped = lines[j].strip()
                    if not stripped or stripped == "}{" or re.match(r"^\\(?:section|subsection|paragraph)", stripped):
                        break
                    text_lines.append(stripped)
                    j += 1
                text = clean_latex(" ".join(text_lines))
                page_matches = re.findall(r"p{1,2}\.?~?\s*\d+(?:--\d+)?(?:\s*(?:,|and|plus)\s*p{0,2}\.?~?\s*\d+(?:--\d+)?)*", " ".join(text_lines))
                pages = "; ".join(clean_latex(item) for item in page_matches)
                labels = assign_labels(text, pages)
                section = current_section(lines, i)
                callout_rows.append({
                    "SourceType": "Integrated Callout",
                    "DataAnalysisChapter": str(chapter),
                    "DataAnalysisContext": section,
                    "DataAnalysisUse": section,
                    "MathFoundationsSupport": text,
                    "CurrentNotesPages": pages,
                    "SourceFile": file.name,
                    "SourceLine": str(i + 1),
                    "FutureMFLabels": "; ".join(labels),
                    "FutureMFTarget": format_target(labels),
                })
    return source_rows, callout_rows


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_outputs() -> None:
    METADATA.mkdir(parents=True, exist_ok=True)
    source_rows, callout_rows = extract_rows()
    all_rows = source_rows + callout_rows

    md = [
        "# Math Foundations Connections Map",
        "",
        "Generated from the canonical Data Analysis textbook sources in `0. Current Textbook/Sources` on 2026-04-25. Future Math Foundations targets were filled from the chronological rewrite plan v2 on 2026-04-25.",
        "",
        "Purpose: preserve every current dependency from the Data Analysis textbook back to `MathFoundationsNotes.pdf` before rewriting Math Foundations as its own textbook. The future rewrite should keep these concepts addressable by stable section labels so the Data Analysis textbook can later point to the new Math Foundations textbook without losing any existing connection.",
        "",
        "## Summary",
        "",
        f"- Source-map entries extracted: {len(source_rows)}",
        f"- Integrated connection callouts extracted: {len(callout_rows)}",
        "- Current source of truth: `0. Current Textbook/Sources/Ch01_..._v3.tex` through `Ch12_..._v3.tex`",
        "- Current Math Foundations source: `MathFoundationsNotes.pdf` at the Lectures project root",
        "- Rewrite policy: keep the Math Foundations textbook chronological, not reorganized around Data Analysis dependencies.",
        "- Body length target: 128--133 pages; practical body cap about 135 pages; front/back total cap about 141 pages.",
        "- Label convention: keep singular `mf:set-*` labels (`mf:set-membership`, `mf:set-operations`) rather than switching to `mf:sets-*`.",
        "",
        "## Rewrite Protection Rules",
        "",
        "1. Do not remove a Math Foundations concept from the future rewrite if it supports a Data Analysis chapter below.",
        "2. Give each rewritten Math Foundations section a stable label, such as `mf:vectors-rn` or `mf:least-squares-normal-equations`.",
        "3. Keep the main Math Foundations textbook chronological. Use Appendix A as the Data Analysis bridge index rather than reorganizing the main book around Data Analysis.",
        "4. After the Math Foundations rewrite exists, replace page-only references in the Data Analysis textbook with section labels plus page references where useful.",
        "",
        "## Chronological Math Foundations Structure",
        "",
    ]
    for key, title in CHAPTER_TITLES.items():
        md.append(f"- Appendix A. {title}" if key == "A" else f"- Chapter {int(key)}. {title}")

    md += [
        "",
        "## Consolidated Source Map",
        "",
        "| DA Ch. | Data Analysis chapter | Data Analysis use | Math Foundations support | Current notes pages | Source | Future MF textbook target |",
        "|---:|---|---|---|---|---|---|",
    ]
    for row in source_rows:
        source = f"`{row['SourceFile']}:{row['SourceLine']}`"
        md.append(
            f"| {row['DataAnalysisChapter']} | {md_cell(row['DataAnalysisContext'])} | {md_cell(row['DataAnalysisUse'])} | "
            f"{md_cell(row['MathFoundationsSupport'])} | {md_cell(row['CurrentNotesPages'])} | {source} | {md_cell(row['FutureMFTarget'])} |"
        )

    md += [
        "",
        "## Integrated Connection Callouts",
        "",
        "These are the in-chapter reader-facing callouts, not just the end-of-chapter source-map rows. They should be preserved conceptually when updating Data Analysis references to a future Math Foundations textbook.",
        "",
        "| DA Ch. | Section context | Current notes pages | Source | Current callout text | Future MF textbook target |",
        "|---:|---|---|---|---|---|",
    ]
    for row in callout_rows:
        source = f"`{row['SourceFile']}:{row['SourceLine']}`"
        pages = row["CurrentNotesPages"] or "Not explicit in extracted paragraph"
        md.append(
            f"| {row['DataAnalysisChapter']} | {md_cell(row['DataAnalysisContext'])} | {md_cell(pages)} | {source} | "
            f"{md_cell(row['MathFoundationsSupport'])} | {md_cell(row['FutureMFTarget'])} |"
        )

    md += [
        "",
        "## Page Reference Clusters",
        "",
        "Use these clusters as a rough outline for the chronological Math Foundations rewrite. They show which old notes pages are most important to the Data Analysis textbook and which future labels should preserve them.",
        "",
    ]
    by_page: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in all_rows:
        if row["CurrentNotesPages"]:
            by_page[row["CurrentNotesPages"]].append(row)
    for pages in sorted(by_page):
        contexts = sorted({f"Ch{row['DataAnalysisChapter']}: {row['DataAnalysisUse']}" for row in by_page[pages]})
        labels = sorted({label for row in by_page[pages] for label in row["FutureMFLabels"].split("; ") if label})
        md.append(f"- `{md_cell(pages)}`: {md_cell('; '.join(contexts))}. Future labels: `{('`, `'.join(labels))}`")

    md += [
        "",
        "## Suggested Initial Math Foundations Textbook Sections",
        "",
        "- Logic and mathematical implication: truth tables, implications, biconditionals, De Morgan's laws.",
        "- Vectors in `R^n`: coordinates, entries, subvectors, ones vectors, and feature-vector interpretation.",
        "- Linear combinations and weighted sums: scalar multiplication, dot products, and inner-product models.",
        "- Norms, distances, angles, and orthogonality: geometric language needed for residuals and projections.",
        "- Matrix notation and matrix-vector multiplication: rows as inner products, columns as linear combinations, transformations, and transposes.",
        "- Rank, column space, bases, independence, and invertibility: identifiability and regression geometry.",
        "- Probability and expectation: variance, covariance, correlation, linearity of expectation, and bias.",
        "- Least squares and optimization: stationary points, normal equations, gradient reasoning, and positive-semidefinite `A^T A`.",
        "- Computational linear algebra bridge: array shapes, transposes, multiplication, and numerically stable solver habits.",
    ]
    (REWRITE / "MF_Connections_Map.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    write_csv(
        METADATA / "MF_Label_Registry.csv",
        [
            {
                "Label": label,
                "ProposedChapter": chapter,
                "ProposedChapterTitle": CHAPTER_TITLES["A"] if chapter == "Appendix A" else CHAPTER_TITLES[chapter[2:]],
                "ProposedSectionTitle": section,
                "OldNotesPages": pages,
                "Notes": notes,
            }
            for label, chapter, section, pages, notes in LABEL_ROWS
        ],
        ["Label", "ProposedChapter", "ProposedChapterTitle", "ProposedSectionTitle", "OldNotesPages", "Notes"],
    )

    crosswalk_fields = [
        "SourceType",
        "DataAnalysisChapter",
        "DataAnalysisContext",
        "DataAnalysisUse",
        "MathFoundationsSupport",
        "CurrentNotesPages",
        "FutureMFLabels",
        "FutureMFTarget",
        "SourceFile",
        "SourceLine",
    ]
    write_csv(METADATA / "MF_DA_Crosswalk.csv", all_rows, crosswalk_fields)

    old_page_rows = []
    for pages, rows in sorted(by_page.items()):
        old_page_rows.append({
            "OldNotesPages": pages,
            "FutureMFLabels": "; ".join(sorted({label for row in rows for label in row["FutureMFLabels"].split("; ") if label})),
            "ProposedChapterTargets": " || ".join(sorted({row["FutureMFTarget"] for row in rows})),
            "DataAnalysisUses": " || ".join(sorted({f"Ch{row['DataAnalysisChapter']}: {row['DataAnalysisUse']}" for row in rows})),
        })
    write_csv(
        METADATA / "Old_Page_to_New_Label_Map.csv",
        old_page_rows,
        ["OldNotesPages", "FutureMFLabels", "ProposedChapterTargets", "DataAnalysisUses"],
    )

    name_rows = acknowledgments_rows()
    write_csv(
        METADATA / "Acknowledgments_Name_Audit.csv",
        name_rows,
        ["Name", "Role", "EvidenceSource", "EvidenceSnippet", "AuditStatus", "Notes"],
    )

    plan_lines = [
        "# Math Foundations Textbook Rewrite Plan v2",
        "",
        "## Purpose",
        "",
        "Turn `MathFoundationsNotes.pdf` into a standalone textbook for the next cohort while preserving all Data Analysis textbook dependencies recorded in `MF_Connections_Map.md`.",
        "",
        "## Governing Policy",
        "",
        "- Keep the Math Foundations textbook chronological, following the current notes order.",
        "- Do not reorganize the main textbook around Data Analysis dependencies.",
        "- Use Appendix A as the Data Analysis Bridge Index.",
        "- Preserve every concept listed in `MF_Connections_Map.md`.",
        "- Do not update Data Analysis references until the Math Foundations labels compile in the new book.",
        "",
        "## Length Constraint",
        "",
        "- Current notes length: 123 pages.",
        "- Target main body: 128--133 pages.",
        "- Absolute body cap: about 135 pages.",
        "- Front/back buffer: about 6 pages.",
        "- Practical total cap: about 141 pages.",
        "",
        "## Chronological Chapter Structure",
        "",
    ]
    for key, title in CHAPTER_TITLES.items():
        plan_lines.append(f"- Appendix A. {title}" if key == "A" else f"- Chapter {int(key)}. {title}")
    plan_lines += [
        "",
        "## Required Metadata",
        "",
        "- `metadata/MF_Label_Registry.csv`",
        "- `metadata/MF_DA_Crosswalk.csv`",
        "- `metadata/Old_Page_to_New_Label_Map.csv`",
        "- `metadata/Acknowledgments_Name_Audit.csv`",
        "",
        "## Current Implementation Status",
        "",
        "- Future Math Foundations targets have been filled in `MF_Connections_Map.md`.",
        "- Metadata CSVs have been initialized.",
        "- The middle chapter order has been revised so linear systems and Vandermonde matrices precede Gram-Schmidt/QR, and inverses/rank/subspaces follow afterward.",
        "- Set labels are normalized on the singular `mf:set-*` convention.",
        "- Identifiability-related Data Analysis rows now include `mf:null-space` as a future target.",
        "- A short `mf:least-squares-projection-bridge` label has been added for Data Analysis projection language without creating a long new chapter.",
        "- A preliminary acknowledgments name audit was run against `MathFoundationsNotes.pdf` using extracted text. Entries marked unclear need manual page-image verification before final acknowledgments.",
    ]
    (REWRITE / "Math_Foundations_Textbook_Rewrite_Plan_v2.md").write_text("\n".join(plan_lines) + "\n", encoding="utf-8")

    print(f"source_map_entries={len(source_rows)}")
    print(f"connection_callouts={len(callout_rows)}")
    print(f"crosswalk_rows={len(all_rows)}")
    print(f"label_registry_rows={len(LABEL_ROWS)}")
    print(f"old_page_map_rows={len(old_page_rows)}")
    print(f"acknowledgment_rows={len(name_rows)}")


def acknowledgments_rows() -> list[dict[str, str]]:
    raw = [
        ("Dr. / Professor Bassett", "Professor / course instructor", "Professor Bassett appears in course header and scribe lines; Dr. Bassett wording requested in handoff.", "Observed as Professor Bassett; Dr. title requested", "Use wording that covers Dr./Professor Bassett without implying a different person."),
        ("Adrian Tomaneng", "Scribe / highlighted note taker", "Scribe(s): Adrian Tomaneng, Mary Poltrack", "Observed", ""),
        ("Mary Poltrack", "Scribe / highlighted note taker", "Scribe(s): Adrian Tomaneng, Mary Poltrack", "Observed", ""),
        ("Anna Delaney", "Scribe / highlighted note taker", "Scribe(s): Anna Delaney, Robert Moore; Scribes: Anna Delaney and Camille Herman; Scribes: Anna Delaney, Ian Moss", "Observed", ""),
        ("Robert Moore", "Scribe / highlighted note taker", "Scribe(s): Anna Delaney, Robert Moore; Scribes: Katie Hernandez, Robert Moore, Ryan Warren; Scribes: Robert Moore, Christopher Posadas, Ryan Warren", "Observed", ""),
        ("Brandon De La Rosa", "Scribe / highlighted note taker", "Professor: Bassett Scribes: Brandon Delarosa, Jessica Sanders; Scribes: Mariano Amaro, Brandon De La Rosa, Ian Moss", "Corrected by user", ""),
        ("Jessica Sanders", "Scribe / highlighted note taker", "Multiple scribe lines include Jessica Sanders.", "Observed", ""),
        ("Brian Park", "Scribe / highlighted note taker", "Scribe(s): Brian Park and Duke Brady; Vectors (2OCT2025) Scribes: Brian Park, Kevin Crush", "Observed", ""),
        ("Duke Brady", "Scribe / highlighted note taker", "Scribe(s): Brian Park and Duke Brady; Scribe(s): Duke Brady and Greg Lucarelli; Scribe(s): Ryan Berry and Duke Brady", "Observed", ""),
        ("Paul Deist", "Scribe / highlighted note taker", "Scribe(s): Capt Paul Deist and 1stLt Camille Herman; Scribe(s): Paul Deist, Jessica Sanders", "Corrected by user", ""),
        ("Camille Herman", "Scribe / highlighted note taker", "Scribe(s): Capt Paul Deist and 1stLt Camille Herman; Scribes: Anna Delaney and Camille Herman", "Corrected by user", ""),
        ("Ryan Berry", "Scribe / highlighted note taker", "Scribe(s): Capt Ryan Berry; Scribe(s): Ryan Berry and Duke Brady", "Corrected by user", ""),
        ("Greg Lucarelli", "Scribe / highlighted note taker", "Scribe(s): Duke Brady and Greg Lucarelli; Scribes: Leigh Freitag and Greg Lucarelli", "Observed", ""),
        ("Joshua Brewster", "Scribe / highlighted note taker", "Scribe(s): Joshua Brewster, Christopher Posadas, Daniel Valdelamar; Scribe(s): Joshua Brewster, Katie Hernandez, Daniel Valdelamar", "Observed", ""),
        ("Christopher Posadas", "Scribe / highlighted note taker", "Scribe(s): Joshua Brewster, Christopher Posadas, Daniel Valdelamar; Scribes: Robert Moore, Christopher Posadas, Ryan Warren", "Observed", ""),
        ("Daniel Valdelamar", "Scribe / highlighted note taker", "Scribe(s): Joshua Brewster, Christopher Posadas, Daniel Valdelamar; Scribe(s): Joshua Brewster, Katie Hernandez, Daniel Valdelamar", "Observed", ""),
        ("Katie Hernandez", "Scribe / highlighted note taker", "Scribe(s): Joshua Brewster, Katie Hernandez, Daniel Valdelamar; Scribes: Katie Hernandez, Robert Moore, Ryan Warren", "Observed", ""),
        ("Katerina Franco", "Scribe / highlighted note taker", "Scribe(s): Katerina and Jackson Franco", "Corrected by user", ""),
        ("Jackson Franco", "Scribe / highlighted note taker", "Scribe(s): Katerina and Jackson Franco", "Observed", ""),
        ("Kevin Crush", "Scribe / highlighted note taker", "Scribe(s): Kevin Crush, Brian Park, Jessica Sanders; Vectors (2OCT2025) Scribes: Brian Park, Kevin Crush", "Observed", ""),
        ("Ryan Warren", "Scribe / highlighted note taker", "Scribe(s): Ryan Berry, Katie Hernandez, Ryan Warren; Scribes: Robert Moore, Christopher Posadas, Ryan Warren", "Observed", ""),
        ("Ian Moss", "Scribe / highlighted note taker", "Scribes: Anna Delaney, Ian Moss; Scribes: Mariano Amaro, Brandon De La Rosa, Ian Moss", "Observed", ""),
        ("Keisha Castillo", "Scribe / highlighted note taker", "Scribes: Keisha Castillo and Shaun Ketner", "Observed", ""),
        ("Shaun Ketner", "Scribe / highlighted note taker", "Scribes: Keisha Castillo and Shaun Ketner", "Observed", ""),
        ("Leigh Freitag", "Scribe / highlighted note taker", "Scribes: Leigh Freitag and Greg Lucarelli", "Observed", ""),
        ("Mariano Amaro", "Scribe / highlighted note taker", "Scribes: Mariano Amaro, Brandon De La Rosa, Ian Moss; Scribes: Mariano Amaro, Ian Moss", "Observed", ""),
        ("Samantha Brooker", "Scribe / highlighted note taker", "Scribes: Samantha Brooker, Christine La", "Observed", ""),
        ("Christine La", "Scribe / highlighted note taker", "Scribes: Samantha Brooker, Christine La", "Observed", ""),
    ]
    return [
        {
            "Name": name,
            "Role": role,
            "EvidenceSource": "MathFoundationsNotes.pdf text audit",
            "EvidenceSnippet": evidence,
            "AuditStatus": status,
            "Notes": notes,
        }
        for name, role, evidence, status, notes in raw
    ]


if __name__ == "__main__":
    write_outputs()
