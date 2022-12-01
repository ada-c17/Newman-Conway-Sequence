def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not num or num < 0:
        raise(ValueError)

    if num == 1:
        return "1"

    nc_list = [1,1]
    for i in range(2,num):
        nc = nc_list[(nc_list[i-1]-1)] + nc_list[i - nc_list[i-1]]
        nc_list.append(nc)
    

    # debug  
    # print(" ".join(str(x) for x in nc_list))
    return " ".join(str(x) for x in nc_list)
