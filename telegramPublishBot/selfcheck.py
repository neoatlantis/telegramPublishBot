#!/usr/bin/env python3

def selfCheck():
    try:
        import sys
        if sys.version_info[0] < 3:
            raise Exception("You need python3 to start this!")

        import os
        import subprocess
        import base64
        import requests
        import json
        import yaml
        import urllib.parse
        import bottle
        import nacl
        
        subprocess.check_output(["curl", "--version"])
    except Exception as e:
        raise Exception("""
------------------------------------------------------------------------------
telegramPublishBot cannot start. Make sure you've installed all modules as
specified in requirements.txt. And you need to install `curl` on your system.

Details:
%s
------------------------------------------------------------------------------
""" % e)
