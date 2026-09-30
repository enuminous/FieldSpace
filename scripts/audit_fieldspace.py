#!/usr/bin/env python3
from itertools import combinations
import json, re
from pathlib import Path

SECTORS=["E","M","S","F","W","T","I","R","H","P","A"]
SCALARS=set(["F","W","T","I","R","H","P","A"])
SRC=Path("EFMW_165_field_equations.txt")
text=SRC.read_text()
lines=text.splitlines()
rx=re.compile(r"^=== Triplet \('([A-Z])', '([A-Z])', '([A-Z])'\) ===$")
blocks=[]
cur=None
for line in lines:
    m=rx.match(line)
    if m:
        if cur is not None: blocks.append(cur)
        cur={"triplet":list(m.groups()),"lines":[]}
    elif cur is not None:
        cur["lines"].append(line)
if cur is not None: blocks.append(cur)

observed={"".join(sorted(b["triplet"])):b for b in blocks}
expected={"".join(sorted(c)) for c in combinations(SECTORS,3)}
missing=sorted(expected-set(observed))
empty=sorted(k for k,b in observed.items() if not any(x.strip() for x in b["lines"]))

def count(p):
    return sum(1 for line in lines if p(line))
report={
  "triplet_headings":len(blocks),
  "populated_blocks":len(blocks)-len(empty),
  "missing_triplets":missing,
  "empty_triplets":empty,
  "statement_counts":{
    "einstein":count(lambda x:x.startswith("GR (Einstein):")),
    "gauge_dynamics":count(lambda x:x.endswith("-gauge:")),
    "bianchi":count(lambda x:"∇_[μ" in x),
    "scalar":count(lambda x:x.startswith("Scalar ")),
  }
}
report["statement_counts"]["total"]=sum(report["statement_counts"].values())
print(json.dumps(report,indent=2))
