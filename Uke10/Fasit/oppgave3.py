def mindre_enn(tall, maksimumsverdi):
    for t in tall: 
        if (t > maksimumsverdi):
            tall.remove(t)
    return tall

liste = [0, 4 ,5 , 6, 2, 10]
print(mindre_enn(liste[:], 4))
print(liste)

def mindre_enn_kopi(orginale_tall, maksimumsverdi):
    tall = orginale_tall[:]
    mindre_enn(tall, maksimumsverdi)
    return tall
liste = [0, 4 ,5 , 6, 2, 10]
ny_liste = mindre_enn_kopi(liste, 4)
print(liste)
print(ny_liste)