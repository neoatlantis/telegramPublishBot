#!/usr/bin/env python3

from .selfcheck import selfCheck
selfCheck()

import base64
import requests
import json
import subprocess

from .token import *
from .network import postAsync






class Message:
    def __init__(self, action, **argv):
        self.data = argv
        self.data["action"] = action
    def __str__(self):
        return json.dumps(self.data)
        

class PlainMessage(Message):
    def __init__(self, message, mode="HTML"):
        Message.__init__(self, "sendMessage",
            text=message,
            parse_mode=mode
        )

class PhotoMessage(Message):
    def __init__(self, photo, caption=''):
        Message.__init__(self, "sendPhoto",
            photo=photo,
            caption=caption
        )

class LocationMessage(Message):
    def __init__(self, lat, lng):
        Message.__init__(self, "sendLocation",
            latitude=lat,
            longitude=lng
        )



def publish(url, privateKey, message):
    assert isinstance(message, Message)

    publicToken = derivePublicToken(privateKey)
    if not url.endswith("/"): url += "/"
    url += publicToken + "/publish"
    data = base64.b64encode(sign(privateKey, str(message).encode('utf-8')))

    postAsync(url, data.decode('ascii'))
    return

    r = requests.post(url, data=data)
    print(url)
    print(data)
    print("=" * 30)
    print(r.status_code)
    print(r.text)
    return
