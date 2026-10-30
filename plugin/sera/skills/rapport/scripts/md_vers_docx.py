"""Convertit un document Markdown simple en Word (.docx).

Usage : python md_vers_docx.py <document.md> <document.docx> [--pied "texte du pied de page"]

Éléments reconnus : titres (#, ##, ###), paragraphes, listes à puces (-) et numérotées (1.),
tableaux Markdown (| a | b |), gras (**texte**), italique (*texte*), images seules sur une ligne
(![légende](chemin)), saut de page (une ligne contenant seulement \\pagebreak).
Les chemins d'images sont relatifs au fichier Markdown.
"""
import argparse
import pathlib
import re
import sys

from docx import Document
from docx.shared import Cm, Pt

INLINE = re.compile(r"(\*\*.+?\*\*|\*.+?\*|`.+?`)")


def ajouter_texte(paragraphe, texte):
    for morceau in INLINE.split(texte):
        if not morceau:
            continue
        if morceau.startswith("**") and morceau.endswith("**"):
            paragraphe.add_run(morceau[2:-2]).bold = True
        elif morceau.startswith("*") and morceau.endswith("*") and len(morceau) > 2:
            paragraphe.add_run(morceau[1:-1]).italic = True
        elif morceau.startswith("`") and morceau.endswith("`") and len(morceau) > 2:
            paragraphe.add_run(morceau[1:-1]).font.name = "Consolas"
        else:
            paragraphe.add_run(morceau)


def cellules(ligne):
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    a = argparse.ArgumentParser()
    a.add_argument("md")
    a.add_argument("docx")
    a.add_argument("--pied", default="")
    x = a.parse_args()

    source = pathlib.Path(x.md)
    lignes = source.read_text(encoding="utf-8").splitlines()
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    if x.pied:
        doc.sections[0].footer.paragraphs[0].text = x.pied

    i = 0
    while i < len(lignes):
        ligne = lignes[i].rstrip()
        if not ligne.strip():
            i += 1
            continue
        if ligne.strip() == "\\pagebreak":
            doc.add_page_break()
        elif m := re.match(r"^(#{1,4})\s+(.*)", ligne):
            doc.add_heading(m.group(2).replace("**", ""), level=len(m.group(1)) - 1 if len(m.group(1)) > 1 else 0)
        elif m := re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", ligne):
            image = (source.parent / m.group(2)).resolve()
            if image.exists():
                doc.add_picture(str(image), width=Cm(16))
                if m.group(1):
                    doc.add_paragraph().add_run(m.group(1)).italic = True
            else:
                doc.add_paragraph(f"[image introuvable : {m.group(2)}]")
        elif ligne.lstrip().startswith("|"):
            bloc = []
            while i < len(lignes) and lignes[i].lstrip().startswith("|"):
                bloc.append(cellules(lignes[i]))
                i += 1
            bloc = [b for b in bloc if not all(re.fullmatch(r":?-{2,}:?", c) for c in b if c)]
            n_col = max(len(b) for b in bloc)
            table = doc.add_table(rows=len(bloc), cols=n_col)
            table.style = "Table Grid"
            table.autofit = False
            # Largeur de chaque colonne proportionnelle à son texte le plus long (bornée)
            poids = [min(60, max(10, len(bloc[0][c]) + 2 if c < len(bloc[0]) else 0, max(len(b[c]) if c < len(b) else 0 for b in bloc))) for c in range(n_col)]
            largeurs = [Cm(16 * w / sum(poids)) for w in poids]
            for colonne, largeur in zip(table.columns, largeurs):
                colonne.width = largeur
            for r, b in enumerate(bloc):
                for c, texte in enumerate(b):
                    table.cell(r, c).width = largeurs[c]
                    p = table.cell(r, c).paragraphs[0]
                    ajouter_texte(p, texte)
                    if r == 0:
                        for run in p.runs:
                            run.bold = True
            doc.add_paragraph()
            continue
        elif m := re.match(r"^\s*[-*]\s+(.*)", ligne):
            ajouter_texte(doc.add_paragraph(style="List Bullet"), m.group(1))
        elif m := re.match(r"^\s*\d+[.)]\s+(.*)", ligne):
            ajouter_texte(doc.add_paragraph(style="List Number"), m.group(1))
        elif ligne.startswith(">"):
            p = doc.add_paragraph(style="Intense Quote")
            ajouter_texte(p, ligne.lstrip("> "))
        else:
            texte = [ligne.strip()]
            while i + 1 < len(lignes) and lignes[i + 1].strip() and not re.match(r"^(#|\||[-*]\s|\d+[.)]\s|>|!\[)", lignes[i + 1].lstrip()):
                i += 1
                texte.append(lignes[i].strip())
            ajouter_texte(doc.add_paragraph(), " ".join(texte))
        i += 1

    doc.save(x.docx)
    print(f"Document Word écrit : {x.docx}")


if __name__ == "__main__":
    main()
