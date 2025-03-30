import random


def random_option():
    comp_variable = random.choice(['kamień', 'papier', 'nożyce'])
    return comp_variable


def user_option():
    user_variable = input('Wybierz swoją opcję : ').strip().lower()
    while user_variable not in ['kamień', 'papier', 'nożyce']:
        print('Wpisz poprawną opcję')
        user_variable = input('Wybierz swoją opcję : ').strip().lower()
    return user_variable


def kpn():
    comp_variable = random_option()

    menu = '''

    1- kamień
    2 - papier
    3 - nożyce


    ''' 

    print(menu)
    user_variable = user_option()

    print(f'Ty : {user_variable}, Komputer : {comp_variable}')
    if user_variable == comp_variable:
        print('Remis')
    else:
        print('Coś innego')



kpn()
