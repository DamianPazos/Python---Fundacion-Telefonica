# Escribir un programa que pida al usuario, que ingrese una frase por teclado.
# El programa deberá tener dos funciones, una que reciba la frase y devuelva 
# solo las vocales de dicha frase y otra función que reciba la misma frase pero 
# que devuelva solo las consonantes.
# Mostrar por pantalla la frase original ingresada por el usuario, las vocales y 
# las consonantes devueltas por sus respectivas funciones.

frase_ingresada = input('Ingrese una frase: ')

def devolucion_vocales(frase):
    frase_modificada = frase
    for letra in frase:
        if letra == 'a' or letra == 'e' or letra == 'i' or  letra == 'o' or letra == 'u':
            frase_modificada = frase_modificada.replace(letra,'')
    return frase_modificada

def devolucion_consonantes(frase):
    frase_modificada = frase
    for letra in frase:
        if letra != 'a' and letra != 'e' and letra != 'i' and  letra != 'o' and letra != 'u':
            frase_modificada = frase_modificada.replace(letra,'')
    return frase_modificada

print(frase_ingresada)
print(devolucion_vocales(frase_ingresada))
print(devolucion_consonantes(frase_ingresada))