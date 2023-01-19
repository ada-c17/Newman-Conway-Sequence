def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num <= 0:
        raise ValueError
    if num == 1:
        return "1" 
    
    dp = [0] * (num+1)
    dp[1] = 1
    dp[2] = 1
    for x in range(3, num+1):
        dp[x] = dp[dp[x-1]] + dp[x - dp[x-1]]
    
    dp_str = [str(n) for n in dp[1:]]
    
    return " ".join(dp_str)