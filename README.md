# SERA : Suivi, Évaluation, Redevabilité, Apprentissage

**Une méthode guidée d'évaluation de projets et de politiques publiques, pour Claude et ChatGPT.** SERA accompagne l'évaluateur pas à pas, des termes de référence à la restitution, comme le ferait un évaluateur senior : il propose, explique et vérifie. **Le jugement reste le vôtre.**

> **Bêta.** SERA est en cours de test. Vos retours sont précieux : [donnez votre avis](https://forms.gle/tNVJDj6FbKduRwCS8).

## Pour qui

- Les consultants et consultantes en évaluation, juniors ou confirmés.
- Les équipes de suivi-évaluation (S&E, MEAL) des ONG et des institutions.
- Les experts seniors qui veulent voir ce que l'IA peut faire, et ce qu'elle ne doit pas faire, dans une évaluation.

## Ce que fait SERA

| | |
|---|---|
| **Il guide** | 10 étapes, du cadrage des TDR à la restitution, selon les normes OCDE-CAD, UNEG et ALNAP |
| **Il explique** | un mode pédagogique pour chaque notion, et pourquoi tel choix plutôt qu'un autre |
| **Il fait réfléchir** | aux moments où se joue le jugement, il vous interroge avant de proposer |
| **Il vérifie** | aucun chiffre sans calcul exécuté, aucune citation sans vérification mot pour mot, une revue critique avant le rapport |
| **Il prend en charge la technique** | matrice en Excel, notebook Python ouvrable dans Colab, codage des entretiens, rapport en Word |

Le détail : [les étapes](docs/etapes.md).

## Ce que SERA ne fait pas

- Il ne remplace pas l'évaluateur : il instruit, vous jugez et vous signez.
- Il ne garantit pas que vos données ne passent pas par l'IA. Il encadre ce risque : pseudonymisation, vérification avant chaque livrable. Lisez [Données et confidentialité](docs/donnees-et-confidentialite.md) avant de l'utiliser sur de vraies données.
- Il ne couvre pas encore tout : voir [Limites et questions fréquentes](docs/limites.md).

## Installer

Le guide pas à pas, avec le guide PDF « Prendre en main SERA » : [shauri.cc/sera](https://www.shauri.cc/sera).

- **Dans Claude** (abonnement payant, de préférence l'application avec **Cowork**) : **Personnaliser → Plugins → Ajouter → Ajouter une marketplace → Ajouter depuis un dépôt**, tapez `Soguy-fr/sera`, puis **Synchro**, et installez SERA.
- **Dans ChatGPT** (l'offre gratuite suffit) : téléchargez `sera-chatgpt-<version>.zip` dans les [Releases](https://github.com/Soguy-fr/sera/releases), passez en mode **Cowork** et ajoutez-le comme plugin au format ZIP.

Connectez ensuite un dossier contenant vos TDR, et écrivez : « Je démarre une évaluation avec SERA, voici les TDR. »

Claude Code, mode dégradé, problèmes fréquents : [Installer SERA](docs/installer.md).

## Essayer sans vos données

Le dossier [exemples/cas-fictif](exemples/cas-fictif/) contient un cas d'évaluation entièrement inventé : des TDR, une base d'enquête brute et 10 entretiens. Suivez le [premier parcours](docs/premier-parcours.md).

## Licence

- Les textes (skills, documentation, cas fictif) sont sous licence [CC BY 4.0](LICENSE).
- Les scripts Python sont sous licence [MIT](LICENSE-MIT).

Vous pouvez utiliser SERA librement, y compris pour des missions payées. Si vous le redistribuez ou le modifiez, citez la source : « SERA, Shauri ».

## Proposé par Shauri

SERA est offert par [Shauri](https://shauri.cc), qui propose des formations et un accompagnement pour utiliser l'IA en suivi-évaluation.
