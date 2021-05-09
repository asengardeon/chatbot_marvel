# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .marvel_requests import marvel_request

class ActionHeroDescription(Action):

    def name(self) -> Text:
        return "action_hero_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = tracker.get_slot('hero_name')

        found, desc = marvel_request.char_description(char_name)
        dispatcher.utter_message(text=desc)
        return []


class ActionHeroPhoto(Action):

    def name(self) -> Text:
        return "action_hero_photo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = tracker.get_slot('hero_name')

        found, result = marvel_request.char_photo(char_name)
        if found:
            dispatcher.utter_message(image=result)
        else:
            dispatcher.utter_message(text=result)
        return []


class ActionHeroComicsQuantity(Action):

    def name(self) -> Text:
        return "action_hero_comics_quantity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = tracker.get_slot('hero_name')

        result = marvel_request.comics_qtd_for_char(char_name)

        dispatcher.utter_message(text=result)
        return []


class ActionDateOfComic(Action):

    def name(self) -> Text:
        return "action_comic_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.date_of_comic(comic_name)

        dispatcher.utter_message(text=result)
        return []


class ActionCreatorOfComic(Action):

    def name(self) -> Text:
        return "action_comic_creators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.creator_of_comic(comic_name)

        dispatcher.utter_message(text=result)
        return []


class ActionCharactersOfComic(Action):

    def name(self) -> Text:
        return "action_comic_heros"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.characters_of_comic(comic_name)

        dispatcher.utter_message(text=result)
        return []


class ActionComicPrices(Action):

    def name(self) -> Text:
        return "action_comic_prices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.prices_of_comic(comic_name)

        dispatcher.utter_message(text=result)
        return []


class ActionComicPhoto(Action):

    def name(self) -> Text:
        return "action_comic_photo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.comic_photo(comic_name)
        if found:
            dispatcher.utter_message(image=result)
        else:
            dispatcher.utter_message(text=result)
        return []


class ActionComicsOfCreator(Action):

    def name(self) -> Text:
        return "action_creators_comics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        first_name = tracker.get_slot('first_name')
        last_name = tracker.get_slot('last_name')
        found, result = marvel_request.comics_of_creator(first_name, last_name)
        dispatcher.utter_message(text=result)
        return []


class ActionQuantityOfComicsOfCreator(Action):

    def name(self) -> Text:
        return "action_creators_comics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        first_name = tracker.get_slot('first_name')
        last_name = tracker.get_slot('last_name')
        found, result = marvel_request.qtd_comics_of_creator(first_name, last_name)
        dispatcher.utter_message(text=result)
        return []
