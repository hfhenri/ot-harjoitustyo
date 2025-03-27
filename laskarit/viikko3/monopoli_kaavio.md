classDiagram
    class NormaaliKatu {
        nimi
    }
    class Pelaaja {
        rahamaara
    }
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Monopolipeli --> Aloitusruutu
    Monopolipeli --> Vankila
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- SattumaRuutu
    Ruutu <|-- YhteismaaRuutu
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- NormaaliKatu
    NormaaliKatu "1" -- "0..4" Talo
    NormaaliKatu "1" -- "1" Hotelli
    SattumaRuutu "1" -- "*" Kortti
    YhteismaaRuutu "1" -- "*" Kortti
    Pelaaja "1" -- "1" NormaaliKatu
    Ruutu "1" -- "1" Toiminto
    Kortti "1" -- "1" Toiminto