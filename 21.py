def d(val):
    total = 0
    for i in range (1,int(val**0.5)+1):
        if val % i == 0:
            total += i + int(val/i)
    total -= val
    return total

check = [True]*10000

count = 0
for i in range(10000):
    if check[i]:
        check[i] = False
        a = d(i)
        b = d(a)
        if i == b and a != b:
            print (a,b)
            count += a + b
            print (count)
            print ()
            check[a] = False