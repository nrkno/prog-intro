"""6.5 - Lag en dictionary som inneholder tre store elver og landet elven går igjennom. Et eksempel kan være nilen : egypt.
Bruk en for-løkke for å printe ut en setning om hver elv, som for eksempel Nilen er i Egypt.
Bruk en for-løkke for å printe ut alle elvene som er inkludert i dictionarien.
Bruk en for-løkke for å printe ut alle landene som er inkludert i dictionarien."""

elver = {
    "Nilen" : "Egypt",
    "Amazonas" : "Brasil",
    "Yangzte" : "Kina"
}

for elv, land in elver.items():
    print(f"{elv} er i {land}")

for elv in elver.keys():
    print(elv)

print(elver.keys())

for land in elver.values():
    print(land)

print(elver.values())