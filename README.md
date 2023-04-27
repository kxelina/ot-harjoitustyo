# Ohjelmistotekniikka, Muistipeli
Muistipelissä on tarkoitus etsiä pareja, jossa on sama numero.

## Dokumentaatio
- [käyttöohje](./dokumentaatio/käyttöohje.md)
- [vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [changelog](./dokumentaatio/changelog.md)
- [arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Asennus
### Asenna riippuvuudet:
Tarkista, onko uusin python versio (joka tukee tkinker:iä):

```
python3 --version tai python --version
```
Asenna Poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
```
```
poetry install
``` 
Linkki Releasiin:
[Release](https://github.com/kxelina/python-elinanpeli/releases/tag/viikko5palautus)
```
- zip-file pitää purkaa
```
## Komennot
### Peli käynnistyy:
```
poetry run invoke start
```
- peli toimii full screen mode:ssa eli laita peli full screen mode:iin
### Testit:
```
poetry run invoke test
```
### Coverage-report:
Komento pitää suorittaa src hakemistossa.
```
poetry run invoke coverage-report
```
Raportti tulee _htmlcov_ kansioon index tiedostoon

### Pylint:
```
poetry run invoke lint
```

