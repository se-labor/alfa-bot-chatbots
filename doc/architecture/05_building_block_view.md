# Bausteinsicht

To be created

<!--
**Inhalt**

Diese Sicht zeigt die statische Zerlegung des Systems in Bausteine sowie
deren Beziehungen. Beispiele für Bausteine sind unter anderem:

-   Module

-   Komponenten

-   Subsysteme

-   Klassen

-   Interfaces

-   Pakete

-   Bibliotheken

-   Frameworks

-   Schichten

-   Partitionen

-   Tiers

-   Funktionen

-   Makros

-   Operationen

-   Datenstrukturen

-   …

Diese Sicht sollte in jeder Architekturdokumentation vorhanden sein. In
der Analogie zum Hausbau bildet die Bausteinsicht den *Grundrissplan*.

**Motivation**

Behalten Sie den Überblick über den Quellcode, indem Sie die statische
Struktur des Systems durch Abstraktion verständlich machen.

Damit ermöglichen Sie Kommunikation auf abstrakterer Ebene, ohne zu
viele Implementierungsdetails offenlegen zu müssen.

**Form**

Die Bausteinsicht ist eine hierarchische Sammlung von Blackboxen und
Whiteboxen (siehe Abbildung unten) und deren Beschreibungen.

![Hierarchie in der Bausteinsicht](images/05_building_blocks-DE.png)

**Ebene 1** ist die Whitebox-Beschreibung des Gesamtsystems, zusammen
mit Blackbox-Beschreibungen der darin enthaltenen Bausteine.

**Ebene 2** zoomt in einige Bausteine der Ebene 1 hinein. Sie enthält
somit die Whitebox-Beschreibungen ausgewählter Bausteine der Ebene 1,
jeweils zusammen mit Blackbox-Beschreibungen darin enthaltener
Bausteine.

**Ebene 3** zoomt in einige Bausteine der Ebene 2 hinein, usw.

Siehe [Bausteinsicht](https://docs.arc42.org/section-5/) in der
online-Dokumentation (auf Englisch!).

-->

<!--
![Hierarchie in der Bausteinsicht](images/05_building_blocks-DE.png) 
-->

## Ebene 1: Rasa Chatbot und Backend-Dienste

Die Backenddienste von ALFA-Bot bestehen aus:

* Der Medienverwaltung und Projektwebseite innerhalb eines Wordpress-CMS auf alfacms.se-labor.de
* Einer SpringBoot API 
* Einer Instanz von Rasa X, die den Chatbot von Rasa Open Source enthält
* Einem Rasa Custom Action Server

<!--
An dieser Stelle beschreiben Sie die Zerlegung des Gesamtsystems anhand
des nachfolgenden Whitebox-Templates. Dieses enthält:

-   Ein Übersichtsdiagramm

-   die Begründung dieser Zerlegung

-   Blackbox-Beschreibungen der hier enthaltenen Bausteine. Dafür haben
    Sie verschiedene Optionen:

    -   in *einer* Tabelle, gibt einen kurzen und pragmatischen
        Überblick über die enthaltenen Bausteine sowie deren
        Schnittstellen.

    -   als Liste von Blackbox-Beschreibungen der Bausteine, gemäß dem
        Blackbox-Template (siehe unten). Diese Liste können Sie, je nach
        Werkzeug, etwa in Form von Unterkapiteln (Text), Unter-Seiten
        (Wiki) oder geschachtelten Elementen (Modellierungswerkzeug)
        darstellen.

-   (optional:) wichtige Schnittstellen, die nicht bereits im
    Blackbox-Template eines der Bausteine erläutert werden, aber für das
    Verständnis der Whitebox von zentraler Bedeutung sind. Aufgrund der
    vielfältigen Möglichkeiten oder Ausprägungen von Schnittstellen
    geben wir hierzu kein weiteres Template vor. Im schlimmsten Fall
    müssen Sie Syntax, Semantik, Protokolle, Fehlerverhalten,
    Restriktionen, Versionen, Qualitätseigenschaften, notwendige
    Kompatibilitäten und vieles mehr spezifizieren oder beschreiben. Im
    besten Fall kommen Sie mit Beispielen oder einfachen Signaturen
    zurecht.
-->


<!--
### &lt;Name Blackbox 1>

Beschreiben Sie die &lt;Blackbox 1> anhand des folgenden Blackbox-Templates:

- Zweck/Verantwortung

- Schnittstelle(n), sofern diese nicht als eigenständige Beschreibungen herausgezogen sind. Hierzu gehören eventuell
  auch Qualitäts- und Leistungsmerkmale dieser Schnittstelle.

- (Optional) Qualitäts-/Leistungsmerkmale der Blackbox, beispielsweise Verfügbarkeit, Laufzeitverhalten o. Ä.

- (Optional) Ablageort/Datei(en)

- (Optional) Erfüllte Anforderungen, falls Sie Traceability zu Anforderungen benötigen.

- (Optional) Offene Punkte/Probleme/Risiken

*&lt;Zweck/Verantwortung>*

*&lt;Schnittstelle(n)>*

*&lt;(Optional) Qualitäts-/Leistungsmerkmale>*

*&lt;(Optional) Ablageort/Datei(en)>*

*&lt;(Optional) Erfüllte Anforderungen>*

*&lt;(optional) Offene Punkte/Probleme/Risiken>*

### &lt;Name Blackbox 2>

*&lt;Blackbox-Template>*

### &lt;Name Blackbox n>

*&lt;Blackbox-Template>*

### &lt;Name Schnittstelle 1>

…

### &lt;Name Schnittstelle m>

-->

## Ebene 2: App
Die App wird seit Mai 2022 mit Angular entwickelt und besteht aus einer Chatview. Diese hält pro Nachricht eine Nachrichten-Komponente.


<!--
Beschreiben Sie den inneren Aufbau (einiger) Bausteine aus Ebene 1 als Whitebox.

Welche Bausteine Ihres Systems Sie hier beschreiben, müssen Sie selbst entscheiden. Bitte stellen Sie dabei Relevanz vor
Vollständigkeit. Skizzieren Sie wichtige, überraschende, riskante, komplexe oder besonders volatile Bausteine. Normale,
einfache oder standardisierte Teile sollten Sie weglassen.
-->


