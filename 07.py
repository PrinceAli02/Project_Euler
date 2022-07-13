def prime(val):
    for i in range (2,int(val**0.5)+1):
        if val % i == 0:
            return False
    return True

count = 0
c = 2
while c != -1:
    if prime(c):
        count += 1
    if count == 10001:
        break
    c += 1
print (c)
