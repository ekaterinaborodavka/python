import string

# Task 8.1
def add_one(some_list):
    numb_str = "".join((str(num) for num in some_list))
    numb = int(numb_str)+1
    return [int(n) for n in str(numb)]
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

# Task 8.2
def is_palindrome(text):
    if len(text):
        for char in string.punctuation + " ":
            text = text.replace(char, "")
        text = text.lower()
        text_reverse = ''.join(reversed(text))
        if text == text_reverse:
            return True
        else:
            return False
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

# Task 8.3
def find_unique_value(some_list):
    for num in some_list:
        if some_list.count(num) == 1:
            return num
   # counts = {}
   # for num in some_list:
   #     if num in counts:
   #         counts[num] += 1
   #     else:
   #         counts[num] = 1
   #
   # for num in some_list:
   #     if counts[num] == 1:
   #         return num

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")