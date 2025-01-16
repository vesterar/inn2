import numpy as np

# Program som regner om grader til radianer
v_grad = float(input("Skriv inn gradetallet: "))
v_rad = v_grad*np.pi/180

# Skriv svar med 2 desimaler
print(f"{v_grad} grader = {v_rad:.2f} radianer")



