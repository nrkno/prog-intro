# Oppgave 1 Yatzy

# Alternativ 1
start = 1
slutt = 5

total = 0
for i in range(start, slutt + 1):
    total += i
print(total)

# Alternativ 2
start = 2
slutt = 6
print(sum(range(start, slutt + 1)))

# Oppgave 2 Sette sammen strenger fra en liste
tekst = ['Et', 'veldig', 'stort', 'og', 'fint', 'hus']

# Del 1
langtekst = ''
for term in tekst:
    langtekst += term # hurtigvariant for langtekst = langtekst + term
print(langtekst)

# Del 2 
langtekst = ''
for term in tekst:
    langtekst += term + ' '
langtekst = langtekst.strip()
print(langtekst)

# Oppgave 3 Summere en liste
liste = [1, 2, 3, 4, 5, 6]
total = 0
for i in liste:
    total += i
print(total)

# Oppgave 4 reversere en liste
liste = [1, 2, 3, 4, 5, 6]

# Alternativ 1 
# Bruke slice med hopp på -1 (da går man baklengs gjennom lista)
ny_liste = []
for i in liste[::-1]: # liste[::-1] er samme som liste[0:len(liste):-1] 
    ny_liste.append(i)
print(ny_liste)

# Alternativ 2
# En annen måte å gå gjennom lista baklengs på
ny_liste = []
for i in range(len(liste)):
    ny_liste.append(liste[(len(liste)-i)-1])
print(ny_liste)

# Alternativ 3
# Bruker insert med indeks, og setter alltid inn elementer først i lista
ny_liste = []
for i in liste:
    ny_liste.insert(0, i)
print(ny_liste)

# Alternativ 4
# Snur rekkefølgen i samme liste, men må midlertidig mellomlagre innhold i en ekstra variabel
# merk at for-løkka bare går gjennom halve lista
# innholdet i liste[0] byttes med liste[len(liste) - 1]
# innholdet i liste[1] byttes med liste[len(liste) - 2]
# generelt: innholdet i liste[i] byttes med liste[len(liste) -i - 1] 
for i in range(0, int(len(liste) / 2)):
    j = len(liste) - 1 - i
    temp = liste[j]
    liste[j] = liste[i]
    liste[i] = temp
print(liste)
