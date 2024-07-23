import re
import statistics
from collections import Counter
from datetime import datetime, timedelta


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


def median_to_first_sunday(dct):
    """
    Computes the median of all values in the dictionary up to the first Sunday of each month.

    Parameters:
    dct (dict): A nested dictionary where:
                - The first-level keys are strings in the format 'YYYY-MM', representing year and month.
                - The second-level keys are strings representing days of the month.
                - The third-level keys can be any strings.
                - The third-level values are lists of numbers.

    Returns:
    float: The median of all values up to the first Sunday of each month. If there are no values, returns None.

    Example:
    input_dict = {
        '2024-07': {
            '1': {'key1': [10, 20], 'key2': [30]},
            '2': {'key1': [40]},
            '3': {'key1': [50, 60], 'key2': [70]},
            '4': {'key1': [80]}
        },
        '2024-08': {
            '5': {'key1': [15]},
            '6': {'key2': [25, 35]},
            '7': {'key1': [45]},
            '8': {'key2': [55, 65]}
        }
    }
    median_to_first_sunday(input_dict)
    Output: 40.0
    """

    all_values = []

    for key, second_level in dct.items():
        # Split the key into year and month
        year, month = map(int, key.split('-'))
        first_day_of_month = datetime(year, month, 1)

        # Calculate the first Sunday of the month
        first_sunday = first_day_of_month + timedelta(days=(6 - first_day_of_month.weekday()))

        first_sunday_day = first_sunday.day

        for second_key, third_level in second_level.items():
            # If the second-level key is less than or equal to the first Sunday day
            if int(second_key) <= first_sunday_day:
                # Extend values directly into the list
                for sublist in third_level.values():
                    all_values.extend(sublist)

    # Calculate the median if the list is not empty
    return statistics.median(all_values) if all_values else None


def most_frequent_word_func(text):
    """
    Counts the occurrences of each word in the given text and returns a dictionary with the most frequently occurring word(s).

    The function processes the text as follows:
    1. Removes punctuation and digits.
    2. Converts the text to lowercase.
    3. Splits the text into individual words.
    4. Counts the occurrences of each word.
    5. Identifies the word(s) with the highest count.

    Args:
        text (str): The input text in which words will be counted.

    Returns:
        dict: A dictionary where the keys are the most frequently occurring word(s) and the values are their counts.

    Examples:
        >>> most_frequent_word_func("This is a test. This is only a test.")
        {'this': 2}

        >>> most_frequent_word_func("Python is great. Python is fun!")
        {'python': 2, 'is': 2}
    """
    # Remove punctuation and digits, convert to lowercase, and split into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Find the maximum occurrence count
    max_occurrence = max(word_counts.values())

    # Create a dictionary with the most frequently occurring word(s)
    most_frequent_word = {word: count for word, count in word_counts.items() if count == max_occurrence}

    return most_frequent_word

