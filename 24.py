from math import factorial

# there are 725760 arrangements starting from 0 and 1
# there are 1088640 arrangements starting from 0 ~ 2
count = 725760
num = [0,1,3,4,5,6,7,8,9]
#725760th number = 1987654320
#2013456789, 2013456798, 2013456879, 2013456897, 2013456978, 2013456987
#will start with 2

from itertools import permutations 

perm = permutations(num)

for i in list(perm): 
    count += 1
    if count == 1000000:
        print (i)
        break

#answer = 2 + output = 2783915460