# Oppgave: Min, max, sum

liste = [-34, 2, -24, 4, 23, -45, 5, 7, 35, 3]

# Finne minste tall

minst = liste[0]

for tall in liste:
    if tall < minst:
        minst = tall

print(f"Det minste tallet i listen er {minst}.")

# Finne største tall 

størst = liste[0]

for tall in liste:
    if tall > størst:
        størst = tall

print(f"Det største tallet i listen er {størst}.")

# Finne summen av tallene i listen

sum = 0

for tall in liste:
    sum = sum + tall

print(f"Summen av tallene i listen er {sum}.")

# Finne gjennomsnittet

gjennomsnitt = sum / len(liste)

print(f"Gjennomsnittet av tallene i listen er {gjennomsnitt}.")
