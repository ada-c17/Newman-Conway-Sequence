def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: On
        Space Complexity: On
    """
    arr = [0, 1, 1]
    if num < 1:
        raise ValueError
    if num == 1:
        return '1'

    for i in range(3, num + 1):
        num = arr[arr[i-1]]+arr[i-arr[i-1]]
        arr.append(num)
    arr.pop(0)

    result = [str(i) for i in arr]
    return " ".join(result)