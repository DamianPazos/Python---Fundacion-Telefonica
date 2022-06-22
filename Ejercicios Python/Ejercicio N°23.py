# Escribir un programa que genere 20 números al azar entre 1 y 5, los guarde 
# en una lista, muestre la lista y luego muestre los dos números que más se 
# repiten.
# En caso de haber dos o más números con la misma cantidad de apariciones, 
# mostrarlos a todos. Por ejemplo, el número más repetido es el 5, mostramos 
# el 5, pero en segundo lugar aparecen los números 2 y 4 con la misma 
# cantidad de repeticiones, mostrarlos a ambos, además de mostrar el 5.

import random

contador = 0
list_numeros_random = []
dicc_numeros = {1:0,2:0,3:0,4:0,5:0}
lista_valores = []
numeros_mas_repetidos = []
numeros_segundos = []

while contador != 20:
    contador += 1
    numero_random = int((random.random())*5+1)
    list_numeros_random.append(numero_random)

for x in list_numeros_random:
    for y in dicc_numeros:
        if x == y:
            valor = dicc_numeros[y] + 1
            dicc_numeros.update({y : valor})

for i in dicc_numeros.values():
    lista_valores.append(i)

lista_valores.sort(reverse=True)

for j in dicc_numeros:
    if dicc_numeros[j] == lista_valores[0]:
        numeros_mas_repetidos.append(j)
    elif dicc_numeros[j] == lista_valores[1]:
        numeros_segundos.append(j)

print(f'La lista de numeros que se creo es {list_numeros_random}')
print(f'El/Los numero/s que mas se repite/n es/son: {numeros_mas_repetidos}')
print(f'El/Los numero/s que mas se repite/n despues del anterios/res es/son: {numeros_segundos}')

print(dicc_numeros)


