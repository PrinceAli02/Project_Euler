def num1():
    total = 0
    for i in range (100):
        total += (i+1)
    total = total ** 2
    return total

def num2():
    total = 0
    for i in range (100):
        total += (i+1)**2
    return total

a = num1()
b = num2()

print (a-b)