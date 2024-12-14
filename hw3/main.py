# Task 3.1
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

# Task 3.2
numbers_v1 = [12, 3, 4, 10]
new_numbers_v1 = [numbers_v1.pop()] + numbers_v1 if len(numbers_v1) > 1 else numbers_v1
numbers_v2 = [5]
new_numbers_v2 = [numbers_v2[-1]] + numbers_v2[:len(numbers_v2)-1] if len(numbers_v2) > 1 else numbers_v2
numbers_v3 = [1, 2, 3, 4, 5, 6]
numbers_v3.insert(0, numbers_v3.pop()) if len(numbers_v3) > 1 else numbers_v3
print(new_numbers_v1)
print(new_numbers_v2)
print(numbers_v3)

# Task 3.3
nums = [1, 2, 3, 4, 5, 6]
length = len(nums)
half = length//2
is_even = length % 2 == 0
match length:
    case 0 | 1:
        print(nums, [])
    case _:
        if is_even:
            print("Result:", nums[:half], nums[half: length])
        else:
            print("Result:", nums[:half+1], nums[half+1: length])
