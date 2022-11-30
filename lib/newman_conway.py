def newman_conway(n):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if n <= 0:
        raise ValueError
    elif n == 1:
        return "1"
    
    nums = {1: 1, 2: 1}

    p(n, nums)

    return ' '.join(str(c) for c in nums.values())

def p(n, result):
    if n not in result:
        pn_1 = p(n - 1, result)
        nc = p(pn_1, result) + p(n - pn_1, result)
        result[n] = nc

    return result[n]