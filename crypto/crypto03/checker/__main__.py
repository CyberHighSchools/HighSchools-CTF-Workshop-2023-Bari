#!/bin/python3

from os import getenv
from bs4 import BeautifulSoup
import requests
import json

URL = getenv('URL', 'http://xorlandia.challs.itasec.it:8080')


def xor(a, b): return bytes([int(x) ^ int(y)
                             for x, y in zip(a, b)])  # from danidisp import xor


def encrypt(plain: bytes, key: bytes) -> str:
    if len(key) == 0:
        return ''
    if len(key) < len(plain):
        key = key * (len(plain)//len(key) + 1)
    return xor(plain, key).hex()


r = requests.get(URL)
page = BeautifulSoup(r.text, 'html.parser')
flag_enc = page.find('input', {'name': 'testo'})['value']

r = requests.post(f'{URL}/api/xor', json={'text': flag_enc, 'key': 'gabibbo'})
flag = json.loads(r.text)['ascii']
print(flag)
