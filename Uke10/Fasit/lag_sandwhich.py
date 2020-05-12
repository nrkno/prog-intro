def lag_sandwich(*ingredienser):
    print("Sandwichen inneholder disse ingrediensene:")
    for ingrediens in ingredienser:
        print(f"{ingrediens},")

lag_sandwich("Ost", "Skinke")