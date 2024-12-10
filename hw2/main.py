# Task 2.1
# variant 1
number = int(input("Enter four-digit number: "))
number1 = number // 1000
number2 = number % 1000 // 100
number3 = number % 1000 % 100 // 10
number4 = number % 10

# variant 2
# number1, residue = divmod(number, 1000)
# number2, residue2 = divmod(residue, 100)
# number3, number4 = divmod(residue2, 10)

print(number1, number2, number3, number4, sep="\n")
print(f"{number1}\n{number2}\n{number3}\n{number4}")
print("amount", amount := number1 + number2 + number3 + number4)

# Task 2.2
num = int(input('Enter a five-digit number: '))  # 56198

# variant 1
num1 = num // 10000
num2 = num % 10000 // 1000
num3 = num % 10000 % 1000 // 100
num4 = num % 10000 % 1000 % 100 // 10
num5 = num % 10

# variant 2
# num1, res = divmod(num, 10000)
# num2, res2 = divmod(res, 1000)
# num3, res3 = divmod(res2, 100)
# num4, num5 = divmod(res3, 10)

result = num5 * 10000 + num4 * 1000 + num3 * 100 + num2 * 10 + num1
print(result)
print(f"{num5}{num4}{num3}{num2}{num1}")