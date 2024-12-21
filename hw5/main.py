# Task 5.1
import string
import  keyword

variable = input("Enter the variable name : ")
punc = string.punctuation.replace('_', ' ')
is_punc = False
for char in punc:
    if variable.find(char) != -1:
        is_punc = True

while True:
    if variable[0].isdigit():
        print(False)
        break
    elif not variable.islower():
        if variable == "_":
            print(True)
        else:
            print(False)
        break
    elif variable in keyword.kwlist:
        print(False)
        break
    elif variable.find("__") != -1:
        print(False)
        break
    elif is_punc:
        print(False)
        break
    else:
        print(True)
        break

# Task 5.2
while True:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    operation = input("Enter operation: ")

    match operation:
        case "+":
            print("Result:", number1 + number2)
        case "-":
            print("Result:", number1 - number2)
        case "*":
            print("Result:", number1 * number2)
        case "/":
            if number2 == 0:
                print("You can't divide by zero!")
            else:
                print("Result:", number1 / number2)
        case _:
            print("You have entered an incorrect operation")
    user_input = input("Enter 'Y' if you want to continue calculations: ")
    if user_input != "Y":
        print("Exit from program...")
        break

# Task 5.3
text = input("Enter the text: ")
text_title_without_space = text.title().replace(" ", "")
hashtag = "#"

for char in text_title_without_space:
    if char not in string.punctuation:
        hashtag += char
print(hashtag[:141])