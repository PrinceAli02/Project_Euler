def fpower(val):
    val = str(val)
    num = 0
    for x in val:
        num += int(x)**5
    if num == int(val):
        return True
    return False

sum = 0
for i in range (2,1000000):
    stat = fpower(i)
    if stat:
        sum += i
print (sum)