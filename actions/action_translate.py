from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from duckduckgo_search import DDGS

languages = {
    'russian': 'ru',
    'spanish': 'es',
    'english': 'en',
    'swedish': 'sv',
    'finnish': 'fi',
}


class ActionTranslate(Action):
    def name(self) -> Text:
        return "action_translate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = next(tracker.get_latest_entity_values("search_request"), None)
        language = next(tracker.get_latest_entity_values("language"), None)

        if request is None or language is None or language not in languages:
            dispatcher.utter_message(
                text="Sorry, I don't understand what you mean. Please try again.")
            return []

        try:
            with DDGS() as ddgs:
                translated_response = ddgs.translate(request, to=languages[language])
                translated = translated_response['translated']
        except:
            dispatcher.utter_message(
                text="Sorry, I can't translate this. Please try again.")
            return []
        
        dispatcher.utter_message(text=translated)

        return []
