def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
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
    # for loop that iterates through num
        for n in range(3,num+1):
    # P(P(n - 1)) + P(n - P(n - 1))
            cache.append(cache[cache[n-1]] + cache[n - cache[n - 1]])
    # append this ^
    cache_string = [str(x) for x in cache]
    return " ".join(cache_string[1:])

