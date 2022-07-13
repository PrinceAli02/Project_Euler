import algorithm
from itertools import permutations

def primegen(val):
    list = []
    for i in range (1000,val):
        if algorithm.prime(i):
            list.append(i)
    return list

def check(a,b,c):
    a = sorted(str(a))
    b = sorted(str(b))
    c = sorted(str(c))
    if a == b and b == c:
        return True
    return False

pnum = primegen(10000)

for i in range(len(pnum)):
    for j in range (i+1,len(pnum)):
        difference = pnum[j] - pnum[i]
        for h in range (i+2,len(pnum)):
            if (pnum[h] - pnum[j]) == difference:
                a = check(pnum[i],pnum[j],pnum[h])
                if a:
                    print (pnum[i],pnum[j],pnum[h],difference)

#answer = 296962999629 (pnum[i],pnum[j],pnum[h],difference : 2969 6299 9629 3330)