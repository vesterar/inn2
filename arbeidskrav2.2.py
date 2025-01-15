import math


# Beregning av antall pizzaer til elever
antall_elever = int(input("Skriv inn antall elever: "))
antall_pizza = math.ceil(antall_elever / 4)

print(f"Det må handles inn {antall_pizza} pizza til festen")