#Cast 1 - Nepalarerny pristup

import numpy as np
import matplotlib.pyplot as plt
import time

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return n
    return max_iter

"""
Pokiaľ program nesplní podmienku tak to vráti maximálny počet iterácii, inak ta funkcia počíta podľa predpisu
"""


M = 2000
x_min, x_max = -2, 1
y_min, y_max = -1, 1
max_iter = 100


x = np.linspace(x_min, x_max, M)
y = np.linspace(y_min, y_max, M)
mandelbrot_set = np.zeros((M, M))


start_time = time.time()

for i in range(M):
    for j in range(M):
        c = complex(x[i], y[j])
        mandelbrot_set[j, i] = mandelbrot(c, max_iter)

end_time = time.time()
execution_time = end_time - start_time


plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set, cmap='inferno', extent=[x_min, x_max, y_min, y_max])
plt.colorbar(label='Počet iterácií')
plt.title(f"Mandelbrotova množina (neparalelný výpočet)\nČas výpočtu: {execution_time:.2f} s")
#Popisky os grafů
plt.xlabel("Reálna časť")
plt.ylabel("Imaginárna časť")
plt.show()
