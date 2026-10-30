---
name: matrice-evaluation
description: "Formuler les questions d'évaluation, choisir les critères CAD-OCDE et les indicateurs, et construire ou vérifier la matrice d'évaluation qui relie questions, indicateurs, sources et méthodes (étape 3 de SERA). Utiliser quand l'utilisateur doit définir des questions évaluatives, des critères, des indicateurs, ou relire une matrice d'évaluation."
---

# Étape 3 : questions et matrice d'évaluation

Sources : ALNAP (2016) ch. 6 ; UNEG (2016) règle 4.5 ; OCDE (2019, 2021) pour les critères.

Lis d'abord `<skills>/sera/references/regles.md`, le fichier `etat.md`, puis [references/criteres-cad.md](references/criteres-cad.md).

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## Contexte minimal (entrée directe)

Si les étapes 1 et 2 ne sont pas validées, pose ces questions en une fois :
1. Quelle intervention est évaluée, et pour quelle décision ?
2. Quels critères les TDR demandent-ils ?
3. Les TDR posent-ils déjà des questions d'évaluation ?
4. Quelles données existent ou pourront être collectées (enquête, entretiens, statistiques) ?
5. Avez-vous une théorie du changement ou un cadre logique ?

## Mode pédagogique

Si `mode_pedagogique: oui`, propose à l'évaluateur de formuler d'abord lui-même deux questions pour un critère. Commente-les avec les règles de [references/criteres-cad.md](references/criteres-cad.md) : est-ce un jugement ou un constat, est-ce faisable, est-ce utile. Ensuite seulement, propose la matrice complète.

## 1. Questions

**Point de jugement J2** (règle 11) : avant de proposer des questions, demande à l'évaluateur, en un round court et sans ta recommandation, quelles décisions l'évaluation doit éclairer et quelles questions comptent le plus pour lui. En mode rapide : « Quelle est la question à laquelle l'évaluation doit absolument répondre ? »

Pars ensuite de ses réponses, des critères demandés par les TDR (section « Exigences des TDR » de `etat.md`), des objectifs spécifiques et des **hypothèses de la TOC** (`analyses/02-toc.md`). Une hypothèse fragile vaut une question. Propose 6 à 12 questions au total, chacune rattachée à un critère. Signale tout critère demandé par les TDR qui resterait sans question. Montre-les à l'évaluateur **avant** de détailler les indicateurs, et attends sa validation ou ses modifications.

## 2. Indicateurs, sources, méthodes

Pour chaque question validée, remplis une ligne par indicateur :
- au moins un indicateur quantitatif et un indicateur qualitatif quand c'est possible ;
- au moins **deux sources distinctes** par question, pour la triangulation ;
- la désagrégation demandée par les TDR (sexe, âge, handicap, zone...) ;
- le maillon de la TOC testé (E1, H3...).

Si une situation du tableau « Choisir une méthode spécialisée » se présente, propose la méthode en une phrase argumentée dans la colonne « Remarques », et signale-la à l'évaluateur.

## 3. Écrire et vérifier

1. Écris `analyses/03-matrice.json`, une liste d'objets aux clés : `id`, `critere`, `question`, `sous_question`, `indicateur`, `desagregation`, `sources`, `collecte`, `analyse`, `maillon_toc`, `remarques`. Les identifiants vont de `Q1.1` à `Qn.m`, et le texte de la question est identique sur toutes les lignes d'une même question.
2. Lance `python <skills>/matrice-evaluation/scripts/matrice.py ecrire analyses/03-matrice.json matrice-evaluation.xlsx`.
3. Lance `python <skills>/matrice-evaluation/scripts/matrice.py verifier matrice-evaluation.xlsx --criteres-attendus "<critères des TDR, séparés par des virgules>"`.
4. Corrige toutes les **ERREUR**, puis relance la vérification. Pour chaque **ALERTE**, corrige-la ou explique à l'évaluateur pourquoi tu la gardes.

Si l'évaluateur modifie la matrice dans Excel, relis-la avec `matrice.py lire matrice-evaluation.xlsx` avant toute nouvelle modification, puis relance `verifier`.

## 4. Présenter

Présente un résumé : nombre de questions par critère, sources les plus sollicitées, méthodes spécialisées proposées, alertes conservées. Indique que la matrice s'ouvre dans Excel et qu'elle est le **fichier pivot** : les étapes 4 à 9 s'y réfèrent.

**L'étape est terminée** quand `verifier` ne renvoie aucune ERREUR, que chaque ALERTE restante est justifiée, et que l'évaluateur a validé la matrice. Propose alors une revue critique de la matrice (skill `revue-critique`, facultative), puis l'étape 4, `echantillonnage-outils`.
