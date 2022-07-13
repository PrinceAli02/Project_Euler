from math import factorial

count = 0
for n in range (1,101):
    for r in range (1,n+1):
        combination = factorial(n)/(factorial(r)*factorial(n-r))
        if combination > 1000000:
            count += 1
print (count)