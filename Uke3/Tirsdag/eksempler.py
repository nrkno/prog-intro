serier = ["Skam", "Nobel", "Exit"]
print(serier)
print(serier[0])
print(f"Dette blir det samme: {serier[2]} og {serier[-1]}")
#print(f"Dette blir feil: {serier[3]}")

#Oppgaver s. 36 
#3-1: Navn - Lagre navnene til noen av vennene dine i en liste du kaller “navn”. Print navnene til alle i lista ved å hente ut hvert element i lista, én etter én. 

navn = ["Bjørn", "Malin", "Heidi"]
hilsen = "Hei og hallo"
print(f"{hilsen} {navn[0]}!")
print(f"{hilsen} {navn[1]}!")
print(f"{hilsen} {navn[2]}!")

serier = ["dagsrevyen", "exit", "lindmo"]
print(serier[2])
print(serier[-1])
# print(serier[-4]) Gir index out of range
serier.append("norge rundt")

serier.insert(0, "debatten")
print(serier)
#serier[0] = "ikke debatt"
#print(serier)
del serier[2]
print(serier)
serier.pop()
print(f"Denne verdien ble fjernet fra lista {serier.pop()}")
print(serier)
#serier[7] = "ny serie"


gjester = ["Bjørn", "Malin", "Heidi"]
beskjed = "Velkommen til middag, "
print(f"{beskjed}{gjester[0]}")
print(f"{beskjed}{gjester[1]}")
print(f"{beskjed}{gjester[2]}")
print(f"{gjester[1]} kunne ikke komme.")
gjester[1] = "Per Edvard"
print (gjester)

gjester.insert(0,"Einar")
gjester.append("Kristoffer")
gjester.insert(int(len(gjester)/2), "Malin")
print(gjester)
#for gjest in gjester: 
#    print (gjest)

print(f"Vi har invitert {len(gjester)} gjester. De er: {gjester[0]}")

gjester.pop()
print(gjester)
gjester.pop()
print(gjester)
gjester.pop(int(len(gjester)/2))
print(gjester)
gjester.pop(int(len(gjester)/2))
print(gjester)
gjester.pop(int(len(gjester)/2))
gjester.pop(int(len(gjester)/2))
print(gjester)

original_liste = ["Malin", "Heidi", "Bjørn"]
ny_liste = sorted(original_liste)
original_liste.reverse()
print(original_liste)
print(original_liste)
print(ny_liste)

ny_liste.insert(len(ny_liste), "Siste element")
print(ny_liste)
ny_liste.insert(0, "Første element")
print(ny_liste)
del ny_liste[0]
print(ny_liste)
print(list(reversed(ny_liste)))

