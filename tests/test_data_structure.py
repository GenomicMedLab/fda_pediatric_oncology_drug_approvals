from pathlib import Path
import json

from ga4gh.va_spec.base import Statement


def test_valid_data_structure():
    with (Path(__file__).parents[1] / "fda_poda.json").open() as f:
        data = json.load(f)
    for statement in data.get("statements", []):
        assert Statement(**statement)
