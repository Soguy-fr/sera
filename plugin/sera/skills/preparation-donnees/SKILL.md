---
name: preparation-donnees
description: "Préparer les données de terrain reçues avant l'analyse : inventaire par rapport à l'échantillon prévu, transcription, pseudonymisation, conversion des exports KoboToolbox, ODK ou Excel (étape 5 de SERA). Utiliser quand les données de collecte arrivent, ou pour vérifier ce qui a été collecté par rapport au plan."
---

# Étape 5 : collecte et préparation des données

Sources : ALNAP (2016) ch. 10 à 15 ; UNEG (2016) règle 4.7 (éthique, droits humains et genre).

Lis d'abord `<skills>/sera/references/regles.md` et le fichier `etat.md`.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## 1. Inventaire

Compare ce qui est arrivé dans `sources/` avec l'échantillon prévu à l'étape 4 (`analyses/04-echantillonnage.md`). Fais un tableau par outil : prévu, réalisé, écart, et répartition par sexe et par profil. Un écart de composition (par exemple aucune personne en situation de handicap interrogée) est une **limite à signaler** dans le rapport.

## 2. Préparer

Selon le type de données :
- **Audio ou documents scannés** : skill `transcription`.
- **Tout ce qui contient des personnes identifiables** : skill `anonymisation`. Le résultat va dans `donnees/`.
- **Bases d'enquête** (Excel, CSV, export KoboToolbox ou ODK) : garde l'export original dans `sources/`. Après pseudonymisation éventuelle, place une copie de travail dans `donnees/`. Le nettoyage se fera dans le notebook de l'étape 6, pour rester traçable.
- **Transcriptions d'entretiens** : un fichier texte par entretien dans `donnees/transcriptions/`, avec `<skills>/analyse-qualitative/scripts/extraire_texte.py`.

## 3. Consigner

Ajoute dans `etat.md` les décisions et les écarts. Indique les étapes suivantes possibles : 6 (quanti), 7 (quali), ou les deux.

**L'étape est terminée** quand chaque source de la matrice a ses données dans `donnees/`, pseudonymisées et vérifiées, ou que son absence est consignée comme limite, et que l'évaluateur a validé l'inventaire.
