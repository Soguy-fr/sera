"""Produit une présentation PowerPoint à partir d'un plan JSON.

Usage : python plan_vers_pptx.py <plan.json> <sortie.pptx> [--modele modele.pptx]

plan.json :
  {"titre": "...", "sous_titre": "...",
   "diapositives": [
     {"titre": "...", "points": ["...", "..."], "notes": "texte pour l'orateur"},
     {"titre": "...", "image": "chemin/vers/image.png", "notes": "..."}
   ]}
Les chemins d'images sont relatifs au fichier JSON. Avec --modele, les dispositions du modèle
(charte du commanditaire) sont utilisées : 0 pour la couverture, 1 pour titre + contenu.
"""
import argparse
import json
import pathlib
import sys

from pptx import Presentation
from pptx.util import Inches, Pt


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    a = argparse.ArgumentParser()
    a.add_argument("plan")
    a.add_argument("sortie")
    a.add_argument("--modele")
    x = a.parse_args()

    chemin = pathlib.Path(x.plan)
    plan = json.load(open(chemin, encoding="utf-8"))
    prs = Presentation(x.modele) if x.modele else Presentation()

    couverture = prs.slides.add_slide(prs.slide_layouts[0])
    couverture.shapes.title.text = plan.get("titre", "")
    if len(couverture.placeholders) > 1:
        couverture.placeholders[1].text = plan.get("sous_titre", "")

    for d in plan["diapositives"]:
        diapo = prs.slides.add_slide(prs.slide_layouts[1] if "points" in d else prs.slide_layouts[5])
        diapo.shapes.title.text = d.get("titre", "")
        diapo.shapes.title.text_frame.paragraphs[0].font.size = Pt(30)
        if "points" in d:
            corps = diapo.placeholders[1].text_frame
            corps.clear()
            for i, point in enumerate(d["points"]):
                p = corps.paragraphs[0] if i == 0 else corps.add_paragraph()
                p.text = point
                p.font.size = Pt(20)
        if "image" in d:
            image = chemin.parent / d["image"]
            titre = diapo.shapes.title
            haut = titre.top + titre.height + Inches(0.1)
            hauteur_max = prs.slide_height - haut - Inches(0.4)
            img = diapo.shapes.add_picture(str(image), Inches(0.5), haut, height=hauteur_max)
            if img.width > prs.slide_width - Inches(1):
                ratio = (prs.slide_width - Inches(1)) / img.width
                img.width, img.height = int(img.width * ratio), int(img.height * ratio)
        if d.get("notes"):
            diapo.notes_slide.notes_text_frame.text = d["notes"]

    prs.save(x.sortie)
    print(f"Présentation écrite : {x.sortie} ({len(prs.slides)} diapositives)")


if __name__ == "__main__":
    main()
