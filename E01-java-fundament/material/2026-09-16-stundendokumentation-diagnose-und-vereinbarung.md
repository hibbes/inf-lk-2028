# Stundendokumentation Mittwoch, 16.09.2026: Vereinbarung, Diagnose, Operator „beschreiben“

**Informatik LK, 1./2. Stunde | Einheit 1 „Java-Fundament“, Stunden 3 und 4 von 20**

## Was wir gemacht haben

1. **KI-Vereinbarung beschlossen.** Die Sätze aus der Hausaufgabe sind in den Entwurf vom Dienstag
   eingearbeitet, der Kurs hat die Fassung beschlossen. Sie steht in
   [`ki-und-wir.md`](ki-und-wir.md) und gilt ab sofort.
2. **Diagnose** in der Schmiede, Lektion 1 „Einstieg: Woher kommst du?“: sechs Coding-Aufgaben und
   das Quiz, Einzelarbeit, ohne Hilfe und ohne KI. Nichts davon zählt als Note.
3. **Auswertung** am Beamer: zwei Lösungswege zu `summeBis` und `quersumme`, der Sonderfall 0 bei
   `anzahlZiffern`.
4. **Operator „beschreiben“** eingeführt.
5. **Partnerübung** „Fahrer und Navigator“ mit Wechsel nach zehn Minuten: Lektion 2 „Methoden und
   Bedingungen“.

## Wenn du gefehlt hast

Mach die Aufgaben zuerst selbst in der Schmiede, **bevor** du den Erwartungshorizont unten liest.
Die Diagnose ist keine Note, sie zeigt nur, wo du stehst, und dafür nützt sie nur ungelöst etwas.

1. Schmiede, Unit „E1 Java-Fundament“, Lektion 1 komplett samt Quiz.
2. Danach Lektion 2 „Methoden und Bedingungen“.
3. Lies die beschlossene KI-Vereinbarung in [`ki-und-wir.md`](ki-und-wir.md).

## Erwartungshorizont Lektion 1 (Diagnose)

Die Lösungen unten sind je eine saubere Fassung, nicht die einzig richtige. Entscheidend ist, dass
alle Testfälle grün sind und du erklären kannst, warum.

**`verdoppeln(int n)`**

```java
public static int verdoppeln(int n) {
    return 2 * n;
}
```

**`groesser(int a, int b)`**

```java
public static int groesser(int a, int b) {
    if (b > a) {
        return b;
    }
    return a;
}
```

`Math.max(a, b)` ist genauso richtig. Beachte: Nach einem `return` braucht es kein `else`, die
Methode ist an dieser Stelle schon verlassen.

**`istTeilbar(int n, int t)`**

```java
public static boolean istTeilbar(int n, int t) {
    return n % t == 0;
}
```

Ein Vergleich ist bereits ein `boolean`. Wer `if (n % t == 0) { return true; } else { return false; }`
geschrieben hat, hat nichts falsch gemacht, aber vier Zeilen zu viel.

**`summeBis(int n)`**

```java
public static int summeBis(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}
```

Die Formel von Gauß, `n * (n + 1) / 2`, ist ebenfalls richtig und war einer der beiden Wege am
Beamer. Der Startwert 0 erledigt den Fall n kleiner als 1 von selbst: Die Schleife läuft dann keinmal.

**`quersumme(int n)`**

```java
public static int quersumme(int n) {
    int s = 0;
    while (n > 0) {
        s += n % 10;
        n = n / 10;
    }
    return s;
}
```

`n % 10` trennt die letzte Ziffer ab, `n / 10` schneidet sie weg (Ganzzahldivision). Für n gleich 0
läuft die Schleife keinmal, das Ergebnis 0 stimmt.

**`anzahlZiffern(int n)`**

```java
public static int anzahlZiffern(int n) {
    if (n == 0) {
        return 1;
    }
    int z = 0;
    while (n > 0) {
        z++;
        n = n / 10;
    }
    return z;
}
```

**Das war die Stelle, an der es hakte.** Dieselbe Schleife wie bei der Quersumme, aber ohne den
Sonderfall liefert `anzahlZiffern(0)` den Wert 0, und 0 hat nun einmal eine Ziffer. Daraus die Lehre,
die am Donnerstag die ganze Stunde getragen hat: **Randfälle zuerst denken, nicht zuletzt.**

**Quiz**

| Frage | richtige Antwort | warum |
|---|---|---|
| Was gehört zur Signatur von `public static int summeBis(int n)`? | Name und Parameterliste (Anzahl und Typen der Parameter) | Der Rückgabetyp steht im Methodenkopf, gehört in Java aber nicht zur Signatur. Deshalb darf es keine zweite Methode `summeBis(int)` mit anderem Rückgabetyp geben. |
| Was passiert, wenn in einer Methode mit Rückgabetyp `int` ein Zweig kein `return` enthält? | Der Compiler lehnt die Methode ab („missing return statement“) | Java verlangt, dass jeder mögliche Weg durch die Methode einen Wert zurückgibt. |

## Erwartungshorizont Operator „beschreiben“

Der wichtigste Satz der Stunde:

> **Beschreiben** heißt: sagen, **was** etwas tut. **Erläutern** heißt: sagen, **was und warum**.

Beschrieben wird in ganzen Sätzen und auf der Ebene des Zwecks, nicht Zeile für Zeile.

**Aufgabe:** „Beschreibe, was `quersumme` tut.“

*Erwartet:*

> Die Methode bekommt eine nicht negative ganze Zahl und liefert die Summe ihrer Ziffern. Dazu trennt
> sie in einer Schleife wiederholt die letzte Ziffer ab und addiert sie, bis von der Zahl nichts mehr
> übrig ist.

*Nicht erwartet (das ist kein Beschreiben, das ist Vorlesen):*

> Zuerst wird s gleich 0 gesetzt. Dann kommt eine while-Schleife mit der Bedingung n größer 0. Darin
> steht s plus gleich n modulo 10. Dann n gleich n durch 10.

## Erwartungshorizont Lektion 2 (Partnerübung)

**`betrag(int x)`**, ohne `Math.abs`

```java
public static int betrag(int x) {
    if (x < 0) {
        return -x;
    }
    return x;
}
```

Der Testfall `betrag(-2147483647)` ist mit Absicht so gewählt. Bei `Integer.MIN_VALUE`, also
-2147483648, gäbe es kein passendes positives Gegenstück im Typ `int`, und `-x` liefert die Zahl
unverändert zurück. Darüber reden wir in Lektion 5 („Typen, Wertebereiche und Casts“).

**`maxVonDrei(int a, int b, int c)`**

```java
public static int maxVonDrei(int a, int b, int c) {
    int m = a;
    if (b > m) {
        m = b;
    }
    if (c > m) {
        m = c;
    }
    return m;
}
```

Das ist bereits das Muster „Startwert, dann Schritt für Schritt aktualisieren“, das am Donnerstag für
Arrays wiederkam. Der Startwert kommt aus den Daten (hier `a`), nicht aus dem Nichts.

**`vorzeichen(int x)`**

```java
public static int vorzeichen(int x) {
    if (x < 0) {
        return -1;
    } else if (x == 0) {
        return 0;
    } else {
        return 1;
    }
}
```

**`zwischen(int x, int a, int b)`**, Grenzen eingeschlossen

```java
public static boolean zwischen(int x, int a, int b) {
    return x >= a && x <= b;
}
```

„Grenzen eingeschlossen“ heißt `>=` und `<=`, nicht `>` und `<`. Genau dafür stehen die Testfälle
`zwischen(1, 1, 10)` und `zwischen(10, 1, 10)` in der Aufgabe.

**Merke aus der Lektion:** Bei mehreren Fällen zuerst den strengsten prüfen. Wer `if (x > 0)` vor
`if (x > 10)` schreibt, erreicht den zweiten Fall nie.

**`istSchaltjahr` und `notenpunkte`** stehen hier bewusst noch nicht. `istSchaltjahr` haben wir am
Donnerstag gemeinsam entwickelt, die Lösung steht in der Stundendokumentation vom 17.09.
`notenpunkte` ist noch offen und wird im Unterricht besprochen.

## Hausaufgabe aus dieser Stunde

Bis Donnerstag, 17.09.: Lektion 2 fertig, `istSchaltjahr` und `notenpunkte` durften offen bleiben.
