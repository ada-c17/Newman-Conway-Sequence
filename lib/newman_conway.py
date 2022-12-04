
import array
def newman_conway(num):
    val = 0

    if num <= 0:
        raise ValueError
    
    if num == 1:
        return str(1)
    
    if num == 2:
        return "1 1"
    
    arr = array.array("i", [1, 1])

    for i in range(1, num+1):
        val = arr[arr[i - 1]] + arr[i-arr[i-1]]
        arr.append(val)
    
    result = ' '.join(str(elem) for elem in arr)

    return result


