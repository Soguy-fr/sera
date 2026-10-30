# Le dossier d'évaluation

Il y a un dossier par évaluation, créé par `scripts/init_dossier.py`.

```
<evaluation>/
├── etat.md                    fichier d'état, lu et mis à jour par toutes les skills
├── matrice-evaluation.xlsx    fichier pivot (étape 3)
├── sources/                   tout ce qui vient de l'extérieur, jamais modifié, jamais partagé
├── donnees/                   données pseudonymisées, prêtes pour l'analyse
├── analyses/                  travail de SERA : notes, notebooks, codages (préfixe = n° d'étape)
└── livrables/                 ce qui part chez le commanditaire ou l'équipe terrain, et le tableau de bord
```

## Règles

- **`sources/`** : les TDR, documents de projet, bases brutes, enregistrements, transcriptions originales. On ne modifie jamais un fichier de `sources/`. La table de correspondance des pseudonymes est rangée ici (`sources/table-correspondance.csv`), puisque ce dossier n'est jamais partagé.
- **`donnees/`** : les versions pseudonymisées. Les analyses lisent seulement ici.
- **`analyses/`** : chaque fichier commence par le numéro d'étape (`01-cadrage.md`, `06-analyse-pnasi.ipynb`, `07-codage.xlsx`).
- **`livrables/`** : chaque fichier commence aussi par le numéro d'étape. Un livrable ne contient aucune donnée personnelle. `tableau-de-bord.html` y est régénéré, et son historique est gardé dans `livrables/tableau-de-bord/`.

## Le fichier `etat.md`

Six réglages en tête, en clair, à lire avant toute action :

```
mode_pedagogique: non
mode_grill: approfondi
profil_modeles: a choisir        (qualite, equilibre ou economique)
annonces: oui
confidentialite_verifiee: non
etape_courante: 1
```

Suivent cinq sections :
- **Avancement** : un tableau des 10 étapes. Le statut vaut `à faire`, `en cours`, `validé` ou `sautée`, et la colonne livrable donne le chemin du fichier produit.
- **Exigences des TDR** : `| Id | Exigence | Source | Étape | Statut |`.
  - Une ligne par objectif spécifique, critère demandé, livrable attendu et méthode imposée.
  - Le statut vaut `non couverte`, `en cours`, `couverte` ou `à venir`.
- **Contexte** : commanditaire, objet, période, zone, budget et délais.
- **Décisions** : une ligne datée par **décision prise**, marquée « (évaluateur) » quand elle s'écarte de la proposition de SERA. Pas de compte rendu des échanges.
- **Points en attente** : informations manquantes, données promises non reçues, questions ouvertes.

## Le fichier `analyses/tableau-de-bord.json`

Mis à jour par SERA à chaque validation d'étape. Il complète ce que le script lit déjà dans `etat.md` (avancement, exigences, points en attente). Toutes les clés sont facultatives.

```json
{
  "prochaine_action": "Étape 7 : livre de codes, puis calibration avec l'évaluateur.",
  "changement": "Notebook exécuté sans erreur ; 50 questionnaires analysés.",
  "questions": [
    {"id": "Q1", "critere": "Pertinence", "question": "...", "etat": "provisoire",
     "solidite": "Fort à moyen", "jugement": "Dans une large mesure (évaluateur)"}
  ],
  "resultats": [
    {"chiffre": "40 % contre 92 %", "libelle": "Femmes et hommes qui utilisent les e-services (10 sur 25, 23 sur 25)",
     "source": "analyses/06-resultats.xlsx"}
  ],
  "alertes": [
    {"niveau": "à traiter", "texte": "Décision contredite : livre de codes validé alors que kappa = 0 sur DEPENDANCE_TIERS."}
  ]
}
```

- `etat` d'une question : `pas de données`, `provisoire`, `validée`, `au rapport`.
- `resultats` : 3 à 5 chiffres ou constats clés au plus, chacun avec sa source (règle de preuve).
- `alertes` : les décisions contredites et les écarts à traiter. Les simples points en attente restent dans `etat.md`.
