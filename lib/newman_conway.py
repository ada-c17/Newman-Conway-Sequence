def newman_conway(num: int) -> str:
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError('Input must be a positive integer')
    sequence = []
    i = 0
    for i in range(num):
        sequence.append(str(p(i + 1)))
    return ' '.join(sequence)

def p(num: int) -> int:
    return 1 if num < 3 else p(p(num - 1)) + p(num - p(num - 1))
