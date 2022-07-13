import algorithm

def step(num,prime):
    list = []
    val = ['0','1','2','3','4','5','6','7','8','9']
    num = str(num)
    for x in num:
        val.remove(x)
    for x in val:
        s = int(num[-2]+num[-1]+x)
        if s%prime == 0:
            list.append (int(num+x))
    return list

num = []
for i in range (100,1000):
    p = [str(i)[0],str(i)[1],str(i)[2]]
    q = algorithm.remove_duplicate(p)
    j = ""
    for x in q:
        j += x
    if str(i) in j:
        num.append(i)

prime = algorithm.primegen2(7)
for i in range (7):
    nextlist = []
    for j in range (len(num)):
        x = step(num[j],prime[i])
        nextlist.extend(x)
    num = nextlist

answer = 0
for x in num:
    answer += x

print (answer)