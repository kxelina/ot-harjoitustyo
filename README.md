# Ohjelmistotekniikka, Muistipeli
Muistipelissä on tarkoitus etsiä pareja, jossa on sama numero.

## Dokumentaatio
- [vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [changelog](./dokumentaatio/changelog.md)
- [arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Asennus
### Asenna riippuvuudet:
```
- poetry install
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
