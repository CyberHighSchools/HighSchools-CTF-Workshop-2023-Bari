import os

basedir = os.path.abspath(os.path.dirname(__file__))

#cat_food = "---P4ssw0rd$$$$$$uperSicura@@###!meaw---"

static_articles = [
    {
        "title":"1.000.000$ FLAG 🚩",
        "description":"Acquista una flag antica 1.000.000 di anni fa, vale 1$ per ogni anno di vita. Affrettati a comprarla!",
        "price":1_000_000.00,
        "img":"/static/imgs/art6.png",
        "secret_content": f"""
Hai davvero speso 1.000.000$ di dollari per una flag?
Ecco un tutorial per la prossima volta:
<iframe width="560" height="315" src="https://www.youtube.com/embed/KEkrWRHCDQU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
e la tua flag: {os.getenv('FLAG1','ITASEC{REDACTED1}')}
"""
    },
    {
        "title":"Maglietta ITASEC",
        "description":"La maglietta ufficiale di ITASEC23 🤖",
        "price":21.40,
        "img":"/static/imgs/art0.png",
        "secret_content": "Le magliette sono finite, ecco a te un floppydisk di ITASEC23 💾"
    },
    {
        "title":"Cappello Gatto 😺",
        "description":"Descrizione Articolo 1",
        "price":8.0,
        "img":"/static/imgs/art4.png",
        "secret_content": "🎩🐈"
    },
    {
        "title":"Cuscino ITASEC",
        "description":"La cuscino ufficiale di ITASEC23 💤",
        "price":2.25,
        "img":"/static/imgs/art1.png",
        "secret_content": "Mi dispiace era una truffa, non c'è nessun cuscino 😵‍💫"
    },
    {
        "title":"-10°C FLAG 🚩",
        "description":"Questa flag deve essere conservata a -10°C, hai bisogno di un 'Samsung Smart Fridge' per poterla acquistare'",
        "price":4_599.98,
        "img":"/static/imgs/art7.png",
        "secret_content": f"""
<img src="/static/imgs/samsung_smart_fridge.png" >
{os.getenv('FLAG2','ITASEC{REDACTED2}')} 
"""
    },
    {
        "title":"Maglietta Pwnzer0tt1",
        "description":"La maglietta ufficiale dei Pwnzer0tt1 🍕 (solo per i più forti)",
        "price":20.50,
        "img":"/static/imgs/art2.png",
        "secret_content": "La maglietta migliore 🍕, quella dei M0nt3c4rl0 è abbastanza brutta non credi? 🤔"
    },
    {
        "title":"Maglietta M0nt3c4rl0",
        "description":"La maglietta ufficiale dei M0nt3c4rl0 🎲 (solo per i più forti)",
        "price":20.50,
        "img":"/static/imgs/art3.png",
        "secret_content": "La maglietta migliore 🎲, quella dei Pwnzer0tt1 è abbastanza brutta non credi? 🤔"
    },
    {
        "title":"STACCAH! STACCAH!",
        "description":"CI STANNO TRACCIANDO! STACCAH 🔌",
        "price":0.01,
        "img":"/static/imgs/art5.png",
        "secret_content": f"""
        <iframe width="560" height="315" src="https://www.youtube.com/embed/oE5JTpoIYck" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        """
    },


]