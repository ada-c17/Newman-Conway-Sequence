def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) where n is the input
        Space Complexity: O(n) where n is the input
    """

    if num < 1:
        raise ValueError
    elif num == 1:
        return "1"

    memo = [0, 1, 1]
    
    output_string = "1 1 "
    for i in range(3, num + 1):
        new_number = memo[memo[i - 1]] + memo[i - memo[i - 1]]
        memo.append(new_number)
        output_string += f"{str(new_number)} "

    return output_string[:-1]
