# Wiederholung für Klausur 1: fünf Stationen

**Informatik LK J1 | Dienstag, 13.10.2026 | zum Behalten | vor Klausur 1 am Di 20.10.**

**So gehst du vor:** Schau in deine Wiederholliste. Wo hast du noch kein Häkchen? Fang mit der Station an, die zu deinem schwächsten Block passt, und schaff mindestens zwei Stationen. Alles **von Hand**, ohne BlueJ, wie in der Klausur. Erst wenn du fertig bist, holst du dir die Lösung zu der Station vom Pult und korrigierst selbst mit einem anderen Stift.

| Station | Thema | Block der Wiederholliste |
|---------|--------------------------------------|------------|
| 1 | Code lesen mit Wertetabelle | 2 und 6 |
| 2 | Methode implementieren, Testfälle zuerst | 1 und 5 |
| 3 | Wert und Typ von Ausdrücken | 3 und 4 |
| 4 | Klassen und Objekte | 8 |
| 5 | Fehler finden, Javadoc | 7 |

## Station 1: Code lesen mit Wertetabelle

```java
public static int raetsel(int[] a) {
    int z = 0;
    for (int i = 1; i < a.length; i++) {
        if (a[i] > a[i - 1]) {
            z++;
        }
    }
    return z;
}
```

a) **Bestimme** `raetsel(new int[] {3, 5, 2, 8, 9})` mit einer Wertetabelle (Spalten `i`, `a[i - 1]`, `a[i]`, `z`).

| `i` | `a[i - 1]` | `a[i]` | `z` |
|-----|-----------|--------|-----|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

b) **Beschreibe**, was die Methode allgemein berechnet (ein Satz, nicht Zeile für Zeile).

c) Was liefert die Methode für ein leeres Array und für `{7}`? **Begründe** kurz.

## Station 2: Methode implementieren

Die Methode `public static double mittelwertPositiv(int[] a)` soll den Mittelwert aller **positiven** Zahlen im Array liefern. Gibt es keine positive Zahl, liefert sie `0.0`.

a) Schreib zuerst **vier Testfälle** auf (Eingabe und erwartetes Ergebnis), darunter mindestens zwei Randfälle.

b) **Implementiere** die Methode. Achte auf die Ganzzahldivision.

## Station 3: Wert und Typ

**Gib** jeweils Wert und Typ an. `String s = "Java";`

| Ausdruck | Wert | Typ |
|----------|------|-----|
| `17 / 5` | | |
| `17 % 5` | | |
| `-17 % 5` | | |
| `(double) 17 / 5` | | |
| `17 / 5 * 1.0` | | |
| `s.charAt(1) + 1` | | |
| `s.substring(1, 3)` | | |
| `"7" + 3 + 4` | | |
| `7 + 3 + "4"` | | |
| `(int) 'B'` | | |

<div style="page-break-before: always;"></div>

## Station 4: Klassen und Objekte

```java
public class Becher {

    private int inhalt;
    private int max;

    public Becher(int max) {
        this.max = max;
        this.inhalt = 0;
    }

    public void fuellen(int menge) {
        inhalt = inhalt + menge;
        if (inhalt > max) {
            inhalt = max;
        }
    }

    public int getInhalt() {
        return inhalt;
    }
}
```

a) **Bestimme** die Ausgabe. Leg dazu eine Zustandstabelle für beide Objekte an.

```java
Becher b1 = new Becher(250);
Becher b2 = new Becher(100);
b1.fuellen(200);
b2.fuellen(80);
b2.fuellen(50);
b1.fuellen(30);
System.out.println(b1.getInhalt() + " " + b2.getInhalt());
```

b) **Nenne** in der Klasse je ein Beispiel für: Attribut, Konstruktor, Parameter.

c) **Implementiere** eine Methode `ausgiessen()`, die den Becher leert und zurückgibt, wie viel drin war.

## Station 5: Fehler finden, Javadoc

Die Methode soll die Summe aller **geraden** Zahlen im Array liefern. Sie enthält drei Fehler.

```java
public static int summeGerade(int[] a) {
    int s = 0
    for (int i = 0; i <= a.length; i++) {
        if (a[i] % 2 == 1) {
            s = s + a[i];
        }
    }
    return s;
}
```

a) Finde die drei Fehler. **Gib** zu jedem die Fehlerart an (Compiler, Laufzeit, semantisch) und **belege** ihn mit der Meldung oder einem Testfall.

| Zeile | Fehler | Fehlerart | Beleg | Korrektur |
|-------|--------|-----------|-------|-----------|
| | | | | |
| | | | | |
| | | | | |

b) Schreib für die korrigierte Methode einen **Javadoc-Kommentar** mit `@param` und `@return`.

**Schnell fertig?** Nimm dir eine Station, die du noch nicht hattest, oder die Schmiede: Unit 49, Lektion 8 und 9, oder Unit 56, Lektion 2.
