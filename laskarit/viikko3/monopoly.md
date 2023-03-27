```mermaid
---
title: Monopoly
---
classDiagram
    class Pelaaja{
    Pelaaja : nimi
    Pelaaja : raha (amount) int
    Pelaaja : nappula (2-8)
} --|> class Nappula --> class Pelilauta
class Pelaaja --> class Noppa{
    Noppa: nimi (1/2)
    Noppa: arvo (0-6) int
}
    class Pelilauta{
    Pelilauta: ruudut[40]
} --|> class Ruutu{
    Ruutu: numero (1-40) int
    Ruutu: omistaja (pelaaja)
    Ruutu: arvo int
} --> class Nappula