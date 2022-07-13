maxr = 0
maxd = 0
for d in range (1,1000):
    n = 1
    r = []
    while True:
        n = (n*10)%d
        if n in r:
            if len(r)>maxr:
                maxr, maxd = len(r),d
            break
        else:
            r.append (n)

print (maxd)