# ITASEC23 - CTF Workshop

## [OSINT] Chi cerca, trova!!! (17 risoluzioni)

Sto navigando sul [sito dell'azienda](http://www.azienda-losca.tech/).

Leggendo ciò che c'è scritto, sembra che l'azienda si dedichi alla progettazione di software.

Io però non mi fido, sicuramente stanno mentendo come il CERN mente sulla macchina del tempo. Vorrei che indagassi, sono sicuro che cercando attentamente scopriremo qualcosa...

### Soluzione

Navigando sul sito, tra le varie pagine, giungiamo alla pagina `/futuro.html`. Questa pagina presenta una foto e una descrizione che suggerisce la presenza di un'informazione all'interno dell'immagine. Provando a leggere i metadati dell'immagine è possibile trovare la seguente stringa: `Il nome del cavallo è Leonard. Prova a cercare i resoconti delle spese dell'azienda.`.

Quindi provando a usare uno dei seguenti Google Dorks:

- `site:azienda-losca.tech intext:"resoconto"`
- `site:azienda-losca.tech intext:"spese"`

Otterremo una lista di file che terminano con l'estensione `.papera`. In realtà, leggendo i magic bytes o quello che ci suggerisce Google, sono dei file PDF.
Quindi una volta cambiata l'estensione provando a leggere i vari file giungiamo al file chiamato `Resoconto_spese_anno_2010.papera` che contiene uno strano testo. Facendo attenzione, notiamo che termina con un `=`(uguale) e questo suggerisce il fatto che sia stato codificato in base 64. Decodificandolo otteniamo il seguente testo:

```text
La flag non è quì ma la puoi ottenere connettendoti ad un servizio remoto presente su questo server. Il problema è che non mi ricordo la porta. Però so che è composta dal giorno e mese di un evento molto importante per l'azienda. Il formato della porta è questo: ggmm

Quindi, poi, connettiti facendo: nc azienda-losca.challs.itasec.it ggmm
```

Vagando per il sito, nella pagina `/origini.html`, scopriamo che la data di fondazione dell'azienda è il 31 Dicembre 1909. Questa data sembra essere importante, perciò provando ad usarla otteniamo la porta `3112`. Usiamo poi il comando `nc azienda-losca.challs.itasec.it 3112` ed abbiamo ottenuto la flag.
