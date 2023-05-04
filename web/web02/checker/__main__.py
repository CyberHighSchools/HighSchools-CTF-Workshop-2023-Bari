#!/bin/python3

import os
import requests
import base64
import re


# Se challenge web
URL = os.getenv('URL', 'http://cookie.challs.itasec.it')
endpoint = "/static/js/main.js"

# risolvo la challenge
jsfile = requests.get(URL + endpoint).text
flag = re.search('(sus = \")(\S+)\"', jsfile).group(2)
# Stampo la flag
print(base64.b64decode(flag))
