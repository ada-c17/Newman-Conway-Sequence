def newman_conway(num):

    if num <= 0:
        raise ValueError
    elif num == 1:
        return '1'


    f = [0, 1, 1]

    print(f[1], end='')
    print(f[2], end='')
    for i in range(3, num + 1):
        f.append(f[f[i-1]] + f[i-f[i -1]])
        print(f[i], end='')
    

    sequence = [str(x) for x in (f[1:])]

    return ' '.join(sequence)


