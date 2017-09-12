#!/usr/bin/env python3

import requests
import json
from .token import *
from .network import postAsync


URL = lambda token, method:\
    "https://api.telegram.org/bot%s/%s" % (token, method)

def getMe(token):
    url = URL(token, "getMe")
    r = requests.get(url)
    try:
        j = r.json()
        return j["ok"] == True
    except:
        return False
    

def publishToTelegram(token, channel, data):
    try:
        assert type(data) in [str, bytes]
        if type(data) == bytes:
            data = data.decode('utf-8')
        data = json.loads(data)
    except:
        raise Exception("Data sent to server must be stringified JSON.")

    action = data["action"]
    legitKeys = {
        "sendMessage": ["text", "parse_mode"],
        "sendPhoto": ["photo", "caption"],
        "sendLocation": ["latitude", "longitude"],
    }

    assert action in legitKeys

    url = URL(token, action)
    print(url)
    
    payload = {
        "chat_id": channel,
    }

    for key in data:
        if key in legitKeys[action]:
            payload[key] = data[key]

    postAsync(url, payload)
    return

    r = requests.post(url, data = payload)
    print(r.status_code)
    print(r.text)
    return r.status_code
