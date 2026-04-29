# Combat

La section **Combat** est le suivi opérationnel des affrontements dans DnDino. Elle est conçue pour rester rapide, compacte et lisible quand la scène devient la plus intense autour de la table.

Un combat naît toujours depuis un **lieu** et peut inclure les héros de l'aventure, les présences locales, les PNJ et les monstres liés à la scène.

Cette page explique :

- la préparation du pré-combat
- la saisie et le tri de l'initiative
- l'écran principal de combat
- les contrôles de tour
- attaques, dégâts, soins, états et jets de sauvegarde
- les liens internes dans les attaques et capacités
- le récapitulatif latéral, les derniers événements et l'annulation
- la Fenêtre Joueurs
- le résumé final et les statistiques

## Un ou Deux Écrans

Le combat fonctionne très bien sur **un seul écran** : tout le travail du MJ reste dans la fenêtre principale, avec le suivi d'initiative, les fiches compactes et le récapitulatif.

Avec un second écran, tu peux aussi utiliser la **Fenêtre Joueurs** :

- l'écran du MJ garde les contrôles, fiches, cibles, états et statistiques
- l'écran des joueurs affiche une présentation plus propre, avec images et informations visibles

!!! tip
    Le second écran est optionnel. Il sert surtout à séparer la vue technique du MJ de la présentation destinée aux joueurs.

## Fenêtre Joueurs Pendant le Combat

Quand l'affrontement commence, DnDino peut ouvrir ou mettre à jour la **Fenêtre Joueurs**.

Si la présentation est active, elle peut montrer :

- l'introduction du combat avec les participants
- le participant dont c'est le tour
- les animations d'attaque
- le résumé final

![Écran joueurs pendant le pré-combat](../images/en_combat_schermogiocatori_precombat.png){ .img-shot }

L'affichage peut inclure :

- round
- PV actuels, maximums et temporaires
- états
- prochain tour

![Écran joueurs pendant le tour d'un héros](../images/en_combat_schermogiocatori_turnoeroi.png){ .img-shot }
![Écran joueurs pendant le tour d'un monstre](../images/en_combat_schermogiocatori_turnomostri.png){ .img-shot }

Pour les héros/alliés, PNJ et monstres, les réglages permettent de choisir séparément quelles informations sont visibles par les joueurs. Si un PNJ ou un monstre est marqué comme `Allié`, il est aussi traité comme un héros/allié sur l’écran joueurs.

## Réglages Utiles

Les options principales se trouvent dans **Réglages**, dans les sections Combat et Fenêtre Joueurs.

Les plus importantes sont :

- `Ouvrir la Fenêtre Joueurs même avec un seul écran`
- `Afficher les contrôles de la Fenêtre Joueurs dans la barre supérieure`
- `Afficher l'intro du combat aux joueurs`
- `Afficher le résumé final aux joueurs`
- `Afficher le round sur l'écran joueurs`
- `Afficher le prochain tour sur l'écran joueurs`
- `Afficher les PV des héros sur l'écran joueurs`
- `Afficher les états des héros sur l'écran joueurs`
- `Afficher les PV des PNJ aux joueurs`
- `Afficher les états des PNJ aux joueurs`
- `Afficher les noms des PNJ aux joueurs`
- `Afficher les PV des monstres aux joueurs`
- `Afficher les états des monstres aux joueurs`
- `Afficher les noms des ennemis aux joueurs`

La fin du combat demande toujours confirmation, car fermer un affrontement synchronise l'état et les statistiques.

## Où S'ouvre le Combat

Le combat est créé depuis un **lieu**. Une fois ouvert, l'écran change selon l'état de l'affrontement :

- **Pré-combat** : préparer participants, noms et initiatives.
- **Combat actif** : gérer tours, fiches, cibles et récapitulatif.
- **Combat terminé** : consulter le résumé final du MJ.

## Pré-Combat

![Écran de pré-combat](../images/en_combat_precombat.png){ .img-hero }


Le pré-combat sert à préparer l'affrontement avant le premier tour.

L'écran comporte trois zones principales :

- **Héros**
- **Monstres et PNJ**
- **Ordre final**

En haut, tu vois aussi le nom de l'affrontement, le nombre de participants et les actions principales.

## Actions du Pré-Combat

Les actions principales sont :

- `Ajouter`
- `Démarrer l'affrontement`
- `Init PNJ/Monstres`, dans la colonne monstres et PNJ

`Ajouter` ouvre le sélecteur de participants.

`Démarrer l'affrontement` lance le combat. Si au moins un participant a une initiative à `0`, DnDino demande confirmation.

`Init PNJ/Monstres` lance automatiquement l'initiative uniquement pour les monstres et PNJ. Les héros restent prévus pour une saisie manuelle, car leur initiative vient généralement de la table.

## Modifier Noms et Initiative

Dans le pré-combat, tu peux corriger :

- le nom affiché du participant
- l'initiative

C'est surtout utile pour les monstres, par exemple :

- Gobelin 1
- Gobelin 2
- Capitaine gobelin

L'initiative est prise en compte pendant la saisie, sans attendre de quitter le champ. Les colonnes de travail ne se réordonnent pas sans cesse pendant que tu écris : le tri définitif est appliqué au lancement du combat.

## Ordre Final

![Ordre d’initiative préparé](../images/en_combat_precombat_valorizzato.png){ .img-hero }


Le panneau **Ordre final** montre l'aperçu toujours à jour de l'ordre qui sera utilisé au lancement.

L'ordre est calculé ainsi :

1. initiative la plus haute
2. en cas d'égalité, modificateur de Dextérité le plus haut
3. si l'égalité persiste, départage aléatoire

Ce panneau permet de vérifier le résultat sans gêner la saisie.

## Origine des Participants

Le panneau d'ajout peut proposer :

- `Héros`
- `Présences du lieu`
- `Globaux`

Les héros déjà liés à l'aventure ne peuvent entrer qu'une seule fois dans le même combat.

Les présences du lieu réutilisent leur état local si disponible.

Les monstres globaux peuvent être ajoutés plusieurs fois, car ils représentent souvent plusieurs exemplaires d'une même créature.

## Combat Actif

![Combat actif](../images/en_combat_main.png){ .img-hero }


Quand l'affrontement démarre, l'écran passe à la gestion opérationnelle.

Il est divisé en trois zones :

- à gauche, le **suivi d'initiative**
- au centre, les fiches compactes du **tour courant** et du **participant sélectionné**
- à droite, le **récapitulatif** de santé, dégâts et événements

L'objectif est de garder un maximum d'informations utiles visibles sans ouvrir de grands panneaux.

## Contrôles du Tour

Les contrôles principaux sont en haut.

À gauche :

- `Précédent`
- `Pause` / `Reprendre`
- `Suivant`
- `Annuler événement`

À droite :

- `Ajouter`
- `Trier`
- `Fin du combat`

`Précédent` et `Suivant` changent le tour.

`Pause` arrête le chronomètre du combat. En pause, le bouton devient `Reprendre`.

`Annuler événement` restaure l'un des derniers événements annulables.

`Ajouter` insère d'autres participants pendant le combat.

`Trier` reconstruit l'ordre d'initiative.

`Fin du combat` clôt l'affrontement après confirmation.

## Suivi d'Initiative

La colonne de gauche montre tous les participants sous forme compacte.

Chaque ligne affiche :

- initiative
- nom
- CA
- PV
- PV temporaires
- indicateur d'état, si présent
- couleur de rôle

La couleur latérale aide à distinguer :

- héros
- alliés
- neutres
- ennemis

Cliquer sur une ligne :

- ouvre ce participant comme **sélectionné**
- referme la colonne sélectionnée si ce participant était déjà sélectionné

Le bouton corbeille de la ligne retire le participant du combat.

## Fiches du Tour et du Sélectionné

Au centre, tu peux voir jusqu'à deux fiches :

- le participant dont c'est le tour
- le participant sélectionné dans la liste

Les fiches ont une largeur fixe et leur propre défilement vertical, pour garder la page stable même avec de longs textes.

La partie supérieure montre :

- nom
- type, ascendance ou sous-type
- langues, si présentes
- facteur de puissance et PX, si présents
- aperçu d'image
- boutons d'action

## Champs Rapides

Depuis la fiche, tu peux modifier :

- PV actuels
- PV temporaires
- initiative

La CA est affichée de façon compacte avec une icône de bouclier.

Les héros de l'aventure peuvent aussi afficher le bouton d'**Inspiration héroïque**.

Les changements de PV restent synchronisés avec la liste de gauche et le récapitulatif de droite.

## Actions du Participant

Chaque fiche peut afficher :

- `Attaquer`
- `Dégâts`
- `Soins`
- `JS`
- `États`
- `Notes MJ`
- `Modifier`

`Attaquer` ouvre une fenêtre avec l'attaquant et la liste des cibles.

![Fenêtre Attaquer](../images/en_combat_attaccosemplice.png){ .img-shot }

`Dégâts` applique des dégâts directs au participant.

![Fenêtre Dégâts](../images/en_combat_danni.png){ .img-detail }

`Soins` applique une guérison directe.

![Fenêtre Soins](../images/en_combat_cura.png){ .img-detail }

`JS` ouvre les jets de sauvegarde disponibles.

![Fenêtre jet de sauvegarde](../images/en_combat_tirosalvezza.png){ .img-detail }

`États` ouvre une fenêtre dédiée à la gestion des états.

`Notes MJ` enregistre des notes sur le participant. Les notes ne font pas partie de l'annulation.

`Modifier` ouvre l'éditeur complet du participant.

## Listes de Cibles

Les listes de cibles sont ordonnées selon l'attaquant.

Si l'attaquant est un ennemi :

- héros et alliés d'abord
- puis neutres
- puis ennemis

Si l'attaquant est un héros, un allié ou un neutre :

- ennemis d'abord
- puis neutres
- puis héros et alliés

Dans chaque groupe, les noms sont triés alphabétiquement.

La ligne colorée latérale aide à reconnaître le rôle de la cible.

## Attaques, Capacités et Liens Internes

Les sections principales sont :

- `États`
- `Attaques`
- `Capacités spéciales`
- `Capacités`
- `Sorts`
- `Description`

Les sections sont repliables et utilisent un léger dégradé lié à la couleur du titre.

Les textes d'attaques, capacités spéciales et capacités peuvent contenir des liens internes créés pendant la création ou la modification du personnage.

Pendant le combat, ces liens ouvrent des fenêtres dédiées pour résoudre l'action avec plus d'espace.

Les liens les plus utiles sont :

- `Attaque complète`
- `1d20 + MOD`
- jet libre
- jet de dégâts
- liens vers des entités internes

## Attaque Complète

![Fenêtre Attaque complète](../images/en_combat_attaccocompleto.png){ .img-shot }
![Création du lien Attaque complète](../images/en_combat_attaccocompleto_link.png){ .img-shot }


`Attaque complète` est pensée pour les textes d'attaque des monstres, PNJ ou héros.

Tu la prépares dans l'écran de création ou de modification du personnage : sélectionne le texte de l'attaque et crée un lien de type `Attaque complète`. Pendant le combat, ce texte devient une action prête à ouvrir et résoudre.

Quand tu l'utilises en combat :

- la fenêtre montre le nom de l'attaque
- l'attaquant est indiqué clairement
- tu peux choisir une ou plusieurs cibles
- tu peux gérer plusieurs lignes de dégâts
- tu appliques les dégâts sélectionnés aux cibles choisies

Lors de la création du lien, les dégâts sont modulaires : le bouton `+` ajoute des lignes et seules les lignes renseignées sont affichées.

## Sorts

Si le participant possède des sorts, la fiche affiche la section `Sorts`.

Les sorts sont regroupés par niveau.

Pour les monstres et PNJ, la ligne de niveau peut aussi montrer le compteur d'emplacements utilisés, par exemple :

- `0/3`
- `2/3`
- `3/3`

Le bouton `Utiliser` sur un sort augmente le compteur du niveau correspondant.

Le compteur ne bloque pas l'utilisation quand il atteint le maximum : il sert seulement de pense-bête pour le MJ.

Les tours de magie n'utilisent pas d'emplacements.

## États

![Fenêtre États](../images/en_combat_condizioni.png){ .img-shot }


La fenêtre `États` permet de :

- ajouter des états
- retirer des états
- choisir une durée
- lier l'expiration au tour d'un participant
- gérer des notes associées

Quand un état est appliqué, DnDino affiche un retour visuel sur l'écran et sur la ligne concernée.

## Héros à 0 PV ou Moins

Les héros suivent une règle différente des monstres et PNJ.

Un héros peut descendre sous `0` PV.

La règle est :

- de `0` à `-(PV maximums - 1)`, le héros est **Inconscient**
- à `-PV maximums` ou moins, le héros meurt
- il meurt aussi après 3 échecs aux jets de sauvegarde contre la mort

Quand un héros est à `0` PV ou moins sans être mort, la fiche affiche les **jets de sauvegarde contre la mort**.

Après 3 réussites, le héros revient à `1` PV.

## PNJ et Monstres à 0 PV

Pour les PNJ et les monstres, la règle est plus simple :

- à `0` PV ou moins, ils sont considérés morts
- ils sont exclus du cycle des tours
- le récapitulatif peut les afficher comme morts

## Récapitulatif Latéral

La colonne de droite affiche le **Récapitulatif**.

Tu y trouves :

- round
- durée
- tour courant
- santé des héros et alliés
- santé des PNJ et monstres
- dégâts infligés
- dégâts subis
- 5 derniers événements

C'est une vue de contrôle : elle sert à lire la situation d'un coup d'oeil.

Les PV changent de couleur :

- normal si le participant est en bonne condition
- jaune sous 50 %
- orange sous 10 %
- rouge à 0 ou moins

Pour les héros, les PV ne sont barrés que lorsque le personnage est vraiment mort, pas simplement sous 0 PV.

## 5 Derniers Événements et Annulation

Le combat conserve les derniers événements annulables.

L'annulation peut inclure :

- attaques
- dégâts appliqués par des attaques
- soins, s'ils sont gérés comme événement annulable
- états appliqués ou modifiés

Les `Notes MJ` ne sont pas annulées.

L'annulation restaure aussi les statistiques liées, afin que dégâts infligés et subis restent cohérents.

## Retour Visuel

Quand quelque chose arrive en combat, DnDino donne un retour immédiat :

- bannière en haut
- animation sur la ligne du participant concerné
- effet sur le bouton `Appliquer`, si présent
- mise à jour du récapitulatif

Cela permet de comprendre tout de suite que la commande a été prise en compte.

## Résumé Final

![Résumé final du combat](../images/en_combat_postcombat.png){ .img-hero }

![Résumé final sur l'écran joueurs](../images/en_combat_schermogiocatori_postcombat.png){ .img-shot }

Quand tu confirmes la fin du combat, l'affrontement n'est plus modifiable.

L'écran final montre :

- rounds totaux
- durée
- ennemis tués
- dégâts infligés
- dégâts subis
- état final des participants

Les PV finaux et les états sont synchronisés avec les fiches liées.

## Synchronisation Finale

À la fermeture du combat, DnDino synchronise les données nécessaires.

Pour les héros de l'aventure :

- PV actuels
- PV temporaires
- états
- état final

Pour les présences du lieu avec état local :

- PV actuels
- PV temporaires
- états
- état final

Le combat peut aussi alimenter les données de **session live** et les statistiques.

## Statistiques

DnDino utilise les combats terminés pour alimenter statistiques et graphiques.

Les statistiques peuvent inclure :

- dégâts infligés
- dégâts subis
- durée des affrontements
- nombre de combats
- ennemis tués
- évolution des dégâts par jour
- durée moyenne des sessions

Dans le tableau de bord de l'aventure, la vue **Statistiques d'aventure** rassemble les combats terminés, même hors d'une session live unique, et les regroupe de façon lisible.

Le résumé de session live peut afficher les graphiques des combats terminés pendant cette session.

## Bon Usage

Le combat de DnDino fonctionne au mieux quand tu :

1. prépares soigneusement le pré-combat
2. attribues initiatives et noms avant de commencer
3. utilises le suivi de gauche pour garder toute la scène sous les yeux
4. gardes ouverte la fiche du tour et, si utile, celle de la cible sélectionnée
5. utilises les liens dans les attaques et capacités
6. consultes le récapitulatif pour santé, dégâts et événements récents
7. termines le combat seulement quand tu es sûr, pour garder statistiques et synchronisations propres

!!! tip
    Même si DnDino automatise de nombreuses opérations, tu peux continuer à lancer de vrais dés. Dans ce cas, utilise surtout le combat pour appliquer rapidement dégâts, soins et états, sans refaire les calculs de PV et de statistiques à la main.
