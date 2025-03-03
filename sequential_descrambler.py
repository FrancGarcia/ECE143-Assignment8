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
    #combinations = generate_word_combinations(final_perms)
    #for combo in combinations:
    #    print(combo)

def generate_word_combinations(word_dict):
    # Sort keys to maintain order in the output
    sorted_keys = sorted(word_dict.keys())
    
    # Get corresponding word sets in order
    word_sets = [word_dict[key] for key in sorted_keys]
    
    # Generate all possible combinations
    combinations = list(it.product(*word_sets))
    
    return combinations




# Example Usage
w = 'trleeohelh'
k=(8,2)
#descrambler(w,k)
descrambler('choeounokeoitg',(3,5,6))
#descrambler('qeodwnsciseuesincereins',(4,9,10))
#print(list(descrambler('qeodwnsciseuesincereins', (4,7,12))))
#print(descrambler())