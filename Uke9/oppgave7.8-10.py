# Det kan være lurt å kommentere ut hver oppgave før scriptet kjøres


# 7.8

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
