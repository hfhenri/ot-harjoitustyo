# Ohjelmistotekniikka, harjoitustyö

## Hiekka/Hiukkassimulaattori peli

Peli on fysiikkapohjainen hiekkalaatikko, jossa erilaiset pikselit/hiukkaset, kuten hiekka, vesi ja laava, ovat vuorovaikutuksessa toistensa kanssa painovoiman ja eri sääntöjensä perusteella.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Asentaminen

Riippuvuuksien asentaminen:

```bash
poetry install
```

Aloitus toimenpiteet:

```bash
poetry run invoke build
```

## Toiminnot

### Sovelluksen suorittaminen

```bash
poetry run invoke start
```

### Testaaminen

```bash
poetry run invoke test
```

### Testikattavuus

```bash
poetry run invoke coverage-report
```

### Pylint-tarkistus

```bash
poetry run pylint src
```


