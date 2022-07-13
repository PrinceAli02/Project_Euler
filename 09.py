b = 1
while b != -1:
    a = 1
    for a in range (b):
        c = (a**2+b**2)**(1/2)
        if c - int(c) == 0:
            if a + b + c == 1000:
                print (a*b*c)
                break
    b += 1
