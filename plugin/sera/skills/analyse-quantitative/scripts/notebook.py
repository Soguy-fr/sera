"""Transforme un script Python « à cellules » en notebook, puis l'exécute.

Usage : python notebook.py <analyse.py> <analyse.ipynb>

Le script source sépare les cellules par des lignes :
  # %%               cellule de code
  # %% [markdown]    cellule de texte : chaque ligne commence par « # »
Le notebook est exécuté depuis le dossier qui le contient : les chemins de fichiers du script
doivent donc être relatifs à ce dossier. Les sorties (tableaux, graphiques) sont enregistrées
dans le .ipynb, qui s'ouvre ensuite dans Google Colab ou Jupyter.
Code de sortie 1 si une cellule échoue ; le notebook est alors enregistré avec l'erreur visible.
"""
import pathlib
import re
import sys

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


def cellules(source):
    blocs = re.split(r"^# %%(.*)$", source, flags=re.MULTILINE)
    resultat = []
    if blocs[0].strip():
        resultat.append(nbformat.v4.new_code_cell(blocs[0].strip()))
    for entete, corps in zip(blocs[1::2], blocs[2::2]):
        if "[markdown]" in entete:
            texte = "\n".join(re.sub(r"^# ?", "", l) for l in corps.strip().splitlines())
            resultat.append(nbformat.v4.new_markdown_cell(texte))
        elif corps.strip():
            resultat.append(nbformat.v4.new_code_cell(corps.strip()))
    return resultat


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    source, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    nb = nbformat.v4.new_notebook()
    nb.cells = cellules(source.read_text(encoding="utf-8"))
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nb.metadata["language_info"] = {"name": "python"}
    client = NotebookClient(nb, timeout=600, kernel_name="python3",
                            resources={"metadata": {"path": str(sortie.parent.resolve())}})
    code = 0
    try:
        client.execute()
    except CellExecutionError as erreur:
        code = 1
        print("ÉCHEC d'une cellule :")
        print(str(erreur)[:3000])
    nbformat.write(nb, str(sortie))
    n_code = sum(c.cell_type == "code" for c in nb.cells)
    print(f"Notebook {'enregistré avec erreur' if code else 'exécuté'} : {sortie} ({len(nb.cells)} cellules, dont {n_code} de code)")
    sys.exit(code)


if __name__ == "__main__":
    main()
