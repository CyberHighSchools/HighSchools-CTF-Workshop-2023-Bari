# ITASEC23 - CTF Workshop

## [OSINT] Suonano al citofono... (36 risoluzioni)

Il losco individuo mi ha inviato una foto dicendo di essersi iscritto ad un evento organizzato da un suo amico.

Sei in grado di recuperare il dominio del sito dal quale si è registrato?

Dopo aver trovato il dominio, aiutami a contattare l'admin.

Il formato della flag è: `ITASEC{Nome_Cognome}`

Quindi se per esempio l'admin si chiama "Mario Francesco Rossi", la flag sarà: `ITASEC{Mario_Francesco_Rossi}`

### Soluzione

Vedendo la foto allegata, è possibile notare che sul monitor del computer è visualizzata un'immagine con su scritto ITASEC23. Di conseguenza, cercando online `ITASEC23`, le pagine che escono come risultato presentano la stasse immagine. Leggendo l'URL scopriamo che il dominio è: `itasec.it`.

Addesso che abbiamo il dominio basta cercare i record WHOIS associati. Leggendo i record WHOIS notiamo che il nome dell'admin del dominio è `Paolo Ernesto Prinetto` e quindi la flag è: `ITASEC{Paolo_Ernsesto_Prinetto}`
