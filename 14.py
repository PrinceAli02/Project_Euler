import timeit

start = timeit.timeit()

def sequence(num):
    count = 1
    while num != 1:
        if num%2 == 0:
            num = int(num/2)
        else:
            num = 3*num+1
        count += 1
    return count


max = 0
for c in range(2,1000000):
    count = sequence(c)
    if count > max:
        max = count
        number = c

print (number)

end = timeit.timeit()
print(end - start)