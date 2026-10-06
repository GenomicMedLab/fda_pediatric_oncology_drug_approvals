import json
import re
from pathlib import Path

import pytest
from ga4gh.cat_vrs.models import CategoricalVariant
from ga4gh.core.models import MappableConcept
from ga4gh.va_spec.base import Method, Statement


@pytest.fixture(scope="session")
def data():
    with (Path(__file__).parents[1] / "fda_poda.json").open() as f:
        return json.load(f)


def test_valid_data_structure(data: dict):
    for condition in data["condition"].values():
        assert MappableConcept(**condition)
    for strength in data["strength"].values():
        assert MappableConcept(**strength)
    for therapy in data["therapy"].values():
        assert MappableConcept(**therapy)
    for gene in data["gene"].values():
        assert MappableConcept(**gene)
    for variant in data["variant"].values():
        assert CategoricalVariant(**variant)
    for method in data["method"].values():
        assert Method(**method)
    for statement in data["statement"].values():
        assert Statement(**statement)


def test_age_phenotype_format(data: dict):
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


# TODO test derefs/pointers all work... general bundle functions?
# https://ga4gh.github.io/gkm-starter-kit/0.4.0/tools/gkm-toolkit/notebooks/validation-notebook/
