
programmer = [
    'Dagsrevyen',
    'Fantorangen',
    'Nytt på nytt',
    'Fra bølle til bestevenn'
]

# for-løkke, viktig å passe på indentering
for program in programmer:
    print(f'Dette er et program i NRK: {program}')

    print('Tilhører løkka')
print('Tilhører ikke løkka')

# Oppgave 4.1
pizzaer = ['Grandiosa', 'Big One', 'Ristorante']

for pizza in pizzaer:
    print(pizza)

for pizza in pizzaer:
    print(f'Jeg liker {pizza}')

print('Jeg liker virkelig pizza!')


# Oppgave 4.2
kattedyr_liste = ['Puma', 'Tiger', 'Løve']

for kattedyr in kattedyr_liste:
    print(f'En {kattedyr} er ikke et bra kjæledyr!')

print('Ingen av disse dyrene er bra kjæledyr!')


# Range kan også telle nedover ved at tredje argument er negativt
for i in range(10, -10, -3):
    print(i)


# min, max og sum er nyttige funksjoner for lister med tall
tall = list(range(13, 48))
print(min(tall))
print(max(tall))
print(sum(tall))

# list comprehensions - en måte å slå sammen for-løkke med utregning og legge i liste på en linje
kvadrater = [ i**2 for i in range(1, 10)]
print(kvadrater)

# oppgave 4.4
# for i in range(1, 1000000):
# print(i)

# oppgave 4.5
print(sum(range(1, 10000001)))    

# oppgave 4.8 kan bruke list() istedet for [] (begge ting er en liste)
kubikker = list(i**3 for i in range(1, 11))
print(kubikker)

# slicing
kanaler = ['NRK1', 'NRK2', 'NRK3', 'NRKSUPER']
print(kanaler[0:2])
print(kanaler[1:])
print(kanaler[2:1])
print(kanaler[-3: -2])

for kanal in kanaler[:2]:
    print(kanal)

# viktig forskjell på å kopiere en liste og å sette to variable til å peke på det samme
# kanaler_ekstra = kanaler vs kanaler_ekstra = kanaler[:]
kanaler = ['NRK1', 'NRK2', 'NRK3', 'NRKSUPER', 'NRK4', 'NRK5', 'NRK6', 'NRK7', 'NRK8']
kanaler_ekstra = kanaler[:]

kanaler.append('NRK4')
kanaler_ekstra.append('NRKW')

# vi oppdaget også et eget slice-object man kan bruke i stedet for [:] 
# og at vi kan steppe på slicing også med en tredje parameter med kolon i mellom
slice_objekt = slice(2)
print(kanaler[slice(0, 3, 2)]) # kanaler[0:3:2]

# finne de tre midterste elementene i en liste (med odde antall elementer totalt)
print(kanaler[int(len(kanaler)/2)-2:int(len(kanaler)/2)+1])

print(kanaler)
print(kanaler_ekstra)

kanaler = ('NRK1', 'NRK2', 'NRK3', 'NRKSUPER')
print(kanaler[2])

kanaler = kanaler[0:2]

print(kanaler)

# oppgave 2 i ekstraoppgavene
tall_0 = 0
tall_1 = 1
tall_2 = 2
tall_3 = 3
tall_4 = 4

# vi lurte på om det var mulig å få tak i en variabel basert på navnet på den
# feks hente ut verdien av tall_0 utfra 'tall_0'
# det er mulig med funksjonen globals() som gir en dictonary av alle globale variable
# da kan vi hente ut en variabel med variabelnavnet som streng
print(globals()['tall_0'])

# dictionaries kommer vi til seinere i kurset men det er konseptet med en struktur av par med key-value
pizzaer = { 'pizza_1': 'grandiosa' }
# henter ut verdi med nøkkelnavn, istedet for indeks som for lister
print(pizzaer['pizza_1'])
# men nøkkel kan være tall, og da ser man ikke forskjell på måten man henter ut ting
pizzaer = { 0: 'grandiosa'}
pizza_liste = ['grandiosa']
print(pizzaer[0])
print(pizza_liste[0])


tall = []
for i in range(0, 5):
    tall.append(globals()[f'tall_{i}'])

print(tall)
print(globals())