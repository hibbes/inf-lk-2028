# Stundendokumentation Donnerstag, 08.10.2026: Fehlerarten, Debugger, Struktogramm, Javadoc

**Informatik LK, 8./9. Stunde | Einheit 1 „Java-Fundament“, Stunden 17 und 18 von 20, Abschluss der Einheit**

## Was wir gemacht haben

1. **Einstieg:** die offene Frage vom 01.10.: Welche der drei Fehler in `anzahlMaximum` hätte der
   Compiler gefunden? Antwort: keinen. Am Beamer drei Programme gestartet: eines übersetzt nicht,
   eines bricht ab, eines läuft und gibt `3.0` aus. Daraus die Tabelle „Drei Arten von Fehlern“
   oben auf dem Blatt.
2. **Aufgabe 1 allein und ohne Rechner:** neun Codezeilen (A bis I) einer Fehlerart zugeordnet und
   belegt, dazu die drei Fehler in `anzahlMaximum` eingeordnet. Die strittigen Fälle B und H am
   Beamer entschieden.
3. **Debugger am Beamer:** `anzahlMaximum({2, 5, 5})` in BlueJ mit Haltepunkt, Schritt für Schritt,
   Variablen beobachten, bei `i = 1` anhalten. Begriffe Haltepunkt, Schritt, Schritt hinein,
   Fortsetzen.
4. **Aufgabe 2 zu zweit mit dem Debugger** an `istSortiert`, `quersumme` und `anzahlVokale`: zuerst
   das tatsächliche Ergebnis ermitteln, dann mit Haltepunkt die Ursache suchen, korrigieren und
   einen eigenen Randfall testen.
5. **Aufgabe 3:** die Bausteine eines Struktogramms an der Tafel (Anweisung, Verzweigung,
   Schleife), dann allein: Struktogramm in Java übersetzen, Wertetabelle zu `ggT`, danach in BlueJ
   geprüft.
6. **Aufgabe 4:** Javadoc am Beispiel `istSortiert`, Umschalten auf „Dokumentation“ im
   BlueJ-Editor, dann Javadoc für `anzahlGroesser` und `ggT`.
7. **Schmiede:** Unit 49 „E1 Java-Fundament“, Lektion 6 „Codeanalyse und Fehlerarten“, wer fertig
   war, Lektion 7 „Struktogramm und Javadoc“.
8. **Sicherung:** Block 7 der Wiederholliste gemeinsam abgehakt. Ins Heft: „Compilerfehler: startet
   nicht. Laufzeitfehler: bricht ab. Semantischer Fehler: läuft, aber falsch, nur ein Testfall
   zeigt ihn.“

## Wenn du gefehlt hast

1. Hol dir das Blatt **„Fehler finden, Debugger, Struktogramm, Javadoc“** und `Debugtraining.java`
   aus dem Gruppenordner KW41.
2. Bearbeite **Aufgabe 1** ohne Rechner. Schreib zu jeder Zeile einen Beleg dazu, nicht nur die
   Fehlerart.
3. Öffne `Debugtraining.java` in BlueJ und bearbeite **Aufgabe 2** mit dem Debugger (Anleitung auf
   dem Blatt). Trag „tatsächlich“ erst ein, wenn du die Methode aufgerufen hast. Auch wenn du den
   Fehler schon beim Lesen siehst: Zeig ihn dir im Debugger.
4. Bearbeite **Aufgabe 3** erst auf Papier (Ergebnis vorher bestimmen, Wertetabelle), dann in
   BlueJ, und danach **Aufgabe 4**.
5. Erst dann den Erwartungshorizont lesen. Danach in der Schmiede Unit 49, Lektion 6 und 7, und
   Block 7 der [Wiederholliste](klausur-1-wiederholliste.md) abhaken.

## Erwartungshorizont

Alle Meldungen und Ergebnisse stammen aus Läufen mit `javac` 25; jede Zeile aus Aufgabe 1 wurde
dafür als eigenes kleines Programm übersetzt und gestartet.

### 0. Drei Arten von Fehlern (Tabelle oben auf dem Blatt)

| Fehlerart | Wann merkst du ihn? | Wie belegst du ihn? |
|------------------|------------------------------|-----------------------------|
| Compilerfehler (syntaktisch) | beim Übersetzen; das Programm startet gar nicht | mit der Meldung des Compilers und der Zeile |
| Laufzeitfehler | beim Ausführen; das Programm bricht mit einer Exception ab | mit einem Testfall, der den Abbruch auslöst, und dem Namen der Exception |
| semantischer (logischer) Fehler | gar nicht von selbst; das Programm läuft, liefert aber Falsches | mit einem Testfall: erwartet gegen tatsächlich |

Der Compiler prüft, ob der Code die Regeln von Java einhält. Ob das Programm das Richtige tut, prüft
er nicht.

### 1. Aufgabe 1: Welche Art von Fehler?

BlueJ zeigt die Meldungen je nach Spracheinstellung auf Deutsch oder Englisch.

| Nr. | Fehlerart | Beleg |
|----|-------------|----------------------------------------------------------------|
| A | Compiler | „Inkompatible Typen: Möglicher Verlust bei Konvertierung von double in int“ (`possible lossy conversion from double to int`). Ein `double` passt ohne Cast nicht in ein `int`. |
| B | Compiler | „Rückgabeanweisung fehlt“ (`missing return statement`). Für `x <= 0` gibt es kein `return`. Das sieht nach Logik aus, prüft aber der Compiler. |
| C | Compiler | „Symbol nicht gefunden“ (`cannot find symbol`). Bei Strings ist `length()` eine Methode mit Klammern, bei Arrays ist `a.length` ein Attribut. |
| D | Laufzeit | `ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5`. Gültig sind die Indizes 0 bis 4. |
| E | Laufzeit | `NumberFormatException: For input string: "12a"` |
| F | semantisch | erwartet 3.5, ausgegeben `3.0`. `summe / anzahl` ist eine Ganzzahldivision (Ergebnis 3), erst danach wird in `double` umgewandelt (29.09.). Richtig: `(double) summe / anzahl` |
| G | semantisch | Eingabe „ja“, erwartet „weiter“, das Programm bricht ab. `==` vergleicht bei Strings die Referenzen (30.09.). Richtig: `e.equals("ja")` |
| H | semantisch | Endlosschleife: `i` wird nie erhöht, das Programm endet nie und gibt nichts aus. Im Debugger bleibt `i` bei 0. Richtig: `i++` in der Schleife |
| I | Laufzeit | `ArithmeticException: / by zero`, weil `x - 10` gleich 0 ist |

**Zu B:** Viele ordnen B als semantisch ein. Der Compiler verlangt aber, dass eine Methode mit
Rückgabetyp auf jedem Weg einen Wert zurückgibt. Deshalb startet das Programm gar nicht.

**Zu H:** Wer „Laufzeitfehler“ sagt, weil man ihn beim Laufen bemerkt: Es gibt keinen Abbruch und
keine Exception, das Programm läuft und tut etwas anderes als gemeint. Darum zählt die
Endlosschleife als semantischer Fehler (so auch in der Schmiede, Lektion 6). In BlueJ beendet man
sie mit „Virtuelle Maschine zurücksetzen“ (Rechtsklick auf die Laufanzeige unten links).

**`anzahlMaximum` vom 01.10.:** Fehler 1 (`i <= a.length`) ist ein Laufzeitfehler, er löst eine
`ArrayIndexOutOfBoundsException` aus. Fehler 2 (`max = 0` als Startwert) und Fehler 3 (`anzahl`
wird bei einem neuen Maximum nicht zurückgesetzt) sind semantisch. Der Compiler findet keinen der
drei.

### 2. Vorführung: `anzahlMaximum({2, 5, 5})` im Debugger

In `Debugtraining.java` sind Fehler 1 und 2 behoben, Fehler 3 steckt noch drin. Erwartet ist 2 (die
5 kommt zweimal vor), die Methode liefert 3. Haltepunkt auf die Zeile `if (a[i] > max)`, dann
Schritt für Schritt:

| `i` | `a[i]` | `max` danach | `anzahl` danach |
|---|---|---|---|
| 0 | 2 | 2 | 1 |
| 1 | 5 | 5 | 2 |
| 2 | 5 | 5 | 3 |

Bei `i = 1` sieht man es: `max` springt auf 5, aber `anzahl` zählt die alte 2 weiter mit.
Korrektur: Wenn ein neues Maximum gefunden wird, `anzahl` auf 0 zurücksetzen.

```java
if (a[i] > max) {
    max = a[i];
    anzahl = 0;
}
if (a[i] == max) {
    anzahl++;
}
```

### 3. Aufgabe 2: der Debugger in BlueJ

**a)**

| Methode | Testfall | erwartet | tatsächlich | was der Debugger zeigt | Korrektur |
|--------------|----------|--------|-----------|------------------------|------------------|
| `istSortiert` | `{1, 2, 0}` | `false` | `true` | Die Schleife läuft nur einmal, mit `i = 1`: 2 ist nicht kleiner als 1, also `else` und sofort `return true`. Das Paar 2 und 0 wird nie geprüft. | `else`-Zweig streichen; `return true` steht erst nach der Schleife |
| `quersumme` | `407` | `11` | `7` | `n` wird 407, 40, 4. Bei `n = 4` ist `n > 9` falsch, die Schleife endet, und die 4 wird nie addiert. | `while (n > 0)` |
| `anzahlVokale` | `"banane"` | `3` | `1` | Bei `c = 'a'` wird `z` nicht erhöht: `"aeiou".indexOf('a')` ist `0`, und `0 > 0` ist falsch. Nur das `e` (Index 1) wird gezählt. | `indexOf(c) >= 0` |

Alle drei sind semantische Fehler: Die Methoden laufen ohne Meldung und liefern das Falsche.

**b)** Die korrigierten Methoden:

```java
public static boolean istSortiert(int[] a) {
    for (int i = 1; i < a.length; i++) {
        if (a[i] < a[i - 1]) {
            return false;
        }
    }
    return true;
}

public static int quersumme(int n) {
    int s = 0;
    while (n > 0) {
        s = s + n % 10;
        n = n / 10;
    }
    return s;
}

public static int anzahlVokale(String text) {
    int z = 0;
    for (int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);
        if ("aeiou".indexOf(c) >= 0) {
            z++;
        }
    }
    return z;
}
```

Geprüft: `istSortiert` liefert `false` für `{1, 2, 0}` und `true` für `{1, 2, 2, 7}` und das leere
Array `{}`. `quersumme` liefert 11, 5 und 0 für 407, 5 und 0. `anzahlVokale` liefert 3 für
`"banane"`. Gute Randfälle sind das leere Array, die Zahl 0, eine einstellige Zahl und ein Text ohne
Vokale.

**c)** Jede **einstellige Zahl**, zum Beispiel `quersumme(5)`: Mit dem Fehler kommt 0 statt 5
heraus, weil die Schleife gar nicht läuft.

**Für Genaue:** `anzahlVokale("Ei")` liefert auch nach der Korrektur 1, weil das große `E` nicht in
`"aeiou"` steht. Ob das ein Fehler ist, entscheidet die Aufgabenstellung. Wer Großbuchstaben
mitzählen will, prüft `text.toLowerCase()`.

### 4. Aufgabe 3: Struktogramme lesen

**a)** Für `{3, 8, 5, 10, 5}` und die Grenze 5 muss **2** herauskommen (8 und 10). Die beiden 5
zählen nicht, weil im Struktogramm `>` steht. Ein leeres Array liefert 0.

```java
public static int anzahlGroesser(int[] a, int grenze) {
    int anzahl = 0;
    for (int i = 0; i < a.length; i++) {
        if (a[i] > grenze) {
            anzahl++;
        }
    }
    return anzahl;
}
```

- „für i von 0 bis a.length - 1“ meint **einschließlich** a.length - 1. In Java also
  `i < a.length` oder `i <= a.length - 1`.
- **Typischer Fehler:** `i <= a.length`. Dann greift der letzte Durchlauf auf `a[a.length]` zu,
  und es gibt eine `ArrayIndexOutOfBoundsException`.
- Der leere Nein-Zweig (`∅`) wird in Java einfach weggelassen, es braucht kein `else`.

**b)** `ggT(84, 36)`:

| Durchlauf | `r` | `a` | `b` |
|---|---|---|---|
| Start | | 84 | 36 |
| 1 | 12 | 36 | 12 |
| 2 | 0 | 12 | 0 |

Jetzt ist `b` gleich 0, die Schleife endet, Rückgabe **12**.

**c)** `ggT(36, 84)` = **12**, mit drei Durchläufen. Im ersten Durchlauf ist `36 mod 84 = 36`,
danach ist `a = 84` und `b = 36`. Die beiden Zahlen werden also nur vertauscht, und es geht weiter
wie in b). Es kostet einen zusätzlichen Durchlauf.

**d)**

```java
public static int ggT(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}
```

- `mod` aus dem Struktogramm ist in Java der Operator `%`, `←` ist die Zuweisung `=`, und
  „solange b ≠ 0“ wird `while (b != 0)`.
- Geprüft: `ggT(84, 36)` und `ggT(36, 84)` liefern beide 12.
- **Typischer Fehler:** die Reihenfolge der Zuweisungen vertauscht (`b = r;` vor `a = b;`). Dann
  bekommt `a` schon den neuen Wert von `b`, und das Ergebnis stimmt nicht mehr.

### 5. Aufgabe 4: Javadoc

**a)** Zum Beispiel:

```java
/**
 * Zählt, wie viele Elemente eines Arrays größer als eine Grenze sind.
 *
 * @param a      das Array, das durchsucht wird
 * @param grenze die Vergleichszahl; Elemente, die gleich der Grenze sind, zählen nicht
 * @return die Anzahl der Elemente, die echt größer als grenze sind
 */
public static int anzahlGroesser(int[] a, int grenze) {

/**
 * Berechnet den größten gemeinsamen Teiler zweier Zahlen nach Euklid.
 *
 * @param a die erste Zahl, a > 0
 * @param b die zweite Zahl, b >= 0
 * @return der größte gemeinsame Teiler von a und b
 */
public static int ggT(int a, int b) {
```

Darauf kommt es an (so wird es auch in der Klausur bewertet):

- Der erste Satz sagt, **wozu** die Methode da ist. Wie sie das im Einzelnen macht (Schleife,
  Zähler), gehört nicht hinein.
- Für **jeden** Parameter eine Zeile `@param` mit dem Namen des Parameters und seiner Bedeutung.
- Eine Zeile `@return`, die sagt, **was** der Wert bedeutet. „Gibt a zurück“ beschreibt nur den
  Code und bringt keinen Punkt.
- **Einschränkungen** stehen beim Parameter, zum Beispiel `b >= 0` beim `ggT`.

**b)** In der Ansicht „Dokumentation“ sieht man nur noch Kommentar und Methodenkopf, keinen Rumpf.
Der Kommentar reicht, wenn man damit die Methode richtig aufrufen kann, ohne den Code zu lesen.

### Merksatz (Heft)

> **Compilerfehler: Das Programm startet nicht. Laufzeitfehler: Es bricht ab. Semantischer Fehler:
> Es läuft, aber falsch; nur ein Testfall zeigt ihn. Mit dem Debugger halte ich das Programm an
> einem Haltepunkt an, gehe Schritt für Schritt weiter und beobachte die Variablen.**

### Zum Selbstprüfen

Erst selbst antworten, dann die erwartete Antwort lesen.

1. **Woran erkennst du einen Laufzeitfehler, woran einen semantischen Fehler?**\
   *Erwartet:* Beim Laufzeitfehler bricht das Programm mit einer Exception ab. Beim semantischen
   Fehler läuft es durch und liefert ein falsches Ergebnis; das zeigt nur ein Testfall mit
   erwartetem und tatsächlichem Ergebnis.
2. **Warum ist `static boolean istPositiv(int x) { if (x > 0) { return true; } }` ein
   Compilerfehler?**\
   *Erwartet:* Für `x <= 0` gibt es kein `return`. Der Compiler verlangt, dass eine Methode mit
   Rückgabetyp auf jedem Weg einen Wert zurückgibt („Rückgabeanweisung fehlt“).
3. **Welchen Testfall wählst du, um den Fehler in `while (n > 9)` bei der Quersumme am
   deutlichsten zu zeigen?**\
   *Erwartet:* eine einstellige Zahl, zum Beispiel 5: erwartet 5, tatsächlich 0.
4. **Was bedeutet „für i von 0 bis a.length - 1“ in Java?**\
   *Erwartet:* `for (int i = 0; i < a.length; i++)`. Das „bis“ ist einschließlich gemeint.
5. **Welche Werte haben `a` und `b` nach dem ersten Durchlauf von `ggT(36, 84)`?**\
   *Erwartet:* `a = 84`, `b = 36`. Die Zahlen sind vertauscht, danach geht es weiter wie bei
   `ggT(84, 36)`.
6. **Was gehört in einen Javadoc-Kommentar über einer Methode mit zwei Parametern und
   Rückgabewert?**\
   *Erwartet:* ein Satz zum Zweck der Methode, zwei Zeilen `@param` (je Parameter, mit
   Einschränkungen), eine Zeile `@return` mit der Bedeutung des Rückgabewerts.
7. **Wozu brauchst du den Debugger, wenn du doch einen Testfall hast?**\
   *Erwartet:* Der Testfall zeigt, **dass** etwas falsch ist. Der Debugger zeigt, **wo**: an
   welcher Zeile und bei welchem Variablenwert das Programm anders läuft als gedacht.

## Was als Nächstes drankommt

Dienstag, 13.10.: Wiederholungsstunde für Klausur 1, mit euren Fragen und Aufgaben im Klausurstil.
Am 14.10. (Wandertag) und 15.10. (Fortbildungstag) fällt der Kurs aus. **Bringt eure offenen Fragen
mit.**

**Klausur 1 am Dienstag, 20.10.** prüft E1 komplett und den Einstieg in Klassen und Objekte vom
06.10. (Block 8 der [Wiederholliste](klausur-1-wiederholliste.md)). Aus dieser Stunde
klausurtauglich: Fehlerart bestimmen und mit Testfall oder Meldung belegen (Aufgabe 1 und 2),
Struktogramm in Java übersetzen und mit Wertetabelle durchrechnen (Aufgabe 3), Javadoc schreiben
(Aufgabe 4). Vom Debugger zählt das Prinzip: Haltepunkt, Schritt für Schritt, Variablen beobachten,
und wozu man das braucht. Die Klausur schreibt ihr von Hand, ohne BlueJ.

Donnerstag, 22.10.: weiter in E2 mit Klassen, die ihr selbst schreibt, Kapselung und Referenzen.
Javadoc wird ab dann für jede eigene Klasse verlangt.
