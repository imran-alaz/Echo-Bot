import time
import random
import re

import json

responses = {}
patterns = {}

def start():
    load_json()


def load_json():
    with open('responses.json') as out:
        data = json.load(out)
        global responses
        global patterns
        responses = data["responses"]
        patterns = data["patterns"]

start()