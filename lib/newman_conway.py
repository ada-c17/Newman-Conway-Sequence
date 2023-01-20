def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError("invalid input")
    seq = [1,1]
    for i in range(2,num):
        seq.append(seq[seq[i-1]-1]+seq[i-seq[i-1]])
    return ' '.join(map(str, seq[:num]))

