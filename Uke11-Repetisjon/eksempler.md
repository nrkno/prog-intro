# Repetisjon - eksempler på bruk av funksjoner

## En mer

Lag en funksjon `en_mer` som tar inn et tall `n` og returnerer et tall som er én mer enn `n`.

Noen eksempler: 

en_mer(0) => 1
en_mer(1) => 2
en_mer(2) => 3
en_mer(-1) => 0

Hvordan kan du bruke funksjonen `en_mer` til å lage et tall som er 3 større? 5 større?

## Dobbel

Lag en funksjon `dobbel` som tar inn et tall `n` og returnerer et tall som er det dobbelte av `n`.

Noen eksempler:

dobbel(0) => 0
dobbel(1) => 2
dobbel(2) => 4
dobbel(3) => 3

Kan du implementere `dobbel_med_en_mer` som gir samme svar som `dobbel`, men bruker funksjonen `en_mer` istedenfor addition eller multiplikasjon?

## Bare positive

Lag en funksjon `bare_positive` som tar inn en liste med tall og returnerer en liste med de tallene som var positive (større enn 0).

Noen eksempler: 

bare_positive([1, 0, -34, 278, 7]) => []
bare_positive([1, 2, 3]) => [1, 2, 3]
bare_positive([-1, -2, -3]) => []
bare_positive([0, 1, -2, 3]) => [1, 3]

## Velg programmer

Lag en funksjon `velg_programmer_for_kanal` som tar inn en liste med programmer og en kanal. Listen med programmer skal inneholde dictionaries med nøklene "tittel" og "kanal". Funksjonen skal returnere en liste med programtitler for den gitte kanalen.

For eksempel, gitt koden under:

```
programliste = [
    {
        "tittel": "Dagsrevyen 21",
        "kanal": "NRK1"
    },
    {
        "tittel": "Mesternes mester",
        "kanal": "NRK2"
    },
    {
        "tittel": "Oggy og kakerlakkene",
        "kanal": "NRKSUPER"
    },
    {
        "tittel": "Nesten voksen",
        "kanal": "NRK3"
    },
    {
        "tittel": "Pandaene kjem",
        "kanal": "NRK2"
    },
    {
        "tittel": "Blodsbånd",
        "kanal": "NRK1"
    }
]

nrk2_titler = velg_programmer_for_kanal(programliste, "NRK2")
```

Etter kjøring skal `nrk2_titler` inneholde listen `[ "Mesternes mester", "Pandaene kjem" ]`.
