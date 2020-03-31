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
Par av lister

Gitt at du har to lister, en med mat, og en med antall, skriv et program som henter ut verdi fra samme indeks i de to listene og skriver ut en setning om antall mat, feks Jeg har 5 epler.

Hvis mat = ["eple", "banantwist", "frossenpizza" ], antall = [5, 17, 3] skal programmet skrive ut Jeg har 5 epler, Jeg har 17 banantwist, Jeg har 3 frossenpizza

Det er kanskje litt rart at to ting på samme plass i hver sine lister hører sammen. Lag en ny liste som består av tupler med mat og tall som hører sammen, som ('eple', 5). Loop gjennom lista og skriv ut samme setninger som over.
'''

mat = ["eple", "pære", "banan", "lime"]
antall = [1, 10, 4, 97]

for i in range(len(antall)):
    ending = "er"
    if ( (mat[i])[-1] == "e"):
        ending = "r"
    if (antall[i] == 1):
        ending = ""
    print (f"Vi har {antall[i]} {mat[i]}{ending}")

tuple_eksempel = ("eple", 1)


mat_med_antall = []
for i in range(len(antall)):
    mat_med_antall.append((mat[i], antall[i]))

print (mat_med_antall)

for i in range(len(mat_med_antall)):
    mat = mat_med_antall[i][0]
    antall = mat_med_antall[i][1]
    print(f"Vi har {antall} {mat}")

for mat_antall in mat_med_antall:
    print(f"Vi har {mat_antall[1]} {mat_antall[0]}")


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
Summen av diagonalen i en kvadratisk matrise
En kvadratisk matrise er noe som ser ut som

1 3 5
1 4 6
7 6 9

med like mange rader som kolonner. I kode kan vi representere en matrise som en liste av lister, der hvert element i lista er en rad i matrisen. F.eks blir matrisen over som [[1,3,5],[1,4,6],[7,6,9]] For kvadratiske matriser kan man finne summen av diagonalen (kalles trase på norsk). I eksempelet over er det summen av første tall i første rad (= 1), andre tall i andre rad ( = 4) og tredje tall i tredje rad ( = 9), som gir sum 1 + 4 + 9 = 14.

Lag et program som regner ut summen av diagonalen. Prøv å lage programmet slik at det virker uavhengig av hvor stor matrisen er, så både for [[2,0],[0,2]] og [[1,2,3],[4,5,6],[7,8,9]].
'''

matrise = [[1,2,3,5,5],[4,5,6,5,5],[7,8,9,3,98],[16,62,63,65,65],[1234,2234,3234,5,532424]]
liten_matrise = [[2,0],[0,2]]
print (matrise[1][2])

summen = 0
for i in range(0, len(matrise)):
    summen = summen + matrise[i][i]

print(summen)

summen = 0
for i in range(0, len(liten_matrise)):
    summen = summen + liten_matrise[i][i]
    
print(summen)

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

'''
Strenger ligner på lister
Strenger ligner faktisk på lister, en streng er en slags liste av tegn. Det betyr at ting vi gjør med lister kan vi gjøre med strenger. Lag et program som tar utgangspunkt i en streng, feks tekst = 'blomsten er gul'.

Se at funksjonen for å finne lengden til en liste også virker for strengen
Lag en for-løkke som looper gjennom strengen og printer ut alle tegnene på hver sin linje
Bruke slice på samme måte som for lister til å hente ut ordet gul fra strengen, og bokstaven r
Lag en ny streng som er som tekst, bare at setningen har stor forbokstav og punktum til slutt
'''
tekst = 'blomsten er gul'
tekst_som_liste = ["b", "l", "o"]

print(len(tekst))

for tegn in tekst:
    print(tegn)

print(tekst[4:7])
print(tekst[:3])

print(tekst[3:])

print(tekst[12:])
print(tekst[-3:])

tekst_med_tegnsetting = tekst[0].upper() + tekst[1:] + "."
print(tekst_med_tegnsetting)

#Ikke gjør dette hjemme:
tekst_med_tegnsetting = chr(ord(tekst[0])-32) + tekst[1:] + "."
print(tekst_med_tegnsetting)