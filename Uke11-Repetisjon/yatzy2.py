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

print(f"Verdi av 2'ere: {verdi}")
print(f"Terninger igjen: {terninger_igjen}")

