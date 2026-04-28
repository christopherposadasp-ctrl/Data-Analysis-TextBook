from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(r"C:\Users\posad\OneDrive\Desktop\DataAnalysis\Lectures")
REWRITE = ROOT / "Math Foundations Rewrite"
SOURCES = REWRITE / "Sources"
METADATA = REWRITE / "metadata"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def source_labels() -> dict[str, str]:
    labels: dict[str, str] = {}
    for source in sorted(SOURCES.glob("*.tex")):
        text = source.read_text(encoding="utf-8", errors="ignore")
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            labels[label] = source.name
    return labels


def main() -> None:
    labels = source_labels()

    registry = read_csv(METADATA / "MF_Label_Registry.csv")
    registry_status = []
    for row in registry:
        label = row["Label"]
        implemented_in = labels.get(label, "")
        status = "implemented" if implemented_in else "planned"
        out = dict(row)
        out["DraftStatus"] = status
        out["ImplementedInSource"] = implemented_in
        registry_status.append(out)

    registry_fields = list(registry[0].keys()) + ["DraftStatus", "ImplementedInSource"]
    write_csv(METADATA / "MF_Label_Implementation_Status.csv", registry_status, registry_fields)

    crosswalk = read_csv(METADATA / "MF_DA_Crosswalk.csv")
    crosswalk_status = []
    for row in crosswalk:
        future_labels = [item.strip() for item in row["FutureMFLabels"].split(";") if item.strip()]
        primary_labels = [label for label in future_labels if label != "mf:data-analysis-bridge-index"]
        implemented = [label for label in primary_labels if label in labels]
        remaining = [label for label in primary_labels if label not in labels]

        if primary_labels and not remaining:
            status = "all primary labels implemented"
        elif implemented:
            status = "partially implemented"
        else:
            status = "not yet implemented"

        out = dict(row)
        out["ImplementedLabels"] = "; ".join(implemented)
        out["RemainingLabels"] = "; ".join(remaining)
        out["ImplementationStatus"] = status
        crosswalk_status.append(out)

    crosswalk_fields = list(crosswalk[0].keys()) + [
        "ImplementedLabels",
        "RemainingLabels",
        "ImplementationStatus",
    ]
    write_csv(METADATA / "MF_DA_Crosswalk_Implementation_Status.csv", crosswalk_status, crosswalk_fields)

    print(f"source_labels={len(labels)}")
    print(f"registry_rows={len(registry_status)}")
    print(f"implemented_registry_labels={sum(1 for row in registry_status if row['DraftStatus'] == 'implemented')}")
    print(f"crosswalk_rows={len(crosswalk_status)}")
    print(f"fully_implemented_rows={sum(1 for row in crosswalk_status if row['ImplementationStatus'] == 'all primary labels implemented')}")
    print(f"partially_implemented_rows={sum(1 for row in crosswalk_status if row['ImplementationStatus'] == 'partially implemented')}")


if __name__ == "__main__":
    main()
