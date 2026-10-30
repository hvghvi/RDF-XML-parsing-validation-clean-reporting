import csv
from pathlib import Path

def clean(errors, output_path="output/test_report.csv"):
    fieldnames = [
        "uuid",
        "tag",
        "missing_field",
        "reference_field",
        "missing_reference",
    ]
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        if errors:
            for error in errors:
                writer.writerow(error)