def prime(val):
    for i in range (2,int(val**(1/2))+1):
        if val%i == 0:
            return False
    return True

def trunc_LtoR(val):
    val = str(val)
    while len(val) > 1:
        val = val[1:]
        # print (val)
        if not prime(int(val)):
            return False
    return True

def trunc_RtoL(val):
    val = str(val)
    while len(val) > 1:
        val = val[:-1]
        # print (val)
        if not prime(int(val)):
            return False
    return True

count = 0
sum = 0
x = 23
while count < 11:
    if prime(x) and str(x)[0] != '1' and str(x)[-1] != '1':
        if trunc_LtoR(x):
            if trunc_RtoL(x):
                count += 1
                sum += x
                # print (sum,count,x)
    x += 2

print (sum)