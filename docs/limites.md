# Limites et questions fréquentes

## SERA est en bêta

Il a été testé sur des cas de formation, pas encore sur une large série de missions réelles. Relisez tout ce qu'il produit : c'est d'ailleurs ce qu'il vous demande.

## Ce que SERA ne fait pas (encore)

- **Les méthodes d'impact** (score de propension, double différence) ne sont pas couvertes.
- **L'outcome mapping, le Most Significant Change et l'évaluation réaliste** ne sont pas encore des skills à part entière.
- **La conformité à une charte ou à un référentiel national** (charte éthique IA, guide national d'évaluation) n'est pas vérifiée. Seules les normes OCDE-CAD, UNEG et ALNAP sont intégrées.
- **L'export vers KoboToolbox** (XLSForm) des questionnaires n'existe pas encore.
- **La transcription en langues locales** (fon, yoruba, wolof, bambara...) n'a pas de solution fiable. Une relecture humaine par un locuteur est obligatoire.
- **Une autre langue que le français** : SERA est en français uniquement.

## Questions fréquentes

**SERA remplace-t-il ATLAS.ti, NVivo ou R ?**
Non. SERA est une méthode guidée de bout en bout. Il reproduit certaines fonctions (codage, statistiques), mais son but est de vous accompagner d'une étape à l'autre, pas de remplacer un logiciel spécialisé.

**Les chiffres sont-ils fiables ?**
Chaque chiffre vient d'un notebook Python réellement exécuté, que vous pouvez relancer dans Colab. L'interprétation, elle, reste la vôtre : la revue critique est là pour la mettre à l'épreuve.

**Puis-je l'utiliser sur une mission payée ?**
Oui. La licence (CC BY 4.0 pour les textes, MIT pour les scripts) l'autorise, à condition de citer la source si vous redistribuez SERA ou une version modifiée.

**Quel modèle Claude choisir ?**
SERA propose trois profils (qualité, équilibré, économique) et vous conseille un modèle au début de chaque étape. Le profil équilibré est recommandé.

**Mes données sont-elles en sécurité ?**
Lisez [Données et confidentialité](donnees-et-confidentialite.md) : SERA encadre le risque, il ne le supprime pas.

**Ça marche avec une autre IA que Claude ?**
Oui, avec ChatGPT : le même plugin s'y installe, en mode Cowork (voir [Installer SERA](installer.md)). SERA a été écrit et testé d'abord avec Claude. Dans ChatGPT, les sous-agents (codeurs et relecteurs indépendants) et les profils de modèles peuvent ne pas fonctionner comme prévu : signalez-nous ce qui ne marche pas. Les autres IA ne sont ni testées ni prévues.
