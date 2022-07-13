# Generar una lista, usando FOR con números del 1 al 100.
# Escribir una función lambda, usando REDUCE que me permita calcular el
# promedio de todos los números contenidos en la lista.
# No usar funciones tradicionales

from functools import reduce

lista_numeros = []

for i in range(100):
    lista_numeros.append(i + 1)

promedio = float(reduce(lambda x,y: x + y,lista_numeros)/len(lista_numeros))