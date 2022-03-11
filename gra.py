import random


def valid_input(user_info, choos):
    player_input = input(user_info)
    if player_input != "x":
        if player_input not in choos:
            print("Input should be: 'paper', 'scissors', 'rock' (or 'x' to exit).")
            return None
        else:
            user_value = player_input
    else:
        user_value = player_input
    return user_value


def compare_choices(p):
    cpu_choice = random.choice((list(choices.keys())))
    cpu = choices.get(cpu_choice)
    check_win = cpu - p
    return cpu_choice, check_win


def show_who_win(winner):
    if winner in [-1, 2]:
        print("CPU win!")
    elif winner in [-2, 1]:
        print("Human win.")
    else:
        print("Draw!")


def main():
    initial_value = None
    while initial_value is None:
        initial_value = valid_input("Entry paper, scissors or rock (x to exit):", choices)
        if initial_value == "x":
            break

        try:
            player_choice = choices[initial_value]
        except KeyError:
            continue

        cpu, check_winner = compare_choices(player_choice)
        print(f"CPU get: {cpu}.")
        print(f"Human get: {initial_value}.")
        show_who_win(check_winner)

        if input("Would you like to play again?(yes/any for exit):") == "yes":
            initial_value = None
        else:
            break


if __name__ == "__main__":
    choices = {"rock": 1, "scissors": 2, "paper": 3}
    main()