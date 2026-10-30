"""Écrit, relit et vérifie la matrice d'évaluation SERA (fichier Excel pivot).

Usage :
  python matrice.py ecrire <matrice.json> <matrice-evaluation.xlsx>
  python matrice.py lire <matrice-evaluation.xlsx>            (affiche le JSON)
  python matrice.py verifier <matrice-evaluation.xlsx> [--criteres-attendus "Pertinence,Efficacité"]

Une ligne = un indicateur. L'identifiant Qn.m regroupe les lignes d'une même question n.
Code de sortie de verifier : 0 si aucune erreur (les alertes n'empêchent pas), 1 sinon.
"""
import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

# (clé JSON, en-tête Excel, largeur, obligatoire)
COLONNES = [
    ("id", "ID", 7, True),
    ("critere", "Critère", 14, True),
    ("question", "Question d'évaluation", 40, True),
    ("sous_question", "Sous-question / point d'appréciation", 40, False),
    ("indicateur", "Indicateur", 38, True),
    ("desagregation", "Désagrégation", 20, False),
    ("sources", "Sources de données", 30, True),
    ("collecte", "Méthode de collecte", 26, True),
    ("analyse", "Méthode d'analyse", 26, True),
    ("maillon_toc", "Maillon TOC / hypothèse", 14, False),
    ("remarques", "Remarques", 30, False),
]
CRITERES_CAD = ["Pertinence", "Cohérence", "Efficacité", "Efficience", "Impact", "Durabilité"]
CRITERES_AUTRES = ["Genre et inclusion", "Droits humains", "Apprentissage"]
COULEURS = {
    "Pertinence": "DCE6F0", "Cohérence": "E1D5E7", "Efficacité": "D5E8D4",
    "Efficience": "FFF2CC", "Impact": "F8CECC", "Durabilité": "FCE4D6",
}
MOTS_GENRE = ["sexe", "genre", "femme", "homme", "fille", "garçon", "handicap", "âge", "inclusion"]


def sans_accents(texte):
    return "".join(c for c in unicodedata.normalize("NFD", texte) if unicodedata.category(c) != "Mn").lower()


def ecrire(chemin_json, chemin_xlsx):
    lignes = json.load(open(chemin_json, encoding="utf-8"))
    wb = Workbook()
    ws = wb.active
    ws.title = "Matrice"
    bord = Border(*(Side(style="thin", color="999999"),) * 4)
    ws.append([c[1] for c in COLONNES])
    for cellule, (_, _, largeur, _) in zip(ws[1], COLONNES):
        cellule.font = Font(bold=True, color="FFFFFF")
        cellule.fill = PatternFill("solid", fgColor="1C2A39")
        cellule.alignment = Alignment(wrap_text=True, vertical="center")
        cellule.border = bord
        ws.column_dimensions[cellule.column_letter].width = largeur
    for ligne in lignes:
        ws.append([ligne.get(cle, "") for cle, *_ in COLONNES])
        couleur = COULEURS.get(ligne.get("critere", ""), "FFFFFF")
        for cellule in ws[ws.max_row]:
            cellule.alignment = Alignment(wrap_text=True, vertical="top")
            cellule.border = bord
            cellule.fill = PatternFill("solid", fgColor=couleur)
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = ws.dimensions

    aide = wb.create_sheet("Lisez-moi")
    aide.append(["Colonne", "Contenu attendu"])
    for cle, entete, _, obligatoire in COLONNES:
        aide.append([entete, ("Obligatoire. " if obligatoire else "") + AIDE[cle]])
    aide.column_dimensions["A"].width = 34
    aide.column_dimensions["B"].width = 100
    aide.append([])
    aide.append(["Règle", "Une ligne par indicateur. Les lignes Q1.1, Q1.2... appartiennent à la question Q1."])
    aide.append(["Source", "Critères : OCDE (2019), Des critères d'évaluation mieux adaptés pour de meilleures évaluations."])
    wb.save(chemin_xlsx)
    print(f"Matrice écrite : {chemin_xlsx} ({len(lignes)} lignes)")


AIDE = {
    "id": "Qn.m : n = numéro de la question, m = numéro de l'indicateur.",
    "critere": "Un critère CAD-OCDE (Pertinence, Cohérence, Efficacité, Efficience, Impact, Durabilité) ou un critère demandé par les TDR.",
    "question": "La question d'évaluation, ouverte, qui appelle un jugement.",
    "sous_question": "Ce qu'on regarde précisément pour répondre.",
    "indicateur": "Ce qu'on mesure ou observe. Formulé pour être mesurable.",
    "desagregation": "Par sexe, âge, handicap, zone, statut... selon les TDR.",
    "sources": "D'où vient l'information. Au moins deux sources distinctes par question, pour trianguler. Séparer par « ; ».",
    "collecte": "Comment l'information est recueillie (enquête, entretien, focus group, revue documentaire...).",
    "analyse": "Comment elle est traitée (statistiques descriptives, test, codage thématique, analyse de contribution...).",
    "maillon_toc": "Élément ou hypothèse de la théorie du changement testé (E1, H3...).",
    "remarques": "Limites, risques, points à clarifier.",
}


def lire(chemin_xlsx):
    ws = load_workbook(chemin_xlsx, data_only=True)["Matrice"]
    entetes = [c.value for c in ws[1]]
    cles = {entete: cle for cle, entete, *_ in COLONNES}
    lignes = []
    for ligne in ws.iter_rows(min_row=2, values_only=True):
        if all(v in (None, "") for v in ligne):
            continue
        lignes.append({cles.get(e, e): ("" if v is None else str(v).strip()) for e, v in zip(entetes, ligne)})
    return entetes, lignes


def verifier(chemin_xlsx, criteres_attendus):
    entetes, lignes = lire(chemin_xlsx)
    erreurs, alertes = [], []

    attendues = [c[1] for c in COLONNES]
    if entetes[: len(attendues)] != attendues:
        erreurs.append(f"En-têtes modifiés. Attendu : {attendues}")

    autorises = {sans_accents(c): c for c in CRITERES_CAD + CRITERES_AUTRES + criteres_attendus}
    vus, par_question = set(), defaultdict(list)
    for n, ligne in enumerate(lignes, start=2):
        ident = ligne.get("id", "")
        if not re.fullmatch(r"Q\d+\.\d+", ident):
            erreurs.append(f"Ligne {n} : ID « {ident} » invalide (format attendu Qn.m).")
        elif ident in vus:
            erreurs.append(f"Ligne {n} : ID {ident} en double.")
        vus.add(ident)
        for cle, entete, _, obligatoire in COLONNES:
            if obligatoire and not ligne.get(cle):
                erreurs.append(f"Ligne {n} ({ident}) : « {entete} » est vide.")
        if ligne.get("critere") and sans_accents(ligne["critere"]) not in autorises:
            alertes.append(f"Ligne {n} ({ident}) : critère « {ligne['critere']} » hors CAD-OCDE et non annoncé par --criteres-attendus.")
        if ident and "." in ident:
            par_question[ident.split(".")[0]].append(ligne)

    for q, lignes_q in par_question.items():
        questions = {l.get("question", "") for l in lignes_q}
        if len(questions) > 1:
            erreurs.append(f"{q} : les lignes n'ont pas le même texte de question.")
        sources = {s.strip().lower() for l in lignes_q for s in re.split(r"[;\n]", l.get("sources", "")) if s.strip()}
        if len(sources) < 2:
            alertes.append(f"{q} : une seule source de données, pas de triangulation possible.")

    presents = {sans_accents(l.get("critere", "")) for l in lignes}
    for c in criteres_attendus:
        if sans_accents(c) not in presents:
            erreurs.append(f"Critère demandé par les TDR sans aucune question : {c}.")

    texte = sans_accents(" ".join(l.get("desagregation", "") + " " + l.get("indicateur", "") for l in lignes))
    if not any(sans_accents(m) in texte for m in MOTS_GENRE):
        alertes.append("Aucun indicateur ni désagrégation ne mentionne le sexe, le genre, l'âge ou le handicap.")

    print(f"Matrice : {len(par_question)} questions, {len(lignes)} indicateurs.")
    for e in erreurs:
        print(f"ERREUR : {e}")
    for a in alertes:
        print(f"ALERTE : {a}")
    if not erreurs and not alertes:
        print("Aucun problème détecté.")
    return 1 if erreurs else 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    sous = parser.add_subparsers(dest="commande", required=True)
    p = sous.add_parser("ecrire")
    p.add_argument("json")
    p.add_argument("xlsx")
    p = sous.add_parser("lire")
    p.add_argument("xlsx")
    p = sous.add_parser("verifier")
    p.add_argument("xlsx")
    p.add_argument("--criteres-attendus", default="")
    args = parser.parse_args()

    if args.commande == "ecrire":
        ecrire(args.json, args.xlsx)
    elif args.commande == "lire":
        print(json.dumps(lire(args.xlsx)[1], ensure_ascii=False, indent=2))
    else:
        attendus = [c.strip() for c in args.criteres_attendus.split(",") if c.strip()]
        sys.exit(verifier(args.xlsx, attendus))


if __name__ == "__main__":
    main()
