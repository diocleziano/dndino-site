# Topbar

![Topbar](../images/en_topbar.png){ .img-hero }


La **topbar** est la zone de raccourcis globale de DnDino. Elle garde à portée de main les outils utilisés le plus souvent pendant la préparation ou la session.

Elle peut afficher seulement les icônes, ou les icônes avec leur nom, selon le réglage choisi dans **Réglages**.

## Comportement Général

Les boutons de gauche sont des raccourcis globaux. Certains ouvrent une section complète, d'autres ouvrent un panneau rapide pour consulter une information sans quitter l'écran courant.

## Accueil

`Accueil` ramène à la page de départ de l'application.

Utilise-le pour revenir à la vue générale ou repartir depuis l'entrée principale.

## Aventures

`Aventures` change de comportement selon le contexte.

Depuis l'**Accueil** ou une section qui n'est pas liée à une aventure précise, il ouvre la liste des aventures.

Depuis un **tableau de bord d'aventure**, les **lieux** ou un **combat** lié à une aventure, il ramène au tableau de bord de cette aventure.

## Personnages

Chaque résultat possède deux boutons ronds à droite : **Visualisation** ouvre la fiche compacte, **Modification** l'éditeur. La ligne seule n'ouvre plus la fiche et aucun réglage global ne choisit entre les deux actions.

## Équipement

`Équip.` ouvre la recherche rapide d'équipement.

Elle couvre :

- armes
- armures
- outils
- équipement d'aventure

Tu peux chercher par nom, catégorie, CA, dégâts, propriétés, utilisation ou description. Les résultats s'ouvrent dans une fenêtre de consultation, tandis que les boutons inférieurs ouvrent les sections complètes.

## Règles

`Règles` ouvre la recherche rapide dans les références de jeu.

Elle couvre :

- dons
- glossaire
- sorts

Tu peux chercher par nom, catégorie, prérequis, type de règle, école ou description. Les sorts s'ouvrent dans une fenêtre dédiée ; les dons et entrées de glossaire peuvent s'ouvrir en consultation ou modification selon les réglages.

## Outils Rapides

`Outils rapides` rassemble les outils utiles immédiatement pendant la préparation ou la session.

Depuis ce panneau, tu peux ouvrir :

- le **lanceur de dés rapide**
- le **générateur de noms**
- les **timers rapides**

### Lanceur de dés

Le lanceur de dés permet de choisir le nombre de dés, le type de dé et le modificateur.

Le dé par défaut se règle dans **Réglages**. Le résultat affiche chaque dé et le total, utile pour les tests rapides et les jets improvisés.

### Générateur de noms

Choisis espèce, genre et **nom complet** ou **prénom seul**. Verrouille prénom ou nom de famille pour ne régénérer que l’autre partie, ou régénère une proposition seule. Copie un résultat ou retrouve-le dans l’historique récent, partagé avec l’accès rapide. Cet historique peut être vidé.

### Timers rapides

Les timers rapides permettent de suivre des échéances de table sans quitter l'écran courant.

Tu peux donner un nom au timer, choisir une durée avec un contrôle de style macOS et lancer jusqu'à quatre timers en parallèle. Chaque timer peut être mis en pause, repris, arrêté ou supprimé.

## Réglages

`Réglages` ouvre les préférences de l'application : langue, thème, topbar, panneaux, combat, Fenêtre Joueurs, base de données, diagnostic et support.

## Session en direct dans la barre inférieure {#live-session-control}

Sur une page d’aventure, ouvre la **Session live** dans la **barre inférieure**, à gauche de Hero. Clique sur **Démarrer** et confirme pour commencer une session de l’aventure actuelle.

Si une session est ouverte, la commande reste accessible en dehors de l’aventure. Tu ne peux pas en lancer une deuxième en parallèle. [Guide de la session en direct](live-session.md#live-session-bottom-bar).

## Fenêtre Joueurs au Centre

Si l'option est active, la topbar affiche aussi les contrôles de la **Fenêtre Joueurs**.

Ils servent à ouvrir ou fermer manuellement la fenêtre destinée aux joueurs, utile pour afficher images, combats ou résumés sur un second écran.

## Quand l'Utiliser

Utilise la topbar pour :

- revenir rapidement des lieux au tableau de bord d'aventure
- chercher une règle sans changer d'écran
- consulter un personnage ou un objet à la volée
- faire un jet rapide, lancer un timer ou générer un nom improvisé
- gérer une session live depuis la section courante

## Remplir la fenêtre principale {#fill-main-window}

Si l’action macOS de double-clic sur la barre de titre est **Remplir**, double-clique dans une zone vide de la barre. La fenêtre principale occupe la zone visible sans passer en plein écran. Un second double-clic rétablit la taille précédente.

<!-- guide-coverage: MOD-023 MOD-024 MOD-025 MOD-034 MOD-038 MOD-039 MOD-044 MOD-045 MOD-048 MOD-054 MOD-067 MOD-069 -->

## Barre inférieure et fenêtres ouvertes

La barre du bas apparaît lorsqu'il existe des fenêtres de travail ou raccourcis de retour ; la Fenêtre Joueurs en est exclue. Titre et icône distinguent **Modification** et **Visualisation** : clique pour rappeler/restaurer la fenêtre, ou sur X pour la fermer. Les fiches/éditeurs de personnages sont indépendants et minimisables ; les états et l'Attaque complète ne le sont pas.

Quitter un combat non terminé le met en pause et conserve un raccourci **tout à gauche**, avec un trait coloré. Clique pour revenir. Sa X masque seulement le raccourci, sans terminer ni supprimer le combat. Il disparaît pendant ce combat, mais les autres fenêtres restent listées.

Les chats reçus de Hero apparaissent même à fenêtre fermée, sans interrompre ton travail ; un point indique les messages non lus. Ouvrir et lire la conversation efface l'indicateur. À droite, la zone Hero conserve les joueurs contactés pendant l'ouverture actuelle de l'app, même déconnectés : état, test, chat, téléchargement de fiche, live et déconnexion. Voir [guide Hero](hero-sync.md).
