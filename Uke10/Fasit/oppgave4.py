def vis_hilsen(navn, alder, lokasjon):
    print(f"Velkommen {navn}! Du er {str(alder)} år gammel og bor i {lokasjon}")

vis_hilsen("Preben", 33, "Oslo")
vis_hilsen("Oslo", 33, "Preben")
vis_hilsen(lokasjon="Oslo", navn="Preben", alder=33)