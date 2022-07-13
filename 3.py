def prime(val):
    for i in range (2,int(val**0.5)+1):
        if val % i == 0:
            return False
    return True

for c in range (2,600851475143):
     if  600851475143 % c == 0:
         if prime(c):
            print (c)