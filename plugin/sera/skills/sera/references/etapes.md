# Les 10 étapes SERA

L'ossature suit les *Normes de qualité pour l'évaluation du développement* (OCDE-CAD, 2010). Chaque étape est sourcée dans les *Normes et règles d'évaluation* (UNEG, 2016) et le *Guide de l'évaluation de l'action humanitaire* (ALNAP, 2016).

| # | Étape | Skill | Livrable principal | Sources |
|---|---|---|---|---|
| | **Phase 1 : Finalité, planification et conception** (OCDE-CAD 2.x) | | | |
| 1 | Cadrage des TDR | `cadrage-tdr` | `analyses/01-cadrage.md` | ALNAP ch. 2-7 ; UNEG 4.3-4.4 |
| 2 | Démarrage : théorie du changement et évaluabilité | `theorie-changement` | `analyses/02-toc.md` + `livrables/02-toc.png` | ALNAP ch. 8 ; UNEG 4.2 |
| 3 | Questions et matrice d'évaluation | `matrice-evaluation` | `matrice-evaluation.xlsx` | ALNAP ch. 6 ; UNEG 4.5 ; OCDE 2019 |
| 4 | Échantillonnage et outils de collecte | `echantillonnage-outils` | `analyses/04-echantillonnage.md` + outils dans `livrables/` | ALNAP ch. 10-15 |
| | **Phase 2 : Mise en oeuvre et présentation des résultats** (OCDE-CAD 3.x) | | | |
| 5 | Collecte et préparation des données | `preparation-donnees` | `donnees/` (pseudonymisé) | ALNAP ch. 10-15 ; UNEG 4.7 |
| 6 | Analyse quantitative | `analyse-quantitative` | `analyses/06-*.ipynb` | ALNAP ch. 16 |
| 7 | Analyse qualitative | `analyse-qualitative` | `analyses/07-codage.xlsx` | ALNAP ch. 16 |
| 8 | Triangulation et synthèse | `triangulation` | `analyses/08-constats.md` | ALNAP ch. 16 |
| 9 | Rapport et recommandations | `rapport` | `livrables/09-rapport.docx` | ALNAP ch. 17 ; UNEG 4.9-4.10 |
| 9 bis | Revue critique (obligatoire avant le rapport final, proposée après les étapes 3, 6 et 7) | `revue-critique` | `analyses/09-revue-critique.md` | OCDE-CAD 2010, section 1 (contrôle qualité) ; UNEG règle 5 |
| | **Phase 3 : Suivi, utilisation et enseignements** (OCDE-CAD 4.x) | | | |
| 10 | Restitution et diffusion | `restitution` | `livrables/10-restitution.pptx` | UNEG 4.11 et 1.4 |

## Skills de méthode

Elles sont appelées depuis une étape, ou directement par l'utilisateur.

| Skill | Usage |
|---|---|
| `anonymisation` | Pseudonymiser des transcriptions ou des bases avant analyse (étape 5) |
| `transcription` | Passer d'enregistrements audio, ou de documents scannés, à du texte (étape 5) |
| `analyse-contribution` | Juger la contribution d'une intervention sans groupe de comparaison (étapes 3, 8) |
| `outcome-harvesting` | Recenser les changements observés puis remonter à la contribution (étapes 3, 5, 8) |

## Références

- OCDE (2010), *Normes de qualité pour l'évaluation du développement*. https://www.oecd.org/normes-de-qualite-pour-l-evaluation-du-developpement_5kmmnc2wd828.pdf
- UNEG (2016), *Normes et règles d'évaluation*. https://www.unevaluation.org/sites/default/files/file_uploads/UNEGNormsStandardsforEvaluation_French_2017_1914_31513791020700.pdf
- ALNAP (2016), *Guide de l'évaluation de l'action humanitaire*. https://alnap.org/documents/11500/fr-alnap-eha-guide-2016.pdf
- OCDE (2019), *Des critères d'évaluation mieux adaptés pour de meilleures évaluations* ; OCDE (2021), *Appliquer les critères d'évaluation de façon réfléchie*.
