def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    #P(1) = 1
#P(2) = 1
#for all n > 2
#P(n) = P(P(n - 1)) + P(n - P(n - 1))
    if not num or num < 0:
        raise(ValueError)

    if num == 1:
        return "1"

    if num == 2:
        return "1 1"

    nc_list = [None,1,1]
    for i in range(3,num+1):
        nc = nc_list[nc_list[i-1]] + nc_list[i - nc_list[i-1]]
        nc_list.append(nc)
    

        
    print(" ".join(str(x) for x in nc_list[1:]))
    return " ".join(str(x) for x in nc_list[1:])

newman_conway(20)
