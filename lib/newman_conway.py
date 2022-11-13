def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError
    elif num == 1:
        return "1"

     # add a 0 to line up with 1-based indexing in the formula
    res = [0, 1, 1]

    while len(res) < num + 1:
        n = len(res)
        res.append(res[res[n - 1]] + res[n - res[n - 1]]) 

    return " ".join([str(n) for n in res[1:]])