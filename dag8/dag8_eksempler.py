from math import pi
from math import sin

#Enkel funksjon uten returverdi
def skriv_noe(noe):
    print(f"Du har skrevet \"{noe}\"")

#Enkel funksjon med returverdi
def sirkel_areal(radius):
     areal = pi * radius**2
     return areal

skriv_noe("noe")
print(sirkel_areal(1))

#Enkel funksjon med flere parametre
def areal_trekant(a, c, theta):
    return a*c*sin(theta)

#Parametre matches med argumenter basert på rekkefølge. 
print(areal_trekant(10,100,pi/6))
#Her blir det "feil"
print(areal_trekant(pi/6,10,100))
#Du kan også matche argumenter ved å navngi parameteren når du kaller funksjonen. Kallet under gir samme resultat som det første kallet over. 
print(areal_trekant(theta=pi/6, c = 100, a=10))

#Parametre kan settes til defualt-verdier. Du kan også la enkelte variable være valgfrie
def bygg_tvserie(tittel, antall_episoder, aarstall, land='Norge', orginalserie=''): 
    #Bygg grunn-tv serien med alle påkrevde argumenter
    tv_serie = {'tittel': tittel, 'antall episoder': antall_episoder, 'aarstall': aarstall, 'land': land}
    #Hvis orginalserie er satt, ta den med i tv-serie-dictionary
    if orginalserie: 
        tv_serie['orginalserie'] = orginalserie
    return tv_serie

#Hvis du endrer en liste inni en funksjon, endrer du den også utenfor funksjonen
def fiks_kanaler(kanaler):
    if "tv2" in kanaler:
        kanaler.remove('tv2')
    return kanaler 

kanaler = ['nrk1', 'nrk2', 'nrk3', 'tv2']

#Her sender vi inn en kopi av list - orginalen er uendret
fiksede_kanaler = fiks_kanaler(kanaler[:])
print(fiksede_kanaler)
print(kanaler)

#Her sender vi inn selve lista, her endrer vi på lista
fiks_kanaler(kanaler)
print(kanaler)

kanaler = ['nrk1', 'nrk2', 'nrk3', 'tv2']
#For å unngå å endre på lista via funksjonen, kan vi kopiere lista i selve funksjonen. 
def fiks_kanaler_v2(kanaler):
    kanaler_kopi = kanaler[:]
    if "tv2" in kanaler_kopi:
        kanaler_kopi.remove('tv2')
    return kanaler_kopi 

fiksede_kanaler = fiks_kanaler_v2(kanaler)
print(fiksede_kanaler)
print(kanaler)

def print_kanaler(*kanaler):
    for kanal in kanaler:
        print(kanal)


print_kanaler('nrk1', 'nrk2', 'nrk3', 'tv2')


##Rekursiv funksjon
# n=3
# def loop(n):
#     if n>0: 
#         print("continue")
#         loop(n-1)
#     else:
#         print("stop")

