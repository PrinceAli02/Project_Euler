def prime(val): #checks if number is prime or not
    for i in range (2,int(val**(1/2))+1):
        if val%i == 0:
            return False
    return True

def fibonacci(val): #returns fibonacci number correspondant to index
    num = 0
    n1 = 0
    n2 = 1
    if val == 2:
        return n2

    while val > 2 :
        num = n1 + n2
        n1 = n2
        n2 = num
        val -= 1
    return num

def primegen(val): #returns prime numbers less than input
    list = []
    for i in range (2,val):
        if prime(i):
            list.append(i)
    return list

def primegen2(val): #returns val number of prime numbers
    list = []
    i = 2
    while val > 0:
        if prime(i):
            list.append(i)
            val -= 1
        i += 1
    return list


def armstrong(val): #checks if number is an armstrong number
    val = str(val)
    for i in range (len(val)):
        if not val[i] == val[-(i+1)]:
            return False
    return True

def triangle(val): #returns nth triangle number
    num = val*(val+1)/2
    return num

def tri_check(val):  #checks if number is a triangle number
    n = (2*val+(1/4))**(1/2)-(1/2)
    if n == int(n):
        return True
    return False

def pentagonal(val): #returns nth pentagonal number
    num = val * (3*val-1)/2
    return num

def penta_check(val): #checks if number is a pentagonal number
    num = ((24*val+1)**(0.5)+1)/6
    if num == int(num):
        return True
    return False

def hexagonal(val): #returns nth hexagonal number
    num = val*(2*val-1)
    return num

def hexa_check(val): #checks if number is a hexagonal number
    num = ((val+1/8)/2)**(0.5)+1/4
    if num == int(num):
        return True
    return False

def binary(val): #converts decimal value to binary (string)
    bin = []
    while val >= 1:
        if val%2 == 1:
            bin.append("1")
            val -= 1
        else:
            bin.append("0")
        val = val/2
    bin.reverse()
    x = ""
    for y in bin:
        x += y
    return x

def palindrome(val): #checks if value is palindrome
    val = str(val)
    list = []
    for x in val:
        list.append(x)
    for i in range (len(list)):
        if not list[i] == list[-(i+1)]:
            return False
    return True

def pandigital(val): #checks if number is pandigital number
    val = sorted(str(val))
    for i in range (len(val)):
        if not int(val[i]) == i+1:
            return False
    return True

def remove_duplicate(val): #removes duplicate from the list
    list = []
    for i in range(len(val)):
        dup = False
        for x in list:
            if x == val[i]:
                dup = True
        if not dup:
            list.append(val[i])
    return list
