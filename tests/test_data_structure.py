from pathlib import Path
import re
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


def test_age_phenotype_format(data: dict):
    age_of_onset_pattern = re.compile(r"^\d+ (months|years) and older$")
    for statement in data.get("statements", []):
        for condition in statement["proposition"]["conditionQualifier"]["conditions"]:
            if condition["id"].startswith("fda_poda.onset"):
                assert condition["id"].split(":")[-1] == condition["name"]
                assert re.match(age_of_onset_pattern, condition["name"])


def test_statement_ids_successive(data: dict):
    """Test that statement IDs are unique and incrementing"""
    id_values = [int(s["id"].split(":")[-1]) for s in data.get("statements", [])]
    assert id_values == list(range(1, max(id_values) + 1))
