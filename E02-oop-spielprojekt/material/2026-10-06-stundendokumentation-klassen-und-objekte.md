# Stundendokumentation Dienstag, 06.10.2026: Klassen und Objekte, das erste Konto

**Informatik LK, 1./2. Stunde | Einstieg in Einheit 2 „Objektorientierung und Spielprojekt“, im Zeitplan von Einheit 1 die Stunden 15 und 16 von 20**

## Was wir gemacht haben

1. **Einstieg:** An der Tafel standen nebeneinander `Zahlenanalyse.maximum(a)` und `s.length()`.
   Woher weiß `length()` ohne Parameter, welchen Text sie messen soll? Der Text gehört zu `s`, und
   `s` merkt ihn sich. Das knüpft an `==` gegen `equals` vom 30.09. an.
2. **Aufgabe 1 allein und ohne Rechner:** die Klasse `Konto` gelesen, Attribute, Konstruktor und
   Methoden benannt, `abheben` beschrieben. Besprochen mit dem Tafelbild: links die Klasse `Konto`
   als Bauplan, rechts zwei Objekte `ada` und `bo` mit eigenen Werten.
3. **BlueJ am Beamer:** `new Konto("Ada", 100)`, die Objektleiste, der Inspektor, `einzahlen(50)`.
   Dazu die Fehlermeldung, wenn man `Ada` ohne Anführungszeichen eingibt.
4. **Aufgabe 2 zu zweit in BlueJ:** zwei Objekte erzeugt, vor jedem Aufruf die Vermutung in die
   Tabelle geschrieben, dann verglichen.
5. **Aufgabe 3:** erst auf Papier die Tabelle zu `Bank.main`, dann in BlueJ gestartet und
   verglichen.
6. **Aufgabe 4:** erst den Testfall auf Papier, dann das Attribut `anzahlBuchungen` mit Getter
   ergänzt und im Code Pad geprüft. Für Schnelle: `ueberweisen` und `einzahlen(-500)`.
7. **Schmiede:** Unit „E2 Objektorientierung und Spielprojekt“, Lektion 1 „Klassen und Objekte
   benutzen“.
8. **Sicherung ins Heft:** der Merkkasten vom Blatt und der Satz „Eine Klasse ist der Bauplan, ein
   Objekt ein Exemplar mit eigenem Zustand. `new` ruft den Konstruktor auf, `objekt.methode()`
   arbeitet mit den Attributen dieses Objekts.“

## Wenn du gefehlt hast

1. Hol dir das Blatt **„Klassen und Objekte: das erste Konto“** und den Ordner `konto`
   (`Konto.java`, `Bank.java`) aus dem Gruppenordner KW41. Kopier den Ordner in deinen eigenen
   Ordner und öffne ihn in BlueJ.
2. Bearbeite **Aufgabe 1** ohne Rechner, dann **Aufgabe 2** in BlueJ (immer erst vermuten, dann
   aufrufen).
3. Füll die Tabelle in **Aufgabe 3** auf Papier aus, **bevor** du `Bank` startest. Das ist der
   Aufgabentyp, der in der Klausur kommen kann.
4. Versuch **Aufgabe 4**: zuerst den Testfall 4a aufschreiben, dann programmieren.
5. Erst danach den Erwartungshorizont lesen, den Merkkasten ins Heft übertragen und in der Schmiede
   Lektion 1 „Klassen und Objekte benutzen“ machen.

## Erwartungshorizont

Alle Programme sind mit `javac` 25 übersetzt und ausgeführt; die Ergebnisse unten stammen aus
diesen Läufen.

### 1. Aufgabe 1: eine Klasse lesen

**1a)** `inhaber` vom Typ `String`, `kontostand` vom Typ `int`.

**1b)** `public Konto(String inhaber, int startbetrag)`. Zwei Merkmale: Er heißt **genau wie die
Klasse**, und er hat **keinen Rückgabetyp**, auch nicht `void`. Gute Zusatzantwort: Er wird nur mit
`new` aufgerufen.

**1c)**

| Methode | Parameter | Rückgabe |
|---|---|---|
| `einzahlen` | `int betrag` | nichts (`void`) |
| `abheben` | `int betrag` | `boolean`: hat es geklappt? |
| `getKontostand` | keiner | `int`, den aktuellen Kontostand |
| `getInhaber` | keiner | `String`, den Namen |

**1d)** *Erwartet:* „Die Methode hebt den Betrag vom Konto ab, aber nur, wenn genug Geld darauf
ist. Dann verringert sie den Kontostand und meldet mit `true` den Erfolg. Reicht das Guthaben
nicht, bleibt der Kontostand unverändert, und sie liefert `false`.“ Den Code Zeile für Zeile
vorzulesen ist beim Operator „beschreiben“ zu wenig.

**1e)** `kontostand` ist ein **Attribut**. Es ist in der Klasse deklariert, nicht in der Methode,
und gehört zu dem Objekt, an dem `einzahlen` aufgerufen wird. Anders als eine lokale Variable
verschwindet es nach dem Aufruf nicht: Der neue Wert bleibt im Objekt gespeichert und ist beim
nächsten Aufruf noch da. Genau das unterscheidet `Konto` von der `Zahlenanalyse`, deren Methoden
sich nichts merken.

**Zu `this`:** Im Konstruktor heißen Parameter und Attribut gleich. `this.inhaber` ist das Attribut
dieses Objekts, `inhaber` allein der Parameter.

### 2. Aufgabe 2: Objekte in BlueJ

**2b)** Der Inspektor zeigt `private String inhaber = "Ada"` und `private int kontostand = 100`.

**2d)**

| Nr. | Aufruf | Rückgabe | `ada` | `bo` |
|---|---|---|---|---|
| 1 | `ada.einzahlen(50)` | keine (`void`) | 150 | 20 |
| 2 | `bo.abheben(30)` | `false` | 150 | 20 |
| 3 | `ada.abheben(30)` | `true` | 120 | 20 |
| 4 | `bo.einzahlen(15)` | keine | 120 | 35 |
| 5 | `bo.getKontostand()` | `35` | 120 | 35 |

**Die Pointe:** Nr. 2 und 3 rufen dieselbe Methode mit demselben Betrag auf und liefern
Verschiedenes, weil die beiden Objekte verschiedenen Zustand haben.

**2e)** An der Klasse bietet BlueJ nur `new Konto(...)` an (dazu Bearbeiten, Übersetzen usw.),
keine der vier Methoden. *Erwartet:* „`einzahlen` braucht ein bestimmtes Konto, auf das eingezahlt
wird; die Klasse selbst hat keinen Kontostand.“ Bei der `Zahlenanalyse` standen die Methoden direkt
an der Klasse, weil sie `static` waren. Mehr zu `static` nach der Klausur.

**2f)** `c.getKontostand()` zeigt `40 (int)`. `Konto.getKontostand()` liefert den Compilerfehler
`non-static method getKontostand() cannot be referenced from a static context`. *Erwartet:* „Wessen
Kontostand? Die Methode braucht ein Objekt, die Klasse selbst hat keinen.“

### 3. Aufgabe 3: Zustand verfolgen

**3a)**

| Zeile | `a` | `b` | Ausgabe |
|---------------------------------------------|------|------|------------|
| `Konto a = new Konto("Ada", 100);` | 100 | | |
| `Konto b = new Konto("Bo", 20);` | 100 | 20 | |
| `a.einzahlen(50);` | 150 | 20 | |
| `b.einzahlen(a.getKontostand());` | 150 | 170 | |
| `boolean ok = a.abheben(200);` + Ausgabe | 150 | 170 | `false` |
| `ok = b.abheben(120);` + Ausgabe | 150 | 50 | `true` |
| `a.abheben(a.getKontostand() / 2);` | 75 | 50 | |
| die beiden letzten Ausgaben | 75 | 50 | `Ada: 75`, `Bo: 50` |

**3b)** Ausgabe des Programms:

```
false
true
Ada: 75
Bo: 50
```

**Typische Fehler:** `b` nach Zeile 4 mit 150 statt 170 (die Einzahlung addiert, sie überschreibt
nicht); bei `a.abheben(200)` trotzdem abziehen; einen Rückgabewert von `a.abheben(75)` suchen,
obwohl er gar nicht ausgegeben wird.

**3c)** **Zwei.** `new` steht genau zweimal da, und jedes `new` erzeugt ein Objekt.
`a.getKontostand()` erzeugt kein Objekt, sondern liefert eine Zahl.

### 4. Aufgabe 4: die Klasse ergänzen

**4a)** Kontostand **120**, Anzahl der Buchungen **2**. Das Abheben von 500 scheitert und zählt
nicht.

**4b)** Musterlösung, die Änderungen gegenüber der Fassung im Gruppenordner sind markiert:

```java
public class Konto {

    private String inhaber;
    private int kontostand;
    private int anzahlBuchungen;               // neues Attribut

    public Konto(String inhaber, int startbetrag) {
        this.inhaber = inhaber;
        this.kontostand = startbetrag;
        this.anzahlBuchungen = 0;               // neu
    }

    public void einzahlen(int betrag) {
        kontostand = kontostand + betrag;
        anzahlBuchungen++;                      // neu
    }

    public boolean abheben(int betrag) {
        if (betrag <= kontostand) {
            kontostand = kontostand - betrag;
            anzahlBuchungen++;                  // neu, nur im Erfolgsfall
            return true;
        }
        return false;
    }

    public int getKontostand() {
        return kontostand;
    }

    public String getInhaber() {
        return inhaber;
    }

    public int getAnzahlBuchungen() {           // neu
        return anzahlBuchungen;
    }
}
```

**Häufigster Fehler:** `anzahlBuchungen++` vor das `if` in `abheben` gesetzt. Dann zählt auch das
gescheiterte Abheben, und der Testfall liefert 3 statt 2. Ein `int`-Attribut ist ohne Zuweisung
schon 0; die Zeile im Konstruktor ist trotzdem guter Stil.

**4c)** Im Code Pad zum Beispiel:

```java
Konto k = new Konto("Ada", 100);
k.einzahlen(50);
k.abheben(500)
k.abheben(30)
k.getKontostand()
k.getAnzahlBuchungen()
```

Erwartet: `false`, `true`, `120`, `2`.

**Für Schnelle, `ueberweisen`:**

```java
public boolean ueberweisen(Konto ziel, int betrag) {
    if (abheben(betrag)) {
        ziel.einzahlen(betrag);
        return true;
    }
    return false;
}
```

`abheben` prüft schon, ob genug Geld da ist; nur wenn es klappt, wird auf `ziel` eingezahlt. Probe:
Ada hat nach 4a 120. `ada.ueberweisen(bo, 70)` liefert `true`, ein zweites Mal `false`. Hier wird
zum ersten Mal ein **Objekt als Parameter** übergeben.

**Für Schnelle, `einzahlen(-500)`:** Der Kontostand sinkt, auch unter 0. Das ist weder ein
Compiler- noch ein Laufzeitfehler, sondern ein **semantischer Fehler**: Das Programm tut etwas
anderes, als es soll. Darum ging es am Donnerstag, 08.10.

### 5. Schmiede: Lektion „Klassen und Objekte benutzen“

Die Schmiede gibt zu jeder Aufgabe selbst Rückmeldung. Die Kernpunkte:

- **Zuordnung:** `private int kontostand;` Attribut; `public Konto(String inhaber, int startbetrag)`
  Konstruktor; `abheben` Methode mit Rückgabewert, `einzahlen` Methode ohne Rückgabewert;
  `new Konto("Ada", 100)` Objekt erzeugen; `a.einzahlen(50);` Methode an einem Objekt aufrufen.
- **Konstruktor erkennen:** Er heißt genau wie die Klasse und hat keinen Rückgabetyp.
- **Lückentext:** `new`, `einzahlen`, `getKontostand`.
- **Zustand Kim und Mo:** `60` (k hat 65, m bekommt 10 + 65 = 75, k hebt 50 ab und hat 15, 75
  minus 15).
- **Pia:** `false` (nach dem ersten Abheben sind nur noch 10 da).
- **Anzahl Objekte:** 2, weil `new` zweimal dasteht.
- **Wahr/Falsch:** gleiche Attributwerte immer: falsch; Konstruktor ohne Rückgabetyp: wahr;
  `Konto.einzahlen(50);`: falsch (Compilerfehler); Attribut behält seinen Wert: wahr.
- **Freitext Klasse und Objekt:** Die Klasse `Konto` ist der Bauplan (jedes Konto hat Inhaber und
  Kontostand und kann einzahlen und abheben). Ein Objekt ist ein konkretes Konto, mit
  `new Konto("Ada", 100)` erzeugt, mit eigenen Attributwerten. Zwei Objekte haben dieselben
  Methoden, aber verschiedenen Zustand.

**Programmieraufgabe `Zaehler`** (Musterlösung, mit dem Test der Schmiede geprüft, Ausgabe `3`,
`1`, `2`):

```java
class Zaehler {
    private int stand;

    Zaehler() {
        stand = 0;
    }

    void klick() {
        stand++;
    }

    void zuruecksetzen() {
        stand = 0;
    }

    int getStand() {
        return stand;
    }
}
```

Die beiden Zähler `eingang` und `ausgang` zählen unabhängig voneinander, weil jedes Objekt sein
eigenes `stand` hat. Die Klasse steht ohne `public` davor, sonst lehnt die Schmiede sie ab.

### Merkkasten (ins Heft)

| Begriff | Bedeutung | im Code |
|----------------|--------------------------------------------------------------|-------------------------|
| Klasse | Bauplan: legt fest, welche Attribute und Methoden jedes Objekt hat | `public class Konto { ... }` |
| Objekt | ein nach dem Bauplan erzeugtes Exemplar mit eigenen Attributwerten | `new Konto("Ada", 100)` |
| Attribut | eine Variable, die jedes Objekt für sich hat; ihre Werte sind der **Zustand** | `private int kontostand;` |
| Konstruktor | wird bei `new` aufgerufen und setzt die Startwerte; heißt wie die Klasse, kein Rückgabetyp | `public Konto(String inhaber, int startbetrag)` |
| Methode | etwas, das jedes Objekt kann; sie arbeitet mit den Attributen **dieses** Objekts | `a.einzahlen(50);` |

> **Eine Klasse ist der Bauplan, ein Objekt ein Exemplar mit eigenem Zustand. `new` ruft den
> Konstruktor auf, `objekt.methode()` arbeitet mit den Attributen dieses Objekts.**

### Zum Selbstprüfen

Erst selbst antworten, dann die erwartete Antwort lesen.

1. **Woran erkennst du in einer Klasse den Konstruktor?**\
   *Erwartet:* Er heißt genau wie die Klasse und hat keinen Rückgabetyp, nicht einmal `void`.
2. **Warum gibt `bo.abheben(30)` `false` zurück, `ada.abheben(30)` aber `true`?**\
   *Erwartet:* Gleiche Methode, gleicher Betrag, aber verschiedener Zustand: `bo` hat nur 20,
   `ada` hat 150.
3. **Was ist der Unterschied zwischen dem Attribut `kontostand` und einer lokalen Variable in
   einer Methode?**\
   *Erwartet:* Das Attribut gehört zum Objekt und behält seinen Wert nach dem Methodenaufruf. Eine
   lokale Variable verschwindet am Ende des Aufrufs.
4. **Warum ist `Konto.getKontostand()` ein Fehler?**\
   *Erwartet:* Die Methode braucht ein bestimmtes Objekt. Die Klasse selbst hat keinen Kontostand
   („non-static method ... cannot be referenced from a static context“).
5. **Wie viele Objekte erzeugt
   `Konto a = new Konto("A", 1); Konto b = new Konto("B", 2); a.einzahlen(b.getKontostand());`?**\
   *Erwartet:* Zwei. Nur `new` erzeugt Objekte; `getKontostand()` liefert eine Zahl.
6. **In `abheben` steht `anzahlBuchungen++` vor dem `if`. Was geht schief?**\
   *Erwartet:* Auch ein gescheitertes Abheben wird gezählt. Der Testfall 100, `einzahlen(50)`,
   `abheben(500)`, `abheben(30)` liefert 3 statt 2 Buchungen.

## Noch nicht hier

Kapselung mit `private` im Detail, `static`, Referenzen und `null`. Das kommt ab dem 22.10.

## Was als Nächstes drankommt

Donnerstag, 08.10.: Abschluss von E1 mit Fehlerarten, Debugger, Struktogramm und Javadoc.
`einzahlen(-500)` ist dort das Beispiel für einen semantischen Fehler. Dienstag, 13.10.:
Wiederholungsstunde vor der Klausur.

**Klausur 1 am Dienstag, 20.10.** prüft E1 und den Einstieg in Klassen und Objekte (Block 8 der
[Wiederholliste](../../E01-java-fundament/material/klausur-1-wiederholliste.md)): Klasse und Objekt
unterscheiden, Objekte mit `new` erzeugen, Methoden mit der Punktnotation aufrufen, den Zustand
mehrerer Objekte mit einer Tabelle verfolgen (wie Aufgabe 3), einen Konstruktor erkennen und eine
kleine eigene Klasse schreiben (wie `Zaehler` oder Aufgabe 4).

Donnerstag, 22.10.: Klassen, die ihr selbst schreibt, Kapselung (`private`), Referenzen und `null`.
`ueberweisen` ist dort der Anschluss an „Objekt als Parameter“.
