import parse_cim as parse_cim
import validating as validate

def main():
    data = 'data/TD Basic Golden InstanceSet.xml' #right now its hardcoded 
    #will be changed into a get function.

    required_fields = { #hardcoded in this example, will be changed into a function
    'Feeder': ['IdentifiedObject.name', 'Feeder.TraceStart'],
    'ConnectivityNode': ['IdentifiedObject.name']
    }

    parsed_data = parse_cim.parse_cim(data)
    validated_data = validate.validate(parsed_data, required_fields)


    