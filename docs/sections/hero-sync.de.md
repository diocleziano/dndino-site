# DnDino Hero verbinden: Anleitung für die Spielleitung

Empfange die Charakterbögen der Spieler im Abenteuer und verwalte Spielwerte auf dem Mac. Die Verbindung bleibt lokal und benötigt keinen externen Server. Siehe auch die [Anleitung für Hero-Spieler](../companion/dndino-sync.md).

!!! info "Verfügbarkeit"
    Diese Seite beschreibt auch den neuen Datenabgleich, der für das nächste App-Update vorbereitet ist. Er benötigt Versionen von **DnDino und DnDino Hero, die ihn beide unterstützen**. Ältere Versionen können andere Optionen und ein anderes Startverhalten haben.

## Vorbereitung

Öffne das richtige Abenteuer. Nutzt dasselbe lokale Netzwerk, erlaubt den Zugriff auf das lokale Netzwerk und lasst WLAN sowie Bluetooth eingeschaltet. Die Geräte sollten in der Nähe sein. Jeder Spieler wählt in Hero den richtigen Charakter.

Live-Synchronisierung erfordert **iOS/iPadOS 26 oder neuer** auf Hero. Ältere Systeme unterstützen **nur das manuelle Senden des Bogens**, auch außerhalb eines Kampfes. **Verbunden bedeutet nicht synchronisiert.**

## Erste Verbindung

1. Starte im Bereich **DnDino Hero** der Karte **Live-Sitzung** auf der Abenteuerübersicht die Verbindung. Eine Spielsitzung muss dafür nicht gestartet werden.
2. Der Spieler öffnet **Einstellungen → DnDino-Verbindung**, sucht nach DnDino und wählt dein Abenteuer.
3. Autorisiere das Gerät nach Prüfung von Gerätename und Charakter.
4. Importiere einen neuen Bogen oder verknüpfe einen bestehenden. Prüfe die Bestätigung zum Ersetzen, damit nicht der falsche Bogen überschrieben wird.
5. Aktiviere **Automatische Synchronisierung** für dieses Gerät. **Nur die Spielleitung steuert die Aktivierung**; Hero zeigt den Status ohne zweiten Schalter.

Die Verknüpfung verwendet Kennungen, nicht nur Namen. Umbenennen erfordert keine neue Charakterkopie.

## Welche Werte bleiben erhalten?

**Hero liefert die Struktur des Bogens:** Stufen, Attribute, Beschreibungen, Zauber und Progressionskonfiguration verwaltet der Spieler.

Mit den neuen Versionen sendet Hero bei jeder Verbindung und Wiederverbindung zuerst einen vollständigen aktuellen Bogen. Auch erneutes Aktivieren erfordert den Abgleich. Stimmen alle Werte überein, erscheint kein Vergleich.

Andernfalls vergleicht das Abgleichfenster **aktuelle, maximale und temporäre TP, RK, heroische Inspiration, Zustände, verbleibende Ressourcen und verwendete Zauberplätze**. Wähle pro Unterschied den DnDino- oder Hero-Wert. **Hero ist vorausgewählt**. Die Sammelaktionen übernehmen alle Werte einer Seite; bestätige anschließend und warte auf das Ergebnis.

Beispiel: Behalte 18 TP von DnDino statt 24 aus Hero, aber übernimm Heros Zustände. Zustände werden **als vollständige Gruppe** gewählt und niemals automatisch zusammengeführt.

Ressourcenmaxima und Konfiguration stammen weiterhin aus Hero. Unvereinbare Kombinationen werden gemeldet. Nur dieses Gerät wartet; andere Spieler können weitermachen. Ändern sich Werte inzwischen, prüfe den aktualisierten Vergleich erneut. Wiederholen fordert frische Daten an. Das Schließen des Fensters oder Abbrechen der Verbindung trennt das Gerät. **Die Bestätigung allein aktiviert Live nicht.**

## Während des Spiels

Live tauscht unterstützte Werte aus: aktuelle/maximale/temporäre TP, RK, Inspiration und Zustände. Im Kampf wird der verknüpfte Teilnehmer berücksichtigt.

| Information | Verwendung |
| --- | --- |
| Verbrauchbare Progressionen | Verbleibend/Gesamt; Minus verbraucht, Plus stellt wieder her |
| Feste Progressionen der aktuellen Stufe | Informationskarten ohne Verbrauchsschalter |
| Zauberplätze | Gesamt und verwendet, bei Bedarf nach Quelle getrennt |

Zähler werden auch in DnDino gespeichert. Unterstützte Befehle der Spielleitung werden von Hero bestätigt. Bei gleichzeitigen Änderungen prüfe das Ergebnis und versuche es nach der Aktualisierung erneut. Neue Stufen oder Konfigurationen benötigen einen **vollständigen Bogen**, nicht nur Zählerupdates.

## Bogen anfordern, Chat und untere Leiste

Rechts neben dem Chat fordert der Downloadknopf den bereits verknüpften Bogen an, ohne erneutes manuelles Senden durch den Spieler. Voraussetzung: kompatibles, verbundenes und autorisiertes Hero. Während des Abgleichs ist er gesperrt; er aktiviert Live nicht.

Der Hero-Bereich in der unteren Leiste behält die während des aktuellen DnDino-Starts verbundenen Geräte auch nach Verbindungsabbruch. Prüfe Identität und Status, teste die Verbindung, öffne den Chat, steuere Live oder trenne das Gerät. Ein Test importiert keine Daten. **Privater Chat erfordert aktives Live**; ungelesene Nachrichten werden in der Leiste markiert.

## Wiederverbinden und Fehlerbehebung

Standardmäßig muss die Spielleitung Live bei jeder neuen Verbindung erneut aktivieren. Ein optionaler automatischer Start für bereits autorisierte Geräte ist in den Einstellungen verfügbar; der neue Abgleich bleibt erforderlich.

- **Mac nicht gefunden:** prüfe empfangsbereites Abenteuer, Netzwerk, lokale Netzwerkfreigaben und geöffnete Apps.
- **Verbunden, aber keine Updates:** prüfe Autorisierung, Zuordnung, iOS/iPadOS 26+, abgeschlossenen Abgleich und Live-Schalter.
- **Verbindung verloren:** Hero im Vordergrund lassen. Bei Rückkehr kann die App erneut verbinden; die Wiederverbinden-Taste hilft ebenfalls.
- Trennen beendet nur die aktuelle Verbindung und löscht keinen importierten Bogen.
- Zuordnung entfernen widerruft Autorisierung und Verknüpfungen dieses Abenteuers; Gerät vergessen gilt für alle Abenteuer. Importierte Bögen bleiben erhalten.

Teste vor der Sitzung eine kleine TP-Änderung und prüfe das Ergebnis auf beiden Geräten.
