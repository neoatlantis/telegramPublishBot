#!/usr/bin/env python3

import os
import sys
import yaml

from .token import *



### READ CONFIG

try:
    ACTION = sys.argv[1]
    assert ACTION in ["newtoken", "publish", "serve"]
    if ACTION in ["serve", "publish"]:
        CONFIGFILE = os.path.realpath(sys.argv[2])
        assert os.path.isfile(CONFIGFILE)
except:
    print("Usage: python3 -m telegramPublishBot [newtoken|[publish|serve] <Config File Path>]")
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

config = yaml.load(open(CONFIGFILE, 'r'))

if ACTION == "publish":
    try:
        print("Type in your input...")
        message = sys.stdin.read()
    except KeyboardInterrupt:
        print("Publishing cancelled. Exit.")
        exit()

    from .publisher import *
    from .client import PlainMessage

    message = PlainMessage(message)

    token = config["token"]
    channel = config["channel"]
    print(token)
    print(channel)
    getMe(token)
    print(publishToTelegram(token, channel, str(message)))

elif ACTION == "serve":
    from .server import startServer
    startServer(config)
    exit()
