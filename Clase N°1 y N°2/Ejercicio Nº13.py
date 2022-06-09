# Escribir una función que encuentre los números primos comprendidos entre 
# dos números enteros ingresados por teclado.

def numeros_primos (numero_uno,numero_dos):
    
    list_numeros_primos = []
    
    for i in range(numero_uno,numero_dos):
        bandera_primo = True
        for x in range(2,10):
            if i % x == 0 and i != x:
                bandera_primo = False
                break
        
        if bandera_primo == True:
            list_numeros_primos.append(i)
            
    return list_numeros_primos