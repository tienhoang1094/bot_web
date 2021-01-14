from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class HealthForm(FormAction):

    def name(self):
        return "health_form"

    @staticmethod
    def required_slots(tracker):

        return ["name", "number_people",
         "order_time", "phone_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [
                self.from_entity(entity="name"),
            ],
            "number_people": [
                self.from_entity(entity="number_people"),
            ],
            "order_time": [
                self.from_entity(entity="order_time"),
            ],
            "phone_number": [
                self.from_entity(entity="phone_number"),
            ],
        }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []

