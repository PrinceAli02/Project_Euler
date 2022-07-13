def tri(val):
    num = val*(val+1)/2
    return num

def penta_check(val):
    num = ((24*val+1)**(0.5)+1)/6
    if num == int(num):
        return True
    return False

def hexa_check(val):
    num = ((val+1/8)/2)**(0.5)+1/4
    if num == int(num):
        return True
    return False


val = 286
while val != 1:
    i = tri(val)
    if hexa_check(i):
        if penta_check(i):
            print (i)
            break
    val += 1
