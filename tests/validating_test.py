import pytest

from validating import validate

def test_get_required_fields(get_required_fields):
    required_fields = get_required_fields
    assert isinstance(required_fields, dict)
    assert 'Feeder' in required_fields
    assert 'ConnectivityNode' in required_fields
    assert 'ERORR' in required_fields
    assert required_fields['Feeder'] == ['IdentifiedObject.name', 'Feeder.TraceStart', 'shouldbeerror']
    assert required_fields['ConnectivityNode'] == ['IdentifiedObject.name']
    assert required_fields['ERORR'] == ['ERROR', 'ERROR']   

def test_validate(get_required_fields, required_fields2):
    assert validate(get_required_fields) == ['Feeder: shouldbeerror', 'ERORR: ERROR', 'ERORR: ERROR']
    assert validate(required_fields2) == []
