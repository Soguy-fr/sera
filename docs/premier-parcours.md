# Premier parcours : le cas fictif PEHY

Ce tutoriel vous fait découvrir SERA sur un cas d'évaluation entièrement inventé : l'évaluation finale d'un projet d'eau et d'hygiène autour de Yaoundé (PEHY). Comptez une à deux heures pour les étapes 1 à 3, davantage pour aller jusqu'au rapport.

Le cas est décrit dans [exemples/cas-fictif/README.md](../exemples/cas-fictif/README.md). Il a été conçu avec de **vraies difficultés** : des TDR incomplets, une base d'enquête brute avec ses défauts, des entretiens qui se contredisent. Il n'y a pas de corrigé : c'est à vous de juger.

## Préparer

1. Installez SERA ([Installer](installer.md)).
2. Copiez le dossier `exemples/cas-fictif` sur votre ordinateur, par exemple dans `Documents/evaluations/pehy`.
3. Connectez ce dossier à Claude (Cowork : « + » → « Add folder »).

## Étape 1 : le cadrage des TDR

Écrivez :

> Je démarre une évaluation avec SERA, les TDR sont dans sources/.

SERA se présente, vous demande de confirmer votre réglage de confidentialité et de choisir un profil de modèles, puis lance le cadrage. Avant de proposer quoi que ce soit, il vous pose quelques questions : c'est le **grilling**. Répondez comme si vous étiez l'évaluateur recruté.

**Ce qu'il faut regarder** dans `analyses/01-cadrage.md` :
- chaque affirmation cite sa source (« [TDR §3] ») ;
- ce que les TDR ne disent pas est écrit « non précisé », pas inventé ;
- les questions à envoyer au commanditaire.

## Étapes 2 et 3 : la théorie du changement et la matrice

Validez le cadrage, puis laissez SERA proposer l'étape suivante. À l'étape 3, la matrice d'évaluation (`matrice-evaluation.xlsx`) est vérifiée par un script : regardez ses **ERREUR** et ses **ALERTE**, par exemple un indicateur qui ne repose que sur une seule source.

## Étapes 5 à 7 : les données

- **Préparation** : l'export d'enquête `sources/enquete_menages_2026.xlsx` est brut. SERA vous aide à repérer et à traiter ses défauts, et documente chaque décision de nettoyage.
- **Analyse quantitative** : SERA écrit un notebook Python, l'exécute et vous le remet. Ouvrez-le dans Google Colab (Fichier → Importer le notebook) : chaque chiffre vient d'un calcul que vous pouvez relancer.
- **Analyse qualitative** : SERA propose une consigne de codage, que vous validez, puis code les 10 entretiens. Chaque citation est retrouvée mot pour mot dans la transcription par un script.

## Étapes 8 à 10 : conclure

La triangulation confronte le quanti et le quali. La revue critique fait relire vos analyses par plusieurs relecteurs indépendants avant le rapport. Le rapport (Word) et la restitution (PowerPoint) arrivent en dernier.

## Pendant tout le parcours

- « où en est-on ? » : l'état d'avancement ;
- « montre le tableau de bord » : une page HTML de suivi ;
- « active le mode pédagogique » : SERA explique chaque notion et vous propose de faire avant de voir sa proposition ;
- « sera aide » : toutes les commandes.
