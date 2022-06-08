# Escribir una función para determinar si un número entero, ingresado por 
# teclado es un número primo.
# Un número primo es aquel que solo tiene como divisores enteros (resto igual 
# a cero) al número 1 y a sí mismo, por ejemplo, el número 5.

numero_ingresado = int(input('Ingrese un numero entero: '))
bandera_primo = True

for x in range(9):
    if x != 1 and x != 0:
        if numero_ingresado % x == 0 and numero_ingresado != x:
            
            bandera_primo = False
            break

if bandera_primo == False:
    print('El numero ingresado no es un numero primo')
else:
    print('El numero ingresado es un numero primo')