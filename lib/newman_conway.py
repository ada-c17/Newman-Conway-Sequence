nc_dict = {
    1: 1,
    2: 1
}
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """

    if num <= 0:
        raise ValueError
    elif num == 1:
        return str(nc_dict[1])
    
    for i in range(3, num + 1):
        nc_dict[i] = newman_conway_helper(nc_dict[i - 1]) + newman_conway_helper(i - nc_dict[i - 1])

    output_string = ""
    for n in nc_dict.keys():
        output_string += f"{str(nc_dict[n])} "
    return output_string[:-1]

def newman_conway_helper(n):
    if n == 1:
        return nc_dict[1]
    elif n == 2:
        return nc_dict[2]
    elif n >= 3:
        for i in range(3, n+1):
            if i not in nc_dict:
                nc_dict[i] = newman_conway_helper(nc_dict[i - 1]) + newman_conway_helper(i - nc_dict[i - 1])
        
        return newman_conway_helper(nc_dict[n - 1]) + newman_conway_helper(n - nc_dict[n - 1])