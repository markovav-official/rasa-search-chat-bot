import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from duckduckgo_search import DDGS


class ActionSearchImage(Action):
    def name(self) -> Text:
        return "action_search_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = next(tracker.get_latest_entity_values("search_request"), None)

        if request is None:
            dispatcher.utter_message(text="Sorry, I don't understand what you mean. Please try again.")
            return []

        with DDGS() as ddgs:
            images = [i for i in ddgs.images(request, max_results=10)]
            if not len(images):
                dispatcher.utter_message(text="Sorry, I couldn't find any image.")
                return []

            random_image = random.choice(images)
            url = random_image['thumbnail']
            dispatcher.utter_message(image=url)

        return []
