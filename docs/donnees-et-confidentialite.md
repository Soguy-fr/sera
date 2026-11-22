# Données et confidentialité

C'est la première question que se pose un évaluateur, et elle est légitime : des entretiens, des bases d'enquête, des noms de répondants. Voici ce que SERA fait pour vos données, et surtout ce qu'il **ne garantit pas**.

## Le point de départ

SERA est un ensemble de consignes pour votre assistant, Claude ou ChatGPT. Quand l'assistant lit un fichier de votre dossier d'évaluation, le contenu de ce fichier est envoyé aux serveurs de son éditeur pour être traité : Anthropic pour Claude, OpenAI pour ChatGPT. **SERA ne change rien à cela.**

Sans outil, beaucoup d'évaluateurs envoient déjà leurs transcriptions à une IA, sans précaution. SERA **encadre** ce risque : il le réduit et le rend visible. Il ne le supprime pas.

## Avant de commencer

1. **Vérifiez que vous en avez le droit.** Le contrat avec le commanditaire, le protocole de collecte ou le consentement des répondants peuvent interdire le traitement des données par un service d'IA externe. Dans ce cas, n'utilisez pas SERA sur ces données, ou seulement sur des données déjà pseudonymisées.
2. **Désactivez l'utilisation de vos conversations pour l'entraînement.** Dans Claude : Paramètres → Confidentialité → « Aider à améliorer Claude ». Dans ChatGPT : Paramètres → Gestion des données → « Améliorer le modèle pour tout le monde ». SERA vous le demande au démarrage de chaque évaluation. Il ne peut pas lire ce réglage lui-même : il vous fait confiance.
3. **Lisez les conditions de votre abonnement.** Les offres d'entreprise n'ont pas les mêmes conditions que les offres individuelles, et l'offre gratuite de ChatGPT non plus. En cas de doute, demandez à votre organisation.
4. **Pensez au consentement.** Pour une nouvelle collecte, envisagez de mentionner dans le formulaire de consentement que des outils d'IA servent à l'analyse.

## Ce que SERA fait

- **Un dossier qui sépare le brut du traité.** Les données brutes restent dans `sources/`, et ce dossier n'est jamais partagé. Les analyses portent sur des versions pseudonymisées, rangées dans `donnees/`.
- **La pseudonymisation avant toute analyse.** La skill `anonymisation` repère deux sortes d'identifiants :
  - les identifiants directs : noms, téléphones, adresses ;
  - les identifiants indirects : par exemple « la seule pharmacienne du quartier ».

  Elle vous soumet la liste, puis remplace les identifiants par des codes (`[E05]`, `[quartier A]`). La table de correspondance reste dans `sources/`.
- **Une vérification par script.** Avant chaque livrable, un script cherche dans les fichiers produits chaque original de la table de correspondance. Un livrable qui contient encore un nom ne part pas.
- **Des livrables sans personne reconnaissable.** Ni nom, ni téléphone, ni combinaison de détails qui désignerait un répondant.
- **Une transcription au choix.** Pour des enregistrements très sensibles, SERA conseille une transcription locale (Whisper sur votre ordinateur), où rien ne quitte votre machine.

## Ce que SERA ne garantit pas

- **Les données passent par l'IA.** Même pseudonymisées, elles sont traitées par l'assistant. Et pour pseudonymiser, l'assistant doit d'abord lire les originaux, sauf si vous pseudonymisez vous-même avant.
- **Une table ne trouve que ce qu'on y a mis.** Un identifiant oublié reste en clair. Une relecture humaine complète reste indispensable : SERA vous la demande, il ne peut pas la faire à votre place.
- **La table de correspondance est sur votre ordinateur.** Sa protection (chiffrement, sauvegarde, accès) est de votre responsabilité.
- **Les services tiers ont leurs propres conditions.** Si vous utilisez un service externe de transcription ou d'OCR (Mistral par exemple), vos fichiers lui sont envoyés. Vérifiez où il héberge les données.

## Pour les données les plus sensibles

Violences basées sur le genre, protection de l'enfance, personnes en danger, données de santé : pseudonymisez **vous-même, avant** de donner les fichiers à Claude, ou travaillez sans IA sur ces données. SERA peut vous aider sur la méthode (matrice, outils de collecte, plan d'analyse) sans jamais voir les données.

## Les annonces Shauri

Au démarrage et en fin d'évaluation, SERA affiche une courte annonce de Shauri (formations). Pour cela, un script **lit** un fichier public sur GitHub. Il n'envoie aucune donnée de votre évaluation. Pour ne plus les voir, écrivez « sans annonces ».

## Le cas fictif

Le cas d'exemple (`exemples/cas-fictif/`) est entièrement inventé : aucune donnée réelle, aucune personne réelle.
