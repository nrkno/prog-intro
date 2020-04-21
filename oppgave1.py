# Oppgave 1

lindmo = {
    "id": "abe0f2e1ef19ab6e150cabfd46377a58",
    "title": "Lindmo",
    "subtitle": "Norsk talkshow",
    "category": "underholdning"
}

kategori = lindmo["category"]
print(f"Kategori er {kategori}")

print( lindmo.get("seriesType", "Ingen verdi"))

lindmo["seriesType"] = "standard"

print( lindmo.get("seriesType", "Ingen verdi"))

print(lindmo)

del lindmo["id"]

print(lindmo)

