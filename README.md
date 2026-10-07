# FDA Pediatric Drug Oncology Approvals Curation

Description TBD

## Releases

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

For example, if `dataVersion` is `1.2.0`, push the `1.2.0` tag. If the tag and
data version differ, or the tests fail, no release is published. Re-pushing an
existing release tag updates its archive asset.
