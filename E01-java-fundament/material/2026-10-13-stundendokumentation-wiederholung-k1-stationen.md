# Stundendokumentation Dienstag, 13.10.2026: Wiederholung für Klausur 1 an Stationen

**Informatik LK, 1./2. Stunde | E1 Java-Fundament und Block 8 (Klassen und Objekte) | Vorbereitung auf Klausur 1 am Di 20.10.**

## Was wir gemacht haben

1. **Ampel und Fragenwand:** Alle haben an der Tafel für die Blöcke 1 bis 8 der
   [Wiederholliste](klausur-1-wiederholliste.md) mit einem Strich eingetragen, wie sicher sie sind
   (grün, gelb, rot). Dazu hat jede und jeder eine offene Frage auf einen Zettel geschrieben, die
   Zettel hingen nach Blöcken sortiert an der Seitentafel.
2. **Stationen:** Mit dem Blatt [„Wiederholung für Klausur 1: fünf Stationen“](2026-10-13-wiederholung-k1-stationen.md)
   hat jede und jeder nach der eigenen Ampel mindestens zwei Stationen bearbeitet, von Hand und
   ohne Rechner wie in der Klausur. Danach mit dem Lösungsstreifen vom Pult selbst korrigiert, mit
   einem anderen Stift.
3. **Fragenrunde:** Die Fragen von der Fragenwand, die mehrere betreffen, an der Tafel geklärt,
   jeweils mit einem Beispiel aus den Stationen.
4. **Schmiede:** Unit 49 „E1 Java-Fundament“, Lektion 7 und 8 (Struktogramm, Javadoc); wer die
   schon hatte, Lektion 9 oder Unit 56, Lektion 2 (Klassen benutzen, Training).
5. **Ausblick:** Am Donnerstag, 15.10., schreiben wir in der 8./9. Stunde eine Probeklausur.

## Wenn du gefehlt hast

1. Hol dir das Blatt **„Wiederholung für Klausur 1: fünf Stationen“** aus dem Gruppenordner KW42.
2. Geh die [Wiederholliste](klausur-1-wiederholliste.md) durch und markier für jeden Block, wie
   sicher du bist (grün, gelb, rot).
3. Fang mit der Station an, die zu deinem schwächsten Block passt, und bearbeite mindestens zwei
   Stationen **von Hand**, ohne BlueJ.
4. Erst dann den Erwartungshorizont unten lesen und mit einem anderen Stift korrigieren.
5. Deine offenen Fragen bringst du am Donnerstag mit.

## Erwartungshorizont

Alle Ergebnisse sind in Java nachgeprüft. Welche Station zu welchem Block gehört:

| Station | Thema | Block der Wiederholliste |
|---------|--------------------------------------|------------|
| 1 | Code lesen mit Wertetabelle | 2 und 6 |
| 2 | Methode implementieren, Testfälle zuerst | 1 und 5 |
| 3 | Wert und Typ von Ausdrücken | 3 und 4 |
| 4 | Klassen und Objekte | 8 |
| 5 | Fehler finden, Javadoc | 7 |

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

### Station 2

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

### Station 3

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

### Station 4

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

### Station 5

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

### Zum Selbstprüfen

Erst selbst antworten, dann die erwartete Antwort lesen.

1. **Warum ist `(double) 17 / 5` gleich 3.4, `(double) (17 / 5)` aber 3.0?**\
   *Erwartet:* Im ersten Fall wird nur die 17 umgewandelt, dann rechnet Java `double / int`. Im
   zweiten Fall wird zuerst ganzzahlig geteilt (3), erst danach umgewandelt.
2. **Woran erkennst du in einer Klasse den Konstruktor?**\
   *Erwartet:* Er heißt wie die Klasse und hat keinen Rückgabetyp, auch kein `void`.
3. **Warum braucht `ausgiessen()` eine lokale Variable?**\
   *Erwartet:* Nach `inhalt = 0` ist der alte Wert weg. Man muss ihn vorher in einer lokalen
   Variablen merken, um ihn zurückgeben zu können.
4. **Welcher Testfall zeigt, dass `i <= a.length` ein Laufzeitfehler ist?**\
   *Erwartet:* Jedes Array, sogar das leere. Zum Beispiel `{2}`: Beim letzten Durchlauf ist
   `i = 1`, der Zugriff auf `a[1]` löst eine `ArrayIndexOutOfBoundsException` aus.

## Was als Nächstes drankommt

Donnerstag, 15.10., 8./9. Stunde: **Probeklausur** über 45 Minuten im Klausurstil, danach
korrigierst du selbst mit dem Erwartungshorizont. Bring die Wiederholliste mit und bring bis dahin
mindestens eine rote Ampel auf gelb.

**Klausur 1 am Dienstag, 20.10.** prüft E1 komplett und den Einstieg in Klassen und Objekte vom
06.10. (Block 8). Du schreibst von Hand, ohne BlueJ.
