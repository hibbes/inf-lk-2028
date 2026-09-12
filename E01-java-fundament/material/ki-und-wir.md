# KI und wir: Lernen, Fach, Gesellschaft (Dienstag, 15.09.2026)

Wir beginnen den Kurs nicht mit Java, sondern mit der Frage, ob ihr Java überhaupt noch lernen
müsst. Die Antwort erarbeiten wir gemeinsam. Das hier ist das Material der Stunde und danach der
Ort, an dem unsere Vereinbarung steht.

## Die fünf Thesen

1. Programmieren lernen lohnt sich nicht mehr, das macht die KI.
2. Ich hatte schon einmal eine KI-Antwort, die überzeugend klang und falsch war.
3. Wer KI benutzt, lernt weniger.
4. In zehn Jahren gibt es den Beruf „Softwareentwicklerin“ nicht mehr.
5. Ich will wissen, wie das Ding von innen funktioniert.

## Die drei Tische

**Tisch Lernen:** Was hilft dir beim Lernen, was schadet? Welche Regel willst du für dich selbst?

**Tisch Fach:** Was ändert sich am Programmieren und an der Informatik? Was bleibt wichtig, was
wird wichtiger?

**Tisch Gesellschaft:** Arbeit, Information, Macht, Energie, Fairness. Drei Chancen, drei Risiken,
eine Forderung. Hilfsfragen: Wer verdient daran, wer zahlt? Was passiert mit der Aufgabe, die gerade
ein Mensch macht?

## Was ein Sprachmodell tut (in acht Sätzen)

Ein großes Sprachmodell ist eine Wahrscheinlichkeitsmaschine für Sprache. Es wurde mit riesigen
Textmengen darauf trainiert, immer nur das nächste Wortstück zu erraten. Wörter werden dabei zu
Zahlen, zu Koordinaten in einem Bedeutungsraum, in dem „König“ und „Königin“ nah beieinander liegen.
Bei jedem Wort entscheidet das Modell, auf welche anderen Wörter im Text es achten muss (das heißt
Attention und ist der Kern der Transformer-Architektur). Dann rät es das wahrscheinlichste nächste
Wortstück, hängt es an und macht weiter. Mehr nicht. Es hat kein Weltbild und keine Datenbank, in der
es nachschlägt, sondern ein Gefühl dafür, wie plausibler Text klingt. Deshalb kann es brillant klingen
und trotzdem selbstbewusst Unsinn erzählen, und es weiß nicht, dass es nicht weiß.

Alles, was unter einem solchen Modell liegt, ist Stoff dieses Kurses: wie Daten codiert werden, was
ein Algorithmus kostet, was berechenbar ist und was nicht, wie Verschlüsselung funktioniert. Am Ende
von J2 schauen wir in das Modell hinein.

## Unsere KI-Vereinbarung

Entwurf vom 15.09., beschlossen am 16.09.2026 (die beschlossene Fassung ersetzt diesen Text).

1. **Lernen zuerst.** Die Übungen in der Schmiede und alles, was wir „von Hand“ üben, machen wir ohne
   KI. Klausuren und Abitur sind ohnehin ohne, und was dort zählt, muss im Kopf sein.
2. **Erklären lassen ist erlaubt, machen lassen nicht.** Ein guter Prompt heißt „Erklär mir, warum
   meine Schleife nicht endet“, kein guter heißt „Löse Aufgabe 3“.
3. **Wer KI-Hilfe genutzt hat, sagt es.** Ein Kommentar im Code oder ein Satz bei der Abgabe genügt.
   Das ist kein Geständnis, sondern Handwerk: Auch Profis schreiben dazu, woher Code stammt.
4. **Was du abgibst, kannst du erklären.** Bei Projektabgaben gibt es ein kurzes Gespräch über den
   eigenen Code.
5. **Keine Namen, keine Schuldaten in KI-Werkzeuge.** Der schulische Zugang ist AIS.chat über einen
   QR-Code, den die Lehrkraft freigibt; dort landen keine Eingaben im Training. Andere Werkzeuge nur
   privat und ohne Daten anderer Menschen.
6. **Ab Einheit 8 arbeiten wir bewusst mit KI als Programmierpartner**, mit git, mit Tests und mit
   den Regeln von oben.

## Zum Weiterlesen

- Handreichungen zu KI für Schulen in Baden-Württemberg (ZSL): https://zsl-bw.de/,Lde/Startseite/lernen-ueberall/ki
- Die Java-Dokumentation, mit der wir KI-Behauptungen prüfen: https://docs.oracle.com/en/java/javase/21/docs/api/index.html
