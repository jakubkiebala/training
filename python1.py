def find_boundries(lst):
    max_value = [None, None]
    for l in lst:
        if isinstance(l, (int, float)):
            if max_value[0] == None or l < max_value[0]:
                max_value[0] = l
            elif max_value[1] == None or l > max_value[1]:
                max_value[1] = l
    return tuple(max_value)

lst = [1, 4, 2, 10, 5, 'Jk', 55, 12, 0, 'Auu' ,100, 10, 13, 'AUU', -12]
new_lst = find_boundries(lst)
print(new_lst)