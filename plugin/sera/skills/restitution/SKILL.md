---
name: restitution
description: "Préparer la restitution et la diffusion des résultats d'une évaluation : présentation PowerPoint adaptée au public, atelier de validation, note de synthèse, plan de diffusion, réponse de la direction et suivi des recommandations (étape 10 de SERA). Utiliser quand l'utilisateur prépare une restitution, un atelier de validation, une présentation des résultats ou la diffusion d'un rapport."
---

# Étape 10 : restitution et diffusion

Sources : UNEG (2016) règles 4.11 (communication et diffusion) et 1.4 (réponse de la direction et suivi) ; OCDE-CAD (2010) section 4.

Lis d'abord `<skills>/sera/references/regles.md`, le fichier `etat.md` et le rapport (`analyses/09-rapport.md`).

**Format de chaque réponse qui donne un chiffre, un avis ou attend une décision** (même pour une question directe) : blocs 📍 Où on en est, 🔎 Ce que j'ai constaté, 💭 Mon analyse, 💡 Mes conseils, ❓ Vos décisions, ➡️ Ensuite, dans cet ordre, sans bloc vide (détail : règle 13 de `<skills>/sera/references/regles.md`).

## 1. Public et format

Demande à l'évaluateur à qui s'adresse la restitution (décideurs, équipe de projet, bénéficiaires, partenaires) et combien de temps elle dure. Adapte le message :
- **décideurs** : 3 à 5 messages clés et les recommandations prioritaires ;
- **équipe de projet** : constats détaillés et pistes opérationnelles ;
- **communautés** : résultats concrets, en langage simple, sans jargon, dans la langue du public si possible.

## 2. Présentation

Écris `analyses/10-restitution.json` (format dans `<skills>/restitution/scripts/plan_vers_pptx.py`), à raison d'une idée par diapositive et de 40 mots au plus à l'écran. Le détail va dans les notes de l'orateur. Réutilise les schémas et graphiques déjà produits (`02-toc.png`, graphiques des notebooks).

`python <skills>/restitution/scripts/plan_vers_pptx.py analyses/10-restitution.json livrables/10-restitution.pptx [--modele <charte du commanditaire>.pptx]`

## 3. Atelier de validation

Prépare pour l'atelier :
- les questions à poser aux participants sur chaque conclusion (« est-ce conforme à votre expérience ? qu'est-ce qui manque ? ») ;
- une grille pour noter les réactions, qui seront intégrées dans le rapport final.

## 4. Réponse de la direction et suivi

Prépare `livrables/10-reponse-direction.docx` avec `md_vers_docx.py`. Il contient un tableau : recommandation, destinataire, accepté / partiellement / refusé, actions prévues, responsable, échéance. Le commanditaire le remplit. Propose un plan de diffusion : qui reçoit quoi, sous quel format et quand.

**L'étape est terminée** quand la présentation, la grille de l'atelier et le tableau de réponse de la direction sont produits et validés par l'évaluateur.
