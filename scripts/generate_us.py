#!/usr/bin/env python3
"""Régénère src/data/etats-unis-geo.json (tracés SVG des 50 États) à partir de us-atlas.

Source attendue dans le dossier passé en argument (par défaut ./sources) :
  - states-albers-10m.json   https://cdn.jsdelivr.net/npm/us-atlas@3/states-albers-10m.json
    (TopoJSON déjà projeté en Albers USA, Alaska et Hawaï repositionnés ; d'après le US Census Bureau)

Usage :
    python3 scripts/generate_us.py [dossier_sources]
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from generate_data import to_svg  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data"
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "sources"

# Code FIPS → code postal (le district de Columbia, « 11 », n'est pas un État : il est ignoré)
FIPS = {"01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO", "09": "CT", "10": "DE", "12": "FL",
        "13": "GA", "15": "HI", "16": "ID", "17": "IL", "18": "IN", "19": "IA", "20": "KS", "21": "KY", "22": "LA",
        "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN", "28": "MS", "29": "MO", "30": "MT", "31": "NE",
        "32": "NV", "33": "NH", "34": "NJ", "35": "NM", "36": "NY", "37": "NC", "38": "ND", "39": "OH", "40": "OK",
        "41": "OR", "42": "PA", "44": "RI", "45": "SC", "46": "SD", "47": "TN", "48": "TX", "49": "UT", "50": "VT",
        "51": "VA", "53": "WA", "54": "WV", "55": "WI", "56": "WY"}
PAD = 8  # marge autour de la carte et des encarts


def decode_arcs(topo):
    (sx, sy), (tx, ty) = topo["transform"]["scale"], topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x, y = x + dx, y + dy
            pts.append([x * sx + tx, y * sy + ty])
        arcs.append(pts)
    return arcs


def ring(arcs, idx):
    pts = []
    for i in idx:
        a = arcs[i] if i >= 0 else arcs[~i][::-1]
        pts.extend(a if not pts else a[1:])
    return pts


def main():
    topo = json.loads((SRC / "states-albers-10m.json").read_text(encoding="utf-8"))
    arcs = decode_arcs(topo)
    x0, y0, x1, y1 = topo["bbox"]
    shift = lambda p: [p[0] - x0 + PAD, p[1] - y0 + PAD]
    projected = {}
    for g in topo["objects"]["states"]["geometries"]:
        if g["id"] not in FIPS:
            continue
        polys = g["arcs"] if g["type"] == "MultiPolygon" else [g["arcs"]]
        projected[FIPS[g["id"]]] = [[[shift(p) for p in ring(arcs, r)] for r in poly] for poly in polys]
    states = to_svg(projected, 0.2, 0.5)

    # États voisins : ceux qui partagent au moins un tronçon de frontière (arc TopoJSON)
    arcs_of = {}
    for g in topo["objects"]["states"]["geometries"]:
        if g["id"] in FIPS:
            polys = g["arcs"] if g["type"] == "MultiPolygon" else [g["arcs"]]
            arcs_of[FIPS[g["id"]]] = {i if i >= 0 else ~i for poly in polys for r in poly for i in r}
    for code, mine in arcs_of.items():
        states[code]["n"] = sorted(o for o, theirs in arcs_of.items() if o != code and mine & theirs)

    # Encarts autour de l'Alaska et d'Hawaï
    boxes = {}
    for code in ("AK", "HI"):
        pts = [p for poly in projected[code] for r in poly for p in r]
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        m = 5  # assez petit pour que les deux encarts ne se chevauchent pas
        boxes[code] = [round(min(xs) - m, 1), round(min(ys) - m, 1),
                       round(max(xs) - min(xs) + 2 * m, 1), round(max(ys) - min(ys) + 2 * m, 1)]

    out = {"states": states, "boxes": boxes, "vb": [0, 0, round(x1 - x0 + 2 * PAD), round(y1 - y0 + 2 * PAD)]}
    (DATA / "etats-unis-geo.json").write_text(json.dumps(out, separators=(",", ":")), encoding="utf-8")
    print(f"{len(states)} États → src/data/etats-unis-geo.json")


if __name__ == "__main__":
    main()
