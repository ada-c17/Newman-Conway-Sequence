def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    
    # base cases
    if num <= 0:
        raise ValueError("Number must be greater than 0")
    if num == 1:
        return "1"

    # main
    seq = [0, 1, 1]

    for i in range(3, num+1):
        sequence = seq[seq[i-1]] + seq[i-seq[i-1]]
        seq.append(sequence)

    return " ".join(str(i) for i in seq[1:])
