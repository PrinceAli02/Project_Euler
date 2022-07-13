t1 = 1
t2 = 1
total = 0
while t2 < 4000000:
    temp = t2
    t2 += t1
    t1 = temp
    if t2%2 == 0:
        total += t2
print (total)
    
    
