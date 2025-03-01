def next_permutation(t:tuple)->tuple:
    """
    Given the input tuple, returns the next lexicographic tuple
    in a given permutation of the tuple itself.

    :param t: The tuple of any length.
    
    :return: The next tuple in permutations list that is lexicographically larger.
    """
    assert(isinstance(t, tuple)), "Input must be of type tuple"
    assert(len(t) > 0), "Tuple cannot be empty"

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
    l = (2,3,1)
    print(next_permutation(l))