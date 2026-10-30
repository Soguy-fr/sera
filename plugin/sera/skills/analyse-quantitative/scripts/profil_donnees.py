"""Diagnostic d'une base de données avant nettoyage.

Usage : python profil_donnees.py <base .xlsx/.csv> <sortie .md> [--feuille NOM] [--id COLONNE]

Produit un rapport Markdown : dimensions, type probable de chaque variable, valeurs manquantes,
doublons sur l'identifiant, modalités des variables catégorielles, valeurs atypiques
(règle de Tukey et |z| > 3) des variables numériques. Le rapport ne modifie pas la base.
"""
import argparse
import pathlib
import sys

import pandas as pd


def charger(chemin, feuille):
    chemin = pathlib.Path(chemin)
    if chemin.suffix.lower() == ".csv":
        return pd.read_csv(chemin, sep=None, engine="python")
    return pd.read_excel(chemin, sheet_name=feuille or 0)


def type_probable(s, n):
    valeurs = s.dropna()
    if valeurs.empty:
        return "vide"
    if str(s.name).lower().startswith("id") or (valeurs.nunique() == n and pd.api.types.is_integer_dtype(valeurs)):
        return "identifiant"
    if valeurs.nunique() == 2:
        return "binaire"
    if pd.api.types.is_numeric_dtype(valeurs):
        return "numérique" if valeurs.nunique() > 10 else "numérique discrète (à vérifier : catégorie codée ?)"
    return "catégorielle" if valeurs.nunique() <= 30 else "texte libre"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("base")
    parser.add_argument("sortie")
    parser.add_argument("--feuille")
    parser.add_argument("--id")
    args = parser.parse_args()

    df = charger(args.base, args.feuille)
    n = len(df)
    types = {c: type_probable(df[c], n) for c in df.columns}
    ident = args.id or next((c for c in df.columns if c.lower().startswith("id")), None)

    r = [f"# Profil de la base `{pathlib.Path(args.base).name}`", "",
         f"- **{n} lignes**, **{df.shape[1]} variables**",
         f"- Valeurs manquantes : **{int(df.isna().sum().sum())}** au total"]
    if ident:
        doublons = df[df[ident].duplicated(keep=False)]
        r.append(f"- Identifiant retenu : `{ident}` ; lignes en double sur cet identifiant : **{len(doublons)}**"
                 + (f" (identifiants : {', '.join(map(str, sorted(doublons[ident].unique())[:20]))})" if len(doublons) else ""))
        lignes_identiques = int(df.duplicated().sum())
        r.append(f"- Lignes entièrement identiques : **{lignes_identiques}**")
    else:
        r.append("- Aucun identifiant repéré : préciser la colonne avec --id")

    r += ["", "## Variables", "", "| Variable | Type probable | Manquants | Modalités / étendue |", "|---|---|---|---|"]
    for c in df.columns:
        s = df[c]
        manq = int(s.isna().sum())
        if pd.api.types.is_numeric_dtype(s) and types[c] not in ("binaire", "identifiant"):
            etendue = f"min {s.min():g} ; médiane {s.median():g} ; max {s.max():g}"
        else:
            vc = s.value_counts(dropna=True)
            etendue = " ; ".join(f"{k} ({v})" for k, v in vc.head(8).items()) + (" ; ..." if len(vc) > 8 else "")
        r.append(f"| `{c}` | {types[c]} | {manq} ({100 * manq / n:.1f} %) | {etendue} |")

    numeriques = [c for c in df.columns if types[c] == "numérique"]
    if numeriques:
        r += ["", "## Valeurs atypiques (variables numériques)", "",
              "| Variable | Tukey (hors [Q1 - 1,5 IQR ; Q3 + 1,5 IQR]) | |z| > 3 | Exemples de valeurs atypiques |",
              "|---|---|---|---|"]
        for c in numeriques:
            s = df[c].dropna()
            q1, q3 = s.quantile([0.25, 0.75])
            iqr = q3 - q1
            tukey = s[(s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)]
            z = s[((s - s.mean()) / s.std()).abs() > 3]
            exemples = ", ".join(f"{v:g}" for v in sorted(tukey.unique())[:6])
            r.append(f"| `{c}` | {len(tukey)} | {len(z)} | {exemples} |")
    r += ["", "Ce diagnostic signale des valeurs à examiner. Une valeur atypique n'est pas forcément une erreur :",
          "la décision de la corriger, de la garder ou de l'exclure revient à l'évaluateur."]

    pathlib.Path(args.sortie).write_text("\n".join(r) + "\n", encoding="utf-8")
    print("\n".join(r))


if __name__ == "__main__":
    main()
