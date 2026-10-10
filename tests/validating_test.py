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


def test_validate(get_required_fields, get_required_fields2):
    storage_with_errors = {
        'uuid1': {
            'tag': 'Feeder',
            'IdentifiedObject.name': 'Feeder A',
            'Feeder.TraceStart': '2024-01-01',
        },
        'uuid2': {
            'tag': 'ConnectivityNode',
            'IdentifiedObject.name': 'Node 1',
        },
        'uuid3': {
            'tag': 'ERORR',
        },
    }

    assert validate(storage_with_errors, get_required_fields) == [
        {'uuid': 'uuid1', 'tag': 'Feeder', 'missing_field': 'shouldbeerror'},
        {'uuid': 'uuid3', 'tag': 'ERORR', 'missing_field': 'ERROR'},
        {'uuid': 'uuid3', 'tag': 'ERORR', 'missing_field': 'ERROR'},
    ]

    storage_without_errors = {
        'uuid1': {
            'tag': 'Feeder',
            'IdentifiedObject.name': 'Feeder A',
            'Feeder.TraceStart': '2024-01-01',
        },
        'uuid2': {
            'tag': 'ConnectivityNode',
            'IdentifiedObject.name': 'Node 1',
        },
        'uuid3': {
            'tag': 'ERORR',
            'ERROR': 'A value',
        },
    }

    assert validate(storage_without_errors, get_required_fields2) == []
