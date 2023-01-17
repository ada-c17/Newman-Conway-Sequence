def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError

    if num == 1:
        return "1"
    
    if num == 2:
        return "1 1"
    
    seq = [0, 1, 1]

    for i in range(3, num + 1):
        cal = seq[seq[i-1]] + seq[i-seq[i-1]]
        seq.append(cal)
    seq_str = [str(i) for i in seq[1: ]]
    return " ".join(seq_str)