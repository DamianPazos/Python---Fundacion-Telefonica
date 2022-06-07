# Pedirle al usuario que ingrese dos números enteros por teclado y contar 
# cuantos números pares hay entre ambos valores ingresados.

numero_uno = int(input('Ingrese un numero entero: '))

numero_dos = int(input('Ingrese otro numero entero: '))

contador = 0

if numero_uno < numero_dos:
    for i in range(numero_uno , numero_dos):
        if i%2 == 0:
            contador += 1
else:
    for i in range(numero_dos , numero_uno):
        if i%2 == 0:
            contador += 1
            
print(f'Hay {contador} numeros pares')
