# Solicitar por teclado el ingreso de un número entero.
# Asignar dicho número a una variable, transformarla a coma flotante y 
# mostrarla por pantalla (valor y tipo de variable).

numero = int(input('Ingrese un numero:'))

numero = float(numero)

print(f'{numero} tipo {type(numero)}')