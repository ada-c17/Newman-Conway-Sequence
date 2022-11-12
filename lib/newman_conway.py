def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1 :
        raise ValueError

    if num == 1:
        return "1"
    
    if num == 2 :
        return "1 1"
    
    storage_array = [0, 1, 1]

    for i in range(3, num + 1):
        new_num = storage_array[storage_array[i - 1]]+ storage_array[i - storage_array[i - 1]]
        storage_array.append(new_num)
    
    return_string = ""

    for i in range(1, len(storage_array)):
        if i == len(storage_array) - 1:
            return_string = return_string + str(storage_array[i])
        else:
            return_string = return_string + str(storage_array[i]) + " "
    
    
    return return_string