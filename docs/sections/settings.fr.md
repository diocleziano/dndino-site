# Réglages

La section **Réglages** regroupe les préférences globales de DnDino. Ici, on ne travaille pas sur une aventure ou un personnage précis, mais on définit **comment l’application doit se comporter dans son ensemble**.

Les réglages influencent surtout :

- l’aspect général de l’interface
- le comportement de la topbar
- le flux de `Lieux`
- le comportement du `Combat`
- la gestion des images, des sauvegardes et des snapshots
- le support et la partie diagnostique de la base de données

## Comment l’écran est organisé

La page est divisée en deux zones :

- une **barre latérale gauche** avec les catégories
- un **panneau principal** à droite avec les options de la section sélectionnée

Les catégories disponibles sont :

- `Général`
- `Topbar`
- `Lieux`
- `Combat`
- `Médias`
- `Thème`
- `Base de données`
- `Diagnostic`
- `Support`
- `Licences`

Cette structure sépare bien les préférences d’usage quotidien des réglages plus techniques, comme les sauvegardes et le diagnostic.

## Général

La section `Général` regroupe les préférences de base de l’application.

### Profil MJ

Tu peux personnaliser ton profil avec :

- `Nom d’utilisateur`
- `Genre`

Le nom est réutilisé dans d’autres parties de l’application, par exemple dans le message de bienvenue de la `Home`.

### Langue de l’interface

Tu peux choisir de :

- suivre la langue du système
- forcer une langue spécifique dans l’application

### Confirmations globales

L’option `Demander confirmation avant les suppressions` ajoute une confirmation avant les actions destructives, comme les retraits et suppressions.

### Métadonnées

Dans `Général`, tu trouves aussi :

- `Afficher les métadonnées dans l’application`

Cette option décide si les panneaux de métadonnées doivent être visibles dans les écrans qui les prennent en charge.

### Disposition des panneaux de la dashboard aventure

Cette partie est importante si tu utilises souvent la `Dashboard Aventure`.

Tu peux :

- glisser les panneaux
- les réorganiser dans la colonne de gauche ou de droite
- les déplacer d’une colonne à l’autre

### Thème actif

Dans `Général`, le **thème actuellement sélectionné** est également affiché comme résumé rapide. Le vrai changement de thème se fait dans la section `Thème`.

### Guides d’introduction

Depuis ici, tu peux rétablir le comportement de premier lancement de l’application.

Le bouton `Réinitialiser le premier lancement` indique à DnDino de considérer à nouveau comme non vus les guides contextuels et les parcours d’onboarding.

## Topbar

La section `Topbar` définit le comportement des outils rapides présents dans la barre supérieure de l’application. Pour la description complète de chaque bouton, consulte la page `Topbar`.

### Apparence de la topbar

Tu peux choisir d’afficher la topbar :

- avec les icônes seules
- ou avec icônes et nom en dessous

### Dé par défaut

Ici, tu peux choisir le **type de dé par défaut** proposé par le lanceur de dés rapide.

### Ouverture rapide des personnages

Ce réglage contrôle le comportement de l’ouverture rapide des personnages.

Tu peux décider si le raccourci doit mener :

- vers une vue davantage orientée lecture
- ou vers un mode plus proche de l’édition

### Ouverture rapide des règles

Ce réglage contrôle l’ouverture rapide des `Règles`.

Depuis ici, tu peux décider si ce raccourci doit ouvrir :

- l’éditeur complet
- ou une fenêtre plus compacte et orientée consultation

### Contrôles de la fenêtre joueurs dans la topbar

L’option `Afficher les contrôles de la fenêtre joueurs dans la topbar` affiche les contrôles rapides pour ouvrir ou fermer manuellement la `Fenêtre Joueurs`.

## Lieux

La section `Lieux` contient les préférences globales utilisées comme comportement par défaut dans la dashboard des lieux.

### Rôle de présence par défaut

Quand tu ajoutes une présence à un lieu, DnDino peut proposer un rôle initial par défaut.

### Afficher par défaut les cartes des lieux parents

Si cette option est activée, dans l’écran `Lieux`, les cartes héritées des lieux parents démarrent déjà visibles.

### Mémoriser le dernier lieu visité

Si actif, lorsque tu reviens dans l’écran `Lieux`, l’application tente de restaurer le dernier lieu sélectionné pour cette aventure.

### Fermer automatiquement le lieu précédent

Ce réglage s’applique pendant une **session live active**.

Quand un lieu est marqué `En visite`, le lieu qui était auparavant `En visite` est automatiquement marqué comme `Visité`.

## Combat

La section `Combat` regroupe les préférences globales du système de combat.

Tu y trouves les options de présentation et les préférences qui influencent la `Fenêtre Joueurs`.

### Activer l’écran de combat pour les joueurs

C’est l’interrupteur principal. S’il est désactivé, DnDino n’utilise pas la fenêtre joueurs pour afficher l’intro, le tour courant, le round ou le résumé final du combat, et les options liées sont masquées.

### Ouvrir la fenêtre joueurs si elle est fermée

Si cette option est active, DnDino ouvre automatiquement la `Fenêtre Joueurs` quand le combat commence. Sinon, la présentation est mise à jour seulement si la fenêtre est déjà ouverte.

### Ouvrir la fenêtre joueurs même avec un seul moniteur

Cette option apparaît seulement si l’ouverture automatique est active. Elle sert à utiliser la `Fenêtre Joueurs` même sans second écran.

## Présentation du combat

Cette sous-section contrôle les informations générales affichées aux joueurs pendant l’affrontement :

- `Afficher l’intro du combat aux joueurs`
- `Afficher le résumé final aux joueurs`
- `Afficher le round sur l’écran joueurs`
- `Afficher la durée de l’affrontement sur l’écran joueurs`
- `Afficher le prochain tour sur l’écran joueurs`

La durée de l'affrontement est affichée comme un minuteur lisible ; si le combat est en pause, le compteur s'arrête.

## Informations des héros

Ces options s’appliquent lorsque le participant actif est un héros ou un allié. Un PNJ ou un monstre marqué comme `Allié` utilise donc aussi ces réglages. Tu peux choisir d’afficher :

- les PV actuels, maximums et temporaires
- les états actifs

## Informations des PNJ

Ces options s’appliquent uniquement lorsque le participant actif est un PNJ non allié. Les PNJ marqués comme `Allié` utilisent les réglages héros/alliés. Tu peux choisir séparément d’afficher :

- les PV actuels, maximums et temporaires
- les états actifs
- le vrai nom du PNJ

Si les noms des PNJ sont masqués, la `Fenêtre Joueurs` utilise le nom générique `PNJ`.

## Informations des monstres

Ces options s’appliquent uniquement lorsque le participant actif est un monstre non allié. Les monstres marqués comme `Allié` utilisent les réglages héros/alliés. Tu peux choisir séparément d’afficher :

- les PV actuels, maximums et temporaires
- les états actifs
- le vrai nom des ennemis

Si les noms des monstres/ennemis sont masqués, la `Fenêtre Joueurs` utilise le nom générique `Ennemi`.

## Médias

La section `Médias` regroupe les préférences liées à la gestion des images et à la fenêtre de présentation.

### Images joueurs en plein écran

Si cette option est activée, les images montrées aux joueurs s’ouvrent en mode plein écran.

### Images MJ sur le moniteur principal

Cette option fait en sorte que la fenêtre du MJ s’ouvre par défaut sur le premier écran disponible.

### Mémoriser la taille de la fenêtre MJ

Si actif, quand tu rouvres une nouvelle image pour le MJ, la fenêtre conserve :

- la dernière taille
- la dernière position

## Maintenance des médias

La section `Maintenance des médias` couvre le côté plus technique de la gestion des images.

Depuis ici, tu peux lancer `Nettoyer les médias inutilisés`, qui vérifie les fichiers images enregistrés par l’application et supprime ceux qui ne sont plus liés à aucune entité.

## Thème

La section `Thème` permet de choisir la **palette globale** de l’application.

Chaque thème affiche un petit aperçu visuel avec ses couleurs principales, pour que tu comprennes tout de suite comment l’interface va changer.

## Base de données

La section `Base de données` est l’une des plus importantes pour la sécurité des données.

Tu y trouves :

- le chemin du dossier de données
- le chemin de la base SQLite
- le chemin du dossier de sauvegarde
- des informations sur les derniers snapshots

### Sauvegarde automatique

Tu peux choisir :

- la fréquence de la sauvegarde automatique
- le nombre maximal de snapshots automatiques à conserver

### Snapshots cloud

DnDino gère aussi le comportement des snapshots cloud.

Depuis ici, tu peux choisir le comportement relatif aux sauvegardes cloud et consulter l’état actuel à travers le texte récapitulatif affiché à l’écran.

### Actions principales

Dans le panneau `Base de données`, tu trouves les principaux boutons de maintenance :

- `Ouvrir le dossier de données`
- `Ouvrir le dossier de sauvegarde`
- `Créer un snapshot...`
- `Restaurer un snapshot...`
- `Restaurer depuis iCloud`

### Réinitialisation de l’application

La fonction `Réinitialiser les données de l’application` supprime :

- la base de données de l’application
- les médias de l’application

mais conserve les sauvegardes déjà créées.

### Derniers snapshots

Dans la partie basse de la section `Base de données`, DnDino affiche aussi la liste des derniers snapshots trouvés.

Pour chacun, on voit :

- nom du fichier
- date
- taille

## Diagnostic

La section `Diagnostic` sert à contrôler l’état technique de la base SQLite utilisée par l’application.

Ici, tu peux :

- actualiser les données de diagnostic
- voir le chemin de la base
- vérifier si le fichier existe
- vérifier sa taille et sa date de modification
- voir la version de SQLite

### Tables

Le diagnostic affiche aussi la liste des tables trouvées dans la base, avec le nombre d’enregistrements présents dans chacune.

## Support

La section `Support` regroupe les canaux rapides pour contacter la personne qui développe l’application.

Tu y trouves :

- l’e-mail de support
- le bouton `Demander de l’aide`
- le bouton `Envoyer une suggestion`
- le bouton `Copier l’e-mail`

## Licences

La section `Licences` regroupe les références légales et d’attribution utilisées par l’application.

Elle inclut actuellement en particulier la partie liée au **System Reference Document 5.2** de Dungeons & Dragons, avec des références :

- au document SRD
- à la licence `CC-BY-4.0`

!!! tip
    Si tu configures DnDino pour la première fois, les sections les plus utiles à vérifier tout de suite sont `Général`, `Topbar`, `Combat` et `Base de données`. Ce sont généralement celles qui influencent le plus l’usage quotidien et la sécurité des données.
