# Woche 1 (15. bis 17.09.2026): KI-Gespräch, Kursstart, Methoden, Arrays

## A. Das Wichtigste zum Kurs

- Fünf Stunden pro Woche: Di 1./2., Do 8./9., Mi 1./2. nur in ungeraden Kalenderwochen (in dieser Woche also ja, nächste Woche nein).
- Sieben Klausuren in zwei Jahren. Die Termine legt die Schule zentral fest, sie werden bekannt gegeben, sobald sie feststehen.
- Schriftliches Abitur Informatik: Dienstag, 02.05.2028, 270 Minuten, Pflichtteil plus drei von vier Wahlaufgaben.
- Drei Orte: dieses Repo (was wir gemacht haben, Aufgaben, Links), die Schmiede unter learn.schiller-offenburg.de (Üben mit Punkten, Anmeldung mit dem iServ-Konto), die iServ-Gruppe J1_LF_Inf1 (Forum, Dateien, Messenger).
- Arbeitsweise: Testfälle zuerst, dann Code. Was die Schmiede prüft, prüft ihr im Kopf vorher selbst.
- Zu KI im Kurs: siehe `ki-und-wir.md` (Thesen, Tischfragen, unsere Vereinbarung).

## B. Hausaufgaben der Woche

| bis | Aufgabe |
|---|---|
| Mi 16.09. | Steckbrief ausgefüllt mitbringen. Einen Satz überlegen, den ihr an der KI-Vereinbarung ändern oder ergänzen wollt. Messenger-Raum „Informatik LK J1 (Abi 2028)“ beitreten (dazu den Messenger einmal öffnen). |
| Do 17.09. | Schmiede, Lektion 2 „Methoden und Bedingungen“ fertig (`istSchaltjahr` und `notenpunkte` dürfen offen bleiben, die machen wir gemeinsam). |
| Di 22.09. | Schmiede, Lektion 3 „Schleifen und Arrays“: mindestens `summe`, `maximum`, `mittelwert`. Programm „Zahlenanalyse“ (Teil D) als Datei ins Forum der Gruppe. Teil C (Kopfrechnen) auf Papier vorbereiten. Freiwillig: Lektion 4 „Strings“ anfangen. |

## C. Kopfrechnen mit Arrays (Vorbereitung auf Dienstag, 22.09., ohne Rechner)

Gegeben ist `int[] a = {4, 9, 1, 7};`

1. Was liefert `a[a.length - 1]`? Und was passiert bei `a[a.length]`?
2. Was tut diese Schleife, und was steht am Ende in `s`?

```java
int s = 0;
for (int i = 0; i < a.length; i++) {
    if (a[i] % 2 == 1) {
        s += a[i];
    }
}
```

3. Diese Maximumsuche hat einen Fehler, der bei `{4, 9, 1, 7}` nicht auffällt. Bei welchem Array fällt er auf, und wie behebt man ihn?

```java
int max = 0;
for (int i = 0; i < a.length; i++) {
    if (a[i] > max) {
        max = a[i];
    }
}
```

## D. Programm „Zahlenanalyse“ (Donnerstag, in BlueJ)

BlueJ ist bis Ende der zweiten Einheit unser Werkzeug: neues Projekt anlegen, Klasse anlegen, Code schreiben, Rechtsklick auf die Klasse und `main` ausführen. Das Code Pad unten rechts rechnet Ausdrücke wie `7 / 2` sofort aus.

In der Schmiede bekamen eure Methoden die Zahlen als Text („3,1,4“) und haben sich das Array selbst gebaut. In einem echten Programm bekommt die Methode das Array direkt. Die Logik bleibt dieselbe.

Aufgabe: Lege eine Klasse `Zahlenanalyse` mit einer `main`-Methode an. Das Array steht fest im Code. Das Programm gibt Maximum, zweitgrößtes Element, Mittelwert und die Anzahl der geraden Zahlen aus. Jede dieser vier Größen wird von einer eigenen statischen Methode berechnet, die das Array als Parameter bekommt.

Starter:

```java
public class Zahlenanalyse {

    public static int maximum(int[] a) {
        // Startwert: das erste Element, nicht 0
        return 0;
    }

    public static int zweitgroesstes(int[] a) {
        // zwei Variablen: max und zweit, beide mit Integer.MIN_VALUE starten
        return 0;
    }

    public static double mittelwert(int[] a) {
        // Summe als int, Division als double
        return 0.0;
    }

    public static int anzahlGerade(int[] a) {
        return 0;
    }

    public static void main(String[] args) {
        int[] a = {12, -3, 7, 7, 25, 0, 18, 4};
        System.out.println("Maximum:       " + maximum(a));
        System.out.println("Zweitgroesstes: " + zweitgroesstes(a));
        System.out.println("Mittelwert:    " + mittelwert(a));
        System.out.println("Gerade Zahlen: " + anzahlGerade(a));
    }
}
```

Erwartete Ausgabe für das Array im Starter:

```
Maximum:       25
Zweitgroesstes: 18
Mittelwert:    8.75
Gerade Zahlen: 4
```

Erweiterung für Schnelle: `histogramm(int[] a)` liefert ein `int[]` der Länge 11, in dem an Position k steht, wie oft der Wert k (0 bis 10) im Array vorkommt. Gib das Histogramm zeilenweise aus. Genau so eine Aufgabe stand 2026 im Pflichtteil des Abiturs.

## E. Hinweiskarten (nur wenn es klemmt)

- **Die Methode gibt nichts zurück:** Jeder Weg durch die Methode braucht ein `return`, auch der Weg, auf dem die Schleife gar nicht läuft.
- **Schleife über ein Array:** `for (int i = 0; i < a.length; i++)`, der Index läuft von 0 bis `a.length - 1`.
- **Maximum:** `int max = a[0];` dann ab Index 1 vergleichen.
- **Mittelwert:** `(double) summe / a.length`, sonst rechnet Java ganzzahlig.
- **Zweitgrößtes:** Ist `x > max`, wandert das alte `max` nach `zweit` und `x` nach `max`. Ist `x` nur größer als `zweit` und ungleich `max`, wird `zweit` ersetzt.
