# Einstellungen

Der Bereich **Einstellungen** sammelt die globalen Voreinstellungen von DnDino. Hier arbeitest du nicht an einem einzelnen Abenteuer oder Charakter, sondern legst fest, **wie sich die App insgesamt verhalten soll**.

Die Einstellungen beeinflussen vor allem:

- das allgemeine Erscheinungsbild der Oberfläche
- das Verhalten der Topbar
- den Ablauf in `Orte`
- das Verhalten des `Kampfs`
- die Verwaltung von Bildern, Backups und Snapshots
- Support und Diagnose der Datenbank

## Inhalte, Hilfe und zusätzliche Themen

**Allgemein → Offizielle Inhalte** zeigt oder verbirgt SRD-Kataloge, ohne persönliche Daten zu löschen oder Verweise zu beschädigen. Die Einstellung gilt auch für die Listen. Siehe [Offizielle Inhalte](official-content.md).

Die standardmäßig aktiven **?**-Hilfeschaltflächen lassen sich global abschalten. **Halloween** ergänzt die Themen; **System** folgt weiterhin dem tatsächlichen macOS-Erscheinungsbild. Topbar, Kontextschaltflächen und Menüs verwenden einheitliche Layouts für lesbare Symbole und Texte.

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

### Bildschirm eingeschaltet lassen

Aktiviere unter **Einstellungen > Allgemein** die Option **Bildschirm eingeschaltet lassen**, damit sich das Display nicht automatisch ausschaltet, solange DnDino im Vordergrund ist. Das ist während einer Sitzung praktisch, wenn du Notizen liest oder Inhalte präsentierst, ohne ständig Maus oder Tastatur zu verwenden.

Die Option ist **standardmäßig ausgeschaltet**. Sie funktioniert auch im Batteriebetrieb, erhöht aber den Energieverbrauch. Deine Auswahl bleibt zwischen App-Starts gespeichert: Beim Wechsel zu einer anderen App wird die Anforderung freigegeben; bei der Rückkehr zu DnDino wird sie wieder aktiviert, sofern die Option noch eingeschaltet ist. Du kannst sie jederzeit über denselben Schalter ausschalten.

Es sind keine besonderen Berechtigungen erforderlich, und die Sicherheitseinstellungen von macOS werden nicht geändert. Manuelles Sperren, vom Benutzer angeforderter Ruhezustand, Zuklappen und Systemschutzfunktionen bleiben möglich. Unabhängige Bildschirmschoner- oder Sicherheitsrichtlinien werden nicht garantiert verhindert.

Kann macOS die Funktion nicht aktivieren, erscheint ein Hinweis. Schalte die Option aus und wieder ein, um es erneut zu versuchen. Beim vollständigen Zurücksetzen der Einstellungen wird sie wieder ausgeschaltet.

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

Anleitungen verwalten Sie unter [App und Anleitungen zurücksetzen](#app-and-guide-reset): Einführung erneut öffnen und kontextbezogene Hilfen zurücksetzen sind getrennte Aktionen ohne Datenlöschung.

## Topbar

Der Bereich `Topbar` definiert das Verhalten der Schnellwerkzeuge in der oberen Leiste der App. Die vollständige Beschreibung aller Schaltflächen findest du auf der Seite `Topbar`.

### Darstellung der Topbar

Du kannst wählen, ob die Topbar angezeigt wird:

- nur mit Symbolen
- oder mit Symbolen und Namen darunter

### Standardwürfel

Hier kannst du den **Standardwürfeltyp** des Würfelrollers in den `Schnellwerkzeugen` festlegen.

### Schnelles Öffnen von Charakteren

Jeder Treffer hat rechts zwei runde Schaltflächen: **Anzeige** öffnet den kompakten Bogen, **Bearbeiten** den Editor. Die Zeile selbst öffnet keinen Bogen mehr; eine globale Auswahl zwischen den beiden Aktionen entfällt. [Topbar](topbar.md).

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

Darstellungs- und Sichtbarkeitsoptionen sind **Vorgaben für neue Kämpfe**. Ändere einzelne Kämpfe über [Verwaltung des zweiten Bildschirms und Sichtbarkeit](combat.md#player-screen-options), auch gruppenweise. Gespeicherte Entscheidungen anderer Kämpfe werden nicht überschrieben.

Die Aktivierung des Spielerbildschirms und das Öffnungsverhalten der Fenster bleiben global. Bestehende, nicht abgeschlossene Kämpfe speichern die Ausgangswerte einmalig beim ersten Öffnen.

### Kampfbildschirm für Spieler aktivieren

Diese Steuerelemente erscheinen nur, wenn **Kampfbildschirm für Spieler aktivieren** unter **Einstellungen > Kampf** eingeschaltet ist. Ausschalten blendet sie in der Vorbereitung und im laufenden Kampf aus; gespeicherte Entscheidungen bleiben erhalten. Ein zweiter Monitor muss weder angeschlossen noch das Spielerfenster bereits geöffnet sein.

### Spielerfenster öffnen, wenn es geschlossen ist

Wenn aktiv, öffnet DnDino das `Spielerfenster` automatisch beim Start des Kampfs. Wenn deaktiviert, wird die Darstellung nur aktualisiert, wenn das Fenster bereits offen ist.

### Spielerfenster auch mit nur einem Monitor öffnen

Diese Option erscheint nur, wenn das automatische Öffnen aktiv ist. Sie ist für Setups ohne zweiten Bildschirm gedacht.

## Kampfpräsentation

Diese Optionen sind Darstellungsvorgaben für neue Kämpfe; du kannst sie im einzelnen Kampf ändern, ohne die Einstellungen anzupassen:

- `Kampf-Intro für Spielende anzeigen`
- `Endzusammenfassung für Spielende anzeigen`
- `Runde auf dem Spielerbildschirm anzeigen`
- `Kampfdauer auf dem Spielerbildschirm anzeigen`
- `Nächsten Zug auf dem Spielerbildschirm anzeigen`

Die Kampfdauer wird als lesbarer Timer angezeigt; wenn der Kampf pausiert ist, hält die Zeit an.

## Heldeninformationen

Diese Optionen legen die anfängliche Sichtbarkeit von Teilnehmenden des Typs Held in neuen Kämpfen fest. Du kannst anzeigen:

- aktuelle, maximale und temporäre TP
- aktive Zustände

## NSC-Informationen

Diese Optionen legen die anfängliche Sichtbarkeit von NSC in neuen Kämpfen fest, auch bei der Rolle Verbündeter. Du kannst getrennt anzeigen:

- aktuelle, maximale und temporäre TP
- aktive Zustände
- den echten Namen des NSC

Wenn NSC-Namen verborgen sind, verwendet das `Spielerfenster` den generischen Namen `NSC`.

## Monsterinformationen

Diese Optionen legen die anfängliche Sichtbarkeit von Monstern in neuen Kämpfen fest. TP und Zustände verwenden sie auch bei Verbündeten; Namen nicht feindlicher Monster bleiben anfangs sichtbar. Du kannst getrennt anzeigen:

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

<!-- guide-coverage: MOD-042 MOD-043 MOD-049 MOD-051 MOD-060 MOD-061 MOD-062 MOD-070 MOD-071 MOD-073 MOD-077 MOD-078 MOD-079 MOD-080 MOD-086 MOD-088 MOD-145 MOD-146 MOD-147 MOD-148 MOD-163 MOD-164 MOD-168 MOD-170 -->

## Themen, Hintergründe und Deckkraft

**System** steht zuerst und folgt macOS. Weitere Themen sind in **Farbpaletten**, **Spezial** und **Jahreszeiten** gruppiert. Spezial enthält **Inferno** und **Magie**; alle vier Jahreszeiten zeigen illustrierte Fantasy-Landschaften mit Abenteurern. Hero verwendet dieselben Themen und Bilder.

Dekorative Hintergründe sind abschaltbar; alternativ importieren Sie einen **eigenen Hintergrund**. Ein neues Bild ersetzt das bisherige. Ein Themenwechsel deaktiviert den eigenen Hintergrund, löscht ihn aber nicht.

Der Deckkraftregler aktualisiert unterstützte Bereiche sofort, darunter Ortstitel und Suche, Abenteuerkopf, Heldenkarten und Sitzungen. Für Lesbarkeit behalten diese Flächen einen dunkleren Farbton oder abgeschwächte Transparenz; Texte, Bilder und Bedienelemente werden nicht transparent. Andere Bereiche bleiben undurchsichtig. **Standard** stellt die ursprünglichen Deckkräfte und die passende Reglerposition wieder her, nicht einen gemeinsamen Wert von 50 %.

Ein Themenwechsel erstellt die Hauptansicht neu und kehrt zu **Einstellungen → Thema** zurück. Offene Nebenfenster und ungespeicherte Entwürfe bleiben erhalten; die untere Leiste übernimmt das Thema. Hauptschaltflächen und Seitenleistenauswahl nutzen Themenfarben mit angepasstem Textkontrast. **System** behält native macOS-Steuerelemente bei.

Berechtigungen, Geräteverlauf, optionaler automatischer Live-Start sowie Trennen, Zuordnung entfernen und Gerät vergessen beschreibt [Verbindung mit Hero](hero-sync.md).

## Benachrichtigungen und Ton {#notification-settings}

Unter **Einstellungen → Hero-Geräte** lässt sich der Verlauf in der unteren Leiste ausblenden, ohne Banner abzuschalten. Ein separater, standardmäßig aktiver Schalter steuert Töne für **neue Nachrichten und Kopplungsanfragen**. Live-Änderungen, Verbindungen/Trennungen und Kampfhinweise bleiben lautlos. Siehe [Benachrichtigungen](topbar.md#notification-history).

## App und Anleitungen zurücksetzen {#app-and-guide-reset}

Diese Aktionen unterscheiden sich. Lesen Sie vor der Bestätigung die Erläuterung.

- **Einführung öffnen** startet die Einführung erneut, ohne Daten oder kontextbezogene Anleitungen zurückzusetzen. Die neue Einführung für 2.0.0 erscheint auch nach Abschluss der vorherigen.
- **Kontextbezogene Anleitungen erneut anzeigen** setzt nur Bildschirmhilfen zurück. Diese scrollen zu verdeckten Bereichen und öffnen benötigte Abschnitte.
- **App-Daten zurücksetzen**, auch unter Datenbank und Medien, löscht Archiv und Medien, behält aber Profil, Einstellungen, Anleitungen sowie lokale/iCloud-Backups.
- **Lokale Backups löschen** entfernt verwaltete manuelle und automatische Kopien, nicht aktuelle Daten oder extern exportierte Dateien.
- **iCloud-Kopie löschen** entfernt nur den App-Snapshot, sofern verfügbar. Aktivierte Cloud-Backups können ihn später neu erstellen.
- **Vollständig zurücksetzen**, unten getrennt mit doppelter Bestätigung, löscht Daten, Medien, verwaltete Backups, eigenen Hintergrund, Hero-Zugangsdaten, Profil, Einstellungen und Anleitungen und beendet die App. Externe Exporte bleiben unberührt.

Vor Archivaktionen Live-Sitzung und Nebenfenster schließen. Ohne iCloud muss lokales Zurücksetzen ausdrücklich gewählt werden; schlägt eine angeforderte Cloud-Löschung fehl, bleiben lokale Daten erhalten. Nicht rückgängig zu machen: Erhaltenswertes zuerst exportieren.
