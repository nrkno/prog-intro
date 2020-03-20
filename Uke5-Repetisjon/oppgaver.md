# Repetisjonsoppgaver
Disse oppgavene bruker bare ting vi allerede har gått gjennom i kurset. Men oppgavene er litt annerledes enn de fra boka, så kanskje du må jobbe litt før du finner løsningen.

## Yatzy
Lag et program med to variable, `start` og `slutt`, som finner summen av tallene fra og med `start` til og med `slutt`.
Sjekk at programmet beregner liten straight i Yatzy (summen av 1, 2, 3, 4 og 5) til å være 15, og stor straight (summen av 2, 3, 4, 5 og 6) til å være 20.

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

Det er kanskje litt rart at to ting på samme plass i hver sine lister hører sammen. Lag en ny liste som består av tupler med mat og tall som hører sammen, som `('eple', 5)`. Loop gjennom lista og skriv ut samme setninger som over.

## Ut med kjedisene
Lånt fra [http://introtopython.org/](http://introtopython.org/lists_tuples.html#Exercises-lists)

Lag en liste som inneholder navn på fire kjendiser.
Fjern kjendisene ved å bruke de fire ulike måtene å fjerne fra liste som vi har lært:
* `del` 
* `.pop()`
* `.pop()` med indeks
* `.remove()` med navn

## Summen av diagonalen i en kvadratisk matrise
En kvadratisk matrise er noe som ser ut som
```
1 3 5
1 4 6
7 6 9
```
med like mange rader som kolonner. I kode kan vi representere en matrise som en liste av lister, der hvert element i lista er en rad i matrisen. F.eks blir matrisen over som `[[1,3,5],[1,4,6],[7,6,9]]`
For kvadratiske matriser kan man finne summen av diagonalen (kalles trase på norsk). I eksempelet over er det summen av første tall i første rad (= 1), andre tall i andre rad ( = 4) og tredje tall i tredje rad ( = 9), som gir sum 1 + 4 + 9 = 14.

Lag et program som regner ut summen av diagonalen. Prøv å lage programmet slik at det virker uavhengig av hvor stor matrisen er, så både for `[[2,0],[0,2]]` og `[[1,2,3],[4,5,6],[7,8,9]]`.

## Liste i liste i liste

Lag et program som har en variabel `tall`, og som lager en liste som inneholder `tall` tomme lister inni hverandre. 
Om `tall`er 2, lages lista `[[]]`, om `tall` er 5, lista `[[[[[]]]]]`

# Videre opppgaver
Disse oppgavene inneholder ting vi ikke helt har lært enda, men de er kanskje ikke så vanskelig allikevel.

## Strenger ligner på lister
Strenger ligner faktisk på lister, en streng er en slags liste av tegn. Det betyr at ting vi gjør med lister kan vi gjøre med strenger.
Lag et program som tar utgangspunkt i en streng, feks `tekst = 'blomsten er gul'`.

* Se at funksjonen for å finne lengden til en liste også virker for strengen
* Lag en for-løkke som looper gjennom strengen og printer ut alle tegnene på hver sin linje
* Bruke slice på samme måte som for lister til å hente ut ordet `gul` fra strengen, og bokstaven `r`
* Lag en ny streng som er som `tekst`, bare at setningen har stor forbokstav og punktum til slutt



