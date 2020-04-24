# Repetisjonsoppgaver

## Fjerne duplikater

Lag et program som løper gjennom en liste og lager en ny liste som er som den opprinnelige lista bortsett fra at hver verdi bare finnes én gang i den nye lista. Skriv ut den nye lista. 

For eksempel skal programmet med lista `[1, 4, 7, 5, 8, 3, 4, 5, 2, 1, 3]` skrive ut `[1, 4, 7, 5, 8, 3, 2]`

## FizzBuzz

Basert på en barnelek og en populær programmeringsoppgave ([Wikipedia](https://en.wikipedia.org/wiki/Fizz_buzz))

Gå gjennom tall fra 1 til 100 og skriv ut etter følgende regler:
* Hvis tallet er delelig med 3 skal ordet `Fizz` skrives ut
* Hvis tallet er delelig med 5 skal ordet `Buzz`skrives ut
* Hvis tallet er delelig med både 3 og 5 skal ordet `FizzBuzz` skrives ut
* Hvis tallet hverken er delelig med 3 eller 5 skal tallet skrives skrives ut.
 
 De første tjue tallene skal bli til `1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz`
 
 Du vil gjerne vite hvor mange FizzBuzzer det er som skrives ut. Endre programmet ditt slik at det også teller hver gang det er FizzBuzz. Skriv ut dette antallet til slutt i programmet.

## Nytt på nytt

Lag et program som inneholder følgende dictionary med informasjon om fredagens "Nytt på nytt":

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
