from collections import Counter
from itertools import product
    
def load_dictionary(filename):
    """
    Load words from the given file into a dictionary of sets by word length.
    It will be located in /tmp/google-10000-english-no-swears.txt in the autograder.

    :param filename: The string name of the file that contains the corpus.

    :return: A set of the words found in the corpus to
    cross-reference with the input word in the descrambler().
    """
    # open("/tmp/google-10000-english-no-swears.txt")
    assert(isinstance(filename, str) and len(filename) > 0), "filename must be a valid str"
    with open(filename) as f:
        return set(word.strip().lower() for word in f)

def valid_word_list(w_counter, words):
    """
    Filters words to ensure they only contain characters from w.

    :param words: The words that are in the dictionary of words from the corpus.
    :param w_coutner: The frequency of characters in the input word for descrambler().

    :return: The list of filtered words that do not match the
    frequency of characters in the input word for descrambler().
    """
    assert(isinstance(w_counter, Counter) and len(w_counter) > 0), "The counter collection must contain elements"
    assert(isinstance(words, list) and len(words) > 0), "words must be a valid list with elements"
    return [word for word in words if not (Counter(word) - w_counter)]

def descrambler(w,k):
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

    # file for autograder = "/tmp/google-10000-english-no-swears.txt"
    # file for local testing = "text_file.txt"
    dictionary = load_dictionary("/tmp/google-10000-english-no-swears.txt")
    w_counter = Counter(w)
    
    word_lists = [valid_word_list(w_counter, [word for word in dictionary if len(word) == length]) for length in k]
    
    for words in product(*word_lists):
        temp_counter = w_counter.copy()
        for word in words:
            temp_counter.subtract(Counter(word))
        if all(v == 0 for v in temp_counter.values()):
            yield " ".join(words)

# print(list(descrambler("trleeohelh", (5, 5))))
# print(list(descrambler("choeounokeoitg", (3, 5, 6))))
# print(list(descrambler("qeodwnsciseuesincereins", (4, 7, 12))))