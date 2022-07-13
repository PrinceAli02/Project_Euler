def cancel(n,d):
    n = str(n)
    d = str(d)
    for x in n:
        for y in d:
            if x == y:
                n = n.replace(x,"")
                d = d.replace(y,"")
    if n == "":
        n = 0
    else:
        n = int(n)
    if d == "":
        d = 0
    else:
        d = int(d)
    return n,d

tn = 1
td = 1
for d in range (11,100):
    for n in range (10,d):
        n_,d_ = cancel(n,d) 
        if d_ != 0 and n/d == n_/d_ and n != n_ and n%10 != 0:
            tn *= n
            td *= d
print (tn,td)