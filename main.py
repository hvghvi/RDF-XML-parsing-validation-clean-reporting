import parse_cim as parse_cim
import validating as validate
import cleaner as cleaner

import argparse
from pathlib import Path

def main(): #change prog name lol
    parser = argparse.ArgumentParser(description="Program takes a CIM file, validates the file, and makes a report",
                                     prog="CIM CHECKER")

    parser.add_argument("filename", help="file thats going to be parsed")#makes it required to send a file in
    args = parser.parse_args()

    parser.add_argument("-o","--o", "--output", dest="output", default=args.filename)

    required_fields = { #hardcoded in this example, will be changed into a function
    'Feeder': ['IdentifiedObject.name', 'Feeder.TraceStart', 'shouldbeerror'],
    'ConnectivityNode': ['IdentifiedObject.name'],
    'ERORR': ['ERROR', 'ERROR']
    }

    parsed_data = parse_cim.parse_cim(args)
    validated_data = validate.validate(parsed_data, required_fields)


    cleaner.clean(validated_data)

if __name__ == "__main__":
    main()

    