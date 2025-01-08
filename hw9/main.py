# Task 9.1
def popular_words (text, words):
    """
    Determining the popularity of words in a text.

    :param text: Text.
    :param words: Word list.
    :return: Dictionary where the key is the word and the value is the number of repetitions.
    """
    count_words = {}
    if len(words):
        for w in words:
            count_words[w] = text.lower().split().count(w)
    return count_words
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

# Task 9.2
def difference (*args):
    """
    Finds the difference between the minimum and maximum number.

    :args args: Set of numbers (float or int).
    :return: Difference between the minimum and maximum as a number.
    """
    numbers = list(args)
    if len(numbers) :
        max_num = max(numbers)
        min_num = min(numbers)
        return round(max_num - min_num, 2)
    else:
        return 0
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

