# Installer SERA

## Ce qu'il faut

SERA fonctionne dans **Claude** ou dans **ChatGPT**. Il a besoin d'un dossier qui persiste d'une conversation à l'autre, et de Python pour ses calculs et ses vérifications.

- **Claude** : un abonnement payant (Pro, Max, Team ou Enterprise), et de préférence l'**application Claude avec Cowork**, ou **Claude Code**.
- **ChatGPT** : l'offre gratuite suffit, en **mode Cowork**, avec un projet auquel vous connectez le dossier de l'évaluation.
- Dans le chat claude.ai seul, SERA fonctionne en **mode dégradé** : rien n'est enregistré entre deux conversations, et il le rappelle à chaque réponse. C'est suffisant pour essayer une étape, pas pour mener une évaluation.

## Application Claude (Cowork ou chat)

1. Dans l'application Claude, ouvrez **Personnaliser**, puis l'onglet **Plugins**. Cliquez sur **Ajouter** et choisissez **Ajouter une marketplace**.
2. Choisissez **Ajouter depuis un dépôt**.
3. Dans le champ URL, tapez `Soguy-fr/sera`, puis cliquez sur **Utiliser « Soguy-fr/sera »**.
4. Laissez **Synchroniser automatiquement** activé, puis cliquez sur **Synchro**. Claude affiche un avertissement sur les sources de confiance : c'est normal.
5. SERA apparaît dans la liste : cliquez sur **Ajouter** à côté de lui.

Avec la synchronisation automatique, SERA se met à jour tout seul.

**Autre méthode, par fichier** : téléchargez `sera-claude-<version>.zip` depuis la page [Releases](https://github.com/Soguy-fr/sera/releases), sans le décompresser, puis **Personnaliser → Plugins → Ajouter → Téléverser un plugin**. Pour une mise à jour, il faut téléverser à nouveau le fichier de la nouvelle version.

## Claude Code

```
claude plugin marketplace add Soguy-fr/sera
claude plugin install sera@sera
```

Pour une mise à jour : `claude plugin marketplace update sera`.

## ChatGPT

SERA s'installe tel quel dans ChatGPT : c'est le même plugin. L'offre gratuite suffit.

1. Téléchargez `sera-chatgpt-<version>.zip` depuis la page [Releases](https://github.com/Soguy-fr/sera/releases), sans le décompresser.
2. Passez ChatGPT en mode **Cowork**, ajoutez un plugin au format ZIP et choisissez ce fichier.
3. Créez un **projet** et connectez-y le dossier de votre évaluation, pour que ChatGPT puisse lire et écrire vos fichiers.

Pour une mise à jour, ajoutez le fichier de la nouvelle version.

## Démarrer une évaluation

1. **Créez un dossier** pour votre évaluation sur votre ordinateur, et mettez les TDR dedans.
2. **Connectez ce dossier** à votre assistant. Dans Cowork : « + » → « Add folder ». Dans Claude Code : lancez `claude` depuis ce dossier. Dans ChatGPT : connectez-le à votre projet.
3. **Désactivez l'entraînement sur vos conversations** : dans Claude, Paramètres → Confidentialité ; dans ChatGPT, Paramètres → Gestion des données → « Améliorer le modèle pour tout le monde ». Voir [Données et confidentialité](donnees-et-confidentialite.md).
4. Écrivez : « Je démarre une évaluation avec SERA, voici les TDR. »

SERA crée ses sous-dossiers (`sources/`, `donnees/`, `analyses/`, `livrables/`) et un fichier d'état, `etat.md`, qui lui permet de reprendre là où vous vous êtes arrêté.

Pour un premier essai sans vos propres données, suivez le [premier parcours](premier-parcours.md) sur le cas fictif.

## En cas de problème

- **SERA ne se déclenche pas** : nommez-le dans votre message (« avec SERA »), ou écrivez « sera aide ».
- **Python manque une bibliothèque** dans Cowork : c'est normal, SERA l'installe en début de session. Cowork n'a accès qu'à PyPI et GitHub.
- **Les fichiers disparaissent** : aucun dossier n'est connecté, et SERA est en mode dégradé.
