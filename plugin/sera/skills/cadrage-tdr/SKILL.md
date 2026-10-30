---
name: cadrage-tdr
description: "Analyser des termes de référence (TDR) d'évaluation : fiche de cadrage, lacunes, enjeux implicites, exigences à couvrir et questions à poser au commanditaire (étape 1 de SERA). Utiliser quand l'utilisateur reçoit, dépose ou cite des TDR, prépare une offre technique ou une note de démarrage, ou demande ce qu'attend vraiment le commanditaire."
---

# Étape 1 : cadrage des TDR

Sources : ALNAP (2016) ch. 2 à 7 ; UNEG (2016) règles 4.3 et 4.4 ; OCDE-CAD (2010) section 2.

Lis d'abord `<skills>/sera/references/regles.md` et le fichier `etat.md` du dossier d'évaluation. S'il n'y a pas de dossier d'évaluation, appelle la skill `sera`.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## 1. Lire les TDR en entier

Lis tous les documents de `sources/` : les TDR, et aussi les documents de projet s'il y en a. Pour un `.docx`, utilise `python-docx` ; pour un PDF, l'outil de lecture de PDF. Note la section ou la page de chaque élément que tu relèves.

## 2. Fiche de cadrage

Remplis chaque rubrique avec sa source entre crochets (`[TDR §2.1]`). Pour une rubrique absente des TDR, écris **« non précisé »**.

| Rubrique | Contenu attendu |
|---|---|
| Commanditaire et utilisateurs | Qui commande, qui finance, qui utilisera les résultats, et pour quelle décision |
| Objet évalué | Intervention, composantes, budget de l'intervention, acteurs de mise en oeuvre |
| Type d'évaluation | Ex ante, mi-parcours, finale, ex post ; formative ou sommative ; interne, externe ou mixte |
| Objectifs | Objectif général et objectifs spécifiques, tels qu'écrits |
| Périmètre | Période, zone, groupes cibles, composantes incluses et exclues |
| Critères demandés | Critères CAD-OCDE et autres (genre, inclusion, droits humains) |
| Questions déjà posées | Questions d'évaluation formulées dans les TDR |
| Méthodes imposées | Collecte, échantillon, approche (mixte, participative, contrefactuelle) |
| Livrables et calendrier | Rapport de démarrage, rapport provisoire, rapport final, restitution, avec leurs dates |
| Moyens | Budget, nombre de jours, composition de l'équipe |
| Données existantes | Système de suivi, études de base, statistiques administratives annoncées |

## 3. Lecture critique

C'est le coeur de la valeur ajoutée. Relève, en citant les TDR :
- **Incohérences** : un objectif sans critère correspondant, un critère sans moyen de le juger, un calendrier incompatible avec la collecte demandée.
- **Lacunes** : les rubriques « non précisé » qui bloqueront la suite. Classe-les par gravité.
- **Enjeux implicites** : ce que les TDR laissent deviner sans le dire. Par exemple une réforme politiquement portée, un financement à renouveler, une tension entre acteurs.
- **Évaluabilité préliminaire** : les objectifs sont-ils mesurables ? Les données de référence existent-elles ? Les parties prenantes sont-elles accessibles ?
- **Genre et inclusion** : comment ils sont traités, ou leur absence.

## 4. Grilling de l'évaluateur (point de jugement J1)

Avant de lui montrer ta lecture critique, interroge l'évaluateur sur ce que les TDR ne disent pas : le vrai utilisateur des résultats, les enjeux politiques, l'accès au terrain, les données réellement disponibles, la marge de négociation sur la méthode.

Procède par rounds de 3 ou 4 questions numérotées au plus, **sans ta recommandation**, et attends les réponses (règle 11). Ta lecture n'apparaît qu'après, ou si l'évaluateur répond « je ne sais pas ». En mode rapide, une seule question : « Que veut vraiment le commanditaire ? »

Intègre ensuite ses réponses à la lecture critique, en disant ce que tu en as repris.

## 5. Livrable

Écris `analyses/01-cadrage.md`, qui contient :
1. la fiche de cadrage ;
2. la lecture critique ;
3. les réponses de l'évaluateur (enjeux et contexte qu'il a apportés) ;
4. une liste de **questions de clarification à adresser au commanditaire**, rédigée pour être envoyée telle quelle.

Mets à jour les sections « Exigences des TDR » et « Contexte » de `etat.md`, et ajoute les lacunes aux « Points en attente ».

**L'étape est terminée** quand chaque rubrique de la fiche est renseignée ou marquée « non précisé », que chaque élément cite sa source, et que l'évaluateur a validé la note. Propose alors l'étape 2, `theorie-changement`.
