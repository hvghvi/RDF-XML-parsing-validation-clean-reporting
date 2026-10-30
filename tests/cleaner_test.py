import csv

from cleaner import clean


def test_right_number_of_errors():
    errors = [
        {"uuid": "u1", "tag": "Feeder", "missing_field": "shouldbeerror"},
        {"uuid": "u2", "tag": "ERORR", "missing_field": "ERROR"},
        {"uuid": "u3", "tag": "ERORR", "missing_field": "ERROR"},
    ]

    clean(errors)
    with open("test_report", "r") as csvfile:
        rows = list(csv.DictReader(csvfile, delimiter="|"))
    assert len(rows) == 3

    clean([])
    with open("test_report", "r") as csvfile:
        rows = list(csv.DictReader(csvfile, delimiter="|"))
    assert len(rows) == 0


def test_clean_writes_missing_reference_context(tmp_path):
    output_path = tmp_path / "report.csv"
    errors = [
        {
            "uuid": "urn:uuid:feeder-1",
            "tag": "Feeder",
            "reference_field": "Feeder.TraceStart",
            "missing_reference": "urn:uuid:missing-node",
        },
    ]

    clean(errors, output_path)

    with output_path.open(newline="") as csvfile:
        rows = list(csv.DictReader(csvfile, delimiter="|"))

    assert rows == [
        {
            "uuid": "urn:uuid:feeder-1",
            "tag": "Feeder",
            "missing_field": "",
            "reference_field": "Feeder.TraceStart",
            "missing_reference": "urn:uuid:missing-node",
        },
    ]
