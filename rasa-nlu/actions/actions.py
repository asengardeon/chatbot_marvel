# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from marvel import Marvel
from googletrans import Translator

translator = Translator()

class ActionHeroHistory(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        PUBLIC_KEY = "8e015296ba3e131887a0d5d2df0f1a9f"
        PRIVATE_KEY = "5dc31df476a489fc560bcbdd67646a4feed203ce"
        m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
        char_name = next(tracker.get_latest_entity_values("character_name"), None)
        char = m.characters.all(nameStartsWith=char_name)
        description = char['data']['results'][0]['description']


        #dispatcher.utter_message(text="Sim! conheço o " + char_name)
        dispatcher.utter_message(text=description)
        return []
