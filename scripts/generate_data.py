#!/usr/bin/env python3
"""Régénère les tracés SVG de src/data/ à partir des données géographiques brutes.

Ce script ne sert qu'à refaire les fichiers *-geo.json et prefectures-points.json
(changement de projection, de simplification, nouvelle source…). Pour le jeu lui-même,
seul scripts/build.py est nécessaire.

Sources attendues dans le dossier passé en argument (par défaut ./sources) :
  - departements-version-simplifiee.geojson   } https://github.com/gregoiredavid/france-geojson
  - departements-avec-outre-mer.geojson        }
  - regions-version-simplifiee.geojson         }
  - cities.json   (paquet npm « cities.json », extrait de GeoNames, licence CC BY 4.0)

Usage :
    python3 scripts/generate_data.py [dossier_sources]
"""
import json
import math
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data"
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "sources"

# --- Projection de la métropole (équirectangulaire centrée sur 46,5° N) -------------------
LAT0, K = 46.5, 95
COSM = math.cos(math.radians(LAT0))
X0, Y0, OX, OY = -5.2, 51.15, 215, 15
# --- Encarts outre-mer : colonne de carrés à gauche de la carte ------------------------
DOM = ["971", "972", "973", "974", "976"]
BOX, GAP, BOX_X, BOX_Y0, BOX_PAD = 168, 14, 15, 15, 18


def load(name):
    return json.loads((SRC / name).read_text(encoding="utf-8"))


def polys(g):
    return g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]


def douglas_peucker(pts, tol):
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = math.hypot(dx, dy)
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        p = pts[i]
        d = (math.hypot(p[0] - a[0], p[1] - a[1]) if length == 0
             else abs(dy * p[0] - dx * p[1] + b[0] * a[1] - b[1] * a[0]) / length)
        if d > dmax:
            dmax, idx = d, i
    if dmax > tol:
        return douglas_peucker(pts[:idx + 1], tol)[:-1] + douglas_peucker(pts[idx:], tol)
    return [a, b]


def area(r):
    return abs(sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r)))) / 2


def centroid(r):
    a = cx = cy = 0
    for i in range(len(r)):
        x0, y0 = r[i - 1]
        x1, y1 = r[i]
        c = x0 * y1 - x1 * y0
        a += c
        cx += (x0 + x1) * c
        cy += (y0 + y1) * c
    return r[0] if a == 0 else [cx / (3 * a), cy / (3 * a)]


def to_svg(projected, tol, min_area):
    """{id: [[ring…]…]} déjà projeté → {id: {d: path SVG, c: centre du plus grand polygone, a: son aire}}"""
    out = {}
    for code, polygons in projected.items():
        d, best, best_area = [], None, 0
        for poly in polygons:
            for j, ring in enumerate(poly):
                s = douglas_peucker(ring, tol)
                a = area(s)
                if len(s) < 4 or a < min_area:
                    continue
                if j == 0 and a > best_area:
                    best_area, best = a, s
                d.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in s[:-1]) + "Z")
        out[code] = {"d": "".join(d), "c": [round(v, 1) for v in centroid(best)], "a": round(best_area)}
    return out


def project_metro(geometry):
    return [[[[OX + (lo - X0) * COSM * K, OY + (Y0 - la) * K] for lo, la in r] for r in p] for p in polys(geometry)]


def dom_transforms(full):
    """Pour chaque DOM : fonction (lon, lat) → (x, y) dans son encart, et la boîte de l'encart."""
    tr, boxes, y = {}, {}, BOX_Y0
    for code in DOM:
        pts = [p for poly in polys(full[code]["geometry"]) for r in poly for p in r]
        lats, lons = [p[1] for p in pts], [p[0] for p in pts]
        cl = math.cos(math.radians(sum(lats) / len(lats)))
        w, h = (max(lons) - min(lons)) * cl, max(lats) - min(lats)
        s = (BOX - 2 * BOX_PAD) / max(w, h)
        ox, oy = BOX_X + (BOX - w * s) / 2, y + (BOX - h * s) / 2 + 6
        tr[code] = (lambda lo, la, ox=ox, oy=oy, mlo=min(lons), mla=max(lats), cl=cl, s=s:
                    [ox + (lo - mlo) * cl * s, oy + (mla - la) * s])
        boxes[code] = [BOX_X, y, BOX, BOX]
        y += BOX + GAP
    return tr, boxes


def norm(s):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower())


def main():
    metro = load("departements-version-simplifiee.geojson")["features"]
    full = {f["properties"]["code"]: f for f in load("departements-avec-outre-mer.geojson")["features"]}
    tr, boxes = dom_transforms(full)

    # Départements
    deps = to_svg({f["properties"]["code"]: project_metro(f["geometry"]) for f in metro}, 0.25, 1.5)
    for code in DOM:
        proj = [[[tr[code](lo, la) for lo, la in r] for r in p] for p in polys(full[code]["geometry"])]
        deps.update(to_svg({code: proj}, 0.35, 2))
    (DATA / "departements-geo.json").write_text(
        json.dumps({"deps": deps, "boxes": boxes}, separators=(",", ":")), encoding="utf-8")

    # Régions (les DOM réutilisent le tracé de leur département)
    insee = {"11": "IDF", "24": "CVL", "27": "BFC", "28": "NOR", "32": "HDF", "44": "GE", "52": "PDL",
             "53": "BRE", "75": "NAQ", "76": "OCC", "84": "ARA", "93": "PAC", "94": "COR"}
    regions = to_svg({insee[f["properties"]["code"]]: project_metro(f["geometry"])
                      for f in load("regions-version-simplifiee.geojson")["features"]}, 0.25, 1.5)
    for code, rid in zip(DOM, ["GUA", "MTQ", "GUF", "REU", "MAY"]):
        regions[rid] = deps[code]
    (DATA / "regions-geo.json").write_text(json.dumps(regions, separators=(",", ":")), encoding="utf-8")

    # Préfectures : coordonnées GeoNames (pays FR + code département en admin2 ; pays propre pour les DOM)
    raw = (DATA / "departements.js").read_text(encoding="utf-8").split("`")[1].strip().split("\n")
    prefs = {line.split("|")[0]: line.split("|")[3] for line in raw}
    cities = load("cities.json")
    country = {"971": "GP", "972": "MQ", "973": "GF", "974": "RE", "976": "YT"}
    alias = {"Évry-Courcouronnes": "Evry"}
    points = {}
    for code, pref in prefs.items():
        want = norm(alias.get(pref, pref))
        cand = [c for c in cities if (c["country"] == "FR" and c["admin2"] == code) or c["country"] == country.get(code)]
        match = ([c for c in cand if norm(c["name"]) == want]
                 or [c for c in cand if norm(c["name"]).startswith(want) or want.startswith(norm(c["name"]))])
        if not match:
            sys.exit(f"Préfecture introuvable dans GeoNames : {pref} ({code})")
        lo, la = float(match[0]["lng"]), float(match[0]["lat"])
        xy = tr[code](lo, la) if code in tr else [OX + (lo - X0) * COSM * K, OY + (Y0 - la) * K]
        points[code] = [round(xy[0], 1), round(xy[1], 1)]
    (DATA / "prefectures-points.json").write_text(json.dumps(points, separators=(",", ":")), encoding="utf-8")

    print(f"{len(deps)} départements, {len(regions)} régions, {len(points)} préfectures → src/data/")


if __name__ == "__main__":
    main()
