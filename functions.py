def add_next_number(lst):
    """
       Function to add the next element's value to each element in the list.

       This function iterates through the list and adds the value of the next element
       to each element. If it is the last element of the list, nothing is added and
       the function terminates.
   """

    lst = [lst[i] + lst[i + 1] if i < len(lst) - 1 else lst[i] for i in range(len(lst))]
    return lst


def get_even_numbers(lst):
    # Returns a list containing the even numbers from the input list or empty list, when it's empty.

    lst = [x for x in lst if x % 2 == 0]
    return lst


def average_of_positive_odd_integers(lst):
    # Returns an average of positive elements of the list and None, when its 0 or empty

    try:
        lst = [i for i in lst if i % 2 != 0 and i > 0]
        return sum(lst) / len(lst)
    except ZeroDivisionError:
        return None
