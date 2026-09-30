> [!IMPORTANT]
> **2026-09-29 Zoo/formal audit:** direct parsing of the frozen source finds **164 triplet headings, 163 populated blocks, and 578 displayed statements**, not the documented 165/585. The existing S-P-A heading is empty and H-P-A is absent. The source is intentionally preserved unchanged. See [AUDIT_2026-09-29.md](./AUDIT_2026-09-29.md), [ZOO_46_RUN.md](./ZOO_46_RUN.md), [THEOREM_REGISTER.md](./THEOREM_REGISTER.md), the [Lean formalization](./FieldSpace.lean), and the [toy simulator](./sim/fieldspace_sim.py).

# FieldSpace

EFMW FieldSpace is a repository for the complete 165-triplet field-interaction formulation supplied as the current EFMW field-space master set.

The present formulation treats EFMW as an 11-sector field space and enumerates every possible three-sector projection. The primary source file is preserved as supplied; this repository's commentary describes its structure, scope, and formalization requirements without silently rewriting the equations.


## Website

A compact technical reference site is included at [index.html](./index.html). It presents the structural theorems of the 11-sector / 165-triplet index, the relevant field-equation families, and a separate list of consistency principles that remain to be derived.

The site is GitHub Pages-ready from the repository root. Once Pages is enabled for the `main` branch / root directory, the expected public address is:

`https://enuminous.github.io/FieldSpace/`


## Repository contents

- EFMW_165_field_equations.txt — complete master set of field equations for all 165 triplets.
- COMMENTARY.md — structural interpretation, formal status, consistency obligations, and proposed next steps.
- README.md — overview and navigation.

## Status

**Proposed phenomenological formulation; independently unreviewed.**

This repository does not by itself establish that the sectors correspond to distinct physical fields, that the couplings occur in nature, or that the full construction is a validated theory of fundamental physics. The source explicitly describes the lambda and kappa quantities as phenomenological couplings. No fitted parameter set, master action, dimensional table, or experimental validation dataset is included in the supplied equation file.

The equation source is therefore best read as a structured candidate interaction family and a specification for further mathematical and empirical work.

## The 11 sectors

The source defines:

| Symbol | Source description |
|---|---|
| E | gravity |
| M | electromagnetic gauge sector |
| S | symmetry gauge sector |
| F | scalar sector |
| W | scalar sector |
| T | scalar sector |
| I | scalar sector |
| R | scalar sector |
| H | scalar sector |
| P | scalar sector |
| A | scalar sector |

No additional physical interpretation of the eight scalar labels is assumed here beyond what the source itself states.

## Why there are exactly 165 triplets

There are 11 channels and each FieldSpace element contains exactly 3 distinct channels:

    C(11,3) = 11! / (3! 8!) = 165

A structural audit of the supplied file finds:

- 165 triplet blocks
- 165 unique triplets
- 0 missing three-channel combinations
- 0 duplicate triplets
- every channel appears in exactly 45 triplets

In graph-theoretic language, the index structure is the complete 3-uniform hypergraph on 11 vertices.

This is a statement about the enumeration structure only. It does not imply that the dynamics of every triplet are physically realized.

## Structural taxonomy

| Triplet class | Count |
|---|---:|
| three scalar sectors | 56 |
| one gauge + two scalar sectors | 56 |
| gravity + two scalar sectors | 28 |
| gravity + one gauge + one scalar | 16 |
| two gauges + one scalar | 8 |
| gravity + two gauges | 1 |
| **Total** | **165** |

## Equation inventory

Counting displayed equation statements in the supplied source yields:

| Equation type | Count |
|---|---:|
| Einstein equations | 45 |
| gauge dynamical/divergence equations | 90 |
| gauge Bianchi-type identities | 90 |
| scalar equations | 360 |
| **Total displayed statements** | **585** |

The phrase “165-triplet formulation” is therefore more precise than calling this simply “165 equations.”

## Core pattern

A triplet may contain some combination of:

1. an Einstein equation when E is present;
2. one or two gauge equations and identities when M and/or S are present;
3. scalar wave/Klein–Gordon-like equations for the scalar sectors in the triplet;
4. pairwise couplings;
5. mixed three-sector interaction terms.

For example, a gravity–gauge–scalar triplet combines the gravitational field equation, gauge dynamics, a gauge identity, and a scalar equation with cross-coupling terms.

The full source is in [EFMW_165_field_equations.txt](./EFMW_165_field_equations.txt).

## Source notation

The supplied file defines or uses:

- G_{μν} — Einstein tensor
- g_{μν} — metric
- Λ — cosmological constant
- F_{μν} — M-sector gauge strength
- S_{μν} — S-sector gauge strength
- J^ν — currents
- ℜ — symbolic curvature scalar/invariant placeholder
- φ_X — scalar field associated with scalar sector X
- λ, κ — phenomenological couplings
- T_{μν}^{(int)} — mixed interaction stress contribution
- Ξ^ν — mixed interaction/current structure appearing in gauge equations

Some of these objects require more explicit definition before a closed field theory can be claimed.

## A useful mathematical interpretation

The formulation can be viewed as an interaction atlas over an 11-sector field space.

    V = {E, M, S, F, W, T, I, R, H, P, A}

FieldSpace contains one dynamical block for every three-element subset of V.

The central object is therefore not necessarily a single privileged equation. It can instead be treated as a rule assigning a coupled dynamical system to every rank-3 projection of the larger sector space.

That interpretation suggests a stronger future formulation:

> derive the triplet systems from one master action or generating rule, then recover the 165 blocks as consistent restrictions/projections.

At present, the supplied file does not provide such a master action.

## Formal issues to resolve

The source is intentionally preserved verbatim. Several items should be settled in a later normalization pass rather than silently changed here.

### 1. Master action

A Lagrangian or action principle should be specified if the 165 systems are intended to arise from a single coherent field theory. This would constrain reciprocal couplings and stress-energy terms and make conservation analysis substantially cleaner.

### 2. Gauge-index normalization

The source contains gauge expressions written in forms such as:

    ∇_μ F_{μν}^{μν}
    ∇_[μ F_{μν}_{νρ]} = 0

These should be reviewed against the intended tensor definitions. If the intended forms are conventional divergence and Bianchi expressions, that change should be made in a versioned normalization commit, not retroactively assumed.

### 3. Geometry when E is absent

Scalar equations continue to use □_g, R, or related curvature structures in triplets that do not contain the E channel. The framework therefore needs to state whether geometry is universal background structure and E denotes only dynamical gravity, or whether E is the geometry/gravity sector itself and curvature terms should be handled differently when it is absent.

### 4. Dimensions and units

A dimensional table is required for every field, coupling, current, mass term, and mixed interaction.

### 5. Interaction tensors and currents

T_{μν}^{(int)}, Ξ^ν, and the channel currents need explicit definitions or generating rules.

### 6. Symmetry and conservation

The intended gauge symmetries, diffeomorphism behavior, Noether currents, and conservation identities need to be derived rather than presumed.

### 7. Parameter economy

The current notation permits many phenomenological couplings. A useful theory will need a principled account of which parameters are independent, constrained, zero by symmetry, or derivable from more fundamental quantities.

## Research program suggested by the formulation

A rigorous development path would be:

1. freeze the 165-triplet source as a versioned reference;
2. normalize notation without changing content;
3. define fields, units, signatures, domains, and boundary conditions;
4. propose a master Lagrangian/action or explicit generating rule;
5. derive each triplet as a projection of that master object;
6. test gauge and stress-energy consistency;
7. determine independent versus redundant coupling parameters;
8. identify known-theory limits and equivalent prior formulations;
9. formalize algebraic identities and projection rules;
10. construct numerical benchmark cases with prespecified failure conditions;
11. compare predictions against named standard models and data.

## Versioning principle

EFMW_165_field_equations.txt should be treated as the source snapshot for this formulation.

Corrections, normalizations, or reductions should be committed separately so that the original proposed system remains auditable.

## Provenance

Initial FieldSpace repository population: **September 29, 2026**.

The equation set was supplied for publication to this repository and has been preserved as the primary source artifact. The structural counts in this README are bookkeeping/audit results over that supplied file, not empirical validation.

## License and rights

No license is inferred by this repository documentation. Add an explicit LICENSE file only when the rights holder chooses the applicable terms.
