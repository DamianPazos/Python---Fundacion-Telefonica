# Crear una función que reciba una cantidad variable de números enteros y 
# retorne la suma de todos.
# Por ejemplo, si le pasamos los números 1,3 y 5, deberá devolver el número 
# 9.
# El código debe funcionar para cualquier cantidad de números que le 
# pasemos como argumentos.

def suma_numeros(*args):
    suma = 0
    for i in args:
        suma += i
    return suma
        
print(suma_numeros(1,5,3,5,1))        