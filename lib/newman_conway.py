def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    if num <= 0:
        raise(ValueError)
    if num == 1:
        return '1'
    
    solutions = [0,1,1]
    current = 3

    while current <= num:
        solutions.append(solutions[solutions[current-1]] + solutions[current - solutions[current - 1]])
        current += 1

    return ' '.join(str(x) for x in solutions[1:])


# P(1) = 1
# P(2) = 1
# for all n > 2
# P(n) = P(P(n - 1)) + P(n - P(n - 1))
