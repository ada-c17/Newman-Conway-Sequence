def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    if num <= 0:
        raise ValueError("Invalid input")
    elif num == 1:
        return "1"

    sequence = [0] * (num + 1)
    sequence[1] = 1
    sequence[2] = 1

    for i in range(3, num + 1):
        sequence[i] = sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]]

    return " ".join([str(el) for el in sequence[1:]])