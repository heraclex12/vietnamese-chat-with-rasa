from rasa_sdk import Action
import requests
import json
import re

# class ActionGetTime(Action):
#
#     def name(self):
#         return 'action_get_times'
#
#     def run(self, dispatcher, tracker, domain):
#         region = tracker.get_slot('timezone')
#         url = 'http://worldtimeapi.org/api/timezone/Asia/' + region.replace(" ", "_")
#         response = requests.get(url).text
#         json_data = json.loads(response)['datetime']
#         dispatcher.utter_message(json_data)
#         return []

class ActionLookUpWordDictionary(Action):
    def name(self):
        return 'action_lookup_word'

    def run(self, dispatcher, tracker, domain):
        word = tracker.get_slot('enword')
        url = 'https://api.tracau.vn/WBBcwnwQpV89/s/{}/en'.format(word)
        response = requests.get(url).text
        json_data = json.loads(response)['tratu'][0]['fields']['fulltext']
        pro = re.search(r"<\s*tr\s+id\s*=\s*\"pa\"[^>]*>.+?<\s*\/\s*tr>", json_data).group()
        tl = re.search(r"<\s*tr\s+id\s*=\s*\"tl\"[^>]*>.+?<\s*\/\s*tr>", json_data).group()
        meanings = re.findall(r"<\s*tr\s+id\s*=\s*\"mn\"[^>]*>.+?<\s*\/\s*tr>", json_data)
        pro = re.sub(r"<\s*[^>]+>", "", pro)
        tl = re.sub(r"<\s*[^>]+>", "", tl)
        for i in range(len(meanings)):
            meanings[i] = re.sub(r"<\s*[^>]+>", "", meanings[i])
        text_respond = "=> " + word + pro.replace("◘", " ")
        text_respond += "\n" + tl.replace("*", "* ")
        for mean in meanings:
            text_respond += "\n" + mean.replace("■", "  -  ")
        dispatcher.utter_message(text_respond)
        return []