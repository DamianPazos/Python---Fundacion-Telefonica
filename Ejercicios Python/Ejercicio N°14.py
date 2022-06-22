# Escribir un programa que llene una lista con 50 números al azar y muestre 
# por pantalla el número (o números) que más se repite.

import random

contador = 0
list_numeros_random = []
dicc_numeros = {}
valor_mas_alto = None
keys_mas_alto = []

while contador != 50:
    contador += 1
    numero_random = int((random.random())*10)
    list_numeros_random.append(numero_random)

for x in list_numeros_random:
    list_keys = dicc_numeros.keys()
    if x not in list_keys:
        dicc_numeros.update({x : 1})
    else:
        valor = dicc_numeros.get(x) + 1
        dicc_numeros.update({x : valor})

for y in dicc_numeros:
    if valor_mas_alto == None:
        valor_mas_alto = dicc_numeros.get(y)
    else:
        if valor_mas_alto < dicc_numeros.get(y):
            valor_mas_alto = dicc_numeros.get(y)
            
for y in dicc_numeros:
    if dicc_numeros.get(y) == valor_mas_alto:
        keys_mas_alto.append(y)

print(f'El numero que mas se repite en la lista es/son: {keys_mas_alto}')