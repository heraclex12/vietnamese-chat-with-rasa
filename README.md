## How to install
- [Get started with Rasa](https://rasa.com/docs/rasa/user-guide/installation/)
- [Get started with Rasa X](https://rasa.com/docs/rasa-x/installation-and-setup/)
*note: you needn't install RasaX if you dont like
- Rasa-SDK -> pip install rasa-sdk

## Core
- Rasa -> include Rasa NLU and Rasa Core
- Rasa X -> interface to manage data, chat log or teach bot
- Rasa-SDK, using Python to change custom actions

## Where is data?
- data/nlu.md: this is the file which will be trained by Rasa NLU, and it's pattern user message
- data/stories.md: this is timeline the conversations. It match pattern message of users with pattern message of bot
- domain.yml: this is a initialy file (i think so). You will init entities, actions and intents in here

## References: 
 - https://medium.com/@itsromiljain/build-a-conversational-chatbot-with-rasa-stack-and-python-rasa-nlu-b79dfbe59491 -> how to build a rasa chat bot step by step
 - https://github.com/RasaHQ/rasa/pull/1312 -> import file txt to training data

