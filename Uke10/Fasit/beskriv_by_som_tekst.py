def beskriv_by_som_tekst(by, land):
    return f"{by.title()} ligger i landet {land.title()}"

by = "mo i rana"
land = "norge"
setning = beskriv_by_som_tekst(by, land)
print(setning)