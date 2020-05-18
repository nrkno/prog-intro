I Noen av oppgavene under trenger du å få tak i tilfeldig tall i et gitt intervall. Det kan gjøres ved å importere Pythons random-bibliotek ved å inkludere følgende linje
```
import random
```
Da får man tilgang til mange slags funksjoner, de to vi kan få brukt for er `randint` og `randrange` som gir tilfeldig tall mellom start og slutt-verdier, forskjellen på de er at `randint`tar med slutt-tallet i trekning, mens `randrange`er som andre range-funksjoner vi har sett på som ikke tar med slutt-verdien
```
random.randrange(1, 3)  # Mulige resultater: 1,2
random.randint(1, 3)    # Mulige resultater:  1,2,3
```



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
Brukeren får et propt med beskjed om å gjette et tall, eller q for å avslutte.
Etter hver gjetting får brukeren tilbakemelding på om tallet var for høyt, for lavt eller riktig.
Om tallet er for høyt eller for lavt må brukeren få gjette videre, og tallet er riktig avsluttes programmet.


