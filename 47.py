import algorithm

def check(num):
    list = []
    for i in range (2,int(num**0.5+1)):
        if num%i == 0:
            if algorithm.prime(i):
                list.append(i)
            if algorithm.prime(int(num/i)):
                list.append(int(num/i))
    if len(list) == 4:
        return True
    return False

i = 2
while True:
    if check(i):
        if check(i+1):
            if check(i+2):
                if check(i+3):
                    print (i)
                    break
    i += 1