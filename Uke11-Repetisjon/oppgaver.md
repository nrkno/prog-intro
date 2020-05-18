I noen av oppgavene under trenger du å få tak i tilfeldig tall i et gitt intervall. Det kan gjøres ved å importere Pythons random-bibliotek ved å inkludere følgende linje
```
import random
```
Da får man tilgang til mange slags funksjoner. De to vi kan få bruk for er `randint` og `randrange` som gir tilfeldig tall mellom start og slutt-verdier. Forskjellen på de to funksjonene er at `randint` tar med slutt-tallet i trekningen, mens `randrange` er som andre range-funksjoner vi har sett på som ikke tar med slutt-verdien.
```
random.randrange(1, 3)  # Mulige resultater: 1,2
random.randint(1, 3)    # Mulige resultater: 1,2,3
```

# Yatzy

## Et kast
Lag en funksjon som tar inn et tall `n` og returnerer liste av n tilfeldig trekte tall mellom 1 og 6. 
Hvis n er 5 representerer det et "nytt" kast i Yatzy, n kan være lavere enn 5 når man er inne i en runde og har spart noen terninger.

## Beregn kast for en verdi
Lag en funksjon, f.eks `beregn_kast` som tar inn et kast (liste med terningverdier), og en verdi (tall mellom 1 og 6). Funksjonen looper gjennom terningene i kastet og returnerer summen av terningverdiene som har verdi lik parameteren man sendte inn, og antall terninger som ikke har samme verdi. 
Denne funksjonen svarer til et kast i yatzy der man plukker ut feks alle toere, og returnerer summen av toere og antall terninger som er igjen (de man kaster på nytt i neste kast)
```
beregn_kast([2, 5, 5, 2, 4], 2) = (4, 3)
```

## En runde
Lag en funksjon som gjør alle tre kastene i en runde, og returnerer totalsummen.
Denne funksjonen tar inn en terningverdi, og må kalle `kast` og `beregn_kast` tre ganger, men antall terninger i `kast` er antall terninger igjen fra `beregn_kast`, og den totale summen er summen fra alle tre kastene. Print ut kastene underveis og totalsummen før den returneres.

## Bonus
Lag en funksjon som gjør alt i et yatzyspill fram til bonus-utregningen. Det betyr å kalle runde-funksjonen en gang for hver terningverdi fra 1 til 6. Om summen er 63 eller mer har man fått bonus. Skriv ut om man får bonus eller ikke.

# Passordgenerator

Lag et program som genererer tilfeldige passord etter følgende regler:
Passordet er
* 8 tegn langt
* inneholder 2 store bokstaver A-Z
* inneholder 2 små bokstaver a-z
* inneholder 2 siffer
* inneholder 2 spesialtegn blant !?.,%&
* bokstaver, tall og tegn er på tilfeldige plasser

Se om det kan være nyttig å bruke funksjoner for de ulike delene av programmet.

# Gjettelek
Lag et program som lar brukeren gjette på hvilket tall programmet har valgt, f.eks mellom 1 og 100.
Brukeren får et prompt med beskjed om å gjette et tall, eller `q` for å avslutte.
Etter hver gjetting får brukeren tilbakemelding på om tallet var for høyt, for lavt eller riktig.
Om tallet er for høyt eller for lavt må brukeren få gjette videre, hvis tallet er riktig avsluttes programmet.
