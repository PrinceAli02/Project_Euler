list = []
for i in range (2,101):
    for j in range (2,101):
        list.append (i**j)

list = sorted(list)
count = len(list)

for i in range (len(list)-1):
    if list[i] == list[i+1]:
            count -= 1

print (count)