# Règles et équipement

Cette section regroupe les références de l'app : **Règles**, **Dons**, **Glossaire**, **Sorts** et **Équipement**.

Les champs restent libres, afin de s'adapter à ta campagne. Pour obtenir des filtres plus propres et des regroupements plus utiles, utilise toutefois des valeurs cohérentes.

## Fonctionnement de la recherche

La recherche rapide de la topbar vérifie plusieurs champs à la fois.

Pour les **règles**, elle cherche dans :

- nom
- catégorie
- prérequis
- type de règle
- école
- description

Pour l'**équipement**, elle cherche dans :

- nom
- catégorie
- CA
- dégâts
- propriétés
- utilisation
- description

## Dons

Pour les dons, le champ le plus utile pour classer les entrées est **catégorie**.

Exemples :

- `Origine`
- `Général`
- `Combat`
- `Magie`

Les **prérequis** servent à comprendre rapidement qui peut prendre le don. Garde-les courts, par exemple `Niveau 4`, `Force 13+`, `Lanceur de sorts`.

## Glossaire

Le glossaire sert aux termes, conditions, règles fréquentes et rappels de table.

Utilise **type de règle** ou **catégorie** pour regrouper les entrées similaires.

Exemples :

- `Condition`
- `Action`
- `Déplacement`
- `Jet de sauvegarde`

La description doit rester claire et directe, pour être utile pendant la partie.

## Sorts

Les sorts sont plus structurés, car ils sont aussi utilisés en combat lorsqu'ils sont associés aux personnages.

Pour des regroupements fiables :

- pour les **tours de magie**, choisis `Tour de magie` dans le menu du niveau
- pour les autres sorts, choisis un niveau de `1` à `9`
- dans **classes**, sépare les noms par des virgules, par exemple `Magicien, Clerc, Druide`
- dans **école**, indique seulement le nom de l'école, par exemple `Invocation`

Évite les valeurs comme `Invocation de niveau 3` dans le champ école : le niveau a déjà son champ et l'école fonctionne mieux lorsqu'elle reste propre.

### Champs utiles

Renseigne avec soin :

- **temps d'incantation**
- **portée**
- **composantes**
- **durée**
- **description**
- **niveaux supérieurs**

Ces informations apparaissent dans la fenêtre de détail du sort et permettent de le consulter sans ouvrir de manuel externe.

## Sorts en combat

Si des sorts sont associés à un personnage, ils apparaissent dans sa fiche de combat, regroupés par niveau.

La section affiche aussi les informations d'incantation disponibles, comme le bonus d'attaque des sorts, le DD de sauvegarde et les emplacements.

Pour les **PNJ et monstres**, le bouton `Utiliser` sur un sort augmente le compteur d'emplacements utilisés pour ce niveau. C'est un rappel pour le MJ : il ne bloque pas l'incantation, mais indique clairement quand la limite prévue est atteinte.

Les tours de magie ne consomment pas d'emplacement.

## Équipement

L'équipement est divisé en :

- armes
- armures
- outils
- équipement d'aventure

Les champs restent libres, mais des valeurs cohérentes rendent la recherche beaucoup plus efficace.

## Armes

Pour les armes, les champs les plus importants sont **catégorie**, **dégâts** et **propriétés**.

Exemples :

- catégorie : `Simple`, `Guerre`, `À distance`
- dégâts : `1d8 perforants`
- propriétés : `Polyvalente, Lancer`

Si tu réutilises les mêmes noms de propriétés, tu retrouveras plus facilement toutes les armes qui partagent un trait.

## Armures

Pour les armures, garde **catégorie** et **CA** bien ordonnés.

Exemples :

- catégorie : `Légère`, `Intermédiaire`, `Lourde`, `Bouclier`
- CA : `14 + Dex max 2`

La description peut contenir notes, prérequis, désavantage ou règles spéciales.

## Outils et équipement

Pour les outils et l'équipement d'aventure, les champs les plus utiles sont **catégorie**, **utilisation** et **description**.

Exemples :

- catégorie : `Outils d'artisan`
- utilisation : `Tests de Dextérité ou d'Intelligence`
- catégorie : `Équipement d'exploration`
- utilisation : `Voyage, donjon, survie`

Préfère des catégories courtes et réutilisables plutôt que de longues phrases.

## Bonnes pratiques

Pour garder le database lisible :

- utilise les mêmes noms pour les catégories similaires
- sépare les listes de valeurs par des virgules lorsqu'elles doivent être lisibles comme groupes
- évite de répéter dans le texte une information qui possède déjà son champ
- garde les descriptions complètes, mais les champs de filtre courts et propres
