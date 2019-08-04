from rasa_core_sdk import Action
import requests
import json

class ActionGetTime(Action):

    def name(self):
        return 'action_get_times'

    def run(self, dispatcher, tracker, domain):
        region = tracker.get_slot('timezone')
        url = 'http://worldtimeapi.org/api/timezone/Asia/' + region.replace(" ", "_")
        response = requests.get(url).text
        json_data = json.loads(response)['datetime']
        dispatcher.utter_message(json_data)
        return []
