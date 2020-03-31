'''
Liste med tall tall
Lag et program med en variabel tall som lager 
en liste som inneholder tall, tall ganger, 
og printer ut lista. 
For eksempel hvis tallet er 7, skrives det ut [7, 7, 7, 7, 7, 7, 7]. 
Test at programmet virker for ulike verdier av tall.
'''

tall = 12
liste = []
for i in range(tall):
    liste.append(tall)

# eller med list comprehension
liste = [tall for i in range(tall)]

print(liste)

'''
Ut med kjedisene

Lag en liste som inneholder navn på fire kjendiser. 
Fjern kjendisene ved å bruke de fire ulike måtene å fjerne fra liste 
som vi har lært:

del
.pop()
.pop() med indeks
.remove() med navn
'''
kjendiser = ['Hugh Grant', 'Tom Hanks', 'Natalie Portman', 'Bernie Sanders']

del kjendiser[1]
print(kjendiser)

kjendiser.pop()
print(kjendiser)

kjendiser.pop(0)
print(kjendiser)

kjendiser.remove('Natalie Portman')
print(kjendiser)

'''
Liste i liste i liste
Lag et program som har en variabel tall, 
og som lager en liste som inneholder tall tomme lister inni hverandre. 
Om tall er 2, lages lista [[]], om tall er 5, lista [[[[[]]]]]
'''

tall = 42
liste = []
for i in range(tall - 1):
    liste = [ liste ]
    # første iterasjon: liste = [ liste ] = [ [] ]
    # andre iterasjon: liste = [ liste ] = [ [[]] ]
    # osv...

print(liste)

