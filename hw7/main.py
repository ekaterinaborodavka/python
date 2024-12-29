# Task 7.1
def say_hi(name, age):
    if age > 0:
        return f"Hi. My name is {name} and I'm {age} years old"
    else:
        return "Incorrect age"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
print(say_hi("Alex", 32))
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print(say_hi("Frank", 68))
print('ОК')

# Task 7.2
def correct_sentence(text):
    cap_text = text[0].upper() + text[1:]
    cap_text = cap_text if cap_text[len(cap_text)-1] == "." else cap_text + "."
    return cap_text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

# Task 7.3
def second_index(text, some_str):
  first_entry = text.find(some_str)
  if first_entry == -1:
      return None
  else:
      second_entry = text.find(some_str, first_entry+1)
      return None if second_entry == -1 else second_entry

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

# Task 7.4
def common_elements():
    multiple3 = set(range(0,100, 3))
    multiple5 = set(range(0, 100, 5))
    return multiple3.intersection(multiple5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print(common_elements())