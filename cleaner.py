import csv


def clean(errors):
    fieldnames = ["uuid", "tag", "missing_field"]
    with open('test_report', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()  # always write the header, even when there are no errors
        if errors:
            for error in errors:
                writer.writerow(error)  # writes each error as a row in the CSV file
   