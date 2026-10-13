#!/usr/bin/env python3
"""Assemble index.html à partir de src/template.html et des données de src/data/.

Usage :
    python3 scripts/build.py              # écrit index.html (page autonome pour GitHub Pages)
    python3 scripts/build.py --fragment   # écrit dist/fragment.html (sans <html>/<head>, pour un hébergeur qui ajoute son propre squelette)

Aucune dépendance : uniquement la bibliothèque standard de Python 3.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DATA = SRC / "data"


def compact(path):
    return json.dumps(json.loads(path.read_text(encoding="utf-8")), separators=(",", ":"), ensure_ascii=False)


def render_body():
    t = (SRC / "template.html").read_text(encoding="utf-8")
    geo = json.loads((DATA / "departements-geo.json").read_text(encoding="utf-8"))
    replacements = {
        # __GEO__ doit être remplacé en dernier : son nom est un préfixe de __GEOREG__
        "__RAW__": (DATA / "departements.js").read_text(encoding="utf-8").strip(),
        "__GEOREG__": compact(DATA / "regions-geo.json"),
        "__PREFPTS__": compact(DATA / "prefectures-points.json"),
        "__GEO__": json.dumps({"deps": geo["deps"], "boxes": geo["boxes"]}, separators=(",", ":"), ensure_ascii=False),
    }
    for key, value in replacements.items():
        if t.count(key) != 1:
            sys.exit(f"Le marqueur {key} doit apparaître une seule fois dans src/template.html")
        t = t.replace(key, value)
    return t


HEAD = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Quiz de géographie de la France : départements, numéros, régions et préfectures sur carte interactive.">
<meta name="theme-color" content="#1f5fae">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%231f5fae'/%3E%3Cpath d='M16 6a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z' fill='%23fff'/%3E%3C/svg%3E">
<style>
/* Base commune (remplace le squelette fourni par l'hébergeur d'origine) */
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box}
body{margin:0;font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""


def standalone(body):
    # Le template commence par <title>, <link> et <style> : ils vont dans <head>, le reste dans <body>.
    cut = body.index("</style>") + len("</style>")
    return HEAD + body[:cut] + "\n</head>\n<body>\n" + body[cut:].lstrip() + "\n</body>\n</html>\n"


def main():
    body = render_body()
    if "--fragment" in sys.argv:
        out = ROOT / "dist" / "fragment.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(body, encoding="utf-8")
    else:
        out = ROOT / "index.html"
        out.write_text(standalone(body), encoding="utf-8")
    print(f"{out.relative_to(ROOT)} écrit ({out.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
