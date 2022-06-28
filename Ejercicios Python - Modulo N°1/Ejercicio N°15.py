# Escribir un programa que le pregunte al usuario cuantas palabras desea 
# ingresar, luego le permita ingresarlas todas y finalmente mostrarlas por 
# pantalla.

cantidad_palabras = int(input("Cuantas palabras desea ingresar: "))
list_palabras = []
contador = 0

for x in range(cantidad_palabras):
    palabra = input("Ingrese la palabra: ")
    list_palabras.append(palabra)

for i in list_palabras:
    contador += 1
    print(f'{contador}. {i}')
    
