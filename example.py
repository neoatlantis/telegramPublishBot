#!/usr/bin/env python3

import sys
from telegramPublishBot.client import *


try:
    url, private_token = sys.argv[1:][:2]
except:
    print("Usage: python3 example.py URL TOKEN_FOR_SERVER")
    exit(1)

print(url)
print(private_token)

publish(url, private_token, PlainMessage("Hello, world!"))
publish(url, private_token, LocationMessage(51.0, 10.0))
publish(url, private_token, PhotoMessage(\
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Gustav_chocolate.jpg/420px-Gustav_chocolate.jpg"))
