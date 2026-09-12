# Projektauftrag: Flugsimulator für die Schulrakete (E2, Alternative zum Spielprojekt)

**Für wen:** eine Person oder ein Zweierteam, das in E2 lieber rechnet als zeichnet. Das Projekt
läuft parallel zum Spielprojekt, auf demselben Framework, mit denselben Terminen und derselben
Bewertung. Es ist nicht weniger und nicht mehr Arbeit, nur eine andere Sorte.

## Worum es geht

Die Schule hat eine Modellrakete, den ApexExplorer. Sie fliegt mit einem echten Treibsatz (C6 mit
10 Ns oder D9 mit 20 Ns Gesamtimpuls), hat einen barometrischen Höhensensor an Bord, eine
Lagemessung in drei Achsen und einen Kraftsensor, der den Schub des Treibsatzes während des Fluges
aufzeichnet. Der Physik-Leistungskurs startet sie im Frühjahr 2027.

Dein Programm sagt diesen Flug voraus, bevor er stattfindet: Start, Brennphase, Freiflug bis zum
Gipfelpunkt, Fallschirm, Landung, animiert auf dem Bildschirm und als Zahlen in einer Tabelle. Am
Ende steht eine Vorhersage: **so hoch fliegt sie, so schnell wird sie, so lange dauert es bis zum
Gipfel.** Wenn die Rakete geflogen ist, wird deine Vorhersage gegen den Bordsensor gehalten, und
deine angenommene Schubkurve gegen die gemessene. Das ist der Test, den ein Spiel nie bekommt.

## Was am Ende vorliegt

1. **UML-Klassendiagramm** deines Entwurfs, gezeichnet bevor du programmierst (Besprechung am 05.11.).
2. **Das Programm** als BlueJ-Projekt, mit Animation im Framework des Spielprojekts.
3. **Eine CSV-Datei** der simulierten Flugkurve mit den Spalten Zeit, Höhe, Geschwindigkeit,
   Beschleunigung, Schub, Masse. Diese Datei benutzt der ganze Kurs in E5 als Übungsdatensatz.
4. **Eine Seite Vorhersage:** Gipfelhöhe, Zeit bis zum Gipfel, Höchstgeschwindigkeit, dazu alle
   Annahmen (Massen, Widerstandsbeiwert, Zeitschritt) und ein Höhenbereich statt einer einzelnen
   Zahl, weil der Widerstandsbeiwert unsicher ist.
5. **Fünf Minuten Präsentation** am 01. oder 03.12., wie alle anderen Teams.

## Die Physik (Physik-LK-Niveau, nicht mehr)

Auf die Rakete wirken drei Kräfte, alle entlang der Flugbahn, die Rakete fliegt senkrecht:

- **Schub** $F_S(t)$ aus der Schubkurve des Treibsatzes. Die Kurve ist eine Wertetabelle (Zeit,
  Kraft), zwischen den Stützstellen wird linear interpoliert. Nach dem Brennschluss ist der Schub 0.
- **Gewicht** $m(t) \cdot g$. Die Masse nimmt ab, solange der Treibsatz brennt: der verbrannte
  Anteil ist der bis dahin gelieferte Impuls geteilt durch den Gesamtimpuls,
  $m(t) = m_\text{leer} + m_\text{Treibstoff} \cdot \left(1 - \frac{I(t)}{I_\text{ges}}\right)$.
- **Luftwiderstand** $F_W = \tfrac{1}{2} \, c_w \, \rho \, A \, v^2$, immer gegen die Bewegung,
  mit $\rho = 1{,}2\ \text{kg/m}^3$, $A = \pi d^2 / 4$ und $c_w$ zwischen 0,5 und 0,75 für
  Modellraketen. Nach dem Öffnen des Fallschirms wird $c_w \cdot A$ so groß, dass die Rakete mit
  etwa 5 m/s sinkt.

Die Simulation läuft in Zeitschritten (Euler-Verfahren): Kräfte summieren, $a = F / m$,
$v \leftarrow v + a \cdot \Delta t$, $h \leftarrow h + v \cdot \Delta t$. Beginne mit
$\Delta t = 0{,}01$ s und prüfe, ob sich die Gipfelhöhe bei $\Delta t = 0{,}001$ s noch ändert.
Der Fallschirm öffnet nach der Ausstoßverzögerung des Treibsatzes (je nach Typ 3 oder 5 Sekunden
nach Brennschluss), nicht automatisch am Gipfel. Ob das gut passt, ist eine Frage, die dein
Programm beantworten kann.

**Drei Prüfungen, die dein Modell bestehen muss, bevor du der Vorhersage traust:**

1. Ohne Schub und ohne Luftwiderstand fällt die Rakete frei: $h(t) = h_0 - \tfrac{1}{2} g t^2$
   muss herauskommen, bis auf den Fehler des Zeitschritts.
2. Mit konstantem Schub $F$, konstanter Masse $m$ und ohne Luftwiderstand gilt
   $h(t) = \tfrac{1}{2} \left(\tfrac{F}{m} - g\right) t^2$.
3. Plausibilität: Der Hersteller nennt für den C6 rund 60 m Gipfelhöhe, für den D9 über 200 m.
   Liegst du weit daneben, stimmt eine Annahme nicht.

## Die Daten

- Schubkurve des Treibsatzes: von thrustcurve.org (Suche nach dem Treibsatztyp, Datenformat als
  Wertetabelle) oder aus den Unterlagen der Raketenwerkstatt. Ersatzweise die Kurve eines
  vergleichbaren C6 oder D9, mit Angabe, welche du genommen hast.
- Leermasse der Rakete, Masse des Treibsatzes, Durchmesser, Ausstoßverzögerung: kommen von Herrn Abs,
  spätestens am 03.11. Bis dahin rechnest du mit Platzhaltern, die du deutlich kennzeichnest.
- Erdbeschleunigung 9,81 m/s², Luftdichte 1,2 kg/m³ als Konstanten.

## Die Objektorientierung (das ist der Pflichtteil, den ich prüfe)

Das Projekt ersetzt das Spiel, also muss es dieselben Konzepte tragen. Sie ergeben sich hier aus
der Sache und nicht aus der Aufgabe:

- **Abstrakte Klasse `Kraft`** mit der abstrakten Methode `betrag(Zustand z)`, dazu die
  Unterklassen `Schub`, `Gewicht` und `Luftwiderstand`. Der Simulator hält eine `ArrayList<Kraft>`
  und summiert über alle Elemente, ohne zu wissen, welche Kraft er gerade in der Hand hat. Das ist
  Polymorphie mit Zweck: Der Fallschirm ist dann nur eine weitere Kraft in der Liste.
- **`Rakete` als Kompositum** aus Bauteilen: `Rumpf`, `Triebwerk`, `Nutzlast`, `Fallschirm` sind
  Unterklassen von `Bauteil`. Masse und Schwerpunkt der Rakete ergeben sich aus den Teilen, wie
  die Größe eines Verzeichnisses aus seinen Dateien.
- **`Zustand`** (Zeit, Höhe, Geschwindigkeit, Masse) als eigene Klasse mit Konstruktor und
  Zugriffsmethoden. **`Messpunkt`** als das, was pro Zeitschritt in die Liste wandert; die Liste ist
  eine `ArrayList<Messpunkt>` und wird am Ende als CSV geschrieben.
- **Die Rakete ist ein zeichenbares Objekt des Frameworks.** Der Zeichentakt ist nicht der
  Simulationsschritt: Pro Bild rechnest du mehrere kleine Zeitschritte, sonst hängt deine Physik von
  der Bildrate ab.
- Kapselung durchgehend (private Attribute, Zugriffsmethoden), Konstruktoren mit Parametern,
  `static` nur für echte Konstanten, `toString()` in jeder Datenklasse, `super` und Überschreiben
  dort, wo eine Unterklasse etwas anders macht. `instanceof` nur, wenn du begründen kannst, warum
  Polymorphie an der Stelle nicht reicht.
- Das UML-Diagramm zeigt Vererbung, Assoziation und die Komposition mit Kardinalitäten, und der
  Code sieht danach genauso aus. Beides in beide Richtungen lesen zu können ist die Abiturform.

## Termine (gleich wie das Spielprojekt)

| Datum | Meilenstein |
|---|---|
| Di 13.10. | Projektauftrag, Wahl: Spiel oder Simulator |
| Do 05.11. | Entwurf: UML-Klassendiagramm und das Physikmodell auf einer Seite, Besprechung |
| Do 12.11. | Zwischenstand: Simulation ohne Luftwiderstand läuft, Prüfungen 1 und 2 bestanden, Animation zeigt Rakete und Höhe |
| Di 17.11. | Klausur 1 (für alle, nicht projektbezogen) |
| Do 26.11. | Vollausbau: Luftwiderstand, Masseabnahme, Fallschirm, CSV, Höhenbereich |
| Di 01.12. | Abgabe; Präsentationen am 01. und 03.12. |
| Frühjahr 2027 | Start der Rakete, Vergleich mit dem Bordsensor, Nachtrag zur Vorhersage |

## Bewertung

Wie beim Spielprojekt: der Entwurf (UML und Modell), die Umsetzung der Konzepte aus E2, die
Funktion und Nachvollziehbarkeit des Programms, die Präsentation. **Die Vorhersage wird nicht
danach bewertet, ob sie im Frühjahr stimmt, sondern ob die Abweichung erklärt werden kann.** Eine
begründete Fehlersuche nach dem Flug ist mehr wert als ein Zufallstreffer.

Es gilt unsere KI-Vereinbarung: erklären lassen ja, machen lassen nein, Nutzung wird angegeben.
Physikformeln und die Schubkurve darfst du selbstverständlich nachschlagen, gib die Quelle an.

## Wenn noch Zeit ist (freiwillig)

- Zeitschrittweiten vergleichen und den Fehler des Euler-Verfahrens sichtbar machen.
- Unsicherheit: $c_w$ und Masse in einem Bereich zufällig ziehen, tausend Flüge rechnen, die
  Verteilung der Gipfelhöhen zeigen.
- Wind oder Startneigung: aus einer Dimension werden zwei, aus dem Zustand ein Vektor.
- Im Frühjahr: die echte CSV des ApexExplorer einlesen und beide Kurven übereinander zeichnen.

## Quellen

- Schubkurven: https://www.thrustcurve.org/
- Der Bausatz: https://www.raketenwerkstatt.de/
- Java-API (ArrayList, Math): https://docs.oracle.com/en/java/javase/21/docs/api/index.html
