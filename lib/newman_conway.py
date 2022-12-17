def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError("Input cannot be less than one.")
    if num == 1:
        return "1"

    memo = [0, 1, 1]

    count = 3
    while count <= num:
        memo.append(memo[memo[count - 1]] + memo[count - memo[count - 1]])
        count += 1

    string = [str(item) for item in memo]

    answer = " ".join(string[1:])

    return answer
    