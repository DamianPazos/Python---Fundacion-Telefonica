# Modificar el siguiente código para que no de error al recibir un argumento 
# que no es del tipo Lista.

# def lista (argumento):
#     print(argumento)
#     print(len(argumento))

def lista(argumento):
    if type(argumento) != list:
        print('Argumento erroneo, no ingreso una lista')
    else:
        print(argumento)
        print(len(argumento))
