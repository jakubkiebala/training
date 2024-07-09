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


def process_numbers_1(lst):
    """
        Processes a list of integers according to specified rules.

        The function returns a new list where:
        - Positive even numbers are replaced by their square.
        - Positive odd numbers are replaced by their cube.
        - Negative numbers are removed.
        - Zero remains unchanged.

        Parameters:
        lst (list of int): The list of integers to process.

        Returns:
        list of int: A new list of integers after processing.

        Example:
        >>> process_numbers_1([1, 2, -3, 0, 4, -5, 3])
        [1, 4, 0, 16, 27]

        Note:
        - Positive even numbers are squared.
        - Positive odd numbers are cubed.
        - Negative numbers are removed from the list.
        - Zero remains unchanged.
        """

    lst = [x for x in lst if type(x) is int]
    if lst:
        lst = [x ** 2 if x > 0 and x % 2 == 0 else
               x ** 3 if x > 0 and x % 2 != 0 else
               x for x in lst if x >= 0]
        return lst
    else:
        print('List must contains integers')
    return None
