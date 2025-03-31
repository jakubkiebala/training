from random import choice


def computer_random_choice_func():
    computer_choice = choice(['rock', 'paper', 'scissors'])
    return computer_choice


def player_choice_func():
    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input('write your choice : ').lower()
        if player_choice in choices:
            return player_choice
        else:
            print('write correct choice')



def game_logic():
    computer_choice = computer_random_choice_func()
    player_choice = player_choice_func()
    print(f'Your choice : {player_choice} | Computer choice : {computer_choice}')

    if player_choice == computer_choice:
        print('Draw')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('You won')
    elif player_choice == 'scissors' and computer_choice == 'paper':        
        print('You won')
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('You won')
    else:
        print('You loose')



game_logic()
