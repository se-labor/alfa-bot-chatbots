from typing import Any, Text, Dict
import random
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import List
# from .A03_learning_bot_actions import randomSelection, getButtonsFromDict, QuickReplyButton


# Helper vars and classes
termsInsurance = {"Basistarif": "Was ist ein Basistarif", "Versicherungsnehmer": "Was ist ein Versicherungsnehmer",
                "Riester Rente": "Was ist die Riester Rente",
                "Beitrag": "Was sind Beiträge?", "Garantieleistung": "Was sind Garantieleistungen",
                "Gesundheitsprüfung": "Was ist eine Gesundheitsprüfung",
                "Versicherungsvertreter": "Versicherungsvertreter", "Schadensfall": "Was ist ein Schadensfall",
                "Police": "Was ist eine Police",
                "Risiko": "Was bedeutet Risiko bei Versicherungen"}

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
        print("Action_insurance_terms triggered")
        buttons = randomSelection(termsInsurance, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_insurance_terms"})
        buttons.append({"title": "Alle Fachbegriffe", "payload": "/all_insurance_terms"})
        dispatcher.utter_message(text="utter_fachbegriffe_versicherungen")
        return []

# List all insurance terms
class ActionGetAllInsuranceTerms(Action):
    def name(self) -> Text:
        return "action_get_all_insurance_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_get_all_insurance_terms triggered")
        buttons = getButtonsFromDict(termsInsurance)
        dispatcher.utter_message(text=f"Hier sind alle Fachbegriffe für Versicherungen, die ich dir anbieten kann:", buttons=buttons)
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
