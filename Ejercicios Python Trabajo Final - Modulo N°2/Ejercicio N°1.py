# 1.1) Generar una lista que contenga los números del 1 al 100, usando un
# FOR.
# 1.2) Escribir una función lambda, usando FILTER, que me devuelva, en
# formato LISTA, todos los números pares que también sean múltiplos de 5,
# contenidos en dicha lista.

lista_numeros = []

for i in range(100):
    lista_numeros.append(i + 1)

lista_filtrada = list(filter(lambda x: x % 2 == 0 and x % 5 == 0, lista_numeros))