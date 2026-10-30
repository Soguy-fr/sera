---
name: transcription
description: "Transcrire des enregistrements audio d'entretiens ou de focus groups, ou lire des documents scannés et des photos de fiches (OCR) : choix du service (Mistral Voxtral, Whisper local), locuteurs, horodatage, relecture (méthode SERA). Utiliser quand l'utilisateur a des fichiers audio, des PDF scannés ou des images de documents à exploiter dans une évaluation."
---

# Transcription audio et OCR

Lis d'abord `<skills>/sera/references/regles.md`.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## 1. Choisir l'outil avec l'évaluateur

| Besoin | Option recommandée | Coût indicatif (octobre 2026) | Points d'attention |
|---|---|---|---|
| Entretiens en **français** | API Mistral Voxtral Transcribe : identification des locuteurs, horodatage au mot | environ 0,003 à 0,004 $ par minute | Clé API Mistral nécessaire ; hébergement des données à vérifier dans le contrat |
| Données **très sensibles** | Whisper large-v3 en local, sur l'ordinateur de l'évaluateur | gratuit, mais lent sans carte graphique | Rien ne quitte l'ordinateur |
| **Langues locales** (fon, yoruba, wolof, bambara, pidgin...) | Aucun service généraliste n'a une qualité démontrée. Modèles Whisper adaptés aux langues africaines (Sunbird, MALIBA-AI pour le bambara) | variable | Taux d'erreur de 20 à 40 % au mieux. **Relecture humaine par un locuteur obligatoire**, ou transcription-traduction humaine |
| **Documents scannés**, photos de fiches | Lecture directe par Claude pour quelques pages ; Mistral OCR pour un gros volume | environ 4 $ pour 1000 pages | Vérifier les chiffres recopiés |

Ces prix et capacités évoluent : vérifie-les sur la documentation officielle avant de les citer dans une offre.

## 2. Transcrire

- Garde les fichiers originaux dans `sources/`, et écris les transcriptions brutes dans `sources/transcriptions/`.
- Une transcription par entretien, nommée par son code (`E01.txt`). En tête, mets le profil de la personne interrogée, sans son nom.
- Les locuteurs sont notés `Enquêteur :` et `E01 :`. Pour un focus group, `P1 :`, `P2 :`...
- Un passage inaudible se marque `[inaudible 00:12:30]`, et une traduction `[traduit du fon]`.
- Pour l'API Mistral, la clé API ne s'écrit jamais en clair dans un fichier ni dans la conversation : l'utilisateur la place lui-même dans une variable d'environnement.

## 3. Relire

Fais relire un échantillon par l'évaluateur, au moins 10 % du corpus et un extrait de chaque enregistrement de mauvaise qualité. Corrige les noms propres et le vocabulaire local. Ensuite, passe par `anonymisation` avant toute analyse.

**La transcription est terminée** quand chaque enregistrement a sa transcription, que chaque passage inaudible ou traduit est marqué, et que la relecture de l'échantillon est faite.
