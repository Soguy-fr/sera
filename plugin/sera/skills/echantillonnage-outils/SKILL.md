---
name: echantillonnage-outils
description: "Calculer une taille d'échantillon et choisir qui interroger (enquête, entretiens, focus groups, quotas, désagrégation), puis rédiger les outils de collecte (questionnaire, guide d'entretien, guide de focus group) tracés vers la matrice (étape 4 de SERA). Utiliser quand l'utilisateur demande combien de personnes interroger, comment échantillonner, ou veut un questionnaire ou un guide d'entretien."
---

# Étape 4 : échantillonnage et outils de collecte

Sources : ALNAP (2016) ch. 10 à 15. Lis d'abord `<skills>/sera/references/regles.md`, le fichier `etat.md`, puis la matrice (`<skills>/matrice-evaluation/scripts/matrice.py lire matrice-evaluation.xlsx`).

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## Contexte minimal (entrée directe)

Sans matrice validée, demande ce qu'on cherche à savoir, auprès de qui, avec quels moyens (jours de terrain, enquêteurs) et quelles contraintes (accès, sécurité, langues).

## 1. Échantillon quantitatif

Calcule avec `python <skills>/echantillonnage-outils/scripts/taille_echantillon.py` et les paramètres validés par l'évaluateur. Ils sont tous expliqués dans la sortie du script.

- Une **marge** de 5 points et une **confiance** de 95 % sont les valeurs par défaut courantes.
- Un **effet de plan** de 1,5 à 2 s'applique si l'on tire des grappes (quartiers, écoles) avant les personnes.
- `--groupes` s'emploie si les TDR demandent des résultats **par** groupe (femmes et hommes, zones) : donner les noms (`"Femmes,Hommes"`) ou le nombre de groupes (`2`). Sinon, la désagrégation reste indicative.

- `--tirage quotas` s'emploie dès que le tirage n'est pas aléatoire (quotas, choix raisonné). Le script donne alors la taille comme un simple repère, **sans marge d'erreur**. Ne présente jamais de marge d'erreur pour un échantillon non aléatoire : ni « ± », ni fourchette (« entre 36 % et 64 % »), ni marge « indicative » ou « comme repère ». Dis seulement que les résultats décrivent les personnes interrogées et ne s'extrapolent pas.

Explique en deux phrases ce que permet et ne permet pas cet échantillon. Décris le mode de tirage : aléatoire, stratifié, par grappes, ou par quotas (moins rigoureux, à signaler comme limite).

## 2. Échantillon qualitatif

Le choix est **raisonné**, pas aléatoire. Pour chaque groupe d'acteurs de la matrice, indique qui interroger, combien, et pourquoi :
- les profils à couvrir, avec la diversité demandée par les TDR (femmes, personnes âgées, personnes en situation de handicap, non-usagers) ;
- un repère courant : 8 à 12 entretiens par groupe homogène suffisent souvent à voir les thèmes principaux se répéter (saturation) ; 2 à 4 focus groups de 6 à 10 personnes par catégorie ;
- les **non-usagers** et les cas défavorables, que l'on oublie souvent et qui éclairent les barrières.

## 3. Outils de collecte

Pour chaque outil prévu par la matrice (questionnaire, guide d'entretien, guide de focus group, grille d'observation), écris un Markdown dans `analyses/04-<outil>.md` :
- un en-tête : consentement éclairé, anonymat, droit de refuser, durée estimée ;
- les questions dans un ordre naturel, des plus simples aux plus sensibles ;
- après chaque question, l'**identifiant de la matrice** qu'elle alimente (`[Q2.1]`).
  - Pour un questionnaire : réponses fermées avec modalités, et filtres (« si non, passer à 12 »).
  - Pour un guide d'entretien : questions ouvertes, sans induire la réponse, avec des relances.

**Variables souvent oubliées.** Pour tout questionnaire sur l'usage d'un service, propose à l'évaluateur :
- **qui fait la démarche** : moi-même seul / moi avec de l'aide / un tiers à ma place. C'est ce qui distingue l'usage autonome, l'usage délégué et le non-usage ;
- **le canal** utilisé (application, site, USSD, agent, guichet) ;
- **le titulaire** du compte, de l'abonnement ou du compteur ;
- **la fréquence et le montant** des démarches ou des paiements, pour calculer un coût annuel et pas seulement un coût par démarche ;
- **l'expérience d'un incident**, et sa résolution ;
- **la composante concernée** (par exemple état civil ou factures), pour pouvoir ventiler les résultats.

Vérifie la **couverture** dans les deux sens : chaque ligne de la matrice qui prévoit cet outil a au moins une question, et chaque question sert une ligne de la matrice. Supprime les questions qui ne servent à rien : elles allongent la collecte sans rien apporter.

Convertis en Word pour l'équipe terrain : `python <skills>/rapport/scripts/md_vers_docx.py analyses/04-<outil>.md livrables/04-<outil>.docx`

Écris enfin `analyses/04-echantillonnage.md`, avec les échantillons, leurs justifications, les limites et le tableau de couverture.

**L'étape est terminée** quand chaque ligne de la matrice a son outil et ses questions, que chaque question est tracée vers la matrice, que les tailles d'échantillon sont calculées et justifiées, et que l'évaluateur a validé les outils.
