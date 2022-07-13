from math import factorial

num = factorial(100)

num = str(num)

total = 0
for i in range (len(num)):
    total += int(num[i])

print (total)