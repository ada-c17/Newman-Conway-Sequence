def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) where n is num
        Space Complexity: O(n) where n is num
        P(P(n - 1)) + P(n - P(n - 1))
    """
    if num < 1:
        raise ValueError

    if num == 1:
        return '1'
    elif num == 2:
        return '1 1'

    digits = [0, 1, 1]
    current = 3
    while current <= num:
        digits.append(digits[digits[current - 1]] + digits[current - digits[current - 1]])
        current += 1

    print(digits)
    return ' '.join([str(x) for x in digits[1:]])
