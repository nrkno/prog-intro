"""Dersom man er under 2 år, skal programmet skrive ut “baby”. 
Dersom man er over 2 år og under 4 år, skal programmet skrive ut “toddler”. 
Dersom man er over 4 år og under 13 år, skal programmet skrive ut “kid”. 
Dersom man er over 13 år og under 20 år, skal programmet skrive ut “teenager”. 
Dersom man er over 20 år og under 65 år, skal programmet skrive ut “adult”. 
Dersom man er over 65 år, skal programmet skrive ut “elder”. """


alder = 65

if alder < 2:
    print("Baby")
elif alder >= 2 and alder < 4:
    print("Toddler")
elif alder >= 4 and alder < 13:
    print("Kid")
elif alder >= 13 and alder < 20:
    print("Teenager")
elif alder >= 20 and alder <= 65:
    print("Adult")
elif alder > 65:
    print("Elder")
