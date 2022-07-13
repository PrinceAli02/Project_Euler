f1 = 0
f2 = 1
index = 1
while index != -1:
    #print (f2,index)
    temp = f2
    f2 += f1
    f1 = temp
    index += 1
    if len(str(f2)) == 1000:
        break
print (index)