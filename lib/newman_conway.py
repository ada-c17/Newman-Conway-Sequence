def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    
    if num < 1:
        raise ValueError()

    if num == 1:
        return str(1)

    nc = [0, 1, 1]

    for i in range(3, num + 1):
        maths = nc[nc[i - 1]] + nc[i - nc[i - 1]]
        nc.append(maths)

    return " ".join(str(x) for x in nc[1:])
