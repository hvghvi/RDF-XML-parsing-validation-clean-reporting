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
