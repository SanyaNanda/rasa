# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
#model is trained here using nlu.md and config.yml
# from rasa_nlu.training_data import load_data
# from rasa_nlu.config import RasaNLUModelConfig
# from rasa_nlu.model import Trainer
# from rasa_nlu import config
#
# # loading the nlu training samples
# training_data = load_data("nlu.md")
#
# # trainer to educate our pipeline
# trainer = Trainer(config.load("config.yml"))
#
# # train the model!
# interpreter = trainer.train(training_data)
#
# # store it for future use
# model_directory = trainer.persist("./models/nlu", fixed_model_name="current")
#
# from rasa_core.actions import Action
# from rasa_core.events import SlotSet
# from IPython.core.display import Image, display
#
# import requests
#
# class ApiAction(Action):
#     def name(self):
#         return "action_get_help"
#
#     def run(self, dispatcher, tracker, domain):
#
#         group = tracker.get_slot('services','contact','ts','company')
#
#         r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(group))
#         response = r.content.decode()
#         response = response.replace('["',"")
#         response = response.replace('"]',"")
# from rasa_core.policies import KerasPolicy, MemoizationPolicy
# from rasa_core.agent import Agent
#
# agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])
#
# # loading our neatly defined training dialogues
# training_data = agent.load_data('stories.md')
# 
# agent.train(
#     training_data,
#     validation_split=0.1,
#     epochs=50
# )
#
# agent.persist('models/dialogue')
# from rasa_core.agent import Agent
# agent = Agent.load('models/dialogue', interpreter=model_directory)
