def factors(val):
    total = 0
    for i in range (1,int(val**0.5)+1):
        if val % i == 0:
            total += i
            if i != int(val/i):
                total += int(val/i)
    total -= val
    return total

abundant = []
for i in range (28123):
    sum = factors(i)
    if sum > i:
        abundant.append(i)
num = [False]*28123
for i in range (len(abundant)):
    for j in range (i,len(abundant)):
        a = abundant[i] + abundant[j]
        if a < 28123:
            num[a] = True

sum = 0
for i in range (28123):
    if num[i] == False:
        sum += i
print (sum)