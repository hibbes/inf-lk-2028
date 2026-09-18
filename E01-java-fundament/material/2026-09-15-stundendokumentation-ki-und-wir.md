# Stundendokumentation Dienstag, 15.09.2026: KI und wir

**Informatik LK, 1./2. Stunde | Einheit 1 „Java-Fundament“, Stunden 1 und 2 von 20**

Diese Seite hält fest, was in der Stunde passiert ist und welche Antworten erwartet waren. Sie ist
für alle da, die nachlesen wollen, und besonders für die, die gefehlt haben.

## Was wir gemacht haben

1. **Positionslinie** zu fünf Thesen: Aufstellen im Raum zwischen „stimme zu“ (Fenster) und „stimme
   nicht zu“ (Tür), zu jeder These zwei Begründungen aus dem Kurs.
2. **Kurzinput** „Was ein Sprachmodell tut“: Wahrscheinlichkeitsmaschine für Sprache, Wörter als
   Koordinaten, Attention, nächstes Wortstück raten.
3. **Drei Tische** (Lernen, Fach, Gesellschaft): schreiben, Galerie, Vorstellung.
4. **Entwurf der KI-Vereinbarung** am Beamer, Änderungswünsche gesammelt.
5. **Kursrahmen:** Abitur Informatik am Dienstag, 02.05.2028, 270 Minuten, Pflichtteil plus drei von
   vier Wahlaufgaben. Sieben Klausuren in zwei Jahren, die Termine setzt die Schule zentral an.
   Notentransparenz: schriftlich zu mündlich 2:1. Die drei Orte des Kurses (Repo, Schmiede, iServ).
6. **Anmeldung in der Schmiede** mit dem iServ-Konto, danach die Lektion „Git für Einsteiger“.

## Wenn du gefehlt hast

Arbeite in dieser Reihenfolge, und beantworte die Fragen erst selbst, bevor du weiterliest:

1. Lies die fünf Thesen und die drei Tischfragen in [`ki-und-wir.md`](ki-und-wir.md) und notiere zu
   jeder These in einem Satz, wo du stehst und warum.
2. Melde dich in der Schmiede an (learn.schiller-offenburg.de, „Mit iServ anmelden“). Der Kurs
   „Informatik LK J1“ erscheint automatisch. Falls nicht: Join-Code im Unterricht erfragen.
3. Arbeite die Lektion „Git für Einsteiger“ durch.
4. Fülle den Steckbrief aus und gib ihn nach.
5. Tritt dem Messenger-Raum „Informatik LK J1 (Abi 2028)“ bei.

## Erwartungshorizont

### Die fünf Thesen

Bei einer Positionslinie gibt es keine richtige Position. Erwartet war aber, dass jede Begründung
ein Beispiel oder einen Grund nennt und nicht nur ein Gefühl. So sah eine tragfähige Begründung aus:

| These | tragfähige Begründung, egal auf welcher Seite |
|---|---|
| 1. Programmieren lernen lohnt sich nicht mehr | Wer den erzeugten Code nicht lesen kann, kann ihn nicht prüfen und nicht verantworten. Gegenrichtung: Für Routinecode ist der Zeitgewinn real. |
| 2. Ich hatte schon eine überzeugende, falsche KI-Antwort | Ein konkreter Fall, an dem man sagen kann, woran der Fehler aufgefallen ist. Genau das ist die Kompetenz, um die es geht. |
| 3. Wer KI benutzt, lernt weniger | Es kommt auf die Nutzungsart an: erklären lassen baut auf, machen lassen ersetzt das eigene Denken. Diese Unterscheidung ist Punkt 2 unserer Vereinbarung geworden. |
| 4. In zehn Jahren gibt es den Beruf nicht mehr | Berufe verschwinden selten ganz, sie verschieben sich. Wer das behauptet, sollte sagen, welche Tätigkeit genau wegfällt. |
| 5. Ich will wissen, wie das Ding von innen funktioniert | Führt direkt in den Kursinhalt: Codierung, Laufzeit, Berechenbarkeit, Kryptologie. |

### Die drei Tische

- **Lernen:** Erwartet wurde eine Regel für sich selbst, die man am nächsten Tag befolgen kann, nicht
  ein allgemeiner Vorsatz. Brauchbar: „Erst selbst versuchen, dann fragen, und die Antwort
  nachvollziehen, bevor ich sie übernehme.“
- **Fach:** Was bleibt wichtig (Probleme zerlegen, Korrektheit prüfen, Datenstrukturen wählen), was
  wird wichtiger (Code lesen und beurteilen, Testfälle formulieren, Anforderungen präzise sagen).
- **Gesellschaft:** Drei Chancen, drei Risiken, eine Forderung. Erwartet war, dass zu jedem Punkt
  gesagt wird, wer profitiert und wer die Kosten trägt. Die Hilfsfragen zielten genau darauf.

### Unser Fazit

Der Kurs war sich am Ende einig: Wer KI nur nachplappert, ist ersetzbar. Wer die Thematik wirklich
versteht, wird mit KI produktiver. Und große Sprachmodelle bieten eine große Chance für
individualisiertes Lernen.

### Was ein Sprachmodell tut

Die Kurzfassung des Inputs steht in [`ki-und-wir.md`](ki-und-wir.md) im Abschnitt „Was ein
Sprachmodell tut (in acht Sätzen)“. Der Kernsatz, auf den es ankommt: Das Modell hat kein Weltbild
und keine Datenbank, in der es nachschlägt, sondern ein Gefühl dafür, wie plausibler Text klingt.
Deshalb kann es brillant klingen und trotzdem selbstbewusst Unsinn erzählen.

### Git für Einsteiger

Die Lektion prüft die Befehle, die du am Donnerstag im eigenen Projekt gebraucht hast:

| Befehl | wofür |
|---|---|
| `git init` | legt im Projektordner den versteckten Ordner `.git` an, in dem alle Speicherstände liegen |
| `git config user.name` und `git config user.email` | ohne diese Angaben verweigert git den ersten Commit („Author identity unknown“) |
| `git status` | zeigt, was neu oder geändert ist. Der Befehl, den man am häufigsten tippt |
| `git add .` | merkt alles in diesem Ordner für den nächsten Commit vor. Mit Dateinamen statt Punkt nur diese eine Datei |
| `git commit -m "Erste Fassung"` | legt den Speicherstand an. `-m` steht für message, die Anführungszeichen halten die Nachricht zusammen |
| `git log --oneline` | zeigt den Verlauf, ein Commit je Zeile |
| `git diff` und `git restore <Datei>` | zeigt die Änderungen seit dem letzten Commit bzw. holt die zuletzt gespeicherte Fassung zurück |

Eine `.gitignore` mit den Zeilen `*.class` und `*.ctxt` hält die erzeugten Dateien aus dem Verlauf
heraus. Versioniert wird der Quelltext, nicht das Übersetzungsergebnis.

## Hausaufgabe aus dieser Stunde

Bis Mittwoch, 16.09.: Steckbrief ausgefüllt mitbringen, einen Satz überlegen, den du an der
KI-Vereinbarung ändern oder ergänzen willst, dem Messenger-Raum beitreten.
