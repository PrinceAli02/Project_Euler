#n = prime + 2x^2

def prime(val):
    for i in range (2,int(val**(1/2))+1):
        if val%i == 0:
            return False
    return True

def check(val):
    i = 3
    while i<val:
        num = val
        if prime(i):
            num -= i
            n = (num/2)**0.5
            if n == int(n):
                return True
        i += 1
    return False

num = 1
while num != 0:
    if not prime(num):
        if not check(num):
            print (num)
            break
    num += 2