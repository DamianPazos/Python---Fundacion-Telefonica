# Desarrollar un programa que solicite al usuario los lados de un rectángulo 
# y calcule su perímetro y su superficie.
# Informar ambos resultados por pantalla

lado_uno = float(input('Ingrese el valor de uno de los lados: '))
lado_dos = float(input('Ingrese el valor del lado adyacente: '))

perimetro = lado_uno*2 + lado_dos*2
superficie = lado_uno * lado_dos

print(f'El perimetro es de {perimetro} cm y la superficie es de {superficie} cm2')