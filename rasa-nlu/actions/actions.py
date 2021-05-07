# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from googletrans import Translator
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from marvel_requests import marvel_request

translator = Translator()

class ActionHeroDescription(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = next(tracker.get_latest_entity_values("character_name"), None)

        description = marvel_request.char_description(char_name)

        #dispatcher.utter_message(text="Sim! conheço o " + char_name)
        dispatcher.utter_message(text=description)
        return []
