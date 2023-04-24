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
python3 --version tai python --version
```
Asenna Poetry:
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
