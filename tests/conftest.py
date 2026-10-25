import pytest

@pytest.fixture
def get_required_fields(): # with errors
    required_fields = { #hardcoded in this example, will be changed into a function
        'Feeder': ['IdentifiedObject.name', 'Feeder.TraceStart', 'shouldbeerror'],
        'ConnectivityNode': ['IdentifiedObject.name'],
        'ERORR': ['ERROR', 'ERROR']
        }
    return required_fields

    
@pytest.fixture
def get_required_fields2(): # no errors
    required_fields2 = { #hardcoded in this example, will be changed into a function
        'Feeder': ['IdentifiedObject.name', 'Feeder.TraceStart'],
        'ConnectivityNode': ['IdentifiedObject.name'],
        }
    return required_fields2