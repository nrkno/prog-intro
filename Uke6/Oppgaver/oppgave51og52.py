#Hva printer koden ut?
bil = "subaru"
print("Er bil == ‘subaru’ Jeg tror True")
print(bil == "subaru")
print("Er bil == ‘audi’? Jeg tror False")
print(bil == "audi")

#Lag en test for likhet og ulikhet for tekstvariabler selv.

navn = "Malin"
print(navn == "Malin")

if navn == "Malin":
    print("Navn er Malin!")

if navn != "Tone":
    print("Navn er ikke lik Tone!")

#Lag en test for tallvariabler (mindre enn, større enn, erlik).

alder = 3

if alder < 18:
    print("Du er ikke myndig")

if alder >= 18:
    print("Du er myndig!")

#Bruk lower()-metoden til tekstvariabler
print(f'Bruk av lower: {navn.lower() == "malin"}')

#En som bruker and og en som bruker or

if(alder >= 13 and alder <= 19):
    print("Tenaaring")

if(alder < 13 or alder > 19):
    print("Ikke tenaaring - noe annet")

#Sjekk om et element er i en liste

liste = [1, 2, 4]
tall = 3
if tall in liste:
    print(f"Tallet {tall} er i lista!")


#Sjekk om et element ikke er i en liste
if tall not in liste:
    print(f"Tallet {tall} er ikke i lista!")
