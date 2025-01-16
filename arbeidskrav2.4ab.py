# Oppgave 2.4 a og b for å skrive ut hovedstad og hovedstadsbefolkning i valgt land
data = {"Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }


def hent_befolkning(land):
    if land in data:
        return data[land][1]

    else:
        return "landet finnes ikke i dictionaryen"


def hent_hovedstad_(land):
    if land in data:
        return data[land][0]

land = input("Skriv ett land: ")
befolkning = hent_befolkning(land)
hovedstad = hent_hovedstad_(land)
print(f"{hovedstad} er hovedstaden i {land} og det er {befolkning} mill. innbyggere i {hovedstad}.")
