kanaler = ["nrk1", "nrk2", "nrk3", "nrk4", "nrk5", "nrk6"]

for kanal in kanaler:
    print(f"{kanal} er en kanal")

print("Det var alle kanalene i NRK")

pizzas = ['pepperoni', 'ananas', 'ansjos', 'tunfisk']

#Pass på innrykk/indentering her. 
for pizza in pizzas:
    print (f"{pizza.title()}-pizza er en type pizza") #Dette er inne i løkka 


    print(" ")  #Dette er også inne i løkka
print("Pizza er bra, men ikke alle pizza er like gode") #Dette er utenfor løkka

animals = ["ilder", "mår", "røyskatt", "oter"]
for animal in animals: 
    #Pensum dag 5 if/else
    if animal == "oter":                                   # Inni for-løkka
        print (f"{animal.title()} er ikke et mårdyr")      # Inni for-løkka (og if-blokken)
    else:                                                  # Inni for-løkka
        print (f"{animal.title()} er et mårdyr")           # Inne for-løkka (og else-blokken)
print("Jeg synes disse dyra ligner lit på hverandre")      # Utenfor for-løkka

for tall in range(0,10):
    print(f"Tallet er {tall}")

kvadrater = []                  # Lag tom liste (for å ha et sted å ta vare på kvadrat-tallene)
for verdi in range(1,10):       # For "verdi" mellom 1 og 9
    kvadrat = verdi**2          # Sett verdien til variablen "kvadrat" til "verdi" opphøyd i andre ("verdi" er variablen som inneholder verdiene fra 1-9 i løkka, først 1, så 2, så 3 osv..) 
    kvadrater.append(kvadrat)   # Legg til verdien i variablen over i lista du lagde over. 
print(kvadrater)

kvadrater = [verdi ** 2 for verdi in range(1,10)] # Dette er helt ekvivalent til de fire linjene over. Lista inneholder "verdi" opphøyd i andre for "verdi" mellom 1 og 9.
print(kvadrater)

for number in range(1,21): #For å skrive ut verdier helt opp til 20, må du velge range opp til 21. 
    print(number)

onemillion = range(1, 1000001) #Liste med alle tall fra en til en million
# for number in onemillion:
#     print(number)

print(min(onemillion))  #Det minste tallet i lista (1)
print(max(onemillion))  #Det største tallet i lista (1000000)
print(sum(onemillion))  #Summen av alle tallene i lista (>1000)

odds = range(1, 20, 2) #Alle tall mellom 1 og 19, med steg 2 mellom tallene (dvs 1, 3, 5, 7...)
for n in odds:
    print(n)

evens = range(2, 21, 2) #Alle tall mellom 2 og 20 med steg 2 mellom tallene (dvs 2, 4, 6, 8...)
for n in evens:
    print(n)

threes = range(9, 82, 9) #Alle tall mellom 9 og 81 med steg 9 mellom tallene (9-gangen, 9, 18, 27, 36...)
for n in threes:
    print(n)

cubes = [] #Denne er tilsvarende eksemplet med kvadrater over
for n in range(1,11):
    cube = n ** 3
    cubes.append(cube)
print(cubes)

cubes = [n**3 for n in range(1, 11)]
print(cubes)

#Ikke pensum og ganske komplisert - Finn alle primtall mellom 1 og 99
for number in range(1,100):                     # for "number" mellom 1 til 99
    prime = True                                # Anta at tallet er et primtall (sett variablen "prime" til den boolske verdien True)
    for divisor in range(2,(int)(number/2)+1):  # for alle divisor fra 2 til ca number delt på 2 pluss 1. Husk at denne løkka er inni den første løkka, så den vil starte 99 ganger, en gang for hvert "number". Etterhvert som vi kommer lengre ut i den ytterste løkka og number blir større, vil denne innerste løkka iterere over flere tall. 
        if number % divisor == 0:               # Hvis "number" delt på "divisor" gir rest 0 (det vil si, number er delelig på divisor)
            prime = False                       # Da er tallet ikke et primtall
            break                               # Og da trenger vi ikke teste flere tall - det holder at tallet kan deles på ett tall. (break er en kommando som bryter ut av den løkka du er i - her vil altså den innerste løkka slutte å repetere seg etter "break").
    if prime:                                   # Hvis variablen "prime" er True
        print(number)                           # Print primtallet

kanaler = ["nrk1", "nrk2", "nrk3", "nrk4", "nrk5", "nrk6"]
print(kanaler[2:5]) #Print ut kanaler fra indeks 2 til 5 i lista
print(kanaler[:3])  #Print ut de tre første kanalene
print(kanaler[3:])  #Print ut kanaler fra indeks 3 og til slutten av lista
print(kanaler[-3:]) #Print ut de tre siste kanalene i lista

pizzas = ['pepperoni', 'ananas', 'ansjos', 'tunfisk']

# Kopier lista og legg til ting i den nye lista (den gamle forblir som den var)
vennepizza = pizzas[:]
vennepizza.append("Vegetar")
print(f"Den orginale listen inneholder {pizzas} \nDen nye listen inneholder {vennepizza}")

# Pek variablen "vennepizza" til den samme lista som variablen "pizzas" peker til
vennepizza = pizzas
vennepizza.append("Vegetar")
print(f"Den orginale listen inneholder {pizzas} \nDen nye listen inneholder {vennepizza}")

#Dette er en tuple
basic_foods = ('eggs', 'more eggs', 'omelette', 'scrambled eggs', 'poached eggs')
#Du kan gå gjennom den på samme måte som en liste
for food_item in basic_foods: 
    print(f"{food_item.title()} is a basic type of food")

#Men du kan ikke endre på elementer i lista, ei heller legge til elementer. 
#basic_foods[0] = 'not eggs'
#Hvis du kjører ^ denne får du feilen: "TypeError: 'tuple' object does not support item assignment"
#basic_foods.append('not eggs')
#Append() funksjonen finnes kun for lister. Prøver du den på en tuple, får du: "AttributeError: 'tuple' object has no attribute 'append'"

#Hvis du vil endre tuplen din, må du definere hele greia på nytt
basic_foods = ('not eggs', 'also not eggs', 'omelette', 'scrambled eggs', 'poached eggs')
for food_item in basic_foods: 
    print(f"{food_item.title()} is a basic type of food")