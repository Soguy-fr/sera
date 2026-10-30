"""Génère le tableau de bord HTML d'un dossier d'évaluation SERA.

Usage : python tableau_de_bord.py [dossier d'évaluation, par défaut le dossier courant]

Lit :
  - etat.md : avancement, exigences des TDR, points en attente, étape courante ;
  - analyses/tableau-de-bord.json (facultatif) : prochaine action, changement, questions,
    résultats clés, alertes (format dans sera/references/dossier.md) ;
  - matrice-evaluation.xlsx, si le JSON ne liste pas les questions.
Écrit :
  - livrables/tableau-de-bord.html (version courante) ;
  - livrables/tableau-de-bord/AAAA-MM-JJ-etape-N.html (copie datée, gardée pour l'historique).
"""
import datetime
import html
import json
import pathlib
import re
import sys

NOMS = ["Cadrage", "TOC", "Matrice", "Échantillon et outils", "Collecte", "Analyse quanti",
        "Analyse quali", "Triangulation", "Rapport", "Restitution"]

CSS = """
:root { --fond:#f6f5f1; --carte:#fff; --texte:#1c2a39; --doux:#5b6675; --bord:#dfdcd3;
  --ok:#2e6b5e; --ok-fond:#e3f0ec; --encours:#8a6d1d; --encours-fond:#fbf1d6;
  --alerte:#a8532a; --alerte-fond:#f8e4da; --neutre-fond:#eceae4; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --fond:#14191f; --carte:#1d242c; --texte:#e8e6e1; --doux:#9aa4b0; --bord:#2f3842;
  --ok:#7cc4b1; --ok-fond:#1e3631; --encours:#e2c46b; --encours-fond:#3a321a;
  --alerte:#ec9a73; --alerte-fond:#3d2519; --neutre-fond:#262e37; } }
* { box-sizing:border-box; }
body { margin:0; background:var(--fond); color:var(--texte); font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; }
header, main { max-width:1180px; margin:0 auto; padding:16px; }
h1 { font-size:20px; margin:0 0 4px; } .sous { color:var(--doux); font-size:13px; }
main { display:grid; gap:14px; grid-template-columns:1fr 1fr; padding-top:0; }
section { background:var(--carte); border:1px solid var(--bord); border-radius:10px; padding:14px 16px; min-width:0; }
section.large { grid-column:1/-1; }
h2 { font-size:13px; text-transform:uppercase; letter-spacing:.06em; color:var(--doux); margin:0 0 10px; }
.etapes { display:grid; grid-template-columns:repeat(10,1fr); gap:4px; }
.etape { border-radius:6px; padding:6px 4px; text-align:center; font-size:11px; line-height:1.25; background:var(--neutre-fond); color:var(--doux); }
.etape .n { display:block; font-weight:700; font-size:14px; }
.etape.valide { background:var(--ok-fond); color:var(--ok); }
.etape.encours { background:var(--encours-fond); color:var(--encours); outline:2px solid var(--encours); }
.etape.sautee { background:var(--alerte-fond); color:var(--alerte); }
.etape .livrable { display:block; margin-top:4px; padding-top:4px; border-top:1px solid currentColor; font-size:10px; color:inherit; word-break:break-word; }
.prochaine { font-size:16px; } .change { font-size:13px; color:var(--doux); }
table { width:100%; border-collapse:collapse; font-size:13px; }
th, td { text-align:left; padding:6px; border-bottom:1px solid var(--bord); vertical-align:top; }
th { color:var(--doux); font-size:12px; }
.pastille { display:inline-block; padding:1px 8px; border-radius:999px; font-size:12px; white-space:nowrap; }
.p-ok { background:var(--ok-fond); color:var(--ok); } .p-encours { background:var(--encours-fond); color:var(--encours); }
.p-alerte { background:var(--alerte-fond); color:var(--alerte); } .p-neutre { background:var(--neutre-fond); color:var(--doux); }
ul.liste { margin:0; padding:0; list-style:none; } ul.liste li { padding:6px 0; border-bottom:1px solid var(--bord); font-size:13px; }
.resultats { display:grid; grid-template-columns:repeat(auto-fill,minmax(210px,1fr)); gap:10px; }
.resultat { border:1px solid var(--bord); border-radius:8px; padding:10px; }
.chiffre { font-size:22px; font-weight:700; } .src { color:var(--doux); font-size:12px; margin-top:4px; }
.vide { color:var(--doux); font-style:italic; font-size:13px; }
@media (max-width:760px) { main { grid-template-columns:1fr; } .etapes { grid-template-columns:repeat(5,1fr); } }
"""


def e(texte):
    return html.escape(str(texte or ""))


def section(md, titre):
    """Contenu d'une section ## de etat.md."""
    m = re.search(rf"^## {re.escape(titre)}\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    return m.group(1) if m else ""


def tableau(texte):
    lignes = [l.strip() for l in texte.splitlines() if l.strip().startswith("|")]
    lignes = [l for l in lignes if not re.fullmatch(r"\|[\s:|-]+\|", l)]
    return [[c.strip() for c in l.strip("|").split("|")] for l in lignes[1:]]


def ton_statut(statut):
    s = statut.lower()
    if s.startswith("valid") or s.startswith("couvert"):
        return "ok"
    if "cours" in s or "partiel" in s:
        return "encours"
    if "non couvert" in s or "saut" in s:
        return "alerte"
    return "neutre"


def lien(livrable, profondeur):
    m = re.search(r"https?://\S+|[\w./-]+\.(?:md|xlsx|ipynb|docx|pptx|png|json|py|html)", livrable)
    if not m:
        return e(livrable)
    cible = m.group(0)
    href = cible if cible.startswith("http") else "../" * profondeur + cible
    return f'<a href="{e(href)}">{e(livrable)}</a>'


def questions_matrice(racine):
    chemin = racine / "matrice-evaluation.xlsx"
    if not chemin.exists():
        return []
    from openpyxl import load_workbook
    ws = load_workbook(chemin, data_only=True)["Matrice"]
    vues, sortie = set(), []
    for ident, critere, question, *_ in ws.iter_rows(min_row=2, values_only=True):
        if ident and question and str(ident).split(".")[0] not in vues:
            vues.add(str(ident).split(".")[0])
            sortie.append({"id": str(ident).split(".")[0], "critere": critere, "question": question,
                           "etat": "pas de données"})
    return sortie


def page(racine, md, donnees, profondeur):
    titre = re.search(r"^# (.+)$", md, re.M)
    etape_courante = re.search(r"^etape_courante:\s*(\d+)", md, re.M)
    lignes = tableau(section(md, "Avancement"))
    cases = []
    for i, nom in enumerate(NOMS):
        statut, livrable = (lignes[i][1], lignes[i][2]) if i < len(lignes) and len(lignes[i]) > 2 else ("à faire", "")
        classe = {"ok": "valide", "encours": "encours", "alerte": "sautee"}.get(ton_statut(statut), "")
        liv = f'<span class="livrable">{lien(livrable, profondeur)}</span>' if livrable else ""
        cases.append(f'<div class="etape {classe}"><span class="n">{i + 1}</span>{nom}<br>{e(statut)}{liv}</div>')

    exig = "".join(
        f"<tr><td>{e(l[1])}<br><span class='sous'>{e(l[0])} · {e(l[2])}</span></td>"
        f"<td><span class='pastille p-{ton_statut(l[4])}'>{e(l[4])}</span></td></tr>"
        for l in tableau(section(md, "Exigences des TDR")) if len(l) >= 5 and l[1] and not l[1].startswith("(")
    ) or "<tr><td class='vide'>Aucune exigence renseignée : déposer les TDR.</td></tr>"

    attente = [f"<li><span class='pastille p-alerte'>{e(a.get('niveau', 'à traiter'))}</span> {e(a['texte'])}</li>"
               for a in donnees.get("alertes", [])]
    attente += [f"<li><span class='pastille p-neutre'>en attente</span> {e(l.lstrip('- ').strip())}</li>"
                for l in section(md, "Points en attente").splitlines() if l.strip().startswith("-")]

    qs = donnees.get("questions") or questions_matrice(racine)
    lignes_q = "".join(
        f"<tr><td><b>{e(q['id'])}</b> · {e(q.get('critere'))}<br>{e(q.get('question'))}</td>"
        f"<td><span class='pastille p-{ton_statut(q.get('etat', ''))}'>{e(q.get('etat'))}</span></td>"
        f"<td>{e(q.get('solidite')) or '-'}</td><td>{e(q.get('jugement')) or '-'}</td></tr>" for q in qs
    ) or "<tr><td class='vide'>Pas encore de matrice.</td></tr>"

    res = donnees.get("resultats", [])
    bloc_res = ("<div class='resultats'>" + "".join(
        f"<div class='resultat'><div class='chiffre'>{e(r['chiffre'])}</div><div>{e(r['libelle'])}</div>"
        f"<div class='src'>Source : {e(r['source'])}</div></div>" for r in res) + "</div>"
    ) if res else "<p class='vide'>Aucun résultat pour l'instant.</p>"

    date = datetime.date.today().strftime("%d/%m/%Y")
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tableau de bord SERA</title><style>{CSS}</style></head><body>
<header><h1>Tableau de bord : {e(titre.group(1).replace("État de l'évaluation : ", "") if titre else racine.name)}</h1>
<div class="sous">Mis à jour le {date} · étape courante : {e(etape_courante.group(1) if etape_courante else "?")} · généré par SERA</div></header>
<main>
<section class="large"><h2>Avancement</h2><div class="etapes">{"".join(cases)}</div>
<p class="prochaine">Prochaine action : {e(donnees.get("prochaine_action", "à définir"))}</p>
<p class="change">Ce qui vient de changer : {e(donnees.get("changement", "-"))}</p></section>
<section><h2>Exigences des TDR</h2><table><tbody>{exig}</tbody></table></section>
<section><h2>Points en attente et décisions contredites</h2><ul class="liste">{"".join(attente) or "<li class='vide'>Rien en attente.</li>"}</ul></section>
<section class="large"><h2>Questions de la matrice</h2><table><thead><tr><th>Question</th><th>État de la réponse</th>
<th>Solidité</th><th>Jugement de l'évaluateur</th></tr></thead><tbody>{lignes_q}</tbody></table></section>
<section class="large"><h2>Premiers résultats</h2>{bloc_res}</section>
</main></body></html>
"""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    racine = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    md = (racine / "etat.md").read_text(encoding="utf-8")
    chemin_json = racine / "analyses" / "tableau-de-bord.json"
    donnees = json.load(open(chemin_json, encoding="utf-8")) if chemin_json.exists() else {}
    etape = re.search(r"^etape_courante:\s*(\d+)", md, re.M)

    sortie = racine / "livrables" / "tableau-de-bord.html"
    sortie.parent.mkdir(exist_ok=True)
    sortie.write_text(page(racine, md, donnees, 1), encoding="utf-8")
    historique = racine / "livrables" / "tableau-de-bord"
    historique.mkdir(exist_ok=True)
    copie = historique / f"{datetime.date.today().isoformat()}-etape-{etape.group(1) if etape else 'x'}.html"
    copie.write_text(page(racine, md, donnees, 2), encoding="utf-8")
    print(f"Tableau de bord : {sortie}")
    print(f"Copie datée : {copie}")


if __name__ == "__main__":
    main()
