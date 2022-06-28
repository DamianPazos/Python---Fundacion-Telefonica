# Dada una lista de numeros, mostrar por genere una lista con todos los múltiplos de 7.
# Por ejemplo, para la lista `[1, 2, 7, 10, 21]`, se muestran por pantalla los numeros `7` y `21`

def multiplos_siete(lista):
    lista_multiplos_siete = []
    for i in lista:
        if i % 7 == 0:
            lista_multiplos_siete.append(i)

    return lista_multiplos_siete