# Escribir un programa que llene una lista con 50 números al azar y muestre 
# por pantalla el número (o números) que más se repite.

import random

contador = 0
list_numeros_random = []
dicc_numeros = {}

while contador != 51:
    contador += 1
    numero_random = int((random.random())*10)
    list_numeros_random.append(numero_random)

for x in list_numeros_random:
    if x in dicc_numeros.keys():
        valor = dicc_numeros.get(f'{x}') + 1
        dicc_numeros.update({f'{x}': valor})
    else:
        dicc_numeros.update({f'{x}': 1})


print(list_numeros_random)
print(dicc_numeros)
