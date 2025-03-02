from collections import defaultdict
import itertools as it

def load_dictionary():
    """
    Load words from the given file into a dictionary of sets by word length.
    It will be located in /tmp/google-10000-english-no-swears.txt in the autograder.
    """
    words = defaultdict(set)
    # open("/tmp/google-10000-english-no-swears.txt")
    with open("text_file.txt") as file:
        # One word per line
        for word in file.read().split():
            words[len(word)].add(word)
    return words


def descrambler(w, k):
    """
    Generate all valid phrases from the scrambled string w and tuple k.

    :param w: String containing the scrambled phrase to partition.
    :param k: Tuple containing the word lengths to yield.
    :yield: Valid word combinations from the dictionary of words to output.
    """
    assert(isinstance(k,tuple)), "Second argument must be of type tuple"
    for num in k:
        assert(isinstance(num, int)), "Each element in the input tuple must be of type int"
    assert(isinstance(w, str)), "First argument must be of type string"
    assert(sum(k) == len(w)), "The length of the input word must match the sum of all partition lengths in the input tuple"

    words = load_dictionary()  

    perms = defaultdict(set)
    for l in k:
        print(l)
        perms_of_l = set("".join(tup) for tup in it.permutations(w,l))
        perms[l] = perms_of_l
    
    # Iterate through each key,value pair in the possible words and do the set difference for the same key,different set in the words dictionary
    final_perms = defaultdict(set)
    for length,tuples in perms.items():
        if length in words:
            final_perms[length] = words[length].intersection(tuples)
    print(final_perms)
    generate_permutations(final_perms)

def generate_permutations(d:dict):
    # Extract all sets from the dictionary
    sets = [d[key] for key,value in d.items()]
    
    # Generate all combinations (one word from each set)
    for comb in it.product(*sets):
        # Generate all permutations of the combination
        for perm in it.permutations(comb):
            yield ' '.join(perm)




# Example Usage
w = 'trleeohelh'
k=(5,5)
descrambler(w,k)
#descrambler('choeounokeoitg',(3,5,6))
#print(list(descrambler('qeodwnsciseuesincereins', (4,7,12))))
#print(descrambler())