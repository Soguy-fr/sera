# Choisir et expliquer une analyse

Ce guide est pensé pour un évaluateur qui ne maîtrise pas les statistiques. Pour chaque analyse, il donne le **pourquoi** en une phrase, et ce qu'il faut **dire** du résultat.

## 1. Quel test, selon le type des deux variables

| Variable à expliquer | Variable explicative | Analyse | Taille de l'effet | Conditions à vérifier |
|---|---|---|---|---|
| Catégorie (oui/non, zone...) | Catégorie | Tableau croisé + **khi-deux** | **V de Cramér** | Effectifs attendus ≥ 5 dans au moins 80 % des cases ; sinon test exact de Fisher (tableau 2x2) ou regroupement de modalités |
| Nombre (score, revenu...) | Catégorie à 2 groupes | **Test t de Welch** | **d de Cohen** | Distribution pas trop asymétrique ou effectifs > 30 par groupe ; sinon **Mann-Whitney** |
| Nombre | Catégorie à 3 groupes ou plus | **ANOVA de Welch** | **Eta carré** | Mêmes conditions ; sinon **Kruskal-Wallis** |
| Nombre | Nombre | **Corrélation** de Pearson (ou de Spearman si la relation n'est pas linéaire ou s'il y a des valeurs atypiques) | Le coefficient r lui-même | Regarder le nuage de points d'abord |
| Nombre | Plusieurs variables | **Régression linéaire** | Coefficients, R² | Résidus, multicolinéarité |
| Oui/non | Plusieurs variables | **Régression logistique** | Rapports de cotes (odds ratios) | Au moins 10 événements par variable explicative |

## 2. Lire les résultats : les phrases à écrire

**La p-valeur** répond à la question « une différence aussi grande pourrait-elle venir du hasard de l'échantillon ? ».
- p < 0,05 : « la différence est **statistiquement significative** : il est peu probable qu'elle soit due au hasard ».
- p ≥ 0,05 : « on **ne peut pas conclure** à une différence ». Ce n'est **pas** la preuve qu'il n'y a pas de différence.

**La taille de l'effet** répond à la question « la différence est-elle grande ? ». Il faut toujours la donner, car avec un gros échantillon une différence minuscule devient significative.

| Mesure | Faible | Moyen | Fort |
|---|---|---|---|
| V de Cramér (tableau 2x2) | 0,10 | 0,30 | 0,50 |
| d de Cohen | 0,2 | 0,5 | 0,8 |
| r de corrélation | 0,1 | 0,3 | 0,5 |
| Eta carré | 0,01 | 0,06 | 0,14 |

Ces seuils sont les repères conventionnels de Cohen (1988). Ce sont des ordres de grandeur, pas des règles.

**Modèle de phrase** : « Les élèves bénéficiaires ont une moyenne de 62,1 contre 58,4 pour les non-bénéficiaires. La différence est significative (test t de Welch, p = 0,003), mais d'ampleur faible (d = 0,27). »

## 3. L'alerte sur l'attribution

Elle est **obligatoire** dès qu'on compare des bénéficiaires et des non-bénéficiaires, ou un avant et un après.

> Cette comparaison montre une **association**, pas un **effet** du programme. Si les bénéficiaires ont été choisis selon des critères (pauvreté, zone, motivation), ils différaient déjà des non-bénéficiaires avant le programme : c'est le **biais de sélection**. Pour parler d'effet, il faudrait un groupe de comparaison construit (tirage au sort, appariement sur score de propension, double différence avec une mesure de départ) ou une démarche d'analyse de contribution.

Vérifie aussi, et montre dans le notebook, si les deux groupes diffèrent sur leurs caractéristiques de départ (pauvreté, zone, taille du ménage...). C'est la façon la plus simple de rendre le biais visible. Une régression qui contrôle ces caractéristiques réduit le biais observable, mais pas le biais lié à ce qui n'est pas mesuré : dis-le.

## 4. Désagréger

Chaque indicateur sur des personnes se présente au moins par **sexe**, et selon les TDR par zone, âge, handicap ou niveau de pauvreté. Une moyenne d'ensemble peut cacher un écart entre groupes : c'est souvent le constat le plus utile.

## 5. Nettoyage : les décisions à faire valider

| Problème | Options à proposer | Défaut recommandé |
|---|---|---|
| Doublons sur l'identifiant | Garder la première ligne ; examiner si les lignes diffèrent | Afficher les doublons, puis garder la première ligne si elles sont identiques |
| Valeurs manquantes | Exclure la ligne pour l'analyse concernée ; imputer | Exclusion analyse par analyse, en indiquant l'effectif réel de chaque résultat |
| Valeur impossible (âge de 150 ans, score > 100) | Corriger si la bonne valeur est connue ; sinon mettre en manquant | Mettre en manquant |
| Valeur atypique mais possible (revenu très élevé) | Garder ; tester la robustesse sans elle | Garder, et vérifier que la conclusion ne change pas sans elle |
| Modalités mal saisies (« F », « f », « Femme ») | Harmoniser | Harmoniser |

Chaque décision est écrite dans le notebook, avec le nombre de lignes concernées.

## 6. Quatre pièges d'interprétation

Ce sont les erreurs les plus fréquentes, y compris chez SERA. Vérifie-les avant d'écrire une phrase de résultat.

**1. Absence de preuve n'est pas preuve d'absence.** Un test non significatif sur un petit groupe ne prouve pas que les groupes sont pareils : il n'avait peut-être pas assez de personnes pour voir un écart (manque de puissance). On écrit « aucune différence détectable avec ces effectifs », puis on donne l'intervalle de l'écart (`comparer` et `croiser` le calculent). Exemple : « l'écart réel de gain de temps entre femmes et hommes peut aller de -43 à +44 minutes ».

**2. Effet de composition.** Deux groupes peuvent différer à cause d'une troisième variable. Exemple : les femmes jugent le service moins utile, mais elles sont aussi beaucoup plus souvent non-utilisatrices. Chez les seuls utilisateurs, l'écart disparaît. Avant d'attribuer un écart au sexe, à l'âge ou à la zone, refais la comparaison à l'intérieur de chaque strate de la variable suspecte avec `stratifier()`.

**3. Tests multiples.** Avec 20 tests au seuil de 5 %, on trouve en moyenne un résultat « significatif » par pur hasard. Au-delà de 5 tests, la dernière cellule du notebook (`synthese_resultats()`) corrige les p-valeurs par la méthode de Holm. Un résultat qui ne résiste pas à la correction se présente comme indicatif.

**4. Échantillon non aléatoire.** Avec des quotas ou un choix raisonné, on peut calculer les tests à titre indicatif, mais **il n'y a pas de marge d'erreur** et pas d'extrapolation à la population. De plus, un quota fixe certains pourcentages : avec « au moins 15 non-utilisateurs sur 50 », le taux d'usage observé dépend du quota, pas de la réalité.

## 7. Ventiler par composante

Quand l'intervention a plusieurs composantes (par exemple état civil et factures), un résultat global peut mélanger des réalités différentes. Ventile chaque résultat principal par composante. Si une composante a moins de 10 observations, écris-le au lieu de conclure.
