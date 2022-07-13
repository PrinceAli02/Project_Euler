limit = 1000000

a = [True]*limit

def prime(val):
    for i in range (2,int(val**(1/2))+1):
        if val%i == 0:
            return False
    return True

def mutiples(val):
    for i in range (val,len(a),val):
        a[i] = False

for i in range (1,limit):
    if a[i]:
        b = prime(i)
        if b == False:
            mutiples(i)

primeNum = []
for i in range (2,limit):
    if a[i]:
        primeNum.append(i)

max = 0
maxlength = 0
for h in range (len(primeNum)):
    num = 0
    count = 0
    for i in range(h,len(primeNum)):
        if num < limit:
            num += primeNum[i]
            count += 1
            if prime(num) and count>maxlength:
                maxlength = count
                max = num
                #print (max,maxlength)             
        else:
            break

print (max,maxlength)