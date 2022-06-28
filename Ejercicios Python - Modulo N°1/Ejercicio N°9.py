# Escribir un programa que permita al usuario ingresar por teclado tantos 
# números enteros como desee. Cuando no quiera ingresar más números, 
# deberá ingresar el cero.
# A continuación, determinar cuál de los números ingresados es el mayor y 
# cuál es el menor. Mostrar ambos por pantalla.

numero_mayor = None
numero_menor = None

while True:
    numero_ingresado = int(input('Ingrese un numero (Si desea dejar de ingresar numeros debe ingresar un cero (0): '))
    if numero_mayor == None and numero_menor == None:
        numero_mayor = numero_ingresado
        numero_menor = numero_ingresado
    if numero_ingresado == 0:
        break
    else:
        if numero_mayor < numero_ingresado:
            numero_mayor = numero_ingresado
        if numero_menor > numero_ingresado:
            numero_menor = numero_ingresado

print(f'El numero mayor es {numero_mayor} y el menor es {numero_menor}')
