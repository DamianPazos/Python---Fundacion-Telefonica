# Crea una función llamada modificar() que a partir de una lista de números 
# realice las siguientes tareas sin modificar la original:
# - Borrar los elementos duplicados.
# - Ordenar la lista de mayor a menor.
# - Eliminar todos los números impares.
# - Realizar una suma de todos los números que quedan.
# - Añadir como primer elemento de la lista la suma realizada.
# - Devolver la lista modificada.
# Una vez escrita la función, utilizarla y verificar que el primer elemento de 
# dicha lista, coincide con la suma de los demás elementos.

def modificar(lista):
    copia_lista = []
    sumatoria = 0
    for x in lista:
        bandera = True
        for i in copia_lista:
            if x == i:
                bandera = False
        
        if bandera == True and x % 2 == 0:
            copia_lista.append(x)
            
    copia_lista.sort(reverse=True)
    
    for j in copia_lista:
        sumatoria += j
    
    copia_lista.insert(0,sumatoria)
    
    return copia_lista

