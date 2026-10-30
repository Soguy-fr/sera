"""Applique une table de pseudonymes à des fichiers, puis vérifie qu'aucun original ne subsiste.

Usage :
  python pseudonymiser.py appliquer <table.csv> <fichier ou dossier> <dossier de sortie>
  python pseudonymiser.py verifier <table.csv> <fichier ou dossier>

table.csv (UTF-8, séparateur virgule) : colonnes original, remplacement, type
  ex. « Aïcha Dossou,[Participante E05],nom » ou « Akpakpa,[quartier A],lieu »
Formats traités : .txt, .md, .csv, .xlsx (toutes les cellules texte), .docx (converti en .txt).
Le remplacement ignore la casse et les accents, et ne touche que des mots entiers.
Les originaux les plus longs sont remplacés d'abord (« Aïcha Dossou » avant « Aïcha »).
Code de sortie de verifier : 0 si aucun original trouvé, 1 sinon.
"""
import csv
import pathlib
import re
import sys
import unicodedata

FORMATS = (".txt", ".md", ".csv", ".xlsx", ".docx")


def sans_accents(texte):
    return "".join(c for c in unicodedata.normalize("NFD", texte) if unicodedata.category(c) != "Mn")


def charger_table(chemin):
    with open(chemin, encoding="utf-8-sig", newline="") as f:
        lignes = [l for l in csv.DictReader(f) if l.get("original", "").strip()]
    return sorted(lignes, key=lambda l: -len(l["original"]))


def motif(original):
    """Expression qui reconnaît l'original, quels que soient la casse et les accents."""
    morceaux = []
    for c in sans_accents(original):
        if c.isspace():
            morceaux.append(r"\s+")
            continue
        variantes = {c.lower(), c.upper()}
        variantes |= {v for v in "àâäáãåèéêëìíîïòóôöõùúûüçñÀÂÄÁÃÅÈÉÊËÌÍÎÏÒÓÔÖÕÙÚÛÜÇÑ" if sans_accents(v).lower() == c.lower()}
        morceaux.append("[" + "".join(re.escape(v) for v in sorted(variantes)) + "]" if c.isalpha() else re.escape(c))
    return re.compile(r"(?<!\w)" + "".join(morceaux) + r"(?!\w)")


def remplacer(texte, table, compteur):
    for l in table:
        texte, n = motif(l["original"]).subn(l["remplacement"], texte)
        compteur[l["original"]] = compteur.get(l["original"], 0) + n
    return texte


def fichiers(entree):
    entree = pathlib.Path(entree)
    if entree.is_file():
        return [entree]
    return sorted(p for p in entree.rglob("*") if p.suffix.lower() in FORMATS)


def lire_texte(chemin):
    if chemin.suffix.lower() == ".docx":
        import docx

        doc = docx.Document(str(chemin))
        return "\n".join([p.text for p in doc.paragraphs] + [c.text for t in doc.tables for r in t.rows for c in r.cells])
    if chemin.suffix.lower() == ".xlsx":
        from openpyxl import load_workbook

        wb = load_workbook(chemin)
        return "\n".join(str(c.value) for ws in wb for row in ws.iter_rows() for c in row if isinstance(c.value, str))
    return chemin.read_text(encoding="utf-8")


def appliquer(table_csv, entree, sortie):
    table = charger_table(table_csv)
    sortie = pathlib.Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    compteur = {}
    for f in fichiers(entree):
        if f.suffix.lower() == ".xlsx":
            from openpyxl import load_workbook

            wb = load_workbook(f)
            for ws in wb:
                for row in ws.iter_rows():
                    for c in row:
                        if isinstance(c.value, str):
                            c.value = remplacer(c.value, table, compteur)
            cible = sortie / f.name
            wb.save(cible)
        else:
            cible = sortie / (f.stem + (".txt" if f.suffix.lower() == ".docx" else f.suffix))
            cible.write_text(remplacer(lire_texte(f), table, compteur), encoding="utf-8")
        print(f"{f.name} -> {cible}")
    print("\nRemplacements effectués :")
    for l in table:
        print(f"  {l['original']} -> {l['remplacement']} : {compteur.get(l['original'], 0)}")
    absents = [o for o, n in compteur.items() if n == 0]
    if absents:
        print("ATTENTION, originaux jamais trouvés (orthographe à vérifier) : " + ", ".join(absents))


def verifier(table_csv, entree):
    table = charger_table(table_csv)
    restes = 0
    for f in fichiers(entree):
        texte = lire_texte(f)
        for l in table:
            for m in motif(l["original"]).finditer(texte):
                restes += 1
                contexte = texte[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
                print(f"RESTE [{f.name}] « {l['original']} » : ...{contexte}...")
    print("Aucun original trouvé." if not restes else f"{restes} occurrence(s) d'originaux trouvée(s).")
    return 1 if restes else 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 4 or sys.argv[1] not in ("appliquer", "verifier"):
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == "appliquer":
        appliquer(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit(verifier(sys.argv[2], sys.argv[3]))


if __name__ == "__main__":
    main()
