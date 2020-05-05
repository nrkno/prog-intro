# oppgave 7.1

car = input('Hva slags leiebil ønsker du? ')
print(f'La meg se om jeg kan finne en {car} til deg!')


# oppgave 7.2

people = input('Hvor mange er dere? ')
people = int(people)

if people > 8:
    print(f'Beklager, dere må nok vente på et ledig bord')
else:
    print(f'Ok, vi har et ledig bord her borte')


# oppgave 7.3

number = input('Skriv inn et nummer: ')
number = int(number)

if number % 10 == 0:
    print(f'{number} er delbart med 10')
else:
    print(f'{number} er ikke delbart med 10')