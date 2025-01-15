# # Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# # - домашній номер телефону (тільки цифри та довжина номера)
# # - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# # - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# # - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
# # додатково:
# # - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра,
# # один символ, довжина пароля – від 8 до 16 символів)

import re
def validation(pattern: str, expression: str) -> bool:
    return bool(re.match(pattern, expression))

expression = ""
pattern = r"^\d{5,7}$"
print("1. Home phone number can be from 5 to 7 digits long.")
while not validation(pattern, expression):
    expression = input("Enter your home phone number to verify")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Number {expression} is valid.")

expression = ""
pattern = r"^\+38\(\d{3}\)\d{7}$"
print("1. Mobile phone (UA)")
while not validation(pattern, expression):
    expression = input("Enter your mobile number to verify (format +38(XXX)XXXXXXX): ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Number {expression} is valid.")


expression = ""
pattern = r"^[a-z0-9]+[_]?[a-z0-9]+@[a-z]{2,5}\.[a-z]{2,3}$"
print("1. Email")
while not validation(pattern, expression):
    expression = input("Enter your email number to verify: ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Number {expression} is valid.")

expression = ""
pattern = r"^([A-Z][a-z]{2,19}\s){2}[A-Z][a-z]{2,20}$"
print("4. Last name, first name and patronymic of the client (3 words, minimum 2 char, maximum 20 char).")
while not validation(pattern, expression):
    expression = input("Enter last name, first name and patronymic of the client to verify: ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Number {expression} is valid.")


expression = ""
pattern = r"^([A-Z][a-z]{2,19}\s){2}[A-Z][a-z]{2,20}$"
print("4. Last name, first name and patronymic of the client (3 words, minimum 2 char, maximum 20 char).")
while not validation(pattern, expression):
    expression = input("Enter last name, first name and patronymic of the client to verify: ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Number {expression} is valid.")


MIN_SIZE_PASSWORD = 8
MAX_SIZE_PASSWORD = 16

expression = ""
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_+]).{8,16}$"
print(f"5. Password (minimum: one capital letter, one small letter, one number, one symbol, password length -"
      f" from {MIN_SIZE_PASSWORD} to {MAX_SIZE_PASSWORD} characters). Example for password: ")
while not validation(pattern, expression):
    expression = input("Enter your home password to verify: ")
    if MIN_SIZE_PASSWORD <= len(expression) <= MAX_SIZE_PASSWORD:
        if not validation(pattern, expression):
            print("Validation Error. Please try again.")
        else:
            print(f"Validation OK. Expression {expression} is valid.")
    else:
        print("Validation Error. Please try again.")


#Игра угадай число от 1 до 100
import random
def guess_number():
    try:
        random_number = random.randint(1, 100)
        is_guessed = False
        while not is_guessed:
            user_num = int(input("Guess the number from 1 to 100. Please enter an integer: "))
            if user_num == random_number:
                print(f"You guessed it! The number = {user_num}")
                is_guessed = True
                return
            if user_num > random_number:
                print("Your number is higher than guess")
            if user_num < random_number:
                print("Your number is less than the number guessed ")
    except ValueError:
        print("Incorrect input! Please enter a valid integer.")
guess_number()