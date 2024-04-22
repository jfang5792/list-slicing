def concatenate_new_value(input_list, new_value):
    """Return a list that is the same as the input list, but with new_value
    added on to the end.

    Do this using list concatenation. You cannot use the append() method.

    For example:

    >>> months = ['Jan', 'Feb', 'Mar', 'Apr', May', 'Jun']
    >>> concatenate_new_value(months, 'Jul')
    ['Jan', 'Feb', 'Mar', 'Apr', May', 'Jun', 'Jul']
    """
    #pass
    return input_list + [new_value]


def pig_latin(word):
    """Given a word, return the Pig Latin version of the word.
    Pig Latin Rules:
        1. If the word begins with a consonant (not a, e, i, o, u),
           move the first letter to the end and add ‘ay’
        2. If the word begins with a vowel, add ‘yay’ to the end
    For example:
    >>> pig_latin('porcupines')
    'orcupinespay'

    >>> pig_latin('apple')
    'appleyay'
    """
    #pass
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels: #if the first letter in the word beings with a vowel
        new_word = word + 'yay'
    else:
        new_word = word[1:] + word[0] + 'ay' #else move first letter to the end
    return new_word


def replace_middle(input_list):
    """Replace all elements of a list but the first two and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.
    Input list must be modified in-place, not merely reassigned to a new value.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples
    [0, 3, 42, 37, 24, 27]

    """
    #pass
    input_list[2:-2] = [42, 37]


def delete_middle(input_list):
    """Remove all elements from input_list except the first two and last two.

    Input list must be modified in-place, not merely reassigned to a new value.

    Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes
    ['Do', 'Re', 'Ti', 'Do']

    """

    #pass
    input_list[2:-2] = []

def double_with_list_comprehension(input_list):
    """Given a list of numbers, return a list with all numbers doubled.

    Use a list comprehension to do this.

    For example:

    >>> double_with_list_comprehension([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]
    """
    #pass
    # numbers_doubled = [number * 2 for number in input_list]
    # return numbers_doubled
    return [number * 2 for number in input_list]

def multiplication_table(n):
    """ Return a multiplication table for the given number, in the form
    of a 2D array.

    For example:

    >>> multiplication_table(3)
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

    """
    #pass
    table = []
    numbers = list(range(1, n + 1))
    for number in range(1, n + 1):
        row = [num * number for num in numbers]
        table.append(row)
    return table
