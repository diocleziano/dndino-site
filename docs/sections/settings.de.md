# Einstellungen

Der Bereich **Einstellungen** sammelt die globalen Voreinstellungen von DnDino. Hier arbeitest du nicht an einem einzelnen Abenteuer oder Charakter, sondern legst fest, **wie sich die App insgesamt verhalten soll**.

Die Einstellungen beeinflussen vor allem:

- das allgemeine Erscheinungsbild der Oberfläche
- das Verhalten der Topbar
- den Ablauf in `Orte`
- das Verhalten des `Kampfs`
- die Verwaltung von Bildern, Backups und Snapshots
- Support und Diagnose der Datenbank

## Aufbau des Bildschirms

Die Seite ist in zwei Bereiche aufgeteilt:

- eine **linke Seitenleiste** mit Kategorien
- ein **Hauptpanel** rechts mit den Optionen des ausgewählten Bereichs

Verfügbare Kategorien sind:

- `Allgemein`
- `Topbar`
- `Orte`
- `Kampf`
- `Medien`
- `Thema`
- `Datenbank`
- `Diagnose`
- `Support`
- `Lizenzen`

Diese Struktur trennt alltagsnahe Einstellungen sauber von technischeren Bereichen wie Backups und Diagnose.

## Allgemein

Der Bereich `Allgemein` enthält die grundlegenden Einstellungen der App.

### SL-Profil

Hier kannst du dein Profil anpassen mit:

- `Benutzername`
- `Geschlecht`

Der Name wird auch an anderen Stellen in der App verwendet, zum Beispiel in der Begrüßung der `Home`.

### Oberflächensprache

Du kannst entscheiden, ob DnDino:

- der Systemsprache folgen soll
- oder eine bestimmte App-Sprache erzwingen soll

### Globale Bestätigungen

Die Option `Bestätigung für Löschvorgänge anfordern` fügt vor destruktiven Aktionen wie Entfernen und Löschen eine Bestätigung ein.

### Metadaten

Unter `Allgemein` findest du außerdem:

- `Metadaten in der App anzeigen`

Diese Option legt fest, ob Metadaten-Panels in den Bildschirmen angezeigt werden sollen, die sie unterstützen.

### Layout der Panels im Abenteuer-Dashboard

Dieser Teil ist wichtig, wenn du das `Abenteuer-Dashboard` häufig verwendest.

Du kannst:

- Panels ziehen
- sie innerhalb der linken oder rechten Spalte neu anordnen
- sie zwischen den Spalten verschieben

### Aktives Thema

Unter `Allgemein` wird außerdem das **aktuell ausgewählte Thema** als schnelle Übersicht angezeigt. Das eigentliche Umschalten erfolgt im Bereich `Thema`.

### Einführungshinweise

Von hier aus kannst du das Erstverhalten der App zurücksetzen.

Die Schaltfläche `Erstnutzung zurücksetzen` weist DnDino an, kontextbezogene Hilfen und Onboarding-Abläufe erneut als ungesehen zu behandeln.

## Topbar

Der Bereich `Topbar` definiert das Verhalten der Schnellwerkzeuge in der oberen Leiste der App. Die vollständige Beschreibung aller Schaltflächen findest du auf der Seite `Topbar`.

### Darstellung der Topbar

Du kannst wählen, ob die Topbar angezeigt wird:

- nur mit Symbolen
- oder mit Symbolen und Namen darunter

### Standardwürfel

Hier kannst du den **Standardwürfeltyp** des schnellen Würfelrollers festlegen.

### Schnelles Öffnen von Charakteren

Diese Einstellung steuert das Verhalten des schnellen Öffnens von Charakteren.

Du kannst entscheiden, ob die Abkürzung zu:

- einer stärker lesefokussierten Ansicht
- oder zu einem eher bearbeitungsnahen Modus

führen soll.

### Schnelles Öffnen von Regeln

Diese Einstellung steuert das schnelle Öffnen der `Regeln`.

Hier kannst du festlegen, ob diese Abkürzung:

- den vollständigen Editor
- oder ein kompakteres, stärker auf Nachschlagen ausgerichtetes Fenster

öffnen soll.

### Steuerung des Spielerfensters in der Topbar

Die Option `Steuerung des Spielerfensters in der Topbar anzeigen` zeigt Schnellsteuerungen, um das `Spielerfenster` manuell zu öffnen oder zu schließen.

## Orte

Der Bereich `Orte` enthält globale Einstellungen, die als Standardverhalten im Orte-Dashboard verwendet werden.

### Standardrolle für Anwesende

Wenn du einem Ort einen Anwesenden hinzufügst, kann DnDino eine Standardrolle vorschlagen.

### Karten übergeordneter Orte standardmäßig anzeigen

Wenn diese Option aktiv ist, werden im Bildschirm `Orte` geerbte Karten übergeordneter Orte direkt sichtbar angezeigt.

### Zuletzt besuchten Ort merken

Wenn aktiv, versucht die App beim Zurückkehren in den Bildschirm `Orte`, den zuletzt ausgewählten Ort für dieses Abenteuer wiederherzustellen.

### Vorherigen Ort automatisch schließen

Diese Einstellung gilt während einer **aktiven Live-Session**.

Wenn ein Ort auf `In Besuch` gesetzt wird, wird der zuvor `In Besuch` befindliche Ort automatisch als `Besucht` markiert.

## Kampf

Der Bereich `Kampf` bündelt die globalen Einstellungen des Kampfsystems.

Hier findest du Darstellungsoptionen und Einstellungen für das `Spielerfenster`.

### Kampfbildschirm für Spieler aktivieren

Das ist der Hauptschalter. Wenn er deaktiviert ist, zeigt DnDino im Spielerfenster kein Kampf-Intro, keinen aktuellen Zug, keine Runde und keine Endzusammenfassung; die zugehörigen Optionen werden ausgeblendet.

### Spielerfenster öffnen, wenn es geschlossen ist

Wenn aktiv, öffnet DnDino das `Spielerfenster` automatisch beim Start des Kampfs. Wenn deaktiviert, wird die Darstellung nur aktualisiert, wenn das Fenster bereits offen ist.

### Spielerfenster auch mit nur einem Monitor öffnen

Diese Option erscheint nur, wenn das automatische Öffnen aktiv ist. Sie ist für Setups ohne zweiten Bildschirm gedacht.

## Kampfpräsentation

Dieser Unterbereich steuert die allgemeinen Informationen, die während der Begegnung angezeigt werden:

- `Kampf-Intro für Spielende anzeigen`
- `Endzusammenfassung für Spielende anzeigen`
- `Runde auf dem Spielerbildschirm anzeigen`
- `Kampfdauer auf dem Spielerbildschirm anzeigen`
- `Nächsten Zug auf dem Spielerbildschirm anzeigen`

Die Kampfdauer wird als lesbarer Timer angezeigt; wenn der Kampf pausiert ist, hält die Zeit an.

## Heldeninformationen

Diese Optionen gelten, wenn der aktive Teilnehmende ein Held oder Verbündeter ist. Ein NSC oder Monster mit der Rolle `Verbündeter` verwendet also ebenfalls diese Einstellungen. Du kannst anzeigen:

- aktuelle, maximale und temporäre TP
- aktive Zustände

## NSC-Informationen

Diese Optionen gelten nur, wenn der aktive Teilnehmende ein nicht verbündeter NSC ist. NSCs mit der Rolle `Verbündeter` verwenden die Helden-/Verbündeten-Einstellungen. Du kannst getrennt anzeigen:

- aktuelle, maximale und temporäre TP
- aktive Zustände
- den echten Namen des NSC

Wenn NSC-Namen verborgen sind, verwendet das `Spielerfenster` den generischen Namen `NSC`.

## Monsterinformationen

Diese Optionen gelten nur, wenn der aktive Teilnehmende ein nicht verbündetes Monster ist. Monster mit der Rolle `Verbündeter` verwenden die Helden-/Verbündeten-Einstellungen. Du kannst getrennt anzeigen:

- aktuelle, maximale und temporäre TP
- aktive Zustände
- den echten Namen der Feinde

Wenn Monster-/Feindnamen verborgen sind, verwendet das `Spielerfenster` den generischen Namen `Feind`.

## Medien

Der Bereich `Medien` bündelt Einstellungen zur Bildverwaltung und zu Präsentationsfenstern.

### Bilder für Spielende im Vollbild

Wenn aktiv, werden Bilder, die den Spielenden gezeigt werden, im Vollbild geöffnet.

### SL-Bilder auf dem Hauptmonitor

Diese Option sorgt dafür, dass das SL-Fenster standardmäßig auf dem zuerst verfügbaren Bildschirm geöffnet wird.

### Größe des SL-Fensters merken

Wenn aktiv, behält das SL-Fenster beim erneuten Öffnen eines Bildes:

- die letzte Größe
- die letzte Position

## Medienwartung

Der Bereich `Medienwartung` deckt die technische Seite der Bildverwaltung ab.

Von hier aus kannst du `Nicht verwendete Medien bereinigen` starten. Dabei prüft die App gespeicherte Bilddateien und entfernt solche, die nicht mehr mit irgendeiner Entität verknüpft sind.

## Thema

Der Bereich `Thema` erlaubt dir die Auswahl der **globalen Farbpalette** der App.

Jedes Thema zeigt eine kleine visuelle Vorschau seiner Hauptfarben, damit du sofort sehen kannst, wie sich die Oberfläche verändern wird.

## Datenbank

Der Bereich `Datenbank` ist einer der wichtigsten für die Datensicherheit.

Hier findest du:

- den Pfad des Datenordners
- den Pfad der SQLite-Datenbank
- den Pfad des Backup-Ordners
- Informationen über die neuesten Snapshots

### Automatisches Backup

Du kannst wählen:

- die Frequenz des automatischen Backups
- die maximale Anzahl automatischer Snapshots, die aufbewahrt werden sollen

### Cloud-Snapshots

DnDino verwaltet auch das Verhalten von Cloud-Snapshots.

Hier kannst du festlegen, wie sich Cloud-Sicherungen verhalten sollen, und den aktuellen Status über den Zusammenfassungstext im Bildschirm ablesen.

### Hauptaktionen

Im Panel `Datenbank` findest du die wichtigsten Wartungsschaltflächen:

- `Datenordner öffnen`
- `Backup-Ordner öffnen`
- `Snapshot erstellen...`
- `Snapshot wiederherstellen...`
- `Aus iCloud wiederherstellen`

### App-Daten zurücksetzen

Die Funktion `App-Daten zurücksetzen` löscht:

- die App-Datenbank
- die App-Medien

behält jedoch bereits erstellte Backups.

### Letzte Snapshots

Im unteren Teil des Bereichs `Datenbank` zeigt DnDino außerdem die Liste der zuletzt gefundenen Snapshots an.

Für jeden Snapshot werden angezeigt:

- Dateiname
- Datum
- Größe

## Diagnose

Der Bereich `Diagnose` dient dazu, den technischen Zustand der von der App verwendeten SQLite-Datenbank zu prüfen.

Hier kannst du:

- Diagnosedaten aktualisieren
- den Datenbankpfad sehen
- prüfen, ob die Datei existiert
- Dateigröße und Änderungsdatum überprüfen
- die SQLite-Version sehen

### Tabellen

Die Diagnose zeigt außerdem die Liste der in der Datenbank gefundenen Tabellen zusammen mit der Anzahl der Datensätze in jeder einzelnen.

## Support

Der Bereich `Support` bündelt die schnellen Wege, um die entwickelnde Person der App zu kontaktieren.

Hier findest du:

- die Support-E-Mail
- die Schaltfläche `Support anfordern`
- die Schaltfläche `Vorschlag senden`
- die Schaltfläche `E-Mail kopieren`

## Lizenzen

Der Bereich `Lizenzen` sammelt die rechtlichen Hinweise und Quellenangaben, die von der App verwendet werden.

Derzeit enthält er insbesondere den Teil zum **System Reference Document 5.2** von Dungeons & Dragons mit Verweisen:

- auf das SRD-Dokument
- auf die Lizenz `CC-BY-4.0`

!!! tip
    Wenn du DnDino zum ersten Mal einrichtest, sind die nützlichsten Bereiche, die du sofort prüfen solltest, `Allgemein`, `Topbar`, `Kampf` und `Datenbank`. Das sind in der Regel die Bereiche, die sich am stärksten auf den täglichen Einsatz und auf die Datensicherheit auswirken.
## Ergänzungen in Version 1.4

Der Bereich `Datenbank` heißt jetzt `Datenbank und Medien`.

In Release-Builds zeigt DnDino keine internen technischen Pfade mehr. Stattdessen konzentriert sich der Bereich auf nützliche Informationen: Datenbankgröße, Anzahl gespeicherter Bilder, Gesamtgröße der Bilder, Snapshots, Backup-Export und Medien-Export.

Snapshots und App-Medien können über den normalen macOS-Speicherdialog an einen vom Benutzer gewählten Ort exportiert werden. Die Medien bleiben trotzdem in der App-Sandbox kopiert, damit DnDino keine Referenzen verliert, wenn Originaldateien verschoben oder gelöscht werden.

Der Diagnosebereich ist Debug-Builds vorbehalten und wird in der Release-Version nicht angezeigt.
