def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Where n is the number of integers in the output string,
        Time Complexity: O(num)
        Space Complexity: O(num)
    """

    if num <= 0:
        raise ValueError
    
    if num == 1:
        return '1'

    return ' '.join(str(n) for n in sequence(num))

def sequence(n):
    result = [None] * n
    result[0] = 1
    result[1] = 1

    for i in range(2, n):
        result[i] = result[result[i - 1] - 1] + result[i - result[i - 1]]
    
    return result


