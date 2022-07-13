num = 1

def function(i,num,digits):
    temp = num
    temp_digits = digits
    while i < 6 and temp_digits == digits:
        temp = num*(i+1)
        temp_digits = split(str(temp))
        temp_digits.sort()
        i += 1
    else:
        if i < 6:
            return False
    print (num)
    return True
    
def split(word):
    return [char for char in word] 

a = False
while True:
    if len(str(num)) == len(str(num*6)):
        digits = split(str(num))
        digits.sort()
        a = function(1,num,digits)
    if a:
        break
    num += 1
