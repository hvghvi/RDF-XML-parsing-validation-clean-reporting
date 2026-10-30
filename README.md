# RDF/XML Parsing, Validation, and Clean Reporting

This project parses CIM-style RDF/XML files, validates required fields and object references, and writes a CSV report of missing values and unresolved references.

## Purpose

This project is meant to practice working with real-world power-system data and CIM/XML import workflows. It focuses on:

- parsing XML data into structured dictionaries
- validating required fields based on equipment type
- reporting missing required fields and references to objects that do not exist
- generating a simple CSV report for downstream review

## Setup

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the project

From the project root, pass the XML file you want to parse:

```bash
python main.py "data/TD Basic Golden InstanceSet.xml"
```

This reads the CIM RDF/XML file and writes the generated CSV report under `output/` by default. The `output/` folder is created if needed and ignored by Git. Use `--output` to choose another report path.
If the input contains no RDF objects, the program prints a warning, exits with a non-zero status, and does not write a report.

## Run tests

```bash
python3 -m pytest
```

## Future improvements

- Scale handling: this dataset is small, so the current approach does not yet account for much larger XML files that may reach GB-scale sizes in real-world use.
- More robust validation: add richer rule sets for equipment-specific CIM fields instead of the current hardcoded examples.
- Better reporting: expand output to include more context, such as equipment type, source file, and fix suggestions.
- Performance tuning: improve memory usage and parsing efficiency for larger datasets and production pipelines.
