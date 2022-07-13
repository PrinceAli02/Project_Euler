from itertools import permutations

def prime(val):
    for i in range (2,int(val**(1/2))+1):
        if val%i == 0:
            return False
    return True

number = ["9","8","7","6","5","4","3","2","1"]
for i in range (len(number)):
    perm = permutations(number) 
    for j in perm:
        num = ""
        for x in j:
            num += x
        check = prime(int(num))
        if check:
            print (num)
            break
    if check:
        break
    number.remove(number[0])
