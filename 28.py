sum = 1
num = 1
i = 2
for x in range (500):
    for y in range (4):
        num += i
        sum += num
    i += 2
print (sum)