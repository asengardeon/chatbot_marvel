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

from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import SlotSet

class ActionGreet(Action):

     def name(self) -> Text:
            return "action_greet"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_template("utter_greet", tracker)

         return [AllSlotsReset()]

# Hero

class ActionSearchHero(Action):

    def name(self) -> Text:
        return "action_search_hero"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = tracker.get_slot('hero_name')

        found, new_char_name = marvel_request.char_name(char_name)

        if found:
            dispatcher.utter_message(text=f"O heroi mais próximo de {char_name} foi {new_char_name}")
            char_name = new_char_name
            return [SlotSet("hero_name", char_name)]
        else:
            dispatcher.utter_message(text=f"Não achei nenhum heroi com o nome {char_name}")

class ActionHeroDescription(Action):

    def name(self) -> Text:
        return "action_hero_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = tracker.get_slot('hero_name')

        found, desc = marvel_request.char_description(char_name)
        if found:
            dispatcher.utter_message(text=f"Vou te contar a história do(a) {char_name}, veja só!")
            dispatcher.utter_message(text=desc)
        else:
            dispatcher.utter_message(text=f"Infelizmente não conheço o(a) {char_name} ")
        return [SlotSet("hero_name", char_name)]


class ActionHeroPhoto(Action):

    def name(self) -> Text:
        return "action_hero_photo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = tracker.get_slot('hero_name')

        found, result = marvel_request.char_photo(char_name)
        if found:
            dispatcher.utter_message(text=f"Toma uma foto bonitona do(a) {char_name}")
            dispatcher.utter_message(image=result)
        else:
            dispatcher.utter_message(text=f"Infelizmente não tenho foto do(a) {char_name}")
        return [SlotSet("hero_name", char_name)]


class ActionHeroComicsQuantity(Action):

    def name(self) -> Text:
        return "action_hero_comics_quantity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        char_name = tracker.get_slot('hero_name')

        result = marvel_request.comics_qtd_for_char(char_name)

        dispatcher.utter_message(text=f"O(a) {char_name} participou de {result} quadrinhos")
        return [SlotSet("hero_name", char_name)]

# Comics

class ActionSearchComic(Action):

    def name(self) -> Text:
        return "action_search_comic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, new_comic_name = marvel_request.comic_name(comic_name)

        if found:
            dispatcher.utter_message(text=f"O quadrinho mais próximo de {comic_name} foi {new_comic_name}")
            comic_name = new_comic_name
            return [SlotSet("comic_name", comic_name)]
        else:
            dispatcher.utter_message(text=f"Não achei nenhum quadrinho com nome {comic_name}")
            return []


class ActionDateOfComic(Action):

    def name(self) -> Text:
        return "action_comic_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.date_of_comic(comic_name)

        if found:
            dispatcher.utter_message(text=f"{comic_name} foi lançado em {result}")
        else:
            dispatcher.utter_message(text=f"Infelizmente não sei a data de lançamento do quadrinho {comic_name}")
        return [SlotSet("comic_name", comic_name)]


class ActionCreatorOfComic(Action):

    def name(self) -> Text:
        return "action_comic_creators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.creator_of_comic(comic_name)

        if found:
            dispatcher.utter_message(text=f"Os(as) criadores(as) de {comic_name} foram: {result}")
        else:
            dispatcher.utter_message(text=f"Infelizmente não sei quem escreveu o quadrinho {comic_name}")
        return [SlotSet("comic_name", comic_name)]


class ActionCharactersOfComic(Action):

    def name(self) -> Text:
        return "action_comic_heros"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.characters_of_comic(comic_name)

        if found:
            dispatcher.utter_message(text=f"Os herois que aparecem no {comic_name} foram: {result}")
        else:
            dispatcher.utter_message(text=f"Infelizmente não sei quais são os herois que aparecem no {comic_name}")
        return [SlotSet("comic_name", comic_name)]


class ActionComicPrices(Action):

    def name(self) -> Text:
        return "action_comic_prices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.prices_of_comic(comic_name)

        if found:
            dispatcher.utter_message(text=f"O preço do quadrinho {comic_name} é {result}")
        else:
            dispatcher.utter_message(text=f"Não sei o preço do quadrinho {comic_name}")
        return [SlotSet("comic_name", comic_name)]


class ActionComicPhoto(Action):

    def name(self) -> Text:
        return "action_comic_photo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comic_name = tracker.get_slot('comic_name')

        found, result = marvel_request.comic_photo(comic_name)
        if found:
            dispatcher.utter_message(text=f"Toma uma foto bonitona do(a) {comic_name}")
            dispatcher.utter_message(image=result)
        else:
            dispatcher.utter_message(text=f"Infelizmente não tenho foto do(a) {comic_name}")
        return [SlotSet("comic_name", comic_name)]

class ActionSaveVote(Action):

    def name(self) -> Text:
        return "action_save_vote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        vote = tracker.get_slot('vote')

        dispatcher.utter_message(text=f"Obrigado por votar, seu voto computado foi {vote}")
        return []
