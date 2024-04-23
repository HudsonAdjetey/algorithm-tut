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


def verify(index):
    if index is not None:
        print("Target  Found at Position : ", str(index))
    else:
        print("Target not found in list")

list_container = [3, 5,6,7,90, 23]
target = 7

linear_fn = linear_search(list_container, target)
verify(linear_fn)