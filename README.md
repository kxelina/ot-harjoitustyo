# Ohjelmistotekniikka, Muistipeli
Muistipelissä on tarkoitus etsiä pareja, jossa on sama numero.

## Dokumentaatio
- [vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [changelog](./dokumentaatio/changelog.md)
- [arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Asennus
### Asenna riippuvuudet:
Tarkista, onko uusin python versio:

```
- python3 --version tai python --version
```
Asenna Poetry (Linux tai MacOS):
```
- curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
- poetry install
``` 
Linkki Releasiin:
```
- https://github.com/kxelina/python-elinanpeli/releases/tag/viikko5
```
## Komennot
### Peli käynnistyy:
```
- poetry run invoke start
```
### Testit:
```
-poetry run invoke test
```
### Coverage-report:
```
-poetry run invoke coverage-report
```
Raportti tulee _htmlcov_ kansioon index tiedostoon

### Pylint:
```
-poetry run invoke lint
```
