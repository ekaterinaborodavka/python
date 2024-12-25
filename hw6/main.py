# Task 6.1
import string

letters_range = input("Enter the range of letters (a-A) : ")
LETTERS_LEN = 3

if len(letters_range) == LETTERS_LEN:
    first_idx = string.ascii_letters.find(letters_range[0])
    second_idx = string.ascii_letters.find(letters_range[2])
    result_range = string.ascii_letters[second_idx:first_idx+1] if first_idx > second_idx else string.ascii_letters[first_idx:second_idx+1]
    print(result_range)
else:
    print("Range entered incorrectly")

# Task 6.2
MIN_SEC = 0
MAX_SEC = 8640000
day = "день"
seconds = int(input(f"Enter a number between {MIN_SEC} and {MAX_SEC}: "))

if MIN_SEC <= seconds <= MAX_SEC:
    days, residue = divmod(seconds, 86400)
    hours, residue2 = divmod(residue, 3600)
    minutes, sec = divmod(residue2, 60)
    if 11 <= days % 100 <= 14:
        day = "днів"
    else:
        last_digit = days % 10
        if last_digit == 1:
            day = "день"
        elif 2 <= last_digit <= 4:
            day = "дні"
        else:
            day = "днів"
    print(f"{days} {day}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}")
else:
    print("Number is incorrect")

# Task 6.3
number = input("Enter a number: ")
MIN_NUM = 9
result = 1

if int(number) > MIN_NUM:
    while int(number) > MIN_NUM:
        result = 1
        for num in number:
            result *= int(num)
        number = str(result)
    print(result)
else:
    print("Number is incorrect")
