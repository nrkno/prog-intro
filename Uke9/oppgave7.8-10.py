# 7.8
'''
Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through the list
of sandwich orders and print a message for each order, such as 'I made your tuna sanwhich'.
As each sandwich is made, move it to the list of finished sandwiches. After all the
sandwiches have been made, print a message listing each sandwich that was made.
'''

sandwich_orders = ['blt', 'tuna', 'steak cheese', 'melt']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0) # .pop(0) fjerner første element i lista, .pop() fjerner siste
    print(f'{sandwich}-sandwichen er ferdig')
    finished_sandwiches.append(sandwich)

print('Disse sandwichene ble laget:')
for sandwich in finished_sandwiches:
    print(sandwich)


# 7.9
'''
No Pastrami: Using the sandwich_orders from Exercise 7-8, make sure the sandwich
'pastrami'appears in the list at least three times. Add code near the beginning of
your program to print a message saying the deli has run out of pastrami, and then
use a while loop to remove all occurrences of 'pastrami' from sandiwch_orders. Make sure
no pastrami sandwiches end up in finished_sandwiches.
'''

sandwich_orders = ['pastrami', 'blt', 'tuna', 'pastrami', 'pastrami', 'steak cheese', 'melt', 'pastrami']
finished_sandwiches = []

print('Subway(tm) er tom for pastrami-sandwich')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0) # .pop(0) fjerner første element i lista, .pop() fjerner siste
    print(f'{sandwich}-sandwichen er ferdig')
    finished_sandwiches.append(sandwich)

print('\nDisse sandwichene ble laget:')
for sandwich in finished_sandwiches:
    print(sandwich)


# 7.10
'''
Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to 'If you could visit one place in the world, where would
you go?' Include a block of code that prints the results of the poll.
'''

dream_vacations = {}
active = True

while active:
    name = input('Hva heter du? ')
    vacation = input('Hvis du kunne velge en drømmeferie, hvor ville det ha reist? ')

    dream_vacations[name] = vacation

    next_person = input('Er det flere personer i spørreundersøkelsen? ')
    if next_person == 'nei':
        active = False

print('\nBesvarelser:')
for name, vacation in dream_vacations.items():
    print(f'{name} kunne tenkt seg å reise til {vacation}.')
