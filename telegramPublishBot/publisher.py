#!/usr/bin/env python3

from .token import *
import requests

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
    

def publishToTelegram(token, channel, text):
    url = URL(token, "sendMessage")
    print(url)
    payload = {
        "chat_id": channel,
        "text": text,
    }
    r = requests.post(url, data = payload)
    print(r.status_code)
    print(r.text)
    return r.status_code
