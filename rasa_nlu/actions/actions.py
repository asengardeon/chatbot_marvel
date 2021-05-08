# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .marvel_request import *

class ActionHeroDescription(Action):

    def name(self) -> Text:
        return "action_hero_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = next(tracker.get_latest_entity_values("hero_name"), None)

        description = char_description(char_name)

        #dispatcher.utter_message(text="Sim! conheço o " + char_name)
        dispatcher.utter_message(text=description)
        return []


class ActionHeroPhoto(Action):

    def name(self) -> Text:
        return "action_hero_photo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = next(tracker.get_latest_entity_values("hero_name"), None)

        description = char_photo(char_name)

        dispatcher.utter_message(text=description)
        return []


class ActionHeroComicsQuantity(Action):

    def name(self) -> Text:
        return "action_hero_comics_quantity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = next(tracker.get_latest_entity_values("hero_name"), None)

        description = comics_qtd_for_char(char_name)

        dispatcher.utter_message(text=description)
        return []


class ActionDateOfComic(Action):

    def name(self) -> Text:
        return "action_comic_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = date_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionCreatorOfComic(Action):

    def name(self) -> Text:
        return "action_comic_creators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = creator_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionCharactersOfComic(Action):

    def name(self) -> Text:
        return "action_comic_heros"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = characters_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionComicPrices(Action):

    def name(self) -> Text:
        return "action_comic_prices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = prices_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionComicPhoto(Action):

    def name(self) -> Text:
        return "action_comic_photo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = comic_photo(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionQuantityOfComicsOfCreator(Action):

    def name(self) -> Text:
        return "action_creators_comics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        creator_name = next(tracker.get_latest_entity_values("creator_name"), None)

        description = qtd_comics_of_creator(creator_name)

        dispatcher.utter_message(text=description)
        return []

