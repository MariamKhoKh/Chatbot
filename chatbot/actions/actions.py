from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet


class ActionGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello! How can I assist you today?")
        return []


class ActionGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Goodbye! Have a nice day!")
        return []


class ActionBookRoom(Action):
    def name(self) -> Text:
        return "utter_book_room"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure! How many rooms would you like to book?")
        return []


class ActionCleanRoom(Action):
    def name(self) -> Text:
        return "utter_clean_room"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I will send someone to clean the room.")
        return []


class ActionCleanRoomNow(Action):
    def name(self) -> Text:
        return "utter_clean_room_now"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I will send someone right now.")
        return []


class ActionCheckInTime(Action):
    def name(self) -> Text:
        return "utter_check_in_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Check-in time is from 2:00 PM.")
        return []


class ActionCheckOutTime(Action):
    def name(self) -> Text:
        return "utter_check_out_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Check-out time is until 11:00 AM.")
        return []


class ValidateBookRoomForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_book_room"

    def validate_number_of_rooms(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if int(slot_value) > 0:
            return {"number_of_rooms": slot_value}
        else:
            dispatcher.utter_message(text="You must book at least one room.")
            return {"number_of_rooms": None}


