def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) - calculates and stores the value for each number in the range up to 
        given number. Previous numbers lookup from dict for calculation will be O(1).
        Space Complexity: O(n) - storing a value in both dictionary and list for each
        value up to the given number, also storing a recursive call on call stack for each number
        calculated.
    """
    if num <= 0:
        raise ValueError

    solutions = {1:1, 2:1}

    def helper(num, solutions):

        if num in solutions:
            return solutions[num]
        else:
            solutions[num] = helper(helper(num-1, solutions), solutions) + helper(num - helper(num-1, solutions), solutions)

        return solutions[num]

    helper(num, solutions)

    answer = []

    for n in range(1, num+1):
        answer.append(str(solutions[n]))

    return " ".join(answer)
