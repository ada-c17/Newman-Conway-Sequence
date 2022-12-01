def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """

    #P(n) = P(P(n - 1)) + P(n - P(n - 1))
    #time compl: O(n2)
    
    sequence = []
    seen = set()

    def _newman_conway(num,sequence):
        if num <= 0:
            raise ValueError('invalid input')
        if num == 2: 
            if num not in seen:
                sequence.append(1)
                sequence.append(1)
                seen.add(num)
            return 1
        elif num == 1:
            if 1 not in seen and 2 not in seen:
                sequence.append(1)
                seen.add(num)
            return 1
        
        else:
            results = _newman_conway(_newman_conway(num-1,sequence),sequence) + _newman_conway(num-_newman_conway(num-1,sequence),sequence)
            if num not in seen:
                sequence.append(results)
                seen.add(num)
            return results

    _newman_conway(num,sequence)
    return " ".join([str(n) for n in sequence])

if __name__ == "__main__":
    print(newman_conway(2))
