import time
import random
import re

import json
import time
import random

responses = {}
patterns = {}
random_responses = {}

name = ""

def start():
    load_json()
    global name
    name = raw_input("{} Mijn naam is E.C.H.O, wat is jouw naam?\n".format("E.C.H.O: "))
    
    print("{}: Welkom, {} bij E.C.H.O.".format("E.C.H.O: ", name))

    while True:
        listen()

def listen():
    global name
    user_input = raw_input()
    reply = get_reply(user_input)
    if reply is None:
        #TODO: Fix this :)
        reply = random.choice(random_responses)
    print_user_and_bot(name, "E.C.H.O", user_input, reply)

def get_reply(question):
    global responses
    for response in responses:
        for quest in response['questions']:
            if (str(quest)).lower() == str(question).lower():
                return response['response']

def print_user_and_bot(user, bot, message, bot_reply):
    print("{}: {}".format(user, message))
    time.sleep(random.randint(1, 3))
    print("{}: {}".format(bot, bot_reply))
    


def load_json():
    with open('responses.json') as out:
        data = json.load(out)
        global responses
        global patterns
        global random_responses
        responses = data["responses"]
        patterns = data["patterns"]
        random_responses = data["random responses"]

start()