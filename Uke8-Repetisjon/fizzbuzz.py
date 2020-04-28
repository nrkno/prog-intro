# Oppgave: FizzBuzz

"""
Gå gjennom tall fra 1 til 100 og skriv ut etter følgende regler:

    Hvis tallet er delelig med 3 skal ordet Fizz skrives ut
    Hvis tallet er delelig med 5 skal ordet Buzz skrives ut
    Hvis tallet er delelig med både 3 og 5 skal ordet FizzBuzz skrives ut
    Hvis tallet hverken er delelig med 3 eller 5 skal tallet skrives ut.

De første tjue tallene skal bli til 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz
"""

# Heltallsdivisjon:
# tall / 3 
# 3 / 3 == 1 (3 går en hel gang i 3)
# 4 / 3 == 1 (4 går en hel gang i 3)
# 5 / 3 == 1 (5 går en hel gang i 3)
# 6 / 3 == 2 (6 går to hele ganger i 3)

# Modulo (Rest fra heltallsdivisjon)
# Sjekke om et tall er delelig på 3: tall % 3 == 0? (True eller False?)
# 3 % 3 == 0 (Delelig med 3, rest er 0)
# 4 % 3 == 1 (Ikke delelig med 3, rest er 1)
# 5 % 3 == 2 (Ikke delelig med 3, rest er 2)
# 6 % 3 == 0 (Delelig med 3, rest er 0)

fizzer = 0
buzzer = 0
fizzbuzzer = 0

for tall in range(1, 101):
    if tall % 3 == 0 and tall % 5 == 0: # if tall % 15 == 0
        print("FizzBuzz")
        fizzbuzzer = fizzbuzzer + 1
    elif tall % 3 == 0:
        print("Fizz")
        fizzer = fizzer + 1
    elif tall % 5 == 0:
        print("Buzz")
        buzzer = buzzer + 1
    else:
        print(tall)

print(f"Det er {fizzbuzzer} FizzBuzz'er.")
print(f"Det er {fizzer} Fizz'er.")
print(f"Det er {buzzer} Buzz'er.")
print(f"Og {100 - fizzbuzzer - fizzer - buzzer} vanlige tall.")
