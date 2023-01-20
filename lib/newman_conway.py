def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError("invalid input")

    res = []

    def helper(n):
        if n == 1 or n == 2:
            return 1
        return res[res[n-2]-1]+res[n-res[n-2]-1]

    for i in range(1, num+1):
        res.append(helper(i))

    return ' '.join(map(str, res))
