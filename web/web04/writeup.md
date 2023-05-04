# ITASEC23 - CTF Workshop

## [web] ITASECshop - 1mln$ Flag (18 risoluzioni)

Per risolvere la challenge, è sufficiente iscriversi alla piattaforma, e accedere alla sezione donazioni:

```python
@app.route('/store/donate', methods=['GET','POST'])
@authorize()
def donate(user:User):
    if request.method == 'POST':
        if not "price" in request.form:
            return render_template("donate.html", user=user, error="La richiesta non è valida", success=False)
        if user.wallet < float(request.form["price"]):
            return render_template("donate.html", user=user, error="Non hai abbastanza soldi", success=False)
        user.wallet -= float(request.form["price"])
        db.session.merge(user)
        db.session.commit()
        return render_template("donate.html", user=user, error=None, success=True)
    return render_template("donate.html", user=user, error=None, success=None)
```

Nelle donazioni, il sito web controlla unicamente che il prezzo sia un numero maggiore o uguale di quello presente nel wallet, e succesivamente sottrae quel valore:

```python
if user.wallet < float(request.form["price"])
[...]
user.wallet -= float(request.form["price"])
```

Il controllo eseguito non è sufficiente, poichè non verifica che il valore sia un numero negativo, che è sempre > del wallet, e che sottratto al valore del wallet va ad incrementare il valore anzichè diminuirlo.

Inserendo ad esempio: `-1000000000` avremo esattamente il milione di dollari necessario a comprare la flag.
