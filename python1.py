def safe_get(lst, index):
    try:
        return lst[index]
    except TypeError:
        print('Thats not a number')
    except IndexError:
        print('Bad index')
    return None
