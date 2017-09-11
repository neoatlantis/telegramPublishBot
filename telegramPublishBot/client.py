#!/usr/bin/env python3

import base64
import requests

from .token import *


def connectToPublisher(url, privateKey, message):
    publicToken = derivePublicToken(privateKey)
    if not url.endswith("/"): url += "/"
    url += publicToken + "/publish"
    data = base64.b64encode(sign(privateKey, message.encode('utf-8')))
    r = requests.post(url, data=data)
    print(url)
    print(data)
    print("=" * 30)
    print(r.status_code)
    print(r.text)
    return
