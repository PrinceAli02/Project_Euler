import algorithm

N = 0
ab = 0

for a in range (1,1000,2):
    for b in range (1,1001,2):

        # both positive
        n = 0
        while True:
            val = n**2 + a*n + b 
            if algorithm.prime(val):
                n += 1
            else:
                break
        if n > N:
            N = n
            ab = a*b

        # a negative
        n = 0
        while True:
            val = n**2 - a*n + b 
            if val >= 0 and algorithm.prime(val):
                n += 1
            else:
                break
        if n > N:
            N = n
            ab = -a*b

        # b negative
        n = 0
        while True:
            val = n**2 + a*n - b 
            if  val >= 0 and algorithm.prime(val):
                n += 1
            else:
                break
        if n > N:
            N = n
            ab = -a*b

        #both negative
        n = 0
        while True:
            val = n**2 - a*n - b 
            if val >= 0 and algorithm.prime(val):
                n += 1
            else:
                break
        if n > N:
            N = n
            ab = a*b

print (ab,N)