# Cas fictif : évaluation finale du projet PEHY

> **Cas fictif, à usage pédagogique.** Le projet PEHY, l'Alliance pour l'Eau du Centre (AEC), la Fondation Horizon Partage, les communes de Nkolfeme, Akok-Bindi et Ondoa-Mesam, leurs villages et toutes les personnes interrogées sont **inventés**. Les données d'enquête sont **simulées**. Toute ressemblance avec des structures, des lieux ou des personnes existants serait fortuite. Seuls le pays (Cameroun) et la région (Centre, autour de Yaoundé) sont réels, pour donner un contexte crédible.

Ce dossier contient ce qu'un évaluateur recevrait au moment de démarrer la mission. Il permet de dérouler SERA de bout en bout, du cadrage des TDR (étape 1) jusqu'au rapport et à la restitution.

## Le projet en bref

Le **Projet Eau et Hygiène dans la périphérie de Yaoundé (PEHY)** a été mis en œuvre de 2022 à 2025 par une ONG nationale, pour 780 millions de FCFA. Il comprend quatre composantes :
- des forages et des mini-adductions d'eau ;
- des comités de gestion des points d'eau, financés par une cotisation des ménages ;
- de la sensibilisation à l'hygiène par des relais communautaires ;
- un appui aux communes.

L'ONG commande une évaluation finale. Une seconde phase est en préparation.

## Contenu

```
cas-fictif/
├── README.md                              ce fichier
├── sources/
│   ├── TDR.md                             termes de référence (Markdown)
│   ├── TDR.docx                           les mêmes TDR au format Word
│   ├── rapport-annuel-2025-extrait.md     extrait du rapport annuel de l'ONG au bailleur
│   └── enquete_menages_2026.xlsx          export brut de l'enquête, non nettoyé
└── donnees/
    └── transcriptions/
        └── E01.txt à E10.txt              10 entretiens individuels transcrits
```

### L'enquête auprès des ménages (`sources/enquete_menages_2026.xlsx`)

| Feuille | Contenu |
|---|---|
| `lisez-moi` | Origine et statut de l'export |
| `menages` | 248 lignes, 27 variables : un ménage par ligne, en zone du projet et en zone de comparaison |
| `points_eau` | Observation des 27 ouvrages du projet : état, comité, solde de caisse déclaré |
| `villages` | Les 16 villages enquêtés : commune, zone, distance à la route, réseau national |
| `dictionnaire` | Libellé, type et valeurs possibles de chaque variable |

L'export est **brut** : comme dans une vraie collecte, il contient des défauts à repérer et à traiter avant l'analyse.

### Les entretiens (`donnees/transcriptions/`)

| Code | Profil |
|---|---|
| E01 | Usagère du forage, commerçante, zone du projet |
| E02 | Usager âgé, forage du quartier en panne, zone du projet |
| E03 | Veuve, cheffe de ménage, zone du projet |
| E04 | Jeune homme, village de comparaison desservi par le réseau national |
| E05 | Mère de deux jeunes enfants, zone du projet |
| E06 | Relais communautaire en hygiène |
| E07 | Président d'un comité de gestion de point d'eau |
| E08 | Agent technique communal, service eau et assainissement |
| E09 | Coordinatrice du projet à l'ONG |
| E10 | Secrétaire général d'une commune |

Les transcriptions sont déjà **pseudonymisées** (codes E01 à E10). Une vérification de confidentialité reste à faire avant tout livrable.

## Utiliser ce cas avec SERA

1. Copiez le dossier `cas-fictif` à l'endroit où vous rangez vos évaluations, puis connectez-le à Claude (Cowork ou Claude Code).
2. Dites à Claude : « Je démarre une évaluation avec SERA, les TDR sont dans `sources/` ». SERA crée le fichier d'état et les dossiers manquants (`analyses/`, `livrables/`), puis lance le cadrage des TDR.
3. Avancez étape par étape. SERA propose, vous jugez.

Les TDR comme les données ont été conçus pour poser de **vraies difficultés d'évaluation**, comme sur une mission réelle. Il n'y a pas de corrigé dans ce dossier : c'est à vous de juger.
