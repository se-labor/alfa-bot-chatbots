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

Installieren von [Rasa X](https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide) (GUI Wrapper):
Sicherstellen, dass man in der gleichen virtuellen Umgebung arbeitet, wo rasa selbst installiert wurde.

* Virtuelle Umgebung starten: `source ./venv/bin/activate`
* Rasa X installieren `pip install -U rasa-x --extra-index-url https://pypi.rasa.com/simple`

**Hinweis zur Installation von Rasa X (Stand 1.4.21):**
Maybe this is incorrect but I noticed I have to downgrade the pip version in the respective virtual environment as well. So make sure the virtual environment with rasa is active and:
```
pip install --upgrade pip==20.2
run pip -V to make sure the right version is installed
run pip install -U rasa-x --extra-index-url https://pypi.rasa.com/simple
```

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

**Action**: Reaktion des Bots in Kombination mit oder ohne einer *Response*. Unterschieden wird hier zwischen **Regular Actions** und **Custom Actions**. *Regular Actions* verwenden die vorgegebenen Responses aus der domain.yml, während *Custom Actions* erweiterte Programmlogik ausführen. Beispiel für Custom Actions: User: *Wie wird das Wetter morgen?* -> Action: *Wetter für aktuellen Ort und nächsten Tag per API abfragen* -> Bot: *Morgen ist für `{ORT}`, `{WETTERPROGNOSE}` vorhergesagt*

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
### Wichtigste yml-Dateien
* data/nlu.yml
* data/rules.yml
* data/stories.yml
* domain.yml

Hilfstool zum verifizieren der yml-Dateien: https://yamlchecker.com

####NLU.yml
Die NLU-Datei enthält Intents **zusammen** mit Beispielen. Zu jedem Intent gehört eine Liste an Beispielsätzen, die diesem Intent zugeordnet werden sollen. 
Es können auch mehrere NLU-Dateien verwendet werden, um eine bessere Übersicht zu gewährleisten.
Pro Intent sind 7-10 Beispielsätze empfehlenswert. Ggf. kann es auch nützlich sein, bei bestimmten Wörtern häufige Rechtschreibfehler mit aufzunehmen.
Beispiel. Ähnliche Eingaben, die so nicht in den Beispielsätzen stehen, werden über ML-Algorithmen auf den jeweiligen Intent geparst.
```yaml
- intent: greet
  examples: |
    - Hi
    - hey
    - moin
    - Hallo
    - Grüß dich
    - ...
```

####Domain.yml
Die Domain.yml besteht aus bis zu sieben Abschnitten:
1. Angabe der Rasa-Version, in diesem Projekt 2.0
2. Eine Auflistung aller Intents (**ohne** Beispiele), die der Chatbot "kennt".
3. *Eine Auflistung aller verwendeten Entities (Variablen)*
4. *Programmspeicher in Form von Slots*
5. Enthält alle **Responses**. Jede Response wird durch **utter_responsename** gekenntzeichnet. Siehe Beispiel unten.
6. *Übersicht von **Action-Names**. Diese Übersicht enthält die Namen aller selbst definierten *Custom-Actions**

Die Bereiche 3, 4 und 6 sind optional und kommen nur vor, wenn die Aspekte im Bot auch verwendet werden.
```yaml
version: "2.0"

intents: 
  - greet
  - goodbye
  - ...

entities:
  - name
    
slots:
  concerts:
    type: list
    influence_conversation: false
  slotname:
    type: type_of_slot // bspw. text
    influence_conversation: true // bool, muss true oder false sein
  
responses:
  utter_greet:
    - text: "Hey, wie geht es dir?" // Antworttext
  
  utter_cheer_up:
    - text: "Hier ist ein Bild, das dich zum Lachen bringt:"
    - image: "https://i.imgur.com/nGF1K8f.jpg" // lädt ein Bild nach 

  utter_mood:
    - text: "Ich bin echt happy"
    - text: "Mir geht es wirklich gut" // Alternative Antwort. Rasa wählt eine der Optionen zufällig aus
  
actions:
  - action_name_of_custom_action
```

####Stories.yml
Die Stories.yml enthält Beispiel-Konversationen, die dem einerseits vorgeben, auf welchen Intent er wie reagieren soll und darüber hinaus konkrete Dialoge mit mehreren Turn-Takings darstellen.
Im Sinne von [Conversation-Driven-Development](https://rasa.com/docs/rasa/conversation-driven-development/) sollten diese Stories am besten über die Interaktion mit dem Bot erstellt werden (bspw. über rasa interactive oder rasa x).


###Kurzdialoge: Chitchat und FAQs
Kurzdialoge wie Chitchat und FAQ unterscheiden sich vom sonstigen Dialog dahingehend, dass es sich um Fragen handelt, die i.d.R. mit einer Antwort erledigt sind. Längere Dialogverläufe sind nicht notwendig.
In Rasa werden diese Gesprächsformen wie folgt implementiert:
1. In der **config.yml** muss die `Rule Policy` zu den Policies hinzugefügt sein, damit **rules.yml** überhaupt vom Datenmodel beachtet wird.
```yaml
policies:
# other policies
- name: RulePolicy
```
2. Ebenfalls in der **config.yml** einen Responseselector pro Kurzdialog-Art anlegen. Der hier definierte Value zum Key `retrievel_intent` muss später in den nlu-Trainingsdaten und in den Responses wieder auftauchen.
```yaml
pipeline:
# Other components
- name: ResponseSelector
  epochs: 100
  retrieval_intent: faq // für FAQ-Kurzdialoge
- name: ResponseSelector
  epochs: 100
  retrieval_intent: chitchat // für Chitchat-Kurzdialoge
```
3. Regeln für die Kurzdialoge in **rules.yml** definieren. Es muss pro `retrievel_intent` nur eine Regel definiert werden. 
   Alle Subintents mit diesem Intent werden durch die Regel gleich behandelt. Wird der Retrievel Intent ausgelöst, ermittelt Rasa den wahrscheinlichsten Sub-Intent und gibt die definierte Response aus.
```yaml
rules:
  - rule: respond to FAQs
    steps:
    - intent: faq
    - action: utter_faq
  - rule: respond to chitchat
    steps:
    - intent: chitchat
    - action: utter_chitchat
```   
4. NLU-Trainingsdaten unter **nlu.yml** anpassen. 
Die Intents werden wie gewöhnlich definiert, allerdings mit gruppierendem Retrievel Intent, also bspw. `faq/`.
```yaml
nlu:
  - intent: faq/democracy
    examples: |
      - Ist Deutschland eine Demokratie?
      - Was ist eine Demokratie?
      - Was bedeutet Demokratie?
  - intent: chitchat/howAreYou
    examples: |
      - wie geht es dir?
      - geht es dir gut?
      - wie ist dein befinden?
```   
5. Domain-Datei **domain.yml** anpassen. Unter intents reicht es, die Retrievel Intent-Namen einzutragen. Die Einzelintents müssen nicht aufgeführt werden.
```yaml
intents:
# other intents
- faq
- chitchat
``` 
6. Ebenfalls in der **domain.yml** müssen die Responses wie die Intents behandelt werden
```yaml
responses:
  utter_chitchat/ask_name:
  - image: "https://i.imgur.com/zTvA58i.jpeg"
    text: Hello, my name is Retrieval Bot.
  - text: I am called Retrieval Bot!
  utter_chitchat/ask_weather:
  - text: Oh, it does look sunny right now in Berlin.
    image: "https://i.imgur.com/vwv7aHN.png"
  - text: I am not sure of the whole week but I can see the sun is out today.
``` 
7. Bot erneut mit `rasa train` trainieren. Danach sollte es funktionieren. 
   Eventuelle Warnings wie *UserWarning: Action 'utter_faq' is listed as a response action in the domain file, but there is no matching response defined. Please check your domain.* können ignoriert werden. Stand April 2021 ist das ein [offener Bug](https://github.com/RasaHQ/rasa/issues/7645) im Rasa-Github

###Sonstiges:
spaCy: https://spacy.io/usage/models#languages

REST-Endpoint: https://rasa.com/docs/rasa/2.2.x/connectors/your-own-website
bei laufendem rasa x über `http://localhost:5005/webhooks/rest/webhook` per JSON-Objekt, bspw.
```JSON
{
    "message": "Wer ist der Kandidat der CDU?",
    "sender": "User-ID"
}
```
pypi-dotenv: https://pypi.org/project/python-dotenv/