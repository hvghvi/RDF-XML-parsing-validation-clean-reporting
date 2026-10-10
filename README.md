# RDF/XML Parsing, Validation, and Clean Reporting

This project parses CIM-style RDF/XML files, validates required fields, and writes a clean CSV report of missing values.

## Purpose

This project is meant to practice working with real-world power-system data and CIM/XML import workflows. It focuses on:

- parsing XML data into structured dictionaries
- validating required fields based on equipment type
- cleaning and reporting missing data
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

```bash
python main.py
```

This currently uses the XML file configured in `main.py` and writes the generated report to `test_report` in the project root.

## Run tests

```bash
python3 -m pytest
```

## Current Disadvantages:

storage problem: since this dataset is quite small we arent really accounting what happens when data starts going into GB range (which is realistic in the real world)
