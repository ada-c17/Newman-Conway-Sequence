# def nth_newman(num):
#     """ Returns the numth of the Newman Conway numbers for the given value.
#     """
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return nth_newman(nth_newman(num-1)) + nth_newman(num - nth_newman(num-1))


# def newman_conway(input):
#     """ Returns a list of the Newman Conway numbers for the given value.
#         Time Complexity: O(n) with n as input
#         Space Complexity: O(n) with n as input
#     """
#     if input <= 0:
#         raise ValueError
#     numbers = []
#     for n in range(1, input+1):
#         print(f"{n=}")
#         numbers.append(str(nth_newman(n)))
#     return " ".join(numbers)


def newman_conway(input):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) with n as input
        Space Complexity: O(n) with n as input
    """
    if input <= 0:
        raise ValueError
    elif input == 1:
        return "1"
    elif input == 2:
        return "1 1"
    else:
        curr_seq = [0, 1, 1]
        for i in range(3, input+1):
            curr_seq.append(curr_seq[curr_seq[i-1]] +
                            curr_seq[i-curr_seq[i-1]])
        seq = curr_seq[1:]  # o(input-1)
        str_seq = map(str, seq)  # o(input-1)
        return " ".join(str_seq)  # o(input-1)
