"""Tableaux d'analyse qualitative et accord entre codeurs.

Usage :
  python codage.py tableaux <codage.json> <livre-de-codes.json> <sortie.xlsx>
  python codage.py accord <codage_A.json> <codage_B.json> [--sortie accord.xlsx]
  python codage.py compter <codage.json> --code CODE [--code AUTRE] [--filtre attribut=valeur]

codage.json :
  {"cas": [{"id": "E01", "attributs": {"sexe": "Femme", "age": "25-34"}}],
   "segments": [{"cas": "E01", "codes": ["GAIN_TEMPS"], "citation": "...", "memo": "..."}]}
livre-de-codes.json :
  [{"code": "GAIN_TEMPS", "definition": "...", "inclure": "...", "exclure": "...",
    "exemple": "...", "question": "Q2"}]

L'accord est calculé sur la présence de chaque code dans chaque cas (code présent ou absent
dans l'entretien) : kappa de Cohen, accord sur les présences 2a / (2a + b + c), et accord brut.
Une ALERTE est levée pour chaque code dont le kappa est inférieur à 0,6.
compter donne le « n sur N » d'un ou plusieurs codes, avec la liste des cas : c'est la seule
source autorisée pour un décompte qualitatif dans un livrable.
"""
import argparse
import itertools
import json
import sys
from collections import Counter, defaultdict

import pandas as pd


def charger(chemin):
    return json.load(open(chemin, encoding="utf-8"))


def presence(codage):
    cas = [c["id"] for c in codage["cas"]]
    pres = defaultdict(set)
    for s in codage["segments"]:
        for code in s["codes"]:
            pres[code].add(s["cas"])
    return cas, pres


def tableaux(chemin_codage, chemin_livre, sortie):
    codage, livre = charger(chemin_codage), charger(chemin_livre)
    connus = {c["code"] for c in livre}
    inconnus = sorted({code for s in codage["segments"] for code in s["codes"]} - connus)
    if inconnus:
        print("ERREUR : codes absents du livre de codes : " + ", ".join(inconnus))
        sys.exit(1)

    attributs = {c["id"]: c.get("attributs", {}) for c in codage["cas"]}
    noms_attr = sorted({k for a in attributs.values() for k in a})
    lignes = []
    for s in codage["segments"]:
        for code in s["codes"]:
            lignes.append({"Cas": s["cas"], **{a: attributs.get(s["cas"], {}).get(a, "") for a in noms_attr},
                           "Code": code, "Citation": s["citation"], "Mémo": s.get("memo", ""),
                           "Début": s.get("debut"), "Fin": s.get("fin")})
    segments = pd.DataFrame(lignes)
    cas_ids = [c["id"] for c in codage["cas"]]

    # Code x cas : nombre de segments
    code_cas = (segments.pivot_table(index="Code", columns="Cas", values="Citation", aggfunc="count", fill_value=0)
                .reindex(index=[c["code"] for c in livre], columns=cas_ids, fill_value=0))
    code_cas["Total segments"] = code_cas[cas_ids].sum(axis=1)
    code_cas["Nb cas"] = (code_cas[cas_ids] > 0).sum(axis=1)

    # Code x attribut : nombre de cas concernés, par modalité
    profils = []
    for attr in noms_attr:
        t = (segments.drop_duplicates(["Code", "Cas"]).groupby(["Code", attr]).size().unstack(fill_value=0))
        effectifs = Counter(a.get(attr, "") for a in attributs.values())
        t.columns = [f"{attr} = {m} (sur {effectifs[m]})" for m in t.columns]
        profils.append(t)
    profil = pd.concat(profils, axis=1).fillna(0).astype(int) if profils else pd.DataFrame()

    # Co-occurrences : nombre de cas où deux codes apparaissent ensemble
    _, pres = presence(codage)
    cooc = Counter()
    for a, b in itertools.combinations(sorted(pres), 2):
        n = len(pres[a] & pres[b])
        if n:
            cooc[(a, b)] = n
    cooc_df = pd.DataFrame([{"Code A": a, "Code B": b, "Nb cas communs": n} for (a, b), n in cooc.most_common()])

    with pd.ExcelWriter(sortie) as w:
        pd.DataFrame(livre).to_excel(w, sheet_name="Livre de codes", index=False)
        segments.to_excel(w, sheet_name="Segments", index=False)
        code_cas.to_excel(w, sheet_name="Code x cas")
        if not profil.empty:
            profil.to_excel(w, sheet_name="Code x profil")
        cooc_df.to_excel(w, sheet_name="Co-occurrences", index=False)
    non_utilises = [c["code"] for c in livre if c["code"] not in pres]
    print(f"Tableaux écrits : {sortie} ({len(segments)} segments codés, {len(cas_ids)} cas)")
    print(code_cas[["Total segments", "Nb cas"]].to_string())
    if non_utilises:
        print("Codes jamais utilisés : " + ", ".join(non_utilises))


def kappa(x, y):
    n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    pa, pb = sum(x) / n, sum(y) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return po, (None if pe == 1 else (po - pe) / (1 - pe))


def accord(chemin_a, chemin_b, sortie):
    a, b = charger(chemin_a), charger(chemin_b)
    cas_a, pres_a = presence(a)
    cas_b, pres_b = presence(b)
    cas = sorted(set(cas_a) & set(cas_b))
    if not cas:
        print("ERREUR : aucun cas commun entre les deux codages.")
        sys.exit(1)
    lignes, desaccords, alertes = [], [], []
    for code in sorted(set(pres_a) | set(pres_b)):
        x = [c in pres_a.get(code, set()) for c in cas]
        y = [c in pres_b.get(code, set()) for c in cas]
        po, k = kappa(x, y)
        deux = sum(xa and yb for xa, yb in zip(x, y))
        un = sum(xa != yb for xa, yb in zip(x, y))
        presences = None if deux + un == 0 else round(100 * 2 * deux / (2 * deux + un), 1)
        lignes.append({"Code": code, "Kappa": None if k is None else round(k, 2) + 0.0,
                       "Accord sur les présences %": presences, "Accord brut %": round(100 * po, 1),
                       "Présent A": sum(x), "Présent B": sum(y)})
        if (k is None and (sum(x) or sum(y)) and sum(x) != sum(y)) or (k is not None and k < 0.6):
            alertes.append(f"ALERTE : {code}, kappa = {'non calculable' if k is None else f'{round(k, 2) + 0.0:.2f}'.replace('.', ',')}. "
                           "Préciser la définition, puis faire recoder un nouvel entretien avant la production.")
        desaccords += [{"Code": code, "Cas": c, "Codeur A": "présent" if xa else "absent",
                        "Codeur B": "présent" if yb else "absent"} for c, xa, yb in zip(cas, x, y) if xa != yb]
    res = pd.DataFrame(lignes)
    print(f"Cas comparés : {len(cas)}. Le kappa corrige l'accord dû au hasard ; l'accord brut est gonflé "
          "par les cases « absent / absent », ne le présentez pas seul.")
    print(res.to_string(index=False))
    for alerte in alertes:
        print(alerte)
    if not alertes:
        print("Aucun code sous le seuil de kappa 0,6.")
    if sortie:
        with pd.ExcelWriter(sortie) as w:
            res.to_excel(w, sheet_name="Accord par code", index=False)
            pd.DataFrame(desaccords).to_excel(w, sheet_name="Désaccords", index=False)
        print(f"Détail écrit : {sortie}")
    return alertes


def compter(chemin, codes, filtres):
    """Nombre de cas où au moins un des codes est présent, parmi les cas qui passent les filtres."""
    codage = charger(chemin)
    conditions = [f.split("=", 1) for f in filtres]
    cas = [c for c in codage["cas"]
           if all(str(c.get("attributs", {}).get(cle, "")).lower() == valeur.lower() for cle, valeur in conditions)]
    ids = [c["id"] for c in cas]
    connus = {code for s in codage["segments"] for code in s["codes"]}
    inconnus = [code for code in codes if code not in connus]
    if inconnus:
        print("ATTENTION, codes jamais utilisés dans ce codage : " + ", ".join(inconnus))
    presents = sorted({s["cas"] for s in codage["segments"] if s["cas"] in ids and set(codes) & set(s["codes"])})
    absents = [i for i in ids if i not in presents]
    filtre = f" ({', '.join(filtres)})" if filtres else ""
    print(f"{' ou '.join(codes)} : {len(presents)} cas sur {len(ids)}{filtre} : {', '.join(presents) or 'aucun'}. "
          f"Absent : {', '.join(absents) or 'aucun'}.")
    return len(presents), len(ids)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    sous = parser.add_subparsers(dest="commande", required=True)
    p = sous.add_parser("tableaux")
    p.add_argument("codage")
    p.add_argument("livre")
    p.add_argument("sortie")
    p = sous.add_parser("accord")
    p.add_argument("a")
    p.add_argument("b")
    p.add_argument("--sortie")
    p = sous.add_parser("compter")
    p.add_argument("codage")
    p.add_argument("--code", action="append", required=True)
    p.add_argument("--filtre", action="append", default=[], help="attribut=valeur, par exemple type=Institution")
    args = parser.parse_args()
    if args.commande == "tableaux":
        tableaux(args.codage, args.livre, args.sortie)
    elif args.commande == "accord":
        accord(args.a, args.b, args.sortie)
    else:
        compter(args.codage, args.code, args.filtre)


if __name__ == "__main__":
    main()
