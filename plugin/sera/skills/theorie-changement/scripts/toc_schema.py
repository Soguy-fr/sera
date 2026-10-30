"""Dessine le schéma d'une théorie du changement à partir d'un JSON.

Usage : python toc_schema.py <toc.json> <sortie.png>
Format du JSON : voir SKILL.md de theorie-changement.
Les niveaux sont des colonnes de gauche à droite. Chaque lien est une flèche
qui porte l'identifiant de son hypothèse.
"""
import json
import sys
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

COULEURS = ["#DCE6F0", "#D5E8D4", "#FFF2CC", "#F8CECC", "#E1D5E7", "#FCE4D6"]
LARGEUR_BOITE = 2.6
ECART_COLONNE = 1.4
HAUTEUR_LIGNE = 0.22


def hauteur_boite(lignes):
    return max(0.7, 0.25 + HAUTEUR_LIGNE * lignes)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    toc = json.load(open(sys.argv[1], encoding="utf-8"))
    sortie = sys.argv[2]
    niveaux = toc["niveaux"]

    # Prépare les textes et la hauteur de chaque colonne
    colonnes = []
    for niveau in niveaux:
        boites = []
        for el in niveau["elements"]:
            lignes = textwrap.wrap(f"{el['id']}. {el['texte']}", 30)
            boites.append({"id": el["id"], "lignes": lignes, "h": hauteur_boite(len(lignes))})
        colonnes.append(boites)
    hauteur_schema = max(sum(b["h"] for b in col) + 0.35 * (len(col) - 1) for col in colonnes)

    hyps = toc.get("hypotheses", [])
    externes = toc.get("facteurs_externes", [])
    texte_bas = ["Hypothèses"] + [
        l for h in hyps for l in textwrap.wrap(f"{h['id']} : {h['texte']}", 150)
    ]
    if externes:
        texte_bas += ["", "Facteurs externes"] + [
            l for f in externes for l in textwrap.wrap(f"- {f}", 150)
        ]
    hauteur_bas = 0.24 * len(texte_bas) + 0.4

    largeur = len(niveaux) * LARGEUR_BOITE + (len(niveaux) - 1) * ECART_COLONNE
    hauteur = hauteur_schema + 1.0 + hauteur_bas
    fig, ax = plt.subplots(figsize=(largeur + 0.6, hauteur + 0.6))
    ax.set_xlim(-0.3, largeur + 0.3)
    ax.set_ylim(-hauteur_bas - 0.3, hauteur_schema + 1.0)
    ax.axis("off")
    ax.text(largeur / 2, hauteur_schema + 0.75, toc.get("titre", ""), ha="center",
            va="center", fontsize=14, weight="bold")

    positions = {}
    for i, (niveau, boites) in enumerate(zip(niveaux, colonnes)):
        x = i * (LARGEUR_BOITE + ECART_COLONNE)
        ax.text(x + LARGEUR_BOITE / 2, hauteur_schema + 0.3, niveau["nom"], ha="center",
                va="center", fontsize=12, weight="bold", color="#1C2A39")
        total = sum(b["h"] for b in boites) + 0.35 * (len(boites) - 1)
        y = hauteur_schema - (hauteur_schema - total) / 2
        for b in boites:
            y_bas = y - b["h"]
            ax.add_patch(FancyBboxPatch((x, y_bas), LARGEUR_BOITE, b["h"],
                                        boxstyle="round,pad=0.02,rounding_size=0.08",
                                        fc=COULEURS[i % len(COULEURS)], ec="#555555", lw=1))
            ax.text(x + LARGEUR_BOITE / 2, y_bas + b["h"] / 2, "\n".join(b["lignes"]),
                    ha="center", va="center", fontsize=8.5)
            positions[b["id"]] = (x, y_bas + b["h"] / 2)
            y = y_bas - 0.35

    inconnus = []
    for lien in toc.get("liens", []):
        source, cible = lien[0], lien[1]
        if source not in positions or cible not in positions:
            inconnus.append(f"{source} -> {cible}")
            continue
        (x1, y1), (x2, y2) = positions[source], positions[cible]
        if x1 == x2:
            # Lien dans une même colonne : arc qui contourne les boîtes par la droite
            debut, fin = (x1 + LARGEUR_BOITE, y1), (x2 + LARGEUR_BOITE, y2)
            style = "arc3,rad=-0.6" if y2 < y1 else "arc3,rad=0.6"
            milieu = (x1 + LARGEUR_BOITE + 0.3 * abs(y1 - y2), (y1 + y2) / 2)
        else:
            debut, fin = (x1 + LARGEUR_BOITE, y1), (x2, y2)
            style = "arc3,rad=0"
            milieu = ((debut[0] + fin[0]) / 2, (debut[1] + fin[1]) / 2)
        ax.add_patch(FancyArrowPatch(debut, fin, arrowstyle="-|>", mutation_scale=12, connectionstyle=style,
                                     color="#444444", lw=1, shrinkA=2, shrinkB=2))
        if len(lien) > 2 and lien[2]:
            ax.text(milieu[0], milieu[1], lien[2], fontsize=7.5,
                    ha="center", va="center", color="#A8532A", weight="bold",
                    bbox=dict(fc="white", ec="none", pad=0.5))

    y = -0.2
    for ligne in texte_bas:
        gras = ligne in ("Hypothèses", "Facteurs externes")
        ax.text(0, y, ligne, fontsize=9 if gras else 8, weight="bold" if gras else "normal",
                va="top")
        y -= 0.24

    fig.savefig(sortie, dpi=160, bbox_inches="tight")
    print(f"Schéma enregistré : {sortie}")
    if inconnus:
        print("ATTENTION, liens vers des identifiants inconnus : " + ", ".join(inconnus))
        sys.exit(1)


if __name__ == "__main__":
    main()
