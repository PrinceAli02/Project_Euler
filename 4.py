max = 0
for c1 in range (100,1000):
    for c2 in range (100,1000):
        s = c1 * c2
        temp=s
        rev=0
        while s>0:
            dig=s%10
            rev=rev*10+dig
            s=s//10 
        if temp==rev and temp > max:
            max = temp
print (max)