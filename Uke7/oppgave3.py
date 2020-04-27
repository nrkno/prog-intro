beholdning = {
    "kaffebønner" : 100,
    "melk" : 400,
    "sjokolader" : 100,
    "karameller" : 70
}
print("Beholdning")
print(beholdning)

liste_over_keys = list(beholdning.keys())
print(liste_over_keys)

bestilling = {
    "kaffebønner" : 20,
    "melk" : 40,
    "sjokolader" : 10,
    "karameller" : 2
}

harNok = True
for vare in liste_over_keys:
    if beholdning[vare] >= bestilling[vare]:
        print(f"Vi har nok av {vare}")
    else:
        print(f"Vi har ikke nok av {vare}")
        harNok = False

if harNok:
    for vare in liste_over_keys:
        beholdning[vare] = beholdning[vare] - bestilling[vare]
    print("Ny beholdning:")
    print(beholdning)
else:
    print("Var ikke nok dessverre, så bestillingen ble ikke gjennomført")


