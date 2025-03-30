dict_1 = [
    {
        'vaquero1': 'colt45',
        'vaquero2': 'knife',
        'vaquero3': 'remington'
    },
    {
        'bandit1': 'knife',
        'bandit2': 'dynamite',
        'bandit3': 'remington'
    },
    {
        'renegade': 'volcanic'
    },
    {
        'sherif': 'chesterfield'
    }
]

def get_sherif_weapons(diction):
    weapons = []
    for i in diction:
        for key in i.items():
            if key[0] == 'sherif':
                weapons.append(key[1])
    return weapons

print(get_sherif_weapons(dict_1))

