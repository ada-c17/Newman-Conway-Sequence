def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1 :
        raise ValueError ("input should be greather than 0")
    
    elif num == 1 :
        return "1"
    
    elif num == 2 :
        return "1 1"
    else:
        sequence = [0 for _ in range(num + 1)]
        sequence[0] = 0
        sequence[1] = 1
        sequence[2] = 1
        for i in range (3, num + 1):
            sequence[i] = sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]]
        result = " "
        for n in range (1, len(sequence)):
            result += str(sequence[n]) + " "
        result = result.strip()
        return result
    