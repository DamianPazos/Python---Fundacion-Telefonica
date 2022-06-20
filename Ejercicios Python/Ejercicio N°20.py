# Escribir un programa que le pida al usuario que ingrese un número por 
# teclado, lo eleve al cubo y muestre el resultado por pantalla. El programa 
# deberá seguir funcionando hasta que el usuario ingrese el número cero.

import math

while True:
    numero_ingresa = int(input('Ingrese un numero: '))
    if numero_ingresa != 0:
        resultado = math.pow(numero_ingresa,2)
        print(f'El numero elevado al cuadrado es {resultado}')
    else:
        break
