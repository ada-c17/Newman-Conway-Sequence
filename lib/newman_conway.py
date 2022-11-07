import array

def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num <= 0:
        raise ValueError
    elif num == 1:
        return '1'

    f = array.array('i', [0, 1, 1])

    for i in range(3, num + 1):
        r = f[f[i - 1]] + f[i - f[i - 1]]
        f.append(r)

    res = ''
    for i in range(1, len(f)):
        if i == len(f) - 1:
            res += str(f[i])
            break
        res += f'{f[i]} '

    return res
