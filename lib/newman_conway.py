def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError
    elif num == 1:
        return str(1)
    
    arr = [0, 1, 1]

    for i in range(3, num + 1):
        val = arr[arr[i-1]] + arr[i-arr[i-1]]
        arr.append(val)
    
    return ' '.join(map(str, arr[1:]))
    
