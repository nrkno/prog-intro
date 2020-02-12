# kode vi gikk igjennom i timen

fornavn = "Heidi"
print(fornavn)
# skrivefeil i variabelnavn gir feil når man kjører programmet
# print(foravn)

# Må ha samme start og slutt-fnutt, enten dobbeltfnutter eller enkeltfnutter
# fnutter som da er inni (mellom start- og slutt-fnutt) må være av motsatt futt-type
fornavn = "Heidi'"
print(fornavn) # skriver ut Heidi'


# Oppgave 2.1/2.2
melding = "Dette er en melding"
print (melding)

melding = "Dette er den nye meldingen"
print (melding)

navn = "Kristoffer"
språk = "Python"

# Oppgave 2.3
tekst = f"Hei, {navn}, har du lyst til å lære {språk} i dag?"
print(tekst)

# Oppgave 2.4
print(navn.lower())
print(navn.upper())
print(navn.title())

# Oppgave 2.5/2.6
sitat_opphav = "Albert Einstein"
print(f'{sitat_opphav} sa en gang: "Det viktigste med et sitat er ikke at det er et reelt sitat, men at opphavet er {sitat_opphav}"')

# Oppgave 2.7
navn_med_mellomrom = "\t \t \n   Kristoffer \t Dyrkorn    \t\t"

print(f"'{navn_med_mellomrom.strip()}'")
print(f"'{navn_med_mellomrom.lstrip()}'")
print(f"'{navn_med_mellomrom.rstrip()}'")

# Oppgave 2.9
min_pin_kode = 3.1415926
print(f"pin-koden min er: {min_pin_kode}")

# Variant av oppgave 3 fra ekstraoppgavene
tall1 = "12" # er en streng
tall2 = 3 # er et tall
tall3 = tall1 + tall2 # får feil om man prøver å legge sammen tall og streng
print(f"tall1: {tall1} tall2: {tall2} tall3: {tall3}")