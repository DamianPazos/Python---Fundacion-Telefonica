# Hacer un menú de cuatro opciones, que le permita al usuario navegar por 
# cuatro módulos diferentes del programa. Mostrar en cada módulo un título 
# diferente para verificar que funciona correctamente

import datetime

while True:
    print("""
Opciones:
1. Dia 
2. Dia y hora
3. Dia, hora y Año
4. Salir
            """)
    
    opcion = int(input('Ingrese la opcion deseada: '))
    ahora = datetime.datetime.now()
    if opcion == 1:
        print(f"El dia es {ahora.strftime('%x')}")
    elif opcion == 2:
        print(f"El dia es {ahora.strftime('%x')} y la hora es {ahora.strftime('%X')}")
    elif opcion == 3:
        print(f'La fecha de hoy es {ahora}')
    elif opcion == 4:
        break
    else:
        print('Eligio una opcion incorrecta')
        
