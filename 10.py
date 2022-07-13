def _10(n):
    a = [True]*n
    sum = 0
    for i in range (2,n):
        if a[i]:
            sum += i
        for l in range(i,n,i):
            a[l] = False
    return sum

print (_10(2000000))