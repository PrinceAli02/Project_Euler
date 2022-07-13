total = 0
for c in range(1000):
    if c % 3 == 0 or c % 5 == 0:
        total += c
print(total)
