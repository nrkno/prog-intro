
'''
navn = ['Øyvind', 'Sven', 'Dag']

print(navn[0])
print(navn[1])
print(navn[2])

####

beskjed = "Hei "

print(f"Navnet er: {navn[0]}")
print(f"Navnet er: {navn[1]}")
print(f"Navnet er: {navn[2]}")

print(beskjed, navn[0])

####

kanaler = ["nrk1", "nrk2", "nrk3"]

kanaler.append("nrk4")
# print(kanaler)

kanaler.insert(0, 'nrk0')
# print(kanaler)

kanaler.insert(2, 'nrk1.5')
# print(kanaler)

kanaler[0] = ''
# print(kanaler)

# del kanaler[0]

#kanaler.insert(len(kanaler)+1, 'test')
kanaler.insert(-1, 'test2')

# gammel_kanal = kanaler.pop()
print(kanaler)
# print(gammel_kanal)

gammel_kanal = kanaler.remove('nrk2')
print(kanaler)
print(gammel_kanal)



kjendiser = ["Donald Duck", "Petter Stordalen", "Dronning Sonja"]
print(f"Hei {kjendiser[0]}, vil du komme på middag?")
print(f"Hei {kjendiser[1]}, vil du komme på middag?")
print(f"Hei {kjendiser[2]}, vil du komme på middag?")
print(f"{kjendiser[1]} kan dessverre ikke komme på middag")

kjendiser[1] = "Bruce Willis"
print(f"Hei {kjendiser[0]}, vil du komme på middag?")
print(f"Hei {kjendiser[1]}, vil du komme på middag?")
print(f"Hei {kjendiser[2]}, vil du komme på middag?")

print("Vi har blitt tildelt et nytt bord, og kan invitere flere gjester!")
kjendiser.insert(0, "Arne Hjeltnes")
# legg til verdi i "midten" av lista
kjendiser.insert(int(len(kjendiser)/2), "Deadpool")
kjendiser.append("Mikke Mus")
print(kjendiser)

print("Petter Stordalen har bestukket restauranten, og vi mistet bordet vårt.")
print("Vi kan kun invitere to personer.")

kjendis_bort = kjendiser.pop()
print(f"Beklager, {kjendis_bort}, du kan ikke komme.")
print(f"Beklager, {kjendiser.pop()}, du kan ikke komme")
print(f"Beklager, {kjendiser.pop()}, du kan ikke komme")
print(f"Beklager, {kjendiser.pop()}, du kan ikke komme")
print(kjendiser)

print(f"Du er fortsatt invitert {kjendiser[0]}")
print(f"Du er fortsatt invitert {kjendiser[1]}")

del kjendiser[0]
del kjendiser[0]

print(kjendiser)


'''


navn = ['1 Øyvind', 'Aage', 'Sven', 'dag']

navn.reverse()
print(navn)

navn.sort()
print(navn)
