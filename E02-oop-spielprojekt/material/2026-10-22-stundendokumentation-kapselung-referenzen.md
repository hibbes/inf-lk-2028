# Stundendokumentation Donnerstag, 22.10.2026: Kapselung, Referenzen, `null` und `static`

**Informatik LK, 8./9. Stunde | Einheit 2 „Objektorientierung und Spielprojekt“, letzte Stunde vor den Herbstferien**

## Was wir gemacht haben

1. **Blitzlicht:** Reihum ein Satz zur Klausur vom Dienstag.
2. **Einstieg:** `k.kontostand = -1000;` und `k.einzahlen(-500);` nebeneinander. Das Erste verhindert
   der Compiler, das Zweite läuft durch. Wer schützt die Regel „Der Kontostand ist nie negativ“?
3. **Aufgabe 1 zu zweit in BlueJ:** die Regel im Code Pad gebrochen, die Tabelle **vor** dem Code
   ausgefüllt, `Konto` repariert und mit der Tabelle geprüft. Besprochen: Warum gibt es kein
   `setKontostand`?
4. **Aufgabe 2:** Ausgabe und Speicherbild erst auf Papier, dann `Referenzen` gestartet. An der Tafel
   entstand das Speicherbild mit den Variablen `x`, `y`, `a`, `b`, `c`.
5. **Aufgabe 3:** ein Array mit leeren Plätzen, die `NullPointerException` gelesen, die Schleife
   repariert.
6. **Aufgabe 4 gemeinsam:** `static` am Kontozähler, vorhergesagt und am Beamer gestartet.
7. **Schmiede:** offene Lektionen aus Unit 56, Unit 48 und Unit 49.
8. **Sicherung ins Heft:** der Merke-Kasten vom Blatt.

## Wenn du gefehlt hast

1. Hol dir das Blatt **„Objekte genauer: Kapselung, Referenzen, `null` und `static`“** und den Ordner
   `konto2` aus dem Gruppenordner KW43. Kopier den Ordner in deinen eigenen Ordner und öffne ihn in
   BlueJ.
2. Bearbeite **Aufgabe 1**. Füll die Tabelle in 1d aus, **bevor** du `Konto` reparierst.
3. Bearbeite **Aufgabe 2** zuerst auf Papier und zeichne das Speicherbild. Starte erst dann
   `Referenzen`.
4. Bearbeite **Aufgabe 3** und **Aufgabe 4**. Sag jeweils zuerst voraus, was passiert.
5. Erst danach den Erwartungshorizont lesen und den Merke-Kasten ins Heft übertragen.

## Erwartungshorizont

Alle Ausgaben stammen aus Läufen mit `javac` und `java` 25.

### Aufgabe 1: Das Konto absichern

**1a)** Compilerfehler `kontostand has private access in Konto`: `kontostand` ist `private`, also darf
nur die Klasse selbst direkt darauf zugreifen.

**1b)** `-400`. Das Programm läuft, tut aber etwas anderes, als es soll: ein **semantischer Fehler**.

**1c)** `k2.abheben(-30)` liefert `true`, der Kontostand ist 130. `new Konto("Bo", -50)` hat den
Kontostand -50, weil der Konstruktor den Startbetrag ungeprüft übernimmt.

**1d)**

| Aufruf | Rückgabe | Kontostand danach |
|---|---|---|
| `einzahlen(50)` | `true` | 150 |
| `einzahlen(0)` | `false` | 100 |
| `einzahlen(-500)` | `false` | 100 |
| `abheben(-30)` | `false` | 100 |
| `abheben(150)` | `false` | 100 |
| `new Konto("Bo", -50)` | (Konstruktor) | 0 |

**1e)**

```java
public Konto(String inhaber, int startbetrag) {
    this.inhaber = inhaber;
    if (startbetrag > 0) {
        kontostand = startbetrag;
    } else {
        kontostand = 0;
    }
}

public boolean einzahlen(int betrag) {
    if (betrag > 0) {
        kontostand = kontostand + betrag;
        return true;
    }
    return false;
}

public boolean abheben(int betrag) {
    if (betrag > 0 && betrag <= kontostand) {
        kontostand = kontostand - betrag;
        return true;
    }
    return false;
}
```

**1f)** Mit `setKontostand` könnte jede andere Klasse einen beliebigen Wert setzen, auch einen
negativen, und die Prüfungen in `einzahlen` und `abheben` wären umgangen. Bei einem Konto ändert sich
der Stand nur durch Buchungen.

**Zusatz `setInhaber`:**

```java
public boolean setInhaber(String neuerName) {
    if (neuerName != null && neuerName.length() > 0) {
        inhaber = neuerName;
        return true;
    }
    return false;
}
```

### Aufgabe 2: Was in einer Objektvariablen steht

**2a)**

```
5 6
150
true
false
true
```

**2b)** Zwei `Konto`-Objekte, weil `new Konto` zweimal ausgeführt wurde. `Konto b = a;` kopiert nur
die Referenz.

**2c)** `int y = x;` kopiert den Wert in ein eigenes Kästchen, `y = y + 1` ändert nur dieses Kästchen.
`Konto b = a;` kopiert die Referenz, `a` und `b` zeigen auf dasselbe Objekt. `b.einzahlen(50)` ändert
dieses eine Objekt, und `a` sieht die Änderung.

**2d)** `==` vergleicht bei Objekttypen die Referenzen. `a` und `c` zeigen auf zwei verschiedene
Objekte mit gleichem Inhalt, deshalb `false`. `a.equals(c)` liefert hier ebenfalls `false`, weil
`Konto` kein eigenes `equals` hat.

**2e)** `7 160`. `verdoppeln` ändert nur eine Kopie des Werts. `aufstocken` bekommt eine Kopie der
Referenz, die auf dasselbe Objekt zeigt wie `c`, und `einzahlen(10)` ändert dieses Objekt.

### Aufgabe 3: Wenn eine Variable auf nichts zeigt

**3a)** Null `Konto`-Objekte. `new Konto[3]` erzeugt ein Array mit drei Plätzen, alle mit `null`
belegt. In `konten[1]` steht weiter `null`.

**3b)** Bei `i = 1` bricht das Programm mit einer `NullPointerException` ab, eine Summe wird nie
ausgegeben. Das ist ein **Laufzeitfehler**.

**3c)**

```java
for (int i = 0; i < konten.length; i++) {
    if (konten[i] != null) {
        summe = summe + konten[i].getKontostand();
    }
}
```

Ausgabe: `Summe: 140`.

### Aufgabe 4: Eine Zahl für alle Konten

**4a)**

```
0
2
1 2 2
```

`Konto c = b;` kopiert nur die Referenz. Es bleibt bei zwei Konten, und `c` hat die Nummer von `b`.

**4b)** `anzahlKonten` gibt es genau einmal, auch wenn noch kein Konto existiert. Deshalb geht der
Aufruf über den Klassennamen. `getKontostand()` ist eine Objektmethode: Die Frage „Wessen
Kontostand?“ hat ohne Objekt keine Antwort.

**4c)** Die Methoden der `Zahlenanalyse` bekommen alle Daten als Parameter und lesen kein Attribut
eines Objekts. Sie brauchen keinen Zustand, also auch kein Objekt.
