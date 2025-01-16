# Beregne omkrtest og areal av figur oppgave 2.5

import math

b = float(input("Skriv in lengden på katet b (cm): "))
a = float(input("Skriv in lengden på katet a (cm): "))

def kalkuler_areal_og_omkrtest(a, b):
    # beregn hypotinus
    c = math.sqrt(a ** 2 + b ** 2)

    # breegn areal av halvsirkel
    areal_halv_sirker = (math.pi * a * a) / 2

    # beregn areal av trekant
    areal_trekant = (b*a)/2

    # Total areal
    total_areal = areal_trekant + areal_halv_sirker

    # Ytre omktest av figur
    omkrets_trekant = a + b + c
    omkrtes_halvsirkel = (math.pi * 2 * a) / 2
    total_omkrets = omkrets_trekant + omkrtes_halvsirkel - c

    return total_areal, total_omkrets


areal, omkrets = kalkuler_areal_og_omkrtest(a, b)
square_c_meter = "cm\u00b2"
print(f"Arealet av figuren er: {areal:.2f} {square_c_meter}")
print(f"Omkrets av figuren er: {omkrets:.2f} cm")
