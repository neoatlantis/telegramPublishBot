#!/usr/bin/env python3

from bottle import *
import base64

from .publisher import *
from .token import *

__CONFIG = None


@get("/")
def hello():
    return "Publish to telegram channels."

@get("/<token:re:pub:[0-9a-z]+>/test")
def test(token):
    global __CONFIG
    if token in __CONFIG["authorized"]:
        return "%s is okay." % token
    return abort(404, "This token is not registered.")

@post("/<token:re:pub:[0-9a-z]+>/publish")
def publish(token):
    global __CONFIG
    if token not in __CONFIG["authorized"]:
        return abort(401, "Unauthorized access with this token.")

    try:
        data = verify(token, base64.b64decode(request.body.read()))
        assert data != None
        data = data.decode('utf-8')
    except:
        return abort(400, "No valid data received for this token.")

    publishToTelegram(__CONFIG["token"], __CONFIG["channel"], data)
        
    return data







def startServer(config):
    global __CONFIG
    __CONFIG = config
    run(host="127.0.0.1", port=3113)
