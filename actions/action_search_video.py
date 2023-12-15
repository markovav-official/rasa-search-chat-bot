from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from duckduckgo_search import DDGS


class ActionSearchVideo(Action):
    def name(self) -> Text:
        return "action_search_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = next(tracker.get_latest_entity_values("search_request"), None)

        if request is None:
            dispatcher.utter_message(
                text="Sorry, I don't understand what you mean. Please try again.")
            return []

        with DDGS() as ddgs:
            videos = [i for i in ddgs.videos(request, max_results=1)]
            if not len(videos):
                dispatcher.utter_message(text="Sorry, I couldn't find any video.")
                return []

            video = videos[0]
            url = video['content']
            dispatcher.utter_message(attachment=url)

        return []
