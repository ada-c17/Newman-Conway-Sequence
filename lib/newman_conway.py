def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: o(n)
        Space Complexity: o(n)
    """

    cache = [0,1,1]
    if num <= 0:
        raise ValueError(ValueError)
    if num == 1:
        return '1'
    if num == 2:
        cache_string = [str(x) for x in cache]
        return " ".join(cache_string[1:])
    if num >= 3:
        for n in range(3,num+1):
            cache.append(cache[cache[n-1]] + cache[n - cache[n - 1]])
    cache_string = [str(x) for x in cache]
    return " ".join(cache_string[1:])

