import re


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
    """
        Returns a list containing the even numbers from the input list or empty list, when it's empty.
    """

    lst = [x for x in lst if x % 2 == 0]
    return lst


def average_of_positive_odd_integers(lst):
    """
        Returns an average of positive elements of the list and None, when its 0 or empty
    """

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

        If the input list contains non-string elements, it returns a string indicating that the list must contain
        strings only.

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


def numbers_and_quarters(lst):
    """
    Returns a dictionary where the keys are numbers from the input list and the values are the squares of those numbers.

    Parameters:
    lst (list of int or float): A list of numbers.

    Returns:
    dict: A dictionary where each key is a number from the input list and the corresponding value is the square of that number.

    Example:
    >>> numbers_and_squares([1, 2, 3, 4, 5])
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    >>> numbers_and_squares([0, -1, 0.5])
    {0: 0, -1: 1, 0.5: 0.25}
    """
    return {x: x ** 2 for x in lst}


def dict_comprehensions_1(lst):
    """
    Returns a dictionary where the keys are words from the input list that start with an uppercase letter
    and consist only of alphabetic characters, and the values are the lengths of those words.

    Parameters:
    lst (list of str): A list of strings.

    Returns:
    dict: A dictionary where each key is a word from the input list that meets the criteria,
          and the corresponding value is the length of that word.

    Example:
    >>> dict_comprehensions_1(["Hello", "world", "Python3", "Code", "123", "Test"])
    {'Hello': 5, 'Code': 4, 'Test': 4}

    >>> dict_comprehensions_1(["apple", "Banana", "1234", "Cherry", "DOG"])
    {'Banana': 6, 'Cherry': 6, 'DOG': 3}
    """

    return {x: len(x) for x in lst if x[0].isupper() and x.isalpha()}


def regex_1(words):
    """
    Finds words starting with an uppercase letter followed by one or more lowercase letters in the input string.

    Parameters:
    words (str): Input string to search for words.

    Returns:
    list: List of words matching the pattern '[A-Z][a-z]+'.

    Example:
    >>> regex_1("Hello World, Python is great!")
    ['Hello', 'World', 'Python']

    >>> regex_1("This is a Test123. Not ThisOne.")
    ['This', 'Not']
    """

    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, words)


def find_numbers_1(text):
    """
    Take a string text and returns a list of numbers contained in this text
    """

    pattern = r'\d+'
    return re.findall(pattern, text)


def regex_2(text):
    """
        Finds all occurrences of the word 'Ala' or 'ala' followed by zero or more lowercase letters in the given text.
    """

    return re.findall(r'[A,a]la[a-z]*', text)


def find_dates(text):
    """
        Finds all dates in the text and returns them as a list
    """

    return re.findall(r'\b[0-3]\d/[0,1]\d/\d{4}\b', text)


def validate_polish_phone_numbers(p_numbers):
    """
    Validate Polish phone numbers based on a specific pattern.

    Parameters:
    p_numbers (list): A list of phone numbers to validate.

    Returns:
    list: A list containing valid phone numbers based on the pattern.

    The function validates phone numbers in Polish format, which may include:
    - Optional prefix '+48 '
    - Three digits followed by an optional separator ('-', ',' or ' ')
    - Another three digits followed by the same optional separator
    - Final three digits

    Examples of valid numbers: '+48 123-456-789', '123 456 789', '456-789-225, +48 123 123 123'

    Invalid numbers will not be included in the returned list.

    """

    pattern = r'\b(\+48 )?\d{3}([-, ]?)(\d{3})\2\d{3}\b'
    numbers = [number for number in p_numbers if re.search(pattern, number)]
    return numbers


def validate_emails(emails):
    """
    Validates a list of email addresses according to specified regex pattern.

    The function returns a new list containing only valid email addresses.

    Parameters:
    emails (list of str): The list of email addresses to validate.

    Returns:
    list of str: A new list containing only valid email addresses.

    Example:
    >>> validate_emails(["test@example.com", "invalid-email", "user.name@domain.co", "user@domain", "user@domain.c"])
    ['test@example.com', 'user.name@domain.co']

    Note:
    - The regex pattern used for validation checks for a basic email format.
    """

    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    emails = [email for email in emails if re.match(pattern, email)]
    return emails


def validate_postal_codes(codes):
    """
    Validates a list of Polish postal codes according to specified regex pattern.

    The function returns a new list containing only valid postal codes in Poland.

    Parameters:
    codes (list of str): The list of postal codes to validate.

    Returns:
    list of str: A new list containing only valid Polish postal codes.

    Example:
    >>> validate_postal_codes(["00-000", "12345", "12-345", "12-34a", "12-3456", "12-34"])
    ['00-000', '12-345']

    Note:
    - The regex pattern used for validation checks for the format xx-xxx.
    """

    codes = [code for code in codes if re.match(r'^[0-9]{2}-[0-9]{3}$', code)]
    return codes


def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$'
    password = re.search(pattern, password)
    return password


def check_quantity_of_words_with_specified_letters(text):
    pattern = r'\b[Nn][a-z]*ar[a-z]*'
    words = re.findall(pattern, text)
    return words
