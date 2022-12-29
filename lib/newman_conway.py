def newman_conway(num):
    """ 
    Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    
    if num <= 0:
        raise ValueError

    if num == 1:
        return "1"

    if num == 2:
        return "1 1"

    sequence = [0, 1, 1]

    for i in range(3, num + 1):
        calculate = sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]]
        sequence.append(calculate)

    sequence_str = [str(i) for i in sequence[1: ]]
    return " ".join(sequence_str)