# Klausur 1 am Di 20.10.2026: Wiederholliste

**Informatik LK J1 | Stand 03.10.2026**

Die Klausur prüft **E1 Java-Fundament komplett**, nichts darüber hinaus. Die Aufgaben sind wie im Abitur Teil A gebaut: Code analysieren, eine Methode implementieren, Begriffe erklären. Du schreibst **von Hand**, ohne BlueJ.

**So gehst du vor:** Hake ab, was du sicher kannst. Bei jedem offenen Punkt steht, wo du nachliest (Stundendokumentationen im Ordner `material/`) und wo du übst (Schmiede, Unit 49 „E1 Java-Fundament“). Zu jedem Block gibt es eine kleine Probieraufgabe. Die Lösungen stehen am Ende, schau sie erst nach deinem eigenen Versuch an.

## 1. Methoden

- ☐ Ich lese und schreibe eine Methodensignatur: Rückgabetyp, Name, Parameterliste, z. B. `public static int summeBis(int n)`.
- ☐ Ich unterscheide **Parameter** (in der Signatur) und **Argument** (beim Aufruf).
- ☐ Ich erkläre, was `return` macht und warum eine `void`-Methode nichts zurückgibt.
- ☐ Ich weiß, dass eine lokale Variable nur in ihrem Block gilt (Gültigkeitsbereich).
- ☐ Ich formuliere **Testfälle vor dem Code**, auch Randfälle: 0, negative Zahlen, ein leeres Array.

**Nachlesen:** Stundendokumentationen 16.09. und 17.09. **Üben:** Schmiede L2 „Methoden und Bedingungen“.

**Probier dich (1):** Implementiere `public static boolean istSchaltjahr(int jahr)` und gib vier Testfälle an, die alle Regeln abdecken.

## 2. Bedingungen und Schleifen

- ☐ Ich verwende `if`/`else`, Vergleichsoperatoren und `&&`, `||`, `!` richtig.
- ☐ Ich schreibe `for`- und `while`-Schleifen und weiß, wann welche passt.
- ☐ Ich gehe eine Schleife **von Hand mit einer Wertetabelle** durch.
- ☐ Ich nutze `%` (Rest) und `/` bei ganzen Zahlen, z. B. um Ziffern abzutrennen, und weiß, was `%` bei negativen Zahlen liefert.

**Nachlesen:** 16.09. (`summeBis`, `quersumme`, `anzahlZiffern`), 29.09. (`% 2` bei negativen Zahlen). **Üben:** Schmiede L2 und L3.

**Probier dich (2):** Erstelle die Wertetabelle (Spalten `n` und `s`) für diesen Aufruf mit `n = 407` und gib das Ergebnis an.

```java
public static int quersumme(int n) {
    int s = 0;
    while (n > 0) {
        s = s + n % 10;
        n = n / 10;
    }
    return s;
}
```

## 3. Datentypen, Wertebereiche, Casts

- ☐ Ich kenne `int`, `long`, `double`, `char`, `boolean` (dazu `byte`, `short`) mit Größe und ungefährem Wertebereich.
- ☐ Ich weiß, dass `7 / 2` gleich `3` ist (Ganzzahldivision) und `7 / 2.0` gleich `3.5`.
- ☐ Ich bestimme bei einem Ausdruck **Wert und Typ**, auch mit Casts: `(int)` schneidet ab, `(double)` wandelt um.
- ☐ Ich erkläre den **Überlauf** bei `Integer.MAX_VALUE + 1`.
- ☐ Ich weiß, dass ein `char` intern eine Zahl ist: `'A' + 1` ergibt `66`.

**Nachlesen:** Blatt „Typen und Casts“ (29.09., mit Calc-Tabelle und `TypenTest`), Stundendokumentation 29.09. **Üben:** Schmiede L5.

**Probier dich (3):** Gib Wert und Typ an: `7 / 2 * 2.0`, `(double) (7 / 2)`, `(int) 3.99`, `'a' + 1`, `Integer.MAX_VALUE + 1`.

## 4. Strings

- ☐ Ich nutze `length()`, `charAt(i)`, `substring(a, b)` (b gehört nicht mehr dazu), `indexOf(...)` und Verkettung mit `+`.
- ☐ Ich wandle Text in Zahlen um: `Integer.parseInt`, `Double.parseDouble`.
- ☐ Ich erkläre, warum man Strings mit `equals` vergleicht und nicht mit `==` (Referenz gegen Inhalt).
- ☐ Ich durchlaufe einen String mit einer Schleife, z. B. für den Palindromtest.

**Nachlesen:** Stundendokumentation 30.09., Strings-Werkzeugkasten. **Üben:** Schmiede L4.

**Probier dich (4):** `String w = "Informatik";` Was liefern `w.length()`, `w.substring(2, 5)`, `w.indexOf('m')`, `"1" + 2 + 3` und `1 + 2 + "3"`?

## 5. Arrays und Standardalgorithmen

- ☐ Ich deklariere und erzeuge Arrays, kenne `length` und die Indizes von `0` bis `length - 1` und weiß, wann eine `ArrayIndexOutOfBoundsException` kommt.
- ☐ Ich implementiere **Summe, Mittelwert (als `double`), Maximum, zweitgrößtes Element, Zählen, Histogramm und lineare Suche**.
- ☐ Ich kenne die Fallen: Maximum mit `0` statt `a[0]` starten (falsch bei nur negativen Zahlen), Mittelwert mit Ganzzahldivision, Sonderfälle wie gleiche Werte oder ein leeres Array.

**Nachlesen:** 17.09., 22.09., 29.09. (Zahlenanalyse) und 01.10. (lineare Suche). **Üben:** Schmiede L3.

**Probier dich (5):** Implementiere `public static int lineareSuche(int[] a, int x)`. Sie liefert den Index des ersten Vorkommens von `x`, sonst `-1`. Gib vorher drei Testfälle an.

## 6. Codeanalyse im Abiturstil

- ☐ Ich kenne die Operatoren und halte mich daran: **angeben/nennen** (ohne Begründung), **bestimmen** (Ergebnis ermitteln, z. B. mit Wertetabelle), **beschreiben** (Zweck in eigenen Worten, nicht Zeile für Zeile), **erläutern** (mit Begründung und Beispiel), **implementieren** (Code schreiben).
- ☐ Ich bestimme die Ausgabe einer Methode für ein gegebenes Array mit einer Wertetabelle.
- ☐ Ich beschreibe, **was** eine Methode tut, nicht, wie jede Zeile funktioniert.
- ☐ Ich erläutere eine Designentscheidung, z. B. warum ein Startwert so gewählt ist.

**Nachlesen:** Stundendokumentation 01.10. (Aufgaben 1 und 2 mit Erwartungshorizont). **Üben:** Schmiede L6.

## 7. Fehler finden (kommt am Di 06.10. dazu)

- ☐ Ich unterscheide **Compilerfehler**, **Laufzeitfehler** und **logische (semantische) Fehler** und nenne je ein Beispiel.
- ☐ Ich belege einen Fehler mit einem Testfall, der ihn zeigt, und korrigiere ihn (wie `anzahlMaximum` am 01.10.).
- ☐ Ich lese ein **Struktogramm** und übersetze es in Java.
- ☐ Ich schreibe einen **Javadoc-Kommentar** mit `@param` und `@return`.
- ☐ Ich nutze den Debugger in BlueJ (Haltepunkt, Schritt für Schritt). In der Klausur zählt davon das Prinzip.

**Nicht in Klausur 1:** Klassen und Objekte, Rekursion, Vererbung und UML. Damit fangen wir nach der Klausur an.

## So übe ich

- **Schmiede:** Unit 49, Lektionen 2 bis 6 fertig machen, dann das Training. Der Code-Runner sagt dir sofort, ob dein Code die Tests besteht.
- **Von Hand:** Schreib Code erst auf Papier, dann tipp ihn in BlueJ ab und prüfe. In der Klausur gibt es keinen Compiler, der dir hilft.
- **Stundendokumentationen:** erst selbst lösen, dann den Erwartungshorizont lesen.
- **Do 08.10.:** gemischte Aufgaben im Stil der Klausur mit Besprechung.
- **Di 13.10.:** Wiederholung mit deinen offenen Fragen. Das ist die letzte Stunde vor der Klausur, am 14.10. (Wandertag) und 15.10. (Fortbildungstag) fällt der Kurs aus.
- **Fragen** sammeln und mitbringen, je früher, desto besser.

<div style="page-break-after: always;"></div>

## Lösungen der Probieraufgaben

**(1) Schaltjahr**

```java
public static boolean istSchaltjahr(int jahr) {
    return jahr % 4 == 0 && (jahr % 100 != 0 || jahr % 400 == 0);
}
```

Testfälle: `2024` → `true` (durch 4), `2023` → `false`, `1900` → `false` (durch 100, nicht durch 400), `2000` → `true` (durch 400).

**(2) Quersumme von 407**

| n | s |
|---|---|
| 407 | 0 |
| 40 | 7 |
| 4 | 7 |
| 0 | 11 |

Ergebnis: `11`.

**(3) Wert und Typ**

| Ausdruck | Wert | Typ | Warum |
|---|---|---|---|
| `7 / 2 * 2.0` | `6.0` | `double` | erst `7 / 2 = 3` (ganzzahlig), dann `3 * 2.0` |
| `(double) (7 / 2)` | `3.0` | `double` | die Klammer rechnet zuerst ganzzahlig |
| `(int) 3.99` | `3` | `int` | Cast schneidet ab, rundet nicht |
| `'a' + 1` | `98` | `int` | `'a'` hat den Code 97 |
| `Integer.MAX_VALUE + 1` | `-2147483648` | `int` | Überlauf, springt auf den kleinsten Wert |

**(4) Strings**

`w.length()` → `10`; `w.substring(2, 5)` → `"for"` (Indizes 2, 3, 4); `w.indexOf('m')` → `5`; `"1" + 2 + 3` → `"123"` (von links: ab dem String wird verkettet); `1 + 2 + "3"` → `"33"` (erst `1 + 2 = 3`, dann verketten).

**(5) Lineare Suche**

Testfälle: `{4, 7, 7}` und `7` → `1` (erstes Vorkommen); `{4, 7}` und `5` → `-1`; `{}` und `3` → `-1` (leeres Array).

```java
public static int lineareSuche(int[] a, int x) {
    for (int i = 0; i < a.length; i++) {
        if (a[i] == x) {
            return i;
        }
    }
    return -1;
}
```
