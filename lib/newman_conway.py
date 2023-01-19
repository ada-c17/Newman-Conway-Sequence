def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError("can't be 0 or neg")
    memory = {}
    answer_list = []
    for num in range(1, num+1):
        if num < 3:
            memory[num] = 1
            answer_list.append("1")
            continue
        recall = memory[num-1]
        solution = memory[recall] + memory[num-recall]
        memory[num] = solution
        answer_list.append(str(solution))
    return " ".join(answer_list)
# newman_conway(4)

