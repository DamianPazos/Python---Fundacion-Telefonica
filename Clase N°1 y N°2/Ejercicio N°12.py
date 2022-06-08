# Escribir una función para determinar si un número entero, ingresado por 
# teclado es un número primo.
# Un número primo es aquel que solo tiene como divisores enteros (resto igual 
# a cero) al número 1 y a sí mismo, por ejemplo, el número 5.

def numero_primo(numero):
    bandera_primo = True

    for x in range(9):
        if x != 1 and x != 0:
            if numero % x == 0 and numero != x:

                bandera_primo = False
                break

    if bandera_primo == False:
        return 'El numero ingresado no es un numero primo'
    else:
        return 'El numero ingresado es un numero primo'
    
numero_ingresado = int(input('Ingrese un numero entero: '))
print(numero_primo(numero_ingresado))