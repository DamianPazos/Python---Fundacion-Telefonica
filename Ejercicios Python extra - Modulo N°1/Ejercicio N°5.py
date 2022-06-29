# Contar cuántos elementos de la lista cumple alguna de las siguientes condiciones:

# - El elemento es un carácter en minúscula
# - Es un número entero par
# ``` python

lista = ['a', 2, 5, 'B', 9, 'd', 4, 'o', 7, '%', 3.1, '&']
contador_condiciones = 0

for i in lista:
    if i % 2 == 0:
        contador_condiciones += 1
    
print(contador_condiciones)
