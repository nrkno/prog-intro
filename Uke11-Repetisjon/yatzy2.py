import random

def kast(n):
    svar = []
    for i in range(0, n):
        terningverdi = random.randint(1, 6)
        svar.append(terningverdi)
    return svar

# beregn_kast([2, 5, 5, 2, 4], 2) = (4, 3)

def beregn_kast(et_kast, terningverdi):
    antall_terninger = len(et_kast)
    terninger_med_riktig_verdi = 0
    for terning in et_kast:
        if terning == terningverdi:
            terninger_med_riktig_verdi = terninger_med_riktig_verdi + 1
    terninger_med_feil_verdi = antall_terninger - terninger_med_riktig_verdi
    verdi_av_terninger = terningverdi * terninger_med_riktig_verdi
    return (verdi_av_terninger, terninger_med_feil_verdi)

def beregn_kast_direkte(et_kast, terningverdi):
    verdi_av_terninger = 0
    terninger_igjen = 0
    for terning in et_kast:
        if terning == terningverdi:
            verdi_av_terninger = verdi_av_terninger + terningverdi
        else:
            terninger_igjen = terninger_igjen + 1
    return (verdi_av_terninger, terninger_igjen)


#(verdi, terninger_igjen) = beregn_kast([2, 5, 5, 2, 4], 2)
(verdi, terninger_igjen) = beregn_kast_direkte([2, 5, 5, 2, 4], 2)

def runde(terningverdi):
    print(f"Kaster en runde for å få terninger med verdi {terningverdi}")
    totalverdi = 0
    terninger = 5
    for kast_nr in range(0, 3):
        print(f"Kast nummer {kast_nr + 1} (med {terninger} terninger).")
        et_kast = kast(terninger)
        print(f"Kastet ble: {et_kast}")
        (verdi, terninger_igjen) = beregn_kast(et_kast, terningverdi)
        print(f"Kastet var verdt: {verdi}")
        print(f"Jeg har igjen {terninger_igjen} terninger.")
        totalverdi = totalverdi + verdi
        terninger = terninger_igjen
    return totalverdi

enere = runde(1)
toere = runde(2)
treere = runde(3)
firere = runde(4)
femmere = runde(5)
seksere = runde(6)

totalt = enere + toere + treere + firere + femmere + seksere 
print(f"Du fikk {totalt} i sum.")
if totalt >= 63:
    print("Gratulerer, du fikk bonus!")
else:
    print("Dessverre, det ble ingen bonus på deg.")
