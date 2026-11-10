# Topbar

![Topbar](../images/en_topbar.png){ .img-hero }


Die **Topbar** ist DnDinos globale Schnellzugriffsleiste. Sie hält die Werkzeuge bereit, die du beim Vorbereiten oder Leiten am häufigsten brauchst.

Sie kann nur Symbole anzeigen oder Symbole mit Text darunter, je nach Einstellung unter **Einstellungen**.

## Allgemeines Verhalten

Die Schaltflächen links sind globale Abkürzungen. Einige öffnen ganze Bereiche, andere öffnen ein Schnellfenster, damit du etwas nachschlagen kannst, ohne den aktuellen Arbeitskontext zu verlassen.

## Startseite

`Startseite` führt zurück zur Hauptseite der App.

Nutze sie, wenn du zur allgemeinen Übersicht zurückkehren möchtest.

## Abenteuer

`Abenteuer` verhält sich je nach Kontext anders.

Von der **Startseite** oder aus Bereichen ohne konkretes Abenteuer öffnet es die Abenteuerliste.

Innerhalb eines **Abenteuer-Dashboards**, der **Orte** oder eines **Kampfes** dieses Abenteuers führt es zurück zum Dashboard dieses Abenteuers.

## Charaktere

Jeder Treffer hat rechts zwei runde Schaltflächen: **Anzeige** öffnet den kompakten Bogen, **Bearbeiten** den Editor. Die Zeile selbst öffnet keinen Bogen mehr; eine globale Auswahl zwischen den beiden Aktionen entfällt.

## Ausrüstung

`Ausr.` öffnet die schnelle Ausrüstungssuche.

Sie durchsucht:

- Waffen
- Rüstungen
- Werkzeuge
- Abenteuerausrüstung

Du kannst nach Name, Kategorie, RK, Schaden, Eigenschaften, Nutzung oder Beschreibung suchen. Ergebnisse öffnen sich in einem Nachschlagefenster, die unteren Knöpfe öffnen die vollständigen Bereiche.

## Regeln

`Regeln` öffnet die schnelle Regelsuche.

Sie durchsucht:

- Talente
- Glossar
- Zauber

Du kannst nach Name, Kategorie, Voraussetzungen, Regeltyp, Schule oder Beschreibung suchen. Zauber öffnen sich in einem eigenen Fenster; Talente und Glossareinträge je nach Einstellung als Ansicht oder Bearbeitung.

## Schnellwerkzeuge

`Schnellwerkzeuge` bündelt die Werkzeuge, die du beim Vorbereiten oder Leiten sofort brauchst.

Von hier öffnest du:

- den **schnellen Würfelroller**
- den **Namensgenerator**
- **Schnelltimer**

### Würfelroller

Der Würfelroller lässt dich Anzahl der Würfel, Würfeltyp und Modifikator wählen.

Der Standardwürfel wird in **Einstellungen** festgelegt. Das Ergebnis zeigt jeden Wurf und die Summe, passend für schnelle Proben und improvisierte Würfe.

### Namensgenerator

Wähle Volk, Geschlecht und **vollständigen Namen** oder **nur Vornamen**. Sperre Vor- oder Nachnamen, um nur den anderen Teil neu zu erzeugen, oder erneuere einen einzelnen Vorschlag. Kopiere Ergebnisse oder finde sie im gemeinsamen Verlauf von Generator und Schnellzugriff wieder. Der Verlauf lässt sich leeren.

### Schnelltimer

Schnelltimer helfen, Fristen am Spieltisch zu verfolgen, ohne den aktuellen Bildschirm zu verlassen.

Du kannst einen Namen vergeben, die Dauer mit einer macOS-ähnlichen Steuerung festlegen und bis zu vier Timer gleichzeitig laufen lassen. Jeder Timer kann pausiert, fortgesetzt, gestoppt oder entfernt werden.

## Einstellungen

`Einstellungen` öffnet die App-Einstellungen für Sprache, Design, Topbar, Bedienverhalten, Kampf, Spielerfenster, Datenbank, Diagnose und Support.

## Live-Sitzung in der unteren Leiste {#live-session-control}

Öffne auf einer Abenteuerseite **Live-Sitzung** in der **unteren Leiste**, links neben Hero. Klicke auf **Starten** und bestätige, um eine Sitzung für das aktuelle Abenteuer zu beginnen.

Eine offene Sitzung bleibt auch außerhalb des Abenteuers erreichbar. Du kannst nicht gleichzeitig eine zweite starten. [Anleitung zur Live-Sitzung](live-session.md#live-session-bottom-bar).

## Spielerfenster in der Mitte

Wenn aktiviert, zeigt die Mitte der Topbar auch die Steuerung des **Spielerfensters**.

Damit öffnest oder schließt du manuell das Fenster für die Spieler, etwa für Bilder, Kämpfe oder Zusammenfassungen auf einem zweiten Bildschirm.

## Wann Nutzen

Nutze die Topbar, um:

- von Orten schnell zum Abenteuer-Dashboard zurückzukehren
- Regeln nachzuschlagen, ohne den Bildschirm zu wechseln
- Charaktere oder Ausrüstung schnell zu öffnen
- schnell zu würfeln, einen Timer zu starten oder einen Namen zu erzeugen
- eine Live-Sitzung aus dem aktuellen Bereich zu steuern

## Hauptfenster füllen {#fill-main-window}

Ist in macOS **Füllen** als Doppelklickaktion der Titelleiste eingestellt, füllt ein Doppelklick auf eine freie Stelle der Leiste den sichtbaren Bereich, ohne in den Vollbildmodus zu wechseln. Ein weiterer Doppelklick stellt die vorige Größe wieder her.

<!-- guide-coverage: MOD-023 MOD-024 MOD-025 MOD-034 MOD-038 MOD-039 MOD-044 MOD-045 MOD-048 MOD-054 MOD-067 MOD-069 -->

## Untere Leiste und offene Fenster

Die untere Leiste erscheint bei Arbeitsfenstern oder Rückkehrverknüpfungen; das Spielerfenster ist ausgenommen. Name und Symbol unterscheiden **Bearbeitung** und **Anzeige**: Klicken bringt das Fenster nach vorn oder stellt es wieder her, X schließt es. Charakterbögen/-editoren sind unabhängig und minimierbar; Zustände und Vollständiger Angriff nicht.

Beim Verlassen eines laufenden Kampfes pausiert dieser. Eine Rückkehrverknüpfung mit Farbstreifen bleibt **ganz links an erster Stelle**. X blendet nur die Verknüpfung aus, ohne den Kampf zu beenden oder zu löschen. Während dieses Kampfes ist sie verborgen; andere Fenster bleiben aufgelistet.

Hero-Chats erscheinen auch bei geschlossenem Fenster, ohne dich zu unterbrechen; ein Punkt kennzeichnet ungelesene Nachrichten. Öffnen und Lesen entfernt die Markierung. Rechts behält der Hero-Bereich die während dieses App-Starts kontaktierten Spieler auch nach einem Verbindungsabbruch: Status, Verbindungstest, Chat, Bogen-Download, Live-Sync und Trennen. Siehe [Hero-Anleitung](hero-sync.md).
