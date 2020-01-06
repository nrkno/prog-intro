# Variabler

# Variabler kan kun inneholde bokstaver, tall og understrek, og de kan ikke starte med et tall

message = "Hello world!"
message2 = "Hello world again!"
message_three = "Hey world!"

# Multiple assignment - man kan deklarere flere variabler med verdier på én linje
message1, message2 =  "hello", "hei"
x, y, z = 0, 1, 2

# Konstanter - verdien til denne variablen skal ikke endres
# Obs: Python gjør ingen sjekker på dette; man kan endre verdien, men upper case indikerer at verdien skal være konstant
MESSAGE = "Hello constant world!"


# Strenger

# Strenger (strings) er en serie med karakterer eller tegn. «Alt» innenfor enkle eller doble «fnutter» regnes som strenger.
string1 = "Dette er en streng"
string2 = 'Dette er også en streng'
string3 = "Dette er en streng som inneholder en fnutt: \" "

# Legge variabler i strenger
hei = "Hei "
paa = "på "
deg = "deg!"
message_with_variables = hei + paa + deg                    # Hei på deg!
message_with_variables_with_format = f"{hei}{paa}{deg}"     # Hei på deg!
message_godt_og_blandet = f"Hei {paa}" + deg                # Hei på deg!

# Strenger med tabs og newline
tab = "Dette er en streng \t med en tab"
newline = "Dette er en \n streng med en newline"

# Noen string-metoder som er innebygd i Python
name = "Ada lovelace"
name.title() # Ada Lovelace
name.lower() # ada lovelace
name.upper() # ADA LOVELACE

name = "     Ada Lovelace     "
name.lstrip() # 'Ada Lovelace     '
name.rstrip() # '     Ada Lovelace'
name.strip()  # 'Ada Lovelace'


# Tall

# Heltall og desimaler (integers og floats)
heltall = 1
desimal = 2.5

# Kan legge til, trekke fra, multiplisere, dele og opphøye i eksponent
tall1 = 5
tall2 = 3
tall_sum = tall1 + tall2    # 8
tall_sum = tall1 - tall2    # 2
tall_sum = tall1 * tall2    # 15
tall_sum = tall1 / tall2    # 1.6666666...
tall_sum = tall1 ** tall2   # 125

# Understrek kan benyttes for å gjøre store tall mer lesbare
tall_stort = 14_000_000_000 # 14000000000

