"""
Fjerne duplikater
Lag et program som løper gjennom en liste og 
lager en ny liste som er som den opprinnelige lista, 
bortsett fra at hver verdi bare finnes én gang i den nye. 
Skriv ut den nye lista.

For eksempel skal programmet med lista 
[1, 4, 7, 5, 8, 3, 4, 5, 2, 1, 3] skrive ut [1, 4, 7, 5, 8, 3, 2] 

liste = [1, 4, 7, 5, 8, 3, 4, 5, 2, 1, 3]
ny_liste = []
"""

liste = [1, 4, 7, 5, 8, 3, 4, 5, 2, 1, 3]
ny_liste = []

for i in liste:
    if i not in ny_liste:
        ny_liste.append(i)

print(ny_liste)