def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    l = [0,1,1]
    answer = ""
    if num <= 0:
        raise ValueError
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    else:
        for i in range(3, num + 1):
            n= (l[l[i-1]] + l[i-l[i-1]])
            l.append(n)

    for i in range(1, len(l)):
        answer += f"{str(l[i])} "
    
    return answer.rstrip()