# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from marvel_requests import marvel_request


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


class ActionHeroPhoto(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = next(tracker.get_latest_entity_values("character_name"), None)

        description = marvel_request.char_photo(char_name)

        dispatcher.utter_message(text=description)
        return []


class ActionHeroComicsQuantity(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = next(tracker.get_latest_entity_values("character_name"), None)

        description = marvel_request.comics_qtd_for_char(char_name)

        dispatcher.utter_message(text=description)
        return []


class ActionDateOfComic(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = marvel_request.date_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionCreatorOfComic(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = marvel_request.creator_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionCharactersOfComic(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = marvel_request.characters_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionComicPrices(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = marvel_request.prices_of_comic(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionComicPhoto(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = next(tracker.get_latest_entity_values("comic_name"), None)

        description = marvel_request.comic_photo(comic_name)

        dispatcher.utter_message(text=description)
        return []


class ActionComicPhoto(Action):

    def name(self) -> Text:
        return "action_hero_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        creator_name = next(tracker.get_latest_entity_values("creator_name"), None)

        description = marvel_request.qtd_comics_of_creator(creator_name)

        dispatcher.utter_message(text=description)
        return []

