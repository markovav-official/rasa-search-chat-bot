from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionConversionRate(Action):
    def name(self) -> Text:
        return "action_conversion_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        from_currency = next(tracker.get_latest_entity_values("from_currency"), None)
        to_currency = next(tracker.get_latest_entity_values("to_currency"), None)

        if from_currency is None or to_currency is None:
            dispatcher.utter_message(
                text="Sorry, I don't understand what you mean. Please try again.")
            return []
        
        try:
            response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{from_currency.lower()}/{to_currency.lower()}.json").json()
            rate = response[to_currency.lower()]
        except:
            dispatcher.utter_message(
                text="Sorry, I can't find the conversion rate. Please try again.")
            return []
        
        dispatcher.utter_message(text=f"1 {from_currency} = {rate} {to_currency}")

        return []
