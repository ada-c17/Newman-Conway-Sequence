def newman_conway(num):
    if num <= 0: 
        raise ValueError("Input can't be 0 or less than 0");

    if num == 1:
        return "1";
    
    p = [0, 1, 1];

    for i in range(3, num + 1):
        maths = p[p[i-1]]+p[i-p[i-1]]
        p.append(maths);

    output = []
    for i in range(1, len(p)):
        output.append(str(p[i]));

    return " ".join(output);
