"""Extrait le texte brut de transcriptions (.docx, .txt, .md) vers des fichiers .txt.

Usage :
  python extraire_texte.py <fichier ou dossier> <dossier de sortie> [--decouper "<regex>"]

--decouper : expression régulière qui repère le début de chaque entretien quand un même
fichier en contient plusieurs. Le premier groupe capturé donne le nom du fichier
(ex. "^Entretien (E\\d+)" produit E01.txt, E05.txt...).
Le texte est écrit tel quel, en UTF-8 : c'est la référence des positions de citation.
"""
import argparse
import pathlib
import re
import sys


def lire(chemin):
    if chemin.suffix.lower() == ".docx":
        import docx

        return "\n".join(p.text for p in docx.Document(str(chemin)).paragraphs)
    return chemin.read_text(encoding="utf-8")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("entree")
    parser.add_argument("sortie")
    parser.add_argument("--decouper")
    args = parser.parse_args()

    entree, sortie = pathlib.Path(args.entree), pathlib.Path(args.sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    fichiers = sorted(p for p in entree.iterdir() if p.suffix.lower() in (".docx", ".txt", ".md")) if entree.is_dir() else [entree]

    for fichier in fichiers:
        texte = lire(fichier)
        if not args.decouper:
            cible = sortie / (fichier.stem + ".txt")
            cible.write_text(texte.strip() + "\n", encoding="utf-8")
            print(f"{cible.name} : {len(texte)} caractères")
            continue
        motif = re.compile(args.decouper, re.MULTILINE)
        debuts = list(motif.finditer(texte))
        if not debuts:
            print(f"ATTENTION : aucun entretien repéré dans {fichier.name} avec {args.decouper}")
            continue
        for i, m in enumerate(debuts):
            fin = debuts[i + 1].start() if i + 1 < len(debuts) else len(texte)
            nom = m.group(1) if m.groups() else f"{fichier.stem}_{i + 1}"
            cible = sortie / f"{nom}.txt"
            cible.write_text(texte[m.start():fin].strip() + "\n", encoding="utf-8")
            print(f"{cible.name} : {fin - m.start()} caractères")


if __name__ == "__main__":
    main()
