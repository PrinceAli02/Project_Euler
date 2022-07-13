#a^2 + b^2 = c^2
#a+b+c = p
#a+b+(a^2+b^2)^0.5 = p 

list = [0]*1001
for a in range (1,1001):
    for b in range (a,1001):
        p = a+b+(a**2+b**2)**0.5
        #print (a,b,p)
        if p == int(p) and p <= 1000:
            list[int(p)] += 1

max = 0
P = 0
for i in range (len(list)):
    if list[i] > max:
        max = list[i]
        P = i

print (P)