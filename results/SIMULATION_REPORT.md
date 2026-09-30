# FieldSpace Toy Simulation and Ablation Report

## Boundary

This simulation is intentionally **not** a numerical solution of the proposed EFMW tensor/scalar/gauge equations.

It collapses each of the 11 named sectors to a single dimensionless state amplitude and supplies small deterministic synthetic pair/triple coefficients. Its purpose is software testing:

- exercise all 165 intended hyperedges;
- verify deterministic propagation;
- run systematic knockouts;
- see whether conclusions are artifacts of one local term family;
- provide a reproducible target for CAT/RHINO/BUTTERFLY-style structural tests.

No fitted physical parameter appears anywhere in the toy model.

## Executed suite

The local run executed **235 trajectories**:

- 1 full model;
- 3 term-family ablations;
- 11 single-sector knockouts;
- 55 two-sector knockouts;
- 165 three-sector knockouts.

All 235 remained numerically bounded for 800 steps at dt=0.03 under the declared synthetic coefficients.

### Full toy trajectory

- terminal L2 norm: **0.0905616931**
- mean tail norm: **0.0817941340**
- peak absolute amplitude: **0.245**

### Term-family ablations

| Run | Mean tail norm | Change vs full |
|---|---:|---:|
| Full | 0.0817941 | — |
| No pair terms | 0.0729417 | -0.0088524 |
| No triple terms | 0.0819610 | +0.0001669 |
| Pair + triple off | 0.0730619 | -0.0087323 |

Under these arbitrary toy parameters, pair couplings matter much more than triple couplings. This is a **negative result against assuming three-way-term dominance**. Different physically fitted parameters could behave differently.

### Knockout ranges

- single-sector knockout change in mean-tail norm: **[-0.0109709, +0.0062430]**
- two-sector knockout: **[-0.0204011, +0.0109232]**
- three-sector knockout: **[-0.0315025, +0.0111681]**

Largest-magnitude executed three-sector effects included F-T-A, F-T-I, E-S-F, E-F-I, and F-P-A. These rankings are properties of the deterministic synthetic coefficient generator, **not predictions about nature**.

## Interpretation

The simulation establishes that a reproducible computational laboratory can be built directly on the intended FieldSpace topology and that exhaustive low-order sector ablations are cheap.

It does **not** establish:

- that any FieldSpace sector is physically real;
- that the toy coefficient rankings correspond to EFMW parameters;
- stability of the proposed PDE system;
- conservation;
- causality;
- quantum behavior;
- experimental advantage over a standard model.

Run `python sim/fieldspace_sim.py` to regenerate the CSV and JSON result files.
