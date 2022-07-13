from math import fabs

def penta(val):
    num = val * (3*val-1)/2
    return num

def penta_check(val):
    num = ((24*val+1)**(0.5)+1)/6
    if num == int(num):
        return True
    return False

numbers = []
count = 0
while count != -1:
    numbers.append(penta(count))
    count += 1
    if len(numbers) >= 2:
        num = penta(count)
        for i in range (1,len(numbers)):
            sum = num + numbers[i]
            if penta_check(sum):
                difference = fabs(num - numbers[i])
                if penta_check(difference):
                    print (difference)
                    count = -1
                    break