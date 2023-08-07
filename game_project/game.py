import random

def game_instructions():
    print('Bienvenido al Juego piedra, papel o tijer!!!...')
    print('Tendras que ganar 3 puntos para vecer a la computadora')
    print('Tienes 3 opciones para jugar: piedra que vence a tijera, tijera que corta papel o papel que envuelve la roca')
    print('Tu elegiras una opcion al igual que la computadora y por cada round uno de los dos sera el ganadora de cada batalla')
    print('Al finalizar las batallas se hara un conteo para descubrir al ganador absoluto')
    return

def user_name():
    user = input('Escribe tu nombre =>')
    user = user.capitalize()
    return user

def choose_options():
    options = ('Piedra', 'Papel', 'Tijera')
    user_option = input('Piedra, Papel o Tijera => ')
    user_option = user_option.capitalize()

    if not user_option in options:
        print('La opcion introducida no es correcta, intentalo de nuevo')
        return None, None

    computer_option = random.choice(options)

    print('Opcion del Usuario =>', user_option)
    print('Opcion de la computadora =>', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins, user):
  
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'Piedra':
        if computer_option == 'Tijera':
            print('La piedra rompe la Tijera')
            print(user, ' gana esta ronda!')
            user_wins += 1
        else:
            print('El papel envuelve a la piedra')
            print('La computadora gana esta ronda!')
            computer_wins += 1
    elif user_option == 'Papel':
        if computer_option == 'Piedra':
            print('El papel envuelve la piedra')
            print(user, 'gana esta ronda')
            user_wins += 1
        else:
            print('La tijera corta a papel')
            print('La compuradora gana esta ronda!')
            computer_wins += 1
    elif user_option == 'Tijera':
        if computer_option == 'Papel':
            print('La tijera corta el papel')
            print(user, 'gana esta ronda!')
            user_wins += 1
        else:
            print('la piedra destruye la tijera')
            print('La computadora gana esta ronda!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
  
    game_instructions()  
    user = user_name()
    computer_wins = 0
    user_wins = 0  
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print(user, user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins, user)

        if computer_wins == 3:
            print('La computadora es el ganador definitivo!!!')
            break

        if user_wins == 3:
            print(user, 'es el ganador definitivo!!!')
            break

run_game()