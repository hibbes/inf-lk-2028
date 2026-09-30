# Stundendokumentation Mittwoch, 30.09.2026: Strings, `equals` und das Palindrom

**Informatik LK, 1./2. Stunde | Einheit 1 „Java-Fundament“, Stunden 11 und 12 von 20**

## Was wir gemacht haben

1. **Werkzeugkasten Zeichenketten:** `length()`, `charAt(i)`, `substring(a, b)`,
   `indexOf(...)`, Vergleich mit `equals`, Umwandlung Text zu Zahl
   (`Integer.parseInt`) und zurück (`String.valueOf`). Zu zweit am Code Pad
   nachgetippt und abgehakt.
2. **`==` gegen `equals`** am Beamer: warum `==` bei Text falsch ist, obwohl der
   Compiler nichts meldet. Bild dazu: eine Variable ist ein Zettel mit einem
   Pfeil auf einen Kasten. `==` vergleicht die Pfeile, `equals` den Inhalt der
   Kästen.
3. **Schmiede-Lektion 4 „Strings“:** `umdrehen`, `istPalindrom`, `zaehle`,
   `vokale`, und wer durch war `initialen` und `caesar`.
4. **Zwei Palindrom-Varianten** verglichen (umdrehen und vergleichen gegen zwei
   Zeiger von außen nach innen) und den Operator **„erläutern“** geübt:
   beschreiben **und** begründen.
5. **Sicherung ins Heft:** „Bei Text immer `equals`. `==` fragt nur, ob zwei
   Variablen auf dasselbe Objekt zeigen.“ und „Erläutern heißt: was und warum.“

## Wenn du gefehlt hast

1. Geh das Blatt „Strings-Werkzeugkasten“ durch und tippe die Methodentabelle am
   Code Pad nach, bis du `length()`, `charAt`, `substring` und `equals` sicher
   benutzt.
2. Öffne die Schmiede, Lektion 4, und mach mindestens `umdrehen` und
   `istPalindrom` **selbst** grün, bevor du die Musterlösungen unten liest. Das
   Blatt trägt Beispiele und gestufte Hilfen.
3. Lies danach den Erwartungshorizont und vergleiche mit deinem Code. Wichtig
   ist nicht, ob es Zeichen für Zeichen gleich ist, sondern ob es für alle
   Beispiele dasselbe liefert.

## Erwartungshorizont

Alle Java-Ausschnitte sind mit `javac` 25 übersetzt und mit den unten genannten
Beispielen getestet.

### Aufwärmen: die drei Vorhersagen

| Ausdruck | Ergebnis | warum |
|---|---|---|
| `"Informatik".length()` | `10` | zehn Zeichen |
| `"Informatik".substring(0, 5)` | `"Infor"` | Zeichen von Position 0 bis **vor** 5, also 0 bis 4 |
| `"42" + 1` | `"421"` | steht ein Text im Spiel, macht `+` aus der Zahl Text und hängt an, es wird **nicht** gerechnet |

Rückblick auf gestern: `(int) -3.99` ist `-3`. Der Cast schneidet die
Nachkommastellen ab, er rundet nicht.

### 1. `==` gegen `equals`

Am Code Pad vorhergesagt und geprüft:

```
String a = "Hallo";
String b = "Hallo";
String teil = "Hal";
String d = teil + "lo";
String e = new String("Hallo");

a == b        -> true     beide zeigen auf dasselbe Literal
a == d        -> false    d wird zur Laufzeit gebaut, ein anderes Objekt
a.equals(d)   -> true     gleicher Inhalt
a == e        -> false    new erzeugt immer ein neues Objekt
a.equals(e)   -> true     gleicher Inhalt
```

> **Merksatz:** Bei Text immer `equals`. `==` fragt nur, ob zwei Variablen auf
> dasselbe Objekt zeigen, nicht ob der Inhalt gleich ist. Dass `a == b` hier
> `true` liefert, ist Zufall des Compilers (gleiche Literale teilen sich ein
> Objekt) und kein Verlass.

### 2. Die sechs Programmieraufgaben der Lektion 4

**Aufgabe 1, `umdrehen`.** Von hinten nach vorn über `charAt` laufen und
anhängen.

```java
public static String umdrehen(String s) {
    String r = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        r = r + s.charAt(i);
    }
    return r;
}
```

Getestet: `umdrehen("Otto")` ist `"ottO"`, `umdrehen("a")` ist `"a"`. Kürzer geht
es mit `new StringBuilder(s).reverse().toString()`.

**Aufgabe 2, `istPalindrom`.** Groß und klein egal, Leerzeichen zählen mit.
Zwei saubere Wege, beide waren am Beamer:

```java
// Variante A: umdrehen und mit equals vergleichen
public static boolean istPalindrom(String s) {
    String k = s.toLowerCase();
    return k.equals(umdrehen(k));
}

// Variante B: zwei Zeiger von außen nach innen
public static boolean istPalindrom(String s) {
    String k = s.toLowerCase();
    int links = 0;
    int rechts = k.length() - 1;
    while (links < rechts) {
        if (k.charAt(links) != k.charAt(rechts)) {
            return false;
        }
        links++;
        rechts--;
    }
    return true;
}
```

Getestet mit `"Otto"`, `"Rentner"`, `"ab ba"`, `""` (alle `true`) und `"Java"`
(`false`). **Falsch** wäre `return k == umdrehen(k);`: das übersetzt und läuft,
liefert aber für jedes Wort `false`, weil `umdrehen(k)` ein neues Objekt baut und
`==` nur die Objekte vergleicht, nicht den Inhalt.

**Aufgabe 3, `zaehle`.** Erst das zu suchende Zeichen holen, dann durchzählen.

```java
public static int zaehle(String s, String zeichen) {
    char c = zeichen.charAt(0);
    int anzahl = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == c) {       // char mit == ist richtig, das ist ein primitiver Typ
            anzahl++;
        }
    }
    return anzahl;
}
```

Getestet: `zaehle("Mississippi", "s")` ist `4`, `zaehle("Mississippi", "p")` ist
`2`, `zaehle("Mississippi", "z")` ist `0`. Hier ist `==` genau richtig, weil
`char` eine Zahl ist und kein Objekt.

**Aufgabe 4, `vokale`.** Text klein machen und für jedes Zeichen fragen, ob es in
`"aeiou"` vorkommt.

```java
public static int vokale(String s) {
    String k = s.toLowerCase();
    int anzahl = 0;
    for (int i = 0; i < k.length(); i++) {
        if ("aeiou".indexOf(k.charAt(i)) >= 0) {
            anzahl++;
        }
    }
    return anzahl;
}
```

Getestet: `vokale("Informatik")` ist `4`, `vokale("Rhythmus")` ist `1` (nur das
`u`, das `y` zählt nicht), `vokale("AEIOU")` ist `5`, `vokale("xyz")` ist `0`.

**Aufgabe 5, `caesar`.** Jeden Großbuchstaben um den Schlüssel verschieben, mit
Umbruch nach Z, alles andere unverändert.

```java
public static String caesar(String text, int schluessel) {
    String r = "";
    for (int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);
        if (c >= 'A' && c <= 'Z') {
            c = (char) ('A' + (c - 'A' + schluessel) % 26);
        }
        r = r + c;
    }
    return r;
}
```

Getestet: `caesar("XYZ", 3)` ist `"ABC"`, `caesar("HALLO WELT", 13)` ist
`"UNYYB JRYG"`, `caesar("Abc", 1)` ist `"Bbc"` (nur das `A` wird verschoben, `bc`
bleiben klein und stehen). Das ist der Rückgriff auf gestern: `c - 'A'` rechnet
mit dem `char` als Zahl, `(char)` macht aus der Zahl wieder ein Zeichen.

*Zum Weiterdenken:* Mit negativem Schlüssel geht das schief, weil `-1 % 26` in
Java `-1` ist und nicht `25`. Wer das abfangen will, rechnet
`((c - 'A' + schluessel) % 26 + 26) % 26`.

**Aufgabe 6, `initialen`.** Am Leerzeichen trennen, die ersten Buchstaben groß.

```java
public static String initialen(String name) {
    String[] teile = name.split(" ");
    return Character.toUpperCase(teile[0].charAt(0)) + "."
         + Character.toUpperCase(teile[1].charAt(0)) + ".";
}
```

Getestet: `initialen("Alan Turing")` ist `"A.T."`, `initialen("grace hopper")`
ist `"G.H."`.

### 3. Die drei Verständnisaufgaben

**Aufgabe 7 (Auswahl): Warum ist `s == t` bei Strings ein Fehler, auch wenn es
manchmal `true` liefert?**

Richtig ist: **`==` vergleicht, ob beide Variablen auf dasselbe Objekt zeigen,
nicht den Inhalt.** Zwei Strings mit gleichem Inhalt können verschiedene Objekte
sein, dann ist `==` falsch, obwohl der Text gleich ist. Genau deshalb `equals`.
Die anderen Antworten stimmen nicht: `==` ist bei Strings erlaubt und übersetzt,
es vergleicht nicht nur die ersten Zeichen, und es ist nicht immer `false`.

**Aufgabe 8: Was liefert `"Informatik".charAt(2)`?** Das Zeichen **`f`**. Die
Positionen beginnen bei 0: `I` ist 0, `n` ist 1, `f` ist 2.

**Aufgabe 9: Was liefert `"Leistungsfach".substring(0, 8)`?** Der Text
**`Leistung`**. `substring(a, b)` nimmt die Zeichen von Position `a` bis **vor**
`b`, hier also die acht Zeichen an den Positionen 0 bis 7.

### 4. Operator „erläutern“: Warum ist Variante B bei langen Texten schneller?

*Erwartet (sinngemäß, drei bis vier Sätze):* Variante B vergleicht jeweils das
vorderste und das hinterste noch nicht geprüfte Zeichen und schiebt beide Zeiger
zur Mitte. Sie braucht deshalb höchstens halb so viele Vergleiche, wie der Text
Zeichen hat, und hört beim ersten Unterschied sofort auf. Variante A baut dagegen
immer erst den ganzen umgedrehten Text, auch wenn schon das erste und letzte
Zeichen verschieden sind, und vergleicht erst danach. Dazu kommt, dass
`r = r + s.charAt(i)` bei jedem Schritt einen neuen String erzeugt und den alten
Inhalt kopiert.

*Nur beschrieben, nicht erläutert wäre:* „B hat zwei Variablen `links` und
`rechts` und eine `while`-Schleife.“ Das sagt, was dasteht, aber nicht, warum es
schneller ist. **Erläutern heißt: das Was und das Warum.**

### 5. Selbsttest (mit Java 25 ausgeführt)

| Aufruf | Ergebnis |
|---|---|
| `umdrehen("Otto")` | `ottO` |
| `istPalindrom("Rentner")` | `true` |
| `istPalindrom("Java")` | `false` |
| `zaehle("Mississippi", "s")` | `4` |
| `vokale("Informatik")` | `4` |
| `caesar("HALLO WELT", 13)` | `UNYYB JRYG` |
| `initialen("Alan Turing")` | `A.T.` |
| `"Informatik".charAt(2)` | `f` |
| `"Leistungsfach".substring(0, 8)` | `Leistung` |

## Was als Nächstes drankommt

Donnerstag, 01.10.: Codeanalyse und Fehlerarten (Schmiede-Lektion 6), fremden
Code lesen und die typischen Fehler benennen. Dazu ein Beispielpaar „schwache
gegen gute Erläuterung“, damit der Operator „erläutern“ sitzt.
