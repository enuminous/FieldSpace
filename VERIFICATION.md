# Reproducible Lean verification

Use the committed toolchain and dependency manifest. The workflow restores
applicable caches, builds the configured library, and audits every safe
declaration defined in the project modules listed in `Audit.lean`, including
private declarations. The permitted axioms are `propext`, `Classical.choice`, and `Quot.sound`.

```sh
lake exe cache get
lake build
lake env lean -DwarningAsError=true Audit.lean
python3 scripts/test_axiom_audit.py
```

The rejection controls inject a public axiom, private axiom and placeholder proof
and require the audit to fail for the intended reason.
Native proof evaluation is rejected. The existing finite enumeration statements now use `decide +kernel`, so no native compiler axiom is admitted. No theorem statement or hypothesis was changed.

The successful job summary records the exact commit and workflow run. Source
declarations and hypotheses determine the mathematical scope; a successful
build does not validate a broader empirical or scientific interpretation.

The source-atlas regression previously expected the historical 164-heading defect. The committed source now contains all 165 populated blocks. The regression now requires exactly that complete atlas, including distinct headings and a nonempty body for every block. The retained generated recovery patch is a historical artifact.
