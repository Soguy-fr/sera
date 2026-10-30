---
name: triangulation
description: "Croiser les résultats quantitatifs, qualitatifs et documentaires pour répondre aux questions d'évaluation, juger la solidité de chaque constat, recueillir le jugement de l'évaluateur et formuler les conclusions (étape 8 de SERA). Utiliser quand les analyses sont faites et qu'il faut répondre aux questions, trianguler, ou vérifier qu'un constat est assez étayé."
---

# Étape 8 : triangulation et synthèse

Source : ALNAP (2016) ch. 16. Lis d'abord `<skills>/sera/references/regles.md`, le fichier `etat.md` et la matrice.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## Contexte minimal (entrée directe)

Demande les questions d'évaluation auxquelles il faut répondre et les résultats disponibles : notebooks, synthèse qualitative, documents.

## 1. Tableau de triangulation

Pour **chaque question de la matrice**, rassemble ce que dit chaque source :
- les chiffres de `analyses/06-*.ipynb` et `06-resultats.xlsx` (avec la colonne « Résiste à la correction ») ;
- les constats de `analyses/07-synthese-qualitative.md` ;
- les documents de `sources/`.

Puis qualifie la **convergence** :
- **convergent** : les sources disent la même chose ;
- **complémentaire** : elles éclairent des aspects différents. Par exemple, le chiffre dit combien et l'entretien dit pourquoi ;
- **divergent** : elles se contredisent. C'est un résultat à expliquer, pas à cacher.

## 2. Solidité de chaque constat

| Niveau | Condition |
|---|---|
| **Fort** | Au moins deux types de sources convergent, avec des données de bonne qualité |
| **Moyen** | Une source solide, ou plusieurs sources de qualité moyenne |
| **Faible** | Une seule source fragile, ou des sources divergentes non expliquées |

Un constat faible peut figurer dans le rapport, à condition d'être présenté comme tel. Un résultat qui ne résiste pas à la correction pour tests multiples, ou qui repose sur un code en ALERTE, ne peut pas être « fort ».

## 3. Le jugement de l'évaluateur (point de jugement J4)

C'est le point de jugement le plus important : il est toujours complet, même en mode rapide (règle 11).

1. Présente, question par question, le tableau de triangulation et la solidité des constats, **sans ta réponse**.
2. Demande à l'évaluateur, par rounds de 3 ou 4 questions au plus : « Au vu de ces éléments, quelle est votre réponse à Q1 : dans une large mesure, en partie, peu ? Pourquoi ? »
3. Ensuite seulement, donne ta propre lecture. Signale tout **écart** entre son jugement et les preuves (« vous jugez l'effet fort, mais les deux constats sont de solidité moyenne »), sans trancher à sa place.
4. S'il répond « je ne sais pas », donne ta lecture argumentée et laisse-le la reprendre ou la corriger.

## 4. Contrôle des affirmations

Avant de présenter les constats, vérifie chacun :
- chaque superlatif ou classement (« principal », « le plus », « la majorité ») renvoie à un tableau qui le montre ;
- chaque pourcentage cite son n, et chaque « n sur N » qualitatif vient de `codage.py compter` ;
- un résultat non significatif est formulé selon la règle 8 (« aucune différence détectable avec ces effectifs »), jamais « identique » ;
- une différence entre groupes a été vérifiée par stratification quand une autre variable peut l'expliquer ;
- le résultat est ventilé par composante quand l'objet évalué en a plusieurs ;
- aucun attribut `(déduit)` ne sert de base à un constat sans réserve.

Corrige ce qui ne passe pas avant de continuer.

## 5. Livrable

Écris `analyses/08-constats.md`, organisé par critère puis par question. Pour chaque question :
1. la **réponse étayée** par SERA, en 2 ou 3 phrases, qui porte un jugement (« dans une large mesure », « en partie », « peu ») ;
2. le **jugement de l'évaluateur**, tel qu'il l'a formulé, et l'écart éventuel avec la réponse étayée ;
3. les **constats** (C1.1, C1.2...), chacun avec sa solidité et ses preuves (chiffre et n, citation « texte » (E01), document) ;
4. les **différences entre groupes** (genre, inclusion) et entre composantes ;
5. les **limites**.

Ajoute ensuite :
- une section **« Bonnes pratiques observées »**, que les TDR demandent souvent. La matière vient des cas divergents positifs : un incident bien traité, une mesure ciblée qui fonctionne ;
- 3 à 6 **conclusions transversales** numérotées, chacune citant ses constats ;
- des pistes de recommandations (R1, R2...), chacune rattachée à une conclusion. Ces identifiants seront repris tels quels dans le rapport.

Quand une question porte sur l'effet de l'intervention sans groupe de comparaison, propose la skill `analyse-contribution`.

Vérifie les citations : `python <skills>/analyse-qualitative/scripts/verifier_citations.py document analyses/08-constats.md donnees/transcriptions/`

Mets à jour `analyses/tableau-de-bord.json` (questions, solidité, jugement) et régénère le tableau de bord.

**L'étape est terminée** quand chaque question de la matrice a une réponse étayée et le jugement de l'évaluateur, que chaque constat a passé le contrôle des affirmations, que toutes les citations sont vérifiées, et que l'évaluateur a validé les constats. Propose alors la skill `revue-critique` (obligatoire avant le rapport final), puis l'étape 9.
