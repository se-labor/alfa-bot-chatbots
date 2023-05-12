from typing import Any, Text, Dict
import random
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import List
# from .A03_learning_bot_actions import randomSelection, getButtonsFromDict, QuickReplyButton


# Helper vars and classes
termsSections = {"Versicherungen": "Fachbegriffe Versicherungen",
                 "Banken & Geld": "Fachbegriffe Banking"}

termsInsurance = {"Basistarif": "Was ist ein Basistarif", "Versicherungsnehmer": "Was ist ein Versicherungsnehmer",
                "Riester Rente": "Was ist die Riester Rente",
                "Beitrag": "Was sind Beiträge?", "Garantieleistung": "Was sind Garantieleistungen",
                "Gesundheitsprüfung": "Was ist eine Gesundheitsprüfung",
                "Versicherungsvertreter": "Versicherungsvertreter", "Schadensfall": "Was ist ein Schadensfall",
                "Police": "Was ist eine Police",
                "Risiko": "Was bedeutet Risiko bei Versicherungen"}

termsBanking = {"Basiskonto": "Was ist ein Basiskonto?", "Bonitätsprüfung": "Bonitätsprüfung", "Schufa": "Was macht die Schufa?",
                "Dauerauftrag": "Was ist ein Dauerauftrag?", "Dispo-Kredit": "Was ist ein Dispo?", "EC-Karte": "Was ist eine EC-Karte?",
                "SEPA-Lastschrift": "Was ist ein Lastschriftmandat?", "Girokonto": "Was ist ein Girokonto", "Gläubiger": "Was ist ein Gläubiger",
                "Guthaben-Konto": "Was ist ein Guthabenkonto?", "Inkasso": "Was macht ein Inkasso-Büro", "Kontoauszug": "Was ist ein Kontoauszug?",
                "Konto-Pfändung": "Was ist eine Kontopfändung?", "Kredit": "Was ist ein Kredit?", "Kredit-Karte": "Was mache ich mit einer Kreditkarte?",
                "Kreditwürdigkeit": "Was ist Kreditwürdigkeit?", "Rück-Lastschrift": "Rücklastschrift", "Mahnverfahren": "Was ist ein Mahnverfahren?",
                "Schuldner-Beratung": "Schuldner-Beratung", "Überweisung": "Was ist eine Überweisung?", "Sparbuch": "Was ist ein Sparbuch?",
                "Tagesgeld": "Tagesgeld", "Festgeld": "Was ist Festgeld", "Zwangsvollstreckung": "Was ist eine Zwangsvollstreckung",
                "Effektivzins": "Effektivzins", "Sicherheit": "Kredit Sicherheit", "Grundbuch": "Was steht im Grundbuch?",
                "Darlehen": "Darlehen", "Eigenkapital": "Brauche ich Eigenkapital?"}

class QuickReplyButton:
    def __init__(self, title: str, payload: str):
        self.title = title
        self.payload = payload

    def getButton(self) -> dict:
        button = {"title": self.title, "payload": self.payload}
        return button


# Get array of buttons
def getButtonsFromDict(pool: dict) -> list:
    buttons = []
    for entry in pool:
        qrButton = QuickReplyButton(entry, pool[entry])
        buttons.append(qrButton.getButton())
    return buttons


# Getting random subset out of dictionary
def randomSelection(pool: dict, size: int) -> list:
    buttons = []
    sample = dict(random.sample(list(pool.items()), size))
    buttons = getButtonsFromDict(sample)
    return buttons

# Gernate buttons for all terms subset of insurance terms
class ActionAllSortOfTerms(Action):
    def name(self) -> Text:
        return "action_all_sort_of_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = getButtonsFromDict(dict(sorted(termsSections.items())))
        dispatcher.utter_message(text="Hier sind die Themen, zu denen ich Fachbegriffe habe", buttons=buttons)
        return []
# Select random subset of insurance terms
class ActionGetRandomInsuranceTerms(Action):
    def name(self) -> Text:
        return "action_get_random_insurance_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        randomButtons = 3
        buttons = randomSelection(termsInsurance, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_insurance_terms"})
        dispatcher.utter_message(text="Hier ist eine weitere Auswahl an Fachbegriffen", buttons=buttons)
        return []

# Present insurance terms
class ActionInsuranceTerms(Action):
    def name(self) -> Text:
        return "action_insurance_terms"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        randomButtons = 2
        buttons = randomSelection(termsInsurance, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_insurance_terms"})
        buttons.append({"title": "Alle Fachbegriffe", "payload": "/all_insurance_terms"})
        dispatcher.utter_message(response="utter_fachbegriffe_versicherungen", buttons=buttons)
        return []

# List all insurance terms
class ActionGetAllInsuranceTerms(Action):
    def name(self) -> Text:
        return "action_get_all_insurance_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = getButtonsFromDict(dict(sorted(termsInsurance.items())))
        print(dict(sorted(termsInsurance.items())))
        dispatcher.utter_message(text=f"Hier sind alle Fachbegriffe für Versicherungen, die ich dir anbieten kann:", buttons=buttons)
        return []

# Select random subset of insurance terms
class ActionGetRandomBankingTerms(Action):
    def name(self) -> Text:
        return "action_get_random_banking_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        randomButtons = 3
        buttons = randomSelection(termsBanking, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_banking_terms"})
        dispatcher.utter_message(text="Hier ist eine weitere Auswahl an Fachbegriffen", buttons=buttons)
        return []

# Present insurance terms
class ActionBankingTerms(Action):
    def name(self) -> Text:
        return "action_banking_terms"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        randomButtons = 2
        buttons = randomSelection(termsBanking, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_banking_terms"})
        buttons.append({"title": "Alle Fachbegriffe", "payload": "/all_banking_terms"})
        dispatcher.utter_message(response="utter_fachbegriffe_banking", buttons=buttons)
        return []

# List all insurance terms
class ActionGetAllBankingTerms(Action):
    def name(self) -> Text:
        return "action_get_all_banking_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = getButtonsFromDict(dict(sorted(termsBanking.items())))
        dispatcher.utter_message(text=f"Hier sind alle Fachbegriffe für Banken & Geld, die ich dir anbieten kann:", buttons=buttons)
        return []

        termsAll = termsInsurance
        termsAll.update(termsBanking)


class ActionListAllTerms(Action):
    def name(self) -> Text:
        return "action_list_all_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        termsAll = {k:v for k,v in termsInsurance.items()}
        termsAll.update(termsBanking)
        buttons = getButtonsFromDict(dict(sorted(termsAll.items())))
        dispatcher.utter_message(text=f"Hier sind alle Fachbegriffe über alle Themen, die ich dir anbieten kann:",
                                 buttons=buttons)
        return []

class ActionRepeat(Action):
    def name(self) -> Text:
        return "action_repeat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Counter to fetch the last three utterances (0 bot - 1 user - 2 bot)
        user_ignore_count = 3
        count = 0
        tracker_list = []

        # filter user utterances
        while user_ignore_count > 0:
            event = tracker.events[count].get('event')
            if event == 'user':
                user_ignore_count = user_ignore_count - 1
            if event == 'bot':
                tracker_list.append(tracker.events[count])
            count = count - 1

        # i controls the output. With -1 it will output only the next to last bot answer
        i = len(tracker_list) - 1
        while i >= 1:
            data = tracker_list[i].get('data')
            if data:
                if "buttons" in data:
                    dispatcher.utter_message(text=tracker_list[i].get('text'), buttons=data["buttons"])
                else:
                    dispatcher.utter_message(text=tracker_list[i].get('text'))
            i -= 1

        return []

# List all nice to knows
#class ActionGetNiceToKnow(Action):
#    def name(self) -> Text:
#        return "action_get_nice_to_know"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        buttons = getButtonsFromDict(niceToKnow)
#        dispatcher.utter_message(text=f"Hier sind alle interessanten Fakten", buttons=buttons)
#        return []
