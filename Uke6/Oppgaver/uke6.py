#print(True)
#print(False)
#print(True and True)
#print(True and False)
#print(True or True)
#print(True or False)
#print(False or False)
#print(not True)
#print(not False)
#print(True and not True)
#print(True and not False)
#print(not True or not False)
#print(3 > 3)
#print(3 >= 3)
#print(3<3)
#print(3<=3)
#print(3==3)
#print(3!=3)

liste = [34, 2, 24, 4, 23, 45, 5, 7, 35, 3]
maksverdi = 10

for tall in liste:
    #print(f"Tall er {tall}")
    if tall < maksverdi:
        print(tall)

liste = [-34, 2, -24, 4, 23, -45, 5, 7, 35, 3]

minste_til_naa = liste[0]

for tall in liste:
    #print(f"Tall vi gaar igjennom{tall}")
    #print(f"Minste til naa {minste_til_naa}")
    if minste_til_naa > tall:
        #print(f"Bytter minste til naa")
        minste_til_naa = tall
        #print(f"Minste til naa {minste_til_naa}")

print(f"Minste tall er {minste_til_naa}")