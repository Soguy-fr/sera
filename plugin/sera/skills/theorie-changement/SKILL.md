---
name: theorie-changement
description: "Reconstituer, construire, critiquer ou schématiser la théorie du changement (TOC, ToC) ou le cadre logique d'un projet ou d'une politique : chaîne de résultats, hypothèses causales, facteurs externes, schéma, évaluabilité (étape 2 de SERA). Utiliser dès que l'utilisateur parle de théorie du changement, de chaîne de résultats, de cadre logique ou d'évaluabilité."
---

# Étape 2 : théorie du changement et évaluabilité

Sources : ALNAP (2016) ch. 8 ; UNEG (2016) règle 4.2 (évaluabilité) ; OCDE (2021) sur l'usage de la TOC avec les critères.

Lis d'abord `<skills>/sera/references/regles.md` et le fichier `etat.md`.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## Contexte minimal (entrée directe)

Si l'étape 1 n'est pas validée, pose ces questions en une fois avant de commencer :
1. Quelle intervention, avec quel objectif général ?
2. Quelles sont ses grandes activités ou composantes ?
3. Qui sont les bénéficiaires visés ?
4. Avez-vous des documents (TDR, document de projet, cadre logique) ? Déposez-les dans `sources/`.

## Mode pédagogique

Si `mode_pedagogique: oui`, propose à l'évaluateur d'écrire d'abord sa propre TOC (quelques lignes suffisent). Commente-la ensuite niveau par niveau avant de montrer la tienne. Explique la différence entre un produit (ce que le projet livre) et un effet (ce qui change chez les gens), parce que c'est la confusion la plus fréquente.

## 1. Reconstituer la chaîne de résultats

À partir des TDR, des documents de projet et de la note de cadrage, propose :
- **Problème central**, avec ses causes principales ;
- **Activités** : ce que l'intervention fait ;
- **Produits** (outputs) : ce qu'elle livre directement et contrôle ;
- **Effets** (outcomes) : les changements de comportement, d'accès ou de pratique chez les acteurs, à court et à moyen terme ;
- **Impact** : le changement de long terme visé.

Chaque élément cite sa source, ou porte la mention **« reconstitué »** quand tu l'as déduit sans qu'aucun document ne l'écrive. Désagrège au moins un effet par groupe (femmes, personnes âgées, personnes en situation de handicap, zone) quand les TDR le demandent.

## 2. Hypothèses et facteurs externes

Pour chaque lien entre deux niveaux, formule l'**hypothèse causale** (H1, H2...) qui doit être vraie pour que le lien fonctionne. Par exemple : « H3 : les usagers disposent d'un téléphone et de mobile money ». Liste à part les **facteurs externes** que l'intervention ne contrôle pas. Ces hypothèses sont ce que l'évaluation devra tester : elles nourriront les questions de l'étape 3.

## 3. Schéma

Écris un fichier `analyses/02-toc.json` au format :

```json
{
  "titre": "...",
  "niveaux": [
    {"nom": "Activités", "elements": [{"id": "A1", "texte": "..."}]},
    {"nom": "Produits", "elements": [{"id": "P1", "texte": "..."}]},
    {"nom": "Effets", "elements": [{"id": "E1", "texte": "..."}]},
    {"nom": "Impact", "elements": [{"id": "I1", "texte": "..."}]}
  ],
  "liens": [["A1", "P1", "H1"], ["P1", "E1", "H3"]],
  "hypotheses": [{"id": "H1", "texte": "..."}],
  "facteurs_externes": ["..."]
}
```

Puis lance `python <skills>/theorie-changement/scripts/toc_schema.py analyses/02-toc.json livrables/02-toc.png`. Ouvre l'image et vérifie qu'elle est lisible : textes non coupés, flèches visibles. Raccourcis les textes à moins de 12 mots par boîte si besoin.

## 4. Évaluabilité

Juge chaque point avec « oui », « en partie » ou « non », et une justification courte :
- les objectifs et les effets attendus sont-ils clairs et mesurables ?
- existe-t-il une situation de référence (baseline) ou des données de suivi ?
- les données nécessaires sont-elles accessibles dans les délais ?
- les parties prenantes sont-elles disponibles et intéressées par l'évaluation ?
- le contexte (sécurité, calendrier, politique) permet-il la collecte ?

Conclus par ce que cela implique pour la méthode, par exemple : « pas de baseline, donc pas de comparaison avant-après chiffrée ; on s'appuiera sur le rappel des usagers et les statistiques du portail ».

## 5. Livrable

Écris `analyses/02-toc.md`, qui contient :
1. le récit de la TOC en 5 à 10 lignes ;
2. le tableau des niveaux ;
3. le tableau des hypothèses ;
4. les facteurs externes ;
5. la grille d'évaluabilité ;
6. le lien vers `livrables/02-toc.png`.

**L'étape est terminée** quand chaque lien du schéma porte une hypothèse, que chaque élément est sourcé ou marqué « reconstitué », et que l'évaluateur a validé la TOC. Propose alors l'étape 3, `matrice-evaluation`.
