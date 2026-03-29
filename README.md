# BonScout — Einkaufsprofil aus Kassenbons

BonScout ist eine local-first Web-Anwendung zur Analyse von Kassenbons und zur Vorhersage des Einkaufsverhaltens.

## Funktionen

- **Automatisierte Analyse**: Erkennt Artikel, Preise und Mengen aus hochgeladenen Kassenbons (derzeit simuliert).
- **Wiederkaufsprognose**: Berechnet auf Basis deiner Kaufhistorie, wann Artikel voraussichtlich wieder benötigt werden (Daily, Weekly, Monthly, Long-lasting).
- **Profil-Kennzahlen**: Überblick über deine Ausgaben, die Anzahl der erkannten Artikel und die genutzten Geschäfte.
- **Einkaufsverhalten**: Zusammenfassung deiner meistgekauften Artikel und der Vorräte.
- **Local-First**: Alle Daten werden ausschließlich in deinem Browser (`localStorage`) gespeichert. Es werden keine Daten an einen Server übertragen.

## Bedienung

1. **Bon hochladen**: Klicke auf "Datei auswählen" oder ziehe ein Bild/PDF eines Kassenbons in das Upload-Feld.
2. **Profil einsehen**: Die Anwendung analysiert den Bon und aktualisiert sofort deine Kennzahlen und die Artikelliste.
3. **Details prüfen**: Klicke auf einen Artikel in der Liste, um detaillierte Statistiken zum Kaufintervall und dem nächsten erwarteten Bedarf zu sehen.
4. **Demo-Daten**: Nutze den Button "Demo-Daten hinzufügen", um die Funktionen mit Beispiel-Daten zu testen.

## Installation / Nutzung

Da BonScout eine reine HTML/JavaScript-Anwendung ist, muss keine Installation erfolgen. Öffne einfach die `BonScout.html` in einem modernen Webbrowser.
