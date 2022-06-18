# Pedir el ingreso por teclado de 3 valores numéricos entre 1 y 10 
# correspondientes a las notas de un alumno.
# En base al promedio final de las tres notas, mostrar un mensaje por pantalla 
# que indique si el alumno promociona la materia (nota final 7,8,9 o 10), debe 
# rendir final (nota final 4,5 o 6) o recursa (nota 1,2,3).

#Varialbes
nota_uno = int(input('Ingrese una nota entre 1 y 10: '))
nota_dos = int(input('Ingrese una nota entre 1 y 10: '))
nota_tres = int(input('Ingrese una nota entre 1 y 10: '))

promedio = (nota_uno + nota_dos + nota_tres)/3

# Verificacion del promedio
if promedio >= 7 :
    print("Promociona la materia")
elif 7 > promedio >= 4 :
    print("Debe rendir final")
else:
    print("Recursa")

