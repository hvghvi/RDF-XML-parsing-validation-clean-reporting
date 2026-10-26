import csv

def clean(errors, output_path="test_report"):
    fieldnames = ["uuid", "tag", "missing_field"]
    with open(output_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        if errors:
            for error in errors:
                writer.writerow(error)