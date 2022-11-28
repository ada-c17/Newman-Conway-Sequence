def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError

    cache = {}

    result = []
    for n in range(1, num + 1):
        result.append(str(getNum(n, cache)))

    return ' '.join(result)


def getNum(n, cache):
    if n in cache:
        return cache[n]

    if n == 1:
        cache[1] = 1
        return 1
    if n == 2:
        cache[2] = 1
        return 1
    result = getNum(getNum(n - 1, cache), cache) + getNum(n - getNum(n - 1, cache), cache)
    cache[n] = result
    return result