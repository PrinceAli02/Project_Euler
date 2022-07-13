def prime(val):
    for i in range (2,int(val**(1/2))+1):
        if val%i == 0:
            return False
    return True

count = 0
for i in range (2,1000000):
    if prime(i):
        temp = []
        condition = True
        for j in range(len(str(i))):
            x = str(i)
            temp.append(x[j])
        for k in range(len(temp)-1):
            temp.remove(temp[0])
            temp.append(x[k])
            num = ''
            for l in range(len(temp)):
                num += temp[l]
            if not prime(int(num)):
                condition = False
                break
        if condition == True:
            count += 1
print (count)