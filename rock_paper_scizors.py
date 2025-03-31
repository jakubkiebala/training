from random import choice


def computer_random_choice_func():
    computer_choice = choice(['rock', 'paper', 'scizors'])
    return computer_choice


def player_choice_func():
    choices = ['rock', 'paper', 'scizors']
    while True:
        player_choice = input('write your choice : ').lower()
        if player_choice in choices:
            print(player_choice)
            return player_choice
        else:
            print('write correct choice')


player_choice_func()
