# Crear una lista con 10 números enteros y mostrarlos por pantalla.
# Luego reemplazar todos los números pares por la palabra PAR y volver a 
# mostrar la lista por pantalla.

list_numeros= []

for x in range(10):
    numero = int(input("Ingrese un numero: "))
    list_numeros.append(numero)
    
for x in list_numeros:
    if x % 2 == 0:
        indice = list_numeros.index(x)
        list_numeros[indice] = 'Par'

print(list_numeros)

