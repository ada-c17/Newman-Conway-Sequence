def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError
    values = []
    for i in range(1,num+1):
        values.append(dp(i, values))
    return " ".join(map(str, values))

def dp(num, values):
    if num == 1 or num == 2:
        return 1
    else:
        return values[values[num-2]-1]+values[num - values[num-2]-1]