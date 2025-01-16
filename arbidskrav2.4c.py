# Program for å legge til land i dictionary

data = {"Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]

        }

# Skriv ut land i dictionary
print("Land in dictionary: ")
for land in data.keys():
        print(land)

land = input("Skriv ett nytt land: ")
hovedstad = input("Skriv inn hovedstad for dette landet: ")
innbygger_hovedstad = float(input(f"Skriv inn innbyggere i {hovedstad}: "))

# legge til land
data[land] = [hovedstad, innbygger_hovedstad]

print(data)

