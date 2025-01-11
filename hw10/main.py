# Task 10.1
def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    results = [begin]
    yield begin
    current_value = begin

    while len(results) < 4:
        current_value = func(current_value)
        results.append(current_value)
        yield current_value

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

# Task 10.2
import string

punc = string.punctuation.replace("'", "")
def cleaned_text(text):
    c_text = text
    c_text = c_text.replace('.', ' ').strip()
    for p in punc:
        c_text = c_text.replace(p, '').strip()
    return c_text

def first_word(text):
    word = ""
    if len(text.strip()):
        clean_text = cleaned_text(text)
        words = clean_text.split()
        word = words[0]
    return word

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')


# Task 10.3
def is_even(digit):
    return digit %2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
