# Stundendokumentation Dienstag, 29.09.2026: Typen und Casts, Zahlenanalyse zu Ende

**Informatik LK, 1./2. Stunde | Einheit 1 „Java-Fundament", Stunden 9 und 10 von 20**

## Was wir gemacht haben

1. **Die offene Frage vom 22.09.** geklärt: Was liefert `zweitgroesstes` bei `{5, 5, 3}` und bei `{7, 7, 7}`?
2. **Typen und Casts vorhergesagt und getestet:** erst allein „Wert und Typ" in die Tabelle eingetragen, dann mit `TypenTest.java` am Beamer Zeile für Zeile geprüft. Schwerpunkte: Ganzzahldivision, Reihenfolge von Cast und Division, Abschneiden gegen Runden, Überlauf, `0.1 + 0.2`, `char` als Zahl, `+` bei Text.
3. **Die Zahlenanalyse fertiggestellt:** `mittelwert` und `anzahlGerade`, dazu für die Schnellen das Histogramm, und alles gegen die vier Selbsttest-Arrays geprüft.
4. **Besprochen:** die drei Fassungen von `mittelwert` (warum eine trotz Cast falsch ist) und `% 2` bei negativen Zahlen.
5. **Gesichert:** Projekt committet (`git commit -m "Zahlenanalyse fertig"`), dann in der Schmiede Lektion 3 und 5 geübt.

## Wenn du gefehlt hast

1. Sag für jede Zeile der Typen-Tabelle **erst selbst** Wert und Typ voraus, bevor du unten nachsiehst. Besonders `7 / 2`, `(double) 7 / 2`, `(double) (7 / 2)` und `100000 * 100000`.
2. Öffne dein BlueJ-Projekt und schreib `mittelwert` und `anzahlGerade` **selbst**, prüf sie mit den vier Arrays aus der Tabelle unten. Erst dann die Musterlösung lesen.
3. Wenn du die Schmiede-Lektionen 3 (Schleifen und Arrays) und 5 (Typen, Wertebereiche, Casts) noch offen hast: die stehen in **Unit 49 „E1 Java-Fundament"**, nicht in Unit 48.

## Erwartungshorizont

Alle Werte mit `javac` 25 und `TypenTest.java` geprüft.

### 1. Typen und Casts

| Ausdruck | Wert | Typ | warum |
|---|---|---|---|
| `7 / 2` | `3` | int | int durch int: der Rest fällt weg |
| `7 % 2` | `1` | int | der Rest |
| `-7 / 2` | `-3` | int | abgeschnitten Richtung 0 |
| `-7 % 2` | `-1` | int | der Rest hat das Vorzeichen von links |
| `7 / 2.0` | `3.5` | double | ein double reicht, dann rechnet Java mit Komma |
| `(double) 7 / 2` | `3.5` | double | Cast zuerst, dann Division |
| `(double) (7 / 2)` | `3.0` | double | zu spät: erst die int-Division, dann der Cast |
| `10 / 4 * 4` | `8` | int | von links: 10 / 4 = 2, dann 2 * 4 |
| `(int) 3.99` | `3` | int | schneidet ab, rundet nicht |
| `(int) -3.99` | `-3` | int | schneidet Richtung 0 ab |
| `Math.round(3.99)` | `4` | long | rundet, liefert aber long |
| `Integer.MAX_VALUE + 1` | `-2147483648` | int | Überlauf |
| `100000 * 100000` | `1410065408` | int | Überlauf, obwohl beide Zahlen passen |
| `(long) 100000 * 100000` | `10000000000` | long | ein long rettet die Rechnung |
| `0.1 + 0.2 == 0.3` | `false` | boolean | 0.1 + 0.2 = 0.30000000000000004 |
| `'A' + 1` | `66` | int | ein char ist eine Zahl (Unicode) |
| `"Summe: " + 3 + 4` | `"Summe: 34"` | String | von links: Text + 3 ist Text |
| `3 + 4 + " Summe"` | `"7 Summe"` | String | von links: erst 3 + 4 = 7 |

Zwei Fallen kommen in der Klausur als Codeanalyse wieder: Zeile `(double) (7 / 2)` (Cast zu spät) und Zeile `100000 * 100000` (Überlauf). Merksatz: **Java rechnet mit dem Typ der Operanden, nicht mit dem Typ des Ziels. Ein Cast wirkt nur auf das, was direkt rechts von ihm steht.**

### 2. Die offene Frage vom 22.09.: `zweitgroesstes`

- **`{5, 5, 3}`:** Zwei Antworten sind vertretbar. Meint „zweitgrößtes Element" den **zweitgrößten Wert**, ist **3** richtig (das liefert unsere Fassung wegen `x != max`). Meint es das **Element auf Platz 2 nach dem Sortieren**, ist **5** richtig (dann muss `x != max` weg und `x >= zweit` hinein). Entscheiden kann das nur die Aufgabenstellung.
- **`{7, 7, 7}`:** Es gibt keinen zweiten Wert. Die Methode liefert `Integer.MIN_VALUE` (-2147483648), eine Zahl, die gar nicht im Array steht. Sauber ist das nur mit einem Kommentar, der das festhält, oder mit der Voraussetzung, dass es zwei verschiedene Werte gibt. Den Javadoc dazu schreiben wir am 06.10.

### 3. Drei Fassungen von `mittelwert`

Array `{12, -3, 7, 7, 25, 0, 18, 4}`, Summe 70, Länge 8.

| Fassung | Ergebnis | warum |
|---|---|---|
| `return summe / a.length;` | 8.0 | `summe` und `a.length` sind `int`, also Ganzzahldivision 70 / 8 = 8; erst der `return` macht daraus 8.0 |
| `return (double) (summe / a.length);` | 8.0 | die Klammer wird zuerst gerechnet, wieder int-Division; der Cast macht aus 8 nur 8.0 |
| `return (double) summe / a.length;` | **8.75** | der Cast wirkt auf `summe`, damit ist ein Operand `double`, und Java teilt mit Komma |

Gleichwertig richtig: `summe / (double) a.length` oder `1.0 * summe / a.length`. Die Musterlösung:

```java
public static double mittelwert(int[] a) {
    int summe = 0;
    for (int x : a) {
        summe += x;
    }
    return (double) summe / a.length;   // Cast vor der Division
}
```

### 4. `anzahlGerade` und negative Zahlen

Im Starter-Array sind -3, 7, 7 und 25 ungerade, also **vier** ungerade Zahlen. Die Bedingung `a[i] % 2 == 1` zählt nur drei, weil `-3 % 2` in Java **-1** ergibt und nicht 1 (der Rest hat das Vorzeichen des linken Operanden). Sicher sind `% 2 != 0` für ungerade und `% 2 == 0` für gerade.

```java
public static int anzahlGerade(int[] a) {
    int anzahl = 0;
    for (int x : a) {
        if (x % 2 == 0) {   // == 0 ist auch für negative Zahlen richtig
            anzahl++;
        }
    }
    return anzahl;
}
```

### 5. Zahlenanalyse: Selbsttest

| Array | Mittelwert | gerade Zahlen | Summe | falsch mit `summe / a.length` |
|---|---|---|---|---|
| `{12, -3, 7, 7, 25, 0, 18, 4}` | 8.75 | 4 | 70 | 8.0 |
| `{-5, -12, -1, -8}` | -6.5 | 2 | -26 | -6.0 |
| `{9, 4, 9, 1}` | 5.75 | 1 | 23 | 5.0 |
| `{18, 25, 3, 7}` | 13.25 | 1 | 53 | 13.0 |

**Histogramm** (Anzahl je Wert). Für das Starter-Array kommt die 0 einmal vor, die 4 einmal, die 7 zweimal, alle anderen Werte nicht. Wer eine feste Skala nimmt (etwa 0 bis 25), zählt für jeden Wert die Treffer im Array.

## Was als Nächstes drankommt

Mittwoch (30.09.): Strings (`length`, `charAt`, `substring`, `equals` gegen `==`, Palindrom), Schmiede-Lektion 4. Donnerstag (01.10.): Codeanalyse und Fehlerarten. Wer die Zahlenanalyse noch nicht committet hat, bekommt am Donnerstag zu Beginn Zeit dafür.
