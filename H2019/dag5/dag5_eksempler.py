#To måter å sjekke om noe ligger i en liste
kanaler = ['nrk1', 'nrk2', 'nrk3', 'nrk4', 'nrk5', 'nrk6']
#Måte 1: 
for kanal in kanaler:  #For hver kanal i kanaler
    if kanal == 'nrk1':#Hvis kanalen er lik nrk1, så
        print("Detter er nrks hovedkanal for lineær-tv")
#Måte 2
if 'nrk1' in kanaler: #Hvis nrk1 finnes i kanaler, så
            print("Detter er nrks hovedkanal for lineær-tv")

#Sjekk om lista inneholder noe
if kanaler:
    print('Vi har kanaler')
else: 
    print("Ingen kanaler funner")



#5-2, s. 78
hovedkanal = "nrk1"
#equality
print(hovedkanal == 'nrk1') #True
#inequality
print(hovedkanal != 'nrk2') #True

#Ikke gjør dette hjemme - du kan bruke større enn og mindre enn på strenger. Da sjekker de alfabetisk, dvs nrk1 < nrk2 
print(hovedkanal < "nrk2") #True

#Sjekk strenger case insensitivt
hovedkanal = "NRK1"
print(hovedkanal == "nrk1") #False
print(hovedkanal.lower() == "nrk1") #True

nummer1 = 1
nummer2 = 1000

#Mindre enn
print(nummer1 < nummer2) #True
#Større enn
print(nummer1 > nummer2) #False
#Større enn eller lik
print(nummer1 >= 1) #True
print(nummer1 <= 1) #True

#Sjekk flere utrykk samtidig. 
print(nummer1 >= 0 and nummer2 <= 1000) #True     - hvis nummer1 er større eller lik 0 og nummer2 er mindre eller lik 1000 
print(nummer1 < 0 or nummer2 >= 1000) #True       - hvis nummer1 er mindre enn 0 eller nummer2 er større eller lik 1000

#Finnes tall i liste
liste = list(range(1,1000,16))

print(372 in liste) #False - finnes ikke i lista
print(417 not in liste) #False - finnes i lista

alder = 12

#Du kan lagre den boolske spørringa i en variabel. 
is_old = alder > 100     #is_ols er en variabel av typen bool. Den vil være True eller False
if is_old:   #Tilsvarer if alder > 100:
    print("Gammel")

#Yoda style - variabelen sist. 
if 11 < alder:
    print ("Yoda")

alder = 13
#Mer kompliserte spørringer. Du kan bruke paranteser for å gruppere spørringer logisk
if ((alder > 6 and alder < 18) or alder > 67): # I dette tilfellet har ikke parantesen noe å si - resultatet blir uansett det samme
    print ("pris = 20")

#I dette eksemplet har plasseringen av parantesen betydning. 
tallet = -3
if (tallet > 0 and tallet %2 == 0) or tallet % 3 == 0: #Hvis tallet er større enn 0 og tallet er et partall (delelig på 2), eller tallet er delelig på 3
    print("Tallet oppfyller kriteriene") #True når tallet = -3  
else: 
    print("Tallet oppfyller ikke kriteriene")  

if tallet > 0 and (tallet %2 == 0 or tallet % 3 == 0): #Hvis talleet er større enn 0 og i tillegg er delelig på enten 2 eller 3. 
    print("Tallet oppfyller kriteriene") #False for tallet = -3 
else: 
    print("Tallet oppfyller ikke kriteriene")  

#5-3, 5-4, 5-5, s. 84
alien_color = 'rød'
# alien_color = 'gul'
# alien_color = 'grønn'
#alien_color = 'blå'
alien_type = 'big'

if 'grønn' == alien_color:
    print("5 poeng til deg")
    if alien_type == 'big':  #Denne if-en er inni if-blokka "if 'grønn' == alien_color"
        print("5 poeng ekstra for stort romvesen")
elif 'gul' == alien_color:
    print("10 poeng til deg")
elif 'rød' == alien_color: 
    print("15 poeng til deg")
else:                           #Her brukes else til å fange opp alle andre tilfeller enn de tre "lovlige" fargene
    print("Ugyldig farge")

alder = 41.857382

if alder < 2:   # Denne slår også ut for negativ alder. Hvordan ville du fikset det?
    print("Dette er en baby")
elif alder < 4: # Her vil else if kun slå inn hvis alder er fra 2 til 4 år
    print("Dette er et småbarn")
elif alder < 13:
    print("Dette er et barn")
elif alder < 20:
    print("Dette er en tenåring")
elif alder < 65:
    print("Dette er en voksen")
elif alder < 90:
    print("Denne personen er godt voksen")
else:         #Denne slår inn for alt som ikke matches over, i dette tilfelle alle aldre fra 90 år og oppover. 
    print("Dette er en olding")

#5-8 til 5-11
usernames = ['bruKer1', 'bruker2', 'bruker3', 'bruker5', 'bruker5', 'admin']
#usernames = []

if usernames: #Sjekk om lista er tom 
    for user in usernames: #For hver bruker i lista
        if user == 'admin': #Hvis brukeren heter admin
            print("Halloen, Admin")
        else:               #Ellers, for alle andre brukere
            print("Velkommen, {user}")
else: #Denne elsen hører til den første if-en, denne intreffer kun hvis lista er tom. 
    print("Ingen brukere i lista")

usernames = ['bruKer1', 'bruker2', 'bruker3', 'bruker5', 'bruker5', 'admin']
new_users = ['brukEr6', 'brUker1', 'admin']

#Denne sjekker om brukeren finnes i lista, men funker ikke hvis brukernavnene i "usernames" ikke allerede er lower case
#Her vil feks "brUker1" aksepteres, selv om den egentlig finnes i usernames som "bruKer1"
for new_user in new_users:
    if new_user.lower() in usernames:
        print(f"Brukernavnet {new_user} er opptatt") 

#En måte å løse dette på er å gå gjennom begge listene etter tur
for new_user in new_users:  #For hver nye bruker i lista,
    user_exists = False     #Før vi sjekker, antar vi at brukeren ikke finnes
    for user in usernames:  #Så sjekker vi lista med eksisterende brukere. For hver bruker i lista, 
        if new_user.lower() == user.lower():    #Hvis new_user og user er like, så eksisterer brukeren fra før 
            user_exists = True                  #Og da setter vi user_exists til True
    
    if user_exists:                             #Nå er vi utenfor løkka som sjekker eksisterende brukere og sjekker om vi har funnet en eksisterende bruker som er lik den nye brukeren. 
        print("Brukernavnet er allerede i bruk")
    else:       #Hvis brukeren ikke finnes fra før,
        usernames.append(new_user.lower()) #Legg den nye brukeren til i lista over brukere
        print(f"Bruker {new_user} lagt til i lista over brukernavn")

#Et alternativ til dette er å sikre at alle brukernavn i lista allerede er i lower case
for i in range(0,len(usernames)):
    usernames[i] = usernames[i].lower()

#Engelskse ordinaler (5-11)
tall = list(range(1,10))
for t in tall:
    if t == 1:      #Håndter spesialtilfellene
        print("1st")
    elif t == 2:
        print("2nd")
    elif t == 3:
        print("3rd")
    else:
        print(f"{t}th") #Alle andre har ending -th
##################################################

#Finn hvilken indeks et objekt ligger på
kanaler = ['nrk1', 'nrk2', 'nrk3', 'nrk4', 'nrk5', 'nrk6']
#Dette er den pyhtonske måten å gjøre det på: 
print(f"nrk3 ligger på indeks {kanaler.index('nrk3')}") #Merk at denne kun finner det første innslaget av 'nrk3' i lista. Hvis det er flere, blir de ignorert. 

#Dette er den tungvinte måten, men funker for stort sett alle språk. 
for i in range(0,len(kanaler)):
   if kanaler[i] == 'nrk3':
       print(f"nrk3 ligger på indeks {i}")


#None definerer null-verdier, eller ikke-eksisterende verdier. Ikke så relevant for oss, men greit å vite. 
kanaler = None
if kanaler is None: 
    print(kanaler)