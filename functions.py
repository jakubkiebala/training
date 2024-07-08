def add_next_number(lst):
    """
       Function to add the next element's value to each element in the list.

       This function iterates through the list and adds the value of the next element
       to each element. If it is the last element of the list, nothing is added and
       the function terminates.

       Parameters:
       lst (list): List of integers.

       Returns:
       list: List with values added from the next elements.

       Example:
       lst = [1, 3, 5, 6, 8]
       add_next_number(lst)
       [4, 8, 11, 14, 8]
       """
    lst = [lst[i] + lst[i + 1] if i < len(lst) - 1 else lst[i] for i in range(len(lst))]
    return lst
