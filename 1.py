import numpy as np
vector = np.array([1, 2, 3])
print(vector)


print("version  ", np.__version__)
print("tipo de dato  ", type(vector))
print("dimension  ", vector.ndim)
print("forma  ", vector.shape)
#crear vector de ceros
vector_ceros = np.zero(5)
print(" vector de ceros ", vector_ceros)
#Crear vector para llenar con unos
vector_unos = np.ones(5)
print("vector de unos  ", vector_unos)
#Crear vector con un rango de numeros
vector_rango = np.arange(10)
print("vector con rango", vector_rango)