"""Codage à plusieurs codeurs IA : découpage en unités, vote, arbitrage par l'évaluateur.

Usage :
  python codage_multiple.py segmenter <dossier des transcriptions .txt> <unites.json>
      Découpe chaque transcription en unités : une unité = une réponse de la personne interrogée
      (ligne qui commence par « E05 : » ou « I02 : »). Identifiants : E05-R1, E05-R2...
  python codage_multiple.py vote <unites.json> <codeur_A.json> <codeur_B.json> [<codeur_C.json>...]
                               --cas <cas.json> --sortie <codage-consolide.json> --arbitrage <arbitrage.xlsx>
      Retient un code sur une unité quand la majorité des codeurs l'y a posé. Écrit le codage consolidé
      (format habituel, utilisable par codage.py et verifier_citations.py) et la liste des désaccords
      à arbitrer par l'évaluateur.
  python codage_multiple.py arbitrer <codage-consolide.json> <arbitrage.xlsx>
      Applique les décisions de l'évaluateur (colonne « Décision » : garder ou retirer).

Format d'un codeur : {"codeur": "B (Opus)", "unites": {"E05-R1": ["DEPENDANCE_TIERS"], "E05-R2": []}}
Une unité absente du fichier d'un codeur compte comme « aucun code ».
cas.json : {"cas": [{"id": "E05", "attributs": {...}}]} (la partie « cas » d'un codage habituel).
"""
import argparse
import itertools
import json
import pathlib
import re
import sys
from collections import defaultdict

import pandas as pd


def charger(chemin):
    return json.load(open(chemin, encoding="utf-8"))


def segmenter(dossier, sortie):
    unites = []
    for fichier in sorted(pathlib.Path(dossier).glob("*.txt")):
        cas = fichier.stem
        n = 0
        for ligne in fichier.read_text(encoding="utf-8").splitlines():
            m = re.match(rf"^{re.escape(cas)}\s*:\s*(.+)$", ligne.strip())
            if m:
                n += 1
                unites.append({"id": f"{cas}-R{n}", "cas": cas, "texte": m.group(1).strip()})
    json.dump(unites, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{len(unites)} unités dans {len({u['cas'] for u in unites})} transcriptions : {sortie}")


def kappa(x, y):
    n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    pa, pb = sum(x) / n, sum(y) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return None if pe == 1 else (po - pe) / (1 - pe)


def vote(chemin_unites, chemins_codeurs, chemin_cas, sortie, chemin_arbitrage):
    unites = charger(chemin_unites)
    codeurs = [charger(c) for c in chemins_codeurs]
    noms = [c.get("codeur", f"codeur {i + 1}") for i, c in enumerate(codeurs)]
    seuil = len(codeurs) // 2 + 1
    codes = sorted({code for c in codeurs for liste in c["unites"].values() for code in liste})
    inconnues = sorted({u for c in codeurs for u in c["unites"]} - {u["id"] for u in unites})
    if inconnues:
        print("ATTENTION, unités inconnues ignorées : " + ", ".join(inconnues[:10]))

    segments, desaccords, stats = [], [], []
    for u in unites:
        votes = {code: [code in c["unites"].get(u["id"], []) for c in codeurs] for code in codes}
        retenus = [code for code, v in votes.items() if sum(v) >= seuil]
        for code, v in votes.items():
            if 0 < sum(v) < len(codeurs):
                desaccords.append({"Unité": u["id"], "Cas": u["cas"], "Code": code,
                                   **{nom: "oui" if x else "" for nom, x in zip(noms, v)},
                                   "Votes": f"{sum(v)} sur {len(codeurs)}",
                                   "Retenu par la majorité": "oui" if sum(v) >= seuil else "non",
                                   "Texte": u["texte"], "Décision (garder / retirer)": ""})
        if retenus:
            accords = [f"{code} {sum(votes[code])}/{len(codeurs)}" for code in retenus]
            segments.append({"cas": u["cas"], "unite": u["id"], "codes": retenus, "citation": u["texte"],
                             "memo": "Vote : " + ", ".join(accords)})

    for code in codes:
        vecteurs = [[code in c["unites"].get(u["id"], []) for u in unites] for c in codeurs]
        ks = [kappa(a, b) for a, b in itertools.combinations(vecteurs, 2)]
        ks = [k for k in ks if k is not None]
        unanimes = sum(1 for i in range(len(unites)) if len({v[i] for v in vecteurs}) == 1 and vecteurs[0][i])
        stats.append({"Code": code, "Kappa moyen entre paires": round(sum(ks) / len(ks), 2) + 0.0 if ks else None,
                      "Unités codées à l'unanimité": unanimes,
                      "Désaccords": sum(1 for d in desaccords if d["Code"] == code)})

    cas = charger(chemin_cas)["cas"] if chemin_cas else [{"id": c} for c in sorted({u["cas"] for u in unites})]
    json.dump({"cas": cas, "segments": segments, "codeurs": noms}, open(sortie, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    tab = pd.DataFrame(stats)
    with pd.ExcelWriter(chemin_arbitrage) as w:
        pd.DataFrame(desaccords).to_excel(w, sheet_name="À arbitrer", index=False)
        tab.to_excel(w, sheet_name="Accord par code", index=False)
    print(f"{len(codeurs)} codeurs ({', '.join(noms)}), {len(unites)} unités, {len(segments)} unités codées "
          f"après vote (code retenu s'il a au moins {seuil} voix).")
    print(tab.to_string(index=False))
    print(f"{len(desaccords)} désaccords à arbitrer par l'évaluateur : {chemin_arbitrage}")
    for ligne in stats:
        if ligne["Kappa moyen entre paires"] is not None and ligne["Kappa moyen entre paires"] < 0.6:
            print(f"ALERTE : {ligne['Code']}, kappa moyen {ligne['Kappa moyen entre paires']:.2f}. "
                  "La définition est sans doute ambiguë : la revoir avec l'évaluateur.")


def arbitrer(chemin_codage, chemin_arbitrage):
    codage = charger(chemin_codage)
    decisions = pd.read_excel(chemin_arbitrage, sheet_name="À arbitrer")
    colonne = "Décision (garder / retirer)"
    faites = decisions[decisions[colonne].astype(str).str.strip().str.lower().isin(["garder", "retirer"])]
    par_unite = {s["unite"]: s for s in codage["segments"]}
    textes = dict(zip(decisions["Unité"], decisions["Texte"]))
    for _, d in faites.iterrows():
        unite, code, garder = d["Unité"], d["Code"], d[colonne].strip().lower() == "garder"
        seg = par_unite.get(unite)
        if garder and seg is None:
            seg = {"cas": d["Cas"], "unite": unite, "codes": [], "citation": textes[unite], "memo": ""}
            codage["segments"].append(seg)
            par_unite[unite] = seg
        if seg is None:
            continue
        if garder and code not in seg["codes"]:
            seg["codes"].append(code)
        if not garder and code in seg["codes"]:
            seg["codes"].remove(code)
        seg["memo"] = (seg.get("memo", "") + f" ; arbitrage évaluateur : {code} {'gardé' if garder else 'retiré'}").strip(" ;")
    codage["segments"] = [s for s in codage["segments"] if s["codes"]]
    json.dump(codage, open(chemin_codage, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{len(faites)} décisions appliquées sur {len(decisions)} désaccords. "
          f"Restent {len(decisions) - len(faites)} désaccords non arbitrés (la majorité s'applique).")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser()
    sous = p.add_subparsers(dest="commande", required=True)
    s = sous.add_parser("segmenter")
    s.add_argument("dossier")
    s.add_argument("sortie")
    s = sous.add_parser("vote")
    s.add_argument("unites")
    s.add_argument("codeurs", nargs="+")
    s.add_argument("--cas")
    s.add_argument("--sortie", required=True)
    s.add_argument("--arbitrage", required=True)
    s = sous.add_parser("arbitrer")
    s.add_argument("codage")
    s.add_argument("arbitrage")
    x = p.parse_args()
    if x.commande == "segmenter":
        segmenter(x.dossier, x.sortie)
    elif x.commande == "vote":
        vote(x.unites, x.codeurs, x.cas, x.sortie, x.arbitrage)
    else:
        arbitrer(x.codage, x.arbitrage)


if __name__ == "__main__":
    main()
