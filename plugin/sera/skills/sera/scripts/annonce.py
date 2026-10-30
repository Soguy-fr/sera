"""Affiche l'annonce Shauri du moment (2 lignes au plus), ou le message permanent si elle est dépassée.

Usage : python annonce.py [dossier d'évaluation]

Le fichier d'annonces est lu en ligne (ADRESSE ci-dessous), sinon dans la copie locale
references/annonces.md. Format :
  ---
  valable_jusqu_au: AAAA-MM-JJ
  ---
  ## Annonce
  texte affiché jusqu'à la date incluse
  ## Message permanent
  texte affiché ensuite
N'affiche rien si etat.md contient « annonces: non », ou si aucun fichier n'est lisible.
Le script ne fait que lire : aucune donnée de l'évaluation n'est envoyée.
"""
import datetime
import pathlib
import re
import sys
import urllib.request

# Adresse « raw » du fichier d'annonces dans le dépôt public.
ADRESSE = "https://raw.githubusercontent.com/Soguy-fr/sera/main/annonces.md"
LOCAL = pathlib.Path(__file__).resolve().parents[1] / "references" / "annonces.md"


def lire():
    if ADRESSE:
        try:
            with urllib.request.urlopen(ADRESSE, timeout=5) as r:
                return r.read().decode("utf-8")
        except Exception:
            pass
    return LOCAL.read_text(encoding="utf-8") if LOCAL.exists() else ""


def section(texte, titre):
    m = re.search(rf"^## {titre}\s*$(.*?)(?=^## |\Z)", texte, re.M | re.S)
    return m.group(1).strip() if m else ""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    etat = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "etat.md"
    if etat.exists() and re.search(r"^annonces:\s*non", etat.read_text(encoding="utf-8"), re.M):
        return
    texte = lire()
    if not texte:
        return
    date = re.search(r"valable_jusqu_au:\s*(\d{4}-\d{2}-\d{2})", texte)
    en_cours = date and datetime.date.today() <= datetime.date.fromisoformat(date.group(1))
    message = section(texte, "Annonce") if en_cours else section(texte, "Message permanent")
    if message:
        print(message)


if __name__ == "__main__":
    main()
