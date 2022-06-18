# Pedir al usuario que ingrese por teclado dos números reales y utilizarlos 
# para realizar todas las operaciones aritméticas vistas (suma, resta, 
# multiplicación, división, potencia, división entera y resto).
# Mostar todos los resultados por pantalla (un resultado por línea) con su 
# respectiva leyenda aclarando de que operación se trata.

import math

numero_uno = float(input('Ingrese el primer numero: '))
numero_dos = float(input('Ingrese el segundo numero: '))

suma = numero_uno + numero_dos
print(f'La suma es: {suma}')

resta = numero_uno - numero_dos
print(f'La resta es: {resta}')

multiplicación = numero_uno * numero_dos
print(f'La multiplicacion es: {multiplicación}')

if numero_dos != 0:
    division = numero_uno / numero_dos
    print(f'La division es: {division}')
else:
    print('No se puede realizar la division')

potencia = math.pow(numero_uno,numero_dos)
print(f'La potencia es: {potencia}')

if numero_dos != 0:
    division_entera = int(numero_uno // numero_dos)
    print(f'La division es: {division_entera}')
else:
    print('No se puede realizar la division')

if numero_dos != 0:
    division_resto = numero_uno % numero_dos
    print(f'La division es: {division_resto}')
else:
    print('No se puede realizar la division')