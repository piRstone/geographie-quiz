# Géographie quiz

Quiz pour réviser la géographie de la France sur une carte interactive : les 101 départements (numéros et noms), les 18 régions et les préfectures, Corse et outre-mer compris.

Tout tient dans un seul fichier, `index.html`, sans serveur ni dépendance : il s'ouvre directement dans un navigateur et se publie tel quel sur GitHub Pages.

## Les quiz

| Quiz | Principe |
| --- | --- |
| **Carte · Départements** | Clique un département, puis donne son nom **et** son numéro. Six indices progressifs : région, géographie, patrimoine, préfecture, première lettre, dernier chiffre. |
| **Carte · Régions** | Clique une région et donne son nom. Indices : particularités, réforme de 2016, chef-lieu, liste des départements, première lettre. |
| **Liste · noms** | Les départements sont listés par numéro (01 → 976) : tape le nom en face de chaque numéro. La carte se colore au fur et à mesure. |
| **Liste · préfectures** | Tape la préfecture de chaque département. Un point marque l'emplacement de chaque préfecture sur la carte. |

Fonctionnement commun :

- **Saisie tolérante** : accents, tirets, apostrophes, majuscules et articles sont ignorés ; « St » vaut « Saint » ; une petite faute de frappe est acceptée (sauf si elle correspond à un autre département, comme Loire / Loiret).
- **Listes** : le curseur passe à la ligne suivante dès que la réponse est complète ; l'ampoule révèle la réponse lettre par lettre ; la carte se centre sur le département de la ligne en cours.
- **Carte** : zoom à la molette ou au pincement, déplacement en glissant.
- **Progression** : enregistrée dans le navigateur (`localStorage`), séparément pour chaque quiz. Elle est propre à chaque appareil et à chaque adresse du site.
- **Lien direct vers un quiz** : `#carte`, `#regions`, `#noms` ou `#prefs` à la fin de l'URL.

## Mise en ligne sur GitHub Pages

1. Pousse le dépôt sur GitHub.
2. Dans **Settings → Pages**, choisis **Deploy from a branch**, branche `main`, dossier `/ (root)`.
3. Le site est disponible après une ou deux minutes à `https://<utilisateur>.github.io/geographie-quiz/`.

Le fichier `.nojekyll` indique à GitHub Pages de servir les fichiers tels quels, sans passer par Jekyll.

## Structure

```
index.html                     page générée, servie par GitHub Pages (ne pas modifier à la main)
src/
  template.html                styles, structure et code du jeu, avec des marqueurs pour les données
  data/
    departements.js           numéro | nom | région | préfecture | indices | autres noms acceptés
    departements-geo.json      tracés SVG des départements et position des encarts outre-mer
    regions-geo.json           tracés SVG des régions
    prefectures-points.json    position des préfectures sur la carte
scripts/
  build.py                     assemble index.html à partir de src/
  generate_data.py             recalcule les tracés à partir des données géographiques brutes
```

## Modifier le jeu

Modifie `src/template.html` (interface, règles, quiz) ou `src/data/departements.js` (noms, préfectures, indices, variantes acceptées), puis regénère la page :

```sh
python3 scripts/build.py
```

Python 3 suffit, sans aucun paquet à installer. Pense à committer `index.html` avec tes modifications : c'est lui que GitHub Pages sert.

Les indices des régions et les variantes de noms des préfectures (« Le Puy », « Évry »…) sont directement dans `src/template.html`.

### Régénérer les tracés (rarement utile)

Uniquement pour changer la projection, la simplification des contours ou la source des données :

1. Crée un dossier `sources/` (ignoré par git) et places-y :
   - `departements-version-simplifiee.geojson`, `departements-avec-outre-mer.geojson` et `regions-version-simplifiee.geojson`, depuis [france-geojson](https://github.com/gregoiredavid/france-geojson) ;
   - `cities.json`, depuis le paquet npm [`cities.json`](https://www.npmjs.com/package/cities.json) (`npm pack cities.json`, puis extraire `package/cities.json`).
2. Lance :

```sh
python3 scripts/generate_data.py sources
python3 scripts/build.py
```

## Sources des données

- **Contours des départements et des régions** : [france-geojson](https://github.com/gregoiredavid/france-geojson) de Grégoire David, d'après les données publiques de l'IGN et de l'INSEE.
- **Position des préfectures** : [GeoNames](https://www.geonames.org/), sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), via le paquet npm `cities.json`.
- **Polices** : Bricolage Grotesque, IBM Plex Sans et IBM Plex Mono, chargées depuis Google Fonts (licence SIL Open Font License).
- **Indices** (géographie, patrimoine, particularités des régions) : rédigés pour ce projet.

Ces crédits sont aussi affichés en bas de la page.
