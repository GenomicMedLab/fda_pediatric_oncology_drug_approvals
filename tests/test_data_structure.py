from pathlib import Path
import json

import pytest

from ga4gh.va_spec.base import Statement


@pytest.fixture(scope="session")
def data():
    with (Path(__file__).parents[1] / "fda_poda.json").open() as f:
        return json.load(f)


def test_valid_data_structure(data: dict):
    for statement in data.get("statements", []):
        assert Statement(**statement)


def test_statement_ids_successive(data: dict):
    """Test that statement IDs are unique and incrementing"""
    id_values = [int(s["id"].split(":")[-1]) for s in data.get("statements", [])]
    assert list(set(id_values)) == id_values
    assert all(id_value > 0 for id_value in id_values)
    assert len(id_values) == max(id_values)
