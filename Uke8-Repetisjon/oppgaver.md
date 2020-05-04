# Repetisjonsoppgaver

## Fjerne duplikater

Lag et program som løper gjennom en liste og lager en ny liste som er som den opprinnelige lista, bortsett fra at hver verdi bare finnes én gang i den nye. Skriv ut den nye lista. 

For eksempel skal programmet med lista `[1, 4, 7, 5, 8, 3, 4, 5, 2, 1, 3]` skrive ut `[1, 4, 7, 5, 8, 3, 2]`

## Minimum, maksimum og sum
Anta at du har en liste med følgende verdier:

`liste = [-34, 2, -24, 4, 23, -45, 5, 7, 35, 3]`
1. Bruk en for-løkke og en if-setning for å finne den minste verdien og skriv
den ut. Du skal ikke bruke Python sin innebygde min-funksjon.
2. Bruk en for-løkke og en if-setning for å finne den største verdien og skriv
den ut. Du skal ikke bruke Python sin innebygde max-funksjon.
3. Bruk en for-løkke for å finne summen av alle tallene i listen og print ut.
4. (Bonus) Finn gjennomsnittet av tallene.

## Opphøyd i annen
Velg et tall (for eksempel 10) og lag en dictionary hvor tallene 1 til tallet du har valgt (for eksempel 1 til 10) er nøkkel, og tallet opphøyd i annen er value. Eksempel på dictionary:

`{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}`

## FizzBuzz

Basert på en barnelek og en populær programmeringsoppgave ([Wikipedia](https://en.wikipedia.org/wiki/Fizz_buzz))

Gå gjennom tall fra 1 til 100 og skriv ut etter følgende regler:
* Hvis tallet er delelig med 3 skal ordet `Fizz` skrives ut.
* Hvis tallet er delelig med 5 skal ordet `Buzz` skrives ut.
* Hvis tallet er delelig med både 3 og 5 skal ordet `FizzBuzz` skrives ut.
* Hvis tallet hverken er delelig med 3 eller 5 skal tallet skrives ut.
 
 De første tjue tallene skal bli til `1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz`
 
 Du vil gjerne vite hvor mange FizzBuzzer det er som skrives ut. Endre programmet ditt slik at det også teller hver gang det er FizzBuzz. Skriv ut dette antallet til slutt i programmet.

## Nytt på nytt

Start med å kopiere følgende dictionary med informasjon om fredagens "Nytt på nytt" inn i programmet ditt:

```
program = {
  "programInformation": {
    "titles": {
      "title": "I dag",
      "subtitle": "Gjester denne uken er Are Kalvø og Ingebjørg Bratland."
    },
    "details": {
      "displayValue": "24.04.2020   ·   Aldersgrense 9 år   ·   31 min",
      "accessibilityValue": "24.04.2020. Aldersgrense 9 år. 31 minutter."
    }
  },
  "moreInformation": {
    "usageRights": {
      "from": {
        "date": "2020-04-24T20:00:00+02:00",
        "displayValue": "24. april 2020 kl. 20:00"
      },
      "to": {
        "date": "2021-12-31T00:00:00+01:00",
        "displayValue": "31. desember 2021 kl. 00:00"
      }
    },
    "productionYear": 2020,
    "duration": {
      "seconds": 1902,
      "iso8601": "PT31M42S",
      "displayValue": "31 min"
    }
  },
  "contributors": [
    {
      "role": "Gjest",
      "name": [
        "Ingebjørg Bratland",
        "Are Kalvø"
      ]
    },
    {
      "role": "Programleder",
      "name": [
        "Bård Tufte Johansen",
        "Johan Golden",
        "Pernille Sørensen"
      ]
    }
  ]
}
```

### Rettigheter

Hent ut rettighetene for programmet, det vil si når det er tilgjengelig fra og når det er tilgjengelig til. De fins i "moreInformation" "usageRights", "from" og "to". Skriv ut en setning som sier når programmet er tilgjengelig:
```
Programmet har rettigheter fra 24. april 2020 kl. 20:00 til 31. desember 2021 kl. 00:00
```

### Deltakere
Hent ut deltakerne i programmet fra "contributors", dette er en liste som inneholder to elementer på formen
```
 {
   "role": <rolle>,
   "name": <liste med navn>
}
```
Skriv ut en linje for hver deltaker i programmet på formen `<navn> er <rolle> i programmet`

## Forekomst av strenger

Lag et program som har en tekststreng som kan være 

`
Norsk rikskringkasting AS, i dagligtale og markedsføring mest kjent som NRK, er et norsk statseid kringkastingsselskap som tilbyr medieinnhold på radio, TV, strømmetjeneste og internett. NRK bygger på prinsippene til en offentlig allmennkringkaster etter samme modell som BBC, og er medlem av Den europeiske kringkastingsunion.
`

1. Finn ut av hvor mange ganger i teksten det er en stor "N". Du skal ikke bruke Python sin innebygde count()-funksjon.
2. Gjør slik at sjekken ikke bryr seg om store og små bokstaver, og sjekk hvor mange ganger både stor og liten n forekommer i teksten.
3. Sjekk så hvor mange ganger "NRK" forekommer i teksten.


