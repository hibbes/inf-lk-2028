# Lösungen zu den fünf Stationen

**Informatik LK J1 | Dienstag, 13.10.2026 | erst nach deinem eigenen Versuch lesen**

Alle Ergebnisse sind in Java nachgeprüft.

## Station 1

a) `raetsel(new int[] {3, 5, 2, 8, 9})` liefert **3**.

| `i` | `a[i - 1]` | `a[i]` | `z` |
|-----|-----------|--------|-----|
| (vor der Schleife) | | | 0 |
| 1 | 3 | 5 | 1 |
| 2 | 5 | 2 | 1 |
| 3 | 2 | 8 | 2 |
| 4 | 8 | 9 | 3 |

b) Die Methode zählt, wie oft ein Element größer ist als sein Vorgänger, also die Anstiege im Array.

c) Beide Male **0**: Die Schleife beginnt bei `i = 1`. Bei Länge 0 und Länge 1 ist `1 < a.length` sofort falsch, die Schleife läuft nicht, `z` bleibt 0. Es gibt keinen Absturz, weil nie auf `a[0]` zugegriffen wird.

## Station 2

a) Zum Beispiel: `{2, -1, 4}` → `3.0`; `{-3, -2}` → `0.0` (keine positive Zahl); `{}` → `0.0` (leer); `{5}` → `5.0`; `{1, 2}` → `1.5` (prüft die Ganzzahldivision). Die Null ist nicht positiv: `{0, 4}` → `4.0`.

b)

```java
public static double mittelwertPositiv(int[] a) {
    int summe = 0;
    int anzahl = 0;
    for (int i = 0; i < a.length; i++) {
        if (a[i] > 0) {
            summe = summe + a[i];
            anzahl++;
        }
    }
    if (anzahl == 0) {
        return 0.0;
    }
    return (double) summe / anzahl;
}
```

Fallen: `summe / anzahl` ohne Cast rechnet ganzzahlig (`{1, 2}` gäbe `1.0`); ohne die Prüfung `anzahl == 0` wird durch 0 geteilt (bei `double` kommt `NaN` heraus, kein Absturz, aber falsch).

## Station 3

| Ausdruck | Wert | Typ | Warum |
|----------|------|-----|-------|
| `17 / 5` | `3` | `int` | Ganzzahldivision |
| `17 % 5` | `2` | `int` | Rest |
| `-17 % 5` | `-2` | `int` | Der Rest hat das Vorzeichen des linken Operanden |
| `(double) 17 / 5` | `3.4` | `double` | Der Cast gilt nur für die 17, dann `double / int` |
| `17 / 5 * 1.0` | `3.0` | `double` | erst `17 / 5 = 3`, dann `3 * 1.0` |
| `s.charAt(1) + 1` | `98` | `int` | `'a'` hat den Code 97, `char + int` ist `int` |
| `s.substring(1, 3)` | `"av"` | `String` | Index 1 und 2, die 3 gehört nicht dazu |
| `"7" + 3 + 4` | `"734"` | `String` | von links: ab dem String wird verkettet |
| `7 + 3 + "4"` | `"104"` | `String` | erst `7 + 3 = 10`, dann verketten |
| `(int) 'B'` | `66` | `int` | Code von `'B'` |

## Station 4

a) Ausgabe: **`230 100`**

| nach | `b1.inhalt` | `b2.inhalt` |
|------|-------------|-------------|
| `new` | 0 (max 250) | 0 (max 100) |
| `b1.fuellen(200)` | 200 | 0 |
| `b2.fuellen(80)` | 200 | 80 |
| `b2.fuellen(50)` | 200 | 100 (130 wird auf 100 begrenzt) |
| `b1.fuellen(30)` | 230 | 100 |

b) Attribut: `inhalt` oder `max`. Konstruktor: `public Becher(int max)`. Parameter: `max` im Konstruktor oder `menge` in `fuellen`.

c)

```java
public int ausgiessen() {
    int vorher = inhalt;
    inhalt = 0;
    return vorher;
}
```

Die lokale Variable `vorher` ist nötig: Nach `inhalt = 0` wäre der alte Wert weg.

## Station 5

a)

| Zeile | Fehler | Fehlerart | Beleg | Korrektur |
|-------|--------|-----------|-------|-----------|
| 2 | Semikolon fehlt | Compiler | „';' expected“ | `int s = 0;` |
| 3 | `i <= a.length` | Laufzeit | `{2}` → `ArrayIndexOutOfBoundsException` bei `a[1]` | `i < a.length` |
| 4 | `% 2 == 1` prüft ungerade | semantisch | `{2, 3, 4}` liefert 3 statt 6 | `a[i] % 2 == 0` |

Hinweis: Bei negativen ungeraden Zahlen ist `% 2` sogar `-1`, `== 1` wäre also auch für „ungerade“ falsch. `== 0` ist für gerade Zahlen immer richtig.

b) Zum Beispiel:

```java
/**
 * Berechnet die Summe aller geraden Zahlen im Array.
 *
 * @param a das Array mit ganzen Zahlen (darf leer sein)
 * @return die Summe der geraden Elemente; 0, wenn es keine gibt
 */
```
