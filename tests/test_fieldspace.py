import unittest
from itertools import combinations
from pathlib import Path
import re

SECTORS=["E","M","S","F","W","T","I","R","H","P","A"]

class FieldSpaceAuditTests(unittest.TestCase):
    def test_complete_atlas_count(self):
        self.assertEqual(len(list(combinations(SECTORS,3))),165)

    def test_current_source_defect_is_detected(self):
        text=Path("EFMW_165_field_equations.txt").read_text()
        rx=re.compile(r"^=== Triplet \('([A-Z])', '([A-Z])', '([A-Z])'\) ===$", re.M)
        headings=[tuple(m.groups()) for m in rx.finditer(text)]
        observed={"".join(sorted(t)) for t in headings}
        expected={"".join(sorted(t)) for t in combinations(SECTORS,3)}
        self.assertEqual(len(headings),164)
        self.assertEqual(expected-observed,{"AHP"})
        self.assertIn("=== Triplet ('S', 'P', 'A') ===",text)
        self.assertTrue(text.rstrip().endswith("=== Triplet ('S', 'P', 'A') ==="))

    def test_generated_recovery_is_explicitly_non_source(self):
        p=Path("generated/RECOVERY_PATCH.txt").read_text()
        self.assertIn("NOT PART OF THE FROZEN SOURCE",p)
        self.assertIn("Generated missing Triplet ('H', 'P', 'A')",p)

if __name__=="__main__":
    unittest.main()
