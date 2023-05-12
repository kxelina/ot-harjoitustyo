# Ohjelmistotekniikka, Muistipeli
Muistipelissä on tarkoitus etsiä pareja, jossa on sama numero. Pelaaja voi valita itselle mieluisan tason pelata. Pelajaa valitsee aina kaksi korttia, jos ne ovat parit, niin kortit häviää näytöltä. Jos kortit eivät olleet parit, niin ne kääntyvät nurin päin. 

## Dokumentaatio
- [käyttöohje](./dokumentaatio/käyttöohje.md)
- [vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [changelog](./dokumentaatio/changelog.md)
- [arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [testausdokumentti](./dokumentaatio/testausdokumentti.md)

## Asennus
### Asenna riippuvuudet:
Linkki [Releasiin](https://github.com/kxelina/python-elinanpeli/releases/tag/loppupalautus)

zip-file pitää purkaa

Tarkista, onko uusin python versio (joka tukee tkinker:iä):

```
python3 --version tai python --version
```
Asenna Poetry:
```
poetry install
``` 
## Komennot
### Peli käynnistyy:
```
poetry run invoke start
```
### Testit:
```
poetry run invoke test
```
### Coverage-report:
```
poetry run invoke coverage-report
```
Raportti tulee _htmlcov_ kansioon index tiedostoon

### Pylint:
```
poetry run invoke lint
```

