# Modificar el ejercicio anterior, para que el usuario pueda en cada opción del 
# programa, ingresar dos números enteros y que en cada opción a esos 
# números se les aplique una suma, una resta, una división o una 
# multiplicación.
# Agregar una nueva opción para que el programa funcione permanentemente 
# hasta que el usuario la seleccione y el programa finalice su ejecución.

while True:
    print("""
Opciones:
1. Suma 
2. Resta
3. Multiplicacion
4. Division
5. Salir
            """)
    
    opcion = int(input('Ingrese la opcion deseada: '))
    
    if opcion == 5:
        break
    
    numero_uno = int(input('Ingrese el primer numero: '))
    numero_dos = int(input('Ingrese el segundo numero: '))
    if opcion == 1:
        suma = numero_uno + numero_dos
        print(f'La suma es {suma}')
    elif opcion == 2:
        resta = numero_uno - numero_dos
        print(f'La resta es {resta}')
    elif opcion == 3:
        multiplicacion = numero_uno * numero_dos
        print(f'La multiplicacion es  {multiplicacion}')
    elif opcion == 4:
        if numero_dos != 0:
            division = numero_uno / numero_dos
            print(f'La division es {division}')
        else:
            print('No se puede dividir por cero')
    else:
        print('Eligio una opcion incorrecta')