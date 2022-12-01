import array
def newman_conway(num):
    if num <= 0:
        raise ValueError()
    elif num == 1:
        return "1"
    elif num == 2:
        return "1 1"
    result = []  
    def newman(n, f):
        f = [0, 1, 1]
    
        # To store values of sequence in array
        for i in range(3, n + 1):
            r = f[f[i-1]]+f[i-f[i-1]]
            f.append(r);

        return f
    result = newman(num, result)[1:]
    result = [str(i) for i in result]
    return " ".join(result)
    