```mermaid
---
title: Monopoly
---
classDiagram
    class Pelaaja{
    -nimi
    -raha (amount) int
    -nappula (2-8)
    }
    class Noppa{
    -nimi (1/2)
    -arvo (0-6) int
    }
    class Pelilauta{
    -ruudut[40]
    }
    class Ruutu{
    -numero (1-40) int
    -omistaja (pelaaja)
    -arvo int
    } 
Pelaaja --|> Nappula 
Nappula --> Pelilauta
Pelilauta --|> Ruutu
Ruutu --> Nappula
Pelaaja --> Noppa
 ```