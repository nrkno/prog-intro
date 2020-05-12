def info_om_bil(produsent, modellnavn, **info):
    info["produsent"] = produsent
    info["modellnavn"] = modellnavn
    return info

print(info_om_bil("Tesla", "Model S", farge="Rød"))
print(info_om_bil("Tesla", "Model S", farge="Blå", Eier="Truls", Arne="hei"))