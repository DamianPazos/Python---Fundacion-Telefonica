# Crear una función que reciba una cantidad variable de números enteros y 
# retorne la suma de todos.
# Por ejemplo, si le pasamos los números 1,3 y 5, deberá devolver el número 
# 9.
# El código debe funcionar para cualquier cantidad de números que le 
# pasemos como argumentos.

def suma_numeros():
    cantidad_numeros = int(input('Ingrese la cantidad de numeros que va ingresar: '))
    contador = 0
    suma = 0
    while contador < cantidad_numeros:
        numero = int(input('Ingrese un numero: '))
        suma += numero
        contador += 1
    return suma
        
print(suma_numeros())        