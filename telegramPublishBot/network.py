#!/usr/bin/env python3

import os
import subprocess
import urllib.parse

def postAsync(url, data):
    cmd = ["curl"]
    if type(data) == str:
        cmd += ["--data-ascii", data]
    elif type(data) == dict:
        cmd += ["--data-ascii", urllib.parse.urlencode(data)]

    cmd += [
        "--connect-timeout", "20",
        "--max-time", "100",
        "--retry", "5",
        url,
    ]
    print(cmd)
    print("")
    subprocess.Popen(cmd)
