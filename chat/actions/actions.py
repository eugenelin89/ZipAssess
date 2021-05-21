# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import logging
logger = logging.getLogger(__name__)

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="Hello World!")

        return []

class ActionGetChallenge(Action):

    def name(self):
        return "action_get_challenge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        # set slots question1 question2 and question3
        logger.info("Run ActionGetChallenge")

        #dispatcher.utter_message(text="Get Challenge: Now?")
        logger.info("Run ActionGetChallenge2")
        return [SlotSet("question1","what is 2 + 2?"), SlotSet("question2","what is 3 plus 3?"), SlotSet("question3","What is 4+4?")]
