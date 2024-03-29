##
#  A04_finance_bot_actions.py
#  ALFA-Bot
#
#  Created by Simon on 24.12.2023
#  Copyright © 2023 Fachhochschule Münster. All rights reserved.
##

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
                 "Kredite": "Fachbegriffe Kredit",
                 "Banken": "Fachbegriffe Banken"
                 }

termsInsurance = {"Basistarif": "Was ist ein Basistarif", "Versicherungsnehmer": "Was ist ein Versicherungsnehmer",
                  "Riester Rente": "Was ist die Riester Rente",
                  "Beitrag": "Was sind Beiträge?", "Garantieleistung": "Was sind Garantieleistungen",
                  "Gesundheitsprüfung": "Was ist eine Gesundheitsprüfung",
                  "Versicherungsvertreter": "Versicherungsvertreter", "Schadensfall": "Was ist ein Schadensfall",
                  "Police": "Was ist eine Police", "Teilkasko": "Teilkasko", "Vollkasko": "Vollkasko",
                  "Risiko": "Was bedeutet Risiko bei Versicherungen"}

termsCredit = {"Bonitätsprüfung": "Bonitätsprüfung", "Schufa": "Was macht die Schufa?",
               "Dispo-Kredit": "Was ist ein Dispo?", "Gläubiger": "Was ist ein Gläubiger",
               "Inkasso": "Was macht ein Inkasso-Büro", "Kontoauszug": "Was ist ein Kontoauszug?",
               "Konto-Pfändung": "Was ist eine Kontopfändung?", "Kredit": "Kredit",
               "Kredit-Karte": "Was mache ich mit einer Kreditkarte?",
               "Kreditwürdigkeit": "Was ist Kreditwürdigkeit?", "Mahnverfahren": "Was ist ein Mahnverfahren?",
               "Schuldner-Beratung": "Schuldner-Beratung", "Überweisung": "Was ist eine Überweisung?",
               "Zwangsvollstreckung": "Was ist eine Zwangsvollstreckung", "Effektivzins": "Effektivzins",
               "Sicherheit": "Kredit Sicherheit", "Grundbuch": "Was steht im Grundbuch?",
               "Eigenkapital": "Brauche ich Eigenkapital?"}

termsBanking = {"Basiskonto": "Was ist ein Basiskonto?",
                "Dauerauftrag": "Was ist ein Dauerauftrag?", "EC-Karte": "Was ist eine EC-Karte?",
                "sepa-Lastschrift": "Was ist ein Lastschriftmandat?", "Girokonto": "Was ist ein Girokonto",
                "Guthaben-Konto": "Was ist ein Guthabenkonto?", "Kontoauszug": "Was ist ein Kontoauszug?",
                "Kredit": "Was ist ein Kredit?", "Kredit-Karte": "Was mache ich mit einer Kreditkarte?",
                "Rück-Lastschrift": "Rücklastschrift", "Überweisung": "Was ist eine Überweisung?",
                "Sparbuch": "Was ist ein Sparbuch?", "Tagesgeld": "Tagesgeld", "Festgeld": "Was ist Festgeld",
                }


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


def randomise_fail_answer() -> str:
    fail_answers = ["Leider die falsche Lösung", "Leider falsch", "Das ist nicht richtig",
                    "Tut mir Leid, das ist nicht korrekt."]
    fail_reactions = ["!", ".", " 😊.", " 👍."]
    random_answer = random.choice(fail_answers)
    random_reaction = random.choice(fail_reactions)
    msg = random_answer + random_reaction
    return msg


# Generate buttons for all terms subset of insurance terms
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
        dispatcher.utter_message(text="Hier sind zufällig ausgewählte Fachbegriffe. Wenn du möchtest, lass dir eine *neue Auswahl* oder *alle Fachbegriffe* anzeigen.", buttons=buttons)
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
        dispatcher.utter_message(text=f"Hier sind alle Fachbegriffe für Versicherungen, die ich dir anbieten kann:",
                                 buttons=buttons)
        return []


# Select random subset of credit terms
class ActionGetRandomCreditTerms(Action):
    def name(self) -> Text:
        return "action_get_random_credit_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        randomButtons = 3
        buttons = randomSelection(termsCredit, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_credit_terms"})
        dispatcher.utter_message(text="Hier sind zufällig ausgewählte Fachbegriffe. Wenn du möchtest, lass dir eine *neue Auswahl* oder *alle Fachbegriffe* anzeigen.", buttons=buttons)
        return []


# Present credit terms
class ActionCreditTerms(Action):
    def name(self) -> Text:
        return "action_credit_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        randomButtons = 2
        buttons = randomSelection(termsCredit, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_credit_terms"})
        buttons.append({"title": "Alle Fachbegriffe", "payload": "/all_credit_terms"})
        dispatcher.utter_message(response="utter_fachbegriffe_credit", buttons=buttons)
        return []


# List all credit terms
class ActionGetAllCreditTerms(Action):
    def name(self) -> Text:
        return "action_get_all_credit_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = getButtonsFromDict(dict(sorted(termsCredit.items())))
        dispatcher.utter_message(text=f"Hier sind alle Fachbegriffe zu Krediten, die ich dir anbieten kann:",
                                 buttons=buttons)
        return []


# Select random subset of banking terms
class ActionGetRandomBankingTerms(Action):
    def name(self) -> Text:
        return "action_get_random_banking_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        randomButtons = 3
        buttons = randomSelection(termsBanking, randomButtons)
        buttons.append({"title": "Neue Auswahl", "payload": "/random_banking_terms"})
        dispatcher.utter_message(text="Hier sind zufällig ausgewählte Fachbegriffe. Wenn du möchtest, lass dir eine *neue Auswahl* oder *alle Fachbegriffe* zu diesem Thema anzeigen.", buttons=buttons)
        return []


# Present banking terms
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


# List all banking terms
class ActionGetAllBankingTerms(Action):
    def name(self) -> Text:
        return "action_get_all_banking_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = getButtonsFromDict(dict(sorted(termsBanking.items())))
        dispatcher.utter_message(text=f"Hier sind alle Fachbegriffe für Banken und Geld, die ich dir anbieten kann:",
                                 buttons=buttons)
        return []


class ActionListAllTerms(Action):
    def name(self) -> Text:
        return "action_list_all_terms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        termsAll = {k: v for k, v in termsInsurance.items()}
        termsAll.update(termsCredit)
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
        needle = 'ist eine freiwillige Versicherung für dein Auto'
        while user_ignore_count > 0:
            event = tracker.events[count].get('event')
            if event == 'user':
                user_ignore_count = user_ignore_count - 1
            if event == 'bot':
                if (needle in (tracker.events[count].get('text'))):
                    dispatcher.utter_message(response='utter_insurance/versicherungen_was')
                    return []

                tracker_list.append(tracker.events[count])
            count = count - 1

        # Variable i controls the output. With -1 it will output only the next to last bot answer
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


# Validate finance quiz question 1
class QuizQuestion1Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_quiz_question1_form"

    def validate_question1(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
            firstTry=bool(True)
    ) -> Dict[Text, Any]:
        solution_question = str(slot_value).lower()
        if solution_question == 'q1_right' or 'haftpflicht' in solution_question:
            dispatcher.utter_message(response="utter_q1_right")
            return {"question1": slot_value}
        # if solution_question != 'q1_right' or 'haftpflicht' not in solution_question:
        else:
            if 'q1_wrong_' in solution_question:
                res_string = f"utter_{solution_question}"
                dispatcher.utter_message(response=res_string)
                return {"question1": slot_value}
            else:
                answer = "Leider nein"
                buttons = ({"title": "Richtige Lösung", "payload": "/q1_right"},
                           {"title": "Weiter", "payload": "enter_question_2"})
                dispatcher.utter_message(text=answer, buttons=buttons)
                return {"question1": slot_value}


# Validate finance quiz question 2
class QuizQuestion2Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_quiz_question2_form"

    def validate_question2(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
            firstTry=bool(True)
    ) -> Dict[Text, Any]:
        solution_question = str(slot_value).lower()
        if solution_question == 'q2_right' or 'unfähigkeit' in solution_question:
            dispatcher.utter_message(response="utter_q2_right")
            return {"question2": slot_value}
        else:
            if 'q2_wrong_' in solution_question:
                res_string = f"utter_{solution_question}"
                dispatcher.utter_message(response=res_string)
            else:
                answer = "Leider nein"
                buttons = ({"title": "Richtige Lösung", "payload": "/q2_right"},
                           {"title": "Weiter", "payload": "enter_question_3"})
                dispatcher.utter_message(text=answer, buttons=buttons)
            return {"question2": slot_value}


# Validate finance quiz question 3
class QuizQuestion3Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_quiz_question3_form"

    def validate_question3(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
            firstTry=bool(True)
    ) -> Dict[Text, Any]:
        solution_question = str(slot_value).lower()
        if solution_question == 'q3_right' or 'schäden an deinem fahrzeug bezahlt sie nicht' in solution_question:
            dispatcher.utter_message(response="utter_q3_right")
            return {"question3": slot_value}
        else:
            if 'q3_wrong_' in solution_question:
                res_string = f"utter_{solution_question}"
                dispatcher.utter_message(response=res_string)
            else:
                answer = "Leider nein"
                buttons = ({"title": "Richtige Lösung", "payload": "/q3_right"},
                           {"title": "Weiter", "payload": "enter_question_4"})
                dispatcher.utter_message(text=answer, buttons=buttons)
            return {"question3": slot_value}


# Validate finance quiz question 4
class QuizQuestion4Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_quiz_question4_form"

    def validate_question4(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
            firstTry=bool(True)
    ) -> Dict[Text, Any]:
        solution_question = str(slot_value)
        if solution_question == 'q4_right' or 'kreditgeber ist verpflichtet' in solution_question:
            dispatcher.utter_message(response="utter_q4_right")
            return {"question4": slot_value}
        else:
            if 'q4_wrong_' in solution_question:
                res_string = f"utter_{solution_question}"
                dispatcher.utter_message(response=res_string)
            else:
                answer = "Leider nein"
                buttons = ({"title": "Richtige Lösung", "payload": "/q4_right"},
                           {"title": "Weiter", "payload": "enter_question_5"})
                dispatcher.utter_message(text=answer, buttons=buttons)
            return {"question4": slot_value}


# Validate finance quiz question 5
class QuizQuestion5Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_quiz_question5_form"

    def validate_question5(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
            firstTry=bool(True)
    ) -> Dict[Text, Any]:
        solution_question = str(slot_value)
        if solution_question == 'q5_right' or 'direkt an der kasse bezahlen' in solution_question:
            dispatcher.utter_message(response="utter_q5_right")
            return {"question5": slot_value}
        else:
            if 'q5_wrong_' in solution_question:
                res_string = f"utter_{solution_question}"
                dispatcher.utter_message(response=res_string)
            else:
                answer = "Leider nein"
                buttons = ({"title": "Richtige Lösung", "payload": "/q5_right"},
                           {"title": "Weiter", "payload": "enter_question_6"})
                dispatcher.utter_message(text=answer, buttons=buttons)
            return {"question5": slot_value}


# Validate finance quiz question 6
class QuizQuestion6Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_quiz_question6_form"

    def validate_question6(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
            firstTry=bool(True)
    ) -> Dict[Text, Any]:
        solution_question = str(slot_value)
        if solution_question == 'q6_right' or 'regelmäßig den gleichen betrag' in solution_question:
            dispatcher.utter_message(response="utter_q6_right")
            return {"question6": slot_value}
        else:
            if 'q6_wrong_' in solution_question:
                res_string = f"utter_{solution_question}"
                dispatcher.utter_message(response=res_string)
            else:
                answer = "Leider nein"
                buttons = ({"title": "Richtige Lösung", "payload": "/q6_right"})
                dispatcher.utter_message(text=answer, buttons=buttons)
            return {"question6": slot_value}


class ActionClearQuizSlots(Action):
    def name(self) -> Text:
        return "action_clear_quiz_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("question1", None), SlotSet("question2", None), SlotSet("question3", None),
                SlotSet("question4", None), SlotSet("question5", None), SlotSet("question6", None)]