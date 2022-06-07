# Si creamos tres listas. La primera contiene 4 números, la segunda contiene 
# 5 letras y en la tercera le cargamos como elementos las dos listas anteriores.
# ¿Cuántos elementos contendrá la tercera lista? Demostrar mediante un 
# breve código.

lista_uno = [0,1,2,3]
lista_dos = ["a","b","c","d","e"]
lista_tres = lista_uno + lista_dos

print(len(lista_tres))