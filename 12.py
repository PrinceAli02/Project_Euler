def factor(val):
    count = 0
    for i in range (1,int(val**0.5)+1):
        if val % i == 0:
            count += 2
    return count

c = 0
num = 0
while num != -1:
    c += 1
    num += c
    count = factor(num)
    if count >= 500:
        break

print (num,count)