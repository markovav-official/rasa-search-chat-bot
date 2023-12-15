from typing import Any, Dict, List, Text

from duckduckgo_search import DDGS
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSearchAnswer(Action):
    def name(self) -> Text:
        return "action_search_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = next(tracker.get_latest_entity_values("search_request"), None)

        if request is None:
            dispatcher.utter_message(text="Sorry, I don't understand what you mean. Please try again.")
            return []

        with DDGS() as ddgs:
            answers = [i for i in ddgs.answers(request)]
            if not len(answers):
                dispatcher.utter_message(text="Sorry, I couldn't find any answer.")
                return []

            answer = answers[0]
            text = answer['text']
            dispatcher.utter_message(text=text)

        return []
