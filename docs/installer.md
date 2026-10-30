# Installer SERA

## Ce qu'il faut

- Un **abonnement Claude payant** : Pro, Max, Team ou Enterprise.
- De préférence l'**application Claude avec Cowork**, ou **Claude Code**. SERA a besoin d'un dossier qui persiste d'une conversation à l'autre, et de Python pour ses calculs et ses vérifications.
- Dans le chat claude.ai seul, SERA fonctionne en **mode dégradé** : rien n'est enregistré entre deux conversations, et il le rappelle à chaque réponse. C'est suffisant pour essayer une étape, pas pour mener une évaluation.

## Application Claude (Cowork ou chat)

1. Téléchargez le fichier `sera-<version>.zip` depuis la page [Releases](https://github.com/Soguy-fr/sera/releases) du dépôt. Ne le décompressez pas.
2. Dans l'application Claude : **Personnaliser → Plugins → Ajouter → Téléverser un plugin**, puis choisissez le zip.
3. Dans **Paramètres → Capacités**, vérifiez que l'exécution de code est activée.
4. Vérifiez que les skills SERA apparaissent dans la liste des plugins.

Pour une mise à jour, téléversez le zip de la nouvelle version.

## Claude Code

```
claude plugin marketplace add Soguy-fr/sera
claude plugin install sera@sera
```

Pour une mise à jour : `claude plugin marketplace update sera`.

## Démarrer une évaluation

1. **Créez un dossier** pour votre évaluation sur votre ordinateur, et mettez les TDR dedans.
2. **Connectez ce dossier** à Claude. Dans Cowork : « + » → « Add folder ». Dans Claude Code : lancez `claude` depuis ce dossier.
3. **Désactivez l'entraînement sur vos conversations** : Paramètres → Confidentialité. Voir [Données et confidentialité](donnees-et-confidentialite.md).
4. Écrivez : « Je démarre une évaluation avec SERA, voici les TDR. »

SERA crée ses sous-dossiers (`sources/`, `donnees/`, `analyses/`, `livrables/`) et un fichier d'état, `etat.md`, qui lui permet de reprendre là où vous vous êtes arrêté.

Pour un premier essai sans vos propres données, suivez le [premier parcours](premier-parcours.md) sur le cas fictif.

## En cas de problème

- **SERA ne se déclenche pas** : nommez-le dans votre message (« avec SERA »), ou écrivez « sera aide ».
- **Python manque une bibliothèque** dans Cowork : c'est normal, SERA l'installe en début de session. Cowork n'a accès qu'à PyPI et GitHub.
- **Les fichiers disparaissent** : aucun dossier n'est connecté, et SERA est en mode dégradé.
