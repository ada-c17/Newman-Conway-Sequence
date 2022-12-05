def newman_conway(n):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) because the for loop iterates over a range of n numbers and computes each number in the sequence once
        Space Complexity: O(n) because the nums list is storing n numbers
    """
    if n <= 0:
        raise ValueError
    if n == 1:
        return '1'
    nums = [1, 1]
    for i in range(2, n):
        nums.append(nums[nums[i - 1] - 1] + nums[i - nums[i - 1]])
    return " ".join(str(num) for num in nums)
