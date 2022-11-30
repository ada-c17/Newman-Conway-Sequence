def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: 
        Space Complexity: 
    """
    if num <= 0:
        raise ValueError

    sequence = []
    for i in range(num+1):
        calc_newman_conway(i, sequence)
    
    return " ".join(str(v) for v in sequence[1:])

def calc_newman_conway(i, P):
    if i <=2:
        P.append(1)
    else:
        next_num = P[P[i-1]] + P[i - P[i - 1]]
        P.append(next_num)
