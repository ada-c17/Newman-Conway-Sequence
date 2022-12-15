def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) because we iterate through the list once
        Space Complexity: O(n) because we create a list of size n
    """
    if num <= 0:
        raise ValueError("Input must be greater than 0")
    newman_conway_list = [0,1, 1]
    if num < 3:
        newman_conway_list = newman_conway_list[:num + 1]
        return newman_conway_list_to_string(newman_conway_list)

    for i in range(3, num + 1):
        newman_conway_list.append(newman_conway_list[newman_conway_list[i - 1]] + newman_conway_list
[i - newman_conway_list[i - 1]])
    return newman_conway_list_to_string(newman_conway_list)
        
def newman_conway_list_to_string(list):
    result = ""
    for i in list[1:]:
        result += str(i) + " "
    return result[:-1]
