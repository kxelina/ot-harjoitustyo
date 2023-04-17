###Arkkitehtuurikuvaus

##Sovelluslogiikka

```mermaid
---
title: sovellulogiikan classdiagram (luonnos)
---
classDiagram
class card{
    - suit
    - value
    - display
    - game
    - ui_card
    - column
    - row
}
class card_suit
class game{
    - level
    - deck
    - start_time
    - root
}
card --> card_suit
```
![pakkauskuva.png](./kuvat/pakkauskuva.png)
