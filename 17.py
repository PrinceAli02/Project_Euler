a = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve", 
    13:"thirteen",
    14:"fourteen", 
    15:"fifteen", 
    16:"sixteen",
    17:"seventeen", 
    18:"eighteen", 
    19:"nineteen",
    20:"twenty",
    30:"thirty", 
    40:"forty", 
    50:"fifty", 
    60:"sixty", 
    70:"seventy", 
    80:"eighty", 
    90:"ninety",
    100:"onehundred",
    200:"twohundred",
    300:"threehundred",
    400:"fourhundred",
    500:"fivehundred",
    600:"sixhundred",
    700:"sevenhundred",
    800:"eighthundred",
    900:"ninehundred",
    1000:"onethousand"
}
for x in a:
    a[x] = len(a[x])

def separate(num):
    if num%100 > 10 and num%100 < 20:
        ones = 0
        tens = num%100
    else:
        ones = num%10
        tens = num%100 - ones
    hundreds = num - tens - ones
    return (hundreds,tens,ones)

total = 0
for i in range (1,100):
    h,t,o = separate(i)
    total += a[h] + a[t] + a[o]

for i in range (100,1001):
    h,t,o = separate(i)
    total += a[h] + a[t] + a[o]
    if i%100 != 0:
        total += 3

print (total)