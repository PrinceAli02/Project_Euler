import algorithm

i = 1
max = 0
while i <= 10000:
    multiplier = 1
    concate = ''
    while len(concate) < 9:
        concate += str(i*multiplier)
        multiplier += 1
    if len(concate) == 9:
        check = algorithm.pandigital(concate)
        if check and int(concate) > max:
            max = int(concate)
    i += 1 

print (max)