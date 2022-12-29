def newman_conway(num, sol = None):
    """ 
    Returns a list of the Newman Conway numbers for the given value.
    Time Complexity: ?
    Space Complexity: ?
    
    """
    if num <= 0:
        raise ValueError("Number must be greater than 0")

    if num == 1:
        return "1"

    solutions = [0, 1, 1]

    for i in range(3, num + 1):
        result = solutions[solutions[i - 1]] + solutions[i - solutions[i - 1]]
        solutions.append(result)
    
    solutions.pop(0)

    return (" ").join(map(str, solutions))
