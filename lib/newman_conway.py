def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n), 2 for loops (initial calculation and conversion to string)
        Space Complexity: O(n), created 2 lists (sequence and sequence_str)
    """
    if num <= 0:
        raise ValueError("input must be greater than 0")

    if num == 1:
        return "1"

    sequence = [0,1,1]

    # P(1) and P(2) both equal to 1, so start calculation from any num > 2
    for integer in range(3, num + 1):
        calculation = sequence[sequence[integer - 1]] + sequence[integer - sequence[integer - 1]]
        sequence.append(calculation)

    sequence_str = []
    # excludes index 0 as num < 1 would raise ValueError
    # can't have range(1,1), so need to account for return for num = 1
    for integer in range(1, len(sequence)):
        sequence_str.append(str(sequence[integer]))

    return " ".join(sequence_str)


    # alternative to line 12:
    # sequence = array.array('i', [0, 1, 1])
    # this creates an array with elements restricted by typecode (‘i’ = int)
    # with optional initalizer (must be a list, bytes-like object, or iterable over elements)
    # but have to import array module
