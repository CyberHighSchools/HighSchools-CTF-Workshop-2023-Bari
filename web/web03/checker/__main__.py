#!/bin/python3

import os
import sys

import requests
import binascii
import re

endpoint = "/static/js/suspiciousLookingJs.js"

# Se challenge web
URL = os.getenv('URL', 'http://cookie.challs.itasec.it')

# risolvo la challenge
jsfile = requests.get(URL + endpoint).text
base64_flag = re.search('(flag = \")(\S+)\"', jsfile).group(2)
hex_flag = binascii.a2b_base64(base64_flag).replace(b' ', b'')
flag = binascii.unhexlify(hex_flag)
# Stampo la flag
print(flag)
