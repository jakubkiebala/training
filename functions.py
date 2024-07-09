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


def transform_words_1(lst):
    """
        Transforms a list of strings according to specified rules.

        The function checks if the input list contains only strings. If so, it returns a new list where:
        - Words longer than 5 characters are replaced by their length.
        - Words with exactly 5 characters are replaced by the string "five".
        - Words shorter than 5 characters are transformed to uppercase.
        - Empty strings are omitted.

        If the input list contains non-string elements, it returns a string indicating that the list must contain strings only.

        Parameters:
        lst (list): The list to process, expected to contain only strings.

        Returns:
        list or str: A new list of transformed strings or an error message if non-string elements are found.

        Example:
        >>> transform_words_1(["apple", "banana", "cat", "", "dog", "elephant"])
        ['five', 'banana', 'CAT', 'DOG', 8]

        >>> transform_words_1([1, 2, "cat", "elephant"])
        'List must contain strings only'

        Note:
        - Words longer than 5 characters are replaced by their length.
        - Words with exactly 5 characters are replaced by the string "five".
        - Words shorter than 5 characters are transformed to uppercase.
        - Empty strings are omitted.
        """
    is_only_str = all(isinstance(x, str) for x in lst)
    if is_only_str:
        lst = [f'{len(x)}' if len(x) > 5 else
               'five' if len(x) == 5 else
               x.upper() for x in lst if x != '']
        return lst
    else:
        return 'List must contains strings only'
