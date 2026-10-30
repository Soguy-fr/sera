---
name: analyse-qualitative
description: "Coder et analyser des entretiens, des focus groups ou des réponses ouvertes : livre de codes, consigne de codage validée, calibration avec l'évaluateur, un ou trois codeurs IA, citations vérifiées mot pour mot, synthèse par question (étape 7 de SERA). Utiliser quand l'utilisateur veut coder des transcriptions, analyser des entretiens, construire un livre de codes ou comparer deux codages."
---

# Étape 7 : analyse qualitative

Source : ALNAP (2016) ch. 16.

Lis d'abord `<skills>/sera/references/regles.md` et le fichier `etat.md`. Les scripts sont dans `<skills>/analyse-qualitative/scripts/`.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## Contexte minimal (entrée directe)

Sans matrice validée, pose ces questions en une fois :
1. Quelle intervention, et quelles questions voulez-vous éclairer avec ces entretiens ?
2. Qui a été interrogé, et selon quels profils (sexe, âge, statut...) ?
3. Avez-vous déjà un livre de codes ou une grille d'analyse ?

## Mode pédagogique

Si `mode_pedagogique: oui`, explique avant de commencer :
- ce qu'est un code (une étiquette posée sur un extrait, qui veut dire la même chose partout) ;
- la différence entre codage **déductif** (codes tirés de la matrice) et **inductif** (codes qui émergent des données) ;
- pourquoi chaque code a une règle « quand ne pas l'utiliser ».

En calibration (section 4), discute avec lui chaque désaccord, code par code.

## 1. Préparer le corpus

1. Vérifie que les transcriptions sont pseudonymisées. Sinon, passe d'abord par la skill `anonymisation`.
2. Convertis-les en texte, un fichier par entretien :
   `python extraire_texte.py <fichier ou dossier> donnees/transcriptions/ [--decouper "^Entretien (E\d+)"]`
   Les fichiers `.txt` produits sont **la référence** des citations. On ne les modifie plus.
3. Lis **chaque transcription en entier** avant de coder.

## 2. Livre de codes

Écris `analyses/07-livre-de-codes.json` : une liste d'objets `code`, `definition`, `inclure`, `exclure`, `exemple`, `question`.
- **Codes déductifs** : un ou plusieurs par question de la matrice (`matrice.py lire matrice-evaluation.xlsx`) et par hypothèse de la TOC.
- **Codes inductifs** : les thèmes qui reviennent dans les données sans être prévus. Signale-les comme tels : ce sont souvent les découvertes de l'évaluation.
- Les noms de codes sont courts, en majuscules sans accents (`GAIN_TEMPS`, `FRAIS_MOMO`).
- La règle `exclure` dit avec quel code voisin ne pas confondre.

Présente le livre de codes à l'évaluateur et attends sa validation.

## 3. Consigne de codage (validée par l'évaluateur)

Le livre de codes dit **ce que** veulent dire les codes. La consigne dit **comment** coder : c'est le texte exact que recevra chaque codeur IA. Écris `analyses/07-consigne-codage.md` :
1. **Règles générales** :
   - l'unité de codage : une réponse de la personne interrogée, identifiée E05-R3 (fichier `analyses/07-unites.json`, produit par `python codage_multiple.py segmenter donnees/transcriptions/ analyses/07-unites.json`) ;
   - plusieurs codes possibles par unité, aucun si rien ne s'applique ;
   - le format de sortie : `{"codeur": "...", "unites": {"E05-R3": ["CODE"]}}`.
2. **Pour chaque code** : définition, quand l'utiliser, quand ne pas l'utiliser (avec le code voisin à ne pas confondre), **2 ou 3 exemples** tirés du corpus (citation exacte et identifiant d'unité), et **1 contre-exemple**, c'est-à-dire une unité qui ressemble au code mais n'en relève pas, avec la raison.

Les exemples sont des citations réelles, vérifiées avec `verifier_citations.py document`. Montre la consigne à l'évaluateur : il valide, corrige ou remplace les exemples. **Aucun codage de production ne commence avant sa validation.** La consigne porte un numéro de version. Toute correction après la calibration crée une nouvelle version, consignée dans `etat.md`.

## 4. Calibration avec l'évaluateur (porte d'entrée en production)

C'est le moment où l'évaluateur garde la main sur le codage. Avant de coder tout le corpus :
1. Propose à l'évaluateur de coder lui-même 1 ou 2 entretiens avec la consigne, sans voir ton codage. S'il ne peut pas, un sous-agent `codeur` qui reçoit seulement la consigne et les unités peut servir de second codeur, mais dis-le : un accord entre deux IA mesure la **stabilité** de la consigne, pas sa **validité**.
2. Compare : `python codage.py accord <codage-evaluateur.json> <codage-sera.json> --sortie analyses/07-accord.xlsx`
3. Présente d'abord le **kappa** et l'accord sur les présences. L'accord brut est gonflé par les cases « absent / absent » : ne le présente jamais seul.
4. **Chaque code en ALERTE (kappa < 0,6) bloque la production.** Corrige la consigne, dans cet ordre : définition, puis règle d'exclusion, puis exemples. Le passage contesté ne sert pas d'exemple. Puis fais recoder par l'évaluateur un **nouvel** entretien, et recalcule l'accord.
5. Consigne dans `etat.md` les kappas finaux par code. Un code qui reste sous le seuil est utilisé avec une réserve écrite dans la synthèse.

## 5. Coder le corpus : un codeur, ou trois

**Demande d'abord à l'évaluateur s'il veut trois codeurs IA**, et explique le prix : le codage coûte environ trois fois plus de quota, en échange de moins d'erreurs et d'une liste ciblée de cas difficiles à trancher.

**Avec un seul codeur** (toi) : code chaque unité selon la consigne, puis écris `analyses/07-codage.json` au format habituel (`cas`, `segments` avec `cas`, `unite`, `codes`, `citation` = texte exact de l'unité, `memo`).

**Avec trois codeurs** :
1. Toi (codeur A), plus deux sous-agents `codeur` lancés **en parallèle**, chacun avec un **modèle différent** selon le profil de modèles (par exemple Opus et Sonnet), et la consigne présentée dans un ordre de codes différent. Chacun reçoit seulement la consigne validée et `analyses/07-unites.json`. Aucun ne voit le codage des autres. Pas de personnage (âge, sexe) dans les consignes : cela n'apporte aucune compétence et risque d'introduire des stéréotypes.
2. Chaque codeur écrit `analyses/07-codeur-A.json`, `-B.json`, `-C.json`. Écris aussi `analyses/07-cas.json` (`{"cas": [{"id": "E01", "attributs": {...}}]}`) avec les profils tels qu'ils figurent dans les transcriptions.
3. Vote : `python codage_multiple.py vote analyses/07-unites.json analyses/07-codeur-A.json analyses/07-codeur-B.json analyses/07-codeur-C.json --cas analyses/07-cas.json --sortie analyses/07-codage.json --arbitrage analyses/07-arbitrage.xlsx`
   - Un code est retenu sur une unité quand **au moins deux codeurs sur trois** l'y ont posé.
   - Chaque désaccord (2 contre 1, ou 1 contre 2) part dans `07-arbitrage.xlsx`, avec le texte de l'unité et le vote de chaque codeur.
4. **Arbitrage par l'évaluateur** : il n'a pas à tout relire, seulement les désaccords. Présente-les par code, en commençant par les codes centraux pour les questions d'évaluation. Il écrit « garder » ou « retirer » dans la colonne Décision. Les désaccords qu'il ne tranche pas suivent la majorité. Puis : `python codage_multiple.py arbitrer analyses/07-codage.json analyses/07-arbitrage.xlsx`
5. Un code dont le kappa moyen entre codeurs reste sous 0,6 est signalé : sa définition est sans doute ambiguë, et il se revoit avec l'évaluateur.

Dans les deux cas, lance ensuite :
`python verifier_citations.py codage analyses/07-codage.json donnees/transcriptions/ --ecrire`
Chaque ÉCHEC se corrige à partir du texte source, jusqu'à **100 % des citations trouvées**. Avec des unités, les citations sont exactes par construction.

Pour une analyse ciblée sur un passage plus court qu'une réponse, un segment peut contenir une citation partielle. Elle est copiée caractère par caractère, et une coupure se marque `[...]`.

## 6. Tableaux

`python codage.py tableaux analyses/07-codage.json analyses/07-livre-de-codes.json analyses/07-codage.xlsx`

Le classeur contient le livre de codes, les segments avec leurs positions, la matrice code x cas, la matrice code x profil et les co-occurrences.

## 7. Synthèse

Écris `analyses/07-synthese-qualitative.md`, organisée **par question de la matrice**. Pour chaque constat :
- le constat en une phrase ;
- sa fréquence : « 3 entretiens sur 3 », jamais « la majorité » sans chiffre ;
- les différences entre profils (sexe, âge, handicap, service) tirées de la feuille « Code x profil » ;
- 1 ou 2 citations au format « texte » (E01) ;
- les **cas divergents**, qui contredisent le constat.

Termine par les limites : taille et composition de l'échantillon, et rappel qu'un petit échantillon qualitatif éclaire des mécanismes mais ne se généralise pas en pourcentages.

Vérifie la synthèse : `python verifier_citations.py document analyses/07-synthese-qualitative.md donnees/transcriptions/`

Règles de la synthèse :
- chaque « n sur N » vient de `python codage.py compter analyses/07-codage.json --code <CODE> [--filtre type=Usager]` (règle de preuve) ;
- un attribut de profil que tu as déduit au lieu de le lire (statut d'utilisateur, par exemple) est marqué `(déduit)` (règle 10) ;
- les constats sont ventilés par composante de l'objet évalué quand il y en a plusieurs (règle 9) ;
- les **données promises** par les personnes interrogées (statistiques, rapports, chiffres par sexe) vont dans les « Points en attente » de `etat.md`, pour être réclamées.

**L'étape est terminée** quand aucun code utilisé n'est en ALERTE sans réserve écrite, que 100 % des citations sont vérifiées dans le codage et dans la synthèse, que chaque question de la matrice qui prévoit des entretiens a sa section, et que l'évaluateur a validé la synthèse. Propose alors l'étape 8, `triangulation`.
