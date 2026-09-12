# Zweijahresplanung Informatik Leistungsfach, Kurs INF1, J1 2026/27 und J2 2027/28 (Abitur 2028)

**J1: 182 Netto-Unterrichtsstunden in 40 Unterrichtswochen** (Halbjahr 1: 80 Stunden in 17 Wochen,
Halbjahr 2: 102 Stunden in 23 Wochen). **J2: rund 134 Stunden bis zum schriftlichen Abitur**
(J2.1 etwa 84, J2.2 etwa 50) plus rund 18 Stunden nach den schriftlichen Prüfungen.

Die J1-Zahlen sind nicht geschätzt, sondern aus dem WebUntis-Stundenplan gegen den
iServ-Schulkalender gerechnet (Ferien, Feiertage, Studieninformationstag J1 abgezogen).
Die J2-Zahlen sind eine Schätzung: gleiches Stundenraster wie 2026/27, Ferien 2027/28 laut
Kultusministerium, Abiturtermine laut Terminplan 2028 (Stand 16.03.2026). Rechenweg: `planung/rechnung/` (`inf1_wochen.py` für J1 auf Basis des WebUntis-Exports, `j2_wochen.py` für J2).

Stand: 12.09.2026. Erster Kurstag: Dienstag, 15.09.2026.

---

## Ausgangslage

**Der Kurs.** INF1 J1, 5 Wochenstunden, Raum 0.209: Di 1./2. (7:40 bis 9:15), Do 8./9.
(14:00 bis 15:35) und Mi 1./2. nur in ungeraden Kalenderwochen. Der Kurs hat also im Wechsel
6 und 4 Stunden pro Woche, drei Doppelstunden in der einen, zwei in der anderen. Das prägt die
Planung: Doppelstunden sind die Grundeinheit, Programmierphasen brauchen die 6er-Wochen.

**Was wir noch nicht wissen (vor dem 15.09. klären, siehe „Offene Punkte“).** Wer im Kurs sitzt und
mit welchem Vorwissen: IMP bis Klasse 10, Brückenkurs Informatik in Klasse 10, oder beides gemischt.
Beim Abiturjahrgang 2026 kamen zwei von fünf Schülern vom Oken-Gymnasium (Schulversuch,
Kooperationskurs). Der Bildungsplan verlangt für das Leistungsfach die Kompetenzen des
Brückenkurses (3.1) als Basis, und der Aufgabenfundus sagt ausdrücklich, dass Inhalte aus der
Schnittmenge von Brückenkurs und IMP im Abitur vorkommen können. Die erste Woche ist deshalb
eine Diagnosewoche, und Einheit 1 ist so gebaut, dass sie mit beiden Vorgeschichten funktioniert.

**Was der letzte Kurs gemacht hat (hausübliche Reihenfolge).** Aus dem iServ-Forum
`J2_LF_Inf1` (Forum 22), den GitHub-Repos `Practices2425`, `JavaWillNurSpielen`,
`zock_reference` und den Abschlussstunden im Repo (`informatik/inf-lk/abschluss/`) lässt sich
der Vorgängerkurs (Abitur 2026) rekonstruieren:

| Phase | Inhalt beim Vorgängerkurs | Beleg |
|---|---|---|
| J1.1 | Java-Grundlagen und Objektorientierung mit dem Spielprojekt nach Panitz, „Java will nur spielen“ | Forum 43, Repos JavaWillNurSpielen, Practices2425 (Fahrzeuge, Mediathek, Composite-Dateisystem) |
| J1.2 | Algorithmen auf Datenstrukturen, Sortieren, Graphen, Datenbanken; Rekursion und Fraktale | Forum 43 und 44 (Beiträge Januar 2025), Practices2425 (Rekursion, MergeSort, Listen), Abschlussstunde Mandelbrot |
| J2.1 | Rechner und Netze, Kryptologie, Automaten und formale Sprachen, Projektmanagement | Forum 77 bis 80 (Beiträge September 2025) |
| J2.2 | Abiturvorbereitung mit alten Prüfungen, dreiwöchiger Ferienlernplan vor der Klausur | Forum 81, Repo InfAbi26 |

Diese Reihenfolge behält die Planung im Kern bei. Sie ändert vier Dinge: die Bitebene
(Zweierkomplement, Huffman, LZW, Hash) bekommt eine eigene Einheit im ersten Halbjahr statt
nebenher zu laufen, Rekursion wird als eigene Einheit dokumentiert (beim Vorgängerkurs gemacht,
aber nirgends festgehalten), Projektmanagement mit git rückt ans Ende von J1, damit die Schüler
das Kurs-Repo auf GitHub von Anfang J2 an selbst benutzen können, und die Abiturvorbereitung
beginnt schon im Januar J2 mit dem Pflichtteil A.

**Lernstand, der Vorsicht verlangt.** Beim letzten Kurs waren die reinen Programmierfertigkeiten die
größte Hürde, bis ins Abitur hinein (Notizen aus der Erst- und Zweitkorrektur 2026). Die
Konsequenz: das erste Halbjahr ist zu drei Vierteln Programmieren, mit täglichen kleinen
Drills in der XP-Edu-Schmiede, und jede spätere Einheit hat einen Implementierungsanteil, auch
Datenbanken (JDBC) und Automaten (DEA in Java).

---

## Verbindliche Vorgaben für das Abitur 2028

Quellen: Bildungsplan 2016 Informatik (Schulversuchsfassung, Stand 21.01.2020), Facherlass
Abitur 2028 (KM35-6615-149/6, Stand 02.07.2026), Aufgabenfundus Leistungsfach Version 3.0
(20.10.2025), Leitfaden Abitur 2028 (16.12.2025), Terminplan 2028 (16.03.2026). Alle sind öffentlich, die Links stehen in `links.md`.

- **Inhalte:** Bildungsplan 3.1 (Brückenkurs) und 3.3 (Leistungsfach). **Nicht Gegenstand der
  schriftlichen Prüfung:** 3.3.3 Rechner und Netze, Kompetenzen (8) bis (13) (Von-Neumann-Maschine,
  Rechnernetze) und damit auch Brückenkurs 3.1.3 (1) bis (6). Alles andere ist prüfbar, auch 3.3.6
  Projektmanagement ist formal nicht ausgenommen, es taucht im Fundus aber in keinem Aufgabenfeld
  auf.
- **Format:** 270 Minuten einschließlich Auswahlzeit, 120 Bewertungseinheiten. Pflichtteil A
  (30 BE, fünf bis sieben unzusammenhängende Basisaufgaben à 4 bis 6 BE aus allen Bereichen) plus
  drei von vier Wahlaufgaben (je 30 BE): B1 Entwurf und Analyse von Programmen,
  Programmiertechniken; B2 Algorithmen und Datenstrukturen; B3 Automaten, formale Sprachen,
  technische Informatik; B4 Datenbanken, Kryptologie, Datenschutz. Die Schüler wählen selbst.
- **Hilfsmittel:** IQB-Formelsammlung (mathematisch-naturwissenschaftlich), wissenschaftlicher
  Taschenrechner, Rechtschreibwörterbuch. Beides muss im Kurs eingeführt sein.
- **Programmiersprache:** die im Kurs eingeführte, bei uns Java. Keine Fehlerbehandlung für
  Falscheingaben, Importe von Standardbibliotheken müssen nicht angegeben werden.
- **Meta-Regeln aus dem Fundus, die den Unterricht steuern:** Nassi-Shneiderman-Diagramme und
  Pseudocode werden nur gelesen und erläutert, nie selbst erstellt. Binäre Suche, Quicksort und
  Mergesort werden nicht vollständig implementiert verlangt, wohl aber erklärt und im Quelltext
  analysiert. Von den nicht-vergleichsbasierten Sortierverfahren genügt eines. Zufallszahlen kommen
  als vorgegebene Methode. Es kann Aufgaben ohne jede Objektorientierung geben und ebenso reine
  OOP-Aufgaben.
- **Leistungsmessung:** in J1.1, J1.2 und J2.1 je mindestens zwei Klausuren, in J2.2 mindestens
  eine, in der Regel zwei Unterrichtsstunden, alle drei Anforderungsbereiche, Schwerpunkt AFB II.
  Drei GFS über die Kursstufe, Fachwahl der Schüler innerhalb von sechs Wochen nach Beginn J1.
- **Termine 2028:** Zeugnis J2.1 spätestens 28.01.2028, Beginn 4. Halbjahr 31.01.2028,
  schriftliche Prüfung 25.04. bis 11.05.2028, **Informatik Dienstag, 02.05.2028, 9:00 bis 13:30**,
  Nachtermin Mittwoch, 17.05.2028, Wiederbeginn des Unterrichts 15.05.2028, mündliche Prüfungen
  27.06. bis 07.07.2028.

**Operatoren (Aufgabenfundus, Seiten 10 und 11):** AFB I: angeben, berechnen, identifizieren,
kommentieren, nennen. AFB II: anwenden/nutzen/verwenden, beschreiben, bestimmen/ermitteln,
darstellen, durchführen, erklären, erläutern, erstellen, ergänzen/erweitern, implementieren,
modellieren, überführen, untersuchen, vergleichen, zuordnen. AFB III: analysieren, begründen,
bewerten, entwerfen, interpretieren, überprüfen. Die Operatoren werden ab Einheit 1 in jeder
Aufgabenstellung benutzt und in Einheit 12 systematisch geübt.

---

## Bildungsplan-Abgleich mit dem Forum

Das Forum `J2_LF_Inf1` ist nach den Abschnitten 3.3.1 bis 3.3.6 gegliedert. Der Abgleich gegen
den Bildungsplan (alle 3.3-Kompetenzen einzeln geprüft, die interne Arbeitsliste liegt beim Lehrer):

| Bildungsplan | Im Forum | Befund |
|---|---|---|
| 3.3.1.1 Bitebene (1) bis (9): Zweierkomplement, Overflow, Festkomma, Textcodierung, Codes, Huffman, LZW, Hash | **fehlt komplett** | Thema 44 heißt „Daten und Codierung“, enthält aber nur Datenbanken. Abitur 2026 fragte im Pflichtteil Zweierkomplement (A3, A4). |
| 3.3.1.2 Datenstrukturen (1) bis (11): 2D-Arrays, Listen, Bäume, Graphen-Repräsentation, ADT Stack/Queue/Set | **fehlt als Thema** | nur indirekt über Videos in Thema 43 |
| 3.3.1.3 Relationale Datenbanksysteme (1) bis (9) | vollständig | in Thema 44, dort falsch als 3.3.1.2 beschriftet |
| 3.3.2.1 Programmierung (1) bis (22) | vollständig | ein toter Link (kstbb), ein kaputtes Video, „abstrakte Klassen nutzen (?)“ ist keine Frage, sondern Pflicht (18) |
| 3.3.2.2 Algorithmen auf Datenstrukturen (1) bis (10) | vollständig | **(11) P-NP-Frage und (12) Greedy-Näherungen fehlen** |
| 3.3.2.3 Rekursion (1) bis (6) | **fehlt komplett** | wurde unterrichtet (J1.2, Fraktale), aber nicht dokumentiert |
| 3.3.3 Rechner und Netze | vollständig | (8) bis (13) korrekt als nicht prüfungsrelevant markiert, deckt sich mit dem Facherlass 2028 |
| 3.3.4 Datensicherheit (1) bis (10) | vollständig | Punkt 10 verlinkt versehentlich das SQL-Injection-Video |
| 3.3.5 Automaten und Sprachen (1) bis (15) | vollständig | zwei tote Links, Skript Gierhardt als Rückgrat |
| 3.3.6 Projektmanagement (1) bis (4) | vollständig | „nicht fürs Schriftliche relevant“ ist praktisch richtig, formal nicht ausgeschlossen |
| 3.1 Brückenkurs: Hexadezimal, Lauflängencodierung, Vigenère und Kryptoanalyse, One-Time-Pad, Kerckhoffs, asymmetrisches Prinzip | **fehlt** | Abitur 2026 fragte Kerckhoffs (A6). Der Fundus nennt die Schnittmenge Brückenkurs/IMP ausdrücklich als prüfbar. |
| Prüfungsformat, Operatoren, Hilfsmittel | fehlt | Thema 46 „Allgemeines“ hat nur den info-bw-Link; der abgelegte Fundus ist die Fassung 2023, aktuell ist 3.0 von 2025 |

Vier neue Themen sind also nötig (Bitebene, Datenstrukturen, Rekursion, Brückenkurs-Schnittmenge),
zwei Ergänzungen (P/NP und Greedy in 43, Formatinfos in 46) und rund ein Dutzend Linkreparaturen.
Für die Planung heißt das: jede dieser Lücken ist eine eigene Einheit oder ein fester Baustein.

---

## Terminanker, die die Planung binden

| Datum | Termin | Konsequenz für den Kurs |
|---|---|---|
| 15.09.2026 | Erste Kursstunde (Di 1./2.) | Diagnosewoche, GFS-Fachwahl läuft bis Ende Oktober |
| 07.10.2026 | Elternabend J1 | Kursstruktur und die drei Plattformen vorstellen |
| 26. bis 30.10.2026 | Herbstferien | KW44 fällt weg |
| 18.11.2026 | Studieninformationstag J1 | Mi-Block entfällt, KW47 hat nur 4 Stunden |
| 20.01.2027 | **Notenschluss J1.1** | Klausur 2 muss bis 12.01. geschrieben sein |
| 26.01.2027 | Halbjahreskonferenz J1 | |
| 04. bis 09.02.2027 | Fastnachtsferien | KW05 und KW06 haben zusammen nur 6 Stunden |
| 22.03. bis 02.04.2027 | Osterferien | Klausur 3 vorher |
| 06.05.2027 | Christi Himmelfahrt (Do) | KW18 hat 2 Stunden |
| 18. bis 28.05.2027 | Pfingstferien | Einheit 6 endet vorher |
| 28.07.2027 | Letzter Schultag | Di 27.07. ist die letzte Kursstunde |
| 13.09.2027 | Erster Schultag J2 (Annahme: Mo nach Ferienende 11.09.) | |
| 02. bis 06.11.2027 | Herbstferien | |
| 23.12.2027 bis 08.01.2028 | Weihnachtsferien | |
| 28.01.2028 | **Späteste Zeugnisausgabe J2.1** | Klausur 6 bis 11.01. |
| 31.01.2028 | Beginn 4. Halbjahr, Wahl der mündlichen Prüfungsfächer | |
| 24. bis 29.02.2028 | Fastnacht (**Annahme**, Muster wie 2027, Rosenmontag 28.02.) | |
| 13.04.2028 | Gründonnerstag frei, danach Osterferien 18. bis 22.04. | Mi 12.04. ist die letzte Unterrichtsstunde vor dem Abitur |
| **02.05.2028** | **Schriftliches Abitur Informatik**, 9:00 bis 13:30 | |
| 15.05.2028 | Wiederbeginn des Unterrichts J2 | Abschlussphase bis Ende Juni |
| 27.06. bis 07.07.2028 | Mündliche Prüfungen | |

Zwei Annahmen für J2 sind ausdrücklich zu prüfen, sobald der Stundenplan 2027/28 und der
Schulkalender stehen: das Stundenraster (5 Stunden mit 14-täglichem Mi-Block) und die
Fastnachtstage. Eine J2-Studienfahrt ist in der Rechnung nicht enthalten.

---

## Zweijahresüberblick

| Einheit | Zeitraum | Std | Schwerpunkt | Klausur | XP-Edu-Unit |
|---|---|---|---|---|---|
| **E1 Java-Fundament** | KW38-41, 15.09. bis 08.10.2026 | 20 | Methoden, Typen, Strings, Arrays, Codeanalyse, Fehlersuche | | `lk-java-fundament` |
| **E2 Objektorientierung und Spielprojekt** | KW42-49, 13.10. bis 03.12.2026 | 34 | Klassen, Vererbung, Polymorphie, UML, Collections, Spiel nach Panitz | K1 Di 17.11. | `lk-oop-spielprojekt` |
| **E3 Daten und Codierung** | KW50-02, 08.12.2026 bis 14.01.2027 | 16 | Zweierkomplement, Festkomma, Textcodes, Huffman, LZW, RLE, Hash | K2 Di 12.01. | `lk-daten-codierung` |
| **E4 Rekursion** | KW03-06, 19.01. bis 11.02.2027 | 16 | Hanoi, Aufrufbaum, Divide and Conquer, Fraktale, Backtracking | | `lk-rekursion` |
| **E5 Datenstrukturen und Sortieren** | KW07-15, 16.02. bis 15.04.2027 | 36 | Listen, Stack, Queue, Binärbaum, Suchen, Sortieren, O-Notation | K3 Di 16.03. | `lk-datenstrukturen-sortieren` |
| **E6 Graphen** | KW16-19, 20.04. bis 13.05.2027 | 18 | Adjazenz, BFS/DFS, Dijkstra, MST, P gegen NP, Greedy | | `lk-graphen` |
| **E7 Datenbanken** | KW22-27, 01.06. bis 08.07.2027 | 30 | ERM, 3NF, SQL, DBMS, SQL-Injection, JDBC | K4 Di 29.06. | `lk-datenbanken` |
| **E8 Projekt und Versionsverwaltung** | KW28-30, 13.07. bis 27.07.2027 | 12 | Vorgehensmodelle, git, GitHub, TDD, Prototyp | | `lk-projekt-git` |
| **E9 Automaten und formale Sprachen** | KW37-43, 14.09. bis 26.10.2027 | 32 | Grammatiken, EBNF, DEA, Mealy, reguläre Ausdrücke, Kellerautomat, Chomsky | K5 Di 26.10. | `lk-automaten-sprachen` |
| **E10 Rechner** | KW43-47, 27.10. bis 25.11.2027 | 20 | Boolesche Algebra, Schaltnetze, KV, Addierer, Latch; Von-Neumann als Überblick | | `lk-rechner-schaltnetze` |
| **E11 Kryptologie und Datensicherheit** | KW48-02, 30.11.2027 bis 13.01.2028 | 22 | Vigenère bis RSA, Signatur, Hash, PKI, Angriffe, Datenschutz | K6 Di 11.01. | `lk-kryptologie` |
| **E12 Abiturtraining** | KW03-15, 18.01. bis 12.04.2028 | 60 | Pflichtteil A, dann B1 bis B4 mit alten Prüfungen, Simulation, Ferienlernplan | K7 Di 14.03. | `lk-abitur-training` |
| **E13 Nach dem Abitur** | 15.05. bis Ende Juni 2028 | ~18 | Informatik, die nie Platz hatte; Mandelbrot-Abschied; Ausblick | | |
| | **J1: 182, J2: ~152** | | | | |

Die Klausuren zählen in den Stundenzahlen mit. Abitur-Aufgabenfelder: E1, E2, E4, E5 tragen B1;
E5, E6 tragen B2; E9, E10 tragen B3; E7, E11 tragen B4; alle Einheiten liefern Pflichtteil-A-Stoff.

---

## Die Einheiten im Einzelnen

Zu jeder Einheit steht, was der Bildungsplan verlangt, was der Vorgängerkurs an Material hinterlassen
hat, was die XP-Edu-Unit trägt und was im Unterricht bleibt. Arbeitsteilung wie in den
9a-Planungen: **in die App**, was wiederholbar, eindeutig und einzeln überprüfbar ist (Begriffe,
Rechenroutinen, Methoden-Drills, Verfahren von Hand); **in den Unterricht**, was Aushandlung braucht
(Modellieren, Entwurfsentscheidungen begründen, Projektarbeit, Fehlersuche im eigenen Code).

Regeln für den Code-Runner der Schmiede, die jede LK-Unit einhalten muss: `code_run` prüft genau
eine statische Methode über Rückgabewerte, Test-Ein- und Ausgaben nur int, double, String, boolean;
kein `char`, keine Arrays als Testwert; im Rumpf laufen Arrays, `String.split`, `StringBuilder`,
`java.util` mit voll qualifizierten Namen. Mehrere Klassen in einer Datei laufen im
`code_program`-Modus (Ausgabevergleich, Lehrerabnahme). Jede Referenzlösung vor dem Import gegen
Piston prüfen.

### E1 Java-Fundament (KW38 bis KW41, 15.09. bis 08.10.2026, 20 Stunden)

**Bildungsplan:** 3.3.2.1 (1) bis (4), (8), (19) interpretieren, (21), (22); Brückenkurs 3.1.2
(1) bis (8), (12) bis (14); Vorgriff auf 3.3.2.2 (1) lineare Suche.

**Leitidee:** Alle schreiben ab Tag eins Methoden, die gegen Testfälle laufen. Die Einheit gleicht
IMP- und Brückenkurs-Herkunft an, ohne die Starken zu langweilen: wer die Basis-Drills in der
Schmiede durch hat, bekommt die Codeanalyse-Aufgaben im Abiturstil („Beschreiben Sie, was dieser
Code tut, erläutern Sie, warum...“, vgl. Übungsfragen Programmieren im Forum).

**Inhalte:** Methoden mit Parametern und Rückgabe, Signatur; primitive Typen, Wertebereiche und
warum `int` überläuft (Brücke zu E3); Casts; Strings (vergleichen, verketten, Zeichenzugriff,
Umwandlung in Zahlen); Arrays und die Standardalgorithmen (Füllen, Maximum, zweitgrößtes Element,
Summe, Mittelwert, Palindromtest, Histogramm); Compiler- gegen Laufzeitfehler, syntaktisch gegen
semantisch; Debugger und Logging; Struktogramm und Pseudocode lesen; Kommentieren nach Javadoc,
Dokumentation nutzen. Operatoren von Anfang an in den Aufgaben.

**Hausübliches Material:** `Practices2425` (CharIncrement, Prime, Probedivision, Collatz iterativ),
Forum 43 Anhang „Übungsfragen Programmieren“, XP-Edu Unit 43 „LK Java“ (Lektionen 1 und 2).

**XP-Edu `lk-java-fundament`, 6 Lektionen:** (1) Diagnose-Check als Trainingslauf (Quiz und drei
Coding-Aufgaben aus Unit 43); (2) Methoden und Bedingungen (Coding); (3) Schleifen und Arrays
(Coding: Maximum, Summe, zweitgrößtes Element, Mittelwert als double); (4) Strings (Coding:
Palindrom, Zeichen zählen, Cäsar mit Verschiebung, Zeichen als 1-Zeichen-Strings); (5) Typen,
Wertebereiche, Casts (Quiz, Zahl, Wahr/Falsch); (6) Codeanalyse (Freitext mit Stichworten,
Lehrerfreigabe) und Fehlerarten (Zuordnung). Trainingsaufgaben aus jeder Lektion. Die App trägt die
Drills und die Begriffe, der Unterricht die Fehlersuche am Beamer und die Besprechung der
Codeanalysen.

### E2 Objektorientierung und Spielprojekt (KW42 bis KW49, 13.10. bis 03.12.2026, 34 Stunden inkl. K1)

**Bildungsplan:** 3.3.2.1 (5) bis (18), (20); 3.3.6 (2) in Ansätzen (Bibliothek nutzen).

**Leitidee:** Das Spielprojekt nach Panitz („Java will nur spielen“, Framework-Repos
`JavaWillNurSpielen`, `zock_reference`) ist das Rückgrat, wie beim Vorgängerkurs. Der Bildungsplan
wird entlang des Spiels abgearbeitet: Objekte sind Spielfiguren, Vererbung ist die Figurenhierarchie,
Polymorphie ist die Liste aller Zeichenbaren, abstrakte Klassen sind das Framework, Collections sind
die Objektlisten. Parallel läuft die Theorie mit klassischen Beispielen, damit die Abiturform
(UML-Diagramm gegeben, Klasse einordnen, Konstruktor schreiben, wie in B1 2026) sitzt.

**Inhalte:** Klassen, Attribute, Methoden, Konstruktoren, Objektlebenszyklus; Referenz gegen
primitiv, `null` und Nullpointer; Zugriffsmodifikatoren, Kapselung, Zugriffsmethoden; `static`;
Vererbung, `super`, Überschreiben; Polymorphie und sichere Casts (`instanceof`); abstrakte Klassen
und Methoden, Interfaces; generische Typen, `ArrayList`, foreach, ein Lambda; UML-Klassendiagramme
mit Assoziation und Vererbung, auch rekursiv (Composite: Dateisystem aus `Practices2425`); Beziehung
UML zu Code in beide Richtungen.

**Klausur 1 (Di 17.11.2026, KW47):** E1 komplett und Objektorientierung bis Vererbung; Pflichtteil-A-
Stil (Codeanalyse, Methode implementieren, Begriffe) plus eine kleine B1-Aufgabe.

**Hausübliches Material:** `Practices2425` (Fahrzeug/Auto/Fahrrad/Zug, Kriechbar/Rennschnecken,
Medium/Buch/DVD/Zeitschrift, Eintrag/Verzeichnis, BauernhofVerwaltung, OutputQuiz2), `Uebung_HundeObjekt`,
`JavaGame`, Forum 43 (Videos zu Klassen, Vererbung, UML), XP-Edu Unit 43 Lektion 3 (Klasse Bruch).

**XP-Edu `lk-oop-spielprojekt`, 7 Lektionen:** (1) Begriffe der Objektorientierung (Zuordnung,
Lückentext); (2) Klasse Bruch und Klasse Konto als Programm-Aufgaben (mehrere Klassen in einer
Datei, Ausgabevergleich); (3) Referenzen und null (Quiz, Ausgabe vorhersagen als Texteingabe);
(4) Vererbung und Polymorphie: „Was gibt das Programm aus?“ (Texteingabe), Figurenhierarchie
(Programm-Aufgabe); (5) UML lesen (Quiz: Kardinalität, Assoziation gegen Vererbung begründen als
Freitext); (6) Collections und Generics (Coding mit `java.util.ArrayList` voll qualifiziert);
(7) Projektabgabe als Sidequest mit Lehrerfreigabe (Code-Abgabe „zur Bewertung“). Die App trägt
Begriffe, Ausgabevorhersagen und die kleinen Klassen; der Unterricht trägt das Spiel, den Entwurf
und die Präsentation am 01. und 03.12.

### E3 Daten und Codierung (KW50 bis KW02, 08.12.2026 bis 14.01.2027, 16 Stunden inkl. K2 und Rückgabe)

**Bildungsplan:** 3.3.1.1 (1) bis (9); Brückenkurs 3.1.1 (1) bis (4).

**Leitidee:** Die Lücke des Forums wird zur Einheit. Alles hier ist „von Hand durchführen“ und
damit Pflichtteil-A-Material: Zweierkomplement bilden und rechnen, Overflow erklären, Festkomma,
Hexadezimal, Textcodierungen (ASCII, Codepages, Unicode, Escapezeichen), Merkmale von Codes
(Umkehrbarkeit, Präfixfreiheit, feste gegen variable Länge), Lauflängencodierung, Huffman-Baum
bauen und decodieren (erster Kontakt mit einem Baum, Implementierung folgt in E5), LZW von Hand,
Hashfunktionen als Konzept (Fingerprint, Integrität, ISBN-Prüfziffer; Kryptologie folgt in E11).
Am Di 22.12. die hausübliche Weihnachtsstunde: ASCII-Weihnachtsbaum programmieren
(`Xmas2018`, `Weihnachtsbaum.java`), zugleich Vorgriff auf Rekursion.

**Klausur 2 (Di 12.01.2027, KW02):** E2 (UML, Vererbung, Polymorphie, Klasse implementieren) und
E3 ohne Hash. Rückgabe Do 14.01., Notenschluss 20.01.

**XP-Edu `lk-daten-codierung`, 5 Lektionen:** (1) Zahlensysteme und Zweierkomplement (Zahl,
Texteingabe mit Bitfolgen); (2) Rechnen mit endlicher Stellenzahl, Overflow, Festkomma (Zahl, Quiz);
(3) Textcodierung und Codemerkmale (Zuordnung, Wahr/Falsch); (4) Kompression: RLE, Huffman
(Codelänge und Bitzahl als Zahl), LZW (Ausgabefolge als Texteingabe); (5) Hashfunktionen (Quiz,
Prüfziffer als Zahl). Fast alles kann die App tragen; der Unterricht braucht nur die Herleitung des
Zweierkomplements und den gemeinsamen Huffman-Baum an der Tafel.

### E4 Rekursion (KW03 bis KW06, 19.01. bis 11.02.2027, 16 Stunden)

**Bildungsplan:** 3.3.2.3 (1) bis (6); 3.3.1.2 (1) zweidimensionale Arrays.

**Leitidee:** Rekursion als Denkfigur, nicht als Trick: Rekursionsbasis und -schritt, Aufrufbaum
und call stack, Türme von Hanoi, Fakultät, Fibonacci (und warum die naive Fassung explodiert),
Palindrom und Dezimal-zu-Binär rekursiv, Divide and Conquer (Vorgriff auf Mergesort), iterativ
gegen rekursiv bewerten, Fraktale (Koch, Sierpinski, Apfelmännchen als Ausblick) und Backtracking
am Acht-Damen-Problem auf einem 2D-Array. Die Fraktale sind die Verbindung zum IMP-Unterricht
(XP-Edu Unit „Rekursion und Fraktale“ der 9d/9e als Aufwärmmaterial) und zum Mandelbrot-Abschied
am Ende von J2.

**Hausübliches Material:** `Practices2425` (fakRek, Collatz, Dez2BinRek, Palindrom, DreieckRek,
HanoiStatic, HanoiDynamicRoles, ZaehlenRek, rek.java, GridSearch), `Mandelbrot`, IMP9-Fraktale.

**XP-Edu `lk-rekursion`, 4 Lektionen:** (1) Basis und Schritt (Coding: fakultaet, potenz, ggT,
summe der Ziffern); (2) Aufrufbaum und call stack (Sortierung: Reihenfolge der Aufrufe; Zahl:
Anzahl Aufrufe); (3) Hanoi und Divide and Conquer (Coding: hanoiZuege(n), Quiz); (4) Backtracking
und Fraktale (Quiz, Zahl: Anzahl Dreiecke in Stufe n). Unit 43 Lektion 2 wird hierhin geklont.

### E5 Datenstrukturen und Sortieren (KW07 bis KW15, 16.02. bis 15.04.2027, 36 Stunden inkl. K3)

**Bildungsplan:** 3.3.1.2 (2), (3), (7), (8), (9), (10); 3.3.2.2 (1) bis (8).

**Leitidee:** Die zweite Forumslücke wird zur größten Einheit von J1. Reihenfolge nach
Komplexität der Struktur: einfach verkettete Liste selbst implementieren (Einfügen, Löschen,
lineare Suche), darauf Stack und Queue als abstrakte Datentypen mit den Bildungsplan-Operationen
(isEmpty, push, pop, top; enqueue, dequeue, front), generisch; Anwendungsfälle Klammerausdrücke,
Rangierbahnhof, Warteschlangen; Binärbaum implementieren, Inorder/Preorder/Postorder von Hand,
Breiten- und Tiefensuche auf Bäumen; lineare und binäre Suche auf Arrays; elementare
Sortierverfahren beschreiben, von Hand durchführen und implementieren (Bubble, Selection,
Insertion); Mergesort und Quicksort beschreiben und von Hand durchführen, eines implementieren;
ein nicht-vergleichsbasiertes Verfahren; O-Notation, Speicherbedarf, Stabilität, best/worst/
average case. Die Fundus-Metaregeln steuern die Tiefe: Merge- und Quicksort werden im Quelltext
analysiert, nicht in der Klausur implementiert.

**Klausur 3 (Di 16.03.2027, KW11):** E4 und E5 bis zu den elementaren Sortierverfahren.

**Hausübliches Material:** `Practices2425` (List, ListenElement, QueueWithList, MergeSort,
Sortieralgorithmen mit Bubble/Gnome/Bogo, Galtonbrett mit Knoten), `ADT`, `Listen`, Forum 43
(Videos zu Suchen, Traversierung, Sortieren).

**XP-Edu `lk-datenstrukturen-sortieren`, 7 Lektionen:** (1) Verkettete Liste (Quiz zum Aufbau,
Coding: lineare Suche auf Array); (2) Stack und Queue (Texteingabe: Inhalt nach Operationsfolge);
(3) Binärbaum und Traversierungen (Texteingabe: Ausgabefolge); (4) Suchen (Coding: binäre Suche als
Analyse per Quiz, Zahl: Anzahl Vergleiche); (5) elementare Sortierverfahren (Sortierung: Array
nach Durchlauf n, Zahl: Vertauschungen); (6) Mergesort und Quicksort (Sortierung der Rekursions-
schritte, Quiz zu Pivot); (7) Laufzeiten (Zuordnung O-Klassen, Wahr/Falsch zu Stabilität). Der
Unterricht trägt die Implementierung von Liste und Baum in Java und die Laufzeitmessung am
eigenen Code.

### E6 Graphen (KW16 bis KW19, 20.04. bis 13.05.2027, 18 Stunden)

**Bildungsplan:** 3.3.1.2 (4), (5), (6), (10), (11); 3.3.2.2 (9) bis (12).

**Inhalte:** Begriffe (Knoten, Kanten, Grad, Kreis, gerichtet, gewichtet, azyklisch), Bäume als
spezielle Graphen; Adjazenzmatrix und Adjazenzliste, Umwandlung; Breiten- und Tiefensuche auf
Graphen von Hand und für reale Probleme (Erreichbarkeit, kürzester Weg in Kantenzahl, topologische
Sortierung wie in B2 2026); Dijkstra mit Tabelle; Prim oder Kruskal für den minimalen Spannbaum;
ein Graphenalgorithmus implementiert mit Bibliothek oder eigenem Adjazenzlisten-Graphen; die
P-NP-Frage als offene Frage mit Beispielen (Handlungsreisender, Rucksack) und Greedy-Näherungen
an 4-Farben-Problem und Dominating Sets. Die beiden zuletzt genannten Punkte fehlen im Forum.

**XP-Edu `lk-graphen`, 5 Lektionen:** (1) Begriffe und Darstellungen (Zuordnung, Texteingabe:
Matrix aus Liste); (2) BFS und DFS (Texteingabe: Besuchsreihenfolge); (3) Dijkstra (Texteingabe:
Distanzen, Zahl: Weglänge); (4) Spannbäume (Zahl: Gesamtgewicht, Quiz Prim gegen Kruskal);
(5) P gegen NP und Greedy (Quiz, Wahr/Falsch). Die Handdurchführungen trägt die App komplett.

### E7 Datenbanken (KW22 bis KW27, 01.06. bis 08.07.2027, 30 Stunden inkl. K4)

**Bildungsplan:** 3.3.1.3 (1) bis (9); 3.3.4 (8) SQL-Injection als Vorgriff.

**Inhalte:** Komponenten eines Datenbanksystems; relationales Modell und Begriffe; Schlüssel;
ER-Diagramm und UML-Klassendiagramm als Modellierungssprachen, Kardinalitäten, n:m-Auflösung;
Überführung Diagramm zu Schema und zurück; Normalisierung bis 3NF; ein DBMS praktisch (SQLite mit
DB Browser, alternativ phpMyAdmin-Demo); SQL: Projektion, Selektion, Verbund über WHERE,
Gruppierung, Aggregatfunktionen, Unterabfragen gegen ORDER BY mit LIMIT (B4 2026); INSERT, UPDATE,
DELETE; SQL-Injection als Angriff und die Gegenmaßnahme (Prepared Statements); Anbindung aus Java
per JDBC als Brücke zum Projekt in E8. Wie beim Vorgängerkurs liegt Datenbanken am Ende von J1.

**Klausur 4 (Di 29.06.2027, KW26):** E5 (höhere Sortierverfahren, Laufzeit), E6 und E7 bis zu
den Abfragen.

**Hausübliches Material:** Forum 44 (ERMTheorie.pdf von Gierhardt, Normalisierungsvideos,
SQL-Trainer perschke.info, sql.hauptquartier.eu, SQL-Insekten).

**XP-Edu `lk-datenbanken`, 6 Lektionen:** (1) Begriffe und Komponenten (Zuordnung); (2) ERM lesen
und Kardinalitäten (Quiz); (3) Schema aus Diagramm (Lückentext: Fremdschlüssel setzen);
(4) Normalformen (Wahr/Falsch, Quiz); (5) SQL lesen: Ergebnis vorhersagen (Texteingabe, Zahl) und
SQL schreiben (Freitext mit Stichworten, Lehrerfreigabe); (6) SQL-Injection (Quiz). Abfragen
gegen eine echte Datenbank bleiben im Unterricht, weil die App keine SQL-Ausführung hat.

### E8 Projekt und Versionsverwaltung (KW28 bis KW30, 13.07. bis 27.07.2027, 12 Stunden)

**Bildungsplan:** 3.3.6 (1) bis (4).

**Leitidee:** Die letzten drei Wochen vor den Sommerferien sind bei allen Kursen unruhig; deshalb
liegt hier die Einheit, die vom Tun lebt. Projektbegriffe und Vorgehensmodelle (Wasserfall,
iterativ, agil mit User Stories und Sprint), Versionsverwaltung mit git (init, add, commit, branch,
merge, Konflikt) und GitHub (das Kurs-Repo wird ab jetzt von den Schülern mitgepflegt),
testgetriebene Entwicklung mit JUnit an einer Klasse aus E5, dann ein Prototyp in Zweiergruppen,
der Datenbank (E7) und Objektorientierung (E2) verbindet, mit Abnahme am 27.07. Damit ist 3.3.6
erledigt, bevor J2 beginnt, und der Kurs kann im Herbst mit einem Projektabschluss als GFS-Angebot
weiterarbeiten.

**XP-Edu `lk-projekt-git`, 3 Lektionen:** (1) Projektbegriffe und Vorgehensmodelle (Zuordnung,
Quiz); (2) git-Befehle (Lückentext, Sortierung eines Workflows); (3) TDD-Zyklus (Sortierung,
Wahr/Falsch). Das Projekt selbst läuft ausschließlich im Unterricht und im Repo.

### E9 Automaten und formale Sprachen (KW37 bis KW43, 14.09. bis 26.10.2027, 32 Stunden inkl. K5)

**Bildungsplan:** 3.3.5 (1) bis (15).

**Inhalte:** Anwendungsbereiche (Kennzeichen, URLs, Rechenausdrücke, Protokolle); Definition
formaler Sprachen, Syntax gegen Semantik; Grammatiken mit Terminalen, Nichtterminalen, Startsymbol,
Produktionen, auch als EBNF; Syntaxdiagramme entwerfen; Wortproblem und Ableitungen; endliche
Automaten mit und ohne Ausgabe (Mealy), Zustandsdiagramm und -tabelle ineinander überführen,
Implementierung eines DEA in Java (Skript Gierhardt 3.5); reguläre Sprachen dreifach beschrieben
(DEA, reguläre Grammatik, regulärer Ausdruck) und ihre Grenzen; kontextfreie Sprachen mit
Kellerautomat und Grammatik, Klammersprachen, Grenzen (a^n b^n c^n wie in B3 2026);
Chomsky-Hierarchie; Einsatzbereiche (Substringsuche, GUI-Zustände, Protokolle, Parser).

**Klausur 5 (Di 26.10.2027, KW43):** E9 komplett, nach dem Vorbild von B3.

**Hausübliches Material:** Forum 79 (Skript Gierhardt „Formale Sprachen und Automatentheorie“,
51 Seiten, inf-schule.de zu Kellerautomaten), Abituraufgaben 2019 B3, 2023 bis 2026 B3.

**XP-Edu `lk-automaten-sprachen`, 6 Lektionen:** (1) Sprachen, Alphabete, Wörter (Wahr/Falsch:
gehört das Wort zur Sprache); (2) Grammatiken und Ableitungen (Sortierung der Ableitungsschritte,
Lückentext EBNF); (3) Syntaxdiagramme (Quiz: welche Wörter erzeugt das Diagramm); (4) DEA und
Mealy (Texteingabe: Endzustand, Ausgabewort); (5) reguläre Ausdrücke (Wahr/Falsch, Texteingabe);
(6) Kellerautomat und Chomsky (Zuordnung, Quiz). Der Unterricht trägt das Entwerfen von Automaten
und Grammatiken zu neuen Sprachen.

### E10 Rechner (KW43 bis KW47, 27.10. bis 25.11.2027, 20 Stunden)

**Bildungsplan:** 3.3.3 (1) bis (7) prüfungsrelevant; (8) bis (13) als Überblick.

**Inhalte:** Boolesche Algebra (Werte, Verknüpfungen, Basis), Wahrheitstafeln, Schaltnetze aus
Gattern entwerfen und untersuchen (Simulator: Logisim Evolution oder Digital), Rechengesetze und
De Morgan, DNF und KNF (auch kanonisch), KV-Diagramme bis vier Variablen, Halb- und Volladdierer,
Mehrbitaddierer im Simulator, SR- und D-Latch als 1-Bit-Speicher. Als Überblick ohne
Prüfungsanspruch (4 Stunden): Von-Neumann-Maschine mit Human Resource Machine, paketorientierte
Übertragung und Schichtenmodell in einer Stunde, weil die Schüler Netze aus dem Alltag kennen und
das Bild vom Rechner sonst unvollständig bleibt.

**Hausübliches Material:** Forum 77 (Hintergrund.pdf von Schaller, RP Freiburg 2011, 46 Seiten,
CC BY-NC-SA; Videos zu Schaltnetzen, Addierern, Flipflops).

**XP-Edu `lk-rechner-schaltnetze`, 5 Lektionen:** (1) Gatter und Wahrheitstafeln (Texteingabe:
Ausgangsspalte); (2) Rechengesetze und De Morgan (Lückentext); (3) Normalformen (Lückentext,
Quiz); (4) KV-Diagramme (Texteingabe: Minimalterm); (5) Addierer und Latch (Zuordnung,
Wahr/Falsch). Der Unterricht trägt den Simulator.

### E11 Kryptologie und Datensicherheit (KW48 bis KW02, 30.11.2027 bis 13.01.2028, 22 Stunden inkl. K6)

**Bildungsplan:** 3.3.4 (1) bis (10); Brückenkurs 3.1.4 (1) bis (9).

**Inhalte:** Die Brückenkurs-Schnittmenge zuerst, weil sie im Pflichtteil vorkommt (2026: A6
Kerckhoffs, B4.3 Vigenère mit Schlüssel und Salt): Transposition gegen Substitution, Vigenère
durchführen und angreifen (Kasiski-Idee, Häufigkeiten), One-Time-Pad und warum es absolut sicher
ist, Kerckhoffs. Dann symmetrisch gegen asymmetrisch (Schlüsselverwaltung, Tausch,
Geschwindigkeit), Diffie-Hellman als Farbenbild und mit kleinen Zahlen, RSA-Idee und
Einwegfunktionen mit exponentiellen Angriffen, Signieren mit asymmetrischer Verschlüsselung,
kryptologische Hashfunktionen (Fingerprint, Signatur, Passworthashes mit Salt), kryptographische
Ziele, Public-Key-Infrastrukturen und Vertrauensmodelle (hierarchisch, Web of Trust), Angriffe
(SQL-Injection aus E7, DDoS, Phishing, Man in the Middle), Maßnahmen zu Datensicherheit und
Datenschutz, Szenarien mit Massendaten bewerten.

**Klausur 6 (Di 11.01.2028, KW02):** E10 und E11; Rückgabe vor der Zeugnisausgabe 28.01.

**Hausübliches Material:** Forum 78 (inf-schule.de, Videos zu Signatur, PKI, MITM), Karte 3 der
Abschlussstunde „Greatest Hits“ (Diffie-Hellman mit Farben).

**XP-Edu `lk-kryptologie`, 6 Lektionen:** (1) Klassische Verfahren (Texteingabe: Vigenère ver- und
entschlüsseln); (2) OTP und Kerckhoffs (Quiz, Wahr/Falsch); (3) symmetrisch gegen asymmetrisch
(Zuordnung, Zahl: Diffie-Hellman mit kleinen Zahlen); (4) Signatur und Hash (Sortierung des
Ablaufs, Quiz); (5) PKI und Zertifikate (Quiz); (6) Angriffe und Datenschutz (Zuordnung, Freitext
zur Bewertung eines Szenarios mit Lehrerfreigabe).

### E12 Abiturtraining (KW03 bis KW15, 18.01. bis 12.04.2028, 60 Stunden inkl. K7)

**Leitidee:** Nicht „Wiederholung“, sondern Training nach der Struktur der Prüfung. Januar bis
Zeugnis: Pflichtteil A, also das Format (120 BE, 270 Minuten, Wahl 3 aus 4), die Operatoren mit
ihren Anforderungsbereichen, die Aufgabentypen des Fundus (Standardalgorithmen erläutern,
Array- und String-Methoden, Laufzeit analysieren, Kardinalitäten, Rekursion nachvollziehen,
SQL, Begriffe, Schaltungen, Wortproblem, Codierung) und die Hilfsmittel (Formelsammlung des IQB,
Taschenrechner). Februar bis April: die vier Wahlfelder mit den Abiturprüfungen 2023 bis 2027
(neues Format) und den älteren als Steinbruch, jeweils erst unter Zeitdruck lösen, dann am
Erwartungshorizont korrigieren, dann die eigene Wahlstrategie (welche drei B-Felder) begründen.

**Klausur 7 (Di 14.03.2028, KW11):** Abitursimulation. Wenn die Schulleitung eine Verlängerung
über zwei Stunden hinaus erlaubt (der Facherlass sagt „in der Regel zwei Unterrichtsstunden“),
270 Minuten mit vollständigem Satz; sonst A plus eine B-Aufgabe in zwei Stunden und die übrigen
B-Aufgaben als Hausübung mit Selbstkorrektur.

**Ferienlernplan 2028:** Übergabe am Mi 12.04. Vorlage ist der Lernplan `InfAbi26`
(drei Wochen, ein Thema pro Tag, Links auf Forum, Videos und alte Prüfungen). Zeitraum 13.04. bis
01.05.2028, Klausur Di 02.05. Statt der Forumslinks zeigt der neue Plan auf das GitHub-Repo und
die XP-Edu-Trainingsarena.

**XP-Edu `lk-abitur-training`:** keine neuen Inhalte, sondern die Trainingsarena: aus jeder
LK-Unit die als Training markierten Aufgaben, dazu eine Lektion „Operatoren und Format“
(Zuordnung Operator zu AFB, Quiz zum Ablauf) und eine Lektion mit Pflichtteil-Aufgaben der
Abiture 2023 bis 2027 in App-Form (Coding, Texteingabe, Zahl). Battle-Pass und Ranking pro Kurs
sind hier das Motivationsmittel für die Durststrecke Februar bis April.

### E13 Nach dem Abitur (15.05. bis Ende Juni 2028, rund 18 Stunden)

Wie beim Vorgängerkurs: die Stunde „Informatik, die wir nie geschafft haben“ (Halteproblem,
P gegen NP, Public-Key, Sprachmodelle), der Mandelbrot-Abschied als letzte Stunde, dazwischen
Ausblick auf Studium und Ausbildung. Beide Stundenentwürfe liegen fertig im Repo
(`informatik/inf-lk/abschluss/`). Sollte ein Schüler eine zusätzliche mündliche Prüfung
bekommen, wird diese Zeit für die Vorbereitung genutzt.

---

## Wochenplan J1 (2026/27, gerechnet)

| KW | Montag | Std | Einheit | Inhalt |
|---|---|---|---|---|
| 38 | 14.09.2026 | 6 | E1 | Kursstart, Diagnose in der Schmiede, Methoden mit Parametern und Rückgabe, Testfälle |
| 39 | 21.09. | 4 | E1 | Datentypen, Wertebereiche, Casts, Strings |
| 40 | 28.09. | 6 | E1 | Arrays und Array-Algorithmen, erste Codeanalysen |
| 41 | 05.10. | 4 | E1 | Fehlerarten, Debugger, Struktogramm lesen, Javadoc; Abschluss E1 |
| 42 | 12.10. | 6 | E2 | Klassen, Objekte, Konstruktoren, Kapselung; Spiel-Framework kennenlernen |
| 43 | 19.10. | 4 | E2 | Referenzen, null, static; erste Spielobjekte |
| 44 | 26.10. | 0 | | Herbstferien |
| 45 | 02.11. | 4 | E2 | Vererbung, UML-Klassendiagramm |
| 46 | 09.11. | 6 | E2 | Polymorphie, abstrakte Klassen, Interfaces, Casts; Wiederholung |
| 47 | 16.11. | 4 | E2 | **K1 Di 17.11.**; Mi Studieninformationstag; Do Projektarbeit |
| 48 | 23.11. | 6 | E2 | Collections, foreach, Generics, Lambda; Composite (rekursive Assoziation) |
| 49 | 30.11. | 4 | E2 | Abnahme und Präsentation Spielprojekt, Rückgabe K1 |
| 50 | 07.12. | 6 | E3 | Zweierkomplement, Rechnen, Overflow, Festkomma, Hexadezimal |
| 51 | 14.12. | 4 | E3 | Textcodierung, Codemerkmale, Huffman, Lauflängencodierung |
| 52 | 21.12. | 2 | E3 | LZW; Di 22.12. Weihnachtsprogrammieren |
| 53, 01 | | 0 | | Weihnachtsferien bis 08.01. |
| 02 | 11.01.2027 | 4 | E3 | **K2 Di 12.01.**; Do Hashfunktionen, Rückgabe |
| 03 | 18.01. | 6 | E4 | Rekursionsbasis und -schritt, Fakultät, Fibonacci, Aufrufbaum, call stack |
| 04 | 25.01. | 4 | E4 | Hanoi, Divide and Conquer, Palindrom und Binärdarstellung rekursiv |
| 05 | 01.02. | 4 | E4 | iterativ gegen rekursiv, Laufzeit; Fraktale (Koch, Sierpinski) |
| 06 | 08.02. | 2 | E4 | Backtracking (Acht Damen), 2D-Arrays; Fastnacht bis 09.02. |
| 07 | 15.02. | 6 | E5 | Verkettete Liste implementieren, lineare Suche |
| 08 | 22.02. | 4 | E5 | Stack und Queue als ADT, generisch; Klammerausdrücke, Rangierbahnhof |
| 09 | 01.03. | 6 | E5 | Binärbaum implementieren, Traversierungen, BFS/DFS auf Bäumen |
| 10 | 08.03. | 4 | E5 | Binäre Suche, Bubble-, Selection-, Insertionsort; Wiederholung |
| 11 | 15.03. | 6 | E5 | **K3 Di 16.03.**; Mi/Do Mergesort |
| 12, 13 | | 0 | | Osterferien 22.03. bis 02.04. |
| 14 | 05.04. | 4 | E5 | Quicksort, ein höheres Verfahren implementieren, Rückgabe K3 |
| 15 | 12.04. | 6 | E5 | Countingsort/Radixsort, O-Notation, Stabilität, best/worst/average |
| 16 | 19.04. | 4 | E6 | Graphenbegriffe, Adjazenzmatrix und -liste |
| 17 | 26.04. | 6 | E6 | BFS und DFS auf Graphen, Dijkstra |
| 18 | 03.05. | 2 | E6 | Prim und Kruskal; Do Himmelfahrt |
| 19 | 10.05. | 6 | E6 | Graphenalgorithmus implementieren, P gegen NP, Greedy-Näherungen |
| 20, 21 | | 0 | | Pfingstferien 18. bis 28.05. |
| 22 | 31.05. | 4 | E7 | Datenbanksysteme, relationales Modell, Schlüssel |
| 23 | 07.06. | 6 | E7 | ERM und UML, Kardinalitäten, Überführung ins Schema |
| 24 | 14.06. | 4 | E7 | Normalformen bis 3NF, SQLite praktisch |
| 25 | 21.06. | 6 | E7 | SQL-Abfragen: Projektion, Selektion, Verbund, Gruppierung, Aggregate |
| 26 | 28.06. | 4 | E7 | **K4 Di 29.06.**; Do SQL-Manipulation |
| 27 | 05.07. | 6 | E7 | SQL-Injection und Prepared Statements, JDBC, Rückgabe K4 |
| 28 | 12.07. | 4 | E8 | Projektbegriffe, Vorgehensmodelle, User Stories; git-Grundlagen |
| 29 | 19.07. | 6 | E8 | GitHub-Workflow im Kurs-Repo, TDD mit JUnit, Prototyp |
| 30 | 26.07. | 2 | E8 | Di 27.07. Abnahme der Prototypen, Jahresabschluss |
| | | **182** | | |

## Wochenplan J2 (2027/28, geschätzt)

| KW | Montag | Std | Einheit | Inhalt |
|---|---|---|---|---|
| 37 | 13.09.2027 | 6 | E9 | Formale Sprachen: Alphabet, Wort, Sprache, Syntax gegen Semantik, Anwendungen |
| 38 | 20.09. | 4 | E9 | Grammatiken, Produktionen, Ableitungen, Wortproblem |
| 39 | 27.09. | 6 | E9 | EBNF, Syntaxdiagramme |
| 40 | 04.10. | 4 | E9 | Endliche Automaten, Zustandsdiagramm und -tabelle, Mealy |
| 41 | 11.10. | 6 | E9 | Reguläre Sprachen dreifach: DEA, Grammatik, regulärer Ausdruck; DEA in Java |
| 42 | 18.10. | 4 | E9 | Grenzen regulärer Sprachen, Kellerautomat, kontextfrei, Chomsky |
| 43 | 25.10. | 6 | E9/E10 | **K5 Di 26.10.**; Mi/Do Boolesche Algebra, Gatter, Wahrheitstafeln |
| 44 | 01.11. | 0 | | Herbstferien |
| 45 | 08.11. | 6 | E10 | Schaltnetze im Simulator, De Morgan, DNF und KNF |
| 46 | 15.11. | 4 | E10 | KV-Diagramme, Minimalform |
| 47 | 22.11. | 6 | E10 | Halb- und Volladdierer, Mehrbitaddierer, Latch; Von-Neumann und Netze im Überblick |
| 48 | 29.11. | 4 | E11 | Vigenère, Kryptoanalyse, One-Time-Pad, Kerckhoffs |
| 49 | 06.12. | 6 | E11 | Symmetrisch gegen asymmetrisch, Diffie-Hellman, RSA-Idee, Einwegfunktionen |
| 50 | 13.12. | 4 | E11 | Hashfunktionen, Signaturen, kryptographische Ziele |
| 51 | 20.12. | 4 | E11 | PKI, Zertifikate, Vertrauensmodelle; Angriffe |
| 52, 01 | | 0 | | Weihnachtsferien bis 08.01.2028 |
| 02 | 10.01.2028 | 4 | E11 | **K6 Di 11.01.**; Do Datenschutz und Massendaten bewerten |
| 03 | 17.01. | 6 | E12 | Prüfungsformat, Operatoren, Aufgabentypen des Pflichtteils; Rückgabe K6 |
| 04 | 24.01. | 4 | E12 | Pflichtteil-Training (Codierung, Rekursion, SQL, Automaten); Zeugnis 28.01. |
| 05 | 31.01. | 6 | E12 | B1: Programmiertechniken und OOP mit den Prüfungen 2023 bis 2027 |
| 06 | 07.02. | 4 | E12 | B1: Rekursion, Sortieren, Aufwandsanalyse |
| 07 | 14.02. | 6 | E12 | B2: Listen, Bäume, Codeanalyse |
| 08 | 21.02. | 2 | E12 | B2: Graphen; Fastnacht ab Do 24.02. (Annahme) |
| 09 | 28.02. | 4 | E12 | B3: Automaten und Sprachen |
| 10 | 06.03. | 4 | E12 | B3: technische Informatik; Vorbereitung der Simulation |
| 11 | 13.03. | 6 | E12 | **K7 Di 14.03. Abitursimulation**; Mi/Do B4 Datenbanken |
| 12 | 20.03. | 4 | E12 | B4: Kryptologie und Datenschutz; Rückgabe K7, Fehleranalyse |
| 13 | 27.03. | 6 | E12 | Training der eigenen Schwachstellen, Wahlstrategie B |
| 14 | 03.04. | 4 | E12 | Teilaufgaben unter Zeitdruck, Zeitmanagement |
| 15 | 10.04. | 4 | E12 | Letzte Wiederholung, Übergabe Ferienlernplan (Mi 12.04.) |
| 16, 17 | | 0 | | Gründonnerstag, Osterferien, ab 25.04. schriftliche Prüfungen |
| | | **134** | | |
| 20 bis 25 | 15.05. bis 23.06. | ~18 | E13 | Nach dem Abitur: Greatest Hits, Ausblick, Mandelbrot-Abschied |

---

## Klausurplan und GFS

| Nr. | Termin | Halbjahr | Stoff | Form |
|---|---|---|---|---|
| K1 | Di 17.11.2026 | J1.1 | E1, Objektorientierung bis Vererbung | 2 Std, A-Stil plus kleine B1 |
| K2 | Di 12.01.2027 | J1.1 | E2, E3 ohne Hash | 2 Std |
| K3 | Di 16.03.2027 | J1.2 | E4, E5 bis elementare Sortierverfahren | 2 Std |
| K4 | Di 29.06.2027 | J1.2 | E5 höhere Verfahren, E6, E7 bis Abfragen | 2 Std |
| K5 | Di 26.10.2027 | J2.1 | E9 | 2 Std, nach B3-Muster |
| K6 | Di 11.01.2028 | J2.1 | E10, E11 | 2 Std |
| K7 | Di 14.03.2028 | J2.2 | Abitursimulation | 270 min, falls genehmigt |

Alle Klausuren liegen auf dem Dienstagsblock (1./2. Stunde), damit Oken-Schüler und Nachschreiber
planbar sind. Die Termine müssen in den iServ-Klausurplan und gegen die Klausuren der anderen
Leistungsfächer abgestimmt werden.

**GFS-Angebote** (Schüler wählen ihre GFS-Fächer bis Ende Oktober 2026): Sortierverfahren im
Laufzeitvergleich mit eigener Messung (E5), Turingmaschine und Berechenbarkeit (E9), RSA vollständig
mit Zahlentheorie (E11), Git und Softwareentwicklung im Team (E8), maschinelles Lernen als Erweiterung
von E13, Netzwerkprotokolle mit Wireshark (E10-Überblick), Datenschutzfall der eigenen Wahl (E11).
Je Halbjahr höchstens zwei GFS im Kurs, damit sie nicht in die Klausurwochen fallen.

---

## Die drei Plattformen

**iServ-Forum (Materialsammlung und Abiturprüfungen).** Bleibt der Ort für alles, was nicht
öffentlich sein darf: die Prüfungs-PDFs, Skripte Dritter, Erwartungshorizonte. Die Gruppe `J1_LF_Inf1` mit
eigenem Forum existiert seit dem 12.09.2026, Forum 22 bleibt als Archiv stehen. Neue Themen: Bitebene,
Datenstrukturen, Rekursion, Brückenkurs-Schnittmenge, „So läuft das Abitur 2028“. Dort auch der
Abiturjahrgang 2026 (liegt bei Marek aus der Erstkorrektur) und der Fundus 3.0.

**XP-Edu-Schmiede (Üben).** Ein Kurs „Informatik LK J1“ (Fach Informatik, Schuljahr 2026/2027) mit
den zwölf Units oben. Die Schüler kommen per iServ-Login hinein; damit sie nach dem ersten Login
sofort den Kurs sehen, braucht der Kurs eine zugeordnete iServ-Gruppe (die es für J1 noch nicht
gibt, siehe offene Punkte) und die beiden Schalter `current_schuljahr` und `sso.auto_enroll`.
Die Units entstehen jeweils in der Woche vor der Einheit nach der Authoring-Spezifikation
(`/authoring/spec.md`), Unit 43 „LK Java“ wird als Startpunkt in den Kurs geklont.

**GitHub (Unterrichtsdokumentation).** Dieses Repo:

```
inf-lk-2028/
  README.md                 Kursüberblick, Plattformen, Regeln
  planung/                  diese Zweijahresplanung, Klausurplan (ohne Namen)
  E01-java-fundament/       je Einheit: stunden.md (Datum, Thema, Aufgaben), material/, code/
  E02-oop-spielprojekt/
  ...
  E12-abitur-training/      Lernplan 2028 als GitHub-Page (Vorlage InfAbi26), Links auf KM-Dokumente
  links.md                  geprüfte Linksammlung aus dem Forum, nach Bildungsplan sortiert
```

Regeln: keine Schülernamen, keine Noten, keine Prüfungs-PDFs des Kultusministeriums (nur Links
auf die öffentlichen Dokumente wie Fundus und Facherlass), fremde Skripte nur bei passender Lizenz
(Hintergrund.pdf ist CC BY-NC-SA, Gierhardt-Skripte nicht ohne Rückfrage). Ab E8 committen die
Schüler ihre Prototypen in eigene Ordner. `stunden.md` je Einheit ist zugleich die Vorlage für
den Lehrstoff im WebUntis-Klassenbuch.

---

## Offene Punkte

1. **Vor dem 15.09.2026: Kursliste und Vorwissen.** Wer kommt aus IMP, wer aus dem Brückenkurs,
   wer vom Oken-Gymnasium? WebUntis hat die Liste. Die Diagnose in KW38 entscheidet, ob E1 auf drei
   Wochen verkürzt wird (dann bekommt E2 die Zeit für das Spielprojekt).
2. **iServ-Gruppe und Forum für den neuen Kurs anlegen** (bisher gibt es nur `j2.lf.inf1` vom
   Vorgängerkurs). Erst dann kann XP-Edu den Kurs automatisch zuordnen.
3. **Klausurtermine** in den iServ-Klausurplan eintragen und gegen die anderen Leistungsfächer prüfen;
   Klausur 7 als 270-Minuten-Simulation mit der Schulleitung klären.
4. **J2-Annahmen prüfen**, sobald Stundenplan und Kalender 2027/28 stehen: Stundenraster, Fastnacht,
   Studienfahrt, Notenschluss J2.1 und J2.2.
5. **Werkzeuge festlegen:** JDK-Version und IDE (BlueJ für den Einstieg, danach IntelliJ oder
   VS Code), SQLite mit DB Browser, Logisim Evolution, JUnit. Der Code-Runner der Schmiede läuft
   mit Java 15, Sprachfeatures darüber hinaus gehören nicht in die Drills.
6. **GFS-Fachwahl** der Schüler bis Ende Oktober einsammeln und die GFS-Termine in den Plan legen.
7. **Hilfsmittel einführen:** IQB-Formelsammlung und Taschenrechner spätestens in E5 (Laufzeiten,
   Logarithmen), damit sie im Abitur vertraut sind.
8. **Forum-Arbeitsliste abarbeiten** (tote Links, Doppel-Uploads, fehlende Themen); die geprüfte
   Linksammlung liegt in `links.md`.
