# Dado un string, mostrar por pantalla unicamente las vocales en formato Mayuscula
# Por ejemplo, el string `"Este es un string de prueba"` obtendra como output `['E', 'E', 'E', 'U', 'I', 'E', 'U', 'E', 'A']`

cadena = input('Ingrese una palabra o una frase: ')
cadena_vocales = []
vocales = ('a','A','e','E','i','I','o','O','u','U')

for letra in cadena:    
    if letra in vocales:
        letra_mayus = letra.upper()
        cadena_vocales.append(letra_mayus)

print(f'Las vocales son: {cadena_vocales}')