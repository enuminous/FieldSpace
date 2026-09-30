#!/usr/bin/env python3
"""Deterministic structural toy simulator for the intended 11-sector FieldSpace atlas.

This is NOT a numerical solution of the proposed tensor field equations.
Each named sector is represented by one dimensionless amplitude. Pair and
triple coefficients are deterministic synthetic weights chosen only to make
ablation/reproducibility tests possible.
"""
from itertools import combinations
import argparse, csv, json, math, statistics
from pathlib import Path

SECTORS = ["E","M","S","F","W","T","I","R","H","P","A"]
IDX = {s:i for i,s in enumerate(SECTORS)}
TRIPLETS = list(combinations(SECTORS, 3))

PAIR = {}
for a,b in combinations(SECTORS,2):
    i,j=IDX[a],IDX[b]
    raw=((i+1)*7+(j+1)*11)%9-4
    PAIR[(a,b)] = 0.004*raw

TRIPLE = {}
for t in TRIPLETS:
    i,j,k=(IDX[s] for s in t)
    raw=((i+1)*3+(j+1)*5+(k+1)*7)%11-5
    TRIPLE[t] = 0.0006*raw

GAMMA={s:0.10+0.004*(IDX[s]%5) for s in SECTORS}

PAIR_NEIGH={s:[] for s in SECTORS}
for (a,b),w in PAIR.items():
    PAIR_NEIGH[a].append((b,w))
    PAIR_NEIGH[b].append((a,w))

TRIPLE_NEIGH={s:[] for s in SECTORS}
for tri,w in TRIPLE.items():
    for s in tri:
        other=[q for q in tri if q != s]
        TRIPLE_NEIGH[s].append((other[0],other[1],w))

def simulate(removed=(), pair_on=True, triple_on=True, steps=800, dt=0.03):
    active=[s for s in SECTORS if s not in set(removed)]
    aset=set(active)
    x={s:0.08+0.015*(i+1) for i,s in enumerate(SECTORS)}
    for s in removed:
        x[s]=0.0
    peak=max(abs(v) for v in x.values())
    tail=[]
    for n in range(steps):
        t=n*dt
        dx={}
        for s in active:
            value=-GAMMA[s]*x[s]
            if pair_on:
                for r,w in PAIR_NEIGH[s]:
                    if r in aset:
                        value += w*x[r]
            if triple_on:
                for a,b,w in TRIPLE_NEIGH[s]:
                    if a in aset and b in aset:
                        value += w*x[a]*x[b]
            if s=="F":
                value += 0.025*math.sin(0.35*t)
            if s=="M":
                value += 0.012*math.sin(0.73*t+0.4)
            if s=="E":
                value += 0.008*math.cos(0.19*t)
            dx[s]=value
        for s,v in dx.items():
            x[s]+=dt*v
        current_peak=max((abs(x[s]) for s in active), default=0.0)
        peak=max(peak,current_peak)
        norm=math.sqrt(sum(x[s]**2 for s in active))
        if n >= steps-100:
            tail.append(norm)
    return {
        "stable": math.isfinite(norm) and norm < 1e5,
        "final_norm": norm,
        "peak": peak,
        "mean_tail": statistics.fmean(tail),
        "max_abs_final": current_peak,
    }

def run_all():
    base=simulate()
    rows=[("full","",base)]
    rows.append(("term_no_pair","",simulate(pair_on=False)))
    rows.append(("term_no_triple","",simulate(triple_on=False)))
    rows.append(("term_linear_only","",simulate(pair_on=False,triple_on=False)))
    for s in SECTORS:
        rows.append(("remove1",s,simulate((s,))))
    for p in combinations(SECTORS,2):
        rows.append(("remove2","".join(p),simulate(p)))
    for t in TRIPLETS:
        rows.append(("remove3","".join(t),simulate(t)))
    return base, rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--outdir", default="results")
    args=ap.parse_args()
    out=Path(args.outdir)
    out.mkdir(parents=True,exist_ok=True)
    base, rows=run_all()
    with (out/"ablation_results.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["kind","removed","stable","final_norm","peak","mean_tail","delta_mean_tail","max_abs_final"])
        for kind,label,r in rows:
            w.writerow([kind,label,int(r["stable"]),f'{r["final_norm"]:.15g}',f'{r["peak"]:.15g}',
                        f'{r["mean_tail"]:.15g}',f'{r["mean_tail"]-base["mean_tail"]:.15g}',
                        f'{r["max_abs_final"]:.15g}'])
    summary={
        "status":"toy structural simulation only; not physical validation",
        "run_count":len(rows),
        "all_stable":all(r["stable"] for _,_,r in rows),
        "base":base,
        "term_ablations":{k:r for k,l,r in rows if k.startswith("term_")},
    }
    for kind,name in [("remove1","single_sector"),("remove2","two_sector"),("remove3","three_sector")]:
        ds=[r["mean_tail"]-base["mean_tail"] for k,l,r in rows if k==kind]
        summary[name+"_delta_range"]=[min(ds),max(ds)]
    (out/"simulation_summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
