def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError
    if num == 1:
        return '1'
    numbers = [0, 1, 1]

    for i in range(3, num + 1):
        num = numbers[numbers[i-1]]+numbers[i-numbers[i-1]]
        numbers.append(num); 

    numbers.pop(0)
    print(" ".join([str(elem) for elem in numbers]));
    return " ".join([str(elem) for elem in numbers])

