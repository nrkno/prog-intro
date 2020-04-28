"""
Velg et tall (for eksempel 10) og lag en dictionary 
hvor tallene 1 til tallet du har valgt (for eksempel 1 til 10) er nøkkel, 
og tallet opphøyd i annen er value. Eksempel på dictionary:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
"""

opphøyd = {}

for i in range(1, 11):
    opphøyd[i] = i * i

print(opphøyd)