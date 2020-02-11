# Kode-eksempler og oppgaver vi gikk gjennom i timen

# Oppgave 2.1 og 2.2
beskjed = "Hei, og velkommen til Python-kurs, dag 2"
print(beskjed)
beskjed = "Hei, og velkommen til Python-kurs, dag 3"
print(beskjed)

# Hvordan ser teksten om ut vil har satt inn tab \t og linjeskift \n ?
fornavn = "Bjarne\tTab"
etternavn = "\nAleksandersen"
fullt_navn = f"{fornavn} {etternavn}"
print(fullt_navn)
print(f"Trønderrockens gudfar er \n\t{fullt_navn}")


# Metoder for å trimme whitespace (mellomrom, linjeskift, tab etc) fra strenger
# strip() fjerner i begge ender av strengen
# lstrip() fjerner fra starten av strengen (l står for left)
# rstrip() fjerner fra slutten av strengen (r står for right)
tekst = "     Her er det unødvendige mellomrom       "
print(f"'{tekst.strip()}'")
print(f"'{tekst.lstrip()}'")
print(f"'{tekst.rstrip()}'")   
print(tekst.replace(' er ', ' var '))

# Problem med tekst som skal inneholde ' eller " i selve teksten
# feil_i_streng = 'Jens' nye sykkel lager problemer for Python'
# man kan enten bruke motsatte fnutter for å markere strengen som det man vil at skal printes 
riktig_streng = "Jens' nye sykkel lager ikke lengre problemer for Python"
# eller escape fnutt med \
riktig_streng_2 = 'Jens\' nye sykkel lager ikke lengre problemer for Python'


# Oppgave 2.3
fornavn = "Bjørn"
etternavn = "Bamse"
fullt_navn = f"{fornavn} {etternavn}"
print(f"Hei, {fullt_navn}")

# Oppgave 2.4
nytt_navn = "teRJe TYSlanD"
print(nytt_navn.title())
print(nytt_navn.lower())
print(nytt_navn.upper())

# oppgave 2.5/2.6
quote = "A person who never made a mistake never tried anything new"
famous_person = "Albert Einstein"
print(f'{famous_person} sa: "{quote}"')


# Oppgave 2.7
name = " \t\n \n \t Max Mekker \n \t \n\t  "
print(f"'{name.lstrip()}'")
print(f"'{name.rstrip()}'")
print(f"'{name.strip()}'")

# Metodene vi kan bruke på stenger har ikke noe med print å gjøre
# kan lagre resultatet i ny variablen og printe ut denne
pretty_name = name.strip()
print(pretty_name)

# Tall
# Hva med kvadratrot?
# Kan opphøye i en halv
print(4 ** 0.5)

# eller bruke sqrt funksjonen fra mattebiblioteket
from math import sqrt, pi, sin
print(sqrt(4))
# i mattebiblioteket har man jo også mange andre morsomme ting, som pi og sinus
print(pi)
print(sin(pi/2))

# Oppgave 2.8
print(2 * 4)
print(32 / 4)
print( 5 + 3)
print(11- 3)
# Hvordan kan vi få flyttallet i 32/4 til å bli heltall?
# Bruke funksjonen int
print(int(32/4))

# Oppgave 2.9
favoritt_tall = 23
print(f"Mitt favoritt tall er {favoritt_tall}")


tall1 = "12"
tall2 = "3"
# strengene settes sammen til 123
print(tall1 + tall2)

# hvis man prøver å legge sammen et heltall og en streng får man en feil
# print(int(tall1) + tall2)

# hvis man prøver å bruke int-funksjonen på en streng som inneholder et flyttall får man også feil
# print(int("3.2"))

# Oppgave 3 fra ukesark - areal av trekant
lengde = 5
høyde = 4
areal = lengde * høyde / 2
print(areal)