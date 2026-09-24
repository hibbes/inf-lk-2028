# Stundendokumentation Dienstag, 22.09.2026: Maximum und zweitgrößtes Element

**Informatik LK, 1./2. Stunde | Einheit 1 „Java-Fundament“, Stunden 7 und 8 von 20**

## Was wir gemacht haben

1. **Kopfrechnen mit Arrays** (Teil C, Frage 1 und 2): Code lesen und vorher sagen, was herauskommt,
   ohne Rechner.
2. **Programm „Zahlenanalyse“ in BlueJ weitergeführt** (Teil D von
   [`woche-1-aufgaben.md`](woche-1-aufgaben.md)): die Methoden `maximum` und `zweitgroesstes`.
3. **Die Falle beim Maximum:** Warum `int max = 0;` falsch ist, obwohl das Starter-Array ein
   richtiges Ergebnis liefert (Teil C, Frage 3).
4. **`zweitgroesstes` von Hand:** zwei Variablen laufen durch das Array mit, als Wertetabelle.
5. **Dann kam der Feueralarm.** Der Rest der Doppelstunde fiel aus: `mittelwert`, `anzahlGerade`,
   das Histogramm, Datentypen und Casts sowie die Schmiede-Lektion 3 holen wir nach.

## Wenn du gefehlt hast

1. Beantworte Teil C, Frage 1 und 2 aus [`woche-1-aufgaben.md`](woche-1-aufgaben.md) auf Papier,
   ohne Rechner, bevor du Abschnitt 1 unten liest.
2. Öffne dein BlueJ-Projekt vom 17.09. oder leg es neu an, mit dem Starter aus Teil D.
3. Schreib `maximum` und `zweitgroesstes` **selbst**, bevor du unten weiterliest. Die Hinweiskarten in
   Teil E helfen, wenn es klemmt.
4. Prüf deine beiden Methoden mit allen vier Arrays aus der Tabelle „Selbsttest“ unten. Erst wenn alle
   stimmen, lies die Musterlösung.

## Erwartungshorizont

### 1. Kopfrechnen mit Arrays (Teil C, Frage 1 und 2)

Gegeben ist `int[] a = {4, 9, 1, 7};`

**Frage 1.** `a[a.length - 1]` liefert **7**. Das Array hat vier Elemente, `a.length` ist 4, die
Indizes laufen von 0 bis 3. Der letzte Index ist also `a.length - 1 = 3`, und dort steht die 7.

`a[a.length]` greift auf Index 4 zu, den es nicht gibt. Das Programm übersetzt, bricht aber beim
Ausführen ab:

```
ArrayIndexOutOfBoundsException: Index 4 out of bounds for length 4
```

*Wichtig:* Der Compiler merkt das nicht, erst das laufende Programm. Java prüft jeden Array-Zugriff
und hält lieber an, als eine falsche Zahl zu liefern.

**Frage 2.** Die Schleife geht alle Elemente durch und addiert nur die, bei denen `a[i] % 2 == 1`
ist, also die **ungeraden Zahlen**. Am Ende steht in `s`: 9 + 1 + 7 = **17**.

| i | a[i] | a[i] % 2 | wird addiert? | s |
|---|---|---|---|---|
| Start | | | | 0 |
| 0 | 4 | 0 | nein | 0 |
| 1 | 9 | 1 | ja | 9 |
| 2 | 1 | 1 | ja | 10 |
| 3 | 7 | 1 | ja | 17 |

*Zum Weiterdenken:* Bei negativen Zahlen geht das schief. `-3 % 2` ergibt in Java **-1**, nicht 1,
und die -3 würde deshalb nicht mitgezählt. Wer „ungerade“ sicher prüfen will, schreibt
`a[i] % 2 != 0`.

### 2. Maximum

```java
public static int maximum(int[] a) {
    int max = a[0];                          // Startwert: das erste Element
    for (int i = 1; i < a.length; i++) {     // ab Index 1, a[0] ist schon drin
        if (a[i] > max) {
            max = a[i];
        }
    }
    return max;                              // nach der Schleife, nicht in ihr
}
```

Das ist wieder das Muster vom Donnerstag: **Startwert, Schleife, Aktualisierung.** Anders als bei der
Summe wird nicht immer aktualisiert, sondern nur, wenn ein größerer Wert kommt.

**Teil C, Frage 3: Warum `int max = 0;` falsch ist.**

```java
int max = 0;
for (int i = 0; i < a.length; i++) {
    if (a[i] > max) {
        max = a[i];
    }
}
```

*Erwartet:* Bei `{4, 9, 1, 7}` fällt nichts auf, `max` wird 9. Bei einem Array, in dem **alle Zahlen
negativ** sind, etwa `{-4, -9, -1, -7}`, ist keine Zahl größer als 0. `max` bleibt 0 und die Methode
liefert eine Zahl, **die gar nicht im Array steht**. Richtig ist -1.

*Behebung:* Den Startwert aus dem Array nehmen, `int max = a[0];`, und ab Index 1 vergleichen.
Ebenfalls richtig ist `int max = Integer.MIN_VALUE;`, der kleinste Wert, den ein `int` haben kann.

> **Merksatz:** Ein Startwert, der nicht aus den Daten kommt, ist eine Behauptung über die Daten. Die
> 0 behauptet: „Hier kommt mindestens eine Zahl ab 0 vor.“ Das stimmt nicht immer.

### 3. Zweitgrößtes Element

Zwei Variablen laufen mit: `max` und `zweit`. Beide starten mit `Integer.MIN_VALUE`, damit jede
echte Zahl größer ist.

```java
public static int zweitgroesstes(int[] a) {
    int max = Integer.MIN_VALUE;
    int zweit = Integer.MIN_VALUE;
    for (int i = 0; i < a.length; i++) {
        int x = a[i];
        if (x > max) {
            zweit = max;      // das alte Maximum rutscht auf Platz 2
            max = x;
        } else if (x > zweit && x != max) {
            zweit = x;        // nur Platz 2 wird ersetzt
        }
    }
    return zweit;
}
```

**Von Hand, Array `{3, 9, 2, 7}`:**

| Schritt | x | max | zweit | Regel |
|---|---|---|---|---|
| Start | | MIN | MIN | beide mit `Integer.MIN_VALUE` |
| 1 | 3 | 3 | MIN | x > max: altes max nach zweit, x nach max |
| 2 | 9 | 9 | 3 | x > max: die 3 rutscht auf Platz 2 |
| 3 | 2 | 9 | 3 | x weder > max noch > zweit: nichts passiert |
| 4 | 7 | 9 | 7 | x > zweit und x ≠ max: nur zweit wird ersetzt |

Ergebnis: **7.**

**Die zwei Stellen, an denen es schiefgeht:**

| Fehler | Bei welchem Array man es merkt | Was dann herauskommt |
|---|---|---|
| Das alte `max` wird nicht nach `zweit` verschoben (nur `max = x;`) | `{18, 25, 3, 7}`: Die 18 steht vor der 25 und geht verloren | 7 statt 18 |
| Die Bedingung `x != max` fehlt | `{9, 4, 9, 1}`: Die zweite 9 landet auf Platz 2 | 9 statt 4 |

Beide Fehler fallen **beim Starter-Array nicht auf**, das liefert trotzdem 18. Deshalb die
Selbsttests.

**Offene Frage, die wir noch klären:** Bei `{5, 5, 3}` liefert diese Fassung 3, nicht 5. Ist das
richtig? Das hängt davon ab, was „zweitgrößtes Element“ heißen soll: der zweitgrößte **Wert** (dann 3)
oder das Element auf **Platz 2**, wenn man sortiert (dann 5). Deshalb steht in einer guten
Aufgabenstellung dabei, was gemeint ist. Und was liefert die Methode bei `{7, 7, 7}`, wo es gar keinen
zweiten Wert gibt?

### 4. Selbsttest

Übersetzt und ausgeführt mit Java 25.

| Array | `maximum` | `zweitgroesstes` |
|---|---|---|
| `{12, -3, 7, 7, 25, 0, 18, 4}` (Starter) | 25 | 18 |
| `{-5, -12, -1, -8}` | -1 | -5 |
| `{9, 4, 9, 1}` | 9 | 4 |
| `{18, 25, 3, 7}` | 25 | 18 |

## Noch nicht hier

Die Lösungen zu `mittelwert`, `anzahlGerade` und zum Histogramm folgen, wenn
wir sie im Unterricht bearbeitet haben. Wer vorher weitermachen will: Die Hinweiskarten in Teil E von
[`woche-1-aufgaben.md`](woche-1-aufgaben.md) helfen.

## Was als Nächstes drankommt

Die Zahlenanalyse zu Ende (`mittelwert`, `anzahlGerade`), Datentypen, Wertebereiche und Casts, die
Schmiede-Lektion 3 „Schleifen und Arrays“.
