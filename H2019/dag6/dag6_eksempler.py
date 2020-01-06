# Repetisjon av if
# eksperimenter med ulike tall < 5, tall < 7
# se at det er forskjell på om det står elif eller bare if på linje 8, eller hva skjer om linje 8 har samme test som linje 6, tall < 5
tall = 7

if tall < 5:
    print("tallet er mindre enn 5")
elif tall < 7:
    print("tallet er større enn 4 og mindre enn 7")
else:
    print("tallet er større enn seks")


# dagens tema: dictionaries
# ny type datastruktur som består av par av nøkkel og tilhørende verdi
# strenger i python er enten i enkeltfnutter eller i dobbeltfnutter, det er det samme hva man bruker
# ser ut som det er mer vanlig å bruke enkeltfnutter
embla = {
    'navn': 'Embla', 
    'bygning': 'Glassgården', 
    'etasje': 1,
    'plasser': 28,
    }

print(embla)

# legge til ny nøkkel og verdi
embla['fløy'] = 'vest'
print(embla)

# oppdatere eksisterende nøkkel med ny verdi
embla['fløy'] = 'nord'
print(embla)

# Spørsmål: Er den case-sensitiv eller kan man få tak i fløy ved å skrive embla['Fløy']?
# Den er case-sensitiv, 'fløy' og 'Fløy' er to forskjellige strenger


# Spørsmål: Kan man få tak i flere verdier på en gang ved å gjøre embla['fløy', 'plasser']?
# for å printe ut flere verdier på en gang må man hente en og en verdi
print(embla['fløy'], embla['plasser'])

# Slette nøkkel og tilhørende verdi
del embla['fløy']
print(embla)
# Spørsmål: Kan man skrive ut ordet 'delete' i stedet for 'del'?
# Nei, det kan man ikke

# Linja under vil feile om embla ikke har nøkkelen fløy:
# print(embla['fløy'])
# en trygg måte å hente ut verdi på er å bruke get
print(embla.get('fløy'))
# kan ta inn verdi den skal bruke i stedet om ikke nøkkelen finnes
print(embla.get('fløy', 'har ikke fløy'))

# Spørsmål: Finnes det try i python?
# Ja det gjør det https://www.w3schools.com/python/python_try_except.asp
# Helt utenfor pensum, men kan bruke try-except i stedet for .get feks på følgende måte
try:
    print(embla['fløy'])
except:
    print('har ikke fløy')


# Man kan starte med tom dictionary og legge til nøkler og verdier etterhvert
postnummer = {}
postnummer['1940'] = 'Bjørkelangen'
print(postnummer)


# Spørsmål: Hvilke metoder har dictionaries?
# Svar: https://www.w3schools.com/python/python_ref_dictionary.asp, vi skal bruke items(), keys(), values() og get()

# Spørsmål: Kan man legge inn nye nøkkel-verdi par ved å bruke krøllparenteser?
# Følgende gir oss bare en ny embla, uten de nøkkel-verdi-parene den hadde fra før
# embla = {'fløy': 'vest'}
# men vi kan bruke funksjonen update (igjen beyond pensum)
embla.update({'fløy': 'vest'})
print(embla)


# Oppgave 6.1
heidi = {
    'first_name': 'Heidi',
    'last_name': 'Mork',
    'age': 27, # Litt løgn... :-)
    'city': 'Oslo'
}

print(f"Fornavn: {heidi['first_name']}")
print(f"Etternavn: {heidi['last_name']}")
print(f"Alder: {heidi['age']}")
print(f"By: {heidi['city']}")

# Vi oppdaget at det er viktig å skille mellom hva slags fnutter man bruker inni i f-strengen. 
# Følgende linje (der man også har dobbeltfnutter når man angir nøkkelen) feiler 
# fordi den ser ut til å tolke det som at f-strengen er avsluttet etter dobbelfnutten før city
# print(f"By: {heidi["city"]}")

# Spørsmål: Kan man bruke en printfunksjon, men allikevel få verdiene på hver sin linje?
# Ja, enten ved å bare putte inn '\n' mellom tekst i samme f-streng, eller bruke at print har et sep man kan angi
# Alternativ 1
print(f"Fornavn: {heidi['first_name']} \nEtternavn: {heidi['last_name']}\nAlder: {heidi['age']}\nBy: {heidi['city']}")
# Alternativ 2
print(f"Fornavn: {heidi['first_name']}", f"Etternavn: {heidi['last_name']}", f"Alder: {heidi['age']}", f"By: {heidi['city']}", sep='\n')

# Oppgave 6.2
favoritt_tall = {
    'heidi': 23,
    'truls': 42,
    'olga': 3,
    'guri': 14,
    'nils': 17
}

print(f"Heidi har favoritt-tall {favoritt_tall['heidi']}")
print(f"Truls har favoritt-tall {favoritt_tall['truls']}")


# Loope verdier i dictionaries
# henter ut nøkkel og verdi som et tuppel, og kan printe ut folk og favoritt-tall på bare to linjer
for key, value in favoritt_tall.items():
    print(f"{key.title()} har favoritt-tall {value}")

# henter ut bare nøklene (navnene), looper over de og skriver de ut
for key in favoritt_tall.keys():
    print(f"Navn: {key.title()}")

# henter ut bare tallene
for value in favoritt_tall.values():
    print(f"Tall: {value}")

# Kan sortere nøklene og printe ut navn så de kommer i sortert rekkefølge
for key in sorted(favoritt_tall.keys()):
    print(f"Navn: {key.title()}")

# Kan også sortere verdiene
for value in sorted(favoritt_tall.values()):
    print(f"Tall: {value}")

# Kan loope over verdiene til embla men vi kan ikke sortere de fordi verdiene er en blanding av tall og strenger
for value in embla.values():
    print(value)


# Oppgave 6.5
elver = {
    'nilen': 'egypt',
    'glomma': 'norge',
    'elbe': 'tyskland',
    'volga': 'russland',
    'kwai': 'burma'
}

for elv, land in elver.items():
    print(f"Elven {elv.title()} renner gjennom {land.title()}")

for elv in elver.keys():
    print(f"{elv.title()} er en elv")

for land in elver.values():
    print(f"{land.title()} er et land")

for land in sorted(elver.values()):
    print(f"{land.title()} er et land")

# Sortering av tupler vil gi sortering av nøklene
for elv, land in sorted(elver.items()):
    print(f"Elven {elv.title()} renner gjennom {land.title()}")

# Nesting
# Liste av dictionaries
linux = {
    'navn': 'Linux',
    'bygning': 'N-fløya',
    'plasser': 10,
    'etasje': 5
}

møterom = [embla, linux]
print(møterom)

# Spørsmål: Kan vi blande ulike dictionaries i samme liste?
# Jada, ikke noe problem, møterom og elver hører jo naturlig sammen
møterom_og_elver = [embla, linux, elver]
print(møterom_og_elver)

# Spørsmål: Hvordan kan vi "legge sammen" to dictionaries?
# Vi kan feks lage en tom dictionary, loope over både embla og elvene og legge til alle key-value-par i den nye dictionaryen
embla_og_elver = {}

for k, v in embla.items():
    embla_og_elver[k] = v

for k, v in elver.items():
    embla_og_elver[k] = v

print(embla_og_elver)

# Vi kan også ha dictionary i dictionary (adresse) og liste i dictionary (barn)
person = {
    'navn': 'heidi',
    'adresse': {
        'gate': 'Radarveien',
        'husnummer': '68'
    },
    'barn': [ {'navn': 'lars'}, {'navn': 'frida'}]
}

print(person)


# Oppgave 6.8
marte = {'navn': 'marte', 'type': 'marsvin'}
lisa = {'navn': 'lisa', 'type': 'marsvin'}

dyr = [marte, lisa]

for d in dyr:
    print(f"{d['navn'].title()} er et {d['type']}")