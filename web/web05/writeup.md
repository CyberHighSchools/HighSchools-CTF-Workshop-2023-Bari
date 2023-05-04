# ITASEC23 - CTF Workshop

## [web] ITASECshop - Fridge Flag (11 risoluzioni)

Per risolvere la challenge, bisogna aver risolto la challenge precedente "ITASECshop - 1mln$ Flag" per poter arrivare al denaro necessario per comprare la flag.

Questa flag ha però un controllo aggiuntivo:

```python
if not "Samsung Smart Fridge" in request.headers.get("User-Agent"):
    return render_template("article.html", user=user, article=article, error="Solo i Samsung Smart Fridge possono acquistare questo articolo", success=False)
```

Solo per questa flag, il servizio web controlla che la richiesta arrivi da un "Samsung Smart Fridge" tramite lo user agent.

L'User-Agent è controllabile totalmente dall'utente e modificabile in più modi:

1. Estensione Chrome (ad esempio [questa](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg))
   Tramite alucne estensioni online è possibile decidere che user agent inserire nelle richieste che facciamo
2. [Burpsite](https://portswigger.net/burp)/[Postman](https://www.postman.com/) ecc...
   Tramite la modifica diretta dell'header da inviare

Modificato l'user agent, sarà sufficiente contenga "Samsung Smart Fridge" e la flag potrà essere acquistata e visualizzata
