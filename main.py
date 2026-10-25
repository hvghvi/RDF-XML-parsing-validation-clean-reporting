import parse_cim as parse_cim
import validating as validate
import cleaner as cleaner

import argparse
from pathlib import Path

def main():
    argparser = argparse.ArgumentParser(description="A script to calculate exponential growth.") #init
    



    required_fields = { #hardcoded in this example, will be changed into a function
    'Feeder': ['IdentifiedObject.name', 'Feeder.TraceStart', 'shouldbeerror'],
    'ConnectivityNode': ['IdentifiedObject.name'],
    'ERORR': ['ERROR', 'ERROR']
    }

    parsed_data = parse_cim.parse_cim(data)
    validated_data = validate.validate(parsed_data, required_fields)


    cleaner.clean(validated_data)

if __name__ == "__main__":
    main()

    