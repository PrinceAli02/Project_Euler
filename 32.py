import algorithm

multiplicand = 1
product = 0
list = []

while True:
    multiplicand += 1
    for multiplier in range(multiplicand):
        product = multiplicand*multiplier
        val = str(multiplicand)+str(multiplier)+str(product)
        if algorithm.pandigital(val) and len(val) == 9:
            list.append(product)
    if multiplicand == 2000:
        break

list = algorithm.remove_duplicate(list)
sum = 0
for x in list:
    sum += x
print (sum)