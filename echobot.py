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

def pattern(phrase):
        for pattern in patterns:
                match = re.match(pattern['pattern'].lower(), phrase.lower())
                if match:
                        return random.choice(pattern['responses']).format(match.group(1).replace("!", "").replace("?", ""))
def swap_pronouns(phrase):
        if phrase.endswith("?"):
                return phrase
        if 'i ' in phrase.lower():
                return re.sub('am', 'are', re.sub('I', 'you', phrase.lower()))
        if 'my ' in phrase.lower():
                return  re.sub('my', 'you', re.sub('my', 'you', phrase.lower()))
        if 'you ' in phrase.lower():
                return re.sub('you', 'I', re.sub('are', 'am', phrase.lower()))
        else: 
                return None


def start():
    load_json()
    global name
    name = raw_input("{} My name is E.C.H.O, what is your name?\n".format("E.C.H.O: "))
    
    print("{}: Welcome, {} at E.C.H.O.".format("E.C.H.O: ", name))

    while True:
        listen()

def listen():
    global name
    user_input = raw_input()
    reply = get_reply(user_input)
    if reply is None:
        reply = random.choice(random_responses)
    print_user_and_bot(name, "E.C.H.O", user_input, reply)

def get_reply(question):
    global responses
    if pattern(question):
            if swap_pronouns(pattern(question)):
                    return pattern(question)
            return pattern(question)
    if swap_pronouns(question):
        return swap_pronouns(question)
    for response in responses:
            if question.lower() in response['question'].lower():
                    if swap_pronouns(response['response']):
                            return swap_pronouns(response['response'])
                    else:
                            return response['response']
    return question

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