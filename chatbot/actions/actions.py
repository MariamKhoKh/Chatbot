# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random


class ActionTellJoke(Action):

    def name(self) -> str:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker, domain):
        jokes = [
            "Why don't skeletons fight each other? Because they don't have the guts!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised!",
            "Why did the math book look sad? Because it had too many problems."
        ]
        joke = random.choice(jokes)
        dispatcher.utter_message(text=joke)
        return []


class ActionTellSum(Action):

    def name(self) -> Text:
        return "action_tell_sum"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("addend_1")
        number2 = tracker.get_slot("addend_2")
        dispatcher.utter_message(text=f"The sum of {number1} and {number2} is {float(number1) + float(number2)}")

        return []


class ActionTellFunFact(Action):

    def name(self) -> str:
        return "action_tell_fun_fact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker, domain):
        fun_facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
            "A group of flamingos is called a 'flamboyance'.",
            "Bananas are berries, but strawberries aren't."
        ]
        fact = random.choice(fun_facts)
        dispatcher.utter_message(text=fact)
        return []


class ActionTellMotivation(Action):

    def name(self) -> str:
        return "action_tell_motivation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker, domain):
        motivational_phrases = [
            "Believe in yourself, push your limits, and do whatever it takes to conquer your goals. You got this!",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "Don't watch the clock; do what it does. Keep going."
        ]
        motivation = random.choice(motivational_phrases)
        dispatcher.utter_message(text=motivation)
        return []


