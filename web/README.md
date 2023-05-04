# ITASEC2023 - Web challenges

Challenge web per l'HighSchools CTF Workshop di ITASEC2023 @ Bari - 02/05/2023

## Challenges

| Category | Title                             | Author                                                     | Dynamic            | Type  | Url                         | Port  |
| :------- | :-------------------------------- | :--------------------------------------------------------- | :----------------: | ----: | --------------------------: | :---: |
| web      | [Galleria Vettoriale](web01)      | Vito Cafagno <@Alcu.ino>                                   | :heavy_check_mark: | http  | vectorial.challs.itasec.it  | 8083  |
| web      | [CookieC(TF)liker1](web02)        | Gianluca Parisi <@whyn0>                                   | :heavy_check_mark: | http  | cookie.challs.itasec.it     | 8084  |
| web      | [CookieC(TF)liker2](web03)        | Gianluca Parisi <@whyn0>                                   | :heavy_check_mark: | http  | cookie.challs.itasec.it     | 8084  |
| web      | [ITASECshop - 1mln$ Flag](web04)  | Domingo Dirutigliano <@DomySh>, Vincenzo Turturro <@Sush1> | :heavy_check_mark: | http  | itasecshop.challs.itasec.it | 8085  |
| web      | [ITASECshop - Fridge Flag](web05) | Domingo Dirutigliano <@DomySh>, Vincenzo Turturro <@Sush1> | :heavy_check_mark: | http  | itasecshop.challs.itasec.it | 8085  |
| web      | [ITASECshop - H4ck3d](web06)      | Domingo Dirutigliano <@DomySh>, Vincenzo Turturro <@Sush1> | :heavy_check_mark: | http  | itasecshop.challs.itasec.it | 8085  |

## Struttura challenge

- `/authors.txt`: Autori delle challenge (uno per riga)
- `/title.txt`: Titolo della challenge
- `/description.md`: Descrizione pubblica della challenge da mettere in piattaforma
- `/flags.txt`: Flag delle challenge (uno per riga), usare il format `^...$` per definire una regex
- `/points.txt`: Punteggio della challenge (statico: `score`, dinamico: `max,min,decay`)
- `/endpoint.txt`: Endpoint di deployment della challenge (formato: `{tcp/http},$HOST,$PORT`)
- `/tags.txt`: Tag visibili della challenge (comma-separated)
- `/tags-hidden.txt`: Tag nascosti della challenge (comma-separated)
- `/order.txt`: Indice delle challenga per l'ordine
- `/timeout.txt`: Timeout di esecuzione in secondi per il checker
- `/writeup.md`: Soluzione (privata) della challenge
- `/writeup`: Cartella per risorse del writeup (es. immagini)
- `/attachments/*`: File da allegare in piattaforma
- `/src/*`: Sorgenti necessari per generare la challenge
- `/hints/hint{1,2,...}.md`: Hint della challenge, mettere `_` come prefix per ignorare l'hint
- `/solution.*`: Soluzione challenge
- `/checker/*`: File necessari per il checker
- `/checker/__main__.py`: Checker python che stampa la flag

## Tips

- Dare nomi significativi agli allegati scaricabili (evitare i soliti challenge.py e output.txt)
- Non hardcodare i nomi dei container docker nella challenge (usare le variabili di ambiente)
- Se possibile, non hardcodare flag nella challenge (usare le variabili di ambiente)
- Challenge whitebox > blackbox
- Fissare sempre tutte le versioni delle dipendenze (pip, node, docker, ...)
- Caricare sempre tutti i file necessari alla generazione della challenge (es: sorgenti per i binari)
- Documentare bene ogni parte della challenge (installazione, compilazioni con Makefile, ...)
- Testare sempre le challenge anche su un server remoto e non solo in locale (tenere in considerazione l'overhead della comunicazione in remoto)
- Eseguire test di carico per le challenge pesanti (es: le crypto con Sagemath)
- Aggiungere sempre dei timeout per i servizi remoti per evitare connessioni aperte pendenti (-t/-T con socat)
- Fare enforcing dei permessi nei container per limitare le azioni degli utenti
