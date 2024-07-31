#vamos a recrear el juego de piedra papel o tijera
# las reglas simples son:
# piedra gana a tijera
# tijera gana a papel
# papel gana a piedra
# jugaremos contra el computador 
# el usuario debera ingresar su opcion
# el computador generara una opcion aleatoria
# se compararan las opciones y se determinara un ganador
# el jugador puede cambiar entre las opciones de piedra, papel o tijera y ser avisado si la opcion es invalida
# en cada ronda el jugador debe introducir una opcion de la lista y se informa si gano, perdio o empato
# al final de cada ronda el jugador puede elegir si desea seguir jugando o salir del juego
# muestra la puntuacion del jugador al final de la partida
# El minijuego debe manejar las entradas del usuario, poniéndolas en minúsculas e informando al usuario si la opción no es válida.

import random

def game():
    options = ['piedra', 'papel', 'tijera']
    user_score = 0
    computer_score = 0
    while True:
        user_input = input('Elige piedra, papel o tijera: ')
        computer_input = random.choice(options)
        if user_input.lower() not in options:
            print('Opción no válida')
            continue
        print(f'El computador eligió {computer_input}')
        if user_input.lower() == computer_input:
            print('Empate')
        elif user_input.lower() == 'piedra' and computer_input == 'tijera':
            print('Ganaste')
            user_score += 1
        elif user_input.lower() == 'tijera' and computer_input == 'papel':
            print('Ganaste')
            user_score += 1
        elif user_input.lower() == 'papel' and computer_input == 'piedra':
            print('Ganaste')
            user_score += 1
        else:
            print('Perdiste')
            computer_score += 1
        print(f'Puntuación: Jugador {user_score} - {computer_score} Computador')
        play_again = input('¿Quieres jugar de nuevo? (s/n): ')
        if play_again.lower() != 's':
            break
    print(f'Puntuación final: Jugador {user_score} - {computer_score} Computador')

game()

#Ejecutar el juego
#python app.py