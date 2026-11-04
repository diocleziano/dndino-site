# Connecter DnDino Hero : guide du MJ

Recevez les fiches des joueurs dans votre aventure et gérez les valeurs de jeu depuis le Mac. La connexion est locale, sans serveur externe. Consultez aussi le [guide pour les joueurs Hero](../companion/dndino-sync.md).

!!! info "Disponibilité"
    Cette page décrit notamment le nouveau rapprochement des données, préparé pour la prochaine mise à jour. Il nécessite des versions de **DnDino et DnDino Hero qui le prennent toutes deux en charge**. Les versions précédentes peuvent fonctionner différemment au démarrage.

## Préparer la connexion

Ouvrez la bonne aventure. Utilisez le même réseau local, autorisez l'accès au réseau local et laissez Wi-Fi et Bluetooth activés, appareils à proximité. Chaque joueur doit sélectionner le bon personnage dans Hero.

Le direct exige **iOS/iPadOS 26 ou ultérieur** sur Hero. Sur les systèmes antérieurs, seul **l'envoi manuel de la fiche** est disponible, même hors combat. **Connecté ne signifie pas synchronisé.**

## Première connexion

1. Dans le panneau **Session en direct** du tableau de bord de l'aventure, démarrez la connexion dans la zone **DnDino Hero**. Il n'est pas nécessaire de démarrer une session de jeu.
2. Le joueur ouvre **Réglages → Connexion DnDino**, recherche DnDino et choisit votre aventure.
3. Autorisez son appareil après avoir vérifié le nom et le personnage.
4. Choisissez d'importer une nouvelle fiche ou d'associer une fiche existante. Vérifiez la confirmation de remplacement : elle peut écraser la fiche sélectionnée.
5. Activez **Synchronisation automatique** pour cet appareil si vous souhaitez le direct. **Seul le MJ contrôle cette activation** ; Hero affiche l'état, sans second interrupteur à activer.

L'association utilise des identifiants, pas uniquement le nom : renommer le personnage ne nécessite pas une nouvelle copie.

## Choisir les données à conserver

**La structure de la fiche vient de Hero** : niveaux, caractéristiques, descriptions, sorts et configuration des progressions relèvent du joueur.

Avec les nouvelles versions, Hero envoie la fiche complète à chaque connexion ou reconnexion, avant les échanges en direct. Réactiver le direct demande aussi un alignement. Si les valeurs correspondent, aucune comparaison n'apparaît.

Sinon, la fenêtre d'alignement compare **PV actuels, maximaux et temporaires, CA, inspiration héroïque, conditions, ressources restantes et emplacements utilisés**. Pour chaque différence, conservez la valeur DnDino ou Hero. **Hero est présélectionné** ; les commandes globales permettent de tout prendre de l'une des deux applications. Confirmez puis attendez le résultat.

Exemple : conservez les 18 PV de DnDino plutôt que les 24 de Hero, mais choisissez les conditions de Hero. Les conditions sont choisies **comme un ensemble complet**, jamais fusionnées automatiquement.

Les maxima et la configuration des ressources restent ceux de Hero. Une combinaison incompatible est signalée. Seul cet appareil attend ; les autres joueurs continuent. Si les données changent, revérifiez la comparaison actualisée. Réessayez pour demander des données fraîches. Fermer la fenêtre ou interrompre la connexion déconnecte l'appareil. **Confirmer n'active pas le direct à lui seul.**

## Pendant la partie

Le direct échange les valeurs prises en charge : PV actuels/maximaux/temporaires, CA, inspiration et conditions. En combat, le participant associé est pris en compte.

| Donnée | Présentation |
| --- | --- |
| Progressions consommables | Restant/Total ; moins pour dépenser, plus pour restaurer |
| Progressions fixes du niveau actuel | Fiches consultables, sans boutons de consommation |
| Emplacements de sorts | Total et utilisés, séparés par origine si nécessaire |

Les compteurs sont aussi enregistrés dans DnDino. Les commandes prises en charge du MJ sont confirmées par Hero ; en cas de modification simultanée, vérifiez le résultat avant de réessayer. Les nouveaux niveaux et changements de configuration demandent une **fiche complète**, pas seulement les compteurs.

## Télécharger, discuter et retrouver un appareil

À droite du chat, le bouton de téléchargement demande la fiche déjà associée, sans nouvel envoi manuel du joueur. Il nécessite un Hero compatible, connecté et autorisé ; il est indisponible pendant l'alignement et n'active pas le direct.

La zone Hero de la barre inférieure conserve les appareils connectés pendant l'ouverture actuelle de DnDino, même après une déconnexion. Elle permet de vérifier l'identité et l'état, tester la connexion, ouvrir le chat, gérer le direct et déconnecter. Le test n'importe rien. Le **chat privé exige le direct actif** ; les messages non lus sont signalés dans la barre.

## Reconnexion et dépannage

Par défaut, le MJ réactive le direct à chaque nouvelle connexion. Le démarrage automatique facultatif pour appareils déjà autorisés se règle dans les paramètres ; il ne supprime pas le nouvel alignement.

- **Mac introuvable** : vérifiez l'aventure en écoute, le réseau, les autorisations Réseau local et les applications ouvertes.
- **Connecté sans mises à jour** : vérifiez autorisation, association, iOS/iPadOS 26+, alignement terminé et activation par le MJ.
- **Connexion perdue** : gardez Hero au premier plan ; le retour dans l'application peut déclencher une reconnexion. Le bouton de reconnexion permet aussi de réessayer.
- Déconnecter termine la connexion actuelle sans supprimer la fiche importée.
- Retirer l'association révoque autorisation et associations dans cette aventure ; oublier l'appareil concerne toutes les aventures. Les fiches importées restent disponibles.

Avant la partie, testez une petite variation de PV et vérifiez le résultat sur les deux appareils.
