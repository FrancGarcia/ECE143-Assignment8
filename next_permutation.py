def next_permutation(t:tuple)->tuple:
    """
    Given the input tuple, returns the next tuple in lexicographic order 
    as if the input tuple was from a list of all possible permutations.

    :param t: The tuple of integers of any length.
    
    :return: The tuple of integers that is the next lexicographic tuple in the list of permutations.
    """
    assert(isinstance(t, tuple)), "Input must be of type tuple"
    assert(len(t) > 0), "Tuple cannot be empty"
    assert(len(set(t)) == len(t)), "Tuple must not contain duplicate elements"
    for num in t:
        assert(isinstance(num, int)), "Each number in the input tuple must be an integer"

    l = list(t)
    n = len(l)
    i = 0
    k = -1
    while i < n-1:
        if  l[i] < l[i+1]:
            k = i
        i += 1

    if k == -1:
        return tuple(sorted(l))

    j = n-1
    last = 0
    while j > k:
        if l[k] < l[j]:
            break
        j -= 1

    l[k],l[j] = l[j],l[k]
    l[k+1:] = reversed(l[k+1:])

    res = tuple(l)

    assert(len(res) == len(t)), "Output tuple must be same length as input tuple"
    assert(isinstance(res, tuple)), "Result must be of type tuple"

    return res

if __name__ == "__main__":
    print(next_permutation((2,3,1)))
    print(next_permutation((0, 5, 2, 1, 4, 7, 3, 6)))
    print(next_permutation((3,2,1,0)))