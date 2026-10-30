# Grilles des relecteurs

Chaque relecteur parcourt sa grille point par point. Les exemples viennent d'erreurs réellement commises par un assistant IA lors d'un test de SERA. Chaque grille se termine par la même question : « qu'est-ce qui est solide ? ».

## Statisticien

1. **Absence de preuve** : un test non significatif est-il présenté comme une preuve d'absence (« identique », « aucune différence ») ? L'intervalle de l'écart est-il donné ? *Exemple : « gain identique selon le sexe » avec 10 femmes, alors que l'écart réel peut aller de -43 à +44 minutes.*
2. **Effet de composition** : un écart entre groupes peut-il venir d'une autre variable ? A-t-il été vérifié par stratification ? *Exemple : un écart femmes-hommes sur l'utilité perçue qui disparaît chez les seuls utilisateurs.*
3. **Tests multiples** : combien de tests ? Les résultats cités résistent-ils à la correction de Holm ?
4. **Inférence** : l'échantillon est-il aléatoire ? Si non, le document annonce-t-il une marge d'erreur ou des pourcentages valables pour la population ? Un quota fixe-t-il un taux observé ?
5. **Dénominateurs** : chaque pourcentage a-t-il son n, et le même n partout pour le même indicateur ?
6. **Classements** : chaque « principal », « le plus », « la majorité » est-il conforme au tableau ?
7. **Composantes** : les résultats mélangent-ils des composantes différentes (par exemple état civil et factures) ?
8. **Attribution** : le document parle-t-il d'effet là où il n'y a qu'une association ?

## Méthodologue qualitatif (et usage de l'IA)

1. **Décomptes** : chaque « n sur N » est-il exact ? Recompte avec `codage.py compter`. *Exemple : « 5 institutions sur 5 » alors que l'une parle d'autre chose.*
2. **Codes validés** : les codes centraux ont-ils été calibrés avec un humain ? Quel kappa ? Un code à kappa faible porte-t-il une conclusion ?
3. **Accord présenté** : l'accord brut, gonflé par les « absent / absent », est-il présenté seul ?
4. **Statuts déduits** : des attributs de profil ont-ils été déduits par l'IA au lieu d'être déclarés ? *Exemple : des « non-utilisateurs » dont le foyer paie en ligne (usage délégué).*
5. **Citations** : existent-elles mot pour mot, avec le bon profil ? Sont-elles représentatives, ou choisies pour illustrer une thèse ?
6. **Cas divergents** : sont-ils cherchés et expliqués ?
7. **Affirmations de méthode** : « consentement recueilli », « saturation atteinte »... ont-elles une trace dans le dossier ?
8. **Circularité** : si les données sont fictives ou simulées, le document le dit-il, et ne présente-t-il pas comme découvertes les hypothèses du générateur ?

## Commanditaire

1. **Couverture des TDR** : chaque objectif spécifique, critère et livrable demandé est-il traité ou justifié ? *Exemple : la TOC, objectif n° 1, jamais reconstituée.*
2. **Utilité pour décider** : le document donne-t-il les chiffres qu'un décideur demande en premier (volumes, ventilation par service, coûts) ?
3. **Ce que l'évaluation ne permet pas de dire** : est-ce écrit clairement ?
4. **Bonnes pratiques** : sont-elles identifiées, si les TDR les demandent ?
5. **Données promises** : les données administratives proposées par les acteurs ont-elles été récupérées ?
6. **Acteurs absents** : manque-t-il des institutions clés dans l'échantillon ?
7. **Ton** : les constats sensibles sont-ils assez étayés pour résister à la contestation ?

## Expert du secteur

1. **Faits de contexte** : dates, réglementations, mesures déjà en place sont-elles exactes et à jour ? Toujours donner la source, et noter « à confirmer ».
2. **Variables manquantes** : le questionnaire distingue-t-il ce que le secteur distingue (par exemple prépayé / postpayé, titulaire du compteur, canal utilisé) ?
3. **Destinataires des recommandations** : ont-ils le mandat et le levier pour agir ? Qui régule le secteur ?
4. **Faisabilité et risques** : une recommandation crée-t-elle un risque (fraude, effet pervers) ? Existe-t-elle déjà ?
5. **Coûts** : un ordre de grandeur est-il donné ?
6. **Recommandations manquantes** : qu'est-ce qu'un expert du secteur attendrait et qui n'y est pas ?
