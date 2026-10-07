import json
import re
from pathlib import Path

import pytest
from ga4gh.gkm.bundles import load_bundle


@pytest.fixture(scope="session")
def data():
    with (Path(__file__).parents[1] / "fda_poda.json").open() as f:
        return json.load(f)


def test_age_phenotype_format(data: dict):
    """Ensure that phenotype concept declaration is consistent + matches expected nomenclature"""
    age_of_onset_pattern = re.compile(r"^\d+ (?:months?|years?) and older$")
    for statement in data.get("statements", []):
        for condition in statement["proposition"]["conditionQualifier"]["conditions"]:
            if condition["id"].startswith("fda_poda.onset"):
                assert condition["id"].split(":")[-1] == condition["name"]
                assert (
                    re.match(age_of_onset_pattern, condition["name"])
                    or condition["name"] == "Pediatric"
                )


def test_statement_ids_successive(data: dict):
    """Test that statement IDs are unique and incrementing"""
    id_values = [
        int(s["id"].split(":")[-1]) for s in data.get("statement", {}).values()
    ]
    assert id_values == list(range(1, max(id_values) + 1))


def test_load_bundle():
    """Test overall GKM bundle structure"""
    assert load_bundle("fda_poda.json", schema="schema.json")
