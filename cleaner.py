import csv


def clean(errors):
    if errors:
        with open('test_report', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["uuid", "tag", "missing_field"], delimiter='|')  # initializes the DictWriter with the file and header
            writer.writeheader()  # initializes the DictWriter with the file and header
            for error in errors:
                writer.writerow(error)  # writes each error as a row in the CSV file

    else:
        print("No errors found. No report generated.")
   