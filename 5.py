def check(val):
    for i in range (2,21):
        if val%i != 0:
            return False
    return True

num = 2520
while num != -1:
    if check(num):
        break
    num += 2520
print (num)