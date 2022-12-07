def newman_conway(num: int) -> str:
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) - The for loop that `p()` is called in and the string building at the return statement are both O(n) operations. `p()` itself is O(1), no matter the number passed in, it performs a maximum of 4 array look-ups.
        Space Complexity: O(n) - `sequence` is a list element whose size is proportional to the input number. Space is otherwise constant, even though the solution is recursive, there is a maximum number of 5 additional stack frames opened at any one time, no matter the input number.
    """
    if num < 1:
        raise ValueError('Input must be a positive integer')
    sequence = []
    for i in range(num):
        new_value = 1 if i < 2 else p(i + 1, sequence)
        sequence.append(new_value)
    return ' '.join([str(n) for n in sequence])

def p(num: int, s: list[int]) -> int:
    if num <= len(s):
        return s[num - 1]
    return 1 if num < 3 else p(p(num - 1, s), s) + p(num - p(num - 1, s), s)
