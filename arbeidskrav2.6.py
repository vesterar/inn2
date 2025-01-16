# Kode for plotting av funksjonen f(x) = -x2 -5

import numpy as np
import matplotlib.pyplot as plt

# funksjon for utregning
def f(x):
    return x**2 - 5


x = np.linspace(-10, 10, 400)
y = f(x)
plt.plot(x, y,)


plt.title('Plotting a Function')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
