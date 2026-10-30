"""Crée un dossier d'évaluation SERA : sous-dossiers et etat.md.

Usage : python init_dossier.py <chemin> --titre "<titre de l'évaluation>"
Ne remplace jamais un etat.md existant.
"""
import argparse
import datetime
import pathlib
import sys

SOUS_DOSSIERS = ["sources", "donnees", "analyses", "livrables"]

ETAPES = [
    "1. Cadrage des TDR",
    "2. Théorie du changement et évaluabilité",
    "3. Questions et matrice d'évaluation",
    "4. Échantillonnage et outils de collecte",
    "5. Collecte et préparation des données",
    "6. Analyse quantitative",
    "7. Analyse qualitative",
    "8. Triangulation et synthèse",
    "9. Rapport et recommandations",
    "10. Restitution et diffusion",
]

MODELE = """# État de l'évaluation : {titre}

mode_pedagogique: non
mode_grill: approfondi
profil_modeles: a choisir
annonces: oui
confidentialite_verifiee: non
etape_courante: 1

## Avancement

| Étape | Statut | Livrable |
|---|---|---|
{lignes}

## Exigences des TDR

| Id | Exigence | Source | Étape | Statut |
|---|---|---|---|---|
| | (à remplir dès que les TDR sont déposés) | | | non couverte |

## Contexte

- Commanditaire : à renseigner (étape 1)
- Objet évalué : à renseigner
- Période et zone : à renseigner
- Type d'évaluation : à renseigner
- Budget et délais : à renseigner

## Décisions

- {date} : création du dossier d'évaluation.

## Points en attente

- Déposer les TDR dans `sources/`.
"""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("chemin")
    parser.add_argument("--titre", required=True)
    args = parser.parse_args()

    racine = pathlib.Path(args.chemin)
    etat = racine / "etat.md"
    if etat.exists():
        print(f"etat.md existe déjà dans {racine} : rien n'a été modifié.")
        sys.exit(1)

    for nom in SOUS_DOSSIERS:
        (racine / nom).mkdir(parents=True, exist_ok=True)

    lignes = "\n".join(f"| {e} | à faire | |" for e in ETAPES)
    etat.write_text(
        MODELE.format(titre=args.titre, lignes=lignes, date=datetime.date.today().isoformat()),
        encoding="utf-8",
    )
    print(f"Dossier d'évaluation créé : {racine.resolve()}")
    for nom in SOUS_DOSSIERS:
        print(f"  {nom}/")
    print("  etat.md")


if __name__ == "__main__":
    main()
