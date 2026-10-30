---
name: revue-critique
description: "Relire de façon critique et contradictoire une matrice, des analyses, des constats ou un rapport d'évaluation, avec plusieurs relecteurs indépendants (statisticien, méthodologue, commanditaire, expert du secteur), contre-vérification sur les données et plan de correction (étape 9 bis de SERA). Utiliser quand l'utilisateur demande une relecture critique, un contrôle qualité, un avis extérieur, ou de relire « comme un bailleur » ce qui ne tient pas."
---

# Revue critique

Sources : OCDE-CAD (2010), section 1 (contrôle qualité) ; UNEG (2016), règle 5 (qualité de l'évaluation).

Lis d'abord `<skills>/sera/references/regles.md`, le fichier `etat.md`, puis [references/grilles.md](references/grilles.md).

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## Quand

- **Obligatoire** avant la version finale du rapport (étape 9).
- **Proposée**, sans être imposée, après la validation de la matrice (étape 3) et après les analyses (étapes 6 et 7) : une erreur repérée tôt ne se propage pas.
- **Sur demande**, à tout moment.

## 1. Choisir les relecteurs avec l'évaluateur

Propose les quatre profils par défaut, adaptés au sujet de l'évaluation, et laisse l'évaluateur en retirer, en ajouter ou les modifier :
1. **Statisticien** : solidité des chiffres et de leur interprétation ;
2. **Méthodologue qualitatif** (et usage de l'IA) : décomptes, codage, citations, statuts déduits ;
3. **Commanditaire** : par exemple un cadre du ministère ou de l'ONG qui commande. Il juge l'utilité pour décider, et les écarts aux TDR ;
4. **Expert du secteur** : par exemple télécoms, santé, éducation. Il juge les faits de contexte et la faisabilité des recommandations.

Pour une revue après la matrice, deux relecteurs suffisent souvent (commanditaire et méthodologue).

## 2. Lancer les relectures en parallèle

Lance **un sous-agent `relecteur` par profil, en même temps**, avec le modèle prévu pour les relecteurs par le profil de modèles (Opus ou Fable en profil qualité ou équilibré). Chacun reçoit :
- la liste des fichiers à lire dans le dossier : TDR, `etat.md`, matrice, notebooks et résultats, codage, constats, rapport, selon le moment ;
- sa grille, tirée de [references/grilles.md](references/grilles.md) ;
- cette consigne : « Tu relis ce dossier d'évaluation comme <profil>. Tu n'as pas participé à sa rédaction. Une erreur n'est recevable qu'avec sa preuve : la cellule, la ligne de notebook, le fichier et la citation. Classe chaque point en *erreur* (elle change ce que le document affirme) ou en *risque* (elle fragilise sans fausser). Donne une note de fiabilité et une note d'utilité sur 10, avec une phrase de justification. Termine par ce qui est solide. »

Les relecteurs ne reçoivent **pas** le raisonnement qui a produit le document, seulement le dossier.

Si les sous-agents ne sont pas disponibles (par exemple dans le chat), fais les relectures **l'une après l'autre**, en changeant explicitement de rôle et de grille à chaque passe.

## 3. Contre-vérifier avant de retenir

Les relecteurs peuvent se tromper. Pour chaque erreur signalée :
- revérifie-la sur les données : relance le calcul avec un script, relis la transcription, recompte avec `codage.py compter` ;
- **retiens-la** si elle est confirmée, **rejette-la** si le relecteur a mal lu, en disant pourquoi ;
- regroupe les erreurs signalées par plusieurs relecteurs.

Un fait de contexte apporté par un relecteur (une date, une réglementation, une mesure déjà en place) n'est pas vérifié par les données du dossier. Note-le comme « à confirmer avant usage », avec sa source s'il en donne une.

## 4. Livrable

Écris `analyses/09-revue-critique.md` (ou `03-revue-critique.md`, `07-revue-critique.md` selon le moment) :
1. **Notes** : fiabilité et utilité par relecteur, avec la phrase de justification, puis une note globale ;
2. **Erreurs retenues** : un tableau avec numéro, erreur, preuve, relecteurs, correction ;
3. **Erreurs rejetées** après contre-vérification, et pourquoi ;
4. **Risques**, groupés (méthode et données, sources non collectées, écarts aux TDR, recommandations) ;
5. **Ce qui est solide** ;
6. **Plan de correction** en trois blocs :
   - sans nouvelle collecte ;
   - avec l'évaluateur (recodage, arbitrages) ;
   - avec une collecte complémentaire.

Ajoute une ligne datée dans les « Décisions » de `etat.md`, et une alerte par erreur retenue dans `analyses/tableau-de-bord.json`.

## 5. Corriger

Présente le plan de correction à l'évaluateur. Après son accord, applique les corrections sans nouvelle collecte, puis relance les vérifications (citations, chiffres, décomptes). Les corrections qui demandent l'évaluateur ou une collecte vont dans les « Points en attente ».

**La revue est terminée** quand chaque erreur signalée est retenue ou rejetée après contre-vérification, que le plan de correction est validé par l'évaluateur, et que les corrections sans nouvelle collecte sont appliquées.
