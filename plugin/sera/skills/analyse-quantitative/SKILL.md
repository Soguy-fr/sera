---
name: analyse-quantitative
description: "Analyser une base de données chiffrées (enquête, suivi, Excel, CSV, KoboToolbox) pour un non-statisticien : nettoyage, statistiques descriptives, comparaison de groupes, tests et tailles d'effet, régressions, alerte sur l'attribution, notebook Python ouvrable dans Google Colab (étape 6 de SERA). Utiliser dès qu'il faut analyser, nettoyer, comparer ou interpréter des chiffres d'une évaluation."
---

# Étape 6 : analyse quantitative

Source : ALNAP (2016) ch. 16.

Lis d'abord `<skills>/sera/references/regles.md`, le fichier `etat.md`, puis [references/choisir-analyse.md](references/choisir-analyse.md). Les scripts sont dans `<skills>/analyse-quantitative/scripts/`.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

L'utilisateur n'est pas supposé connaître les statistiques. Tu guides : tu proposes, tu expliques en mots simples, il choisit.

## 0. Environnement

Lance `python preparer_env.py`. Dans Cowork, relance-le à chaque nouvelle session : les installations ne durent pas.

## 1. Comprendre ce qu'on cherche

- Si une matrice existe, lis les questions qui prévoient des données chiffrées (`matrice.py lire matrice-evaluation.xlsx`).
- Sinon, ou si c'est flou, pose ces questions en une fois :
  1. Quelle intervention, et quelle décision cette analyse doit-elle éclairer ?
  2. Que représente une ligne de la base (un élève, un ménage, un usager) ?
  3. Comment les bénéficiaires ont-ils été choisis ?
  4. Quels groupes faut-il comparer (sexe, zone, bénéficiaires et non-bénéficiaires) ?
  5. Y a-t-il une mesure avant le programme (baseline) ?

La question 3 conditionne l'alerte sur l'attribution. Pose-la toujours.

## 2. Diagnostic

Vérifie que la base ne contient pas de données personnelles. S'il y a des noms ou des téléphones, passe d'abord par `anonymisation`. Copie la base de travail dans `donnees/`.

`python profil_donnees.py donnees/<base> analyses/06-profil.md [--id <colonne>]`

Présente le diagnostic en langage simple : combien de lignes et de variables, ce que contient chaque variable, les problèmes trouvés (doublons, manquants, valeurs impossibles ou atypiques).

## 3. Plan de nettoyage et plan d'analyse

**Point de jugement J3** (règle 11) : avant de proposer le plan d'analyse, demande à l'évaluateur, en un round court et sans ta recommandation, ce qu'il s'attend à trouver et ce qui le surprendrait. Ses attentes serviront à repérer, plus tard, les résultats qui confirment ou contredisent son intuition.

Propose **en un seul message**, numéroté :
- **Nettoyage** : une ligne par problème trouvé, avec l'option recommandée (tableau « Nettoyage » de la référence) ;
- **Analyses** : pour chaque question, l'analyse proposée, pourquoi (une phrase), et ce qu'elle permettra de dire ou de ne pas dire.

Attends la validation. En mode pédagogique, ajoute pour chaque test une explication avec une analogie, et demande à l'utilisateur quel test il choisirait avant de donner le tien.

## 4. Écrire et exécuter le notebook

1. Copie `modele_analyse.py` vers `analyses/06-<nom>.py`, puis complète-le. Une cellule `# %%` par opération, précédée d'une cellule `# %% [markdown]` qui explique en français ce que fait la cellule et pourquoi. Utilise les fonctions `croiser` et `comparer` du modèle : elles vérifient les conditions et écrivent les phrases d'interprétation. Le chemin des données est relatif au dossier `analyses/` (`../donnees/...`).
2. Exécute : `python notebook.py analyses/06-<nom>.py analyses/06-<nom>.ipynb`
3. Si une cellule échoue, corrige le `.py` et relance, jusqu'à une exécution complète.
4. Lis les sorties du notebook exécuté : ce sont les seuls chiffres que tu as le droit d'écrire ensuite.

Le notebook contient, dans l'ordre :
1. chargement ;
2. nettoyage, une décision par cellule avec le nombre de lignes concernées ;
3. description de l'échantillon, désagrégée par sexe au minimum ;
4. analyses par question, **ventilées par composante** de l'objet évalué quand il y en a plusieurs (règle 9) ;
5. vérification des effets de composition : `stratifier()` pour chaque différence entre groupes qui pourrait venir d'une autre variable ;
6. si des groupes de bénéficiaires sont comparés, **comparaison des caractéristiques de départ** des deux groupes, puis l'alerte sur l'attribution ;
7. synthèse avec correction pour tests multiples, exportée par `synthese_resultats()` dans `analyses/06-resultats.xlsx`.

Outils du modèle :
- `croiser` : deux catégories ;
- `comparer` : un chiffre selon des groupes de personnes différentes ;
- `comparer_apparie` : un chiffre mesuré deux fois chez les mêmes personnes (avant / après, guichet / en ligne) ;
- `stratifier` : vérifier un écart à l'intérieur de chaque strate ;
- `synthese_resultats` : tableau final avec la correction de Holm.

Avant d'écrire un résultat, relis la section « Quatre pièges d'interprétation » de la référence.

Les graphiques sont simples : barres pour les catégories, boîtes à moustaches pour comparer des distributions. Chacun a un titre et des axes en français.

## 5. Présenter

Résume en 5 à 10 lignes les résultats clés, chacun avec son chiffre, son test et sa taille d'effet, et les limites. Rappelle :
- que le notebook `analyses/06-<nom>.ipynb` s'ouvre dans Google Colab (Fichier, Importer le notebook) ou dans Jupyter, sans rien installer ;
- qu'un notebook modifié dans Colab se remet dans `analyses/` pour que SERA le relise.

**L'étape est terminée** quand le notebook s'exécute sans erreur de bout en bout, que chaque question chiffrée de la matrice a son analyse, que l'alerte sur l'attribution figure partout où des groupes sont comparés, et que l'évaluateur a validé les résultats. Propose alors l'étape 7 ou 8.
