---
name: rapport
description: "Rédiger ou relire le rapport d'évaluation (provisoire ou final) en Word : résumé exécutif, méthode et limites, constats, conclusions, recommandations avec mandat, coût et risques, couverture des TDR (étape 9 de SERA). Utiliser dès que l'utilisateur demande de rédiger, écrire, structurer ou relire un rapport d'évaluation, un résumé exécutif ou des recommandations."
---

# Étape 9 : rapport et recommandations

Sources : ALNAP (2016) ch. 17 ; UNEG (2016) règles 4.9 et 4.10 ; OCDE-CAD (2010) section 3.

Lis d'abord `<skills>/sera/references/regles.md`, le fichier `etat.md`, `analyses/08-constats.md` et la matrice. Si les TDR imposent un plan de rapport, il prime sur celui-ci.

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## 1. Couverture des TDR

Avant de rédiger, confronte la section « Exigences des TDR » de `etat.md` à ce que les constats permettent de couvrir. Présente le tableau à l'évaluateur : exigence, couverte ou non, où dans le rapport. Une exigence non couverte est soit traitée, soit justifiée dans les limites. On ne la passe jamais sous silence.

## 2. Plan par défaut

1. Résumé exécutif (2 pages au plus : objet, méthode, principales conclusions, recommandations)
2. Introduction : contexte, objet, objectifs et utilisateurs de l'évaluation
3. Méthodologie : TOC (schéma `02-toc.png`), matrice (en annexe), collecte, échantillons réalisés, analyse, **limites**, éthique et protection des données
4. Encadré **« Ce que l'évaluation ne permet pas de dire »** : par exemple un effet attribuable sans groupe de comparaison, une composante à faible effectif, des populations non atteintes, des pourcentages non extrapolables (échantillon par quotas)
5. Constats, par critère puis par question, avec la réponse étayée et le jugement de l'évaluateur
6. Conclusions
7. Leçons apprises et bonnes pratiques
8. Recommandations
9. Annexes : TDR, matrice, outils, tableau de couverture des TDR, liste des personnes rencontrées (fonctions, pas de noms de répondants), bibliographie

## 3. Recommandations (point de jugement J5)

Avant de proposer, demande à l'évaluateur, en un round court et sans ta recommandation (règle 11) : quelles pistes il retient, et ce qui est réaliste chez ce commanditaire. Puis complète chaque recommandation avec cette grille :

| Champ | Question à se poser |
|---|---|
| Conclusion d'origine | De quelle conclusion découle-t-elle ? (numéro de l'étape 8) |
| Destinataire et mandat | Le destinataire a-t-il le pouvoir d'agir ? Sinon, qui l'a (ministère sectoriel, régulateur, collectivité) ? |
| Priorité | Haute, moyenne ou basse |
| Coût | Ordre de grandeur (faible, moyen, élevé), ou estimation si elle est possible |
| Risque | Effet pervers ou fraude possible (par exemple un paiement déclaré sans preuve vérifiable) |
| Existant | La mesure existe-t-elle déjà ? À vérifier dans les sources, pour ne pas recommander ce qui est en place |

Il en faut 5 à 10 : au-delà, aucune n'est suivie. Les identifiants (R1, R2...) sont ceux de l'étape 8.

## 4. Rédiger

Écris `analyses/09-rapport.md`, chapitre par chapitre. Montre à l'évaluateur chaque chapitre important (constats, recommandations) avant de passer au suivant.

- Un constat = un chiffre ou un fait sourcé, et son interprétation. Le **degré de solidité** vient de l'étape 8.
- Les mots du jugement suivent la règle 8.
- Les citations se notent « texte » (E05, femme, 35-44 ans) : le profil sans le nom.
- Les affirmations de méthode (consentement, nombre d'entretiens) s'appuient sur une trace du dossier.
- Le résumé exécutif s'écrit **en dernier**.

## 5. Revue critique, puis vérifications

1. **Revue critique** : obligatoire avant la version finale (skill `revue-critique`). Applique ensuite son plan de correction.
2. **Citations** : `python <skills>/analyse-qualitative/scripts/verifier_citations.py document analyses/09-rapport.md donnees/transcriptions/`, jusqu'à 100 %.
3. **Chiffres** : relis chaque chiffre du rapport et retrouve-le dans un notebook ou un tableau de résultats, avec son n. Corrige ou retire ce que tu ne retrouves pas.
4. **Données personnelles** : `python <skills>/anonymisation/scripts/pseudonymiser.py verifier sources/table-correspondance.csv analyses/09-rapport.md`, si une table existe.
5. **Word** : `python <skills>/rapport/scripts/md_vers_docx.py analyses/09-rapport.md livrables/09-rapport.docx --pied "Version provisoire - <date> - préparé avec l'assistance de SERA (IA), validé par <évaluateur>"`

Si le rapport est rédigé ailleurs (Claude Doc, par exemple), exporte-le dans `livrables/`, ou au moins référence son lien dans `etat.md`.

**L'étape est terminée** quand la revue critique a été faite et ses corrections appliquées, que les vérifications passent, que chaque exigence des TDR est couverte ou justifiée, que chaque recommandation a sa grille complète, et que l'évaluateur a validé le rapport.
