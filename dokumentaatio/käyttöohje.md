# Käyttöohje
Lataa peli viimeisin [release] lähdekoodi ja unzip source code. 

## Pelin käynnistäminen
Lataa Poetry:
```
poetry install
``` 
Pelin käynnistys komennolla:
```
poetry run invoke start
```

## Pelin etusivu
Kun peli käynnistetään, näkyy etusivu:
![etusivu](./kuvat/etusivu.png)

Paina o nappulasta, jotta peli on koko ruudun tilassa.

Painamalla game instructions voi nähdä ohjeen, miten peliä pelataan.
![howtoplay](./kuvat/how_to_play.png)

Jos haluaa poistua pelistä, niin voi painaa x nappulaa yläkulmasta.

## Peli näkymä
Painamalla Play Easy avaa peli näkymän easy tasolle.
![pelinäkymä](./kuvat/pelinäkymä_easy.png)
Painamalla Play Medium avaa peli näkymän medium tasolle.
![pelinäkymä](./kuvat/pelinäkymä_medium.png)
Painamalla Play Hard avaa peli näkymän hard tasolle.
![pelinäkymä](./kuvat/pelinäkymä_hard.png)

Painamalla quit game voi palata pelin etusivulle. Peli ei tallennu, joten peli alkaa alusta sen jälkeen. Kun kaikki parit on löydetty, sivulla näkyy CONGRATULATIONS<3 eli olet voittanut pelin ja siinä näkyy myös suoritusaika.



