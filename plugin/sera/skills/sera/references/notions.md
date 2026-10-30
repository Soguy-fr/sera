# Notions et objets de SERA

Ce fichier est la référence commune de vocabulaire. Il sert à expliquer une notion quand on te le demande, ou en mode pédagogique : définition simple, terme anglais courant, piège fréquent. Adapte toujours l'explication avec un exemple tiré du dossier en cours.

## 1. Les objets de SERA et leurs liens (ontologie légère)

```
TDR ──exige──▶ Exigence (OS1, OS2...)
Intervention ──se décrit par──▶ TOC : Activité (A) → Produit (P) → Effet (E) → Impact (I)
                                   chaque lien porte une Hypothèse (H)
Question d'évaluation (Qn) ──relève d'──▶ Critère (CAD-OCDE ou TDR)
Question (Qn) ──se mesure par──▶ Indicateur (Qn.m) ──s'appuie sur──▶ Source ──collectée par──▶ Outil
Outil ──produit──▶ Donnée (enquête, transcription Exx / Ixx)
Transcription ──découpée en──▶ Segment ──porte──▶ Code (défini dans le livre de codes)
Analyse (notebook, codage) ──produit──▶ Résultat
Résultat(s) ──triangulés en──▶ Constat (Cn.m), avec une solidité
Constat(s) ──fondent──▶ Réponse à une question (+ jugement de l'évaluateur)
Constats ──fondent──▶ Conclusion (1, 2, 3...) ──fonde──▶ Recommandation (R1, R2...)
```

| Objet | Identifiant | Défini à l'étape | Où il vit |
|---|---|---|---|
| Exigence des TDR | OS1, OS2a, M... | 1 (ou démarrage) | `etat.md` |
| Élément de TOC, hypothèse | A1, P1, E1, I1, H1 | 2 | `analyses/02-toc.json` |
| Question, indicateur | Q1, Q1.1 | 3 | `matrice-evaluation.xlsx` |
| Entretien | E01 (usager), I01 (institution) | 5 | `donnees/transcriptions/` |
| Code | GAIN_TEMPS (majuscules, sans accents) | 7 | `analyses/07-livre-de-codes.json` |
| Constat | C1.1 (question 1, constat 1) | 8 | `analyses/08-constats.md` |
| Conclusion, recommandation | 1, 2... ; R1, R2... | 8 puis 9 | `analyses/08-constats.md`, rapport |

Un identifiant ne change jamais d'une étape à l'autre. Une recommandation cite la conclusion dont elle découle, et une conclusion cite ses constats.

## 2. Notions de base

### Cadre de l'évaluation

| Notion | Définition simple | Anglais | Piège fréquent |
|---|---|---|---|
| TDR | Document du commanditaire qui définit ce qu'il attend de l'évaluation | ToR | Ne lire que les questions, et rater les objectifs spécifiques et les livrables |
| Commanditaire | Organisation qui commande et finance l'évaluation | Commissioner | Le confondre avec l'utilisateur des résultats |
| Évaluation formative / sommative | Formative : pour améliorer en cours de route. Sommative : pour juger à la fin | Formative / summative | Écrire un jugement sommatif pour une évaluation à mi-parcours |
| Évaluabilité | Mesure dans laquelle une intervention peut être évaluée de façon fiable | Evaluability | Se lancer sans vérifier qu'il existe des données |
| Théorie du changement (TOC) | Le raisonnement qui relie ce que fait le projet aux changements attendus, avec ses hypothèses | Theory of change | Dessiner des boîtes sans écrire les hypothèses entre elles |
| Cadre logique | Tableau objectifs / indicateurs / sources / hypothèses du projet | Logframe | Le prendre pour une TOC complète |
| Produit / effet / impact | Produit : ce que le projet livre. Effet : ce qui change chez les gens. Impact : le changement de long terme | Output / outcome / impact | Présenter un produit (« 50 guichets ouverts ») comme un effet |
| Critères CAD-OCDE | Pertinence, cohérence, efficacité, efficience, impact, durabilité | DAC criteria | Les traiter comme une liste à cocher |
| Matrice d'évaluation | Tableau qui relie chaque question à ses indicateurs, sources et méthodes | Evaluation matrix | Une question avec une seule source |

### Collecte et échantillon

| Notion | Définition simple | Anglais | Piège fréquent |
|---|---|---|---|
| Échantillon aléatoire | Chaque personne a une chance connue d'être tirée | Random sample | Le seul qui permet une marge d'erreur |
| Quotas | On choisit des personnes jusqu'à atteindre des effectifs par profil | Quota sampling | Annoncer une marge d'erreur, ou des pourcentages valables pour toute la population |
| Choix raisonné | On choisit les personnes pour ce qu'elles peuvent éclairer | Purposive sampling | Généraliser des pourcentages tirés de 10 entretiens |
| Saturation | Le moment où de nouveaux entretiens n'apportent plus de thèmes nouveaux | Saturation | La déclarer sans l'avoir vérifiée |
| Pseudonymisation | Remplacer les identifiants par des codes, avec une table gardée à part | Pseudonymisation | Oublier les identifiants indirects (profession rare + quartier) |
| Usage autonome / délégué | Autonome : la personne fait elle-même. Délégué : un proche le fait pour elle | Direct / proxy use | Compter un usage délégué comme un usage |

### Analyse quantitative

| Notion | Définition simple | Anglais | Piège fréquent |
|---|---|---|---|
| p-valeur | Probabilité d'observer un écart aussi grand si, en réalité, il n'y en avait aucun | p-value | Croire qu'un p non significatif prouve l'absence d'effet |
| Intervalle de confiance | La fourchette dans laquelle se trouve probablement la vraie valeur | Confidence interval | Ne donner que le chiffre central |
| Taille de l'effet | La grandeur d'un écart, indépendamment de l'effectif | Effect size | Confondre « significatif » et « important » |
| Puissance | La capacité d'un test à détecter un écart qui existe | Statistical power | Conclure à « pas de différence » avec 10 personnes |
| Effet de composition | Un écart entre groupes qui vient d'une autre variable que celle étudiée | Composition effect | Attribuer au sexe un écart qui vient de l'usage |
| Tests multiples | Plus on fait de tests, plus on trouve des résultats significatifs par hasard | Multiple testing | Présenter le seul test significatif sur vingt |
| Biais de sélection | Les groupes comparés différaient déjà avant le programme | Selection bias | Attribuer au programme une différence de départ |
| Attribution / contribution | Attribution : mesurer l'effet propre. Contribution : montrer de façon plausible que le programme y a contribué | Attribution / contribution | Parler d'effet sans groupe de comparaison |

### Analyse qualitative et synthèse

| Notion | Définition simple | Anglais | Piège fréquent |
|---|---|---|---|
| Code | Étiquette posée sur un extrait, qui veut dire la même chose partout | Code | Un code sans règle d'exclusion |
| Livre de codes | La liste des codes avec définition, inclusion, exclusion, exemple | Codebook | Le modifier sans recoder ce qui est déjà codé |
| Codage déductif / inductif | Déductif : codes tirés de la matrice. Inductif : codes qui émergent des données | Deductive / inductive | Ne faire que du déductif, et rater l'imprévu |
| Accord entre codeurs | Mesure de la concordance entre deux codeurs | Inter-coder reliability | Se fier au pourcentage d'accord, gonflé par les « absent / absent » |
| Kappa de Cohen | Accord corrigé du hasard. Repères courants : < 0,4 faible, 0,4 à 0,6 moyen, 0,6 à 0,8 bon, > 0,8 très bon | Cohen's kappa | Passer en production avec un code à kappa faible |
| Cas divergent | Un cas qui contredit la tendance | Negative case | L'écarter au lieu de l'expliquer |
| Triangulation | Croiser plusieurs sources ou méthodes sur une même question | Triangulation | Additionner les sources sans dire si elles convergent |
| Solidité d'un constat | Fort, moyen ou faible selon le nombre et la qualité des sources convergentes | Strength of evidence | Mettre « fort » sur une seule source |
| Constat / conclusion / recommandation | Constat : ce qu'on observe. Conclusion : ce qu'on en juge. Recommandation : ce qu'on propose de faire | Finding / conclusion / recommendation | Une recommandation qui ne découle d'aucune conclusion |
| Réponse de la direction | Le document où le commanditaire accepte ou refuse chaque recommandation | Management response | Ne pas prévoir de suivi |
