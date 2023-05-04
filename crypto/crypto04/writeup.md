# ITASEC23 - CTF Workshop

## [crypto] CryptoMeme (28 risoluzioni)

Per risolvere la challenge è necessario:

1. [decifrare con CyberChef](<https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,25)&input=SEpWTUpWVFdKSEZPRlNG>) la chiave cifrata in ROT25, il cui risultato sarà la chiave: `GIULIUSVIGENERE`.
2. decifrare con un qualsiasi tool la flag cifrata con Vigenere con la chiave `GIULIUSVIGENERE` e il risultato sarà `ITASEC{CHAD_CAESAR_BASED_BLAISE}`.
