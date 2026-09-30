import Mathlib

namespace FieldSpace

/-- Generic local scalar residual used only to formalize the source grammar algebraically.
    `base` stands for the kinetic/mass/curvature part; the other arguments
    represent two pair terms and one three-way term. -/
def scalarTripletResidual
    (base λij λik λijk φj φk : ℝ) : ℝ :=
  base + λij * φj + λik * φk + λijk * φj * φk

/-- Removing the third field kills both terms that require that field. -/
theorem restrict_third_zero
    (base λij λik λijk φj : ℝ) :
    scalarTripletResidual base λij λik λijk φj 0 =
      base + λij * φj := by
  simp [scalarTripletResidual]

/-- Removing the second field gives the symmetric reduction. -/
theorem restrict_second_zero
    (base λij λik λijk φk : ℝ) :
    scalarTripletResidual base λij λik λijk 0 φk =
      base + λik * φk := by
  simp [scalarTripletResidual]

/-- A genuinely mixed trilinear contribution is invisible on either null slice. -/
theorem trilinear_null_slice_left (λ x : ℝ) :
    λ * x * 0 = 0 := by
  ring

theorem trilinear_null_slice_right (λ y : ℝ) :
    λ * 0 * y = 0 := by
  ring

/-- Two triplet charts that share the same base term and i-j pair coefficient
    glue exactly on the slice where their respective third fields vanish. -/
theorem shared_pair_overlap_consistency
    (base λij λik λijk λiℓ λijℓ φj : ℝ) :
    scalarTripletResidual base λij λik λijk φj 0 =
    scalarTripletResidual base λij λiℓ λijℓ φj 0 := by
  simp [scalarTripletResidual]

/-- Triple-term ablation is exact subtraction of that term. -/
theorem triple_ablation_difference
    (base λij λik λijk φj φk : ℝ) :
    scalarTripletResidual base λij λik λijk φj φk -
      scalarTripletResidual base λij λik 0 φj φk =
      λijk * φj * φk := by
  ring

end FieldSpace
