# Dada una lista de números, se pide iterar los elementos de la lista y almacenar en otra lista el resultado de sumar ese elemento con el anterior.
# Por ejemplo, dada la lista: `[1, 2, 3, 4]`, se espera que la salida sea una lista con los elementos `[3, 5, 7]`

def suma_continua(lista_numeros):
    lista_suma_continua = []
    for indice, valor in enumerate(lista_numeros):
        if indice + 1 < len(lista_numeros):
            suma = valor + lista_numeros[indice + 1]
            lista_suma_continua.append(suma)
    
    return lista_suma_continua