#!/usr/bin/env python3

import os
import sys
import yaml

from .token import *



### READ CONFIG

try:
    ACTION = sys.argv[1]
    assert ACTION in ["newtoken", "serve"]
    if ACTION in ["serve", "publish"]:
        CONFIGFILE = os.path.realpath(sys.argv[2])
        assert os.path.isfile(CONFIGFILE)
except:
    print("Usage: python3 -m telegramPublishBot [newtoken|serve <Config File Path>]")
    sys.exit(1)

if ACTION == "newtoken":
    tokenPair = newToken()
    print("Token generated. Please record:")
    print(" - private token(keep this secret!):\t%s" % tokenPair["private"])
    print(" - public token:                    \t%s" % tokenPair["public"])
    exit()

if ACTION == "serve":
    from .server import startServer
    config = yaml.load(open(CONFIGFILE, 'r'))
    print(config)
    startServer(config)
    exit()
