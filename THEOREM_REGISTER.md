# FieldSpace Theorem Register

Status labels:

- **PROVED-STRUCTURAL** — follows from finite combinatorics/algebra and is formalized in Lean.
- **PROVED-ALGEBRAIC** — follows from the generic residual form and is formalized in Lean.
- **PROVED-PROJECTED-GLUING** — kernel-checked in the separate Post-156 audit under an explicit component-indexed interaction bound; this is a mathematical projection theorem, not physical validation.
- **CANDIDATE-CONSISTENCY-LAW** — required or strongly suggested by a coherent physical master theory, but not established by the current source.
- **OPEN-PHYSICS** — requires physical definitions, units, conservation, data, or validation.

## FS-T01 — Rank-3 Projection Count
**PROVED-STRUCTURAL**

For 11 sectors, the complete rank-3 atlas contains

`C(11,3)=165`

triplets.

## FS-T02 — Uniform Sector Incidence
**PROVED-STRUCTURAL**

Every sector belongs to

`C(10,2)=45`

triplets in the complete atlas.

## FS-T03 — Uniform Pair Incidence
**PROVED-STRUCTURAL**

Every unordered pair of sectors belongs to exactly 9 triplets, since the third sector can be chosen from the remaining nine.

## FS-T04 — Six-Class Decomposition
**PROVED-STRUCTURAL**

With one gravity sector E, two gauge sectors M/S, and eight scalar sectors, the complete atlas decomposes as:

`56 + 56 + 28 + 16 + 8 + 1 = 165`.

## FS-T05 — Statement Inventory
**PROVED-STRUCTURAL**

If every expected block is populated according to the source grammar, the statement inventory is:

`45 + 90 + 90 + 360 = 585`.

The restored current source contains the full expected 585 statements. The earlier 578-statement result is preserved only as the historical 2026-09-29 truncation audit.

## FS-T06 — Sector-Ablation Closure
**PROVED-STRUCTURAL**

Removing k sectors and retaining every triplet among the remaining sectors leaves

`C(11-k,3)`

triplets.

Important cases:

- remove 1 sector -> 120 remain, 45 deleted;
- remove 2 sectors -> 84 remain, 81 deleted;
- remove 3 sectors -> 56 remain, 109 deleted.

Thus the atlas is closed under vertex deletion as a complete 3-uniform hypergraph on the remaining vertices.

## FS-T07 — Projection-Overlap Spectrum
**PROVED-STRUCTURAL**

Among unordered pairs of distinct triplets:

- 1,980 pairs share exactly two sectors;
- 6,930 share exactly one sector;
- 4,620 are disjoint;

and

`1980 + 6930 + 4620 = C(165,2)=13,530`.

## FS-T08 — Trilinear Null-Slice Law
**PROVED-ALGEBRAIC**

For a mixed term `λ x y`, if either participating factor is zero, the three-way contribution vanishes.

This is ordinary algebra, not a new physical law. It has an important identifiability consequence: a three-way coupling cannot be estimated from data restricted to a slice on which one required field/invariant is identically zero.

## FS-T09 — Shared-Pair Overlap Consistency
**PROVED-ALGEBRAIC**

For a generic scalar triplet residual

`R_i = B_i + λ_ij φ_j + λ_ik φ_k + λ_ijk φ_j φ_k`,

restriction to `φ_k=0` gives

`R_i = B_i + λ_ij φ_j`.

Therefore two triplets sharing sectors i,j reduce to the same i-j residual on their respective third-field-zero slices **provided they use the same base term and pair coupling**.

This is the key local gluing condition suggested by FieldSpace.

# Candidate consistency laws

## FS-C01 — Projected Atlas Gluing
**PROVED-PROJECTED-GLUING**

The corrected mathematical contract restricts both field inputs and equation outputs. For compatible rank-3 chart data, the Post-156 audit proves existence and uniqueness of a reconstructed global family inside an explicit component-indexed interaction class. For the 11-sector / 165-triplet atlas this is packaged as a kernel-checked projected-atlas gluing theorem.

This replaces the earlier over-strong full-vector premise. The old zero-padded full-vector counterexample remains valid, and ordinary unrestricted three-body dependence is not sufficient for uniqueness.

The source audit reports 13,530 distinct chart pairs, 9,900 explicit retained-component comparisons, and zero explicit mismatches. This does not certify undefined physical mixed current/stress terms, vacuum conventions, conservation, or empirical validity.

## FS-C02 — Master-Action Reciprocity
**CANDIDATE-CONSISTENCY-LAW**

If scalar pair interactions arise from a conventional bilinear potential term `λ_ij φ_i φ_j`, the induced cross-coupling coefficient appears reciprocally in the i and j Euler-Lagrange equations, up to declared normalization conventions.

The current notation permits directional symbols such as `λ_ij` and `λ_ji`; a master action must determine whether they are equal, related, or genuinely distinct.

## FS-C03 — Noether/Conservation Closure
**CANDIDATE-CONSISTENCY-LAW**

If the final theory is gauge- and diffeomorphism-invariant and derives from a single action, the gauge currents, interaction stress tensor, and field equations cannot be chosen independently. Their divergences must satisfy the corresponding Noether/Bianchi consistency relations.

## FS-C04 — Parameter-Economy Law
**CANDIDATE-CONSISTENCY-LAW**

A successful master generating rule should reduce the number of independent phenomenological `λ` and `κ` parameters relative to treating every displayed coefficient as unrelated.

This is a model-selection principle, not yet a theorem of the source.

# No new fundamental physical law claimed

This pass does **not** establish a new law of nature. The strongest novel contribution is the **projection/gluing consistency structure**: FieldSpace behaves mathematically like a local atlas whose overlapping triplets must agree on shared lower-dimensional restrictions if it is to arise from one master theory.
