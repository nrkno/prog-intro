#8-3 og 8-4
def make_tshirt(size='L', message="Hello World"):
    print(f"A size {size} tshirt with message \"{message}\"")

#Pass på at du skjønner hvorfor hvert av eksemplene printer det de printer
make_tshirt('M') #Overstyrt size, default message
make_tshirt('M','Goodbye World!') #Begge overstyrt
make_tshirt(message='Hello Mars', size = 'M') #Begge overstyrt, matchet vha. parameternavn
make_tshirt() #Både size og message default

#8-5
def describe_city(city, country='Norway'):
    print(f"{city} is in {country}")

describe_city('Bergen')
describe_city('London', 'England')
describe_city('Timphu', 'Bhutan')

#8-6
def city_country(city, country):
    return f"{city}, {country}"

print(city_country("Santiago", "Chile"))

#8-7
def make_album(artist, album, number_of_songs=None):
    album = {'artist': artist ,'album': album}
    if number_of_songs: 
        album['number of songs'] = number_of_songs  #Denne tas med kun hvis number_of_songs er satt
    return album

print(make_album('Big Thief', 'UFOF'))

#Du kan bruke returverdien videre. Her lager vi en liste med to dictionaries
albums = [make_album('Pink Floyd', 'Dark Side of the Moon', 10), make_album('Big Thief', 'UFOF')]
print(albums)

#8-8
# while True:
#     artist = input("Artist: ")
#     if artist == 'q' or artist == 'quit':
#         break
#     album = input("Album: ")
#     if album == 'q':
#         break
#     number_of_songs = input("number_of_songs: ")
#     if number_of_songs == 'q':
#         break
#     print(make_album(artist, album, number_of_songs))

#8-9
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Beskjed 1", "Beskjed 2", "Beskjed 3", "Beskjed 4"]
show_messages(messages)

#8-10 og 8-11
sent_messages = [] 
def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(messages[:])
print(messages)
print(sent_messages)

sent_messages= []

send_messages(messages)
print(messages)
print(sent_messages)


#8-12
def sandwiches(*items):
    summary =  "The sandwich contains the following items: "
    for i in range(0,len(items)-1):  #Tar ikke med siste elementet i lista for å unngå et ekstra komma på slutten
        summary = summary + items[i] + ", " #Du kan plusse sammen strenger 
    summary = summary + items[-1] #Legg til det siste elementet i lista uten komma bak 
    print(summary) #Print den ferdige strengen

sandwiches("ost", "skinke", "smør", "løk")