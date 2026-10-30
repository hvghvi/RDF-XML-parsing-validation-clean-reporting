import pytest

from main import main


def test_empty_parse_warns_and_exits_nonzero(tmp_path, monkeypatch, capsys):
    input_path = tmp_path / "empty.rdf"
    input_path.write_text(
        '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"/>',
        encoding="utf-8",
    )
    output_path = tmp_path / "report.csv"
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", str(input_path), "--output", str(output_path)],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1  #error exit code
    assert "Warning: no RDF objects were found" in capsys.readouterr().err #intercepts the error message
    assert not output_path.exists()
