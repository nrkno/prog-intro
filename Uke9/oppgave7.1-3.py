# oppgave 7.1
'''
Rent Car: Write a program that asks the user what kind of rental car they would like.
Print a message about that car, such as "Let me see if I can find you a Subaru"
'''

car = input('Hva slags leiebil ønsker du? ')
print(f'La meg se om jeg kan finne en {car} til deg!')


# oppgave 7.2
'''
Restaurant Seating: Write a program that asks the user how many people
are in their dinner gorup. If the answer  is more than eight, print a message
saying they'll have to wait for a table. Otherwise, report that teir table is ready
'''

people = input('Hvor mange er dere? ')
people = int(people)

if people > 8:
    print(f'Beklager, dere må nok vente på et ledig bord')
else:
    print(f'Ok, vi har et ledig bord her borte')


# oppgave 7.3
'''
Multiple of Ten. Ask the user for a number, 
and then report whether the number is a multiple of 10 or not
'''

number = input('Skriv inn et nummer: ')
number = int(number)

if number % 10 == 0:
    print(f'{number} er delbart med 10')
else:
    print(f'{number} er ikke delbart med 10')
