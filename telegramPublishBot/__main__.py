#!/usr/bin/env python3

import os
import sys
import yaml

from .token import *



### READ CONFIG

try:
    ACTION = sys.argv[1]
    assert ACTION in ["newtoken", "publish", "serve", "connect"]
    if ACTION == "connect":
        URL, PRIVATE_TOKEN = sys.argv[2:][:2]
    elif ACTION in ["serve", "publish"]:
        CONFIGFILE = os.path.realpath(sys.argv[2])
        assert os.path.isfile(CONFIGFILE)
except:
    print("Usage: python3 -m telegramPublishBot [newtoken|connect <Server URL> <Private Token>|[publish|serve] <Config File Path>]")
    sys.exit(1)


##############################################################################

if ACTION == "newtoken":
    tokenPair = newToken()
    print("Token generated. Please record:")
    print(" - private token(keep this secret!):\t%s" % tokenPair["private"])
    print(" - public token:                    \t%s" % tokenPair["public"])
    exit()

##############################################################################

# Otherwise: serve as a server, or publish from CLI

if ACTION in ["publish", "serve"]:
    config = yaml.load(open(CONFIGFILE, 'r'))

if ACTION in ["publish", "connect"]:
    try:
        print("Type in your input...")
        message = sys.stdin.read()
    except KeyboardInterrupt:
        print("Publishing cancelled. Exit.")
        exit()

    if ACTION == "publish":
        from .publisher import *
        token = config["token"]
        channel = config["channel"]
        print(token)
        print(channel)
        getMe(token)
        print(publishToTelegram(token, channel, message))
    else:
        from .client import *
        print(URL)
        print(PRIVATE_TOKEN)
        print(connectToPublisher(URL, PRIVATE_TOKEN, message))

    exit()


if ACTION == "serve":
    from .server import startServer
    startServer(config)
    exit()
