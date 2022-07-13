from math import factorial

count = 3
sum = 0
while count > 0:
    num = str(count)
    s = 0
    for x in num:
        s += factorial(int(x))
    if s == count:
        sum += count
        print (count,sum)
    count += 1