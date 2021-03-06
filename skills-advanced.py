"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    counter = {}
    
    for char in phrase:
      if char not in [' ', ',', '.']:
        counter[char] = counter.get(char, 0) + 1

    # print counter {'a': 2, 'e': 2, 'f': 4, 'i': 2, 'h': 2, 'k': 2, 's': 1, 'o': 2, 'S': 1, 't': 2}

    highest = max(counter.values())
    return [char for char, frequency in counter.items() if frequency == highest]


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    counter = {}

    for word in words:
        counter[len(word)] = counter.get(len(word), []) + [word]

    counter_list = []

    for word_length, word in counter.items():
        counter_list.append((word_length, sorted(word)))

    return sorted(counter_list)


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
