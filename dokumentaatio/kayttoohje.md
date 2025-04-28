# Käyttöohje

## Lataaminen
---
Uusimman version voit ladata suoraan painamalla pääsivulta Code->Download Zip, tai valita [julkaisun](https://github.com/hfhenri/ot-harjoitustyo/releases)
---
## Asentaminen ja käynnistäminen
---
Asenna riippuvuudet komennolla:

```bash
poetry install
```

Käynnistä komennolla

```bash
poetry run invoke start
```
---
## Pelin toiminnot

Pelillä on hyvin yksinkertainen idea. Näyttöä klikaamalla asetat valitsemasi pikselin.

![](./kuvat/peli.png)

Käyttöliittymän yläkohdasta voi valita pikselin tyypin:

![](./kuvat/pikseli_valikko.png)

Oikealla on eri toimintoja pelin säätämiseen:

![](./kuvat/nappain_valikko.png)

Save-näppäimestä voit tallentaa pelin tietokantaan:

![](./kuvat/save_valikko.png)

Load-näppäimestä voit ladata pelin tietokannasta sekä poistaa pelejä:

![](./kuvat/load_valikko.png)

Settings-näppäimestä voit säätää simulaation nopeutta sekä ruudun kokoa:

![](./kuvat/settings_valikko.png)



