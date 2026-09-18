# Stundendokumentation Donnerstag, 17.09.2026: Signatur, Testfälle, Arrays, erstes Programm

**Informatik LK, 8./9. Stunde | Einheit 1 „Java-Fundament“, Stunden 5 und 6 von 20**

## Was wir gemacht haben

1. **Rückblick auf die Diagnose:** Randfälle zuerst denken.
2. **Methodenkopf:** Rückgabetyp, Name, Parameterliste; Parameter gegen Argument; Gültigkeitsbereich.
3. **Testfälle vor dem Code** am Beispiel `istSchaltjahr`: erst die Herleitung der Regel, dann die
   Testtabelle, dann der Code in drei Anläufen.
4. **Standardalgorithmen auf Arrays:** das Muster Startwert, Schleife, Aktualisierung, dazu die drei
   klassischen Fallen.
5. **Erstes eigenes Programm in BlueJ:** Klasse `Zahlenanalyse` mit `main`.
6. **Projekt mit git versioniert:** `init`, `.gitignore`, `add`, `commit`.

## Wenn du gefehlt hast

1. Arbeite die Abschnitte „Methodenkopf“ und „Schaltjahr“ unten durch. Fülle die Testtabelle selbst
   aus, bevor du den Code liest.
2. Leg in BlueJ ein Projekt an und schreib die Zahlenanalyse nach Teil D von
   [`woche-1-aufgaben.md`](woche-1-aufgaben.md). Die Hinweiskarten in Teil E helfen, wenn es klemmt.
3. Versioniere das Projekt mit git, wie unten beschrieben.

## Erwartungshorizont

### 1. Der Methodenkopf

```
 public static   boolean    istSchaltjahr ( int jahr )
                    |             |              |
              Rückgabetyp       Name      Parameterliste
                                  \______________/
                                       Signatur
```

Die erste Zeile ist ein Vertrag: Gib mir eine ganze Zahl, ich gebe dir wahr oder falsch zurück.

- **Rückgabetyp** `boolean`: Die Methode liefert genau einen Wert dieses Typs, und zwar mit `return`.
  `void` heißt, sie liefert nichts.
- **Name:** klein beginnen, sagt, was die Methode liefert. Bei `boolean` gern `ist…` oder `hat…`.
- **Parameterliste:** Typ und Name, mehrere durch Kommas getrennt.
- `public static` vorerst als feste Formel: `public` heißt von außen aufrufbar, `static` heißt ohne
  Objekt aufrufbar. Was ein Objekt ist, kommt in Einheit 2.

**Fachlich genau, und im Quiz vom Mittwoch schon dran:** Zur **Signatur** gehören in Java nur **Name
und Parameterliste**. Der Rückgabetyp steht im Methodenkopf, gehört aber nicht zur Signatur. Deshalb
darf eine Klasse keine zwei Methoden mit gleichem Namen und gleichen Parametertypen haben, auch nicht
mit verschiedenen Rückgabetypen.

**Parameter gegen Argument**

```java
public static boolean istSchaltjahr(int jahr)   // jahr ist der Parameter
istSchaltjahr(2024)                              // 2024 ist das Argument
```

Beim Aufruf wird der Wert des Arguments in den Parameter kopiert. In der Methode ist `jahr` eine ganz
normale Variable mit dem Wert 2024.

**Gültigkeitsbereich.** Dieser Code wurde am Beamer übersetzt und scheitert mit Absicht:

```java
public static void main(String[] args) {
    System.out.println(istSchaltjahr(2024));
    System.out.println(jahr);    // Fehler beim Uebersetzen: cannot find symbol
}
```

*Erwartete Erklärung:* `jahr` existiert nur innerhalb von `istSchaltjahr`.

> **Merksatz:** Eine Variable gilt von ihrer Deklaration bis zur schließenden Klammer des Blocks, in
> dem sie steht. Ein Parameter gilt in der ganzen Methode. Das `i` aus `for (int i = 0; …)` gilt nur
> in der Schleife.

**Kontrollfrage.** „Wie sieht der Methodenkopf aus für: liefert den Mittelwert eines int-Arrays?“
*Erwartet:* `public static double mittelwert(int[] a)`. Wichtig ist das `double`: Ein Mittelwert ist
selten eine ganze Zahl.

### 2. Woher die Schaltjahrregel kommt

Ein Sonnenjahr, von Frühlingsanfang zu Frühlingsanfang, dauert im Mittel etwa **365,2422 Tage**, also
365 Tage und knapp 6 Stunden. Ein Kalender kann aber nur ganze Tage zählen.

| Kalender | mittleres Kalenderjahr | Fehler gegen das Sonnenjahr | Regelzeile |
|---|---|---|---|
| nur 365 Tage | 365 | 0,2422 Tage zu kurz, nach 4 Jahren fast ein ganzer Tag | |
| Julius Caesar: jedes 4. Jahr ein Schalttag | 365 + 1/4 = 365,25 | gut 11 Minuten zu lang, in 400 Jahren gut 3 Tage | durch 4 teilbar |
| Papst Gregor XIII., 1582: in 400 Jahren 3 Schalttage streichen | 365 + 1/4 − 1/100 + 1/400 = 365,2425 | knapp eine halbe Minute zu lang, ein Tag erst in gut 3.000 Jahren | außer durch 100, außer durch 400 |

**Woher die 3 und die 97 kommen:** In 400 Jahren gibt es 100 durch 4 teilbare Jahre. Vier davon sind
Jahrhundertjahre, und nur eines davon ist auch durch 400 teilbar. Gestrichen werden also drei:
100 − 3 = **97 Schalttage in 400 Jahren**, und 97/400 = 0,2425. Konkret: 1700, 1800 und 1900 waren
keine Schaltjahre, 2000 war eins.

*Nebenbei:* Bei der Umstellung 1582 folgte auf Donnerstag, den 4. Oktober, direkt Freitag, der
15. Oktober. Die zehn aufgelaufenen Tage wurden übersprungen.

Daraus die Regel:

```
Schaltjahr, wenn durch 4 teilbar,
  außer wenn durch 100 teilbar,
    außer wenn durch 400 teilbar.
```

`jahr % 4 == 0` heißt „durch 4 teilbar“, denn `%` liefert den Rest der ganzzahligen Division.

### 3. Testfälle vor dem Code

Die Spalte „erwartet“ füllt man **aus der Regel**, nicht aus einem Programm. Das ist der ganze Trick.

| Eingabe | erwartet | welche Zeile der Regel |
|---|---|---|
| 2024 | true | durch 4 |
| 2023 | false | nicht durch 4 |
| 1900 | false | durch 100, nicht durch 400 |
| 2000 | true | durch 400 |
| 2100 | false | durch 100, nicht durch 400 |

*Erwartete Einsicht:* Jede Zeile der Regel wird von mindestens einem Test getroffen. Das ist die Idee
von Testfällen: jeder Fall der Regel, und die Grenzfälle zuerst.

Dann der Code, in drei Anläufen, so wie er in der Stunde entstanden ist:

**Version 1**, fast immer der erste Vorschlag:

```java
return jahr % 4 == 0;
```

2024, 2023 und 2000 richtig, **1900 und 2100 falsch** (beide liefern `true`). Der Code sieht richtig
aus, der Test sagt nein. Der Test hat recht.

**Version 2**, die typische Reparatur:

```java
return jahr % 4 == 0 && jahr % 100 != 0;
```

1900 und 2100 jetzt richtig, dafür **2000 falsch**. *Lehre:* Nach jeder Änderung laufen **alle**
Tests, nicht nur der, den man reparieren wollte.

**Version 3**, richtig:

```java
return (jahr % 4 == 0 && jahr % 100 != 0) || jahr % 400 == 0;
```

Alle fünf Tests grün. `&&` bindet stärker als `||`, die Klammern wären also nicht nötig, sie machen
den Ausdruck aber lesbar.

**Die Variante mit Verzweigungen**, gleichwertig und für viele besser lesbar:

```java
public static boolean istSchaltjahr(int jahr) {
    if (jahr % 400 == 0) {
        return true;
    }
    if (jahr % 100 == 0) {
        return false;
    }
    return jahr % 4 == 0;
}
```

*Frage aus der Stunde:* „Was passiert, wenn wir zuerst `% 4` prüfen und dort `return true` schreiben?“
*Erwartet:* 1900 landet sofort bei `true`. Deshalb **vom Speziellen zum Allgemeinen** prüfen.

*Und nebenbei:* Ein Vergleich ist schon ein `boolean`. Statt
`if (jahr % 4 == 0) { return true; } else { return false; }` genügt `return jahr % 4 == 0;`.

### 4. Arrays: das Muster

```java
int[] a = {3, 9, 2, 7};    // vier Elemente
a[0]                       // 3: der erste Index ist 0
a.length                   // 4: die Laenge, ohne Klammern
a[a.length - 1]            // 7: das letzte Element
int[] b = new int[5];      // fuenf Plaetze, alle mit 0 belegt
```

Das Muster **Startwert, Schleife, Aktualisierung**, am Beamer an der Summe gezeigt:

```java
public static int summe(int[] a) {
    int s = 0;                              // Startwert
    for (int i = 0; i < a.length; i++) {    // Schleife ueber alle Indizes
        s = s + a[i];                       // Aktualisierung
    }
    return s;
}
```

Für `{3, 9, 2, 7}` liefert das 21. Maximum, Anzahl und Mittelwert sind dasselbe Muster, nur Startwert
und Aktualisierung ändern sich. Genau deshalb programmiert ihr die selbst.

**Die drei Fallen**, an der Tafel bewusst als Fragen:

| Falle | Frage | Was du wissen musst |
|---|---|---|
| Startwert 0 beim Maximum | „Geht `int max = 0;` immer gut?“ | Nein. Den Startwert aus dem Array nehmen: `int max = a[0];`. **Bei welchem Array die 0 danebengeht, ist Frage 3 in Teil C.** Die klären wir am Dienstag gemeinsam, die Antwort steht hier bewusst nicht. |
| Ganzzahldivision beim Mittelwert | „Was ergibt `21 / 4`?“ | `5`, nicht `5.25`. Bei zwei `int` rechnet Java ganzzahlig. Richtig ist `(double) summe / a.length`. Falsch ist `(double) (summe / a.length)`: Da kommt der Cast zu spät, das Ergebnis ist 5.0. |
| `a.length` gegen `a.length - 1` | „Welcher Index ist der letzte?“ | `a.length - 1`. Deshalb `i < a.length`, nicht `i <= a.length`. Sonst: `ArrayIndexOutOfBoundsException`. |

**Zweitgrößtes Element** (nur gezeigt, von Hand rechnen wir am Dienstag), Array `3, 9, 2, 7`:

| Schritt | x | max | zweit | Regel |
|---|---|---|---|---|
| Start | | MIN | MIN | beide mit `Integer.MIN_VALUE` |
| 1 | 3 | 3 | MIN | x > max: altes max nach zweit, x nach max |
| 2 | 9 | 9 | 3 | x > max |
| 3 | 2 | 9 | 3 | x weder > max noch > zweit |
| 4 | 7 | 9 | 7 | x > zweit und x ≠ max |

Standardalgorithmen auf Arrays sind Pflichtteil im Abitur. 2026 kam ein Histogramm dran, das ist die
Erweiterung für Schnelle in Teil D.

### 5. Das Projekt mit git sichern

Im Projektordner die Kommandozeile öffnen (im Explorer in die Adresszeile `cmd` tippen):

```
git init
git config user.name "..."
git config user.email "..."
git add .
git commit -m "Erste Fassung"
```

Dazu eine Datei `.gitignore` im Projektordner mit den beiden Zeilen `*.class` und `*.ctxt`.
Versioniert wird der Quelltext, nicht das Übersetzungsergebnis. Alles bleibt lokal im Projektordner,
nichts geht zu GitHub. Wer fertig war: eine Zeile ändern, `git diff`, zweiter Commit.

## Noch nicht hier: die Zahlenanalyse

Die Musterlösung zum Programm „Zahlenanalyse“ (Teil D) und die Lösungen zum Kopfrechnen (Teil C)
stehen **noch nicht** in dieser Datei. Beides machen wir am **Dienstag, 22.09., gemeinsam im
Unterricht**; danach werden die Lösungen hier nachgetragen.

Wer selbst weiterprobieren will: Die **Hinweiskarten in Teil E** von
[`woche-1-aufgaben.md`](woche-1-aufgaben.md) helfen, wenn es klemmt. Und prüf deine Methoden mit
eigenen Arrays, nicht nur mit dem Starter-Array: Zwei typische Fehler fallen ausgerechnet beim
Starter-Array nicht auf.

## Was am Dienstag drankommt

Kopfrechnen mit Arrays und `zweitgroesstes` von Hand (Teil C), die Zahlenanalyse in BlueJ zu Ende
gebracht (Teil D), dazu Datentypen, Wertebereiche und Casts.
