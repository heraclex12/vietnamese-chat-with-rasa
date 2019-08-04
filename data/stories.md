## happy path
* greet
  - utter_hello
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_hello
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_hello
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## fallback
  - utter_default

## thank you
* thanks
  - utter_nothing
  - utter_nextwork

## say time_zone
* time_zone
  - utter_timez
  - action_get_times

## say introduce
* introduce
  - utter_introduce

## goodnight
* goodnight
  - utter_thanks
  - utter_goodnight

## ask author
* ask_author
  - utter_author

## help
* help
  - utter_reply_help

## suprise
* suprise
  - utter_suprise

## ask relationship
* ask_relationship
  - utter_reply_relationship

## ask_information path
* wat_name
  - utter_wat_name
* how_old
  - utter_how_old
* gender
  - utter_gender
* address
  - utter_address

## how are u
* how_are_u
  - utter_how_are_u

## sing poem
* sing_poem
  - utter_sing_poem

## comedy_story
* comedy_story
  - utter_comedy_story

## affirm
* affirm
  - utter_nextwork

