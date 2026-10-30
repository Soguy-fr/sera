---
name: anonymisation
description: "Pseudonymiser ou anonymiser des transcriptions, des notes ou des bases de données avant analyse ou partage : repérage des identifiants directs et indirects, table de correspondance, remplacement et vérification (méthode SERA). Utiliser dès que des données d'évaluation contiennent des noms, des téléphones, des lieux précis ou des détails permettant de reconnaître une personne."
---

# Anonymisation (pseudonymisation)

Lis d'abord `<skills>/sera/references/regles.md`, règle 4. Le script est dans `<skills>/anonymisation/scripts/`.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

On parle de **pseudonymisation** : les identifiants sont remplacés par des codes, et une table permet de revenir aux originaux. Cette table reste dans `sources/`, qui n'est jamais partagé. Le but est de pouvoir partager les données et rédiger le rapport sans qu'aucune donnée privée n'en sorte. Les autorités de protection des données (comme l'APDP au Bénin) attendent cette pratique.

## 1. Repérer

Lis chaque fichier **en entier**. Liste deux sortes d'identifiants.

**Identifiants directs** :
- noms et prénoms, y compris des tiers cités (« ma cousine Aïchatou ») ;
- surnoms ;
- numéros de téléphone, adresses, numéros de pièce ou de compte ;
- noms d'entreprises individuelles.

**Identifiants indirects** : des détails qui, combinés, désignent une personne. Par exemple :
- une profession rare dans un quartier précis (« la seule pharmacienne de Zogbo ») ;
- un poste unique (« le chef du service état civil de la mairie ») ;
- un événement daté et localisé.

Les identifiants indirects ne se remplacent pas mot à mot. Pour chacun, propose une généralisation, par exemple « Zogbo » devient « un quartier de Cotonou », et « chef du service » devient « un responsable municipal ». Montre la liste à l'évaluateur et attends sa validation.

## 2. Table de correspondance

Écris `sources/table-correspondance.csv`, en UTF-8, avec les colonnes `original,remplacement,type`.
- Une ligne par forme rencontrée : nom complet, prénom seul, nom seul, variantes d'orthographe.
- Les remplacements entre crochets, cohérents d'un fichier à l'autre : `[E05]` pour la personne interrogée, `[voisine de E05]` pour un tiers, `[quartier A]` pour un lieu.
- Les généralisations d'identifiants indirects y figurent aussi, l'original écrit exactement comme dans le texte.

## 3. Remplacer, puis vérifier

1. `python pseudonymiser.py appliquer sources/table-correspondance.csv <fichier ou dossier de sources/> donnees/`
2. `python pseudonymiser.py verifier sources/table-correspondance.csv donnees/`
3. Relis les fichiers produits à la recherche d'identifiants oubliés. Une table ne trouve que ce qu'on y a mis : complète-la, et recommence jusqu'à une relecture sans oubli.

Le script signale les originaux jamais trouvés : c'est souvent une faute d'orthographe dans la table.

## 4. Avant un livrable

Tout livrable se vérifie avant de partir : `python pseudonymiser.py verifier sources/table-correspondance.csv livrables/`

**La pseudonymisation est terminée** quand `verifier` ne trouve aucun original dans `donnees/`, qu'une relecture complète ne trouve aucun identifiant direct ni indirect, et que l'évaluateur a validé la liste.
