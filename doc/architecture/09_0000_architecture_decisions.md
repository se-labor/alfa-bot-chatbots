# Architekturentscheidungen
<!--
**Inhalt**

Wichtige, teure, große oder riskante Architektur- oder
Entwurfsentscheidungen inklusive der jeweiligen Begründungen. Mit
"Entscheidungen" meinen wir hier die Auswahl einer von mehreren
Alternativen unter vorgegebenen Kriterien.

Wägen Sie ab, inwiefern Sie Entscheidungen hier zentral beschreiben,
oder wo eine lokale Beschreibung (z.B. in der Whitebox-Sicht von
Bausteinen) sinnvoller ist. Vermeiden Sie Redundanz. Verweisen Sie evtl.
auf Abschnitt 4, wo schon grundlegende strategische Entscheidungen
beschrieben wurden.

**Motivation**

Stakeholder des Systems sollten wichtige Entscheidungen verstehen und
nachvollziehen können.

**Form**

Verschiedene Möglichkeiten:

-   ADR ([Architecture Decision
    Record](https://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions))
    für jede wichtige Entscheidung

-   Liste oder Tabelle, nach Wichtigkeit und Tragweite der
    Entscheidungen geordnet

-   ausführlicher in Form einzelner Unterkapitel je Entscheidung

Siehe [Architekturentscheidungen](https://docs.arc42.org/section-9/) in
der arc42 Dokumentation (auf Englisch!). Dort finden Sie Links und
Beispiele zum Thema ADR.
-->

### Wahl des Chatbot Frameworks
Rasa Open Source wurde für dieses Projekt ausgewählt, da es zum Projektstart eines der wenigen wirklich offenen
Frameworks war. Zudem ist die Entwicklung von Rasa sehr ausgeprägt und es gibt ein Enterprise Lizenz Model, was darauf schließen
lässt, dass die Software in den nächsten Jahren konstant weiter entwickelt wird. 

### Wahl von flutter
Um den geringen personellen Ressourcen im Projekt Rechnung zu tragen, soll das Projekt auf einer Codebasis für beide Mobilsysteme entwickelt werden.
Flutter erlaubt inzwischen sehr umfänglichen Zugriff auf Systemfunktionen des Smartphones und ist daher absolut ausreichend, 
um das Vorhaben umzusetzen.
