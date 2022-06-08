# Escribir una función en Python para calcular el factorial de un número 
# entero positivo.
# Basarse en la siguiente definición:
# El factorial de un número entero positivo n, se define como el producto de 
# todos los números enteros positivos menores o iguales a n.
# El factorial de cero es 1.
# Por ejemplo, el factorial de 4 será 4x3x2x1 = 24.
# No utilizar ninguna función ni módulo matemático, solo lo visto en clase.

numero_ingresado = int(input('Ingrese el numero para calcular su factorial: '))

factorial = numero_ingresado

for x in range(numero_ingresado):
    if x != 0:
        factorial = factorial * x
        
print(f'El factorial de {numero_ingresado} es {factorial}')

