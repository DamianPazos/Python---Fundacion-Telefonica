# Dados 2 números enteros, imprimir por pantalla el producto.
# Si el producto de ambos numeros es mayor a 100, mostrar además la suma de los numeros.

numero_uno = int(input('Ingrese un numero entero: '))
numero_dos = int(input('Ingrese otro numero entero: '))

multiplicacion = numero_uno * numero_dos

print(f'La multiplicación es {multiplicacion}')

if multiplicacion >= 100:
    print(f'La suma de los numeros es {numero_uno + numero_dos}')