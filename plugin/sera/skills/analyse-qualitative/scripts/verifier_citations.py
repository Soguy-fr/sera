"""Vérifie que chaque citation existe mot pour mot dans sa transcription.

Deux usages :
  python verifier_citations.py codage <codage.json> <dossier des transcriptions .txt> [--ecrire]
      Vérifie chaque segment de codage.json ({"segments": [{"cas": "E01", "citation": "..."}]}).
      Avec --ecrire, ajoute "debut" et "fin" (positions en caractères) aux segments trouvés.
  python verifier_citations.py document <rapport .md/.txt/.docx> <dossier des transcriptions .txt>
      Vérifie toutes les citations au format « texte » (E01) d'un livrable.

La comparaison tolère seulement les différences d'espaces, d'apostrophes et de guillemets typographiques,
ainsi que des points de suspension [...] ou (...) marquant une coupure.
Code de sortie : 0 si toutes les citations sont trouvées, 1 sinon.
"""
import argparse
import difflib
import json
import pathlib
import re
import sys

EQUIVALENCES = str.maketrans({"’": "'", "‘": "'", "`": "'", "“": '"', "”": '"', "«": '"', "»": '"', " ": " ", " ": " "})
COUPURE = re.compile(r"\s*(?:\[\.\.\.\]|\(\.\.\.\)|\[…\]|\(…\)|…)\s*")


def normaliser(texte):
    """Renvoie le texte normalisé et, pour chaque caractère normalisé, sa position d'origine."""
    sortie, positions, espace = [], [], False
    for i, c in enumerate(texte.translate(EQUIVALENCES)):
        if c.isspace():
            if not espace and sortie:
                sortie.append(" ")
                positions.append(i)
            espace = True
            continue
        espace = False
        sortie.append(c)
        positions.append(i)
    return "".join(sortie).strip(), positions


def chercher(citation, texte):
    """Renvoie (debut, fin) dans le texte d'origine, ou None."""
    norm_texte, positions = normaliser(texte)
    morceaux = [normaliser(m)[0] for m in COUPURE.split(citation) if normaliser(m)[0]]
    if not morceaux:
        return None
    curseur, debut = 0, None
    for morceau in morceaux:
        trouve = norm_texte.find(morceau, curseur)
        if trouve < 0:
            return None
        if debut is None:
            debut = trouve
        curseur = trouve + len(morceau)
    return positions[debut], positions[curseur - 1] + 1


def suggestion(citation, texte):
    """Passage du texte, de même longueur en mots, le plus ressemblant à la citation."""
    mots, cible = texte.split(), citation.split()
    n = len(cible)
    meilleur, score = None, 0.5
    for i in range(max(1, len(mots) - n + 1)):
        fenetre = " ".join(mots[i:i + n + 2])
        ratio = difflib.SequenceMatcher(None, citation.lower(), fenetre.lower()).ratio()
        if ratio > score:
            meilleur, score = fenetre, ratio
    return meilleur


def charger_transcriptions(dossier):
    return {p.stem: p.read_text(encoding="utf-8") for p in pathlib.Path(dossier).glob("*.txt")}


def verifier(paires, transcriptions):
    """paires : liste de (cas, citation). Renvoie la liste des résultats."""
    resultats = []
    for cas, citation in paires:
        texte = transcriptions.get(cas)
        if texte is None:
            resultats.append((cas, citation, None, f"transcription {cas}.txt introuvable"))
            continue
        position = chercher(citation, texte)
        resultats.append((cas, citation, position, None if position else suggestion(citation, texte)))
    return resultats


def afficher(resultats):
    echecs = 0
    for cas, citation, position, note in resultats:
        if position:
            continue
        echecs += 1
        print(f"ÉCHEC [{cas}] « {citation[:120]} »")
        if note:
            print(f"   texte le plus proche : « {note[:160]} »")
    print(f"{len(resultats) - echecs}/{len(resultats)} citations trouvées mot pour mot.")
    return 1 if echecs else 0


def texte_document(chemin):
    chemin = pathlib.Path(chemin)
    if chemin.suffix.lower() == ".docx":
        import docx

        doc = docx.Document(str(chemin))
        parties = [p.text for p in doc.paragraphs]
        parties += [c.text for t in doc.tables for r in t.rows for c in r.cells]
        return "\n".join(parties)
    return chemin.read_text(encoding="utf-8")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    sous = parser.add_subparsers(dest="mode", required=True)
    p = sous.add_parser("codage")
    p.add_argument("codage")
    p.add_argument("transcriptions")
    p.add_argument("--ecrire", action="store_true")
    p = sous.add_parser("document")
    p.add_argument("document")
    p.add_argument("transcriptions")
    args = parser.parse_args()

    transcriptions = charger_transcriptions(args.transcriptions)
    if args.mode == "codage":
        codage = json.load(open(args.codage, encoding="utf-8"))
        segments = codage["segments"]
        resultats = verifier([(s["cas"], s["citation"]) for s in segments], transcriptions)
        if args.ecrire:
            for s, (_, _, position, _) in zip(segments, resultats):
                s["debut"], s["fin"] = position if position else (None, None)
            json.dump(codage, open(args.codage, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        sys.exit(afficher(resultats))

    texte = texte_document(args.document)
    paires, sans_source = [], []
    for m in re.finditer(r"«\s*([^«»]+?)\s*»(\s*\(([A-Za-z]+\d+)[^)]*\))?", texte):
        if m.group(3):
            paires.append((m.group(3), m.group(1)))
        elif len(m.group(1).split()) >= 3:
            sans_source.append(m.group(1))
    for citation in sans_source:
        print(f"ALERTE, citation sans identifiant d'entretien (ajouter (E01) après le guillemet fermant, ou ce n'est pas une citation) : « {citation[:100]} »")
    if not paires:
        print("Aucune citation au format « texte » (E01) trouvée dans le document.")
        sys.exit(1 if sans_source else 0)
    code = afficher(verifier(paires, transcriptions))
    sys.exit(1 if sans_source else code)


if __name__ == "__main__":
    main()
