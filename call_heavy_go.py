import ctypes
import os
import platform
import time

if platform.system() == 'Windows':
    libname = os.path.join(os.getcwd(), "heavy_go.dll")
else:
    libname = os.path.join(os.getcwd(), "heavy_go.so")

heavy_go = ctypes.CDLL(libname)

heavy_go.CalculateHeavyTask.argtypes = [ctypes.c_int64]
heavy_go.CalculateHeavyTask.restype = ctypes.c_int64

n = 1000000

start_time = time.time()
result = heavy_go.CalculateHeavyTask(n)
end_time = time.time()

print(f"Resultado de la suma de cuadrados calculado en Go: {result}")
print(f"Tiempo total en Python llamando a Go: {end_time - start_time:.7f} segundos")
