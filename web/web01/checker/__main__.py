#!/bin/python3

import os
import sys

import requests
from pwn import *

# Se challenge web
URL = os.getenv('URL', 'http://vectorial.challs.itasec.it')

# risolvo la challenge
flag = requests.get(
    'http://vectorial.challs.itasec.it/4.jpeg').headers['X-Flag']

# Stampo la flag
print(flag)
