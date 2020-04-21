#Oppgave 2

ansatte = {}

ansatte["n652508"] = "Malin"

print(ansatte)

ansatte["n652508"] = "Malin Aandahl"

print(ansatte)

ansatte["n111111"] = "Einar"

print(ansatte)

for ansattnr in ansatte.keys():
    print(ansattnr)

for navn in ansatte.values():
    print(navn)



