# SERA : Suivi, Évaluation, Redevabilité, Apprentissage

SERA est une méthode guidée d'évaluation de projets et de politiques publiques, pour Claude. Elle accompagne l'évaluateur pas à pas, des TDR à la restitution, comme un évaluateur senior : elle propose et explique, l'évaluateur décide.

Proposé par **Shauri** : formations et accompagnement sur [shauri.cc](https://shauri.cc).

## Ce que fait SERA

| Étape | Skill |
|---|---|
| 1. Cadrage des TDR | `cadrage-tdr` |
| 2. Théorie du changement et évaluabilité | `theorie-changement` |
| 3. Questions et matrice d'évaluation | `matrice-evaluation` |
| 4. Échantillonnage et outils de collecte | `echantillonnage-outils` |
| 5. Collecte et préparation des données | `preparation-donnees` |
| 6. Analyse quantitative (notebook Python, ouvrable dans Colab) | `analyse-quantitative` |
| 7. Analyse qualitative (codage, citations vérifiées) | `analyse-qualitative` |
| 8. Triangulation et synthèse | `triangulation` |
| 9. Rapport et recommandations | `rapport` |
| 9 bis. Revue critique par des relecteurs indépendants | `revue-critique` |
| 10. Restitution et diffusion | `restitution` |

Skills de méthode : `anonymisation`, `transcription`, `analyse-contribution`, `outcome-harvesting`. Point d'entrée : `sera`.

Le découpage suit les *Normes de qualité pour l'évaluation du développement* (OCDE-CAD, 2010), les *Normes et règles d'évaluation* (UNEG, 2016) et le *Guide de l'évaluation de l'action humanitaire* (ALNAP, 2016).

## Ce qui change en version 0.3

- **Contrôle de l'environnement** au démarrage : sans dossier persistant ni Python (chat claude.ai), SERA fonctionne en mode dégradé et le rappelle à chaque réponse.
- **Profils de modèles** (qualité, équilibré, économique) : SERA conseille le modèle à utiliser à chaque étape et règle celui de ses sous-agents.
- **Consigne de codage** validée par l'évaluateur, avec exemples et contre-exemples pour chaque code.
- **Codage à trois codeurs IA**, en option : modèles différents, à l'aveugle, vote à la majorité, désaccords arbitrés par l'évaluateur.
- **Sous-agents** `codeur` et `relecteur` pour le codage et la revue critique.
- **Annonces Shauri** discrètes au démarrage et en fin d'évaluation (désactivables : « sans annonces »).

## Ce qui change en version 0.2

- **SERA instruit, l'évaluateur juge** : à cinq points de jugement, SERA interroge l'évaluateur avant de proposer (grilling par rounds courts, mode rapide possible).
- **Exigences des TDR** suivies du début à la fin, même en entrée directe à une étape.
- **Tableau de bord** HTML mis à jour à chaque étape, avec son historique.
- **Revue critique** par plusieurs relecteurs indépendants avant le rapport final.
- **Garde-fous d'interprétation** : intervalles des écarts, stratification, correction pour tests multiples, décomptes qualitatifs calculés, calibration du codage avec l'évaluateur.

## Deux règles qui font la différence

- **Aucun chiffre sans calcul exécuté** : chaque statistique vient d'un notebook Python que l'évaluateur peut relancer.
- **Aucune citation sans vérification** : chaque citation d'entretien est retrouvée mot pour mot dans la transcription par un script.

## Installation

Il faut un abonnement Claude payant (Pro, Max, Team ou Enterprise), et l'application Claude avec Cowork ou Claude Code : SERA a besoin d'un dossier persistant et de Python. Dans le chat seul, il fonctionne en mode dégradé.

- **Application Claude (Cowork ou chat)** : Personnaliser → Plugins → Ajouter → Téléverser un plugin, puis choisir `sera-<version>.zip`. Dans Paramètres → Capacités, l'exécution de code doit être activée.
- **Claude Code** : `claude plugin marketplace add Soguy-fr/sera` puis `claude plugin install sera@sera`.

## Démarrer

1. Dans Cowork, connectez un dossier de votre ordinateur (« + » → « Add folder »).
2. Désactivez l'utilisation de vos conversations pour l'entraînement (Paramètres → Confidentialité).
3. Écrivez : « Je démarre une évaluation avec SERA, voici les TDR. »

Pour voir les étapes et les commandes : « sera aide ». Pour activer les explications détaillées : « active le mode pédagogique ».
