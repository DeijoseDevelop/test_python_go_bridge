import concurrent.futures
import time

def calculate_square(x):
    return x * x

def calculate_heavy_task(n):
    sum_squares = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(calculate_square, i) for i in range(1, n + 1)]
        for future in concurrent.futures.as_completed(futures):
            sum_squares += future.result()
    return sum_squares

if __name__ == "__main__":
    n = 1000000

    start_time = time.time()
    result = calculate_heavy_task(n)
    end_time = time.time()

    print(f"Resultado de la suma de cuadrados: {result}")
    print(f"Tiempo total en Python: {end_time - start_time:.2f} segundos")
