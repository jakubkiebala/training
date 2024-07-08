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

    lst = [lst[i] for i in range(len(lst)) if lst[i] % 2 == 0]
    return lst
