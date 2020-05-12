# Oppgaver uke 10


## Oppgave 1
Skriv en funksjon som tar i mot to tall. Funksjonen skal returnere det største av de to tallene.

## Oppgave 2
Hva printes ut?

```
def mystisk_funksjon(a):
  print(a)
  
  
a = "hei"
b = "hallo"
mystisk_funksjon(b)
```

## Oppgave 3
* Lag en funksjon som tar en liste med tall og et tall som argument. Funksjonen skal gå igjennom lista og returnere alle elementene som er mindre enn tallet som ble sendt med. For eksempel om man hadde sendt med lista `[3, 9, 2, 23]` og tallet 5, hadde lista som hadde blitt returnert vært `[3, 2]`. Funksjonskallet kan se slik ut: 
```faa_alle_tall_under_verdi(liste_med_tall, max_verdi)```.
* Noen ganger er det viktig at lister ikke blir modifisert. Endre funksjonen til å heller lage en kopi av lista, og sjekk at den orginale lista ikke er modifisert.

## Oppgave 4
Anta at vi har følgende funksjon;

```
def vis_hilsen(navn, alder, lokasjon):
    print(f"Velkommen {navn}! Du er {str(alder)} år gammel og bor i {lokasjon}")
```

* Hvilket funksjonskall er riktig?
```
vis_hilsen("Preben", 33, "Oslo")
vis_hilsen("Oslo", 33, "Preben")
```
* Hvordan kunne `vis_hilsen` vært kalt med keyword arguments? Har rekkefølge noe å si når man benytter seg av keywords arguments?


