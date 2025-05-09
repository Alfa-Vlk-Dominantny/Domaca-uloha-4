#Cast 2 - Palarerny pristup

import numpy as np
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool, cpu_count


def compute_row(args):
    y_idx, y_val, x, max_iter = args
    row_result = []
    for x_val in x:
        c = complex(x_val, y_val)
        z = 0
        for n in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:
                row_result.append(n)
                break
        else:
            row_result.append(max_iter)
    return y_idx, row_result

#PS Při paralelním výpočtu v Pythonu je zásadní uzavříd "globální část kódu" následující podmínkou:
if __name__ == "__main__":
    M = 2000  
    x_min, x_max = -2, 1
    y_min, y_max = -1, 1
    max_iter = 100


    x = np.linspace(x_min, x_max, M)
    y = np.linspace(y_min, y_max, M)

    row_args = [(i, y[i], x, max_iter) for i in range(M)]

    start_time = time.time()


    num_processes = cpu_count()

    with Pool(processes=num_processes) as pool:
        results = pool.map(compute_row, row_args)


    mandelbrot_set = np.zeros((M, M))
    for y_idx, row_result in results:
        mandelbrot_set[y_idx] = row_result

    end_time = time.time()
    execution_time = end_time - start_time


    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot_set, cmap='inferno', extent=[x_min, x_max, y_min, y_max])
    plt.colorbar(label='Počet iterácií')
    plt.title(f"Mandelbrotova množina (paralelný výpočet)\nČas výpočtu: {execution_time:.2f} s")
    #PS Popisky os grafů
    plt.xlabel("Reálna časť")
    plt.ylabel("Imaginárna časť")
    plt.show()
