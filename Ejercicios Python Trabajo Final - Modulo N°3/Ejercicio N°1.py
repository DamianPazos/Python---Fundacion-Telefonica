# Escribir una clase llamada “Alumno” que contenga los siguientes atributos:
# Nombre
# Apellido
# Notas (este atributo debe ser una lista)
# Escribir el método constructor para que, al instanciar la clase, pida por 
# teclado el Nombre, el Apellido y una serie de notas, tantas como quiera 
# ingresar el usuario.
# Las notas deberán estar comprendidas entre 1 y 10, caso contrario mostrar 
# mensaje de error y volver a solicitar.
# El ingreso de notas acaba cuando el usuario ingresa el valor 0 (cero)
# Sobre escribir el método STR para que, al mostrar el objeto por pantalla, 
# muestre los datos de la siguiente manera:
# Nombre: (valor ingresado)
# Apellido: (valor ingresado)
# Promedio: (promedio de las notas ingresadas)
# Estado: Si el promedio es mayor o igual a 7, mostrar la palabra 
# “Promociona”, si es menor a 7 pero mayor o igual a 4, mostrar la palabra 
# “Final” y por último, si el promedio es menor a 4, mostrar la palabra 
# “Recursa”

class Alumno:
    
    notas = []
    promedio = 0
    
    # Constructor
    def __init__(self):
        self.nombre = input('Ingrese el nombre del alumno: ')
        self.apellido = input('Ingrese el apellido del alumno: ')
        
        while True:
            nota = int (input('Ingrese una nota del 1 al 10: '))
            if nota >=1 and nota <= 10:
                self.notas.append(nota)
            elif nota == 0:
                break
            else:
                print('Ingreso un valor incorrecto')

        for i in self.notas:
            self.promedio += i
        
        self.promedio = self.promedio / len(self.notas)
        
        if self.promedio >= 7:
            self.estado = 'Promociona'
        elif self.promedio > 7 and self.promedio >= 4:
            self.estado = 'Final'
        else:
            self.estado = 'Recursa'
    
    # Metodo magico __str__
    def __str__(self):
        
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nPromedio: {self.promedio}\nEstado: {self.estado}'