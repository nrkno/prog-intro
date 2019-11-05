text = input('Jeg er en papegøye, skriv noe og jeg vil gjenta: ')
print(text)

# strengen man bruker i input-funksjonen kan være en variabel, 
# satt sammen av flere strenger, en format-string eller hva som helst som gir en streng
navn = 'Heidi'
prompt = f'Jeg er {navn}, skriv noe og jeg vil gjenta: '
text = input(prompt)
print(text)

# Om man vil gjøre om strengen brukeren skriver inn til et tall kan man bruke funksjonen int()
tall = input('Skriv et tall: ')
tall = int(tall)
print(tall + 10)

# Man kan ha input inni int om man vil, noen gang er det ok, andre ganger kan det kanskje være vanskeligere å lese hva som foregår
# Neste gang når vi lærer om funksjoner man feks lage en int_input funksjon som kan brukes i stedet
tall = int(input('Skriv et tall: '))
print(tall + 10)

# 7.1
bil = input('Hva slags bil vil du ha? ')
print(f'La meg se om jeg kan finne en {bil}')


# 7.2
antall_folk = int(input('Hvor mange personer er dere? '))
if antall_folk > 8 :
    print('Vennligst vent på ledig bord')
else:
    print('Bordet er klart')


# 7.3
tall = int(input('Gi meg et tall: '))
if tall % 10 == 0:
    print('Tallet er delelig med 10')
else:
    print('Tallet er ikke delelig med 10')


# 7-4
prompt = "\nHva vil du ha på pizzaen din?"
prompt += "\nSkriv inn en ingrediens eller 'quit' "
svar = ""
while svar != "quit":
    svar = input(prompt)
    if svar != "quit":
        print(f"Jeg skal putte {svar} på pizzaen din!")


#7-5
prompt = "\nVelkommen til NRKino! Hvor gammel er du? "
aktiv = True
while aktiv:
    svar = int(input(prompt))
    if svar < 3:
        print("Det er gratis!")
    elif svar <= 12:
        print("Det blir 10,-")
    else:
        print("Det blir 15,-")
  
    fortsette = input("Er det flere av dere?")
    aktiv = fortsette == "ja"


# 7-6
prompt = "\nHva vil du ha på pizzaen din?"
prompt += "\nSkriv inn en ingrediens eller 'quit' "
while True:
    svar = input(prompt)
    if svar != "quit":
        print(f"Jeg skal putte {svar} på pizzaen din!")
    else:
        break


# 7-7
# en evig for-løkke, brukt crtl + c for å komme ut av løkka
# while True:
#    print("hei")


# 7-8
smørbrød_bestillinger = ["roastbeef", "ost&skinke", "pastrami", "brie&bacon"]
ferdige_smørbrød = []
while smørbrød_bestillinger:
    smørbrød = smørbrød_bestillinger.pop()
    print(f"Lager {smørbrød.title()}!")
    ferdige_smørbrød.append(smørbrød)
for smørbrød in ferdige_smørbrød:
    print(f"Har laget {smørbrød.title()}")


# 7-9
smørbrød_bestillinger = ["roastbeef", "pastrami", "ost&skinke", "pastrami", "brie&bacon"]
ferdige_smørbrød = []
while "pastrami" in smørbrød_bestillinger:
    smørbrød_bestillinger.remove("pastrami")
    print("No pastrami for you!")
while smørbrød_bestillinger:
    smørbrød = smørbrød_bestillinger.pop()
    print(f"Lager {smørbrød.title()}!")
    ferdige_smørbrød.append(smørbrød)
for smørbrød in ferdige_smørbrød:
    print(f"Har laget {smørbrød.title()}")


# 7-10
besvarelser = {}
aktiv = True
while aktiv:
  navn = input("\nHva heter du? ")
  reisemål = input("\nHvor vil du reise? ") 
  besvarelser[navn] = reisemål
  fortsette = input("\nEr det fler som vil reise? (ja/nei) ")
  if fortsette == 'nei':
    aktiv = False
print("Besvarelser:")
for navn, reisemål in besvarelser.items():
  print(f"{navn.title()} vil reise til {reisemål}.")