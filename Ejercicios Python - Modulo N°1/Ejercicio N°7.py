# Escribir un programa que pida ingresar un número entero mayor que cero 
# por teclado.
# Verificar si el número ingresado es múltiplo de 2, 3, 4, 5, 6, 7,8 o 9.
# Armar una lista con los números encontrados (por ejemplo, si el número 
# ingresado es múltiplo de 3,6 y 7, armamos una lista que contenga estos tres 
# números).
# Mostrar la lista por pantalla, ordenada de mayor a menor.
# En caso de que el número ingresado no sea múltiplo de estos números, 
# mostrar por pantalla el mensaje “No se encontraron divisores exactos”.

numero_ingresado = int(input('Ingrese un numero entero mayor a 0: '))

list_multiplo =[]

if numero_ingresado%2 == 0:
    list_multiplo.append(2)

if numero_ingresado%3 == 0:
    list_multiplo.append(3)

if numero_ingresado%4 == 0:
    list_multiplo.append(4)

if numero_ingresado%5 == 0:
    list_multiplo.append(5)

if numero_ingresado%6 == 0:
    list_multiplo.append(6)

if numero_ingresado%7 == 0:
    list_multiplo.append(7)

if numero_ingresado%8 == 0:
    list_multiplo.append(8)

if numero_ingresado%9 == 0:
    list_multiplo.append(9)

if list_multiplo != []:
    print(f'El numero ingresado es multiplo de {list_multiplo}')
else:
    print('No se encontraron divisores exactos')