def linear_search(list, target):
    """Returns The Index position of the target if found else returns None

    Args:
        list (array): 
        A one-dimensional array or list.
        target (Number or String): 
        The element to be searched in the list.
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None