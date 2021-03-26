# Rasa-Chatbot für Projekt ALFA-Bot - BT-Wahlen Prototyp

## Installation und Inbetriebnahme
###Python3 (venv)
Rasa wird in einer python3 virtual environment (venv) ausgeführt. Benötigt wird Pyhton3 und pip3
* Erstellen: `python3 -m venv ./venv`
* Aktivieren: `source ./venv/bin/activate`
* Deaktivieren: `deactivate`

###Installieren von Rasa
1. Aktivieren der virtuellen Umgebung
2. Update pip `pip3 install -U pip`
3. Installiere Rasa Open Source `pip3 install rasa`

Installieren von Rasa X (GUI Wrapper) -> https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide

###Rasa Open Source Befehle

* `rasa init`: Neues Projekt erstellen
* `rasa x`: Start rasa X Plattform
* `rasa train`: Trainiere ein CB-Model (models-Ordner steht in gitignore)
* `rasa shell`: Starte eine Unterhaltung über die Konsole
* `rasa interactive`: Starte eine Unterhaltung per Konsole mit Training
* `rasa run actions -vv`: Relevant für custom actions
* `rasa run -m models --enable-api --cors "*" -p 5021`: Wird benutzt, wenn ein Bot deployed ist und par API aktiviert werden soll.

## Zentrale Dateien und Konfigurationen

###Grundbegriffe im Rasa-Framework
**Intent**: Was der Nutzer meint (Intention). Zu finden in `nlu.yml` Beispiel: *Wie wird das Wetter?* -> Intent: *Wetterauskunft*

**Entity**: Modifier um Intents genauer zu beschreiben (Variablen). Beispiel: *Wie wird das Wetter **morgen** **in Berlin**?* -> Intent: *Wetterauskunft*, Entities: *Zeit: heute + 1* und *Ort: Berlin* 

**Response**: Eine textuelle Antwort. Zu finden in `domain.yml`. Beispiel: User: *Wie wird das Wetter morgen?* -> Bot: *Das Wetter wird morgen so ähnlich wie heute.*

**Action**: Reaktion des Bots in Kombination mit oder ohne einer *Response*. Beispiel: User: *Wie wird das Wetter morgen?* -> Action: *Wetter für aktuellen Ort und nächsten Tag per API abfragen* -> Bot: *Morgen ist für `{ORT}`, `{WETTERPROGNOSE}` vorhergesagt*

**Stories**: Bausteine eines Rasa-Chatbots. Jede Story stellt auf abstraktem Level Teile eines Dialogverlaufs dar. Zu finden in `stories.yml` Beispiel:

```yaml
-story: say_something_nice  // Name der Story
steps:                      // Dialogverlauf
    - intent: greet         // Intent, der die Story beginnt
    - action: utter_greet   // Reaktion des Bots, hier als Response *utter_greet* (s. domain.yml)
    - intent: tellSthNice   // Nächster Nutzerintent
    - action: utter_compliment // Reaktion per Response
    - intent: bye           // Intent für Verabschiedung
    - action: utter_bye     // Bot reagiert mit Verabschiedung
```
