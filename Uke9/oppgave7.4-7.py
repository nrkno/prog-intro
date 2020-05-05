
# 7.4 pizza toppings
prompt = "Skriv en pizzatopping, eller 'quit' for å avslutte: "
topping = ''
aktiv = True
while aktiv:
    topping = input(prompt)
    if topping == 'quit':
        aktiv = False
    else:
        print(f'Jeg putter {topping} på pizzaen')

# 7.5 kinobilletter
prompt = "Hvor gammel er du?\n'quit' for å avslutte: "
while True:
    tekst =  input(prompt)
    if tekst == 'quit':
        break

    alder = int(tekst)
    if alder < 3:
        print('Billetten er gratis.')
    elif alder < 12:
        print('Billetten koster 75 kr.')
    elif alder < 67:
        print('Billetten koster 150 kr.')
    else:
        print('Billetten koster 75 kr.')

#7.6
# conditional
tall = 0
while tall % 2 == 0:
    tall = int(input('Skriv et tall: '))
    print(f"Tallet {tall} er et fint tall!")
print(f"Ånei, {tall} er et oddetall, da kan vi ikke fortsette")

# aktiv-variabel: se løsning på 7.4
# break: se løsning på 7.5

# 7.7
'''
tall = 2
while tall < 10:
    print(tall)
    tall -= 1

while True:
    continue
'''