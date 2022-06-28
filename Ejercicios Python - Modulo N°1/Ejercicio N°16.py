# Escribir un programa que le solicite al usuario ingresar 10 palabras, luego 
# le pida ingresar una más y le diga si esa última palabra ingresada se 
# encuentra entre las 10 palabras ingresadas anteriormente.

def busqueda (lista,busqueda):
    bandera = False
    for x in lista:
        if busqueda == x:
            bandera = True
            break
    
    return bandera

print('Ingrese 10 palabras')
list_palabras = []

for x in range(10):
    palabra = input('Ingrese una palabra: ')
    list_palabras.append(palabra)

palabra_busqueda = input('Ingrese una palabra para saber si coincide con alguna ingresada anteriormente: ')

coinidencia = busqueda(list_palabras,palabra_busqueda)

if coinidencia == True:
    print('La palabra coincide con una ya ingresada')
else:
    print('No se encontro ninguna coincidencia')
    
