def newman_conway(n):
    if n <= 0:
        raise ValueError("Input should be greater than 0")
    elif n == 1:
        return '1'
    elif n == 2:
        return '1 1'
    else:
        a = [1, 1, 1]
        for i in range(3, n + 1):
            a.append(a[a[i-1]] + a[i-a[i-1]])
        return ' '.join(str(x) for x in a[1:])
