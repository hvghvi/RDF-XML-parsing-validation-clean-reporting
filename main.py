from pathlib import Path
import argparse
import parse_cim as parse_cim
import validating as validate
import cleaner as cleaner

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Program takes a CIM file, validates the file, and makes a report")
    parser.add_argument("filename", help="file thats going to be parsed")
    parser.add_argument("-o", "--output", dest="output", default=None)
    args = parser.parse_args()

    required_fields = {
        'Feeder': ['IdentifiedObject.name', 'Feeder.TraceStart', 'shouldbeerror'],
        'ConnectivityNode': ['IdentifiedObject.name'],
        'ERORR': ['ERROR', 'ERROR']
    }

    parsed_data = parse_cim.parse_cim(args.filename)
    validated_data = validate.validate(parsed_data, required_fields)

    if args.output is None:
        args.output = Path(args.filename).stem + "_report.csv"

    cleaner.clean(validated_data, args.output)

if __name__ == "__main__":
    main()