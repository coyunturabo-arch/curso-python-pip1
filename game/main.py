# Piedra, Papel o Tijera
import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')

    user_option = input('Piedra, papel o tijera => ').lower()

    if user_option not in options:
        print('❌ Esa opción no es válida.')
        return None, None

    computer_option = random.choice(options)

    print('Usuario =>', user_option)
    print('Computadora =>', computer_option)

    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):

    if user_option == computer_option:
        print('🤝 ¡Empate!')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera.')
            print('🎉 ¡Ganó el usuario!')
            user_wins += 1
        else:
            print('Papel gana a piedra.')
            print('💻 ¡Ganó la computadora!')
            computer_wins += 1

    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra.')
            print('🎉 ¡Ganó el usuario!')
            user_wins += 1
        else:
            print('Tijera gana a papel.')
            print('💻 ¡Ganó la computadora!')
            computer_wins += 1

    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel.')
            print('🎉 ¡Ganó el usuario!')
            user_wins += 1
        else:
            print('Piedra gana a tijera.')
            print('💻 ¡Ganó la computadora!')
            computer_wins += 1

    return user_wins, computer_wins


def run_game():

    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:

        print("\n" + "*" * 15)
        print("ROUND", rounds)
        print("*" * 15)

        print("Victorias usuario:", user_wins)
        print("Victorias computadora:", computer_wins)

        rounds += 1

        user_option, computer_option = choose_options()

        # Si la opción es inválida, vuelve a pedir otra
        if user_option is None:
            continue

        user_wins, computer_wins = check_rules(
            user_option,
            computer_option,
            user_wins,
            computer_wins
        )

        if computer_wins == 2:
            print("\n🏆 El ganador es la computadora.")
            break

        if user_wins == 2:
            print("\n🏆 El ganador es el usuario.")
            break


if __name__ == "__main__":
    run_game()