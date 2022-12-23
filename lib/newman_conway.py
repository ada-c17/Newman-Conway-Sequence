def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    memo = [0, 1, 1]
    for i in range(3, num + 1):
        current = memo[memo[i - 1]] + memo[i - memo[i - 1]]
        memo.append(current)

    memo_str = [str(i) for i in memo[1:]]
    return (" ").join(memo_str)

# P(n) = P(P(n - 1)) + P(n - P(n - 1))
# P(3)
# P(P(2)) + P(3 - P(2))
# P(1) + P(3 - 1)
# 1 + P(2)
# 1 + 1
# = 2
