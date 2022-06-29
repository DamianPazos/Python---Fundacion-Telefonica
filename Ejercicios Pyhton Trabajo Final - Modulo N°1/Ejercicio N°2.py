# Escribir una función que, a partir de una lista pasada como argumento, 
# retorne una lista de tuplas conteniendo todas las combinaciones de 2 
# números que sea posible formar, combinando a cada número con todos los 
# números de la lista

def conjunto_tuplas(lista):
    lista_tuplas = []
    for i in lista:
        for x in lista:
            tupla = (i,x)
            lista_tuplas.append(tupla)
    return lista_tuplas

