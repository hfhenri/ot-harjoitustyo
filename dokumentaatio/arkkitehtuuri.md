# Arkkitehtuuri

## Tiedostot ja kansiot

```plaintext
├── app.py              # Sovelluksen pääsilmukka ja aloituskohta
├── ui.py               # Tkinter-käyttöliittymä
├── simulation.py       # Simulaation ydin
├── database.py         # Tietokanta 
└── pixels/             # Kaikkien pikselityyppien määritelmät ja niihin liittyvät funktiot
    ├── empty.py        # Tyhjä pikseli
    ├── sand.py         # Hiekka pikseli
    ├── water.py        # Vesi pikseli
    ├── lava.py         # Laava pikseli
    ├── oil.py          # Öljy pikseli
    ├── steam.py        # Öljy pikseli
    ├── fire.py         # Tuli pikseli
    ├── wood.py         # Puu pikseli
    ├── stone.py        # Kivi pikseli
    ├── shared.py       # Apu funktiot
    └── liquid.py       # Nestemäisten pikselien logiikka
```

---
## Käyttöliittymä (ui.py)

Moduuli sisältää:  

- `Ui`-luokan, joka luo Tkinter-ikkunan ja näyttää pelin `PhotoImage`-oliona.  
- Tyyppivalinta-, tallennus- ja latauspainikkeet.
- Painikkeet simulaatioasetusten säätöön ja tallennettujen pelien hallintaan.

Käyttöliittymä kutsuu `App`-luokan metodiketoja käyttäjän toimiessa ja päivittää näkymän `movement_queue`-jonon perusteella.

---
## Simulaatio (simulation.py)

- **Grid**: Lista (`grid[x][y]`) joka sisältää pikseli-olioita.
- **movement_queue**: Jonotus muuttuneille pikseleille käyttöliittymän päivitystä varten.

**Simulaation kulku:**
1. Nollataan `updated`-liput.
2. Kutsutaan jokaisen pikselin `step(simulation)`-metodia.
3. Mikäli `step` palauttaa `True`, lisätään pikseli `movement_queue`-jonoon.

---
## Tietokanta (database.py)

- SQLite-tietokanta yhdistetään tiedostoihin `saves.db`.  
- Käyttäjä voi **tallentaa**, **ladata**, **listata** ja **poistaa** pelisessioita.
- Pelin tila muunnetaan JSON-muotoon, joka tallenetaan tietokantaan.

```mermaid
classDiagram
    class Database {
      + save_game(name, sim: Simulation)
      + load_game(id)
      + list_saves()
      + delete_save(id)
    }
```

---
## Pikselit (pixels/)

Jokainen tiedosto `pixels/*.py` määrittelee luokan, jolla on ainakin:

- `type_id`: tunniste.
- `color`: piirtoväri.
- `step(simulation)`-metodi: käyttäytymislogiikka (putoaminen, nouseminen, leviäminen, reaktiot).
- `move_self(x,y)`-metodi: koordinaattien päivitys.

```mermaid
classDiagram
    class Sand {
      + step(sim)
    }
    class Water {
      + step(sim)
    }
    class Lava {
      + step(sim)
    }
    class Oil {
      + step(sim)
    }
    class Steam {
      + step(sim)
    }
    class Fire {
      + step(sim)
    }
    class Wood {
      + step(sim)
    }
    class Stone {
      + step(sim)
    }
    class Liquid
    Water --|> Liquid
    Lava --|> Liquid
    Oil --|> Liquid
    Steam --|> Liquid
```

---
## Kaavio ohjelman silmukan kierroksesta

```mermaid
sequenceDiagram
    participant App
    participant Simulation
    participant UI
    participant DB

    App->>Simulation: simulate()
    Simulation-->>Simulation: .step() jokaiselle pikselille
    Simulation->>UI: liitä muutuneet pikselit (@movement_queue)
    UI-->>App: käyttäjän syötteet (lisäys, tallennus, lataus, poisto)
    alt Tallennus
        App->>DB: save_game()
        DB-->>App: commit
    end
    alt Lataus / Poisto
        App->>DB: list_saves()/load_game()/delete_save()
        DB-->>App: tulokset
        App->>UI: init_load_ui()
    end
    App->>App: ajoita seuraava silmukka
```
