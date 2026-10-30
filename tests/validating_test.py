import pytest

from parse_cim import parse_cim
from validating import validate


def test_parse_cim_builds_uuid_index():
    storage = parse_cim('data/TD Basic Golden InstanceSet.xml')

    feeder_uuid = 'urn:uuid:bfaee055-4440-4173-9b95-615b6fafd523'
    node_uuid = 'urn:uuid:5d73925c-b008-472d-a75b-a64c886a8805'

    assert storage[feeder_uuid]['tag'] == 'Feeder'
    assert storage[feeder_uuid]['IdentifiedObject.name'] == 'Fdr 3A'
    assert storage[feeder_uuid]['Feeder.TraceStart'] == 'urn:uuid:5d73925c-b008-472d-a75b-a64c886a8805'
    assert storage[node_uuid]['tag'] == 'ConnectivityNode'
    assert storage[node_uuid]['IdentifiedObject.name'] == 'Feeder A CN'


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


def test_empty_values_count_as_missing():
    storage = {
        'u1': {
            'tag': 'Feeder',
            'IdentifiedObject.name': '',
            'Feeder.TraceStart': None,
        },
    }
    rules = {'Feeder': ['IdentifiedObject.name', 'Feeder.TraceStart']}

    assert validate(storage, rules) == [
        {'uuid': 'u1', 'tag': 'Feeder', 'missing_field': 'IdentifiedObject.name'},
        {'uuid': 'u1', 'tag': 'Feeder', 'missing_field': 'Feeder.TraceStart'},
    ]