# Stundendokumentation Donnerstag, 01.10.2026: Codeanalyse an Arrays im Abiturstil

**Informatik LK, 8./9. Stunde | Einheit 1 „Java-Fundament“, Stunden 13 und 14 von 20**

## Was wir gemacht haben

1. **Einstieg:** zwei Antworten auf „Beschreibe, was `geheim` tut“ (erste Freitextaufgabe der
   Schmiede-Lektion 6) verglichen. Welche bekommt die Punkte, und warum? Dazu die Operatoren
   bestimmen, angeben, beschreiben, erläutern, implementieren, analysieren.
2. **Aufgabe 1 allein und ohne Rechner:** `geheim1` mit einer Wertetabelle durchgerechnet,
   beschrieben, Beispielarrays gesucht und erläutert, warum die Schleife bei 1 beginnt.
3. **Aufgabe 2 zu zweit:** `geheim2` dreht ein Array um. Was passiert, wenn man die Schleifengrenze
   ändert oder die Hilfsvariable streicht?
4. **Aufgabe 3 zu zweit:** lineare Suche `indexVon`, erst die Testfälle auf Papier, dann in BlueJ
   implementiert und alle Testfälle in `main` aufgerufen.
5. **Aufgabe 4:** drei Fehler in `anzahlMaximum` finden, jeden mit einem Array belegen, korrigieren.
   Wer fertig war, hat in der Schmiede die Ausgabeaufgaben der Lektion 6 gemacht.
6. **Sicherung ins Heft:** „Beschreiben: der Zweck in ganzen Sätzen. Erläutern: der Zweck und das
   Warum. Bestimmen: mit Wertetabelle.“

## Wenn du gefehlt hast

1. Hol dir das Blatt „Codeanalyse an Arrays“ aus dem Gruppenordner KW40.
2. Mach **Aufgabe 1 auf Papier und ohne Rechner**, mit Wertetabelle. Genau so sieht der Pflichtteil
   der Klausur aus.
3. Schreib für Aufgabe 3 **zuerst** deine Testfälle auf, dann erst den Code in BlueJ.
4. Vergleiche danach mit dem Erwartungshorizont. Achte bei „beschreiben“ darauf, ob du den Zweck
   triffst oder nur die Zeilen vorliest.

## Erwartungshorizont

Alle Methoden sind mit `javac` 25 übersetzt und mit den genannten Arrays ausgeführt; die Ergebnisse
unten stammen aus diesen Läufen.

### 0. Einstieg: beschreiben, aber richtig

```java
public static int geheim(String s) {
    int z = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == ' ') {
            z++;
        }
    }
    return z + 1;
}
```

*Schwach (vorgelesen, keine Punkte beim Operator „beschreiben“):* „Zuerst wird z auf 0 gesetzt.
Dann läuft eine for-Schleife über den String. Wenn das Zeichen ein Leerzeichen ist, wird z erhöht.
Am Ende wird z plus 1 zurückgegeben.“

*Gut:* „Die Methode bestimmt die Anzahl der Wörter in einem Text, in dem die Wörter durch genau ein
Leerzeichen getrennt sind. Dazu zählt sie die Leerzeichen und addiert eins, weil n Wörter n minus 1
Zwischenräume haben.“ Für „Java will nur spielen“ liefert sie 4. Der zweite Satz ist schon ein Stück
Erläuterung: Er sagt, **warum** das `+ 1` dasteht.

**Die Operatoren auf einen Blick:**

| Operator | Was du lieferst |
|---|---|
| bestimmen | ein Ergebnis mit nachvollziehbarem Weg, zum Beispiel einer Wertetabelle |
| angeben | das Ergebnis, ohne Begründung |
| beschreiben | in ganzen Sätzen, **was** der Code tut, auf der Ebene des Zwecks |
| erläutern | beschreiben **und** begründen, **warum**, gern mit Beispiel |
| implementieren | lauffähigen Java-Code schreiben |
| analysieren | Fehler oder Eigenschaften herausarbeiten und belegen |

### 1. Aufgabe 1: `geheim1`

**a)** Wertetabelle für `{3, 5, 5, 8, 2, 9}`:

| i | a[i - 1] | a[i] | a[i] > a[i - 1]? | z |
|---|---|---|---|---|
| Start | | | | 0 |
| 1 | 3 | 5 | ja | 1 |
| 2 | 5 | 5 | nein | 1 |
| 3 | 5 | 8 | ja | 2 |
| 4 | 8 | 2 | nein | 2 |
| 5 | 2 | 9 | ja | 3 |

Rückgabewert **3**.

**b)** Die Methode zählt, wie oft im Array ein Element echt größer ist als sein Vorgänger, also die
Anzahl der Anstiege zwischen benachbarten Elementen. Gleich große Nachbarn zählen nicht.

**c)** Ergebnis 0: jedes Array ohne Anstieg, zum Beispiel `{5, 4, 3, 2, 1}` oder `{7, 7, 7, 7, 7}`.
Ergebnis 4: jedes echt steigende Array, zum Beispiel `{1, 2, 3, 4, 5}`. Mehr als 4 geht bei Länge 5
nicht, weil es nur vier Nachbarpaare gibt.

**d)** Im Rumpf wird `a[i - 1]` gelesen. Bei `i = 0` wäre das `a[-1]`, ein Index, den es nicht
gibt: Das Programm bricht mit `ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 6`
ab. Inhaltlich: Das erste Element hat keinen Vorgänger, mit dem es verglichen werden könnte. Die
Schleife läuft deshalb über alle Paare `(i - 1, i)` mit `i` von 1 bis `a.length - 1`. Für ein leeres
Array und ein Array mit einem Element läuft sie gar nicht und liefert 0.

### 2. Aufgabe 2: `geheim2`

**a)** Ergebnis `{5, 4, 3, 2, 1}`. Die Schleife läuft `5 / 2 = 2` Mal (Ganzzahldivision, siehe
29.09.): Sie tauscht 1 mit 5 und 2 mit 4. Die 3 in der Mitte bleibt stehen.

**b)** Die Methode kehrt die Reihenfolge der Elemente im Array um. Sie gibt nichts zurück, sondern
verändert das übergebene Array selbst. Dazu tauscht sie jeweils das i-te Element von vorn mit dem
i-ten von hinten, bis die Mitte erreicht ist.

**c)** Ergebnis `{1, 2, 3, 4, 5}`, also unverändert. *Erläuterung:* Die Schleife läuft jetzt fünf
Mal. In der ersten Hälfte (i = 0, 1) wird umgekehrt wie vorher, bei i = 2 tauscht sich die Mitte mit
sich selbst, und in der zweiten Hälfte (i = 3, 4) werden dieselben Paare noch einmal getauscht, also
zurückgetauscht. Doppelt vertauscht ist gar nicht vertauscht.

**d)** Ergebnis `{5, 4, 3, 4, 5}`. *Erläuterung:* Nach `a[i] = a[a.length - 1 - i]` ist der alte
Wert von `a[i]` überschrieben und verloren. Die zweite Zuweisung kopiert deshalb nur den neuen Wert
zurück, beide Positionen enthalten danach den hinteren Wert. Die Hilfsvariable `h` rettet den alten
Wert, bevor er überschrieben wird (Dreieckstausch).

*Zum Weiterdenken (Vorgriff auf E2):* Warum ist das Array in `main` nach dem Aufruf verändert,
obwohl die Methode `void` ist? Weil beim Aufruf nur ein Verweis auf das Array übergeben wird, keine
Kopie. Bei einem `int` ist das anders, siehe die Schmiede-Aufgabe „Was steht am Ende in `a`?“ unten.

### 3. Aufgabe 3: lineare Suche

**a)** Testfälle für `{4, 9, 1, 9, 7}`, aufgeschrieben **vor** dem Code:

| Aufruf | erwartet | Randfall? |
|---|---|---|
| `indexVon(a, 1)` | 2 | nein, Normalfall |
| `indexVon(a, 9)` | 1 | ja: kommt doppelt vor, der **erste** Index zählt |
| `indexVon(a, 4)` | 0 | ja: erstes Element |
| `indexVon(a, 7)` | 4 | ja: letztes Element |
| `indexVon(a, 5)` | -1 | ja: kommt nicht vor |
| `indexVon(new int[0], 3)` | -1 | ja: leeres Array |

Vier davon plus das leere Array genügen; der doppelte und der fehlende Wert sollten dabei sein.

**b)** Musterlösung:

```java
public class Suche {

    public static int indexVon(int[] a, int x) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] == x) {
                return i;       // erster Treffer: sofort zurück
            }
        }
        return -1;              // Schleife ohne Treffer durchlaufen
    }

    public static void main(String[] args) {
        int[] a = {4, 9, 1, 9, 7};
        System.out.println(indexVon(a, 9));          // erwartet: 1
        System.out.println(indexVon(a, 1));          // erwartet: 2
        System.out.println(indexVon(a, 4));          // erwartet: 0
        System.out.println(indexVon(a, 7));          // erwartet: 4
        System.out.println(indexVon(a, 5));          // erwartet: -1
        System.out.println(indexVon(new int[0], 3)); // erwartet: -1
    }
}
```

Zwei häufige Fehler, beide übersetzen ohne Meldung:

- `return -1;` im `else`-Zweig **innerhalb** der Schleife: Dann wird nur `a[0]` geprüft, und
  `indexVon(a, 9)` liefert -1.
- Eine Merkvariable ohne Abbruch (`pos = i;` bei jedem Treffer): Dann kommt der **letzte** Treffer
  heraus, `indexVon(a, 9)` liefert 3.

Beide Fehler fallen nur auf, wenn man den doppelten Wert testet. Deshalb gehören Randfälle in die
Testtabelle.

**c)** Die Methode kann erst sicher -1 melden, wenn sie jedes Element angesehen hat, denn der
gesuchte Wert könnte an jeder Stelle stehen; das Array ist nicht sortiert, es gibt also keinen
Hinweis, wo man aufhören darf. Der schlechteste Fall tritt ein, wenn `x` gar nicht vorkommt oder nur
an der letzten Stelle steht. Dann braucht sie `a.length` Vergleiche. Warum ein sortiertes Array
schneller durchsucht werden kann, sehen wir in E5 bei der binären Suche.

### 4. Aufgabe 4: drei Fehler in `anzahlMaximum`

**a)**

| Nr. | Stelle | Fehler | zeigt sich an | Ergebnis |
|---|---|---|---|---|
| 1 | Schleifenkopf | `i <= a.length` greift auf `a[a.length]` zu | jedem Array, zum Beispiel `{2, 5, 5}` | `ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 3` |
| 2 | `int max = 0;` | Startwert kommt nicht aus den Daten | `{-4, -2, -2}` (Fehler 1 behoben) | 0 statt 2 |
| 3 | `anzahl` wird bei neuem Maximum nicht zurückgesetzt | frühere, kleinere Maxima werden mitgezählt | `{2, 5, 5}` (Fehler 1 behoben) | 3 statt 2 |

Bei `{5, 5, 2}` fällt Fehler 3 nicht auf (Ergebnis 2), weil das Maximum gleich am Anfang steht.
Genau deshalb braucht es Testfälle, bei denen das Maximum spät kommt.

**b)** Korrigierte Fassung, getestet mit `{2, 5, 5}` (2), `{-4, -2, -2}` (2), `{5, 5, 2}` (2),
`{1, 2, 3}` (1) und `{7}` (1):

```java
public static int anzahlMaximum(int[] a) {
    int max = a[0];
    int anzahl = 0;
    for (int i = 0; i < a.length; i++) {
        if (a[i] > max) {
            max = a[i];
            anzahl = 1;          // neues Maximum: neu zählen
        } else if (a[i] == max) {
            anzahl++;
        }
    }
    return anzahl;
}
```

Auch richtig und gut lesbar: zwei Durchläufe, erst mit `maximum(a)` vom 22.09. das Maximum
bestimmen, dann zählen, wie oft es vorkommt. Für die Klausur ist das völlig in Ordnung.

Die Frage für Dienstag bleibt stehen: Welchen der drei Fehler hätte der Compiler gefunden?

### 5. Schmiede Lektion 6: die Ausgabeaufgaben

| Aufgabe | Ergebnis | warum |
|---|---|---|
| `s += i` mit `i = 1; i <= 10; i += 3` | `22` | `i` nimmt 1, 4, 7, 10 an: 1 + 4 + 7 + 10 = 22 |
| zwei Schleifen, innen `j = i` bis `j < 4` | `10` mal „x“ | die innere Schleife läuft 4, 3, 2 und 1 Mal |
| `int a = 5; int b = a; b = b * 2; a = a + b;` | `a` ist `15` | `b` bekommt eine **Kopie** von `a`; primitive Typen werden kopiert, nicht geteilt |

## Was als Nächstes drankommt

Dienstag, 06.10.: Fehlerarten (Compiler, Laufzeit, semantisch) mit Aufgabe 4 als Einstieg, der
Debugger in BlueJ, Struktogramme lesen, Javadoc-Kommentare. Donnerstag, 08.10.: Abschluss von E1
mit gemischten Aufgaben im Stil der Klausur.

**Klausur 1 am Dienstag, 20.10.** umfasst nur E1. Aufgaben wie heute (Wertetabelle, beschreiben,
erläutern, Fehler finden) sind genau der Typ, der dort drankommt.

**GFS:** Wer Informatik als GFS-Fach nehmen will, sagt es mir bis **Freitag, 23.10.**, siehe
[`gfs.md`](../../gfs.md).
