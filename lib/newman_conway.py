def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError(0)
    else: 
        arr = [0, 1, 1]

    if num == 1 or num == 2:
        return '1'
    else:
        for i in range(3, num + 1):                  
            p = arr[arr[i - 1]] + arr[i - arr[i - 1]]
            arr.append(p)
    data = ' '.join(str(n) for n in arr[1:])
    return data

print(newman_conway(4))