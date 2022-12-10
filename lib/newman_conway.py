def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) where n is the number, the larger the number the longer it will take to iterate and compute the newman conway sequence
        Space Complexity: O(n) where n is the number, the larger the number the more space it will take to store the newman conway sequence in the nums list
    """

    if num < 1:
        raise ValueError("Number must be at least 1")
    elif num == 1:
        return "1"
    elif num == 2:
        return "1 1"
    
    nums = [0, 1, 1]
    for i in range(3, num + 1):
        calc = nums[nums[i - 1]] + nums[i - nums[i - 1]]
        nums.append(calc)
    
    
    return " ".join(map(str, nums[1:]))