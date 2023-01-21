def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError
    
    if num == 1:
        return "1"
    
    sequence = [0, 1, 1]

    for i in range(3, num + 1):
        sequence.append(sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]])
    sequence.pop(0)

    str_sequence = [str(i) for i in sequence]
    return " ".join(str_sequence)
