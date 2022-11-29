def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError
    sequence = []
    for i in range(num+1):
        calc_newman_conway(i, sequence)
    return " ".join(str(v) for v in sequence[1:])

def calc_newman_conway(i, P):
    if i == 0 or i == 1 or i ==2:
        P.append(1)
    else:
        next_num = P[P[i-1]] + P[i - P[i - 1]]
        P.append(next_num)

    



# def fibonacci_recursive(n, solutions=None):
#     if solutions is None:
#         solutions = {}

#     if n in solutions:
#         return solutions[n]

#     if n == 0 or n == 1:
#         solutions[n] = n
#     else:
#         solutions[n] = (fibonacci_recursive(n - 1, solutions) +
#             fibonacci_recursive(n - 2, solutions))

#     return solutions[n]

# Pattern printed out
# P(n) = P(P(n - 1)) + P(n - P(n - 1)) 
# P(3) = P(P(2)) + P(3 - P(2))
# P(3) = P(1) + P(3-1)
# P(3) = P(1) + P(2)
# P(3) = 1 + 1 = 2

# P(4) = P(P(3)) + P(4 - P(3))
# P(4) = P(2) + P(4-2)
# P(4) = 1 + P(2) = 1 + 1 = 2

# P(5) = P(P(n - 1)) + P(n - P(n - 1))
# P(5) = P(P(4)) + P(5 - P(4))
# P(5) = P(2) + P(3)
# P(5) = 1 + 2 = 3

# P(6) = P(P(n - 1)) + P(n - P(n - 1))
# P(6) = P(P(5)) + P(6 - P(5))
# P(6) = P(3) + P(3) = 2 + 2 = 4
