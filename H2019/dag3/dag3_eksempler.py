#Her en noen av eksemplene vi tok felles på dag 3. 
#De fleste ting er forklart i kommentarer (med # - som denne kommentaren). 
# I noen tilfeller er kode kommentert ut - du kan selv fjerne kommentarer og kjøre og kommentere ut igjen etter ønske. 
print("Hello World")

#Definer liste
kanaler = ["nrk1", "nrk2", "nrk3"]
print(kanaler)

#Hent ut siste element i liste (og print det)
print(kanaler[-1])

#Print en beskjed sammen med et element i en liste
message = " er en av nrks kanaler"
print(f"{kanaler[0]}{message}")
print(f"Nrks lineære hovedkanal er {kanaler[0]}")

#Å iterere gjennom alle elementer i en liste og printe ut en beskjed (dette er pensum neste sesjon)
for kanal in kanaler:
    print(f"{kanal}{message}")

#Legg til et element bakerst i lista
kanaler.append('nrk4')
print(kanaler)

#Legg til et element fremst i lista
kanaler.insert(0 ,'nrk0')
print(kanaler)

#Erstatt et element i en liste med en ny verdi
kanaler[0] = 'nrk-1'
print(kanaler)

#Slett et element i en liste
del kanaler[0]
print(kanaler)

#Ta ut (pop) en verdi fra en liste. Nesten som del, men her kan du ta vare på elementet du fjerner
popped = kanaler.pop()
print(popped)
print(kanaler)

kanaler = ['nrk1', 'nrk2', 'nrk3', 'nrk4']

#Finn indeksen til det første elementet i en liste med en gitt verdi (dette er mer som en kuriositet og kanskje ikke superviktig å kunne)
print(kanaler.index('nrk3'))

#Kjapp fasit på oppgavene s 42-43
gjester = ['gjest 1', 'gjest 2', 'gjest 3']

for gjest in gjester:  #Obs: Dette er pensum neste uke
    print(f"Velkommen til middag, {gjest}")

#Alternativt uten løkker: 
beskjed = "Velkommen til middag,"
print(f"{beskjed} {gjester[0]}")
print(f"{beskjed} {gjester[1]}")
print(f"{beskjed} {gjester[2]}")

#Ersatt en gjest
print(f"Gjest 3 kan ikke komme, vi inviterer gjest 4 i stedet")
gjester[-1]='gjest 4'
print(gjester)

#Legg til en gjest fremst i lista
gjester.insert(0, 'gjest 0')
print(gjester)

#Legg til en gjest midt i lista
gjester.insert (2, 'gjest 2.5')
print(gjester)

#Legg til en gjest på slutten av lista
gjester.append('gjest 6')
print(gjester)

# Dette er pensum neste uke, men det er en enklere måte å pop-e/fjerne gjester til du bare har to igjen
#while (len(gjester) > 2): #Så lenge lengden på lista med gjester er større enn 2, 
#  print(f"{gjester.pop()} kan ikke komme") #Pop (fjern) en gjest fra lista og print navnet
#print(gjester)

#Dette er måten du kan gjøre nøyaktig det samme på uten en løkke
print(f"{gjester.pop()} kan ikke komme")
print(f"{gjester.pop()} kan ikke komme")
print(f"{gjester.pop()} kan ikke komme")
print(f"{gjester.pop()} kan ikke komme")
print(gjester)

#Liste med kanaler med både store og små bokstaver (og tall)
kanaler = ['tV2', 'euroSport', 'NRK2', 'nrK12']
print(kanaler)

#Sorter en kopi av listen og print den ut
print(sorted(kanaler))

#Sorter den faktiske listen (i minne) og print den
kanaler.sort()
print(kanaler) 

#Merk at lister av tekststrenger med både små og store bokstaver ikke sorteres "riktig". Derfor er det lurt å kun ha det ene i en liste

#To måter å bruke løkker til å endre alle elementene i lista slik at de kun inneholder små bokstaver. 
#Måte 1
#i = 0 
#while i<len(kanaler):
#    kanaler[i] = kanaler[i].lower()
#    i = i + 1
#Måte 2: 
for i in range (0,len(kanaler)):
    kanaler[i] = kanaler[i].lower()

print(kanaler)

#Sorter motsatt alfabetisk
print(sorted(kanaler, reverse=True))
kanaler.sort(reverse=True)
print(kanaler)

kanaler.sort()
print(kanaler)

#lister av tall sorteres fra minste til største tall
tall = [1, 16, 20, 39, 0 ]
print(tall)
print(sorted(tall))
tall.sort()
print(tall)

#Men - hvis du lagrer tallene som tekststrenger, kommer de alfabetisk - altså kommer 139 foran 16
tall_som_streng = ["1", "16", "12", "139", "0" ]
print(tall_som_streng)
print(sorted(tall_som_streng))


#Sniktitt på litt av pensum, dag 5: 
a = 1
b = 2
a = 2
if (a == b): #Hvis a og b er like, så
    print(f"{a} og {b} er like") #Print 
else: #Hvis ikke, så
    print(f"{a} og {b} er ulike") #Print
