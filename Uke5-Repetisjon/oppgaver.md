# Repetisjonsoppgaver

## Sette sammen strenger fra en liste
Lag et program som looper gjennom en liste av strenger og setter de sammen til en lang streng. 
For eksempel skal lista `['Et', 'fint', 'hus']`gi `'Etfinthus'`.

Det hadde kanskje vært fint med mellomrom mellom ordene. Se om du kan endre programmet ditt til også å legge til mellomrom mellom ordene (men ikke til slutt), så resultatet blir `'Et fint hus'`.

## Summere en liste
Lag et program som summerer alle verdiene i en liste av tall **uten** å bruke `sum()`-funksjonen

## Reversere liste

Lag et program som reverserer en liste uten å bruke `list.reverse()`

## Liste med tall tall
 
Lag et program med en variabel `tall` som lager en liste som inneholder `tall`, `tall` ganger, og printer ut lista. 
For eksempel hvis tallet er 7, skrives det ut `[7, 7, 7, 7, 7, 7, 7]`. Test at programmer virker for ulike verdier av `tall`.

## Par av lister
 
Gitt at du har to lister, en med mat, og en med antall, skriv et program som henter ut verdi fra samme indeks i de to listene og skriver ut en setning om antall mat, feks `Jeg har 5 epler`. 

Hvis `mat = ["eple", "banantwist", "frossenpizza" ]`, `antall = [5, 17, 3]` skal programmet skrive ut `Jeg har 5 epler`, `Jeg har 17 banantwist`, `Jeg har 3 frossenpizza`

## Liste i liste i liste

Lag et program som har en variabel `tall`, og som lager en liste som inneholder `tall` tomme lister inni hverandre. 
Om `tall`er 2, lages lista `[[]]`, om `tall` er 5, lista `[[[[[]]]]]`

# Mer avanserte opppgaver
Disse oppgavene inneholder ting vi ikke helt har lært enda, men de er kanskje ikke så vanskelig allikevel.

## Strenger ligner på lister
Strenger ligner faktisk på lister, en streng er en slags liste av tegn. Det betyr at ting vi gjør med lister kan vi gjøre med strenger.
Lag et program som tar utgangspunkt i en streng, feks `tekst = 'blomsten er gul'`.

* Se at funksjonen for å finne lengden til en liste også virker for strengen
* Lag en for-løkke som looper gjennom strengen og printer ut alle tegnene på hver sin linje
* Bruke slice på samme måte som for lister til å hente ut ordet `gul` fra strengen, og bokstaven `r`
* Lag en ny streng som er som `tekst`, bare at setningen har stor forbokstav og punktum til slutt



