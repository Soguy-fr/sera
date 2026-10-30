"""Vérifie les bibliothèques de l'analyse quantitative et installe celles qui manquent.

Usage : python preparer_env.py
Dans Cowork, les installations ne durent que le temps de la session : relancer à chaque session.
"""
import importlib
import subprocess
import sys

REQUIS = {
    "pandas": "pandas", "numpy": "numpy", "scipy": "scipy", "statsmodels": "statsmodels",
    "matplotlib": "matplotlib", "openpyxl": "openpyxl", "nbformat": "nbformat",
    "nbclient": "nbclient", "ipykernel": "ipykernel",
}


def manquants():
    absents = []
    for module, paquet in REQUIS.items():
        try:
            importlib.import_module(module)
        except ImportError:
            absents.append(paquet)
    return absents


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    absents = manquants()
    if not absents:
        print("Toutes les bibliothèques sont présentes.")
        return
    print("Installation : " + ", ".join(absents))
    base = [sys.executable, "-m", "pip", "install", "--quiet"]
    if subprocess.run(base + absents).returncode != 0:
        subprocess.run(base + ["--break-system-packages"] + absents)
    encore = manquants()
    if encore:
        print("ÉCHEC, toujours absentes : " + ", ".join(encore))
        sys.exit(1)
    print("Bibliothèques prêtes.")


if __name__ == "__main__":
    main()
