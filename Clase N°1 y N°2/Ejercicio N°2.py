# Solicitar por teclado la cantidad de partidos ganados, empatados y perdidos 
# de un determinado club de fútbol. Calcular y mostrar el puntaje final 
# sabiendo que cada partido ganado le otorga 3 puntos, cada partido 
# empatado 1 punto y ningún punto por cada partido perdido.

name_club = input('Ingrese el nombre del equipo: ')
game_win = int(input('Ingrese la cantidad de partidos ganados: '))
game_draw = int(input('Ingrese la cantidad de partidos empatados: '))
game_lose = int(input('Ingrese la cantidad de partidos perdidos: '))

points = game_win*3 + game_draw*1

print(f'Los puntos obtenidos por {name_club} son: {points}')