def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError
    result = []
    for i in range(1,num+1):
        result.append(sequence(i))
    return " ".join(str(n) for n in result)

def sequence(i):
    if i == 1 or i == 2:
        return 1
    else:
        next = sequence(sequence(i-1)) + sequence(i-sequence(i-1))
        return next
