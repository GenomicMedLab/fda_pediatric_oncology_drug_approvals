# FDA Pediatric Oncology Drug Approvals

This repository curates the FDA's [Pediatric Oncology Drug Approvals](https://www.fda.gov/about-fda/oncology-center-excellence/pediatric-oncology-drug-approvals) as a machine-readable [GA4GH Genomic Knowledge Model (GKM)](https://genomicsandhealth.org/ga4gh-genomic-knowledge-standards/) bundle. It represents approval statements alongside the relevant therapies, cancer types, age groups, and—where applicable—genomic biomarkers.

## Usage

Use the [GA4GH GKM Starter Kit](https://ga4gh.github.io/gkm-starter-kit/latest/) to load the bundle. Keep `fda_poda.json` and `schema.json` together (as they are in this repository or a release archive), then load and validate the data:

```python
from ga4gh.gkm.bundles import load_bundle

bundle = load_bundle("fda_poda.json", schema="schema.json")
```

## Development

### Minting a release

Pushing a Git tag triggers the `release data` GitHub Actions workflow. The
workflow verifies that the tag exactly matches the `dataVersion` in
`schema.json`, installs the locked dependencies, runs the test suite, and
creates a GitHub release. Its release asset is
`fda-poda-<dataVersion>.tar.gz`, containing `schema.json` and `fda_poda.json`.

To publish a new release, commit the updated data and set `schema.json`'s
`dataVersion` to the intended release version. From that commit, create and
push a matching tag:

```sh
git tag <dataVersion>
git push origin <dataVersion>
```

For example, if `dataVersion` is `2026-01-01`, push the `2026-01-01` tag. If the tag and
data version differ, or the tests fail, no release is published. Re-pushing an
existing release tag updates its archive asset.
