# ITASEC23 - CTF Workshop

## [crypto] Bad at math (5 risoluzioni)

Calcolare le chiavi private

```
log_13(371293)=5
log_13(28561)=4
```

Calcolare la chiave condivisa:

```
(13**5)**4 = 1208925819614629174706176
```

Sottrarre dal messaggio criptato la chiave:

```
23920026561960852065946-1208925819614629174706176=4915062787080052627145
```

Usare Cyberchef to base per decifrare:

https://gchq.github.io/CyberChef/#recipe=To_Base(36)&input=NDkxNTA2Mjc4NzA4MDA1MjYyNzE0NQ
