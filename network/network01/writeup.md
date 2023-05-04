# ITASEC23 - CTF Workshop

## [network] Basic Shark (16 risoluzioni)

La flag è nascosta nell'header Authorization.

Per estrarre la flag, filtrare i pacchetti con il filtro http.authorization, dopodicchè controllare le Crendentials dei vari pacchetti.

![Wireshark http.authorization filter](writeup/wireshark_filter.png)
