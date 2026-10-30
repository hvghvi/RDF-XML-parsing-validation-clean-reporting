from pathlib import Path

from parse_cim import parse_cim


def test_parse_rdf_id_and_resource_reference():
    fixture_path = Path(__file__).parent / "data" / "rdf_id.xml"

    assert parse_cim(fixture_path) == {
        "#CN_Node01": {
            "tag": "ConnectivityNode",
            "IdentifiedObject.name": "Substation_Node_A",
        },
        "urn:uuid:terminal-1": {
            "tag": "Terminal",
            "Terminal.ConnectivityNode": "#CN_Node01",
        },
    }
