import requests

print(requests.get(
    'http://vectorial.challs.itasec.it/4.jpeg').headers['X-Flag'])
