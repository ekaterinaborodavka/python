# Task 4.1

nums = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
res_nums = []
zeros = []
for n in nums:
    if n:
        res_nums.append(n)
    else:
        zeros.append(n)

print(res_nums + zeros)

# Task 4.2
numbers = [0, 1, 7, 2, 4, 8]
amount = 0
for n in range(0,len(numbers),2):
    amount += numbers[n]
res = amount*numbers[-1] if len(numbers) else 0
print(res)

# Task 4.3
import random
lists = []
for i in range(random.randint(3,10)):
    lists.append(random.randint(1,10))

results = [lists[0], lists[2], lists[-2]]
print(lists, "----->" ,results)