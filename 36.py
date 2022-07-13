def binary(val):
    bin = []
    while val >= 1:
        if val%2 == 1:
            bin.append("1")
            val -= 1
        else:
            bin.append("0")
        val = val/2
    bin.reverse()
    x = ""
    for y in bin:
        x += y
    return x

def palindrome(val):
    val = str(val)
    list = []
    for x in val:
        list.append(x)
    for i in range (len(list)):
        if not list[i] == list[-(i+1)]:
            return False
    return True

sum = 0
for i in range (1,1000000):
    if palindrome(i):
        if palindrome(binary(i)):
            sum += i
            print (i,sum)
print (sum)